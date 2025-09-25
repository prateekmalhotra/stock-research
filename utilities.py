# Proposed functions:

# - Write to sheet
# - Call LLM
# - Website contexts

import os
import sys
import json
import gspread
from datetime import datetime, timedelta, UTC, date
from google import genai
from google.genai import types
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from dotenv import load_dotenv

import re
import requests
import praw
import praw.models
from bs4 import BeautifulSoup
from pydantic import BaseModel
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from urllib.parse import urljoin, urlparse, parse_qs

import numpy as np
import yfinance as yf
from scipy.stats import linregress
from gspread.utils import column_letter_to_index
from google.genai.types import Tool, GenerateContentConfig

from requests.exceptions import RequestException, ReadTimeout

load_dotenv()
console = Console()
client = genai.Client()

TICKER_RE = re.compile(r'^[A-Z0-9\.\-]{1,6}$')
DOT_PATTERN = re.compile(r'([A-Z0-9\.\-]{1,6})\s*(?:·|•|-)\s+')
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

def call_llm(prompt, context, response_schema, output_format):
    full_prompt = (
        f"{prompt}\n\n"
        f"--- CONTEXT ---\n{context}\n\n"
        f"--- OUTPUT INSTRUCTIONS ---\n{output_format}\n\n"
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash-lite',
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_schema,
            ),
        )
        return response.text
    except Exception as e:
        console.print(f"[bold red]Gemini API call failed in utilities:[/bold red] {e}", style="red")
        return '{"tickers": []}'


def fetch(url="http://openinsider.com/latest-cluster-buys", timeout=15):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; OpenInsiderScraper/1.0)"}
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()
    return r.text

def extract_from_href(href):
    if not href:
        return None
    p = urlparse(href)
    qs = parse_qs(p.query)
    for key in ("symbol", "s", "q"):
        if key in qs:
            val = qs[key][0].upper()
            if TICKER_RE.match(val):
                return val
    m = re.search(r'/([A-Z0-9\.\-]{1,6})(?:$|/|\?)', p.path, re.I)
    if m:
        return m.group(1).upper()
    return None

def get_openinsider_tickers():
    console.rule("[bold cyan]Starting OpenInsider Ticker Extraction[/bold cyan]")
    
    html = fetch(url="http://openinsider.com/latest-cluster-buys", timeout=15)
    soup = BeautifulSoup(html, "html.parser")
    ticker_data_map: Dict[str, Dict[str, str]] = {}
    
    tables = soup.find_all("table")
    rows = []
    
    console.print(f"[magenta]Found {len(tables)} potential HTML tables.[/magenta]")
    
    table_found = False
    for i, tbl in enumerate(tables):
        thead = tbl.find("thead")
        if thead and any("ticker" in th.get_text().lower() or "issuer" in th.get_text().lower() for th in thead.find_all("th")):
            rows = tbl.find_all("tr")
            console.print(f"[green]Found primary table at index {i} based on header text.[/green]")
            table_found = True
            break
            
    if not table_found:
        console.print("[yellow]Primary table not found. Checking first 3 tables...[/yellow]")
        for i, tbl in enumerate(tables[:3]):
            rows = tbl.find_all("tr")
            if rows:
                console.print(f"[green]Fallback: Using table at index {i} with {len(rows)} rows.[/green]")
                break
            
    if not rows:
        console.print("[bold red]ERROR: No table rows found for parsing.[/bold red]")
        console.rule("[bold cyan]OpenInsider Extraction Complete[/bold cyan]", style="red")
        return []

    console.print(f"[cyan]Processing {len(rows)} table rows for tickers...[/cyan]")
    
    for tr in rows:
        t = None
        for a in tr.find_all("a", href=True):
            txt = a.get_text(strip=True)
            
            if TICKER_RE.match(txt):
                t = txt.upper()
                break
            
            if "·" in txt or "•" in txt:
                m = DOT_PATTERN.search(txt)
                if m:
                    t = m.group(1).upper()
                    break
                    
            href_t = extract_from_href(a["href"])
            if href_t:
                t = href_t
                break
                
        if not t:
            row_text = " ".join(tr.stripped_strings)
            m = DOT_PATTERN.search(row_text)
            if m:
                t = m.group(1).upper()
                
        if t and t not in ticker_data_map:
            ticker_data_map[t] = {
                "ticker": t,
                "source": "openinsider",
                "url": f"https://openinsider.com/{t}"
            }
            
    final_list = sorted(list(ticker_data_map.values()), key=lambda x: x['ticker'])
    
    console.rule("[bold cyan]OpenInsider Extraction Complete[/bold cyan]", style="green")
    console.print(f"[bold green]FINAL COUNT:[/bold green] Extracted [yellow bold]{len(final_list)}[/yellow bold] unique tickers from OpenInsider.", style="green")

    return final_list


def parse_dataroma_fund_links(html):
    soup = BeautifulSoup(html, "html.parser")
    fund_links = {}
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "holdings.php?m=" in href:
            code = parse_qs(urlparse(href).query).get("m", [None])[0]
            if code:
                url = urljoin("https://www.dataroma.com/m/", href)
                link_text = a.get_text(strip=True)
                
                name = link_text.replace(f"({code})", "").strip()
                name = re.sub(r"Updated \d{1,2} \w{3} \d{4}", "", name).strip()
                name = re.sub(r"^[A-Za-z\s\.]+ - ", "", name).strip()

                fund_links[code] = {'name': name, 'url': url}
    return fund_links


def parse_dataroma_holdings(html):
    soup = BeautifulSoup(html, "html.parser")
    holdings = []
    
    table = soup.find("table", id="grid")
    
    if not table:
        return holdings

    base_url = "https://www.dataroma.com/m/"
    for a in table.find_all("a", href=re.compile(r"/m/stock\.php\?sym=")):
        href = a.get("href")
        
        try:
            ticker = href.split("sym=")[1].split("&")[0]
            stock_url = urljoin(base_url, href)
            
            if ticker:
                holdings.append({
                    'ticker': ticker.upper(),
                    'url': stock_url
                })
        except IndexError:
            continue
            
    return holdings


def get_dataroma_tickers():
    console.log("[bold green]Fetching DataRoma home page[/bold green]")
    html = fetch(url="https://www.dataroma.com/m/home.php", timeout=15)
    console.log("[bold green]Parsing fund links[/bold green]")
    
    funds = parse_dataroma_fund_links(html)
    console.log(f"[bold blue]Found {len(funds)} funds[/bold blue]")

    all_tickers_data = []
    
    max_key_len = 0
    if funds:
        max_key_len = max(len(f"{data['name']} ({code})") for code, data in funds.items())

    with Progress(console=console) as progress:
        task_id = progress.add_task("Processing Funds...", total=len(funds))

        for fund_code, fund_data in funds.items():
            code = fund_code
            name = fund_data['name']
            url = fund_data['url']
            
            display_name = f"{name} ({code})"
            
            progress.update(task_id, description=f"Processing [bold yellow]{display_name}[/bold yellow]...")

            try:
                html = fetch(url)
            except Exception as e:
                padded_name = display_name.ljust(max_key_len)
                progress.print(f"[yellow]{padded_name}[/yellow]: [red]Failed to fetch -> {e}[/red]")
                progress.advance(task_id)
                continue
                
            holdings = parse_dataroma_holdings(html)
            
            for item in holdings:
                item['source'] = display_name
                all_tickers_data.append(item)
            
            padded_name = display_name.ljust(max_key_len)
            progress.print(f"[yellow]{padded_name}[/yellow]: {len(holdings)} tickers")
            
            progress.advance(task_id)
        
        progress.update(task_id, description="[bold green]All funds processed[/bold green] ✔")

    unique_tickers_map = {}
    for item in all_tickers_data:
        ticker = item.get('ticker')
        if ticker and ticker not in unique_tickers_map:
            unique_tickers_map[ticker] = {
                'ticker': ticker,
                'source': item.get('source'),
                'url': item.get('url')
            }

    unique_tickers_list = list(unique_tickers_map.values())
    
    console.rule("[bold magenta]Ticker Extraction Complete[/bold magenta]", style="green")
    console.print(f"[bold green]FINAL COUNT:[/bold green] Extracted and merged [yellow bold]{len(unique_tickers_list)}[/yellow bold] unique tickers.", style="green")
    
    return unique_tickers_list

def get_reddit_context(time_period_hours, subreddit_name, flair_text=None):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    time_ago = datetime.now(UTC) - timedelta(hours=time_period_hours)
    timestamp_ago = int(time_ago.timestamp())
    subreddit = reddit.subreddit(subreddit_name)

    post_data_list = []
    should_filter_by_flair = bool(flair_text)

    for post in subreddit.new(limit=1000):
        if post.created_utc >= timestamp_ago:
            if not should_filter_by_flair or (post.link_flair_text == flair_text):
                post.comment_sort = 'top'
                post.comments.replace_more(limit=0)
                
                comments_data = []
                for comment in list(post.comments)[:5]:
                    if isinstance(comment, praw.models.Comment):
                        comments_data.append({
                            "author": str(comment.author),
                            "posted_at_utc": datetime.fromtimestamp(comment.created_utc, UTC).isoformat(),
                            "upvotes": comment.score,
                            "content": comment.body
                        })
                
                post_content = post.selftext if post.selftext else ""
                post_data_list.append({
                    "title": post.title,
                    "author": str(post.author),
                    "posted_at_utc": datetime.fromtimestamp(post.created_utc, UTC).isoformat(),
                    "url": post.url,
                    "upvotes": post.score,
                    "content": post_content,
                    "comments_count": post.num_comments,
                    "comments": comments_data
                })

    context_dump_markdown = ""
    for p in post_data_list:
        content_for_markdown = p['content'].replace('\n', '\n> ')[:2000]

        markdown_block = (
            f"### Post Title: {p['title']}\n"
            f"* **Author:** {p['author']}\n"
            f"* **Posted (UTC):** {p['posted_at_utc']}\n"
            f"* **Stats:** {p['upvotes']} Upvotes, {p['comments_count']} Comments\n"
            f"* **URL:** {p['url']}\n\n"
            f"**Content:**\n"
            f"> {content_for_markdown}...\n"
        )

        if p['comments']:
            markdown_block += "\n**Top Comments:**\n"
            for c in p['comments']:
                comment_content = c['content'].replace('\n', '\n> > ')[:500]
                markdown_block += (
                    f"\n> **{c['author']}** ({c['upvotes']} upvotes):\n"
                    f"> > {comment_content}...\n"
                )

        markdown_block += f"\n---\n\n"
        context_dump_markdown += markdown_block

    return context_dump_markdown

def get_reddit_tickers():
    console.rule("[bold magenta]Starting Ticker Extraction[/bold magenta]")

    SUBREDDIT_CONFIGS = [
        ('valueinvesting', None),
        ('wallstreetbets', 'DD'),
        ('investing', None),
        ('StockMarket', None),
        ('SecurityAnalysis', None),
        ('pennystocks', None),
        ('AsymmetricAlpha', None),
        ('Shortsqueeze', 'DD')
    ]

    ticker_schema = types.Schema(
        type=types.Type.OBJECT,
        properties={
            "results": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "ticker": types.Schema(type=types.Type.STRING),
                        "source": types.Schema(type=types.Type.STRING),
                        "url": types.Schema(type=types.Type.STRING)
                    },
                    required=["ticker", "source", "url"]
                )
            )
        },
        required=["results"]
    )

    prompt = "Below are a few reddit posts. From only these ideas, extract and give me all the stock tickers (only individual companies, no ETFs). For each ticker, you MUST also provide the 'source' (the subreddit name, e.g., r/wallstreetbets) and the 'url' (the exact post link). Use the output format provided."
    output_format = 'Output should be in json format with a single field named "results", where the value is a list of objects. Each object must have fields "ticker" (string), "source" (string, e.g., r/valueinvesting), and "url" (string, the post URL). Example: {"results": [{"ticker": "TSLA", "source": "r/wallstreetbets", "url": "https://reddit.com/r/wallstreetbets/comments/abcde"}, ...]}.'

    json_results = []
    
    for subreddit_name, flair_text in SUBREDDIT_CONFIGS:
        console.print(f"[yellow]Fetching Reddit context from r/{subreddit_name} (Flair: {flair_text})...[/yellow]")
        
        context = get_reddit_context(
            time_period_hours=24,
            subreddit_name=subreddit_name,
            flair_text=flair_text
        )
        
        console.print(f"[green]...Fetched context for r/{subreddit_name} ({len(context)} chars).[/green]")
        
        console.print(f"[cyan]Sending r/{subreddit_name} context to LLM for ticker extraction...[/cyan]")
        
        json_output = call_llm(prompt, context, ticker_schema, output_format)
        json_results.append((subreddit_name, json_output))

    all_tickers_data = []
    
    console.print("[yellow]Attempting to parse all LLM JSON responses...[/yellow]")
    
    for subreddit_name, json_string in json_results:
        try:
            dict_data = json.loads(json_string)
            results = dict_data.get('results', []) 
            
            tickers = [item.get('ticker') for item in results if isinstance(item, dict) and item.get('ticker')] 
            
            all_tickers_data.extend(results)
            console.print(f"[green]Parsed r/{subreddit_name} Results: [bold]{len(tickers)}[/bold][/green]")
            
        except json.JSONDecodeError as e:
            console.rule(f"[bold red]JSON DECODE ERROR for r/{subreddit_name}[/bold red]", style="red")
            console.print(f"[bold red]ERROR:[/bold red] LLM returned invalid JSON for {subreddit_name}.", style="red")
            console.print(f"[bold yellow]Exception:[/bold yellow] {e}", style="yellow")
            rprint(f"  [blue]JSON Source (start):[/blue] {json_string[:200]}...")

    unique_tickers_map = {}
    for item in all_tickers_data:
        ticker = item.get('ticker')
        if ticker and ticker not in unique_tickers_map:
            unique_tickers_map[ticker] = {
                'ticker': ticker,
                'source': item.get('source', 'Unknown'), 
                'url': item.get('url', 'Unknown URL')   
            }

    unique_tickers_list = list(unique_tickers_map.values())
    
    console.rule("[bold magenta]Ticker Extraction Complete[/bold magenta]", style="green")
    console.print(f"[bold green]FINAL COUNT:[/bold green] Extracted and merged [yellow bold]{len(unique_tickers_list)}[/yellow bold] unique tickers.", style="green")
    
    return unique_tickers_list


def prepare_data_for_sheet(merged_tickers):
    console.log("Preparing data for Google Sheets...")
    header = ['Ticker', 'Sources', 'URLs']
    data_for_sheet = [header]
    
    for ticker_data in merged_tickers.values():
        sources_str = ", ".join(sorted(list(set(ticker_data['sources']))))
        urls_str = ", ".join(sorted(list(set(ticker_data['urls']))))
        
        row = [
            ticker_data['ticker'],
            sources_str,
            urls_str
        ]
        data_for_sheet.append(row)
        
    return data_for_sheet


def merge_ticker_data(all_tickers_lists):
    console.log("Merging ticker data...")
    merged_tickers = {}
    
    for item in all_tickers_lists:
        ticker = item.get('ticker')
        if not ticker:
            continue 

        source = item.get('source', 'Unknown')
        url = item.get('url', 'Unknown URL')
        
        if ticker not in merged_tickers:
            merged_tickers[ticker] = {
                'ticker': ticker,
                'sources': [source],
                'urls': [url]
            }
        else:
            merged_tickers[ticker]['sources'].append(source)
            merged_tickers[ticker]['urls'].append(url)
            
    console.log(f"Merged data into {len(merged_tickers)} unique tickers.")
    return merged_tickers

def authenticate_google_sheets():
    """Handles user authentication for Google Sheets and returns credentials."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def authenticate_google_sheets_sa():
    """Authenticates using a Service Account from GitHub Secrets."""
    console.log("Authenticating using Service Account (GitHub Actions)...")
    try:
        gcp_sa_key_content = os.getenv("GCP_SA_KEY")
        if not gcp_sa_key_content:
            raise ValueError("GCP_SA_KEY secret is not set in GitHub repository.")
            
        # The secret is stored as a string, so we must load it as JSON
        gcp_sa_dict = json.loads(gcp_sa_key_content)
        
        # Use gspread's built-in function to authenticate from a dictionary
        client = gspread.service_account_from_dict(gcp_sa_dict, scopes=SCOPES)
        return client
    except Exception as e:
        console.log(f"[bold red]Service Account authentication failed:[/bold red] {e}")
        return None


def write_to_google_sheet(data_to_write, sheet_name, worksheet_name="Sheet1"):
    client = None
    if os.getenv("GITHUB_ACTIONS") == "true":
        client = authenticate_google_sheets_sa()
    else:
        creds = authenticate_google_sheets_oauth()
        if creds:
            client = gspread.authorize(creds)

    if not client:
        console.log("[bold red]Authentication failed. Cannot get gspread client.[/bold red]")
        return

    console.log(f"Attempting to write to Google Sheet: '{sheet_name}', Worksheet: '{worksheet_name}'...")
    try:
        try:
            spreadsheet = client.open(sheet_name)
        except gspread.exceptions.SpreadsheetNotFound:
            console.log(f"Spreadsheet '{sheet_name}' not found. Creating a new one...")
            spreadsheet = client.create(sheet_name)
            try:
                if not os.getenv("GITHUB_ACTIONS") == "true":
                    pass
            except Exception as e:
                console.log(f"[bold yellow]Could not auto-share new sheet:[/bold yellow] {e}")

        try:
            sheet = spreadsheet.worksheet(worksheet_name)
            console.log(f"Found existing worksheet '{worksheet_name}'.")
        except gspread.exceptions.WorksheetNotFound:
            console.log(f"Worksheet '{worksheet_name}' not found. Creating a new one...")
            sheet = spreadsheet.add_worksheet(title=worksheet_name, rows="1000", cols="20")

        existing_tickers = set(sheet.col_values(1))
        console.log(f"Found {len(existing_tickers)} existing tickers in '{worksheet_name}'.")

        header_row = data_to_write[0]
        data_rows = data_to_write[1:]
        rows_to_append = []

        if not existing_tickers or "Ticker" not in existing_tickers:
            rows_to_append.append(header_row)

        new_tickers_added_count = 0
        for row in data_rows:
            ticker = row[0]
            if ticker not in existing_tickers:
                rows_to_append.append(row)
                new_tickers_added_count += 1

        if rows_to_append:
            sheet.append_rows(rows_to_append, value_input_option='USER_ENTERED')
            if new_tickers_added_count > 0:
                console.log(f"[bold green]Successfully added {new_tickers_added_count} new tickers to '{worksheet_name}'.[/bold green]")
            else:
                console.log(f"[bold green]Successfully initialized worksheet '{worksheet_name}' with header.[/bold green]")
        else:
            console.log(f"[bold yellow]No new tickers found. Worksheet '{worksheet_name}' is already up-to-date.[/bold yellow]")

    except Exception as e:
        console.log(f"[bold red]An unexpected error occurred while writing to the sheet:[/bold red] {e}")


def get_all_13f_holdings(urls):
    all_holdings = []
    
    for url in urls:
        try:
            source_name = url.strip('/').split('/')[-1].replace('_portfolio.php', '').replace('_', ' ').title()
        except Exception:
            source_name = "unknown"

        console.print(Panel(f"[bold cyan]{source_name}[/bold cyan]", title="Scraping Fund", expand=False, border_style="blue"))
        console.log(f"Attempting to scrape: {url}")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        current_url_holdings = []

        try:
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                console.log("[green]Successfully fetched the webpage.[/green]")
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                table_body = soup.find('tbody', id='trans13f')
                
                if table_body:
                    console.log("Found the holdings table ('tbody#trans13f').")
                    
                    for row in table_body.find_all('tr'):
                        first_cell = row.find('td')
                        
                        if first_cell:
                            ticker_link = first_cell.find('a')
                            full_text = None
                            
                            if ticker_link:
                                full_text = ticker_link.get_text(strip=True)
                            else:
                                full_text = first_cell.get_text(strip=True)
                                
                            if full_text:
                                ticker = full_text.split()[0]
                                
                                holding_data = {
                                    "ticker": ticker,
                                    "source": source_name,
                                    "url": url
                                }
                                current_url_holdings.append(holding_data)
                    
                    if current_url_holdings:
                        console.print(f"[bold]Holdings found for this fund:[/bold] [cyan]{len(current_url_holdings)}[/cyan]\n")
                    else:
                        console.log("[yellow]Found the table, but could not extract any holdings.[/yellow]")
                        console.log("[yellow]The page structure might have changed, or the table is empty.[/yellow]\n")

                else:
                    console.print("Error: Could not find the table body with id 'trans13f'.", style="bold red")
                    console.print("The website structure may have changed, or the page didn't load correctly.\n", style="red")

            else:
                console.print(f"Error: Failed to retrieve the webpage. Status code: {response.status_code}\n", style="bold red")

        except requests.exceptions.RequestException as e:
            console.print(f"[bold red]A request error occurred for {url}:[/bold red] {e}\n")
        
        all_holdings.extend(current_url_holdings)

    console.print(Panel(f"[bold]Total holdings found from all sources:[/bold] [green]{len(all_holdings)}[/green]", title="Scraping Complete", expand=False, border_style="green"))
    return all_holdings

def get_more_hedge_funds_tickers():
    hedge_funds = [
        "https://fintel.io/i/wynnefield-capital",
        "https://fintel.io/i/roumell-asset-management-llc",
        "https://fintel.io/i/osmium-partners-llc",
        "https://fintel.io/i/bulldog-investors-llc",
        "https://fintel.io/i/cannell-capital-llc",
        "https://fintel.io/i/chou-associates-management",
        "https://fintel.io/i/greenhaven-associates",
        "https://fintel.io/i/lafayette-investments",
        "https://fintel.io/i/kahn-brothers-group-inc-de-",
        "https://fintel.io/i/gagnon-securities-llc",
        "https://fintel.io/i/teton-advisors"   
    ]

    return get_all_13f_holdings(hedge_funds)


def get_step_i_tickers(sheet_name='stock-research', worksheet_name='step-i'):
    client = None
    if os.getenv("GITHUB_ACTIONS") == "true":
        console.log("Authenticating using Service Account (GHA)...")
        client = authenticate_google_sheets_sa()
    else:
        console.log("Authenticating using OAuth (local)...")
        creds = authenticate_google_sheets_oauth()
        if creds:
            client = gspread.authorize(creds)

    if not client:
        console.log("[bold red]Authentication failed. Cannot get gspread client.[/bold red]")
        return []

    console.log(f"Attempting to read from Google Sheet: '{sheet_name}', Worksheet: '{worksheet_name}'...")
    try:
        spreadsheet = client.open(sheet_name)
        sheet = spreadsheet.worksheet(worksheet_name)
        console.log("Successfully opened sheet and worksheet.")

        header = sheet.row_values(1)
        if not header:
            console.log(f"[bold red]Worksheet '{worksheet_name}' appears to be empty.[/bold red]")
            return []

        if 'Ticker' not in header:
            console.log(f"[bold red]'Ticker' column not found in '{worksheet_name}'.[/bold red]")
            console.log(f"Found headers: {header}")
            return []

        ticker_col_index = header.index('Ticker') + 1
        
        tickers = sheet.col_values(ticker_col_index)
        
        if len(tickers) > 1:
            ticker_list = tickers[1:]
            console.log(f"[bold green]Successfully retrieved {len(ticker_list)} tickers.[/bold green]")
            return ticker_list
        else:
            console.log(f"[bold yellow]Found 'Ticker' column, but it contains no data.[/bold yellow]")
            return []

    except SpreadsheetNotFound:
        console.log(f"[bold red]Spreadsheet '{sheet_name}' not found.[/bold red]")
        return []
    except WorksheetNotFound:
        console.log(f"[bold red]Worksheet '{worksheet_name}' not found in '{sheet_name}'.[/bold red]")
        return []
    except Exception as e:
        console.log(f"[bold red]An unexpected error occurred while reading the sheet:[/bold red] {e}")
        return []

def get_step_ii_tickers(sheet_name='stock-research', worksheet_name='step-ii'):
    client = None
    if os.getenv("GITHUB_ACTIONS") == "true":
        console.log("Authenticating using Service Account (GHA)...")
        client = authenticate_google_sheets_sa()
    else:
        console.log("Authenticating using OAuth (local)...")
        creds = authenticate_google_sheets_oauth()
        if creds:
            client = gspread.authorize(creds)

    if not client:
        console.log("[bold red]Authentication failed. Cannot get gspread client.[/bold red]")
        return []

    console.log(f"Attempting to read from Google Sheet: '{sheet_name}', Worksheet: '{worksheet_name}'...")
    try:
        spreadsheet = client.open(sheet_name)
        sheet = spreadsheet.worksheet(worksheet_name)
        console.log("Successfully opened sheet and worksheet.")

        all_data = sheet.get_all_values()
        if not all_data or len(all_data) < 2:
            console.log(f"[bold yellow]Worksheet '{worksheet_name}' is empty or has no data rows.[/bold yellow]")
            return []

        header = all_data[0]
        if 'Ticker' not in header or 'Last Updated' not in header:
            console.log(f"[bold red]'Ticker' or 'Last Updated' column not found in '{worksheet_name}'.[/bold red]")
            return []

        ticker_col_index = header.index('Ticker')
        last_updated_col_index = header.index('Last Updated')
        three_months_ago = datetime.now() - timedelta(days=90)
        
        recent_tickers = []
        for row in all_data[1:]:
            last_updated_str = row[last_updated_col_index]
            ticker = row[ticker_col_index]
            if not last_updated_str:
                continue
            
            try:
                last_updated_date = datetime.strptime(last_updated_str, "%Y-%m-%d")
                if last_updated_date >= three_months_ago:
                    recent_tickers.append(ticker)
            except (ValueError, TypeError):
                continue

        console.log(f"[bold green]Found {len(recent_tickers)} tickers updated within the last 3 months.[/bold green]")
        return recent_tickers

    except SpreadsheetNotFound:
        console.log(f"[bold red]Spreadsheet '{sheet_name}' not found.[/bold red]")
        return []
    except WorksheetNotFound:
        console.log(f"[bold red]Worksheet '{worksheet_name}' not found in '{sheet_name}'.[/bold red]")
        return []
    except Exception as e:
        console.log(f"[bold red]An unexpected error occurred while reading the sheet:[/bold red] {e}")
        return []


def format_large_number(num):
    """Formats a large number into a human-readable string (e.g., 1.2B, 345.6M)."""
    if num is None or not isinstance(num, (int, float)):
        return "N/A"
    if abs(num) >= 1_000_000_000_000:
        return f"{num / 1_000_000_000_000:.1f}T"
    if abs(num) >= 1_000_000_000:
        return f"{num / 1_000_000_000:.1f}B"
    elif abs(num) >= 1_000_000:
        return f"{num / 1_000_000:.1f}M"
    elif abs(num) >= 1_000:
        return f"{num / 1_000:.1f}K"
    else:
        return str(num)


def get_market_stats(ticker):
    console.log(f"Fetching market stats for [bold cyan]{ticker}[/bold cyan]...")
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        quote_type = info.get("quoteType")
        if quote_type == 'ETF':
            console.log(f"[bold yellow]Skipping ETF:[/bold yellow] Ticker [bold cyan]{ticker}[/bold cyan] is an ETF.")
            return None

        stats_data = {
            "market_cap": info.get("marketCap"),
            "shares_outstanding": info.get("sharesOutstanding"),
            "float_shares": info.get("floatShares")
        }

        if stats_data["market_cap"] is None:
            console.log(f"[bold red]Market data not available for {ticker}[/bold red]")
            return None

        stats_table = Table(show_header=False, box=None, padding=(0, 1))
        stats_table.add_column(style="bold magenta", width=20)
        stats_table.add_column(justify="right")

        # Use the helper function to format the numbers
        if stats_data["market_cap"]:
            stats_table.add_row("Market Cap", f"${format_large_number(stats_data['market_cap'])}")
        if stats_data["shares_outstanding"]:
            stats_table.add_row("Shares Outstanding", format_large_number(stats_data['shares_outstanding']))
        if stats_data["float_shares"]:
            stats_table.add_row("Float Shares", format_large_number(stats_data['float_shares']))

        console.print(
            Panel.fit(
                stats_table,
                title=f"[bold green]Market Stats for {ticker}[/bold green]",
                border_style="blue"
            )
        )

        return stats_data

    except Exception as e:
        console.log(f"[bold red]Error fetching data for {ticker}: {e}[/bold red]")
        return None


def get_insider_buying(ticker: str):
    url = f"http://openinsider.com/{ticker.upper()}"
    console.log(f"Fetching insider data for [bold cyan]{ticker.upper()}[/] from {url}")

    try:
        # Set a user-agent to mimic a browser
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Will raise an exception for bad status codes (4xx or 5xx)

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the main data table
        table = soup.find('table', class_='tinytable')
        if not table:
            console.log(f"[yellow]Could not find insider trading table for {ticker}.[/yellow]")
            return json.dumps({"trend": "no transactions"}, indent=4)

        buy_count = 0
        sell_count = 0

        # Iterate through table rows, skipping the header
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            # Ensure the row has enough columns
            if len(cols) > 6:
                trade_type = cols[6].text.strip()
                if trade_type == 'P - Purchase':
                    buy_count += 1
                elif trade_type == 'S - Sale':
                    sell_count += 1
        
        net_buys = buy_count - sell_count
        console.log(f"Transaction summary for [bold cyan]{ticker}[/]: Buys: {buy_count}, Sells: {sell_count}, Net: {net_buys}")

        # Determine the trend based on net buys
        if net_buys >= 3:
            trend = "heavy buying"
        elif 0 < net_buys < 3:
            trend = "buying"
        else: # This covers net_buys <= 0
            trend = "selling"
        
        # Override to "no transactions" if both are zero
        if buy_count == 0 and sell_count == 0:
            trend = "no transactions"
            
        return json.dumps({"trend": trend}, indent=4)

    except ReadTimeout:
        console.log(f"[bold red]Fatal request error for {ticker.upper()}: Read timed out.[/bold red]")
        console.log("[bold red]This is a critical network issue. Terminating script as requested.[/bold red]")
        sys.exit(1)
    except RequestException as e:
        console.log(f"[bold red]A non-fatal request error occurred for {ticker}: {e}[/bold red]")
        return json.dumps({"trend": "no transactions"}, indent=4)


def get_share_buybacks(ticker_symbol: str):
    if not ticker_symbol:
        console.log("[bold red]Error: Ticker symbol cannot be empty.[/bold red]")
        return None

    try:
        console.log(f"Fetching share history for [cyan]{ticker_symbol}[/cyan]...")
        stock = yf.Ticker(ticker_symbol)

        start_date = (datetime.now() - timedelta(days=450)).strftime('%Y-%m-%d')
        shares_history = stock.get_shares_full(start=start_date)

        if shares_history is None or shares_history.empty:
            console.log(f"[bold red]No historical share data available for {ticker_symbol}.[/bold red]")
            return None

        current_shares = shares_history.iloc[-1]
        current_date = shares_history.index[-1]

        target_past_date = current_date - timedelta(days=365)
        
        # New robust method: find the integer position of the closest date
        time_deltas = (shares_history.index - target_past_date).to_series().abs()
        closest_date_position = time_deltas.argmin()
        actual_past_date = shares_history.index[closest_date_position]
        past_shares = shares_history.iloc[closest_date_position]
        
        if (current_date - actual_past_date).days < 270:
            console.log(f"[bold red]Not enough historical data for {ticker_symbol} to make a one-year comparison.[/bold red]")
            return None
            
        percentage_change = ((current_shares - past_shares) / past_shares) * 100

        output_text = Text()
        output_text.append(f"Shares on {actual_past_date.strftime('%Y-%m-%d')}:      ", style="default")
        output_text.append(f"{past_shares:,.0f}\n", style="bold")
        output_text.append(f"Shares on {current_date.strftime('%Y-%m-%d')}:        ", style="default")
        output_text.append(f"{current_shares:,.0f}\n\n", style="bold")

        sign, style = ("+", "bold red") if percentage_change >= 0 else ("", "bold green")

        output_text.append("Total Change over ~1 Year: ", style="default")
        output_text.append(f"{sign}{percentage_change:.1f}%", style=style)

        console.print(
            Panel(
                output_text,
                title=f"[bold cyan]Yearly Share Count Change for {ticker_symbol}[/bold cyan]",
                border_style="blue",
                padding=(1, 2)
            )
        )
        
        return round(percentage_change, 1)

    except Exception as e:
        console.log(f"[bold red]An error occurred for ticker '{ticker_symbol}': {e}[/bold red]")
        return None

def get_superinvestor_interest(ticker: str):
    url = f"https://www.dataroma.com/m/stock.php?sym={ticker.upper()}"
    console.log(f"Fetching data for [bold cyan]{ticker.upper()}[/] from Dataroma")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        
        main_table = soup.find('table', {'id': 'grid'})

        if main_table:
            table_body = main_table.find('tbody')
            if table_body:
                rows = table_body.find_all('tr')
                row_count = len(rows)
                console.log(f"[bold green]Success:[/bold green] Found {row_count} portfolio managers holding [bold cyan]{ticker.upper()}[/].")
                return row_count
        
        console.log(f"[bold yellow]Note:[/bold yellow] No holdings table found for ticker '{ticker}'. The ticker may be invalid or have no managers tracking it.")
        return 0

    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Request Error for {ticker.upper()}:[/bold red] {e}")
        return None
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred for {ticker.upper()}:[/bold red] {e}")
        return None


def get_company_description(ticker):
    console.log(f"Fetching company profile for [bold cyan]{ticker}[/bold cyan]...")
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        profile_data = {
            "description": info.get('longBusinessSummary'),
            "sector": info.get('sector'),
            "industry": info.get('industry'),
            "employees": info.get('fullTimeEmployees')
        }
        
        console.log(f"[bold green]Successfully built profile for {ticker}.[/bold green]")
        return profile_data
            
    except Exception as e:
        console.log(f"[bold red]An error occurred for {ticker}: {e}[/bold red]")
        return None

def get_ticker_step_ii_info(ticker: str):
    console.rule(f"[bold blue]Processing Ticker: {ticker.upper()}[/bold blue]")

    try:
        market_stats = get_market_stats(ticker)
        if market_stats is None:
            console.log(f"[bold yellow]Skipping {ticker.upper()} because market stats are absent.[/bold yellow]")
            return None
    except Exception as e:
        console.log(f"[bold red]Error in get_market_stats for {ticker}: {e}[/bold red]")
        return None

    try:
        insider_buying_json = get_insider_buying(ticker)
    except Exception as e:
        console.log(f"[bold red]Error in get_insider_buying for {ticker}: {e}[/bold red]")
        insider_buying_json = None

    try:
        share_buybacks_pct = get_share_buybacks(ticker)
    except Exception as e:
        console.log(f"[bold red]Error in get_share_buybacks for {ticker}: {e}[/bold red]")
        share_buybacks_pct = None

    try:
        superinvestor_interest = get_superinvestor_interest(ticker)
    except Exception as e:
        console.log(f"[bold red]Error in get_superinvestor_interest for {ticker}: {e}[/bold red]")
        superinvestor_interest = None

    try:
        company_profile = get_company_description(ticker)
    except Exception as e:
        console.log(f"[bold red]Error in get_company_description for {ticker}: {e}[/bold red]")
        company_profile = None

    def safe_json_get(json_string, key):
        if not json_string:
            return "N/A"
        try:
            data = json.loads(json_string)
            return data.get(key, "N/A")
        except (json.JSONDecodeError, TypeError):
            return "JSON Error"

    ins_trend = safe_json_get(insider_buying_json, 'trend')
    superinvestor_count = superinvestor_interest if superinvestor_interest is not None else 0

    trend_score_map_insider = {
        'heavy buying': 2, 'buying': 1, 'selling': 0, 'no transactions': 0
    }

    def score_share_buybacks(change_percentage):
        if not isinstance(change_percentage, (int, float)):
            return 0
        if change_percentage <= -5: return 2
        if -5 < change_percentage < 0: return 1
        return 0

    ins_score = trend_score_map_insider.get(ins_trend, 0)
    buyback_score = score_share_buybacks(share_buybacks_pct)
    superinvestor_score = 1 if int(superinvestor_count) > 0 else 0
    
    total_score = ins_score + buyback_score + superinvestor_score
    
    share_change_str = f"{share_buybacks_pct:.1f}%" if share_buybacks_pct is not None else "N/A"

    flat_data = {
        'Ticker': ticker.upper(),
        'Market Cap': format_large_number(market_stats.get('market_cap', 'N/A')) if market_stats else 'N/A',
        'Shares Outstanding': format_large_number(market_stats.get('shares_outstanding', 'N/A')) if market_stats else 'N/A',
        'Float Shares': format_large_number(market_stats.get('float_shares', 'N/A')) if market_stats else 'N/A',
        'Insider Buying Trend': ins_trend,
        'Share Change (1Y)': share_change_str,
        'Superinvestor Count': superinvestor_count,
        'Total Score': total_score,
        'Description': company_profile.get('description', 'N/A') if company_profile else 'N/A',
        'Sector': company_profile.get('sector', 'N/A') if company_profile else 'N/A',
        'Industry': company_profile.get('industry', 'N/A') if company_profile else 'N/A',
        'Employees': company_profile.get('employees', 'N/A') if company_profile else 'N/A',
        'Last Updated': date.today().strftime("%Y-%m-%d"),
    }
    
    return flat_data

def prepare_data_step_ii(list_of_ticker_data):
    console.log("Preparing data for Google Sheets...")

    if not list_of_ticker_data:
        console.log("[yellow]Warning: No ticker data provided to prepare.[/yellow]")
        return []

    header = [
        'Ticker', 'Market Cap', 'Shares Outstanding', 'Float Shares',
        'Insider Buying Trend', 'Share Change (1Y)', 'Superinvestor Count',
        'Total Score', 'Description', 'Sector', 'Industry', 'Employees', 'Last Updated'
    ]
    
    data_for_sheet = [header]
    
    for ticker_data in list_of_ticker_data:
        row = [ticker_data.get(h, "N/A") for h in header]
        data_for_sheet.append(row)
        
    console.log(f"[green]Successfully prepared {len(list_of_ticker_data)} rows for the sheet.[/green]")
    return data_for_sheet

def write_to_google_sheet_ii(data_to_write, sheet_name, worksheet_name="Sheet1"):
    client = None
    if os.getenv("GITHUB_ACTIONS") == "true":
        client = authenticate_google_sheets_sa()
    else:
        creds = authenticate_google_sheets_oauth()
        if creds:
            client = gspread.authorize(creds)

    if not client:
        console.log("[bold red]Authentication failed. Cannot get gspread client.[/bold red]")
        return
    
    if not data_to_write:
        console.log("[bold red]No data provided to write. Aborting.[/bold red]")
        return

    console.log(f"Attempting smart write to Google Sheet: '{sheet_name}', Worksheet: '{worksheet_name}'...")
    try:
        try:
            spreadsheet = client.open(sheet_name)
        except gspread.exceptions.SpreadsheetNotFound:
            console.log(f"Spreadsheet '{sheet_name}' not found. Aborting process.")
            return

        header = data_to_write[0]
        data_rows = data_to_write[1:]

        try:
            sheet = spreadsheet.worksheet(worksheet_name)
            console.log(f"Found existing worksheet: '{worksheet_name}'.")
            all_sheet_data = sheet.get_all_values()

            if not all_sheet_data or "Ticker" not in all_sheet_data[0]:
                console.log("[bold yellow]Existing worksheet is empty or has an invalid header. Re-initializing...[/bold yellow]")
                sheet.clear()
                sheet.append_row(header, value_input_option='USER_ENTERED')
                if data_rows:
                    sheet.append_rows(data_rows, value_input_option='USER_ENTERED')
                console.log(f"[bold green]Successfully re-initialized sheet with {len(data_to_write)} rows.[/bold green]")
            
            else:
                console.log("Worksheet is valid. Running update/append logic...")
                existing_header = all_sheet_data[0]
                try:
                    ticker_col_index = existing_header.index("Ticker")
                    last_updated_col_index = existing_header.index("Last Updated")
                except ValueError as e:
                    console.log(f"[bold red]Missing a required column in the header: {e}. Aborting update.[/bold red]")
                    return

                existing_tickers_map = {
                    row[ticker_col_index]: {"row_index": i + 2, "last_updated": row[last_updated_col_index]}
                    for i, row in enumerate(all_sheet_data[1:]) if len(row) > max(ticker_col_index, last_updated_col_index)
                }

                rows_to_append = []
                updates_for_batch = []
                three_months_ago = datetime.now() - timedelta(days=90)
                
                new_ticker_idx = header.index("Ticker")

                for row_data in data_rows:
                    ticker = row_data[new_ticker_idx]
                    if ticker not in existing_tickers_map:
                        rows_to_append.append(row_data)
                    else:
                        existing_entry = existing_tickers_map[ticker]
                        should_update = False
                        try:
                            last_updated_date = datetime.strptime(existing_entry["last_updated"], "%Y-%m-%d")
                            if last_updated_date < three_months_ago:
                                should_update = True
                        except (ValueError, TypeError):
                            should_update = True
                        
                        if should_update:
                            update_range = f"A{existing_entry['row_index']}"
                            updates_for_batch.append({"range": update_range, "values": [row_data]})

                if rows_to_append:
                    sheet.append_rows(rows_to_append, value_input_option='USER_ENTERED')
                    console.log(f"[bold green]Successfully appended {len(rows_to_append)} new tickers.[/bold green]")
                else:
                    console.log("[bold yellow]No new tickers to append.[/bold yellow]")

                if updates_for_batch:
                    sheet.batch_update(updates_for_batch, value_input_option='USER_ENTERED')
                    console.log(f"[bold green]Successfully updated {len(updates_for_batch)} stale tickers.[/bold green]")
                else:
                    console.log("[bold yellow]No stale tickers required an update.[/bold yellow]")

        except gspread.exceptions.WorksheetNotFound:
            console.log(f"Worksheet '{worksheet_name}' not found. Creating and initializing...")
            sheet = spreadsheet.add_worksheet(title=worksheet_name, rows=len(data_to_write) + 100, cols=len(header))

            console.log(f"Writing new header to '{worksheet_name}'...")
            sheet.append_row(header, value_input_option='USER_ENTERED')
            
            if data_rows:
                console.log(f"Appending {len(data_rows)} data rows...")
                sheet.append_rows(data_rows, value_input_option='USER_ENTERED')
            
            console.log(f"[bold green]Successfully created and populated new sheet.[/bold green]")

    except Exception as e:
        console.log(f"[bold red]An unexpected error occurred while processing the sheet:[/bold red] {e}")
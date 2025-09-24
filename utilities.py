# Proposed functions:

# - Write to sheet
# - Call LLM
# - Website contexts

import os
import json
import gspread
from datetime import datetime, timedelta, UTC
from google import genai
from google.genai import types
from rich.console import Console
from rich.progress import Progress
from dotenv import load_dotenv

import re
import requests
import praw
import praw.models
from bs4 import BeautifulSoup
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from urllib.parse import urljoin, urlparse, parse_qs

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
            model='gemini-2.5-flash',
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


def write_to_google_sheet(data_to_write, sheet_name):
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

    console.log(f"Attempting to write to Google Sheet: '{sheet_name}'...")
    try:
        try:
            spreadsheet = client.open(sheet_name)
        except gspread.exceptions.SpreadsheetNotFound:
            console.log(f"Sheet '{sheet_name}' not found. Creating a new one...")
            spreadsheet = client.create(sheet_name)
            try:
                if os.getenv("GITHUB_ACTIONS") == "true":
                     console.log("Service Account cannot share. Please check Google Cloud Console for sheet.")
                else:
                    pass
            except Exception as e:
                 console.log(f"[bold yellow]Could not auto-share new sheet:[/bold yellow] {e}")
            
        sheet = spreadsheet.sheet1
        
        # Get all tickers currently in the sheet (Column 1)
        existing_tickers = set(sheet.col_values(1))
        console.log(f"Found {len(existing_tickers)} existing tickers in '{sheet_name}'.")

        header_row = data_to_write[0]
        data_rows = data_to_write[1:]
        
        rows_to_append = []
        
        if "Ticker" not in existing_tickers:
            rows_to_append.append(header_row)

        new_tickers_added_count = 0
        for row in data_rows:
            ticker = row[0]
            # Only append the row if the ticker is not already in the sheet
            if ticker not in existing_tickers:
                rows_to_append.append(row)
                new_tickers_added_count += 1
        
        if rows_to_append:
            sheet.append_rows(rows_to_append, value_input_option='USER_ENTERED')
            
            if new_tickers_added_count > 0:
                console.log(f"[bold green]Successfully added {new_tickers_added_count} new tickers to '{sheet_name}'.[/bold green]")
            else:
                console.log(f"[bold green]Successfully initialized sheet '{sheet_name}' with header.[/bold green]")
        else:
            console.log("[bold yellow]No new tickers found. Sheet is already up-to-date.[/bold yellow]")
        
    except Exception as e:
        console.log(f"[bold red]An unexpected error occurred while writing to the sheet:[/bold red] {e}")
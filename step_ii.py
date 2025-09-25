# Goal: an initial filter

# - Market cap
# - Insider buying
# - Share buybacks
# - Superinvestors buying in
# - Simple elevator pitch of what the company does

import utilities
from rich.console import Console
from rich import print as rprint

console = Console()

def fetch_stock_info(tickers):
    console.log(f"Fetching stock data for tickers {tickers}")

    stock_data = []
    for ticker in tickers:
        ticker_info = utilities.get_ticker_step_ii_info(ticker)

        if ticker_info:
            stock_data.append(ticker_info)

    console.log(f"Fetched a total of {len(stock_data)} ticker entries.")
    return stock_data

if __name__ == "__main__":
    console.rule("[bold blue]Ticker Filtering: Step II[/bold blue]")
    
    tickers_all = set(utilities.get_step_i_tickers())
    already_processed_tickers = set(utilities.get_step_ii_tickers())

    tickers = list(tickers_all - already_processed_tickers)

    batch_size = 5
    for i in range(0, len(tickers), batch_size):
        batch = tickers[i:i + batch_size]

        stock_data = fetch_stock_info(batch)
        sheet_data = utilities.prepare_data_step_ii(stock_data)

        console.rule()

        utilities.write_to_google_sheet_ii(
            data_to_write=sheet_data,
            sheet_name='stock-research',
            worksheet_name='step-ii'
        )
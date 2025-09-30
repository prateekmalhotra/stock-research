# Goal: an initial filter

# - Market cap
# - Insider buying
# - Share buybacks
# - Superinvestors buying in
# - Simple elevator pitch of what the company does

import utilities
from rich.console import Console

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

    # import json

    # tickers_all = set(utilities.get_step_ii_tickers())
    # already_processed_tickers = set(utilities.get_step_ii_tickers(column='Seeking Alpha Sentiment'))

    # tickers = list(tickers_all - already_processed_tickers)

    # for ticker in tickers:
    #     seeking_alpha_info = utilities.get_seeking_alpha_sentiment(ticker)
    #     seeking_alpha_info = json.loads(seeking_alpha_info)
    #     ticker = seeking_alpha_info["ticker"]
    #     trend = seeking_alpha_info["trend"]

    #     seeking_alpha_info = {ticker.upper():trend}

    #     utilities.update_single_column(
    #         sheet_name='stock-research',
    #         data_to_update=seeking_alpha_info,
    #         key_column_name='Ticker',
    #         value_column_name='Seeking Alpha Sentiment',
    #         worksheet_name="step-ii"
    #     )
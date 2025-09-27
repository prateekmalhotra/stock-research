# Goal: get good tickers

# - Reddit posts past day r/valueinvesting r/wallstreetbets 
# - openinsider
# - dataroma (no need daily)

import utilities
from rich.console import Console
from rich import print as rprint

console = Console()

def fetch_all_data():
    console.log("Fetching data from all sources...")
    
    all_tickers_lists = (
        utilities.get_reddit_tickers() +
        utilities.get_openinsider_tickers() +
        utilities.get_dataroma_tickers() +
        utilities.get_more_hedge_funds_tickers() +
        utilities.custom_tickers()
    )
    
    console.log(f"Fetched a total of {len(all_tickers_lists)} ticker entries.")
    return all_tickers_lists

if __name__ == "__main__":
    console.rule("[bold blue]Ticker Aggregation: Step I[/bold blue]")
    raw_data = fetch_all_data()   
    merged_data = utilities.merge_ticker_data(raw_data)    
    sheet_data = utilities.prepare_data_for_sheet(merged_data)
    
    console.rule()
    
    utilities.write_to_google_sheet(
        data_to_write=sheet_data, 
        sheet_name='stock-research',
        worksheet_name='step-i'
    )
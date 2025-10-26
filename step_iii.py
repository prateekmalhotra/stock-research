# Goal a more detailed qualitative analysis 

# Business
# Company history
# Moat analysis
# Catalyst analysis
# Management analysis, track record, and compensation structure
# Price history
# Long thesis
# Holes in the thesis

import utilities
from rich.console import Console

console = Console()

if __name__ == "__main__":
    utilities.send_alert_on_down()
    console.rule("[bold green]Qualitative Analysis: Step III[/bold green]")
    
    tickers_all = utilities.get_step_ii_tickers()
    already_processed_tickers = set(utilities.get_step_iii_tickers())
    tickers = [t for t in tickers_all if t not in already_processed_tickers]
    limit = 10 if len(tickers) > 10 else len(tickers)

    for ticker in tickers[:limit]:
        stock_data = utilities.get_ticker_step_iii_info(ticker)
        sheet_data = utilities.prepare_data_step_iii(stock_data)

        console.rule()

        utilities.write_to_google_sheet_ii(
            data_to_write=sheet_data,
            sheet_name='stock-research',
            worksheet_name='step-iii',
            days=180
        )

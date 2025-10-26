# Goal a detailed quantitative analysis 

# Get a reasonable fair value
# Use Monte Carlo simulation to pressure test assumptions

import os
import utilities
import subprocess
from datetime import date
from github import Github
from rich.console import Console

console = Console()

if __name__ == "__main__":
    console.rule("[bold green]Quantitative Analysis: Step IV[/bold green]")
    console.rule()

    YELLOW = {'red': 1, 'green': 0.9490196, 'blue': 0.8}
    BLUE = {'red': 0.788235294117647, 'green': 0.8549019607843137, 'blue': 0.9686274509803922}

    already_processed_tickers = set(utilities.get_step_iii_tickers(worksheet_name='step-iv'))
    tickers = utilities.find_rows_by_color('stock-research', [BLUE, YELLOW], 'step-iii').to_dict(orient='records')

    for ticker_data in tickers:
        ticker = ticker_data.get('Ticker')
        if ticker not in already_processed_tickers:

            fair_value_text = utilities.get_fair_value(ticker)
            step_iv_script = utilities.get_step_iv_script(ticker, fair_value_text)

            for part in step_iv_script.candidates[0].content.parts:
                if part.executable_code is not None:
                    step_iv_script = part.executable_code.code
                    break

            with open('step_iv.py', 'w', encoding='utf-8') as f:
                    f.write(step_iv_script)
            console.print(f"  [green]✓[/green] Wrote script to step_iv.py.")

            console.print(f"  [blue]Running: poetry run python -B step_iv.py[/blue]")
            result = subprocess.run(
                    ['poetry', 'run', 'python', '-B', 'step_iv.py'],
                    check=True,
                    capture_output=True,
                    text=True,
                    encoding='utf-8'
                )

            console.print(f"  [dim]Script STDOUT:[/dim]\n{result.stdout}")
            console.print(f"  [green]✓[/green] Successfully executed step_iv.py for {ticker}.")

            utilities.save_image_to_github(ticker, "mc", f"{ticker}_montecarlo.png")
            os.remove(f"{ticker}_montecarlo.png")
            link_fv = f'https://github.com/prateekmalhotra/stock-research/blob/main/files/{ticker}/{ticker}_fv.md'
            link_mc = f'https://github.com/prateekmalhotra/stock-research/blob/main/files/{ticker}/{ticker}_mc.png'

            if os.path.exists('step_iv.py'):
                os.remove('step_iv.py')
                console.print(f"\n[dim]Cleaned up step_iv.py[/dim]")

            sheet_data = utilities.prepare_data_step_iv({'Ticker': ticker, 'Fair value analysis': link_fv, 'Monte Carlo analysis': link_mc, 'Last Updated': date.today().strftime("%Y-%m-%d")})

            utilities.write_to_google_sheet_ii(
                data_to_write=sheet_data,
                sheet_name='stock-research',
                worksheet_name='step-iv',
            )


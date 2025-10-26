This valuation of Southwest Airlines Co. (LUV) is conducted using a Discounted Cash Flow (DCF) model, strictly adhering to the rule of using only SEC filings and management guidance.

## Southwest Airlines Co. (LUV) Stock Valuation

### 1. Financial Inputs (as of Q3 2025)

The base financials are derived from the Company's Q3 2025 Form 10-Q and accompanying press releases.

| Metric | Value (in millions) | Justification |
| :--- | :--- | :--- |
| **Total Liquid Cash (Cash & Equivalents + Short-term Investments)** | **\$3,000 million** | Total liquid assets at the end of Q3 2025 [cite: 7, 19 in original search]. |
| **Total Debt Outstanding** | **\$6,700 million** | The most recent explicitly stated "debt outstanding" from the Full Year 2024 earnings release (Dec 31, 2024). This is used as a conservative, verifiable figure, even though the company has since repaid approximately \$2.5 billion in notes in 2025, which would imply a lower current debt figure. |
| **Shares Outstanding (Diluted)** | **517.155 million** | Shares outstanding as of October 22, 2025 [cite: 7 in original search]. |
| **FY 2024 Revenue (Baseline)** | **\$27,500 million** | Record full year operating revenues for 2024. |
| **FY 2025 EBIT Guidance (Midpoint)** | **\$700 million** | Midpoint of the full year 2025 EBIT guidance (excluding special items) range of \$600M to \$800M [cite: 4, 19 in original search]. |
| **Effective Tax Rate (Midpoint Guidance)** | **23%** | Midpoint of the estimated full year 2025 effective tax rate range of 22% to 24%. |
| **Net Income Reinvestment Return (ROIC)** | **4.0%** | The historical ROIC is volatile and often low or negative post-COVID [cite: 3 in original search]. The company's goal is to achieve an ROIC "well above its weighted average cost of capital" [cite: 6 in original search]. As a **conservative but reasonable positive ROIC** for future positive Net Income, **4.0%** is assumed. |

***

### 2. Revenue and Net Income Projections (2025-2030)

The core of the projection is built around the "Southwest Even Better" plan, which has explicit, transformative incremental EBIT targets provided by management.

#### A. Business Engine and Revenue Projections

The valuation utilizes management's direct financial targets for incremental EBIT as the primary driver for future profitability, which, by instruction, must be treated as truth.

| Year | Revenue (\$M) | Operating Income (EBIT) (\$M) | Justification/Model |
| :--- | :--- | :--- | :--- |
| **2024 (Actual)** | \$27,500 | $\sim$\$774 (Estimated from \$597M NI at 23% tax) | Baseline. |
| **2025 (Projected)** | **\$28,500** | **\$700** | Uses the **Management EBIT Guidance Midpoint** of **\$700M** [cite: 7 in original search]. Revenue is estimated with a conservative $\sim$3.6% YoY growth, consistent with management commentary on revenue initiatives and network realignment. |
| **2026 (Projected)** | **\$31,000** | **\$5,000** | **Core EBIT (\$700M) + Incremental EBIT (\$4.3B)**. The \$4.3 billion is the management-guided full-year incremental EBIT target for 2026 from the transformation initiatives. Revenue assumes a conservative 8.8% growth to support the massive increase in profitability. |
| **2027 (Projected)** | **\$32,000** | **\$5,250** | Assumes the **\$1.5B run-rate** from assigned/extra legroom seating and core growth. Projecting a conservative **5.0% YoY EBIT growth** on the 2026 base, maintaining momentum from new services, and $32.0B revenue (3.2% YoY). |
| **2028 (Projected)** | **\$32,800** | **\$5,400** | Steady-state modeling: **2.5% YoY Revenue Growth** (conservative) and **2.9% YoY EBIT Growth**. This assumes the initial bump is over and growth moderates. |
| **2029 (Projected)** | **\$33,620** | **\$5,550** | **2.5% YoY Revenue Growth** and **2.8% YoY EBIT Growth**. |
| **2030 (Projected)** | **\$34,460** | **\$5,700** | **2.5% YoY Revenue Growth** and **2.7% YoY EBIT Growth**. |

#### B. Net Income Calculation (Discounted Cash Flow Proxy)

The Net Income (as a proxy for unlevered Free Cash Flow for this airline's DCF) is calculated by applying the guided 23% tax rate to the projected EBIT, plus the assumed 4.0% ROIC on the prior year's reinvested net income.

**Formula Used:**
*   **Net Income (Year N) = [(EBIT (Year N) * (1 - 0.23 Tax Rate))] + [Net Income (Year N-1) * 4.0% ROIC]**

| Year | EBIT (\$M) | EBT (\$M) | Tax (23%) (\$M) | Net Income from Operations (\$M) | ROIC Income (\$M) | **Total Net Income (\$M)** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2025** | 700 | 700 | 161 | 539 | - | **539** |
| **2026** | 5,000 | 5,000 | 1,150 | 3,850 | 22 | **3,872** |
| **2027** | 5,250 | 5,250 | 1,208 | 4,043 | 155 | **4,198** |
| **2028** | 5,400 | 5,400 | 1,242 | 4,158 | 168 | **4,326** |
| **2029** | 5,550 | 5,550 | 1,277 | 4,273 | 173 | **4,446** |
| **2030** | 5,700 | 5,700 | 1,311 | 4,389 | 178 | **4,567** |

***

### 3. Discounted Cash Flow (DCF) Valuation

#### A. Discount Rate and Terminal Value

1.  **Discount Rate (Conservative but Reasonable):** **9.0%**
    *   This is chosen as a conservative rate, above the estimated industry WACC in one source (5.88% [cite: 4 in original search]) but below a typical equity cost for a company emerging from a period of turbulence with an ambitious turnaround plan.

2.  **Conservative Maturity Rate (Perpetual Growth Rate):** **2.0%**
    *   This is a highly conservative long-term growth rate, reflecting a mature airline business growing only slightly faster than long-term inflation, well below the historical GDP growth.

3.  **Terminal Value (TV) (from 2031 onwards):**
    *   $TV_{2030} = \frac{\text{Cash Flow}_{2030} \times (1 + \text{g})}{\text{WACC} - \text{g}} = \frac{\$4,567 \times (1 + 0.02)}{0.09 - 0.02} = \frac{\$4,658}{0.07} = \mathbf{\$66,543 \text{ million}}$

#### B. Net Present Value (NPV) Calculation

| Year | Total Net Income (\$M) | Discount Factor (9.0%) | Present Value (\$M) |
| :--- | :--- | :--- | :--- |
| **2025** | 539 | 0.917 | 494 |
| **2026** | 3,872 | 0.842 | 3,260 |
| **2027** | 4,198 | 0.772 | 3,241 |
| **2028** | 4,326 | 0.708 | 3,064 |
| **2029** | 4,446 | 0.650 | 2,890 |
| **2030** | 4,567 | 0.596 | 2,720 |
| **Terminal Value** | 66,543 | 0.596 | 39,634 |
| | | **Total NPV** | **\$55,299 million** |

***

### 4. Fair Value Calculation

| Metric | Value (in millions) |
| :--- | :--- |
| **Total Net Present Value (NPV)** | \$55,299 |
| **PLUS: Total Liquid Cash** | \$3,000 |
| **MINUS: Total Debt Outstanding (Conservative)** | \$6,700 |
| **Equity Value** | **\$51,599 million** |
| **Divided by: Shares Outstanding** | 517.155 million |
| **Fair Value Per Share** | **\$99.78** |

***

### 5. Conclusion and Market Comparison

| Metric | Value |
| :--- | :--- |
| **Fair Value Per Share** | **\$99.78** |
| **Current Stock Price (as of valuation date)** | $\sim\$27.00$ (Assumed for comparison) |
| **Discrepancy** | **270% Higher** |

#### Justification for Discrepancy

The calculated Fair Value of **\$99.78** is significantly higher (nearly four times) than the current market price (assumed to be around \$27.00). This major difference is entirely due to one critical assumption: the mandated use of management's highly aggressive turnaround targets.

1.  **Management Guidance as the Engine:** The core of this valuation is built upon the management's publicly stated goal of generating an **incremental EBIT contribution of \$4.3 billion in 2026** from its 'Southwest Even Better' plan. This is a massive, transformative leap from a guided \$700 million EBIT in 2025 (a 614% increase). The market is clearly *not* giving full credit to this guidance, believing it is either over-ambitious, too risky, or contingent on a flawless execution of a complex, multi-year, multi-billion-dollar initiative portfolio.
2.  **Market Skepticism:** The market likely views the execution risk of these initiatives (assigned seating, new loyalty/fare products, etc.) as extremely high, especially in the competitive and low-margin airline industry. The current stock price reflects a high degree of skepticism that LUV can achieve the $5 billion EBIT in 2026 or maintain the projected 16-17% operating margin implied by that EBIT. Instead, the market is likely pricing LUV at a modest growth multiple based on the lower, historical profitability (e.g., using a forward P/E on 2025 earnings).
3.  **Conservative Debt/ROIC Offset:** Using the higher, older debt figure (\$6.7B) and a conservative terminal growth (2.0%) was an attempt to temper the outcome, but the sheer scale of the projected 2026-2030 Net Income, derived directly from management's **\$4.3 billion** guidance, overwhelms any other conservative input.

**Conclusion on Fair Value:**

The Fair Value of **\$99.78** is a direct mathematical consequence of taking Southwest Airlines' public, transformational EBIT guidance for 2026 and subsequent years **as truth**, as required by the valuation rules. An investor who believes in management's explicit targets has an equity value of over \$51 billion. An investor who prices the stock at its current market value is effectively dismissing a significant portion of the planned \$4.3 billion incremental profit as unachievable.
# Valuation of Dow Inc. (DOW) Stock

This valuation utilizes a Discounted Cash Flow (DCF) methodology based strictly on publicly available SEC filings and management commentary from the last four earnings calls, avoiding analyst estimates as requested.

## 1. Baseline Financial Data (as of September 30, 2025)

All financial data is based on Dow Inc.'s Q3 2025 Form 10-Q (filed October 2025) and the 2024 Form 10-K.

| Metric | Value (in millions USD, unless noted) | Source/Notes |
| :--- | :--- | :--- |
| **Current Stock Price** | **$22.32** | As of November 8, 2025. |
| **Shares Outstanding (Diluted)** | **710.77 million** | As of September 30, 2025. |
| **Cash and Cash Equivalents** | **$4,609** | As of September 30, 2025. (Includes proceeds from the asset sale/legal judgment announced in Q1/Q2 2025). |
| **Total Debt** | **$18,255** | Long-Term Debt ($17,709) + Long-Term Debt Due within One Year ($413) + Notes Payable ($133). As of September 30, 2025. |
| **2024 Full Year Revenue** | **$43,000** | |
| **2024 Full Year Net Income (Attributable to Common Stockholders)** | **$1,104** | |
| **2024 Net Income Margin** | **2.57%** | (1,104 / 43,000) - Reflects trough earnings in the cycle. |

## 2. Business Engine and Projection Assumptions

The chemical industry is highly cyclical, and Dow is currently at a cyclical low, which is reflected in the low 2024 Net Income Margin (2.57%). The valuation must project a recovery toward a "mid-cycle" level, driven by two primary factors highlighted by management: **Volume Recovery** and **Structural Cost/Asset Optimization.**

### A. Business Engine (Revenue)

Dow's revenue engine is driven by:
1.  **Macro-cycle Recovery (Price/Volume):** The company is currently experiencing a "lower for longer earnings environment" with depressed prices and volumes. We project a recovery in volume and price back toward a long-term average.
2.  **Structural Efficiencies (Future Margin Uplift):** Management has specifically guided on future EBITDA targets, which implies a return to higher profitability without a corresponding massive revenue surge. The key metric is the **mid-cycle EBITDA target of $8.6 billion**.

**Revenue Projections:**
We assume a gradual recovery to a "mid-cycle" revenue of **$50.0 billion** by 2028, a conservative figure given the 2022 high of $56.9 billion and the long-term average of around $48 billion. The growth rate slows post-2028 as the market normalizes.

| Year | Rationale | Projected Revenue (USD millions) | % Growth |
| :--- | :--- | :--- | :--- |
| **2024 (Actual)** | Baseline | $43,000 | |
| **2025** | Trough recovery, minimal price uplift. Volume up slightly (Q1 up 2% YoY). | $44,500 | 3.49% |
| **2026** | First full year of significant volume/price recovery in core markets; high-single-digit growth. | $48,000 | 7.87% |
| **2027** | Continued strong cyclical recovery towards mid-cycle revenue. | $50,000 | 4.17% |
| **2028** | Stabilization at mid-cycle peak revenue. | $51,000 | 2.00% |
| **2029** | Stable growth/inflation rate. | $52,020 | 2.00% |
| **2030** | Stable growth/inflation rate. | $53,060 | 2.00% |

### B. Margin Projections (Net Income Margin)

Management guidance focuses on a return to higher EBITDA, underpinned by structural improvements:
*   **Targeted Cost Savings:** At least **$1 billion in cost savings by the end of 2026**.
*   **Asset Optimization:** **$200 million annual EBITDA uplift by 2029** (half by 2027) from European asset reviews/shutdowns.

We will translate these EBITDA drivers into a Net Income Margin projection, aiming for a post-tax profitability that corresponds to the projected **mid-cycle EBITDA of $8.6 billion**.

| Year | Rationale | EBITDA Margin Target | Implied Net Income Margin (Conservative Estimate) |
| :--- | :--- | :--- | :--- |
| **2024 (Actual)** | Trough earnings. (2024 Op. EBIT was $2.6B on $43B sales) | Approx. 9.0% | 2.57% |
| **2025** | $\approx \$0.4B$ of cost savings expected. Cyclical pressure continues. | 11.0% | 3.50% |
| **2026** | Full run-rate of $1.0B cost savings. Volume/Price recovery helps. | 13.0% | 5.50% |
| **2027** | Recovery continues + half of $0.2B asset uplift. | 15.0% | 7.00% |
| **2028** | Full cyclical recovery + structural uplift. **$8.6B Mid-cycle EBITDA** on $51B revenue is $\approx 16.9\%$ margin. | 16.5% | 8.50% |
| **2029** | Full asset uplift in place. Sustainable mid-cycle margin. | 17.0% | 9.00% |
| **2030** | Stable margin. | 17.0% | 9.00% |

*Note: The implied Net Income Margin grows slower than the EBITDA margin due to high interest expense and other fixed non-operating costs. A 9.0% Net Income Margin is still conservative compared to peak-cycle margins.*

## 3. Discounted Cash Flow (DCF) Model

### A. Core Assumptions

| Assumption | Value | Rationale/Justification |
| :--- | :--- | :--- |
| **Conservative ROIC (Return on Invested Capital)** | **5.5%** | This is a conservative choice, approximately equal to the company's 3-year average ROIC of 5.45% (from preliminary search) and close to its median 5-year ROIC, assuming the business can generate moderate returns on retained earnings from prior years. |
| **Conservative Discount Rate (WACC Proxy)** | **8.0%** | A conservative but reasonable rate for a large, cyclical chemical company. This implies a higher cost of capital than typical AAA companies, reflecting the industry's volatility. |
| **Conservative Maturity Rate (Terminal Growth Rate)** | **2.0%** | A very conservative rate, in line with or slightly below long-term expected GDP/inflation for developed markets, representing a no-growth-above-inflation maturity. |

### B. Projected Net Income and Terminal Value Calculation

| Year | Projected Revenue (A) | Implied Net Income Margin (B) | Net Income (A * B) (C) | Retained Net Income from Prior Year (D) | ROIC on Prior Retained Income (D * 5.5%) (E) | Total Net Income / Cash Flow (C + E) | NPV at 8.0% Discount |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2025** | $44,500 | 3.50% | 1,558 | 1,104 (2024 NI) | 61 | 1,619 | 1,499 |
| **2026** | $48,000 | 5.50% | 2,640 | 1,619 | 89 | 2,729 | 2,339 |
| **2027** | $50,000 | 7.00% | 3,500 | 2,729 | 150 | 3,650 | 2,900 |
| **2028** | $51,000 | 8.50% | 4,335 | 3,650 | 201 | 4,536 | 3,334 |
| **2029** | $52,020 | 9.00% | 4,682 | 4,536 | 250 | 4,932 | 3,354 |
| **2030** | $53,060 | 9.00% | 4,775 | 4,932 | 271 | 5,046 | 3,179 |
| **Total NPV of Projected Cash Flows (2025-2030)** | | | | | | | **$16,605** |

**Terminal Value (TV) Calculation (Conservative Maturity):**

Terminal Cash Flow = 2030 Total Net Income / (Discount Rate - Maturity Rate)
Terminal Cash Flow = $5,046 million / (8.0% - 2.0%)
Terminal Cash Flow = $5,046 million / 0.06 = **$84,100 million**

**Net Present Value (NPV) of Terminal Value:**

NPV of TV = Terminal Value / (1 + Discount Rate)^(Terminal Year - Current Year)
NPV of TV = $84,100 million / (1.08)^(6) = **$52,999 million**

**Total Enterprise Value (TEV):**

TEV = NPV of Projected Cash Flows + NPV of Terminal Value
TEV = $16,605 million + $52,999 million = **$69,604 million**

## 4. Fair Value Calculation

| Metric | Value (in millions USD, unless noted) |
| :--- | :--- |
| **Total Enterprise Value (TEV)** | $69,604 |
| **LESS: Total Debt** | $18,255 |
| **ADD: Cash and Cash Equivalents** | $4,609 |
| **Total Equity Value** | **$55,958** |
| **Shares Outstanding (Diluted)** | 710.77 million |
| **Fair Value Per Share** | $55,958 / 710.77 = **$78.73** |

***

# FAIR VALUE OF DOW INC. (DOW) STOCK

The calculated **Fair Value Per Share** for Dow Inc. is **$78.73**.

## Justification of Discrepancy

**Current Market Price:** $22.32
**Calculated Fair Value:** $78.73
**Discrepancy:** The calculated Fair Value is approximately **3.5x higher** than the Current Market Price.

**Why is the Market's Assumption so Different from My Valuation?**

The market is currently pricing Dow based on the assumption that the "lower for longer" cyclical downturn **will be significantly more protracted and damaging** than my model assumes, potentially failing to reach mid-cycle profitability targets or sustaining the $8.6 billion EBITDA target.

My conservative but realistic valuation assumes:
1.  **Successful Cyclical Recovery:** A gradual recovery to the management-guided **mid-cycle profitability** (implied 9.0% Net Income Margin on $51B revenue by 2028), driven by volume/price and structural cost actions.
2.  **Structural Improvement is Real:** The **$1 billion in cost savings by 2026** and the **$200 million asset uplift by 2029** are fully realized, serving as a permanent floor for future profitability.
3.  **Low Terminal Growth:** A very conservative terminal growth rate of **2.0%** (below long-term historical GDP) is used.

**The Market is Likely Assuming:**
*   **"Lower for Much Longer":** The market fears the current margin contraction is structural, not just cyclical, driven by **persistent oversupply** from new capacity (e.g., in Asia/Middle East) that will keep product pricing permanently depressed. This means my projected 9.0% Net Income Margin may never be reached, instead stagnating near the current 2.5% to 5.0% levels.
*   **Cost Savings are Offset:** The market may believe the $1 billion in cost savings will be entirely offset by higher raw material/feedstock costs or necessary maintenance CapEx, resulting in no meaningful margin expansion.
*   **Massive Value Destruction:** The extreme discount suggests the market is pricing in a long-term ROIC that is closer to the current TTM low (1.56% to 3.08% from preliminary search) or even below the cost of capital, indicating a view of **long-term value destruction** rather than a moderate recovery.

**My Justification for the Fair Value:**
My valuation of $78.73 is justifiable because it is based on **management's stated mid-cycle target of $8.6 billion EBITDA** and the **$1 billion structural cost program**. Since Dow is a major player in a cyclical industry, a return to mid-cycle economics is the standard, conservative expectation for a DCF valuation. The current market price of $22.32 implies either an **imminent, long-term failure** to monetize its cost-advantaged assets or a perpetual recession, which is inconsistent with Dow's historical performance and the explicit, recent guidance on *structural* improvements designed to navigate this cycle. Therefore, the stock is currently **significantly undervalued** based on a conservative projection toward mid-cycle recovery and execution of stated cost savings.
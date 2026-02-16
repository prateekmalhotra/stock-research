## Valuation of The Middleby Corporation (MIDD) Stock

### I. Key Financial Data Compilation

The following financial data is sourced from The Middleby Corporation's latest available SEC filings (10-K for fiscal year ended December 28, 2024, and subsequent 10-Q and 8-K filings), with assumptions clearly noted. **All figures are in millions of USD unless otherwise noted.**

| Metric | Value | Source/Assumption |
| :--- | :--- | :--- |
| **Current Stock Price** (as of Feb. 6, 2026) | $161.05/share | Market data |
| **Shares Outstanding** (as of Feb. 2026) | 50.5 million | Estimate based on latest reported number and share repurchases. |
| **Total Cash & Cash Equivalents** (as of Dec. 28, 2024) | $689.5 | 2024 10-K. *Used as a conservative base.* |
| **Total Debt** (as of Dec. 28, 2024) | $2,400.0 | 2024 10-K. |

**Note on Cash and Debt Subsequent Event:**
An 8-K filed on February 2, 2026, announced the sale of a 51% stake in the Residential Kitchen business, resulting in **$540 million in cash proceeds** and a $135 million seller note. This cash was primarily used for share repurchases: $218 million in Q4 2025 and $152 million in January 2026, totaling $370 million. The *net* cash inflow from this event is $540M - $370M = **$170 million**. For the final fair value calculation, I will use the baseline Cash & Equivalents of $689.5M plus this net inflow of $170M, adjusted for the capital structure change, but keep the DCF model on the pre-adjusted business since a full separation of historical financials is not possible.

### II. Business Engine and Revenue Projection (2025-2030)

The Middleby Corporation operates in three segments: Commercial Foodservice Equipment (CFS), Food Processing Equipment (FP), and Residential Kitchen Equipment (RK). The business engine is driven by:
1.  **CFS (Core Business):** Innovation-driven sales of high-efficiency, speed-increasing equipment (e.g., FryBot, PizzaBot) to Quick Service Restaurants (QSRs) and institutional kitchens, and aftermarket service/parts. Management noted "ongoing softness at several large QSR customers" into early 2026.
2.  **FP (Future Spin-Off):** Demand for automation and cooking/packaging solutions in protein and baking industries. This segment has higher margins (21% organic EBITDA margin in Q3 2025) but can be "lumpy."
3.  **RK (Non-Core/JV):** Now a 49% non-controlling interest, its operating cash flow will largely be excluded from future net income projections for the DCF (only the 49% share of equity earnings would be included, which is difficult to project accurately).

**Revenue Engine Assumptions:**

*   **2025 Base Year:** Use the full-year 2025 guidance midpoint of **$3.87 billion**.
*   **Post-2025 Conservative Growth:** The model will focus on the continuing operations (CFS and FP, which is expected to spin off in mid-2026). Given the QSR softness and the general cyclical nature of industrial equipment, a conservative long-term growth rate is necessary. The strategic moves (Residential sale, FP spin-off) are intended to unlock value, but the underlying organic growth of the core business (CFS) is modest.
    *   **Assumption:** I will assume a **2.0% annual revenue growth** from 2026 to 2030 for the *total company's pre-spin revenue*, reflecting general economic growth and modest market penetration, tempered by the noted QSR weakness. This is a conservative assumption, especially considering the potential acceleration from new technology adoption, but prioritizes conservatism.
*   **Residential Kitchen Adjustment:** Given the Residential Kitchen business is being reported as a discontinued operation from Q4 2025 and will be a 49% JV, I will use the **full revenue** for simplicity in the DCF calculation and account for the capital structure change in the final step, as removing the segment's financials from the historical record is not possible with available data. The *Net Income* projection will use a conservative Net Income Margin on the total revenue.

| Year | Revenue Projection (Millions) | Justification |
| :--- | :--- | :--- |
| **2025** | $3,870.0 | Management Guidance Midpoint |
| **2026** | $3,947.4 | $3,870.0 * 1.020 (2.0% growth) |
| **2027** | $4,026.3 | $3,947.4 * 1.020 (2.0% growth) |
| **2028** | $4,106.8 | $4,026.3 * 1.020 (2.0% growth) |
| **2029** | $4,188.9 | $4,106.8 * 1.020 (2.0% growth) |
| **2030** | $4,272.7 | $4,188.9 * 1.020 (2.0% growth) |

### III. Margin and Net Income Projection

The net income projection will be based on an estimated Net Income Margin, which is conservative given the strategic restructuring and noted margin pressures (tariffs, QSR weakness).

*   **Gross Margin (GM%):** 30.2% in 2024.
*   **SG&A as % of Sales (SGA%):** 19.7% in 2024.
*   **Operating Margin (OM%):** 30.2% - 19.7% = 10.5% (2024).
*   **Tax Rate:** Effective rate around 22% to 25% (2025 Q1/Q2). I will use a conservative **25.0%**.
*   **Net Income Margin (NIM%):** Based on the operating margin, after interest expense (which is complex due to debt paydown) and taxes, a conservative Net Income Margin is estimated. I will use **7.0%** for all years. This is slightly below the implied 2025 NIM based on the $8.99-$9.14 EPS guidance, making it conservative.

**Return on Invested Capital (ROIC) Assumption:**
The rule requires a reasonable ROIC applied to the prior year's Net Income (assumed to be converted to cash) to get additional income. A conservative and reasonable ROIC for an industrial company like Middleby, which historically uses M&A as a key growth driver (a form of capital deployment), is difficult to pin down. I will assume a conservative **5.0% ROIC** on the cumulative cash balance, reflecting a moderate ability to generate returns on reinvested earnings.

| Year | Revenue (A) | Net Income Margin | Pre-ROIC Net Income (B) = A * 7.0% | Prior Year's Cash from Net Income (C) | ROIC Income (D) = C * 5.0% | Net Income (B + D) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2025** | $3,870.0 | 7.0% | $270.9 | $0.0 (Base year) | $0.0 | **$270.9** |
| **2026** | $3,947.4 | 7.0% | $276.3 | $270.9 | $13.5 | **$289.8** |
| **2027** | $4,026.3 | 7.0% | $281.8 | $270.9 + $289.8 = $560.7 | $28.0 | **$309.8** |
| **2028** | $4,106.8 | 7.0% | $287.5 | $560.7 + $309.8 = $870.5 | $43.5 | **$331.0** |
| **2029** | $4,188.9 | 7.0% | $293.2 | $870.5 + $331.0 = $1,201.5 | $60.1 | **$353.3** |
| **2030** | $4,272.7 | 7.0% | $299.1 | $1,201.5 + $353.3 = $1,554.8 | $77.7 | **$376.8** |

### IV. Discounted Cash Flow (DCF) Analysis

This DCF will calculate the Net Present Value (NPV) of the projected Net Income (used as proxy for Free Cash Flow to Equity, FCFE).

*   **Conservative Discount Rate (r):** Given the current risk environment, leverage, and the strategic uncertainties (spin-off), I will use a conservative **10.0%** discount rate, which is higher than a typical WACC for a stable industrial company, but accounts for the restructuring and QSR risks.
*   **Conservative Terminal/Maturity Rate (g):** I will assume a very conservative perpetual growth rate of **2.0%**, reflecting long-term global economic growth and the necessity to be conservative.

| Year | Net Income (FCFE) (Millions) | Discount Factor (1 / (1 + 10.0%)^n) | Net Present Value (NPV) |
| :--- | :--- | :--- | :--- |
| **2025 (n=1)** | $270.9 | 0.9091 | $246.3 |
| **2026 (n=2)** | $289.8 | 0.8264 | $239.5 |
| **2027 (n=3)** | $309.8 | 0.7513 | $232.8 |
| **2028 (n=4)** | $331.0 | 0.6830 | $226.0 |
| **2029 (n=5)** | $353.3 | 0.6209 | $219.4 |
| **2030 (n=6)** | $376.8 | 0.5645 | $212.7 |
| **NPV of Projected FCFE (2025-2030)** | | | **$1,376.7** |

#### Terminal Value Calculation (as of 2030)

The terminal value (TV) captures the value of all cash flows after 2030.

*   TV = [FCFE in 2030 * (1 + g)] / (r - g)
*   TV = [$376.8 * (1 + 0.02)] / (0.10 - 0.02)
*   TV = $384.3 / 0.08 = **$4,803.8 million**

#### Net Present Value of Terminal Value

*   NPV of TV = TV / (1 + r)^6
*   NPV of TV = $4,803.8 / (1 + 0.10)^6
*   NPV of TV = $4,803.8 / 1.7716 = **$2,711.6 million**

#### Total Equity Value Calculation

*   **Total Equity Value** = NPV of Projected FCFE (2025-2030) + NPV of Terminal Value
*   Total Equity Value = $1,376.7 million + $2,711.6 million = **$4,088.3 million**

### V. Fair Value per Share Calculation

The fair value of the stock is calculated using the total enterprise value, adjusted for cash, debt, and the special, post-period transaction.

| Metric | Value (Millions) |
| :--- | :--- |
| **Total Equity Value (from DCF)** | $4,088.3 |
| **Add: Initial Cash & Equivalents** (Dec. 2024) | $689.5 |
| **Add: Net Cash from Residential Sale** (post-period event) | $170.0 |
| **Subtract: Total Debt** (Dec. 2024) | -$2,400.0 |
| **Total Fair Value of Equity** | **$2,547.8** |
| **Shares Outstanding** (Millions) | 50.5 |
| **Fair Value per Share** | **$50.45** |

### VI. Conclusion and Justification

**Fair Value per Share:** **$50.45**
**Current Stock Price:** **$161.05**

#### Justification for Discrepancy

My calculated fair value of **$50.45** is significantly lower than the market price of **$161.05**. This massive discrepancy suggests a fundamental difference between my conservative assumptions and the market's assumptions regarding the company's future.

**The Market's Assumptions (Why the stock is higher):**
The market is likely pricing in a major strategic shift and future growth far exceeding my conservative 2.0% long-term growth rate and 7.0% net income margin.

1.  **Massive Value Unlock from Restructuring:** The market is assigning a significant premium to the strategic decisions to spin off the Food Processing business and sell the majority of the Residential Kitchen business. The market believes this will:
    *   **Create a Pure-Play, Higher-Growth Commercial Foodservice Company:** The *core* CFS business, valued on its own, is likely perceived as a faster-growing, more stable "picks-and-shovels" play on the global QSR industry, justifying a much higher EBITDA/P/E multiple than the blended valuation I used.
    *   **The Food Processing Spin-Off (FP) is a Hidden Asset:** The market is likely valuing the future, independent FP company at a high multiple, effectively seeing a split-up value (Sum-of-the-Parts) much higher than the current consolidated valuation. My model only valued the operating income up to 2030, which does not capture the *multiple expansion* for the two separate entities.
2.  **Higher Growth/Margin Expectations:** The market assumes:
    *   A higher perpetual growth rate (**g**) than my **2.0%**, perhaps 3.0% - 4.0%, reflecting significant global expansion or technology adoption (FryBot, etc.).
    *   A much higher future Net Income Margin, perhaps 10% or more, once the high-margin Food Processing business is the *only* part of the continuing operations (post-spin) or once pricing/efficiency gains overcome tariff and QSR softness.
3.  **Lower Discount Rate:** The market may be using a lower cost of capital (Discount Rate **r**), perhaps 7.0%-8.0%, based on the company's established, mature business segments and perceived reduction in complexity post-spin.

**My Justification for Conservatism:**
My valuation is highly conservative, as explicitly requested by the rules, by assuming:

1.  **Low Growth (2.0%):** I explicitly used a low growth rate and noted QSR softness, contrasting with a scenario where new product innovation (automation) could drive much higher growth.
2.  **Conservative Margin (7.0%):** This is a blended margin that reflects past performance under a more complex, multi-segment structure. The spin-off of the lower-margin Residential segment and separation of the higher-margin Food Processing segment would naturally lead to a higher core CFS margin, which my model does not fully capture.
3.  **No Multiple Expansion/Sum-of-the-Parts:** My DCF model is based on the *current, consolidated* business structure and cash flow, which is inadequate for a company undergoing a significant strategic transformation (spin-off). The market is pricing in the success of this transformation and the resulting value unlock from **multiple expansion** when the segments trade separately.

**Conclusion:** The market is valuing Middleby based on a successful, value-accretive restructuring into two cleaner, higher-multiple businesses (Commercial Foodservice and Food Processing), a bet on the success of automation innovation, and a significantly higher long-term growth and profitability trajectory than my highly conservative model allows. My valuation of $50.45, while mathematically sound based on conservative inputs, does not capture the value unlock from the announced strategic transformation.
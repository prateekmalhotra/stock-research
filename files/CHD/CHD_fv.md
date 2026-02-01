This valuation of Church & Dwight Co., Inc. (CHD) stock is conducted using a Discounted Cash Flow (DCF) model based on financial data derived exclusively from SEC filings and management guidance.

All figures are in millions of USD, except where noted.

---

## 1. Establishment of Financial Base & Inputs

The valuation uses the most recent full-year financial data available as the base year (Fiscal Year 2025).

| Financial Metric | Value (USD Millions) | Source/Notes |
| :--- | :--- | :--- |
| **Total Cash & Cash Equivalents (12/31/2025)** | \$409.0 | SEC Filings Snippets |
| **Total Debt (12/31/2025)** | \$2,200.0 | SEC Filings Snippets (Treated as \$2.2 billion) |
| **Net Sales (2025)** | \$6,203.2 | SEC Filings Snippets |
| **Net Income (2025)** | \$736.8 | SEC Filings Snippets |
| **Weighted Avg. Diluted Shares Outstanding (2025)** | 244.3 million | SEC Filings Snippets (from Step 2 search) |
| **Current Stock Price** | \$91.96 | Latest quoted market price (from Step 2 search) |

**Base Year Net Income Margin (2025):**
$$
\text{Net Income Margin} = \text{Net Income} / \text{Net Sales} = \$736.8 \text{M} / \$6,203.2 \text{M} \approx 11.88\%
$$

---

## 2. Business Engine and Conservative Future Assumptions

The Church & Dwight business engine is built on:
1.  **"Power Brands" Growth & Innovation:** The strategy is to drive growth through a select portfolio of high-performing brands (Arm & Hammer, Hero, Therabreath, etc.) supported by continued innovation.
2.  **International Expansion:** The International segment has shown strong organic sales growth, which will be a key driver.
3.  **Margin Expansion:** Management commentary indicates a focus on improved productivity and product mix (e.g., higher-margin products), leading to consistent adjusted gross margin expansion (e.g., +90 basis points in Q4 2025).
4.  **Strategic Acquisitions & Divestitures:** The recent divestiture of the lower-growth Vitamin and Mineral Supplement (VMS) business allows for greater focus and should lead to higher *quality* organic growth in the future.

### Revenue Projections (2026 - 2030)

Management has guided for 3% to 4% volume-driven organic sales growth for 2026. The long-term category growth rate has historically been around 3%.

**Assumption:** A conservative, stable organic growth rate of **3.5%** per year is used for the entire projection period (2026-2030), representing the mid-point of guidance and slightly above historical category growth, justified by the renewed focus after the VMS divestiture.

| Year | Net Sales (USD Millions) | Calculation | Rationale |
| :--- | :--- | :--- | :--- |
| **2025 (Base)** | \$6,203.2 | N/A | Full Year Net Sales |
| **2026** | \$6,420.3 | \$6,203.2 * (1 + 0.035) | Conservative Organic Growth (3.5%) |
| **2027** | \$6,644.0 | \$6,420.3 * (1 + 0.035) | Conservative Organic Growth (3.5%) |
| **2028** | \$6,876.1 | \$6,644.0 * (1 + 0.035) | Conservative Organic Growth (3.5%) |
| **2029** | \$7,117.3 | \$6,876.1 * (1 + 0.035) | Conservative Organic Growth (3.5%) |
| **2030** | \$7,366.9 | \$7,117.3 * (1 + 0.035) | Conservative Organic Growth (3.5%) |

### Net Income Projections (2026 - 2030)

Management has guided for 5%-8% EPS growth in 2026 (from Step 1 search), which is higher than the revenue growth, implying margin expansion and/or share count reduction.

**Assumption (Margin):** To be conservative and capture the effect of margin expansion and operating leverage due to an improved product mix (post-VMS sale) and productivity, the Net Income Margin will increase by a very modest **0.05%** per year (5 basis points).

| Year | Net Income Margin | Net Sales | NI from Operations | Additional Income (ROIC) | Total Net Income (USD Millions) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2025 (Base)** | 11.88% | \$6,203.2 | \$736.8 | \$0.0 | \$736.8 |
| **2026** | 11.93% | \$6,420.3 | \$765.1 | \$73.7 | **\$838.8** |
| **2027** | 11.98% | \$6,644.0 | \$796.0 | \$83.9 | **\$880.0** |
| **2028** | 12.03% | \$6,876.1 | \$827.2 | \$88.0 | **\$915.2** |
| **2029** | 12.08% | \$7,117.3 | \$859.6 | \$91.5 | **\$951.1** |
| **2030** | 12.13% | \$7,366.9 | \$893.7 | \$95.1 | **\$988.8** |

### Additional Income from Reinvested Net Income (ROIC)

The rule states to assume net income for each year goes straight into cash for the next year, then get additional income from a reasonable ROIC on the *previous* year's net income.

**Assumption (ROIC):** As a conservative but reasonable rate for an established consumer staples company focused on accretive acquisitions, a **10.0%** Return on Invested Capital (ROIC) is used for the additional income calculation.

$$
\text{Additional Income}_{\text{N}} = \text{Net Income}_{\text{N-1}} * \text{ROIC (10.0%)}
$$
*Example (2026):* $\$736.8 \text{M} * 10.0\% = \$73.7 \text{M}$

---

## 3. Discounted Cash Flow Analysis

### Discount Rate (WACC)

**Assumption (Discount Rate):** For a stable consumer staple business with a moderate debt profile, a conservative (high) discount rate is warranted to reflect the risk of the projections. A **7.5%** discount rate is chosen as a conservative but reasonable WACC estimate.

### Terminal Value (Maturity Rate)

The Terminal Value represents the cash flow capitalized in perpetuity after the projection period.

**Assumption (Maturity Rate):** A conservative long-term growth rate of **2.0%** is used, reflecting a conservative perpetual growth rate below the projected sales growth and long-term US GDP/inflation rate.

$$
\text{Terminal Value} = \frac{\text{Cash Flow}_{\text{2030}} * (1 + \text{Maturity Rate})}{\text{Discount Rate} - \text{Maturity Rate}}
$$
$$
\text{Terminal Value} = \frac{\$988.8 \text{M} * (1 + 0.020)}{0.075 - 0.020} = \frac{\$1,008.6 \text{M}}{0.055} = \$18,338.2 \text{M}
$$

### Net Present Value (NPV) Calculation

The Net Income for each year is treated as the projected Cash Flow for the purpose of this DCF.

| Year (N) | Cash Flow (NI) (USD Millions) | Discount Factor $\left(1 / (1+0.075)^{\text{N}}\right)$ | Present Value (USD Millions) |
| :--- | :--- | :--- | :--- |
| **2026 (N=1)** | \$838.8 | 0.9302 | \$780.3 |
| **2027 (N=2)** | \$880.0 | 0.8653 | \$761.3 |
| **2028 (N=3)** | \$915.2 | 0.8050 | \$736.9 |
| **2029 (N=4)** | \$951.1 | 0.7489 | \$712.5 |
| **2030 (N=5)** | \$988.8 | 0.6966 | \$688.5 |
| **Terminal Value** | \$18,338.2 | 0.6966 | \$12,773.7 |
| | | **Total NPV** | **\$16,453.2** |

The Net Present Value (NPV) of all projected future cash flows is **\$16,453.2 million**.

---

## 4. Fair Value Calculation

The Fair Value of the Equity is calculated by taking the NPV of future cash flows and adjusting for the current balance sheet items.

$$
\text{Fair Value of Equity} = \text{Total NPV} + \text{Cash} - \text{Debt}
$$

$$
\text{Fair Value of Equity} = \$16,453.2 \text{M} + \$409.0 \text{M} - \$2,200.0 \text{M} = \mathbf{\$14,662.2 \text{M}}
$$

**Fair Value Per Share**

$$
\text{Fair Value Per Share} = \text{Fair Value of Equity} / \text{Shares Outstanding}
$$
$$
\text{Fair Value Per Share} = \$14,662.2 \text{M} / 244.3 \text{M shares} = \mathbf{\$60.00 \text{ per share}}
$$

---

## 5. Justification and Market Comparison

| Metric | Valuation Result | Market Price | Difference |
| :--- | :--- | :--- | :--- |
| **Fair Value Per Share** | \$60.00 | \$91.96 | -34.75% |

The calculated Fair Value of **\$60.00** per share is significantly lower (a 34.75% discount) than the current market price of **\$91.96** per share.

### Justification of Discrepancy

The large discrepancy indicates that the market is making more aggressive future assumptions than the conservative assumptions used in this DCF model.

**The Market's Implicit Assumptions (compared to my conservative model):**

| Valuation Metric | My Conservative Assumption | Market's Implicit Assumption | Justification for Market's View |
| :--- | :--- | :--- | :--- |
| **Long-Term Growth (Maturity Rate)** | 2.0% | ~3.0% - 3.5% | The market is likely pricing in a higher perpetual growth rate based on CHD's proven ability to execute accretive M&A and sustain market share gains, especially with the VMS business (Vitamin and Mineral Supplement) being exited, which improves future organic quality. |
| **Discount Rate (WACC)** | 7.5% | ~6.5% - 7.0% | As a stable, recession-resistant consumer staple company, many investors view CHD as a lower-risk investment, thus justifying a lower cost of capital (WACC) than the conservative 7.5% used here. |
| **ROIC/Reinvestment Return** | 10.0% | ~12.0% - 15.0% | The market expects the company to generate a higher return on its retained earnings and capital projects (M&A and organic) than the conservative 10.0% used in this model, reflecting management's historical track record of successful acquisitions. |
| **Organic Revenue Growth (2026-2030)** | 3.5% | ~4.0% - 5.0% | The market is pricing in the top-end of or exceeding the management's 3-4% organic growth guidance, believing that the focus on high-growth brands (Hero, Therabreath, International) will accelerate growth beyond the long-term category average. |

**Conclusion on Valuation vs. Market:**

My valuation is highly conservative, specifically due to the conservative assumptions on the perpetual growth rate (2.0%) and the discount rate (7.5%). If I were to adjust the model to use the market's likely implicit assumptions (e.g., a **3.0%** Maturity Rate and a **7.0%** Discount Rate), the Fair Value would increase significantly:

*   **Adjusted Terminal Value:** $\frac{\$988.8 \text{M} * (1 + 0.030)}{0.070 - 0.030} = \frac{\$1,018.5 \text{M}}{0.040} = \$25,462.5 \text{M}$
*   **New Total NPV:** $\approx \$787.2 \text{M} + \$776.6 \text{M} + \$752.4 \text{M} + \$729.8 \text{M} + (\$698.8 \text{M} + \$17,823.1 \text{M}) = \$20,567.9 \text{M}$
*   **New Fair Value Per Share:** $(\$20,567.9 \text{M} + \$409.0 \text{M} - \$2,200.0 \text{M}) / 244.3 \text{M shares} \approx \mathbf{\$76.01 \text{ per share}}$

While this adjusted calculation is closer, it shows that the market is still anticipating higher-than-average, high-quality growth and lower risk for CHD, likely due to the "flight to quality" and brand premium typical for leading consumer staple companies. The **\$60.00** fair value, being derived from highly conservative assumptions on all key inputs, suggests that at the current price of \$91.96, the stock has very little margin of safety based on a conservative DCF model.

---

### Final Calculated Fair Value

**Fair Value Per Share: \$60.00**
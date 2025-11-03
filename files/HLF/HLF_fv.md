This valuation of Herbalife Ltd. (HLF) is performed using a Discounted Cash Flow (DCF) model, where Net Income is used as a proxy for free cash flow to equity, based on the provided rules. All financial figures are in millions of USD unless otherwise noted.

## I. Initial Financial Data

The data is sourced from Herbalife's SEC filings and earnings call transcripts, primarily the Quarterly Report on Form 10-Q for the quarter ended June 30, 2025, and the associated earnings call transcripts.

| Metric | Value (USD Millions) | Source/Reference Date | Citation |
| :--- | :--- | :--- | :--- |
| **Total Cash & Cash Equivalents** | $320.9$ | June 30, 2025 | |
| **Current Portion of Long-Term Debt** | $168.0$ | June 30, 2025 | |
| **Long-Term Debt (Net of Current Portion)** | $1,973.5$ | June 30, 2025 | |
| **Total Debt** | **$2,141.5** | June 30, 2025 | |
| **Shares Outstanding** | $103.1$ (million) | July 30, 2025 | |
| **Current Stock Price** | $\sim\$8.00$ | (from search) | - |
| **FY 2024 Net Sales (Base Revenue)** | $5,000.0$ | FY 2024 | |

## II. Business Engine and Projection Assumptions

Herbalife's business is currently in a challenging turnaround phase, transitioning from 12 quarters of sales decline. The core business engine is driven by the volume of products sold through its network of independent distributors.

**A. Revenue Projection (2025 - 2030)**

The projection must be conservative, but acknowledge the recent positive trends and management's guidance.

*   **Key Driver:** Management has noted a return to positive new distributor growth (up 14% to 16% year-over-year in Q3 2024 and Q1 2025), which is critical for future sales growth.
*   **Management Guidance (FY 2025):** Constant currency net sales growth is expected to be in the range of $0.5\%$ to $5.5\%$.
*   **Assumption:** We will use the *low end* of the constant currency growth guidance for the initial year and a conservatively declining growth rate thereafter. The persistent foreign exchange (FX) headwinds and volume declines in key markets will temper the overall reported sales growth, even as new distributor counts rise.

| Year | Revenue Growth Assumption (Constant Currency) | FX/Price Headwind | Projected Reported Revenue Growth | Projected Revenue (USD Millions) |
| :--- | :--- | :--- | :--- | :--- |
| **FY 2024** | Base | - | - | $5,000.0$ |
| **2025** | $+0.5\%$ (Low-end Guidance) | $-1.5\%$ | $-1.0\%$ | $4,950.0$ |
| **2026** | $+0.25\%$ | $-1.5\%$ | $-1.25\%$ | $4,887.0$ |
| **2027** | $0.0\%$ | $-1.0\%$ | $-1.0\%$ | $4,838.1$ |
| **2028** | $+0.5\%$ | $0.0\%$ | $+0.5\%$ | $4,862.3$ |
| **2029** | $+0.75\%$ | $0.0\%$ | $+0.75\%$ | $4,898.7$ |
| **2030** | $+1.0\%$ | $0.0\%$ | $+1.0\%$ | $4,947.7$ |

*Rationale:* The model assumes the positive trend in new distributors leads to a moderate recovery in constant currency sales by 2028-2030. However, a significant FX headwind is applied in the near term (2025-2027), which management has consistently highlighted as a major detractor from reported sales. The initial years show a slight reported decline, as the business is still stabilizing.

**B. Margin and ROIC Assumptions**

*   **Net Income Margin:** Q2 2025 and Q3 2024 Net Income margins were approximately $3.8\%$ on net sales. Management is focused on cost savings and margin improvement (Adjusted EBITDA margin increased to $13.5\%$ in Q1 2025).
    *   **Assumption:** We use a conservative, steady **$3.5\%$ Net Income Margin** across the projection period, slightly below the recent reported results to buffer against operational and currency risks.
*   **Return on Invested Capital (ROIC):** Herbalife has negative shareholders' equity, which complicates a traditional ROIC calculation.
    *   **Assumption:** As per instructions, we use a conservative but reasonable positive ROIC of $\mathbf{4.0\%}$.

**C. DCF Terminal and Discount Rates**

*   **Maturity (Terminal) Rate (g):** This is the long-term, conservative growth rate for perpetual cash flows.
    *   **Assumption:** $\mathbf{1.0\%}$ (A very conservative rate, slightly below global GDP/inflation, reflecting the maturity and regulatory risks of the multi-level marketing industry).
*   **Discount Rate (r):** This reflects the risk of the cash flow. Herbalife carries significant debt, and the business model faces high regulatory scrutiny and market skepticism.
    *   **Assumption:** $\mathbf{10.0\%}$ (A conservative rate well above the average market return, reflecting the high financial leverage and industry-specific risks).

## III. Discounted Cash Flow (DCF) Calculation

The Net Income for each year is calculated as:
$$
\text{Net Income}_n = (\text{Projected Revenue}_n \times \text{Net Income Margin}) + (\text{Net Income}_{n-1} \times \text{ROIC})
$$

| Year (n) | Projected Revenue (A) | Net Income Margin (B) | Base Net Income (A * B) (C) | ROIC Income (D) | Total Net Income (C+D) (E) | Discount Factor ($\frac{1}{(1+10\%)^n}$) (F) | Present Value (E * F) (G) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Base** | $5,000.0$ | $3.5\%$ | $175.0$ (FY24 est.) | - | - | - | - |
| **2025** | $4,950.0$ | $3.5\%$ | $173.25$ | $175.0 \times 4.0\% = 7.00$ | $180.25$ | $0.909$ | $163.85$ |
| **2026** | $4,887.0$ | $3.5\%$ | $171.05$ | $180.25 \times 4.0\% = 7.21$ | $178.26$ | $0.826$ | $147.20$ |
| **2027** | $4,838.1$ | $3.5\%$ | $169.33$ | $178.26 \times 4.0\% = 7.13$ | $176.46$ | $0.751$ | $132.50$ |
| **2028** | $4,862.3$ | $3.5\%$ | $170.18$ | $176.46 \times 4.0\% = 7.06$ | $177.24$ | $0.683$ | $121.05$ |
| **2029** | $4,898.7$ | $3.5\%$ | $171.45$ | $177.24 \times 4.0\% = 7.09$ | $178.54$ | $0.621$ | $110.87$ |
| **2030** | $4,947.7$ | $3.5\%$ | $173.17$ | $178.54 \times 4.0\% = 7.14$ | $180.31$ | $0.564$ | $101.65$ |

**Total Net Present Value (NPV) of Forecasted Cash Flows (2025-2030):**
$$
\text{NPV}_{\text{Forecast}} = \$163.85 + \$147.20 + \$132.50 + \$121.05 + \$110.87 + \$101.65 = \mathbf{\$777.12 \text{ million}}
$$

**Terminal Value Calculation (2030):**
The terminal value assumes perpetual growth at the maturity rate after 2030.
$$
\text{Terminal Value}_{2030} = \frac{\text{Cash Flow}_{2030} \times (1+g)}{r - g} = \frac{\$180.31 \times (1+1.0\%)}{10.0\% - 1.0\%} = \frac{\$182.11}{\text{0.09}} = \$2,023.44 \text{ million}
$$
**Terminal Value NPV:**
$$
\text{Terminal Value NPV} = \frac{\text{Terminal Value}_{2030}}{(1+r)^6} = \frac{\$2,023.44}{(1+10\%)^6} = \$2,023.44 \times 0.564 = \mathbf{\$1,141.17 \text{ million}}
$$

**Total Equity Value:**
$$
\text{Total Equity Value} = \text{Cash} + \text{NPV}_{\text{Forecast}} + \text{Terminal Value NPV} - \text{Total Debt}
$$
$$
\text{Total Equity Value} = \$320.9 + \$777.12 + \$1,141.17 - \$2,141.5 = \mathbf{\$97.69 \text{ million}}
$$

## IV. Fair Value and Conclusion

**Fair Value per Share:**
$$
\text{Fair Value per Share} = \frac{\text{Total Equity Value}}{\text{Shares Outstanding}}
$$
$$
\text{Fair Value per Share} = \frac{\$97.69 \text{ million}}{103.1 \text{ million shares}} \approx \mathbf{\$0.95} \text{ per share}
$$

| Metric | Value |
| :--- | :--- |
| **Calculated Fair Value per Share** | **\$0.95** |
| **Current Market Value per Share** | $\sim\$8.00$ |

## V. Justification and Market Comparison

**The calculated Fair Value of \$0.95 is approximately $\mathbf{88\%}$ lower than the current market value of $\mathbf{\$8.00}$ per share.**

### Justification for the Discrepancy

The large difference indicates that the market is making significantly more optimistic assumptions about the company's future cash flows than this conservative, fundamentally-driven DCF model.

1.  **Market Assumption on Future Growth (Revenue/Profitability):**
    *   **Our Assumption:** We use a very conservative growth profile: a near-flat reported revenue for 2025-2027 and a modest $1.0\%$ maturity rate, reflecting significant FX headwinds and the fragility of the new distributor growth trend.
    *   **Market Assumption:** The market likely believes the recent turnaround in new distributor growth will lead to a **much faster and more substantial re-acceleration of reported revenue and profit growth** in the near-term (2025-2028). The market may be projecting constant currency growth closer to $5\%+$ annually, and/or assumes FX headwinds will diminish quickly, resulting in reported sales growth of $3-5\%$ or more.

2.  **Market Assumption on Risk/Discount Rate:**
    *   **Our Assumption:** A high discount rate ($\mathbf{10.0\%}$) is used to account for high leverage, regulatory risk, and the inherent volatility of the multi-level marketing model.
    *   **Market Assumption:** A discount rate of **$7.0\% - 8.0\%$** would significantly increase the NPV of future cash flows. The market may be signaling that it trusts management's debt reduction plan (target $1B$ reduction over 4-5 years) and cost-cutting initiatives, thereby seeing the company as a lower-risk investment on the path to becoming a more stable, mature consumer health company.

3.  **Market Assumption on Terminal Value:**
    *   **Our Assumption:** A very conservative terminal growth rate ($\mathbf{1.0\%}$) is used, contributing only $\$1,141.17$ million to the valuation.
    *   **Market Assumption:** A small change in the terminal growth rate has a massive impact on the valuation. For the current market price of $\$8.00$ to be justified (implying a total equity value of $\sim\$824.8$ million, and a $\text{NPV}_{\text{Forecast}} + \text{Terminal Value NPV} \approx \$2.64$ billion), the market must be assuming a much higher perpetual growth rate, perhaps $\mathbf{3.0\%}$ or more, which would represent a belief that the "Herbalife One" platform and new distributor engagement will lead to a successful, global, long-term growth story.

**Conclusion on Fair Value:**

The market is pricing Herbalife as a turnaround story that will deliver significant and sustainable future growth, with a lower-than-assumed risk profile. The valuation of **\$0.95 per share** is the result of a **highly conservative approach** that prioritizes the company's high debt load and historic lack of consistent growth, while conservatively acknowledging management's guidance and turnaround efforts with a modest Net Income Margin and slow growth. The price discrepancy suggests the market has factored in the success of the multi-year transformation program and a significant re-rating of the company's long-term growth prospects, which this model views as an overly aggressive projection given the historical volatility and structural business risks.
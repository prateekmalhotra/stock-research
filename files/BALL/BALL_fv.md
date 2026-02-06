## Valuation of Ball Corporation (BALL) Stock

This valuation is based on a Discounted Cash Flow (DCF) model using a conservative business engine built upon Ball Corporation's latest available financial data and management guidance.

All financial data used for the starting position is derived from the Unaudited Condensed Consolidated Balance Sheets as of September 30, 2025, and reported full-year 2025 results, which exclude the divested aerospace business to reflect the continuing operations.

---

### Step 1: Initial Financial Data (As of September 30, 2025)

The base financial figures are derived from the Unaudited Condensed Consolidated Balance Sheets as of September 30, 2025, and the shares outstanding as of October 31, 2025.

| Metric | Value (in millions USD) | Source/Notes |
| :--- | :--- | :--- |
| **Total Cash & Cash Equivalents** | **568** | Q3 2025 10-Q (Cash and cash equivalents) |
| Short-term Debt & Current Portion of LT Debt | 344 | Q3 2025 10-Q |
| Long-term Debt | 6,864 | Q3 2025 10-Q |
| **Total Debt** | **7,208** | Sum of short-term and long-term debt |
| **Shares Outstanding** | **267.99 million** | Q3 2025 10-Q (Outstanding at October 31, 2025) |
| **2025 Net Sales (Base Revenue)** | **13,160** | FY 2025 Net Sales (excluding aerospace) |
| **2025 Net Income (Base Cash Flow)** | **912** | FY 2025 GAAP Net Earnings Attributable to Ball Corporation |

---

### Step 2: Business Engine and Revenue Projections (2025-2030)

Ball Corporation's business engine, post-divestiture of the aerospace business, is focused purely on **aluminum packaging** (beverage, personal care, and household products). The key drivers for revenue growth are:
1.  **Volume Growth (Shipments):** Driven by the global shift from plastic to sustainable aluminum packaging (due to recycling/sustainability trends).
2.  **Price/Mix:** Driven by contractual cost pass-throughs and favorable product mix shifts (e.g., smaller cans, specialty cans).

Management has clearly guided a long-term financial algorithm targeting **10%+ comparable diluted EPS growth**. While this is an EPS target, it suggests confidence in revenue growth and/or margin expansion. I will build a conservative model that supports this EPS growth target via conservative revenue growth and modest margin improvement.

**Conservative Revenue Assumptions:**

*   **2026:** Revenue growth is projected based on a blend of volume and price. Global packaging shipments grew 4.1% in 2025. I will assume a conservative **3.5%** volume increase and a **1.0%** pricing/mix benefit, resulting in **4.5%** total revenue growth.
*   **2027 - 2030:** I will conservatively taper the growth rate. The tailwind from aluminum sustainability is strong but capital expenditure for new capacity is leveling off. I will assume a continued strong **3.0%** revenue growth for 2027, followed by a steady **2.5%** growth rate thereafter. This is conservative for a global leader operating in a secular growth industry.

| Year | Revenue Growth Assumption | Projected Net Sales (in millions USD) |
| :--- | :--- | :--- |
| **2025 (Base)** | N/A | 13,160 |
| **2026** | 4.50% | 13,752 |
| **2027** | 3.00% | 14,165 |
| **2028** | 2.50% | 14,519 |
| **2029** | 2.50% | 14,883 |
| **2030** | 2.50% | 15,255 |

---

### Step 3: Margin and Net Income Projections (2025-2030)

The base Net Income Margin for 2025 (GAAP Net Income / Sales) is 6.93% (\$912M / \$13,160M).

Management commentary emphasizes "operational excellence" and a "streamlined operating model" [cite: 2, 6, *from step 2 search*], suggesting an ability to improve efficiency and manage costs better than in the past, leading to margin expansion. Furthermore, the 10%+ EPS growth target implies that net income growth will outpace revenue growth, which means margins must expand or share count must decrease significantly (which it has, to 268M shares).

**Conservative Margin Assumptions:**

*   I will assume a conservative, steady margin expansion from the 2025 base of 6.93% towards a long-term target of **7.5%**, reflecting operating leverage, successful cost-pass-throughs, and structural improvements from the divestiture.

| Year | Projected Net Sales (in millions USD) | Projected Net Income Margin | Net Income from Operations (in millions USD) |
| :--- | :--- | :--- | :--- |
| **2025 (Base)** | 13,160 | 6.93% | 912 |
| **2026** | 13,752 | 7.00% | 963 |
| **2027** | 14,165 | 7.10% | 1,006 |
| **2028** | 14,519 | 7.20% | 1,045 |
| **2029** | 14,883 | 7.30% | 1,086 |
| **2030** | 15,255 | 7.40% | 1,129 |

#### Incorporating Return on Invested Capital (ROIC)

The rule states: *Net income for next year = net income from that year based on reasonable assumptions + ROIC from net income got from previous year.* The projected net income is assumed to go straight into cash.

**ROIC Assumption Justification:** The company generated a record **\$956 million** in adjusted free cash flow in 2025. While past ROIC can be complex to calculate accurately due to historical restructuring and divestitures, a highly conservative and reasonable, positive ROIC on liquid assets/cash for a strong, mature business is necessary. I will assume a conservative **ROIC of 2.0%** on the accumulated net income/cash of the previous year.

| Year | Net Income from Operations (A) | Prior Year Accumulated Cash (B) (a) | ROIC (2.0% * B) (C) | Total Net Income (A + C) (in millions USD) | Accumulated Cash End of Year (b) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2025 (Base)** | 912 | 0 | 0 | **912** | 912 |
| **2026** | 963 | 912 | 18 | **981** | 1,893 |
| **2027** | 1,006 | 1,893 | 38 | **1,044** | 2,937 |
| **2028** | 1,045 | 2,937 | 59 | **1,104** | 4,041 |
| **2029** | 1,086 | 4,041 | 81 | **1,167** | 5,208 |
| **2030** | 1,129 | 5,208 | 104 | **1,233** | 6,441 |
*(a) Accumulated cash starts at \$0 for 2025 for simplicity in the model. (b) For the purpose of the DCF, this accumulated cash is not used, as the DCF discounts future cash flow to the firm. We are using Net Income as a proxy for unlevered cash flow, where the total is then discounted.*

---

### Step 4: Discounted Cash Flow (DCF) Analysis

#### Discount Rate (WACC) Justification

For a conservative and reasonable WACC (Discount Rate), I will select **8.0%**.
*   The company is a global, mature, stable company (Beta close to 1.0).
*   The risk-free rate is assumed to be a conservative 4.0%.
*   The equity risk premium is conservatively assumed to be 5.0%.
*   WACC = Cost of Equity * (E/V) + Cost of Debt * (D/V) * (1-Tax Rate).
*   A blended, conservative figure of **8.0%** reflects a stable, low-beta industry (packaging) but is high enough to account for global operational risks and commodity price volatility.

#### Maturity Rate (Terminal Growth Rate) Justification

The maturity rate represents the conservative long-term growth rate of the business after the explicit forecast period.
*   Given the global industry shift toward aluminum (a secular tailwind) and the company's leading market position, a terminal growth rate above the U.S. GDP/inflation rate is justifiable, but for a **very conservative** model:
*   I will assume a conservative terminal growth rate of **1.5%**. This is well below the long-term inflation average and management's 10%+ EPS growth algorithm, embedding significant conservatism.

#### Net Present Value (NPV) Calculation

The Total Net Income is used as the proxy for future cash flows.

| Year | Total Net Income (in millions USD) | Discount Factor (8.0%) | Present Value (in millions USD) |
| :--- | :--- | :--- | :--- |
| **2026** | 981 | 0.9259 | 908 |
| **2027** | 1,044 | 0.8573 | 895 |
| **2028** | 1,104 | 0.7938 | 876 |
| **2029** | 1,167 | 0.7350 | 858 |
| **2030** | 1,233 | 0.6806 | 839 |
| **Sum of Projected Cash Flows** | | | **4,376** |

#### Terminal Value Calculation

The terminal value (TV) is calculated using the perpetuity growth formula: TV = [Cash Flow (2030) * (1 + g)] / (WACC - g)

*   TV = [1,233 * (1 + 0.015)] / (0.080 - 0.015)
*   TV = 1,251.495 / 0.065
*   TV = **19,254 million USD**

#### Net Present Value of Terminal Value

The TV is discounted back to the present (end of 2025):

*   NPV of TV = 19,254 * Discount Factor (2030)
*   NPV of TV = 19,254 * 0.6806
*   NPV of TV = **13,105 million USD**

#### Total Enterprise Value (TEV)

*   TEV = Sum of Projected Cash Flows + NPV of Terminal Value
*   TEV = 4,376 million USD + 13,105 million USD
*   TEV = **17,481 million USD**

---

### Step 5: Fair Value of Stock Calculation

The fair value of equity is calculated using the formula:
*   Equity Value = TEV + Cash & Cash Equivalents - Total Debt

| Metric | Value (in millions USD) |
| :--- | :--- |
| Total Enterprise Value (TEV) | 17,481 |
| PLUS: Total Cash & Cash Equivalents | 568 |
| LESS: Total Debt | 7,208 |
| **Fair Value of Equity** | **10,841** |

**Fair Value Per Share**

*   Fair Value Per Share = Fair Value of Equity / Shares Outstanding
*   Fair Value Per Share = 10,841 million USD / 267.99 million shares
*   Fair Value Per Share = **\$40.45**

---

### Final Fair Value and Justification

The conservative DCF analysis yields a **Fair Value per Share of $40.45**.

For comparison, as a proxy to the current value of the stock, a market price of **\$65.00** is assumed for the end of the analysis period (early 2026).

#### **Conclusion and Justification for Difference**

The calculated fair value of **\$40.45** is significantly lower than the assumed market price of **\$65.00**.

The market is making assumptions that are substantially more optimistic than the conservative model built here. The difference of over 60% suggests the market believes one or more of the following will occur:

1.  **Higher Growth/Longer-Term Tailwinds:** The market is likely modeling a faster and more sustained revenue growth rate, perhaps exceeding **4.0%** per year and/or a much higher Terminal Growth Rate (Maturity Rate) than the **1.5%** used here. If the global secular shift to aluminum packaging (driven by sustainability) is more disruptive than anticipated, the market is pricing in accelerated volume and pricing power for Ball.
2.  **Significant Margin Expansion:** The market may be assuming the company's "operational excellence" and streamlined business will lead to a net income margin consistently above **8.5%** (compared to the 7.4% used in the terminal year), or a substantial reduction in interest expense, which would flow directly to Net Income.
3.  **Lower Discount Rate (WACC):** The market, viewing Ball as a high-quality, stable industrial company, may be valuing it with a WACC closer to **7.0%** or even lower. A lower discount rate significantly increases the NPV of the terminal value.
4.  **Value of Buybacks:** The market is heavily factoring in the value creation from the aggressive share repurchase program, which will accelerate the EPS growth (the 10%+ algorithm) faster than the net income growth alone. The **268 million** shares outstanding is already down substantially from previous years, and the market is likely anticipating this trend will continue aggressively.

**Justification for the Conservative Model ($40.45):**

The difference is justified by the mandate to be conservative. The model assumes a **terminal growth rate (1.5%)** that barely covers inflation, essentially valuing the company as a utility-like asset with minimal long-term real growth. While management guides for 10%+ EPS growth, that growth relies on a combination of net income growth and share count reduction. By using a highly conservative revenue growth profile (tapering to 2.5%) and a very modest terminal growth rate, the valuation model is protected from over-optimistic long-term projections. To reach the market price of **\$65.00** with the same debt and cash figures, the implied Terminal Growth Rate would need to be approximately **3.0% - 3.5%**, or the WACC would need to be closer to **6.5% - 7.0%**, or a combination of both, reflecting the market's expectation of stronger and more certain long-term financial performance. The conservative valuation simply reflects a deliberate skepticism toward market-implied growth and profitability that extend over a 20+ year horizon.
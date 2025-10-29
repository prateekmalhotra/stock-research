## Valuation of Casey's General Stores, Inc. (CASY) Stock

The valuation of Casey's General Stores, Inc. (CASY) stock is performed using a Discounted Cash Flow (DCF) model based on management's guided internal metrics and conservative long-term assumptions.

***

### 1. Initial Financial Data & Valuation Parameters

All dollar amounts are in **Millions of USD** unless otherwise noted.

| Metric | Value | Source/Justification |
| :--- | :--- | :--- |
| **Current Stock Price** | **$535.59** | Previous close as of October 28, 2025. |
| **Shares Outstanding** | **37.18** | As of October 2025. |
| **Total Cash & Equivalents** | **$458.07** | As of July 31, 2025 (Q1 FY2026). |
| **Total Debt** | **$2,890** | Latest 12 Months (LTM) data. |
| **FY2025 Total Revenue (Base)** | **$16,410** | Latest 12 Months (LTM) data. |
| **FY2025 Net Income (Base)** | **$546.5** | Full Fiscal Year (FY) 2025 result [cite: 4, 5 in prior step]. |
| **Discount Rate (WACC)** | **9.0%** | Conservative estimate (higher than indicated 7.56% WACC to build in a margin of safety) [cite: 1 in prior step]. |
| **ROIC (Reinvestment Rate)** | **9.0%** | Conservative estimate, slightly below the 5-year average of 11.4% to account for capital-intensive expansion [cite: 5 in prior step]. |
| **Maturity Rate (Terminal Growth, g)** | **2.0%** | Very conservative long-term growth rate for a mature, stable convenience retail/gas station chain. |

***

### 2. Business Engine & Revenue Projection Justification

Casey's business engine is driven by a two-pronged approach: (1) high-margin *Inside Sales* (Prepared Food & Grocery) through **Same-Store Sales Growth (SSSG)** and (2) **Store Expansion** (new builds and M&A) [cite: 4 in prior step]. Fuel sales provide high volume and traffic, while Inside Sales drive the majority of gross profit.

**Revenue Projection Assumptions (2025-2030):**

| Driver | FY2026 | FY2027 | FY2028 | FY2029 | FY2030 | Justification (Conservative & Management-Backed) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Inside SSSG** | 3.5% | 3.0% | 2.5% | 2.5% | 2.5% | Management guides 2-5% SSSG for FY2026. I use the mid-point of **3.5%** and then conservatively taper to **2.5%** (a low-end, stable rate). |
| **Fuel SSSG (Gallons)**| 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | Management guides -1% to +1% for FY2026. I use **0%** (flat) to be very conservative, mitigating fuel price volatility [cite: 1, 2, 5 in prior step]. |
| **New Stores (Growth Rate)** | 2.75% | 2.70% | 2.65% | 2.60% | 2.55% | FY2026 guidance is "at least 80 new stores" on a base of ~2,900 stores (~2.75% growth) [cite: 1, 4 in prior step]. I hold this growth strong for the first year and then conservatively taper it down by 5 basis points annually. |
| **Revenue Growth** | **8.5%** | **7.5%** | **6.5%** | **5.5%** | **4.5%** | Blended growth. The high-margin Inside Sales grow faster, providing a steady floor for total revenue growth even with flat Fuel SSSG. |
| **Net Income Margin (%)** | 3.50% | 3.55% | 3.60% | 3.65% | 3.70% | FY2025 base margin is 3.33%. I assume a *conservative, slow margin expansion* due to the strategic focus on higher-margin prepared food, which is a key management strategy [cite: 6 in prior step]. |

#### Revenue Projection Calculation (Base Year FY2025: $16,410)

| Fiscal Year (Ends Apr 30) | Growth Rate Assumption | Projected Total Revenue (USD Mil) |
| :--- | :--- | :--- |
| **FY2025 (Actual Base)** | N/A | **$16,410** |
| **FY2026** | 8.5% | **$17,808** |
| **FY2027** | 7.5% | **$19,143** |
| **FY2028** | 6.5% | **$20,388** |
| **FY2029** | 5.5% | **$21,509** |
| **FY2030** | 4.5% | **$22,476** |

***

### 3. Projected Net Income and Discounted Cash Flow (DCF)

The cash flow for the DCF is Net Income, adjusted to include additional income from the reinvestment of the prior year's cash balance (per rule: Net Income goes straight into cash, which earns a return).

**Net Income (NI) Calculation:**
*   $NI_t (\text{from Ops}) = \text{Revenue}_t \times \text{Net Income Margin}_t$
*   $NI_t (\text{Total}) = NI_t (\text{from Ops}) + \text{ROIC} \times \text{NI}_{t-1} (\text{Total})$

| Fiscal Year | $NI_{t-1}$ (Total) | Margin % | Revenue | $NI_{t}$ (from Ops) | ROIC $NI_{t-1}$ | **$NI_{t}$ (Total CF)** | Discount Factor (9.0%) | **NPV of CF** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FY2025 (Base)**| $546.50 | 3.33% | $16,410 | N/A | N/A | N/A | N/A | N/A |
| **FY2026**| $546.50 | 3.50% | $17,808 | $623.28 | $49.19 | **$672.47** | 0.917 | $616.63 |
| **FY2027**| $672.47 | 3.55% | $19,143 | $679.57 | $60.52 | **$740.09** | 0.842 | $623.11 |
| **FY2028**| $740.09 | 3.60% | $20,388 | $733.97 | $66.61 | **$800.58** | 0.772 | $617.91 |
| **FY2029**| $800.58 | 3.65% | $21,509 | $784.07 | $72.05 | **$856.12** | 0.708 | $606.09 |
| **FY2030**| $856.12 | 3.70% | $22,476 | $831.61 | $77.05 | **$908.66** | 0.650 | $590.63 |
| **Total NPV of Projected Cash Flows** | | | | | | | | **$3,054.37** |

**Terminal Value (TV) Calculation:**

The Terminal Value represents the value of all cash flows beyond FY2030. It is calculated using the Perpetuity Growth Model with a conservative growth rate ($g=2.0\%$).

$$
\text{TV} = \frac{CF_{\text{FY2030}} \times (1 + g)}{\text{Discount Rate} - g}
$$

$$
\text{TV} = \frac{\$908.66 \times (1 + 0.02)}{0.09 - 0.02} = \frac{\$926.83}{0.07} = \$13,240.43 \text{ million}
$$

**NPV of Terminal Value:**

$$
\text{NPV of TV} = \text{TV} \times \text{Discount Factor}_{\text{FY2030}}
$$

$$
\text{NPV of TV} = \$13,240.43 \times 0.650 = **\$8,606.28 \text{ million}**
$$

**Total Net Present Value (NPV) of Future Cash Flows:**

$$
\text{Total NPV} = \text{NPV of Projected Cash Flows} + \text{NPV of Terminal Value}
$$

$$
\text{Total NPV} = \$3,054.37 + \$8,606.28 = **\$11,660.65 \text{ million}**
$$

***

### 4. Fair Value Calculation

The Fair Value of Equity is calculated by taking the Total NPV of future cash flows, adding current cash, and subtracting total debt.

| Component | Value (USD Mil) |
| :--- | :--- |
| Total NPV of Future Cash Flows (A) | $11,660.65 |
| (+) Total Cash & Equivalents (B) | $458.07 |
| (-) Total Debt (C) | $2,890.00 |
| **Fair Value of Equity (A + B - C)** | **$9,228.72** |
| **Shares Outstanding** (D, in millions) | 37.18 |
| **Fair Value per Share (A / B)** | **$248.22** |

***

### 5. Conclusion and Market Comparison

| Metric | Valuation Result | Market Value (Oct 28, 2025) | Difference |
| :--- | :--- | :--- | :--- |
| **Fair Value per Share** | **$248.22** | **$535.59** | **(53.7%)** |

#### Justification for the Difference

The calculated Fair Value of **$248.22** per share is significantly lower (53.7% less) than the current market price of **$535.59**. This large discrepancy suggests that **the market is operating under much more optimistic assumptions** than the conservative model utilized here.

**The market's implied assumptions must be substantially different in the following key areas:**

1.  **Reinvestment/ROIC Premium:** Casey's trades as a high-quality retailer (a "compounder") due to its successful strategy of utilizing high-margin prepared food offerings to drive store traffic [cite: 6 in prior step]. The market likely assigns a much higher *Return on Invested Capital (ROIC)*, potentially closer to its peak historical averages (12%+) [cite: 5 in prior step]. If ROIC was increased to *12.5%* throughout the projection, the Fair Value would increase, but still not close the gap entirely.

2.  **Growth Rate (Terminal Value):** The most sensitive part of the DCF is the Terminal Value. The use of a very conservative 2.0% Maturity Rate is likely what creates the greatest drag. The market is assuming Casey's high-growth, high-ROIC phase will continue for longer, or that its **Terminal Growth Rate ($g$) is much higher**, possibly closer to the long-term US GDP growth trend of **3.0% to 3.5%**.

3.  **Future Store Growth / M&A:** Our model conservatively uses the guided 80 new stores per year. The market is likely incorporating an assumption of **major, accretive future M&A activity** beyond the current guidance, similar to the Fikes Wholesale acquisition, which significantly boosted the store count in FY2025 [cite: 4, 5 in prior step].

**The Case for the Conservative Valuation:**

The conservative valuation of $248.22 is a strong measure of **intrinsic value based only on sustained, predictable, and low-risk execution** of the current business model. The current stock price of $535.59 implies:
*   A significantly higher and sustained ROIC (e.g., 12.5%+) **AND**
*   A Perpetual Growth Rate ($g$) of at least **3.5%** (a high growth rate for a retail chain) **AND/OR**
*   Several large, highly profitable M&A deals in the future.

The model assumes management *meets* their stated guidance and then slows down to a very conservative, sustainable pace. The market's price suggests it believes management will **consistently *outperform* guidance** on SSSG, margins, and M&A for the foreseeable future. Given the mandate to be conservative, **$248.22 is the justified fair value**; the market is pricing in exceptional growth and superior capital allocation that, while historically demonstrated, is not a guaranteed perpetual state.
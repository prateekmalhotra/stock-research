## Valuation of Organon & Co. (OGN) Stock

This valuation is based on a Discounted Cash Flow (DCF) model using a conservative business engine projection through 2030, followed by a conservative perpetuity growth rate.

### 1. Initial Data and Assumptions

| Metric | Value (in millions USD, unless noted) | Source | Rationale/Assumption |
| :--- | :--- | :--- | :--- |
| **Current Stock Price** | **\$7.39** | Step 1 (Search Result) | For comparison to Fair Value. |
| **Shares Outstanding** | **259.98 million** | Step 1 (Search Result) | Used for calculating Fair Value Per Share. |
| **Total Cash & Equivalents** | **\$574** | 10-K, Dec 31, 2025 | All liquid assets in hand. |
| **Total Debt** | **\$8,640** | 10-K, Dec 31, 2025 | Total debt is based on the most recent annual filing data. |
| **Conservative ROIC** | **7.0%** | Step 2 (Search Result) | Conservative estimate. TTM ROIC was 9.21%-9.42%, but the instruction requires a conservative, positive percentage. |
| **Discount Rate (WACC)** | **8.0%** | Assumed | A conservative rate, higher than the implied WACC of 4.76%-4.78%, to account for high leverage and business model risk. |
| **Maturity/Perpetuity Growth Rate** | **1.0%** | Assumed | A very conservative rate for terminal growth for a mature pharmaceutical company. |

---

### 2. Business Engine and Revenue Projections (2025 - 2030)

Organon's business engine is characterized by a portfolio of **Established Brands** (volume and pricing decline) and **Women's Health** (mixed performance with US Nexplanon headwinds), which are being offset by high-growth categories like **Biosimilars** and new product launches like **Vtama**. The current financial guidance reflects this tension, leading to flat revenue projections in the near term.

#### Revenue Projection Rationale

| Year | Revenue (in millions USD) | Year-over-Year Growth | Rationale (Backing the Business Engine) |
| :--- | :--- | :--- | :--- |
| **2025** | **6,200** | -3.0% (vs. 2024) | Based on management's full-year 2025 guidance. |
| **2026** | **6,200** | 0.0% | Based on management's 2026 guidance for flat revenue (growth drivers offsetting Established Brands decline and Jada divestiture headwind). |
| **2027** | **6,262** | 1.0% | The first year where the expected R&D/supply chain restructuring benefits *might* allow growth drivers (Biosimilars, International Nexplanon, Vtama ramp) to slightly outpace the legacy decline. A modest $62 million increase is conservative. |
| **2028** | **6,387** | 2.0% | Biosimilars and new Women's Health launches gain more traction, leading to a slightly higher, but still conservative, growth rate. |
| **2029** | **6,515** | 2.0% | Continued low-to-mid single-digit growth driven by the "growth drivers" franchise. |
| **2030** | **6,645** | 2.0% | Maintaining a 2.0% conservative growth as the long-term potential of the high-growth segments starts to moderate but still outpaces the decline of legacy products. |

#### Margin Projection Rationale

| Year | Margin Metric | 2025 Actual/Guidance | 2026 Assumption | 2027-2030 Assumption | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Gross Margin** | Adjusted % | 60.1% | 59.1% | 60.0% | Management guided a 75-100 bps decline for 2026. For 2027 and beyond, I assume the planned supply chain separation drives a conservative recovery to 60.0%, below the 2025 level, to reflect ongoing pricing pressure. |
| **Operating Expenses (SG&A + R&D)** | % of Revenue | 44.0% | 43.4% | 42.0% | Calculated from 2025 Adjusted EBITDA Margin (30.7%): 100% - 60.1% GM - 30.7% EBITDA = 9.2% Operating Income. $6,200 Revenue * (1-30.7%) = $4,290 COGS/OpEx. OpEx is the rest. In 2026, I assume OpEx leverage partially offsets the GM drop to keep EBITDA flat. From 2027 onwards, management commentary on cost savings and expense discipline allows a modest reduction. |
| **Net Income Margin** | % | 3.0% | 3.5% | 5.0% | **2025:** Reported Net Income of \$187M / \$6,200M Revenue = 3.0%. **2026:** Assumes a modest improvement from flat revenue and slight operating expense leverage. **2027-2030:** Assumes the interest expense burden remains relatively high, but the overall cost structure improves, leading to a conservative 5.0% long-term net income margin (still far below the $\sim 15\%$ non-GAAP adjusted net margin). |
| **Tax Rate** | % | 25.0% | 25.0% | 25.0% | Conservative, simplifying assumption based on a standard corporate tax rate. |

---

### 3. Projected Net Income and Discounted Cash Flow

The model calculates Net Income for each year, assuming it converts directly to cash. Then, the ROIC on the prior year's cash is added as additional income to arrive at the projected cash flow.

| Metric (in millions USD) | 2025 (Initial) | 2026 | 2027 | 2028 | 2029 | 2030 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **(A) Revenue** | 6,200 | 6,200 | 6,262 | 6,387 | 6,515 | 6,645 |
| **(B) Net Income Margin (%)** | 3.0% | 3.5% | 4.0% | 4.5% | 5.0% | 5.0% |
| **(C) Base Net Income (A * B)** | 187 | 217 | 250 | 287 | 326 | 332 |
| **(D) Prior Year Cash Balance** | 574 (Initial) | 761 | 978 | 1,228 | 1,515 | 1,841 |
| **(E) Income from ROIC (D * 7.0%)** | 40 | 53 | 68 | 86 | 106 | 129 |
| **(F) Total Cash Flow (C + E)** | **227** | **270** | **318** | **373** | **432** | **461** |
| **(G) New Cash Balance (D + F)** | **761** | **978** | **1,228** | **1,515** | **1,841** | **2,302** |
| **Discount Factor (8.0%)** | 0.9259 | 0.8573 | 0.7938 | 0.7350 | 0.6806 | 0.6302 |
| **NPV of Cash Flow (F * DF)** | **210** | **232** | **252** | **274** | **294** | **291** |

**Total Net Present Value (NPV) of Projected Cash Flows (2025-2030):**

$$\text{NPV}_{\text{2025-2030}} = 210 + 232 + 252 + 274 + 294 + 291 = \mathbf{\$1,553 \text{ million}}$$

---

### 4. Terminal Value and Final Valuation

#### Terminal Value Calculation (as of EOY 2030)

We use the 2030 Cash Flow and the Perpetuity Growth Model:

$$\text{Terminal Value}_{\text{2030}} = \frac{\text{Cash Flow}_{\text{2030}} * (1 + \text{Maturity Rate})}{\text{Discount Rate} - \text{Maturity Rate}}$$

$$\text{Terminal Value}_{\text{2030}} = \frac{\$461 \text{ million} * (1 + 0.01)}{0.08 - 0.01} = \frac{\$465.61}{0.07} = \mathbf{\$6,652 \text{ million}}$$

#### Terminal Value Net Present Value (NPV)

The Terminal Value must be discounted back to the present (2025):

$$\text{NPV}_{\text{Terminal}} = \text{Terminal Value}_{\text{2030}} * \text{Discount Factor}_{\text{2030}}$$

$$\text{NPV}_{\text{Terminal}} = \$6,652 \text{ million} * 0.6302 = \mathbf{\$4,192 \text{ million}}$$

#### Total Equity Value

$$\text{Total Equity Value} = \text{NPV}_{\text{2025-2030}} + \text{NPV}_{\text{Terminal}} + \text{Current Cash} - \text{Total Debt}$$

$$\text{Total Equity Value} = \$1,553 \text{ million} + \$4,192 \text{ million} + \$574 \text{ million} - \$8,640 \text{ million}$$

$$\text{Total Equity Value} = \$6,319 \text{ million} - \$8,640 \text{ million} = \mathbf{-\$2,321 \text{ million}}$$

### 5. Fair Value Per Share

$$\text{Fair Value Per Share} = \frac{\text{Total Equity Value}}{\text{Shares Outstanding}}$$

$$\text{Fair Value Per Share} = \frac{-\$2,321 \text{ million}}{259.98 \text{ million}} = \mathbf{-\$8.93}$$

---

### Conclusion and Justification

**Fair Value Per Share: -\$8.93**

**Current Market Price: \$7.39**

#### Justification for the Discrepancy

The calculated fair value of $-\$8.93$ is a significant negative number, which is a stark contrast to the current market price of $\$7.39$. This huge discrepancy is almost entirely due to Organon's enormous **Total Debt** of **\$8.64 billion** relative to the projected cash flow and current cash.

The valuation model is asking: *Does the Net Present Value of Organon's future cash flows, plus its current cash, cover its massive debt load?*

The answer from this conservative model is **No**, by over **\$2.3 billion**.

**Why is my assumption so different from the market?**

The market is making a fundamental assumption that my conservative valuation model explicitly challenges:

1.  **Market Assumption: Deleveraging is Imminent and Assured.** The market is likely assuming that management's priority of debt reduction will be far more successful than modeled, either through:
    *   **Higher-than-modeled Free Cash Flow (FCF) conversion:** My model uses *reported* Net Income (3.0% margin in 2025), which was heavily impacted by non-cash charges (like the goodwill impairment). The market is looking at **Non-GAAP Adjusted Net Income** (\$954 million in 2025) or **Adjusted EBITDA** (\$1.9 billion in 2025), which are substantially higher. The market is effectively using a much higher "cash flow" number, which would allow the company to repay the debt.
    *   **Higher Growth/Margin Expansion:** The market may be projecting stronger-than-modeled growth in the **Biosimilars** and **Vtama** franchises, and a more aggressive and successful cost reduction plan post-2026, leading to a higher terminal growth rate (Perpetuity Rate) and a much larger terminal value.
    *   **Lower Discount Rate:** The market may be using the lower, observed WACC of $\sim 4.75\%$, which would significantly increase the NPV of all future cash flows.

2.  **Model's Conservative Stance:**
    *   **Use of Reported Net Income:** The required use of **Net Income** (instead of a more generous proxy like Free Cash Flow or Adjusted EBITDA) severely punishes the valuation, as the **Reported Net Income** is very low due to amortization and one-time charges/impairments (\$187 million vs. \$954 million Adjusted Net Income in 2025).
    *   **Conservative Growth/Margin:** The model's projected 1.0% to 2.0% revenue growth and slow Net Income margin expansion (to a peak of 5.0%) is likely an understatement of the market's expectation for the high-growth Biosimilar and Women's Health portfolio.
    *   **Conservative Discount Rate:** The $8.0\%$ discount rate is nearly double the observed WACC, which aggressively reduces the Net Present Value of future cash flows.

**Conclusion:** The negative fair value is a direct result of using **reported Net Income** as the cash flow proxy and applying a **conservative discount rate** to a highly leveraged company. For the market to justify the **\$7.39** stock price, it must assume Organon's ability to generate cash flow is much closer to its **Non-GAAP Adjusted Net Income** and that the growth from its high-growth segments (Biosimilars, Vtama) will accelerate its deleveraging process well beyond the next five years.
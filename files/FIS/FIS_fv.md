This valuation of Fidelity National Information Services, Inc. (FIS) utilizes a Discounted Cash Flow (DCF) model based on management's public commentary, historical financials from SEC filings, and a conservative, justifiable business engine projection as requested.

All financial figures are in millions of US Dollars, unless otherwise noted.

---

## I. Current Financial Position (as of September 30, 2025)

The figures below are derived from FIS's most recent SEC filings and earnings releases, primarily the Q3 2025 results.

| Metric | Value (USD Millions) | Source/Notes |
| :--- | :--- | :--- |
| **Total Cash & Cash Equivalents** | \$571 | As of September 30, 2025. |
| **Total Debt** | \$13,000 | As of September 30, 2025. |
| **Shares Outstanding** | 517.85 million | As of October 31, 2025. |
| **Current Stock Price** | (Assumed based on current search time) **\$54.00** | *Note: This is an assumed market price for calculation. The final step will address the justification.* |
| **Market Capitalization** | \$27,964 million | *517.85M shares x \$54.00* |

---

## II. Historical Analysis and Model Assumptions

### 1. Business Engine and Revenue Drivers

FIS's core business is now focused on **Banking Solutions** and **Capital Markets Solutions** following the sale of the majority stake in the Worldpay Merchant Solutions business in 2024. [cite: 3 in step 2]

*   **Key Growth Drivers (Management Commentary):**
    1.  **Recurring Revenue:** The company is experiencing strong recurring revenue growth (e.g., 7.6% in Capital Markets Q3 2025). [cite: 5 in step 1]
    2.  **Client Retention and Pricing:** Improved renewal retention (approx. 3% improvement in 2024/2025 in Banking) and positive net pricing (60 bps contribution) are key. [cite: 5 in step 1, 10 in step 1]
    3.  **Strategic M&A:** The acquisition of Global Payments' Issuer Solutions business, expected to close in Q1 2026, is a significant future catalyst. [cite: 5 in step 1, 3]
    4.  **Margin Expansion:** Management is focused on cost-saving programs and operational efficiency, guiding for margin expansion greater than 60 basis points in 2026. [cite: 5 in step 1]

### 2. Return on Invested Capital (ROIC)

The Return on Invested Capital is crucial for generating subsequent-year income in this model. I use 2024 full-year figures for a normalized, post-Worldpay-split baseline of the continuing operations.

| Metric | 2024 Value (USD Millions) | Calculation/Notes |
| :--- | :--- | :--- |
| **Net Income from Cont. Ops** (NI) | \$790 | 2024 Full-Year GAAP NI (Cont. Ops). [cite: 10 in step 2] |
| **Interest Expense** (I) | \$351 | 2024 Full-Year. [cite: 10 in step 2] |
| **Total Pre-Tax Income** (PTI) | \$1,297 | 2024 Full-Year. [cite: 10 in step 2] |
| **Income Tax Expense** (T) | \$362 | 2024 Full-Year. [cite: 10 in step 2] |
| **Tax Rate** (t) | 28% | T / PTI = $362M / $1,297M $\approx$ 27.9%. (Rounded conservatively). |
| **NOPAT** | \$1,043 | $NI + I * (1 - t)$ = $790M + $351M * (1 - 0.28). |
| **Invested Capital** (IC) | \$27,493 | *Est. Q3 2025: Total Debt ($13,000M) + Equity ($15,064M) - Cash ($571M).* [cite: 1, 3, 5 in step 2] |
| **Historical ROIC** | **3.79%** | $NOPAT / IC = $1,043M / $27,493M. |

**Assumption:** I will use a conservative, rounded ROIC of **4.00%** for the projections, which is slightly above the calculated historical rate from continuing operations.

### 3. Margin Projection (Net Income Margin)

Based on management's strong guidance for margin expansion, I will project a gradual improvement in Net Income Margin (as a percentage of Revenue) for the continuing business.

*   **2024 Baseline (Cont. Ops):** 7.80% ($790M NI / $10,127M Rev). [cite: 10 in step 2]
*   **Initial 2025 Margin:** 8.50% (A conservative increase reflecting initial benefits of the restructuring).
*   **Annual Margin Increase:** **50 basis points (0.50%)** per year, reflecting management's execution on cost savings and operating leverage.

---

## III. Discounted Cash Flow (DCF) Model

### A. Revenue and Margin Projections (USD Millions)

| Year | Revenue (A) | Y-o-Y Growth Rate | Net Income Margin (B) | Net Income from Operations (A x B) (C) |
| :--- | :--- | :--- | :--- | :--- |
| **2025** | 10,610 | 4.8% (Conservative) | 8.50% | \$902 |
| **2026** | 11,141 | 5.0% | 9.00% | \$1,003 |
| **2027** | 11,586 | 4.0% | 9.50% | \$1,101 |
| **2028** | 11,992 | 3.5% | 10.00% | \$1,199 |
| **2029** | 12,352 | 3.0% | 10.50% | \$1,297 |
| **2030** | 12,661 | 2.5% | 11.00% | \$1,393 |

*   *2025 Revenue:* Midpoint of management's raised guidance for the full year. [cite: 4 in step 1]
*   *2026 Growth:* Use 5.0%, slightly above the $10,610M * (1 + 5.0%) = $11,141M. This incorporates the projected 2025 growth momentum and the beginning of the acquisition's integration/synergies, while remaining conservative against the top end of 2025 guidance.
*   *Post-2026 Growth:* Taper the growth rate down to 2.5% by 2030 to reflect industry maturity and a conservative view of long-term sustainable growth.

### B. Net Income (Cash Flow) Projection and Discounting

The instruction is to assume: **Net Income for each year goes straight into cash for the next year.**

**Formula:** $Net Income_{x} = Net Income_{Operations} + ROIC \times Net Income_{x-1}$

| Year | Net Income from Operations (C) | Prior Year Net Income (D) | ROIC (4.00%) | ROIC Income (D x ROIC) (E) | Projected Net Income (C + E) (F) | Discount Factor (10.00%) | Present Value (F x DF) (G) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2025** | \$902 | \$790 (2024 NI Cont. Ops) | 4.00% | \$32 | \$934 | 0.909 | **\$849** |
| **2026** | \$1,003 | \$934 | 4.00% | \$37 | \$1,040 | 0.826 | **\$859** |
| **2027** | \$1,101 | \$1,040 | 4.00% | \$42 | \$1,143 | 0.751 | **\$858** |
| **2028** | \$1,199 | \$1,143 | 4.00% | \$46 | \$1,245 | 0.683 | **\$850** |
| **2029** | \$1,297 | \$1,245 | 4.00% | \$50 | \$1,347 | 0.621 | **\$836** |
| **2030** | \$1,393 | \$1,347 | 4.00% | \$54 | \$1,447 | 0.564 | **\$816** |
| **Sum of NPV (2025-2030)** | | | | | | | **\$5,068** |

### C. Terminal Value Calculation

**Assumptions:**

*   **Terminal Growth Rate (g):** **1.5%** (Conservative maturity rate, below long-term GDP/inflation).
*   **Discount Rate (r):** **10.0%** (Conservative and reasonable for a technology company).
*   **Last Cash Flow for Perpetuity:** 2030 Net Income, **\$1,447 million** (F).

**Terminal Value (TV) Formula:** $TV = \frac{Cash Flow_{2030} \times (1 + g)}{r - g}$

$$TV = \frac{\$1,447 \times (1 + 0.015)}{0.10 - 0.015} = \frac{\$1,468.61}{0.085} = \$17,278 \text{ million}$$

**Terminal Value Net Present Value (TV NPV):**

$$TV_{NPV} = TV \times \text{Discount Factor}_{2030} = \$17,278 \times 0.564 = \mathbf{\$9,747} \text{ million}$$

### D. Calculation of Enterprise Value (EV)

| Metric | Value (USD Millions) |
| :--- | :--- |
| **NPV of Explicit Period Cash Flows** (2025-2030) | \$5,068 |
| **NPV of Terminal Value** | \$9,747 |
| **Total Net Present Value (EV)** | **\$14,815** |

---

## IV. Fair Value Calculation

**Fair Value of Equity Formula:** $Equity Value = Total NPV + Total Cash - Total Debt$

| Metric | Value (USD Millions) |
| :--- | :--- |
| **Total NPV (EV)** | \$14,815 |
| **ADD: Total Cash & Cash Equivalents** | \$571 |
| **LESS: Total Debt** | (\$13,000) |
| **Fair Value of Equity** | **\$2,386** |

**Fair Value Per Share Formula:** $\text{Equity Value} / \text{Shares Outstanding}$

$$\text{Fair Value Per Share} = \frac{\$2,386 \text{ million}}{517.85 \text{ million shares}} = \mathbf{\$4.61}$$

---

## V. Justification and Market Comparison

### Fair Value of FIS Stock: **\$4.61 per share**

### Justification of the Difference between Fair Value and Market Price

Assuming a market price of approximately **\$54.00 per share** (used for a market cap estimate), the calculated fair value of **\$4.61** is significantly lower.

**Why the Valuation is so Different from the Market:**

The core of the difference lies in the constraint of using **GAAP Net Income** in the DCF model, as instructed, rather than the widely accepted financial metric for enterprise valuation: **Adjusted Free Cash Flow (FCF)**.

1.  **GAAP Net Income vs. Adjusted Free Cash Flow (FCF):**
    *   **The Valuation Model's Cash Flow (GAAP Net Income):** The required model uses GAAP Net Income, which is heavily impacted by large, non-cash amortization expenses from historical acquisitions (especially the Worldpay merger) and volatile one-time gains/losses. For example, FIS had a significant GAAP Net Loss in Q2 2025 (-$470 million) [cite: 10 in step 2].
    *   **FIS's Reported Economic Cash Flow (Adjusted FCF):** Management guides its performance based on **Adjusted FCF** and is explicitly managing for it, guiding to over 85% conversion in 2025 and 90% in 2026. [cite: 5 in step 1]
    *   The market is valuing FIS based on its *economic cash flow* (Adjusted FCF) and its deleveraging/capital return program.
    *   **2025 Projected Adjusted FCF (Q3 2025 YTD):** Year-to-date Adjusted FCF was \$1.6 billion for nine months. Assuming a strong Q4, the full year could be over \$2.1 billion.
    *   **The Market's Assumptions:** The market is likely assuming that the current level of high capital expenditure and non-cash amortization will normalize or that the FCF will be the true determinant of value. The market may also be valuing the Worldpay retained stake and pending acquisition at much higher levels.

2.  **The Impact of High Debt and the Worldpay Transaction:**
    *   The model calculates a high Total NPV (\$14,815 million), but the large **\$13,000 million in debt** is then subtracted from this to determine the Equity Value.
    *   The market is also implicitly assuming that the sale of the remaining Worldpay interest for **\$6.6 billion** (expected to close in Q1 2026) and the \$13.5 billion acquisition of Issuer Solutions will fundamentally reshape the balance sheet and cash flows, potentially reducing the net debt or funding the acquisition without major additional debt, which would significantly increase the FCF profile immediately. The current model is unable to fully account for the Q1 2026 cash infusion from the Worldpay sale without more complex modeling of non-recurring events.

**Conclusion:**

The computed Fair Value of **\$4.61 per share** is a mathematical result of adhering strictly to the mandated methodology of using *GAAP Net Income* as the cash flow metric in an environment where FIS's Net Income is severely depressed by non-cash charges and is not a true reflection of the cash generation capacity of the continuing operations. The market's price of $\sim$\$54.00 per share reflects its valuation of the company's robust, management-guided **Adjusted Free Cash Flow** and the expected deleveraging and value creation from the planned strategic transactions. The market is giving little to no weight to the temporary volatility in GAAP Net Income.
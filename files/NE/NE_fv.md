## Valuation of Noble Corporation plc (NE) Stock

This valuation is based on a Discounted Cash Flow (DCF) model using a conservative business engine derived from the company's latest financial reports and management commentary, adhering strictly to the provided rules.

### I. Starting Financial Data (as of June 30, 2025)

The following financial data is sourced from Noble Corporation plc's Q2 2025 earnings release, which is filed with the U.S. Securities and Exchange Commission (SEC).

| Metric | Value (USD Millions) | Source/Basis |
| :--- | :--- | :--- |
| **Total Cash & Cash Equivalents** | $338 million | Q2 2025 Balance Sheet |
| **Total Debt** | $2,000 million (or $2.0 Billion) | Q2 2025 Balance Sheet |
| **Shares Outstanding** | 158.8 million | Most recent data [cite: 6 in step 1] |
| **Current Stock Price (approx.)** | $27.48 (as of 10/17/2025) [cite: 14 in step 1] | For comparison purposes only |

---

### II. Business Engine and Financial Projections (2025-2030)

The core business of Noble Corporation (NE) is contract offshore drilling, driven by rig utilization, average day rates, and fleet size/quality. The company's future revenue is heavily underpinned by its substantial **contract backlog** ($6.9 billion as of Q2 2025), which provides excellent visibility into the near-term and a strong base for long-term estimates. The business engine relies on securing new contracts at higher day rates as the deepwater drilling cycle continues its recovery.

**Key Engine Assumptions:**

1.  **2025 Revenue:** Based on management's full-year guidance midpoint.
    *   *2025 Revenue Guidance:* \$3.20 billion - \$3.30 billion.
    *   *Conservative Estimate:* Midpoint **\$3.25 Billion**.
2.  **Backlog Conversion:** The existing backlog provides the floor for future years' revenue:
    *   2026: \$2.3 Billion (49% coverage)
    *   2027: \$1.6 Billion (36% coverage)
    *   2028: \$1.0 Billion (20% coverage)
    *   2029-2031: \$0.9 Billion (5% coverage) [cite: 6 in step 2]
3.  **Uncontracted Revenue (Spot Market):** The remaining revenue for each year must come from new contracts. I will model the uncontracted portion based on a combination of a slowly rising market day rate and conservative, gradual utilization improvement. The company's strategic focus on high-specification fleets and fleet rationalization is expected to capture high-value contracts [cite: 7, 12 in step 1].
    *   **Assumption:** The offshore drilling market is recovering, but the long-term nature of this business cycle warrants conservative uncontracted revenue growth. I assume an annual increase in *new contracting revenue* of **5%** on the uncontracted portion of available days. The uncontracted portion will be estimated as Total Revenue minus Backlog Conversion for each year.
4.  **Net Income Margin (NIM):**
    *   *2025 NIM:* Based on the Q1 and Q2 2025 Net Income and the overall 2025 Revenue estimate. The sum of Q1 and Q2 2025 Net Income is \$108M + \$43M = \$151M. This is an approximate annualized NIM of $\sim 4.6\%$ (if Q3 and Q4 are similar). The 2025 Adjusted EBITDA guidance midpoint is \$1.1125B. Due to the high **\$100 million in merger synergies** expected to be fully realized by the end of 2025 [cite: 7 in step 1] and operating leverage, a slight improvement in NIM is justified.
    *   *Conservative Estimate:* I will project a starting Net Income Margin of **5.5%** for 2025 and assume conservative, incremental expansion to **6.0%** by 2030 due to cost controls, full synergy realization, and improving operating leverage from higher day rates. This is a conservative assumption given the high Adjusted EBITDA guidance and is well below the 9.39% TTM net income margin cited in external data [cite: 1 in step 1].

#### Revenue and Net Income Projection Table

| Year | (A) Backlog Conversion (Billion) [cite: 6 in step 2] | (B) Estimated Total Revenue (Billion) | (C) Net Income Margin (NIM) | (D) Projected Net Income (Billion) (B x C) |
| :--- | :--- | :--- | :--- | :--- |
| **2025** | *N/A (using guidance)* | $3.250 | 5.50% | $0.179 |
| **2026** | $2.300 | $3.500 | 5.60% | $0.196 |
| **2027** | $1.600 | $3.750 | 5.70% | $0.214 |
| **2028** | $1.000 | $3.900 | 5.80% | $0.226 |
| **2029** | $0.300 | $4.000 | 5.90% | $0.236 |
| **2030** | *N/A* | $4.100 | 6.00% | $0.246 |

***Justification for Revenue 2026-2030 (B):***
*   **2026:** \$3.50B is a conservative increase from 2025's \$3.25B, well-justified by the \$2.3B in firm backlog, leaving \$1.2B to be contracted, a reasonable amount given market recovery and $6.9B total backlog [cite: 6 in step 2].
*   **2027-2030:** I model a conservative, decelerating annual revenue growth rate from 7.1% (2026-2027) down to 2.5% (2029-2030). This reflects the expected full utilization of the high-spec fleet and the conservative nature of the offshore deepwater cycle, where growth is constrained by rig supply and day-rate strength rather than massive new fleet capacity.

---

### III. Discounted Cash Flow (DCF) Analysis

The cash flow for this DCF model is defined as: **Projected Net Income** + **Income from Reinvested Cash (ROIC)**.

#### A. Return on Invested Capital (ROIC) Assumption

*   **Rule:** Assume net income for each year goes straight into cash for the next year. Then get a reasonable ROIC percentage based on the past to get additional income for the next year.
*   **Historical ROIC (TTM):** The Trailing Twelve Months (TTM) ROIC is approximately 7.96% [cite: 1 in step 1].
*   **Conservative ROIC for Projection:** I will use a conservative **7.5%** ROIC on the prior year's accumulated cash (Net Income from prior years). This is slightly below the TTM figure and reflects a prudent expectation for returns on reinvested earnings in capital-intensive projects.

#### B. Discount Rate and Maturity Rate

*   **Discount Rate (Conservative but Reasonable):** I will use a **10.0%** discount rate. This is reasonable for an offshore driller operating in a highly cyclical, volatile, and capital-intensive industry, reflecting a higher required rate of return than a stable utility.
*   **Terminal (Maturity) Rate (Conservative):** The conservative long-term growth rate after 2030 is set at **2.0%**. This is a standard conservative rate, slightly above long-term inflation, assuming NE will grow at a modest pace well into maturity.

#### C. DCF Calculation

| Year | Projected Net Income (Billion) | Income from ROIC (7.5%) (Billion) | Total Cash Flow (Billion) | Discount Factor (10.0%) | Present Value (Billion) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2025** | $0.179 | $0.000 | $0.179 | 0.909 | $0.163 |
| **2026** | $0.196 | $0.013 ($0.179 * 7.5%) | $0.209 | 0.826 | $0.173 |
| **2027** | $0.214 | $0.028 ($0.388 * 7.5%) | $0.242 | 0.751 | $0.182 |
| **2028** | $0.226 | $0.046 ($0.630 * 7.5%) | $0.272 | 0.683 | $0.186 |
| **2029** | $0.236 | $0.066 ($0.902 * 7.5%) | $0.302 | 0.621 | $0.188 |
| **2030** | $0.246 | $0.090 ($1.204 * 7.5%) | $0.336 | 0.564 | $0.189 |
| **Sum of NPV (2025-2030)** | | | | | **$1.081 Billion** |

***Note on ROIC:*** *The ROIC base for year N is the accumulated net income from all prior years (Year 2025 Cash Flow Base = 2025 Net Income. 2026 Cash Flow Base = 2025 Net Income + 2026 Net Income etc.). For the table, the Cash Flow base for 2027 is Net Income (2025) + Total CF (2026 Net Income) = $0.179B + $0.209B = $0.388B.*

#### D. Terminal Value (TV) Calculation

The terminal value is calculated as the Perpetuity Growth Model starting from 2031:

$$
\text{Terminal Value} = \frac{\text{Cash Flow}_{2030} \times (1 + \text{Maturity Rate})}{\text{Discount Rate} - \text{Maturity Rate}}
$$

$$
\text{Terminal Value} = \frac{\$0.336 \text{ Billion} \times (1 + 0.02)}{0.10 - 0.02} = \frac{\$0.3427 \text{ Billion}}{0.08} = \$4.284 \text{ Billion}
$$

**NPV of Terminal Value (Discounted to present):**
$$
\text{NPV of TV} = \text{Terminal Value} \times \text{Discount Factor}_{2030}
$$

$$
\text{NPV of TV} = \$4.284 \text{ Billion} \times 0.564 = **\$2.416 \text{ Billion}**
$$

#### E. Total Enterprise Value (EV)

$$
\text{Total Enterprise Value (EV)} = \text{Sum of NPV (2025-2030)} + \text{NPV of TV}
$$

$$
\text{Total Enterprise Value (EV)} = \$1.081 \text{ Billion} + \$2.416 \text{ Billion} = **\$3.497 \text{ Billion}**
$$

---

### IV. Fair Value Calculation

The Fair Value of Equity is calculated by adjusting the Enterprise Value for Debt and Cash.

| Metric | Value (USD Billions) |
| :--- | :--- |
| **Total Enterprise Value (EV)** | $3.497 |
| (+) Total Cash & Cash Equivalents | $0.338 |
| (-) Total Debt | $2.000 |
| **Total Fair Value of Equity** | **$1.835 Billion** |

**Fair Value Per Share Calculation:**

$$
\text{Fair Value Per Share} = \frac{\text{Total Fair Value of Equity}}{\text{Shares Outstanding}}
$$

$$
\text{Fair Value Per Share} = \frac{\$1,835 \text{ Million}}{158.8 \text{ Million Shares}} = **\$11.56 \text{ Per Share}**
$$

---

### V. Final Result and Justification

| Metric | Value |
| :--- | :--- |
| **Fair Value Per Share (DCF)** | **$11.56** |
| **Current Market Price (approx.)** | **$27.48** |

#### Justification for Discrepancy

The calculated Fair Value of **\$11.56** is significantly lower than the market price of approximately **\$27.48**. The market is making assumptions that are *far more optimistic* than the conservative model employed here.

**Reasons for the Market's Higher Valuation (and the Difference from the Model):**

1.  **More Aggressive Day Rate and Utilization Forecast:** The market is likely pricing in a substantially faster and more aggressive recovery in the offshore drilling cycle than my conservative model, which assumes a slow, steady improvement in uncontracted revenue (49% coverage in 2026, 36% in 2027) [cite: 6 in step 2]. The market is assuming that the uncontracted portion of the fleet will secure contracts at *significantly higher day rates* in 2026-2030, driving total revenue much higher than my estimates (which peak at \$4.1B).
2.  **Higher Long-Term Margin Expectations:** My model projects a modest Net Income Margin increase from 5.5% to 6.0%. The market is likely assuming Noble achieves a much higher sustainable margin, perhaps closer to the *double-digit margins* seen during previous peaks in the drilling cycle (which would be consistent with the company's focus on high-spec, highly utilized rigs) [cite: 7 in step 1]. For my DCF to match the current price of \$27.48, the *Total Fair Value of Equity* would need to be $\sim\$4.36$ Billion (158.8M shares * $27.48/share). This would require Net Income in the terminal period to be nearly double my projections, implying a terminal Net Income Margin closer to 10-12% on higher revenue.
3.  **Lower Discount Rate (WACC):** The market might be using a lower cost of capital (Discount Rate) than my conservative **10.0%**. A lower WACC (e.g., 8.0-9.0%) significantly inflates the Terminal Value and, consequently, the overall valuation.
4.  **Assumptions on Cash Return:** My model conservatively reinvests all Net Income at a 7.5% ROIC. The market may be placing a high value on the company's aggressive **return of capital program** (over \$1.1 billion returned since Q4 2022). Investors may be valuing the company based on a higher Free Cash Flow (FCF) yield, which would be a different valuation methodology than my Net Income-based DCF.

**Conclusion on Valuation:**

The **\$11.56** fair value represents a highly conservative estimate, primarily due to:
*   Conservative revenue projections post-2027 that prioritize certainty (backlog) over the full potential of a cyclical upswing.
*   Conservative Net Income Margin expansion (5.5% to 6.0%) despite strong adjusted EBITDA guidance.
*   A high, conservative discount rate of 10.0%.

The market's multiple is a bet on the full, unconstrained recovery of the deepwater drilling market—a high-conviction cyclical call that requires substantially higher utilization and day rates than my model conservatively estimates. For a value investor, the current price suggests the company must generate significantly higher earnings than what management guidance and a prudent extrapolation of the business engine indicate.

### Fair Value of Noble Corporation plc (NE) Stock

**Fair Value Per Share:** **\$11.56**
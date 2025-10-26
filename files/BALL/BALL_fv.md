This valuation of Ball Corporation (BALL) stock uses a Discounted Cash Flow (DCF) approach based exclusively on information derived from SEC filings and management commentary, focusing on the continuing Aluminum Packaging business after the divestiture of the Aerospace segment.

---

## 1. Initial Financial Data & Shares Outstanding

The following financial data is sourced from the most recent SEC filings for Ball Corporation, primarily the Form 10-Q for the quarter ended March 31, 2025, and Form 10-K for the fiscal year ended December 31, 2024.

| Metric | Value (USD Millions) | Source/Notes |
| :--- | :--- | :--- |
| **Total Cash & Cash Equivalents** | $449 | Unaudited Condensed Consolidated Balance Sheet, March 31, 2025. |
| **Total Debt** | $6,717 | Long-Term Debt ($6,134) + Short-Term Debt & Current Portion of L-T Debt ($583) as of March 31, 2025. |
| **Shares Outstanding** | 272.15 million | Based on latest common figures. |
| **Current Stock Price (BALL)** | $49.83 | As of October 24, 2025. |

### 2. Baseline Financials (2024 - Continuing Operations)

The divestiture of the Aerospace business in early 2024 significantly changes the financial profile. The valuation will be based on the continuing aluminum packaging operations.

| Metric | Value (USD Millions) | Source/Notes |
| :--- | :--- | :--- |
| **Net Sales (2024 - Aluminum Pkg. Only)** | $11,800 | Full-year 2024 net sales, excluding the divested aerospace business. |
| **Comparable Net Earnings (2024)** | $977 | A better representation of ongoing business profitability than GAAP net income, which included a $3.47 billion after-tax gain from the Aerospace sale. |
| **Comparable Net Income Margin (2024)** | 8.28% | ($977 million / $11,800 million) |

---

## 3. Business Engine & Revenue / Net Income Projections (2025–2030)

Ball Corporation's business engine is driven by:
1.  **Volume Growth:** Global demand for sustainable aluminum packaging, particularly in energy drinks and non-alcoholic beverages, is driving volume growth. Management guided to global volume growth in the **2% to 3%** range for 2025.
2.  **Price/Mix and Cost Management:** The company benefits from contractual pass-throughs of aluminum costs and a focus on operating efficiencies/cost control to expand margins.

Management's explicit long-term goal is to achieve comparable diluted EPS growth **exceeding 10%** in 2025 and beyond. The latest guidance was for **12-15%** comparable diluted EPS growth for 2025.

To build a conservative and justified model, I will use a revenue growth rate that supports a slightly more conservative EPS growth than the high-end guidance and then rely on management's long-term EPS guidance.

### A. Revenue and Margin Assumptions

| Year | Revenue Growth Rate | Rationale |
| :--- | :--- | :--- |
| **2025** | **4.0%** | Higher than the 2-3% volume guidance to account for favorable price/mix and inflation pass-through, and to support the projected EPS growth. |
| **2026** | **3.0%** | Midpoint of the long-term volume growth guidance. |
| **2027-2030** | **2.5%** | Conservative long-term growth, reflecting a mature, cyclical, but steadily growing packaging industry where volume gains are partially offset by raw material cost pass-through. |

| Year | Comparable Net Income Margin | Rationale |
| :--- | :--- | :--- |
| **2025** | **8.5%** | Modest margin expansion over 2024 (8.28%) due to cost management and efficiency gains, as mentioned in earnings calls. |
| **2026-2030** | **8.75%** | Conservative, sustained margin improvement, capitalizing on the new, leaner operating model post-Aerospace sale and continued focus on cost control (Ball Business System). |

### B. Net Income Projection (DCF Cash Flow)

The valuation will use Net Income with an adjustment for the return on retained cash (ROIC), as per the instructions.

**Initial Parameters:**

*   **2024 Comparable Net Income (NI0):** $977 million
*   **Effective Tax Rate (T):** 23% (Conservative, based on guidance of "slightly above 22%")
*   **Conservative ROIC (r):** **8.0%**

A Return on Invested Capital (ROIC) of 8.0% is a conservative but reasonable assumption for a mature, capital-intensive manufacturing company like Ball, which has divested a large, high-margin, non-core segment to focus on its core business.

The formula for projected Net Income is:
$$\text{NI}_{t} = \text{NI}_{\text{Revenue based, }t} + \text{NI}_{t-1} * (1 - \text{Payout Ratio}) * \text{r}$$
Since the instruction mandates a simplified model where **Net Income for each year goes straight into cash for the next year**, and an additional income is earned via ROIC from the **previous year's Net Income** (which serves as the retained cash), the formula simplifies to:

$$\text{Projected Cash Flow}_{t} = \text{Net Income}_{t} = \text{Net Income}_{\text{Revenue Based}, t} + \text{NI}_{t-1} * \text{ROIC}$$

*Assumption: All Net Income is retained as cash at the beginning of the next year, and the Payout Ratio is effectively 0 for the purpose of the incremental ROIC calculation, making the valuation more conservative than using Free Cash Flow which subtracts Capex.*

| Year | 2024 (Base) | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **A. Revenue (in millions)** | $11,800 | $12,272 | $12,640 | $12,956 | $13,280 | $13,612 | $13,952 |
| **B. Net Income Margin** | 8.28% | 8.50% | 8.75% | 8.75% | 8.75% | 8.75% | 8.75% |
| **C. Revenue-Based NI** (A * B) | $977 | $1,043 | $1,106 | $1,134 | $1,162 | $1,191 | $1,221 |
| **D. ROIC Income** ($) | - | $78 | $83 | $88 | $90 | $93 | $95 |
| **E. Total Projected NI / Cash Flow** (C + D) | **$977** | **$1,121** | **$1,189** | **$1,222** | **$1,252** | **$1,284** | **$1,316** |

*Note: ROIC Income is 8.0% * Net Income from the prior year (e.g., $977M * 8.0% = $78M for 2025).*

---

## 4. Discounted Cash Flow (DCF) Calculation

### A. Rate Assumptions

| Metric | Rate | Rationale |
| :--- | :--- | :--- |
| **Conservative Discount Rate** | **9.0%** | A conservative rate above the risk-free rate, reflecting the company's relatively low-growth, essential industry, and its high debt-to-equity ratio. |
| **Conservative Maturity Rate (g)** | **2.5%** | Matches the long-term conservative revenue growth rate (2027-2030) and is a modest rate for a company operating in a mature, consolidated industry with contractual cost pass-throughs. This rate assumes no significant long-term structural advantage or technological disruption beyond the continued shift to aluminum cans. |

### B. Terminal Value and NPV

**Terminal Value (TV) at EOY 2030:**
The terminal value is calculated using the Gordon Growth Model based on the 2030 projected cash flow:
$$\text{TV}_{2030} = \frac{\text{Cash Flow}_{2030} * (1 + \text{g})}{\text{r} - \text{g}}$$
$$\text{TV}_{2030} = \frac{\$1,316 * (1 + 0.025)}{0.09 - 0.025} = \frac{\$1,348.9}{\textbf{0.065}} = \textbf{\$20,752} \text{ million}$$

| Year | Projected Cash Flow (in millions) | Discount Factor (1 / (1+0.09)^t) | Present Value (in millions) |
| :--- | :--- | :--- | :--- |
| **2025** | $1,121 | 0.9174 | $1,028 |
| **2026** | $1,189 | 0.8417 | $1,001 |
| **2027** | $1,222 | 0.7722 | $943 |
| **2028** | $1,252 | 0.7084 | $887 |
| **2029** | $1,284 | 0.6499 | $835 |
| **2030** | $1,316 | 0.5963 | $786 |
| **Terminal Value (2030)** | $20,752 | 0.5963 | $12,374 |
| **Sum of NPV** | | | **$17,854** |

**Net Present Value (NPV) of Future Cash Flows (Total Equity Value) = $17,854 million**

---

## 5. Fair Value Calculation

$$\text{Fair Value per Share} = \frac{\text{NPV of Cash Flows} + \text{Cash} - \text{Total Debt}}{\text{Shares Outstanding}}$$

| Metric | Value (USD Millions) |
| :--- | :--- |
| NPV of Cash Flows (Total Equity Value) | $17,854 |
| Add: Total Cash & Cash Equivalents | $449 |
| Less: Total Debt | ($6,717) |
| **Total Equity Value** | **$11,586** |
| Shares Outstanding (in millions) | 272.15 |
| **Fair Value per Share** | **$42.57** |

---

## Conclusion and Justification

The calculated **Fair Value per Share** for Ball Corporation (BALL) is **$42.57**.

The **Current Market Price** for the stock is **$49.83**.

The calculated Fair Value is **14.6% lower** than the current market price, indicating that, based on these conservative assumptions, the stock is currently **overvalued** by the market.

### Justification for the Difference

The primary reason for the discrepancy between the calculated Fair Value ($42.57) and the Market Price ($49.83) is that the market is likely making more optimistic assumptions about one or more of the following key conservative inputs:

1.  **Long-Term Growth Rate (Maturity Rate):** I used a conservative long-term growth rate ($g$) of **2.5%**, which is tied to the mid-range of volume growth. The market may be projecting a higher long-term growth rate, perhaps **3.0% - 3.5%**, based on:
    *   The continued, accelerated global trend toward more sustainable aluminum packaging (aluminum can recycling rate is significantly higher than plastic).
    *   Faster-than-expected growth in emerging markets and high-growth segments (energy drinks, non-alcoholic beverages).

2.  **Discount Rate / Risk (Cost of Capital):** I used a conservative Discount Rate of **9.0%**. Given the major deleveraging event from the Aerospace sale and management's target to bring net debt/Comparable EBITDA to $\sim2.75x$ by the end of 2025, the market may see the company as less risky than before, thus warranting a lower Cost of Equity/Discount Rate, such as **8.0%** or **8.5%**.

3.  **Profitability/Margin Expansion:** I projected a modest margin expansion to **8.75%** by 2026. The market may be assuming a stronger margin recovery and greater success from the company's focus on operational excellence and cost control, pushing the long-term margin closer to **9.0%** or higher.

**Hypothetical Market-Implied Assumptions (What it would take to justify $49.83):**

If we keep all other conservative assumptions constant (8.0% ROIC, 8.75% long-term margin, and the 9.0% Discount Rate), to arrive at the current market price of $49.83, the implied **Maturity Growth Rate ($g$)** would need to be approximately **3.2%**. This is significantly higher than my conservative 2.5% but well within the realm of possibility if the global "can-shift" trend is strong and sustained.

**Conclusion:**

The valuation suggests Ball Corporation is slightly overvalued given a **conservative, de-risked DCF model** that prioritizes management's long-term EPS guidance and a modest long-term growth rate in a mature industry. The market is currently pricing in a belief that Ball will achieve a sustained long-term growth rate of at least 3.0% or a lower cost of capital due to the deleveraging and focus on the core packaging business.

---

## FAIR VALUE OF STOCK

The calculated Fair Value of Ball Corporation (BALL) stock is:

## $42.57 per share
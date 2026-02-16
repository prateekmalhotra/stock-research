This valuation of IQVIA Holdings Inc. (IQV) stock is based on a conservative Discounted Cash Flow (DCF) model, utilizing financial data extracted from SEC filings and management guidance from earnings call transcripts.

---

## IQVIA Holdings Inc. (IQV) Stock Valuation

### 1. Balance Sheet Metrics

The figures below are extracted from the latest available financial reports and earnings highlights, primarily reflecting the period ended **December 31, 2025**.

| Metric | Value (in millions USD) | Source/As of Date |
| :--- | :--- | :--- |
| **Total Cash & Cash Equivalents** | $1,980 | Q4 2025 Earnings Highlight |
| **Total Debt (Gross Debt)** | $15,724 | Q4 2025 Earnings Highlight |
| **Shares Outstanding** | 169.6 million | Dec 31, 2025 (SEC Filing) |
| **Current Stock Price (Hypothetical)** | \$240.00 | *Used for comparison* |

---

### 2. Business Engine Analysis & Revenue Projections

IQVIA's business engine is driven by two primary segments:
1.  **Research & Development Solutions (R&DS):** Contract Research Organization (CRO) services, which is largely driven by pharmaceutical and biotech R&D budgets. This segment has high revenue visibility due to its substantial contracted backlog, which stood at **$32.7 billion** as of December 31, 2025. The backlog provides a stable base for future revenue.
2.  **Technology & Analytics Solutions (TAS) / Commercial Solutions (CS):** Provides proprietary data, advanced analytics, and technology solutions (including AI-enabled tools) to the life sciences industry. This segment is characterized by higher growth and is leveraged by the company's investments in AI and real-world data services.

**Management Guidance & Assumptions:**
*   Management is guiding to a shift in segmentation for 2026, which groups the higher-growth data/tech services (Commercial Solutions) separately from R&D.
*   2026 Guidance: Commercial Solutions expected to grow **7%-9%** and R&D Solutions about **4%** at the midpoint. This suggests a blended growth rate near the midpoint of the 2026 overall revenue guidance (5.8%).
*   **Conservative Engine Assumption:** The long-term growth is anchored by the stable, sticky CRO business (R&DS backlog) and the higher-growth data/AI segment (TAS/CS). I will assume the overall revenue growth rate gradually declines toward a maturity rate reflective of the broader healthcare/CRO market.

| Year | Revenue (Millions USD) | YOY Growth Rate | Rationale |
| :--- | :--- | :--- | :--- |
| **2025 (Actual)** | $16,310 | 5.9% | Actual 2025 full-year revenue |
| **2026 (Guidance)** | $17,259 | 5.8% | Midpoint of 2026 guidance range ($17.159B to $17.359B) |
| **2027** | $18,122 | 5.0% | Conservative step-down from guidance, still supported by strong R&DS backlog growth (5.3% YOY) and AI/data initiatives. |
| **2028** | $18,907 | 4.3% | Continued deceleration, nearing the R&DS growth rate as the R&D cycle matures. |
| **2029** | $19,663 | 4.0% | Steady, long-term growth rate for a mature, highly integrated service and technology provider. |
| **2030** | $20,356 | 3.5% | Close to a conservative long-term GDP/sector growth rate, serving as the basis for the perpetuity growth. |

---

### 3. Margin & Net Income Projections

IQVIA operates with a significant difference between GAAP Net Income and Adjusted Net Income, which management often points to as more reflective of underlying operational performance, with $2.1 billion in FCF "representing about 100% of adjusted net income" in 2025. I will use a Net Income Margin that starts conservatively near the **2024 GAAP Net Income Margin (8.91%)** and projects a modest improvement toward the **2025 Adjusted Net Income Margin (16.4%)**, reflecting management's focus on operational efficiency and the higher-margin technology segment.

| Year | Revenue (A) | Net Income Margin | Net Income (B) (A * Margin) |
| :--- | :--- | :--- | :--- |
| 2025 | $16,310 | 10.0% | $1,631 |
| 2026 | $17,259 | 10.5% | $1,812 |
| 2027 | $18,122 | 11.0% | $1,993 |
| 2028 | $18,907 | 11.5% | $2,174 |
| 2029 | $19,663 | 12.0% | $2,359 |
| 2030 | $20,356 | 12.5% | $2,545 |

**ROIC Assumption:**
The instruction requires modeling additional income from a reasonable ROIC on the *previous year's net income*. IQVIA's historical ROIC has averaged around 7.17% (5-year average) to 9.5% (2024 peak). I will use a conservative ROIC of **7.0%**.

**Projected Net Income / Free Cash Flow (FCF) Calculation:**
We will treat *Net Income* as the Free Cash Flow (FCF) for the DCF calculation, as is a common simplification, especially since 2025 FCF was approximately 100% of Adjusted Net Income.

$$
\text{FCF}_n = \text{Net Income}_n + (\text{Net Income}_{n-1} \times \text{ROIC})
$$

| Year | Projected Net Income (B) | ROIC Income (B_prev * 7.0%) | **Total FCF (C)** |
| :--- | :--- | :--- | :--- |
| 2025 | $1,631 | N/A (Starting Year) | $1,631 |
| **2026** | $1,812 | $1,631 * 7.0% = $114 | **$1,926** |
| **2027** | $1,993 | $1,812 * 7.0% = $127 | **$2,120** |
| **2028** | $2,174 | $1,993 * 7.0% = $139 | **$2,313** |
| **2029** | $2,359 | $2,174 * 7.0% = $152 | **$2,511** |
| **2030** | $2,545 | $2,359 * 7.0% = $165 | **$2,710** |

---

### 4. Discounted Cash Flow (DCF) Analysis

**Assumptions:**
*   **Conservative Maturity Rate (g):** 2.5% (Long-term terminal growth rate, conservative for a market-leader in a critical sector).
*   **Conservative Discount Rate (r):** 9.0% (A reasonable WACC proxy, balancing the low-interest-rate environment with the company's significant debt load).

**Terminal Value (TV) Calculation:**
The 2030 FCF ($2,710M) is used to calculate the Terminal Value using the perpetuity growth formula:
$$
\text{TV} = \frac{\text{FCF}_{2030} \times (1 + g)}{r - g} = \frac{\$2,710 \times (1 + 0.025)}{0.09 - 0.025} = \frac{\$2,778}{\text{0.065}} = \$42,738 \text{ Million}
$$

**Net Present Value (NPV) Calculation (Discounted at 9.0%):**

| Year | FCF (Millions USD) | Discount Factor (9.0%) | NPV of FCF |
| :--- | :--- | :--- | :--- |
| 2026 | $1,926 | 0.9174 | $1,766 |
| 2027 | $2,120 | 0.8417 | $1,784 |
| 2028 | $2,313 | 0.7722 | $1,787 |
| 2029 | $2,511 | 0.7084 | $1,779 |
| 2030 | $2,710 | 0.6499 | $1,761 |
| **2030 (Terminal Value)** | $42,738 | 0.6499 | $27,775 |
| **Total NPV of Future Cash Flows** | | | **$36,652** |

---

### 5. Fair Value Calculation

The total intrinsic value of the equity is calculated by combining the NPV of future cash flows, current cash, and subtracting total debt.

| Metric | Value (Millions USD) |
| :--- | :--- |
| **Total NPV of Future Cash Flows** | $36,652 |
| **(+) Total Cash & Cash Equivalents** | $1,980 |
| **(-) Total Debt (Gross Debt)** | $15,724 |
| **Total Equity Value** | **$22,908** |

**Fair Value Per Share:**

$$
\text{Fair Value Per Share} = \frac{\text{Total Equity Value}}{\text{Shares Outstanding}} = \frac{\$22,908,000,000}{169,600,000} = \mathbf{\$135.07}
$$

---

### 6. Conclusion and Justification

| Metric | Value |
| :--- | :--- |
| **Calculated Fair Value** | **\$135.07** |
| **Hypothetical Current Stock Price** | **\$240.00** |

#### Justification for Discrepancy

My calculated Fair Value of **\$135.07** is significantly lower than the hypothetical Current Stock Price of **\$240.00**. This large discrepancy implies that the market is making much more aggressive assumptions about IQVIA's future performance than my conservative model allows.

**Market Assumptions vs. My Conservative Assumptions:**

| Factor | My Conservative DCF Assumption | Market Implied Assumption |
| :--- | :--- | :--- |
| **Revenue Growth** | Decelerates from 5.8% (2026) to 3.5% (2030). | Must sustain a much higher long-term growth rate, likely in the **7-9%** range, reflecting continued dominance and market share gains. |
| **Profitability (Net Income Margin)** | Improves gradually from 10.0% to 12.5%. | Assumes a much faster and higher ramp-up to the **15-20%** Net Income Margin (closer to their Adjusted Net Income) based on significant operating leverage from their high-margin Technology & Analytics Solutions segment and AI investments. |
| **Discount/Risk Rate** | Conservative **9.0%** (reflects high debt). | A lower Discount Rate, potentially **7.5% - 8.0%**, reflecting the company's entrenched, mission-critical position and high-visibility backlog, suggesting lower systematic risk than assumed. |
| **Terminal Value Growth (g)** | Conservative **2.5%** maturity rate. | Must be significantly higher, perhaps **3.5% - 4.0%**, indicating a belief that their proprietary data and AI platforms will allow them to outgrow the broader economy for a very long period. |

My conservative approach, which limits long-term growth and margin expansion, leads to a much lower valuation. The market is clearly placing a premium on IQVIA's transformation into an **AI-enabled, high-growth technology platform** (TAS segment), justifying a significantly higher valuation multiple than a traditional CRO/service provider. The market is pricing in the *Adjusted Net Income Margin* as the sustainable profitability level, and a much higher long-term growth rate driven by AI integration, which my conservative model has deliberately avoided to fulfill the instruction to be *conservative* in all assumptions.
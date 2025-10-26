This valuation of Weis Markets, Inc. (WMK) stock uses a Discounted Cash Flow (DCF) model based solely on publicly available SEC filing data and management commentary from earnings call transcripts, as per the established rules.

---

# **Weis Markets, Inc. (WMK) Stock Valuation**

## **1. Initial Financial Data**

The following data is extracted from the latest available SEC filings (Q2 FY2025, ended June 28, 2025, and FY2024 results).

| Metric | Value (USD Millions) | Source/Justification |
| :--- | :--- | :--- |
| **Total Liquid Cash & Equivalents** | $188.8$ | Sum of Cash & Equivalents ($61.9M) and Marketable Securities ($126.9M). |
| **Total Debt (MRQ)** | $169.4$ | Total Debt as of the latest reported quarter. |
| **Shares Outstanding** | $24.74$ million | Latest reported figure. |
| **Last Fiscal Year Revenue (FY2024)** | $4,770$ | Net sales for the 52-week period ended December 28, 2024. |
| **Trailing Twelve Month (TTM) Net Income** | $107.5$ | TTM Net Income as of Q2 2025. |
| **TTM Net Income Margin** | $2.22\%$ | $107.5M / \$4,840M$ TTM Revenue. |
| **Historical Return on Invested Capital (ROIC)** | $6.1\%$ | The most conservative reported ROIC for the last fiscal year (Dec 2024) is used. |

## **2. Business Engine and Projection Assumptions**

The business engine of Weis Markets is driven by **Comparable Store Sales Growth** (pricing, volume, loyalty programs) and **Footprint Expansion** (new stores, acquisitions). Management commentary indicates a focus on accelerating CapEx for new stores and remodels, while operating costs remain a persistent challenge.

### **A. Revenue Engine Projection**

| Metric | Assumption | Justification (Management Commentary & World Knowledge) |
| :--- | :--- | :--- |
| **Comparable Store Sales Growth (Same-Store)** | $1.5\%$ per year (flat) | Q2 2025 comp sales (ex-fuel) were 2.3% YOY, but only 0.6% adjusted for the Easter shift. The 2-year stacked comp sales are modest (2.6% - 3.5%). A conservative, steady $1.5\%$ is used, reflecting a mature grocery market, ongoing price investments, and economic uncertainty. |
| **Footprint Expansion (New Stores/Acquisitions)** | $0.5\%$ per year (flat) | Management is accelerating capital expenditures, planning 4 new stores for 2025/early 2026, and acquired one store in Q2 2025. $0.5\%$ is a conservative estimate of the incremental sales from this expansion, reflecting the small size of the company's annual store count growth (approx. 2-3 new locations on 199 stores). |
| **Total Annual Revenue Growth** | **$2.0\%$** | Sum of Same-Store Growth ($1.5\%$) and Footprint Expansion ($0.5\%$). |

**Revenue Projection Table (USD Millions)**

| Year | Revenue | Calculation |
| :--- | :--- | :--- |
| **FY2024 (Base)** | $4,770$ | Reported Net Sales. |
| **FY2025** | $4,865$ | $4,770 * (1 + 2.0\%)$ |
| **FY2026** | $4,962$ | $4,865 * (1 + 2.0\%)$ |
| **FY2027** | $5,061$ | $4,962 * (1 + 2.0\%)$ |
| **FY2028** | $5,162$ | $5,061 * (1 + 2.0\%)$ |
| **FY2029** | $5,265$ | $5,162 * (1 + 2.0\%)$ |
| **FY2030** | $5,370$ | $5,265 * (1 + 2.0\%)$ |

### **B. Margin and ROIC Projection**

| Metric | Assumption | Justification (Management Commentary) |
| :--- | :--- | :--- |
| **Net Income Margin** | $2.20\%$ (flat) | TTM Net Income Margin is 2.22%. Management explicitly noted that "rising expenses were a notable theme" and "Operating, general, and administrative expense growth... has been a persistent challenge, growing faster than sales". A slightly lowered, flat $2.20\%$ margin is a conservative reflection of the margin pressure despite efficiency improvements. |
| **Return on Invested Capital (ROIC)** | $6.1\%$ (flat) | Use the most recent conservative TTM ROIC figure from the end of FY2024 to determine the return on cash flows reinvested. |

## **3. Projected Net Income and Discounted Cash Flow (DCF)**

The Net Income for each year is projected as:
$$
\text{Net Income}_n = (\text{Revenue}_n \times \text{Net Income Margin}) + (\text{Net Income}_{n-1} \times \text{ROIC})
$$

### **A. Net Income Projection (USD Millions)**

| Year | Revenue | Net Income Margin | Operating Net Income | ROIC Income (from $\text{NI}_{n-1} \times 6.1\%$) | **Total Net Income (Future Cash Flow)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FY2024 (Base)** | $4,770$ | $2.22\%$ | $105.9$ | - | $105.9$ |
| **FY2025** | $4,865$ | $2.20\%$ | $107.0$ | $6.46$ | $113.5$ |
| **FY2026** | $4,962$ | $2.20\%$ | $109.2$ | $6.92$ | $116.1$ |
| **FY2027** | $5,061$ | $2.20\%$ | $111.4$ | $7.08$ | $118.5$ |
| **FY2028** | $5,162$ | $2.20\%$ | $113.6$ | $7.23$ | $120.8$ |
| **FY2029** | $5,265$ | $2.20\%$ | $115.8$ | $7.37$ | $123.2$ |
| **FY2030 (Terminal)** | $5,370$ | $2.20\%$ | $118.1$ | $7.52$ | $125.6$ |

### **B. Discount Rate and Terminal Value**

*   **Discount Rate (Conservative but Reasonable):** **$8.0\%$**
    *   *Justification:* This is a conservative rate, above the historical Weighted Average Cost of Capital (WACC) for WMK (often cited in the 7.3\%-7.6\% range), reflecting the low-growth, low-beta (0.47) nature of the grocery business and a requirement for a sufficient margin of safety.
*   **Maturity Rate (Very Conservative Terminal Growth Rate):** **$1.0\%$**
    *   *Justification:* A very conservative rate, well below the long-term inflation target and the annual 2.0\% growth rate, reflecting a slowdown to near zero real growth in a saturated market.

**Terminal Value (TV) in 2030:**
$$
\text{TV}_{2030} = \frac{\text{Cash Flow}_{2030} \times (1 + \text{Maturity Rate})}{\text{Discount Rate} - \text{Maturity Rate}} = \frac{\$125.6 \times (1 + 1.0\%)}{8.0\% - 1.0\%} = \$1,811.5 \text{ Million}
$$

### **C. Discounted Cash Flow (DCF) Calculation**

| Year | Cash Flow (NI) (Millions) | Discount Factor (at $8.0\%$) | NPV (Millions) |
| :--- | :--- | :--- | :--- |
| **2025** | $113.5$ | $0.9259$ | $105.1$ |
| **2026** | $116.1$ | $0.8573$ | $99.6$ |
| **2027** | $118.5$ | $0.7938$ | $94.0$ |
| **2028** | $120.8$ | $0.7350$ | $88.8$ |
| **2029** | $123.2$ | $0.6806$ | $83.8$ |
| **2030 (NI)** | $125.6$ | $0.6302$ | $79.1$ |
| **2030 (TV)** | $1,811.5$ | $0.6302$ | $1,141.6$ |
| **Total NPV of Future Cash Flows (Enterprise Value)** | | | **$1,692.0$ Million** |

## **4. Fair Value Calculation**

| Metric | Value (USD Millions) |
| :--- | :--- |
| **Enterprise Value (Total NPV of Future Cash Flows)** | $1,692.0$ |
| **Add: Total Liquid Cash & Equivalents** | $188.8$ |
| **Subtract: Total Debt (MRQ)** | $169.4$ |
| **Equity Value** | **$1,711.4$** |
| **Shares Outstanding (Millions)** | $24.74$ |
| **Fair Value Per Share** | **$69.10$** |

---

# **5. Conclusion and Justification**

**Fair Value of Weis Markets, Inc. (WMK) Stock: $69.10**

### **Justification for Valuation and Market Discrepancy**

The fair value calculated is **\$69.10 per share**.

Assuming a recent market price of approximately **\$68.72** (as seen in search results around Q2 2025 reporting), the calculated fair value is **very close** to the market price.

**Market Assumptions vs. Valuation Assumptions:**

The proximity of the calculated Fair Value to the Market Value suggests that the market's collective assumptions about WMK's future performance are almost identical to the conservative estimates used in this DCF analysis.

| Valuation Assumption | Market Implied Assumption | Conclusion |
| :--- | :--- | :--- |
| **Total Annual Revenue Growth: $2.0\%$** | $~2.0\%$ | The market agrees that WMK is a low-to-moderate growth retailer driven by modest same-store gains and minor footprint expansion. |
| **Net Income Margin: $2.20\%$** | $~2.20\%$ | The market fully prices in the risk of rising Operating, General, and Administrative (OGA) expenses, acknowledging that margins will likely remain flat and under pressure despite efficiency efforts. |
| **Discount Rate (Risk): $8.0\%$** | Implied WACC/Discount Rate is $\approx 8.0\%$ | The market assesses the risk (cost of capital) of WMK as relatively low, consistent with a defensive, low-beta grocery business. |
| **Terminal Growth Rate: $1.0\%$** | $\approx 1.0\%$ | The market assumes WMK will generate perpetual cash flow growth slightly below inflation, typical for a mature, regional retailer. |

The market is making a rational, conservative assessment of Weis Markets, Inc. as a defensive, low-growth regional grocery chain, which is consistent with the explicit management commentary on rising costs and modest comparable sales growth. The fair value calculation of **\$69.10** simply quantifies the implied valuation currently in the stock price.
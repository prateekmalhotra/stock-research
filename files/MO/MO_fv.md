This valuation of Altria Group, Inc. (MO) stock is performed using a Discounted Cash Flow (DCF) model based on projecting the company's Adjusted Net Income (as a proxy for cash flow, per instructions) and applying an incremental Return on Invested Capital (ROIC) model. All values are in millions of U.S. Dollars, except for per-share data.

---

## 1. Initial Financial Data

The valuation is anchored to Altria's latest full-year reported financials and recent management guidance.

| Metric | Value (USD) | Source/Notes |
| :--- | :--- | :--- |
| **Current Stock Price** | **\$67.01** | Closing price as of Feb 12, 2026. |
| **Shares Outstanding** | **1,680 million** | Used a conservative recent figure. |
| **Total Cash & Equivalents (Dec 31, 2024)** | **\$3,127 million** | From consolidated balance sheet data. |
| **Total Debt (Dec 31, 2024)** | **\$24,926 million** | Current + Long-term debt. |
| **Adjusted Diluted EPS (2024 Base)** | **\$5.12** | Management's reported base. |
| **Reported Net Income (2024)** | **\$11,236 million** | Full year 2024. |

### Base Year Adjusted Net Income Calculation (2024)

Since Reported Net Income is distorted by one-time items (like the IQOS sale gain), the management-guided **Adjusted Diluted EPS** is used to derive the most representative starting Net Income for projection.

$$
\text{Adjusted Net Income (2024)} = \text{Adjusted Diluted EPS (2024)} \times \text{Shares Outstanding (2024)}
$$

$$
\text{Adjusted Net Income (2024)} = \$5.12 \times 1,690 \text{ million shares} = \mathbf{\$8,619 \text{ million}}
$$

*For a more conservative approach, I will use $\mathbf{\$8,600 \text{ million}}$ as the base Adjusted Net Income (NI) for 2025 calculations.*

---

## 2. Business Engine Analysis & Projection Assumptions

Altria's business model is a high-margin, cash-generative core (Smokeable Products) funding the transition to a high-growth, smoke-free future (Oral Tobacco/NJOY).

### A. Business Engine and Revenue/Net Income Drivers

1.  **Smokeable Products (Core Profit Driver):**
    *   **Driver:** Robust pricing power offset by declining volumes. Cigarette volumes are declining significantly (e.g., 8.2% in Q3 2025).
    *   **Assumption:** The segment will continue to rely on **pricing power** (Net Price Realization) to drive **Operating Companies Income (OCI)** growth, even as revenue declines. Management is guiding to maintain an adjusted OCI margin of at least 60% through 2028. This is a defensive, high-margin business.

2.  **Oral Tobacco Products (Growth Driver):**
    *   **Driver:** *on!* oral nicotine pouches are the key growth vector, with shipment volume increasing (11% in 2025). The acquisition of NJOY is a major focus.
    *   **Assumption:** The smoke-free portfolio growth will be partially offset by major upfront investments and a challenging illicit e-vapor market, leading to a slower initial impact on *consolidated* net income.

3.  **Management Guidance (EPS CAGR):** Management guides for a **mid-single-digits** Adjusted Diluted EPS compounded annual growth rate (CAGR) through 2028. This is the most conservative and reliable metric for projecting future profitability. I will use the **lower end** of the *mid-single-digit* range for my conservative growth rate assumptions.

### B. Conservative Financial Projection Assumptions

| Metric | 2026 Assumption | 2027-2028 Assumption | 2029-2030 Assumption | Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Annual NI Growth Rate** | **4.0%** | **4.0%** | **2.0%** | **2026:** Mid-point of 2026 EPS guidance (2.5%-5.5%) implies a NI growth rate, I use 4.0%. **2027-2028:** Lower end of management's "mid-single digits" CAGR guidance (3%-5% is often mid-single digits, I use 4.0%). **2029-2030:** A conservative deceleration as core declines accelerate and future smoke-free growth is uncertain/slowing. |
| **Discount Rate** | **9.0%** | | | Represents a moderate-to-high Cost of Equity for a company with MO's risk profile (litigation, regulation, declining core). |
| **Terminal Growth Rate (g)** | **1.0%** | | | Highly conservative, less than U.S. GDP/inflation, appropriate for a company whose core product is in secular decline. |
| **Return on Invested Capital (ROIC)** | **7.0%** | | | Based on historical figures and a conservative estimate of the return on retained earnings, lower than the high historical rates (which are often inflated by asset sales/write-downs). A reasonable, conservative, positive rate is assumed. |

---

## 3. Projected Net Income (as Cash Flow Proxy)

The valuation follows the specific instruction: $\text{Net Income}_n = \text{Net Income}_{\text{base}} \times (1 + \text{Growth Rate}) + \text{ROIC} \times \text{Retained Earnings}_{n-1}$.

*   **Year 2025 (Base):** Adjusted NI is derived from 2024 Base NI and 2025 guidance.
    *   2025 Adjusted EPS guidance is \$5.22 to \$5.37. I use the midpoint $\approx \$5.30$.
    *   $\text{Adjusted Net Income (2025)} = \$5.30 \times 1,680 \text{ million shares} = \mathbf{\$8,904 \text{ million}}$.

| Year | Projected NI from Growth (A) | ROIC Income (B) (7.0% ROIC) | Total Projected NI (A+B) | Retained Earnings | Discount Factor (9.0%) | Net Present Value (NPV) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2025 (Base)** | - | - | \$8,904 | \$8,904 | 0.917 | \$8,165 |
| **2026** | \$9,260 (NI 2025 x 1.04) | \$623 (NI 2025 x 7.0%) | **\$9,883** | \$18,787 | 0.842 | \$8,321 |
| **2027** | \$9,630 (NI 2026 x 1.04) | \$1,315 (Retained 2026 x 7.0%) | **\$10,945** | \$29,732 | 0.772 | \$8,451 |
| **2028** | \$10,015 (NI 2027 x 1.04) | \$2,081 (Retained 2027 x 7.0%) | **\$12,096** | \$41,828 | 0.708 | \$8,565 |
| **2029** | \$10,381 (NI 2028 x 1.02) | \$2,928 (Retained 2028 x 7.0%) | **\$13,309** | \$55,137 | 0.649 | \$8,638 |
| **2030** | \$10,589 (NI 2029 x 1.02) | \$3,860 (Retained 2029 x 7.0%) | **\$14,449** | \$69,586 | 0.596 | \$8,619 |
| **Total NPV (2025-2030)** | | | | | | **\$50,759** |

*Note: For projection, Net Income (NI) is used as the proxy for Free Cash Flow (FCF), and Retained Earnings is the cumulative sum of prior years' NI.*

---

## 4. Terminal Value Calculation

The Terminal Value (TV) captures the value of all cash flows after 2030.

$$
\text{Terminal Value} = \frac{\text{Projected Net Income}_{2030} \times (1 + \text{Terminal Growth Rate})}{\text{Discount Rate} - \text{Terminal Growth Rate}}
$$

$$
\text{Terminal Value} = \frac{\$14,449 \times (1 + 0.01)}{0.09 - 0.01} = \frac{\$14,593}{\mathbf{0.08}} = \mathbf{\$182,413 \text{ million}}
$$

### Terminal Value Net Present Value (TV NPV)

The Terminal Value must be discounted back to the present (beginning of 2025) by multiplying it by the discount factor for the last projected year (2030).

$$
\text{TV NPV} = \text{Terminal Value} \times \text{Discount Factor}_{2030}
$$

$$
\text{TV NPV} = \$182,413 \text{ million} \times 0.596 = \mathbf{\$108,740 \text{ million}}
$$

---

## 5. Fair Value Calculation

### A. Total Equity Value

$$
\text{Total Equity Value} = \text{Total NPV} + \text{TV NPV} + \text{Cash} - \text{Total Debt}
$$

$$
\text{Total Equity Value} = \$50,759 \text{ million} + \$108,740 \text{ million} + \$3,127 \text{ million} - \$24,926 \text{ million} = \mathbf{\$137,700 \text{ million}}
$$

### B. Fair Value Per Share

$$
\text{Fair Value Per Share} = \frac{\text{Total Equity Value}}{\text{Shares Outstanding}}
$$

$$
\text{Fair Value Per Share} = \frac{\$137,700 \text{ million}}{1,680 \text{ million shares}} = \mathbf{\$81.96 \text{ per share}}
$$

---

## Fair Value and Justification

The calculated Fair Value of Altria Group, Inc. (MO) stock is **\$81.96 per share**.

| Metric | Value |
| :--- | :--- |
| **Fair Value Per Share** | **\$81.96** |
| **Current Market Price** | **\$67.01** |
| **Implied Upside** | **22.3%** |

### Justification and Market Assumption Analysis

My calculated fair value of **\$81.96** is substantially higher (22.3% upside) than the current market price of **\$67.01**. This difference implies that the market is currently making more conservative assumptions about Altria's future cash flows than my valuation model.

**Reasons for the Discrepancy (Why the Market is More Conservative):**

1.  **Accelerating Decline in the Core Business:** The market likely assumes the volume decline in the high-margin smokeable products segment will accelerate faster than the 4% annual growth I have projected through 2028. An 8-10% annual volume decline, compounded by increasing excise taxes, makes the pricing power necessary for OCI growth an increasingly high hurdle.
2.  **Smoke-Free Headwinds:** While *on!* and *NJOY* are growth drivers, the market is skeptical about Altria's ability to transition due to the massive competitive advantage of rival Philip Morris International's *ZYN* and the regulatory uncertainty/proliferation of illicit e-vapor products. The market is penalizing MO for the slow success and high investment costs in the smoke-free portfolio.
3.  **High Debt and ROIC Skepticism:** While the debt-to-EBITDA ratio (approx. 2.0x) is within management's target, the high absolute debt level and the use of Net Income (which can be volatile) as the FCF proxy may overstate the actual recurring cash available for debt reduction or additional growth investment. The market may discount future cash flows more heavily due to this perceived balance sheet risk and be skeptical of my 7.0% ROIC assumption.
4.  **Regulatory/Litigation Risk:** Altria is perpetually exposed to significant regulatory risk (e.g., potential menthol ban, FDA restrictions) and litigation, which the market is likely factoring in with a higher implied discount rate than my conservative 9.0%.

**My Case for the Higher Fair Value:**

My valuation is defensible because it uses the most conservative, management-guided internal metrics and makes reasonable long-term assumptions:

1.  **Conservative Growth Rates:** My long-term growth assumption of **4.0% CAGR (2026-2028)** is based on the *low end* of the "mid-single-digits" guidance. My subsequent reduction to **2.0% (2029-2030)** is highly conservative and factors in the eventual acceleration of core business decline.
2.  **Sustainable High Margin:** The core business's exceptional pricing power to maintain **>60% OCI margins** is a demonstrated characteristic that supports the continued generation of strong cash flows, even with declining volumes.
3.  **Conservative Terminal Growth:** A Terminal Growth Rate of **1.0%** is extremely conservative for a going concern and builds in a permanent headwind for the industry.

In conclusion, the market is primarily focused on the **terminal decline risk** of the core business, discounting the sustained profitability and the long-term potential of the smoke-free transition. My valuation assumes the transition, while slow and costly, will ultimately *sustain* the 4.0% adjusted net income growth rate until 2028, leading to a higher intrinsic value.
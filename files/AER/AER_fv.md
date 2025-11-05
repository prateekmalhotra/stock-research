This valuation of AerCap Holdings N.V. (AER) stock is based on a conservative Discounted Cash Flow (DCF) analysis, utilizing data exclusively from recent SEC filings and management commentary from earnings call transcripts. All figures are in millions of U.S. Dollars (USD) unless otherwise noted.

## 1. Initial Financial Metrics

The following metrics are derived from AerCap's latest available financial report (Q3 2025 6-K, as of September 30, 2025).

| Metric | Value (USD Millions) | Source Justification |
| :--- | :--- | :--- |
| **Total Cash & Cash Equivalents** | $1,912 | This figure represents "Total cash, cash equivalents and restricted cash" as reported in the Q3 2025 financial statements and is used as the proxy for highly liquid assets. |
| **Total Debt** | $44,029 | This is the reported total consolidated debt as of September 30, 2025. |
| **Shares Outstanding** | 166.16 million | Ordinary shares outstanding, excluding unvested restricted stock, as of September 30, 2025. This is used for the per-share calculation. |

## 2. Business Engine and Financial Projections

AerCap's core business engine is driven by the vast global demand for aircraft leasing, fueled by the significant and long-term production and delivery delays from major Original Equipment Manufacturers (OEMs) like Boeing and Airbus.

**Business Engine Justification:**
*   **Core Driver: Supply/Demand Imbalance:** Management has repeatedly noted that OEM production rates are "miles below" where they need to be, a situation expected to last "through the end of this decade." This creates an "extraordinarily acute" supply imbalance, leading to higher lease rates and a tight market for both new and older aircraft.
*   **Performance Metrics:** The demand strength is evident in the operational metrics: utilization rates topping **99%** and a widebody lease extension rate of **100%** in Q3 2025.
*   **Margin Expansion:** The strong demand has led to a "significant increase in the lease trends," resulting in a net spread of **8%** in Q3 2025, the highest in five years.
*   **Gain-on-Sale:** AerCap consistently generates profits from asset sales, with a record \$332 million gain-on-sale in Q3 2025. Management notes this is a "repeatable and profitable aspect of our earnings" for over 40 quarters. For a conservative DCF, we will model this as a consistent component of Net Income.

### Revenue and Net Income Projections

**2025 Baseline:**
*   **2025 Adjusted EPS Guidance:** Management has raised its full-year 2025 adjusted EPS guidance to approximately **\$13.70**, which includes gains on sale from the first three quarters but excludes any further gains for Q4.
*   **2025 Adjusted Net Income (Base):** \$13.70 EPS * 166.16 million shares = **\$2,276.79 million** (We use this as the starting point for Net Income, despite being "Adjusted," as it reflects management's core earning power expectation).
*   **Effective Tax Rate (ETR):** The Q3 2025 ETR of **14.5%** is used for future tax estimation.
*   **Total 2025 Revenue (Estimate):** Q3 2025 Revenue was $\sim\$2.31$ billion. Basic Lease Rents for Q3 2025 were \$1.69 billion. Assuming a slight increase in Q4 due to new deliveries, and a Q1-Q2 average of $\sim\$1.89$ billion in Q2 and $\sim\$2.08$ billion in Q1, a full-year revenue of $\sim\$8.0$ billion is a reasonable and conservative estimate.

**Future Revenue Growth Rate (2026-2030):**
*   **Conservative Assumption:** Given the extreme market tightness, **3.5%** annual revenue growth is assumed for all years (2026-2030). This is a highly conservative rate, significantly below the company's Q3 2025 performance run-rate and the stated market dynamic, which provides a strong margin of safety.

**Net Income Margin:**
*   For consistency and conservatism, we will not try to recreate the entire P&L but will use the 2025 Net Income base and assume a conservative, consistent **Net Income Margin** on the projected revenue.
    *   2025 Estimated Revenue: \$8,000 million (conservative run-rate)
    *   2025 Estimated Net Income: \$2,276.79 million
    *   2025 Net Income Margin: $2,276.79 / $8,000 $\approx$ **28.46%**.
*   We will apply this **28.46%** Net Income Margin to all projected years.

**Return on Invested Capital (ROIC) & Reinvestment:**
*   **ROIC Assumption:** Adjusted Return on Equity (ROE) was **19%** in Q3 2025. Management is actively investing in new equipment at "accretive returns." For the model, a conservative **ROIC of 10%** is assumed on all prior year's Net Income that converts to cash. This is a safe assumption, well below the reported ROE, ensuring prudence.
*   **Cash Flow Calculation:** Net Income for the following year is calculated as:
    *   $NI_{Year\_N} = (\text{Projected Revenue}_{Year\_N} * 28.46\%) + (\text{Net Income}_{Year\_N-1} * 10\%)$

### Projected Financials (USD Millions)

| Year | Projected Revenue (3.5% growth) | Net Income (Base Margin) | ROIC Income (10% on prior NI) | Total Projected Net Income (FCF) |
| :--- | :--- | :--- | :--- | :--- |
| **2025** | 8,000.00 | 2,276.79 | 0.00 | **2,276.79** |
| **2026** | 8,280.00 | 2,359.18 | 227.68 | **2,586.86** |
| **2027** | 8,569.80 | 2,444.65 | 258.69 | **2,703.34** |
| **2028** | 8,869.79 | 2,533.36 | 270.33 | **2,803.69** |
| **2029** | 9,180.88 | 2,625.48 | 280.37 | **2,905.85** |
| **2030** | 9,502.61 | 2,721.17 | 290.59 | **3,011.76** |

---

## 3. Discounted Cash Flow (DCF) Analysis

### DCF Assumptions

| Metric | Assumption | Justification |
| :--- | :--- | :--- |
| **Risk-Free Rate (Rf)** | 4.0% | Conservative proxy for long-term safe rate. |
| **Equity Risk Premium (ERP)** | 6.0% | Standard, reasonable long-term ERP. |
| **Beta** | 1.1 | Conservative assumption for a highly levered and cyclical, though currently very strong, leasing company. |
| **Cost of Equity (Ke)** | 10.6% | $K_e = R_f + \beta \times ERP = 4.0\% + 1.1 \times 6.0\% = 10.6\%$ |
| **Cost of Debt (Kd)** | 4.0% | Based on AerCap's Q3 2025 average cost of debt of 4.0%. |
| **Tax Rate (t)** | 14.5% | Based on AerCap's Q3 2025 Effective Tax Rate. |
| **Debt to Capital (D/C)** | 70% | Approximated from the company's debt-heavy structure and adjusted debt/equity ratio (2.1:1). |
| **WACC (Discount Rate)** | **5.59%** | $WACC = [E/C \times K_e] + [D/C \times K_d \times (1-t)]$ |
| **Maturity (Terminal) Growth Rate (g)** | **2.0%** | Very conservative, below long-term global GDP growth, justified by AerCap's business model having a finite, depreciating asset base. |

*WACC Calculation:* $[30\% \times 10.6\%] + [70\% \times 4.0\% \times (1 - 0.145)] = 3.18\% + 2.38\% \approx **5.59\%**$.

### Net Present Value (NPV) Calculation

The Cash Flow (Net Income) is discounted back to the present value using the 5.59% WACC.

| Year | Projected Net Income (FCF) | Discount Factor (5.59% WACC) | Net Present Value (NPV) |
| :--- | :--- | :--- | :--- |
| **2025** | 2,276.79 | 0.947 | 2,156.24 |
| **2026** | 2,586.86 | 0.897 | 2,320.14 |
| **2027** | 2,703.34 | 0.849 | 2,295.42 |
| **2028** | 2,803.69 | 0.804 | 2,253.94 |
| **2029** | 2,905.85 | 0.761 | 2,211.75 |
| **2030** | 3,011.76 | 0.720 | 2,168.47 |
| **Total NPV of Explicit Period (2025-2030)** | | | **13,405.96** |

### Terminal Value Calculation

The Terminal Value is calculated using the Gordon Growth Model: $TV_{2030} = \frac{FCF_{2031}}{WACC - g}$

*   $FCF_{2031} = FCF_{2030} \times (1 + g) = \$3,011.76 \times (1 + 0.02) = \$3,071.99$
*   $TV_{2030} = \frac{\$3,071.99}{0.0559 - 0.02} = \frac{\$3,071.99}{0.0359} = \$85,570.75$

**NPV of Terminal Value:**
*   $NPV(TV) = TV_{2030} \times \text{Discount Factor}_{2030} = \$85,570.75 \times 0.720 = \$61,610.94$

**Total Enterprise Value (NPV):**
*   Total NPV = NPV of Explicit Period + NPV of Terminal Value
*   Total NPV = \$13,405.96 + \$61,610.94 = **\$75,016.90 million**

---

## 4. Fair Value Calculation

| Metric | Value (USD Millions) |
| :--- | :--- |
| **Total Enterprise Value (NPV)** | $75,016.90 |
| **Add: Total Cash & Equivalents** | $1,912.00 |
| **Subtract: Total Debt** | $44,029.00 |
| **Total Equity Value** | **$32,909.90** |
| **Shares Outstanding (in millions)** | 166.16 |
| **Fair Value per Share** | **$198.06** |
| **Current Stock Price (Assumed)** | $120.00* |

*\*Note: The current market price of the stock is not available through search and must be assumed for the final comparison. A placeholder of $120.00 is used for the justification step.*

## 5. Comparison and Justification

The calculated **Fair Value per Share is \$198.06**, which is significantly higher than the assumed market price of $\sim\$120.00$.

### Why is the Fair Value so different from the Market Value?

The primary reason for the large divergence is the market's likely discounting of two major factors that are central to the AerCap business:

1.  **Risk of a Global Cycle Turn and Interest Rate Risk:** AerCap is an aviation leasing company, a business fundamentally tied to the health of the global airline industry and highly sensitive to interest rates (Cost of Debt). The market is likely pricing in a significant risk premium for:
    *   **The Next Downturn:** The cycle is currently extremely strong, as noted by management (99% utilization, high lease rates). The market fears the inevitable next cyclical downturn when utilization will drop, and lease rates will fall. Our model assumes a steady, conservative growth rate (3.5%) anchored to a strong, consistent Net Income Margin (28.46%), which effectively smooths out this cyclicality. The market demands a higher discount rate than our calculated **5.59% WACC** to account for this inherent business volatility.
    *   **High Debt Burden:** The market is cautious of the high **\$44.03 billion** debt load. Any sudden, sharp rise in their cost of debt could severely compress margins. Our model assumes a stable Cost of Debt (4.0%), which the market views as a major risk in an uncertain interest rate environment.

2.  **Uncertainty and Non-Recurring Nature of Ukraine Recoveries and Gains on Sale:**
    *   AerCap's recent reported Net Income has been significantly boosted by insurance and other recoveries related to the lost Russian fleet (total recoveries since 2023 of \$2.9 billion). While we used the *Adjusted* Net Income for the baseline, the market may see the entire environment as temporarily inflated by these one-time cash windfalls.
    *   The high **Gain-on-Sale** margins (Q3 2025 was 28% unlevered margin) are considered "repeatable" by management, but the market views asset sales as more volatile and less predictable than core lease revenue. A more conservative market model would heavily discount the portion of Net Income derived from asset sales, which our model included as part of the total Net Income Margin.

**Conclusion:**

Our conservative DCF model, which is based on management's stated high-margin, high-demand environment and a realistic long-term ROIC, suggests a **Fair Value of \$198.06 per share**. The difference with the market price represents the market's perception of **long-term cyclical risk and financial leverage risk** in the aviation industry, demanding a significantly higher discount rate than our 5.59% WACC to justify the current stock price. AerCap's management is currently executing extremely well to close this value gap through aggressive share repurchases and reinvestment into its high-return new-technology fleet.
# Valuation of eBay Inc. (EBAY) Stock

This valuation is based on a Discounted Cash Flow (DCF) model using a projected stream of Net Income, a business-engine-driven revenue projection, and financial data directly sourced from eBay Inc.'s SEC filings and earnings call transcripts. The base date for the valuation is the end of the latest reported fiscal year or quarter (primarily December 31, 2024, for balance sheet items and full-year results, with projections based on Q3 2025 guidance).

## 1. Initial Financial Figures

The financial data is based on the company's Fourth Quarter and Full Year 2024 results, and subsequent Q1/Q2/Q3 2025 information, primarily sourced from the 2024 Form 10-K and 2025 Quarterly Reports and earnings press releases.

| Metric | Value (USD Millions) | Source/Calculation |
| :--- | :--- | :--- |
| **Total Cash & Cash Equivalents (Liquid Assets)** | \$7,200 | As of December 31, 2024, including cash and non-equity investments, which represents liquid assets in hand. |
| **Short-term Debt** | \$1,673 | As of December 31, 2024. |
| **Long-term Debt** | \$5,752 | As of December 31, 2024. |
| **Total Debt** | **\$7,425** | (\$1,673 + \$5,752) |
| **Diluted Shares Outstanding** | **459 million** | As of June 30, 2025 (latest available share count from Q2 2025 data). |
| **2024 Net Revenue (Actual Baseline)** | \$10,300 | Full Year 2024 Revenue. |
| **2024 GAAP Net Income (Actual Baseline)** | \$1,981 | Full Year 2024 GAAP Net Income from Continuing Operations. |

---

## 2. Business Engine Analysis & Revenue Projections (2025-2030)

The core business engine for eBay is currently focused on shifting Gross Merchandise Volume (GMV) to **"Focus Categories"** (Motors, Collectibles, Luxury Fashion) and increasing the **"Take Rate"** (Revenue / GMV) through higher-margin services like **First-Party Advertising** and **Managed Payments** [cite: 4 (step 1), 8 (step 1), 10 (step 1)].

| Metric | 2024 Actual | 2025 Projection | 2026 Projection | 2027 Projection | 2028 Projection | 2029 Projection | 2030 Projection |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **A. Net Revenue (USD Millions)** | **\$10,300** | **\$11,000** | **\$11,798** | **\$12,683** | **\$13,636** | **\$14,642** | **\$15,699** |
| **B. Net Income Margin (GAAP %)** | **19.23%** | **19.50%** | **20.00%** | **20.50%** | **21.00%** | **21.50%** | **22.00%** |
| **C. Revenue Growth Rate** | 2.0% | 6.80% | 7.25% | 7.50% | 7.50% | 7.38% | 7.22% |

### Justification for Projections:

*   **2025 Revenue:** Based on the midpoint of the company's full-year 2025 guidance of \$10.97 billion to \$11.03 billion.
*   **GMV Growth (Assumption):** eBay's GMV growth has been modest (2% in FY 2024). I assume a conservative, steady growth of **1.5% per year** for overall GMV, reflecting the slow-growth but stable nature of the broad e-commerce market.
*   **Take Rate & Revenue Growth (Engine):** Revenue growth is projected to outpace GMV growth due to the monetization strategy. The 2024 implied Take Rate was $\sim 13.8\%$ (\$10.3B Revenue / $\sim$ \$74.7B GMV). The 2025 revenue guidance implies a Take Rate of $\sim 14.7\%$ (\$11.0B Revenue / $\sim$ \$74.7B GMV * 1.015). This represents an increase of **$\sim$90 bps** (0.9%) from 2024 to 2025. I project the increase in Take Rate will continue but gradually slow down as the market is saturated with ads and payments: **+60 bps in 2026**, **+50 bps in 2027**, **+40 bps in 2028**, **+30 bps in 2029**, and **+20 bps in 2030**. This persistent, engine-driven increase in Take Rate is the primary source of revenue acceleration and justification for the Revenue Growth Rate in Row C.

*   **Net Income Margin (NIM) (Assumption):** The 2024 GAAP NIM was 19.23%. Management's focus on cost discipline and operating leverage from the increasing Take Rate suggests margin expansion [cite: 2 (step 2), 5 (step 3)]. I conservatively project NIM to increase by only **0.50% per year** (e.g., 19.5% in 2025, 20.0% in 2026, etc.), which is a modest increase given the high Non-GAAP Operating Margin in the 27-28% range and a guided Non-GAAP tax rate of 16.5% [cite: 4 (step 3), 2 (step 2)].

---

## 3. Discounted Cash Flow (DCF) Calculation

The Net Income from the previous year is assumed to become cash for the next year. An additional income from Return on Invested Capital (ROIC) is then generated from that cash. Since eBay is focused on share repurchases and dividends, and its cash from operating activities significantly exceeds its capital expenditures, the projection relies on Net Income as a proxy for unlevered cash flow, adjusted for the compounding effect of retained earnings via ROIC.

### Assumptions:

*   **Return on Invested Capital (ROIC):** The past ROIC for eBay has been volatile. To be **conservative but reasonable** and reflect positive net income reinvestment, a fixed annual ROIC of **10.0%** is used.
*   **Discount Rate (Conservative but Reasonable):** A **9.0%** discount rate is used, reflecting the company's established, low-growth business model and medium-high-risk profile in a highly competitive e-commerce sector.
*   **Terminal Maturity Rate (Conservative):** A very conservative long-term growth rate of **2.0%** is assumed for the terminal value, reflecting long-term global e-commerce inflation and an anchor to the conservative projected GMV growth.

### Net Income & Discounted Cash Flow Table (in millions USD)

| Year | Net Revenue | Net Income Margin (B) | Net Income from Operations | Previous Year's Cash from NI | ROIC (10.0%) | Total Net Income (Cash Flow) | Discount Factor (9.0%) | Net Present Value (NPV) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2024 (Base)** | \$10,300 | 19.23% | \$1,981 | - | - | **\$1,981** | - | - |
| **2025** | \$11,000 | 19.50% | \$2,145 | \$1,981 | \$198 | **\$2,343** | 0.9174 | **\$2,149** |
| **2026** | \$11,798 | 20.00% | \$2,360 | \$2,343 | \$234 | **\$2,594** | 0.8417 | **\$2,183** |
| **2027** | \$12,683 | 20.50% | \$2,600 | \$2,594 | \$259 | **\$2,859** | 0.7722 | **\$2,208** |
| **2028** | \$13,636 | 21.00% | \$2,864 | \$2,859 | \$286 | **\$3,150** | 0.7084 | **\$2,231** |
| **2029** | \$14,642 | 21.50% | \$3,148 | \$3,150 | \$315 | **\$3,463** | 0.6499 | **\$2,251** |
| **2030** | \$15,699 | 22.00% | \$3,454 | \$3,463 | \$346 | **\$3,800** | 0.5963 | **\$2,265** |
| **Sum of Projected NPVs (2025-2030)** | | | | | | | | **\$13,287** |

**Terminal Value Calculation (End of 2030):**

*   Terminal Value = [2030 Net Income * (1 + Terminal Maturity Rate)] / (Discount Rate - Terminal Maturity Rate)
*   Terminal Value = [\$3,800 * (1 + 0.02)] / (0.09 - 0.02)
*   Terminal Value = \$3,876 / 0.07 = **\$55,371 million**

**Terminal Value Net Present Value (NPV):**

*   Terminal NPV = Terminal Value * 2030 Discount Factor
*   Terminal NPV = \$55,371 million * 0.5963 = **\$33,026 million**

**Total Enterprise Value (TEV):**

*   Total TEV = Sum of Projected NPVs + Terminal NPV
*   Total TEV = \$13,287 million + \$33,026 million = **\$46,313 million**

---

## 4. Fair Value Calculation

| Metric | Value (USD Millions) |
| :--- | :--- |
| **Total Enterprise Value (TEV)** | **\$46,313** |
| Add: Total Liquid Assets (Cash) | +\$7,200 |
| Subtract: Total Debt | -\$7,425 |
| **Total Equity Value** | **\$46,088** |
| Shares Outstanding (Diluted) | 459 million |
| **Fair Value Per Share** | **\$100.41** |
| *(Current Market Price - Hypothetical)* | *\$60.00* |

**Fair Value Per Share: \$100.41**

---

## 5. Justification and Market Comparison

The calculated **Fair Value Per Share of \$100.41** is significantly higher than the hypothetical current market price of \$60.00. This implies the market is making much more pessimistic assumptions about eBay's future performance.

### Justification for the Discrepancy:

The market is likely discounting EBAY's shares for the following reasons, which contrast with the valuation's assumptions:

1.  **Low/Negative GMV Growth and Competition:** The market is likely modeling a continuation of near-stagnant or even declining GMV, which has been flat to low single-digit for several years [cite: 1 (step 1), 4 (step 1)]. The market is likely concerned that eBay cannot meaningfully compete with hyper-growth e-commerce giants and specialized vertical marketplaces, and thus, views the **1.5% GMV growth assumption** as too optimistic.
2.  **Take Rate Saturation Risk:** The valuation relies heavily on the continued growth of the Take Rate from advertising and managed payments. The market may believe that the low-hanging fruit of this monetization strategy is nearly exhausted, and significant further Take Rate increases will alienate core sellers, leading to a much faster decline in the **Take Rate increase (e.g., +20 bps per year, or a flat rate after 2025)** than the projected path.
3.  **Low ROIC/Terminal Rate:** The market may assign a lower perceived Return on Invested Capital (ROIC) than the **10.0%** used, reflecting skepticism about the capital-intensive nature of sustaining growth and the lack of a genuine "moat." Furthermore, a lower terminal growth rate (e.g., 0% to 1%) would drastically reduce the Terminal Value.
4.  **Risk Premium (Higher Discount Rate):** The market might be applying a higher risk premium and therefore a higher discount rate (e.g., 10-12%) due to the uncertain macroeconomic outlook for discretionary spending and the structural challenges of revitalizing an aging marketplace brand.

In conclusion, the **\$100.41 fair value is an intrinsic value based on the company successfully executing its strategy of growing the Take Rate through enhanced monetization and shifting to higher-value Focus Categories (Motors, Collectibles, etc.), even with only modest GMV growth.** The market is essentially pricing in an execution failure or a higher degree of competitive pressure that will prevent the monetization engine (Take Rate increase) from compensating for the lackluster volume growth. If the market were to adopt the business engine assumptions laid out in this valuation, the stock price would nearly double.
# Evaluation: EOG Resources, Inc. (EOG) — 2026-10-08
## Bear case
This is a price-taker sitting at the top of its own valuation range: P/E 11.3x is at the 92nd percentile of its 5y range and EV/EBITDA 5.5x at the 75th [Certain]. The cheapness against peers (P/E -30%) mostly reflects peers' depressed earnings, not a mispricing of EOG [Likely]. Fundamentals have trended down for five years: ROIC 20.7%→16.0%, FCF margin 25.0%→15.2% FY21-25, and net debt/EBITDA moved from -0.10x to 0.49x in FY2025 [Certain]. TTM results have been flattered by strong oil prices, so they are the high-water mark [Likely]. The macro overlay flags a stronger dollar and a +0.48pp jump in real yields as a headwind for oil prices (small bear tilt) [Likely]. A CFO change ahead of Q3 results on Nov 5 adds some uncertainty about capital allocation [Guessing].

## Bull case
EOG is the low-cost, multi-basin operator, with TTM ROIC 19.8% and ROE 22.5% [Certain]. It has an 8.74% FCF yield, P/FCF 11.4x at the 15th percentile of its 5y range, and 96.2% FCF conversion TTM [Certain]. Buybacks cut shares 3.33% YoY, and management directs most FCF to shareholders [Likely]. The balance sheet is close to unlevered (0.23x net debt/EBITDA, Altman Z 3.69, Piotroski 7) [Certain], and beta is 0.37 [Certain]. The FY21-25 decline looks cyclical, not competitive [Likely].

## Decision
```json
{
  "ticker": "EOG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, low-leverage, low-cost E&P with an 8.74% FCF yield, but it sits near the top of its own 5y P/E and EV/EBITDA range while returns and margins have trended down, so the price already reflects mid-cycle commodity strength.",
  "rationale": "Quality and shareholder returns are real, but EOG is not cheap against its own history on earnings or EBITDA. Its returns have trended down for five years, and its revenue depends on oil prices, which the macro overlay tilts slightly negative. Good but not compelling: conviction 3 is below the buy threshold, so AVOID and keep the cash.",
  "price_at_decision": 144.21,
  "price_date": "2026-10-07",
  "research_note": "research/EOG/2026-10-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, well under the FY2025 low of 16.0%, which would show the cost advantage eroding rather than a cyclical dip.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 15%, under the FY2025 5-year low of 15.2%, which would show cash generation deteriorating structurally.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "FCF conversion (FCF/NI) stays below 50% for two consecutive fiscal years on the cash-flow and income-statement pages (FY2025 was 69.3%)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 158, "basis": "P/FCF re-rates from 11.4x (15th percentile) to its 5y median of 12.5x on TTM FCF [RA], supported by the 8.74% FCF yield and 3.33% annual share shrink [ST]."},
    "base": {"probability": 0.45, "target_price_12m": 145, "basis": "EV/EBITDA holds at 5.5x, the top of a tight 5.3x-5.5x 5y range [RA], on roughly flat TTM EBITDA, so returns come only from buybacks and the dividend."},
    "bear": {"probability": 0.30, "target_price_12m": 119, "basis": "P/E falls back to its 5y minimum of 9.3x on TTM EPS [RA] as oil-driven margins revert toward FY2025 levels [IS]; the macro overlay's small bear tilt (dollar and real yields, research/EOG/2026-10-08-macro.md) moved 5pp of probability from bull to bear."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

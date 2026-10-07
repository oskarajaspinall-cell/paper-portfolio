# Evaluation: NetEase, Inc. (HKG:9999) — 2026-10-07

## Bear case
Ownership rests on VIE contracts covering 85.2% of FY2025 revenue that PRC authorities could challenge [Certain]. Tighter rules on minors' playtime, loot boxes and game approvals could cap monetization at any time [Certain]. That risk is why the stock trades at 16.0x P/E, and it may never re-rate [Likely]. Earnings depend on hits, and the 35.2% TTM operating margin may be a cyclical peak driven by recent titles [Guessing]. Shares outstanding still rose 0.39% YoY despite buybacks, so stock-based compensation is diluting holders [Certain]. Price momentum is weak: -21.6% over 12 months, -38.0pp versus SPY, and below both the 50-day and 200-day moving averages [Certain]. The 368.3% ROIC is inflated by a tiny invested-capital base, so it overstates franchise quality [Likely].

## Bull case
Quality has improved every year. Gross margin rose from 53.6% to 67.2% TTM, operating margin from 18.7% to 35.2% and FCF margin from 26.6% to 43.5% [Certain]. Earnings are backed by cash, with FCF conversion at 156.0% [Certain]. The net cash balance sheet (-3.76x net debt/EBITDA) absorbs regulatory shocks [Certain]. Valuation does not reflect this. EV/EBITDA (8.2x) and P/FCF (10.1x) sit below their own 5-year minimums, P/E is 27% below the peer median, and the FCF yield is 9.86% [Certain]. A deep self-developed IP catalogue extends game lifecycles [Likely]. Beta of 0.77, an Altman Z of 8.53 and a Piotroski F of 6 point to low fundamental fragility [Certain]. Even if the multiple does not re-rate, the 9.86% FCF yield gives a high-single-digit return as long as margins hold [Likely].

## Decision
```json
{
  "ticker": "HKG:9999",
  "decision": "BUY",
  "position_type": "CORE",
  "core_initiation": false,
  "conviction": 4,
  "thesis": "A net-cash, high-margin game developer with five years of rising returns trades below its own 5-year EV/EBITDA and P/FCF minimums and at a 9.86% FCF yield, which prices in a regulatory overhang rather than the quality it has delivered.",
  "rationale": "Quality is exceptional and still improving, cash conversion is strong and valuation is at historic lows on cash-flow multiples. The portfolio is all cash, so no limit binds. Conviction is 4 (7%) rather than 5 because VIE and PRC gaming-regulation risk is structural and cannot be diversified away within this single position.",
  "price_at_decision": 185.60,
  "price_date": "2026-10-06",
  "research_note": "research/HKG-9999/2026-10-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2024 level of 28.1%, reversing the five-year expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28.1}},
    {"text": "TTM FCF margin falls below the FY2024 level of 36.5%, signalling cash generation is no longer keeping pace.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 36.5}},
    {"text": "TTM gross margin falls below the FY2024 level of 62.5%, indicating the game portfolio mix or monetization is deteriorating.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 62.5}},
    {"text": "A new PRC regulation materially restricts game monetization, or a VIE-related regulatory action forces deconsolidation, as disclosed in an SEC 20-F/6-K filing."}
  ],
  "replaces": null,
  "replacement_reason": null
}
```

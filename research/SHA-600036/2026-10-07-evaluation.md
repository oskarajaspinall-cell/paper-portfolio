# Evaluation: China Merchants Bank Co., Ltd. (SHA:600036) — 2026-10-07
## Bear case
Profitability is in steady decline: ROE has slid from 15.1% (FY2021) to 11.5% TTM, with no inflection [Certain]. Management's own 2026 outlook is cautious amid low rates and fee pressure, so NIM compression likely continues [Likely]. The stock still trades at a premium to joint-stock peers — P/E 7.1x vs a 5.9x peer median (+21%) and P/B 0.8x vs 0.4x (+93%) — a premium that assumes a quality gap the ROE trend says is narrowing [Certain]. Piotroski F-score is only 4 and shares grew 1.27% YoY with no buyback [Certain]. Earnings are tied to one regulator and one domestic retail-credit cycle, and retail consumer/microloan credit is the stress point [Likely]. The 12-month return of +1.4% lagged SPY by 15.0pp, so the market has not rewarded the franchise [Certain].

## Bull case
CMB is China's best-run retail and wealth franchise, with a low-cost deposit base and asset quality that has held up through the cycle [Likely]. Absolute valuation is undemanding: 7.1x earnings for an 11.5% ROE, and P/B of 0.8x sits in the 18th percentile of its own 5-year range [Certain]. Net margin has risen from 45.2% to 50.3% TTM, showing fee and cost discipline offsetting NIM pressure [Certain]. Fee income returning to growth and retail AUM expansion point to a stabilising earnings mix [Likely]. Beta of 0.47 makes it a genuine diversifier for a new, all-cash portfolio [Certain]. 3-month momentum of +16.2% and price above both moving averages suggest sentiment is turning ahead of the Oct 31, 2026 results [Certain]. A premium to weaker peers is justified, not a flaw [Guessing].

## Decision
```json
{
  "ticker": "SHA:600036",
  "decision": "BUY",
  "position_type": "CORE",
  "core_initiation": false,
  "conviction": 2,
  "thesis": "A best-in-class Chinese retail and wealth bank bought at 0.8x book and 7.1x earnings, with a double-digit ROE and a rising net margin offsetting NIM compression.",
  "rationale": "Absolute valuation is cheap against an 11.5% ROE and low beta diversifies an all-cash book. Size is held to the minimum 3% because ROE keeps falling, the premium to peers leaves little cushion, the F-score is weak and the exposure is single-country and policy-driven.",
  "price_at_decision": 41.26,
  "price_date": "2026-09-30",
  "research_note": "research/SHA-600036/2026-10-07.md",
  "triggers": [
    {"text": "ROE falls below 10%: the quality premium over peers is no longer earned.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "Net (profit) margin falls below 45%: fee and cost mix no longer offsets NIM compression.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 45}}
  ],
  "replaces": null,
  "replacement_reason": null
}
```

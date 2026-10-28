# Evaluation: Eastroc Beverage (Group) Co., Ltd. (SHA:605499) — 2026-10-28
## Bear case
We still cannot say why the stock fell. The only headlines are filing notices, and the fall (12-month -53.2%, 6-month -31.7%) has no dated catalyst [Certain]. The fall is steady, and it comes with real slippage in the numbers. TTM ROCE fell to 28.3% from 51.7% in FY2025, ROE to 34.7% from 51.6%, and FCF conversion to 92.4% from 123.3% in FY2024 [Certain]. Shares rose 6.50% YoY with no buyback shown [Certain]. The most likely reading is that a one-category growth story is maturing while rivals push into energy and hydration drinks [Guessing]. Peak-earnings risk is flagged: the valuation file puts TTM EPS above its 5y median, so the cheap P/E may flatter [Certain]. Q3 results are due Oct 29, 2026, so buying today is a binary bet on an unknown print [Certain]. The 50-day MA is below the 200-day MA, so there is no sign of a bottom [Certain].
## Bull case
Margins have not broken. TTM gross margin is 46.6%, operating margin 25.0% and net margin 21.7%, all at or near five-year highs [Certain]. ROIC is 130.2% with net cash (-2.78x net debt/EBITDA) [Certain]. Every multiple sits below its own 5y minimum: P/E 15.3x against a 31.5x low, and EV/EBITDA 9.1x against 24.4x [Certain]. The stock is also cheaper than the peer median P/E of 19.9x [Certain]. Base fair value of 141.43 is +37.0% above the price, and even the bear value of 104.58 is above it [Certain]. The reverse DCF implies 7.8% year-1 revenue growth fading to terminal, which is modest for a business still widening margins [Likely]. FCF yield is 6.14% [Certain]. If Q3 shows growth intact, the derating could partly reverse [Guessing].
## Decision
```json
{
  "ticker": "SHA:605499",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 130%-ROIC Chinese energy-drink leader with near-record margins trades below its own 5-year minimum on every multiple, but the cause of its 53% fall is unexplained and ROCE, ROE, cash conversion and dilution are all moving the wrong way.",
  "rationale": "Valuation is compelling, but the fall has no identified cause, TTM returns on equity and capital employed have dropped sharply, shares are diluting, and Q3 results land tomorrow. That is good but not compelling: conviction 3, no position. Q3 results, not a lower price, are what would lift conviction.",
  "price_at_decision": 103.21,
  "price_date": "2026-10-27",
  "research_note": "research/SHA-605499/2026-10-28.md",
  "triggers": [
    {"text": "TTM gross margin (statistics page) falls below 40%, under the five-year low of 42.2%, showing competition is eroding pricing.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
    {"text": "TTM net margin (statistics page) falls below 15%, reversing the five-year rise to 21.7%.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC (statistics page) falls below 80%, showing the moat economics are deteriorating.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 80}},
    {"text": "Quarterly revenue (income statement page) declines year on year in the Q3 2026 or later results; conversely, growth intact with stable margins would make the case for a BUY."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 165.0, "basis": "Q3 shows growth intact and part of the derating reverses, with P/E moving toward the peer median 19.9x [RA] on TTM earnings; set well below the mechanical bull 258.32 because the 5y median P/E 38.8x [RA] reflects a growth phase that looks over."},
    "base": {"probability": 0.45, "target_price_12m": 125.0, "basis": "Margins hold (TTM operating margin 25.0% [IS]) but growth slows; set below the base fair value 141.43 because TTM ROCE/ROE have fallen sharply and shares grew 6.50% YoY [RA,ST]."},
    "bear": {"probability": 0.30, "target_price_12m": 90.0, "basis": "Q3 confirms the slowdown and the peak-earnings flag in the valuation file plays out, so earnings revert toward the 5y average; set below the DCF bear 98.80 [IS,CF] because the cause of the -53.2% fall [ST] is unknown."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The stock already sits near the mechanical bear fair value. What blocks a BUY is the unexplained fall, the sharp TTM drop in ROCE/ROE, dilution and the Q3 results due Oct 29, 2026. Re-research after those results; a lower price alone would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

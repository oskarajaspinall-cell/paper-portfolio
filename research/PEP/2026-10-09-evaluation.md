# Evaluation: PepsiCo, Inc. (PEP) — 2026-10-09
## Bear case
Q3 2026 brought an EPS guidance cut despite a revenue beat: soda volumes declined, management is "not satisfied" with the U.S., and cost inflation, mix and a lost tariff benefit hit margins [Certain]. The cheapness is partly flattered by TTM figures: net margin 11.1% and FCF margin 10.7% sit above FY2025's 8.8% and 8.2%, so forward earnings may be lower than the 15.6x P/E suggests [Likely]. The DCF base value of $144.31 is only ~12% above the $128.34 close; most of the blended upside comes from the P/E method assuming a return to historical multiples that a guidance cut doesn't support [Likely]. Price hikes after a value push risk further volume loss [Guessing]. The macro overlay flags rising real yields (2.92%) and a firmer dollar as a headwind for a low-beta staple and its international growth [Certain]. Momentum is weak: -17.1% over 6 months, 31.6pp behind SPY [Certain].
## Bull case
PEP trades at 15.6x P/E and 10.8x EV/EBITDA, below its 5-year minimums (22.2x, 13.1x) and 46% below peers [Certain]. The reverse DCF implies only 0.8% year-1 revenue growth, while Q3 organic growth accelerated to 3.1%, with 8% internationally [Certain]. Quality is intact: ROIC 20.5% and operating margin 16.8% are both up over five years, FCF conversion is 96.1%, and net debt/EBITDA is down to 2.05x [Certain]. Piotroski F-score is 8 and short interest is only 1.90% [Certain]. A 6.0% FCF yield pays investors to wait for a North American turnaround that management is pursuing aggressively through pricing and portfolio pruning [Likely]. The base fair value of $165.21 implies +28.7% [Certain].
## Decision
```json
{
  "ticker": "PEP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A 20.5%-ROIC staple trades below its own 5-year minimum multiples, but a fresh guidance cut, declining U.S. soda volumes and rising real yields leave the re-rating without a near-term driver.",
  "rationale": "Valuation and quality are attractive, but earnings revisions just turned negative, TTM margins look elevated against FY2025, and the DCF base (+12%) offers modest upside without a P/E re-rating. Macro adds a small headwind. This is good but not compelling, so conviction is 3, below the buy threshold. Cash is the acceptable outcome.",
  "price_at_decision": 128.34,
  "price_date": "2026-10-08",
  "research_note": "research/PEP/2026-10-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 15%, versus 16.8% TTM, showing that cost and mix pressure is structural rather than transitory.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 7%, near the FY2022 five-year low of 6.5% and versus 10.7% TTM, signalling the price-hike and reinvestment plan is consuming cash.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 7}},
    {"text": "TTM ROIC falls below 18%, under the FY2021 level of 18.1%, reversing the five-year improvement.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "Positive mind-change trigger: organic revenue growth (earnings release/transcript) stays at or above 3.1% with North America volumes stabilising in the Q4/FY2026 report, removing the guidance-cut overhang."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 165.21, "basis": "North America stabilises and the P/E partly re-rates toward its 22.2x 5y minimum [RA], reaching the fact sheet's base blended fair value; probability trimmed by the macro overlay's small bear tilt (rising real yields, firmer dollar; research/PEP/2026-10-09-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 144.31, "basis": "Organic growth near Q3's 3.1% (transcript) beats the 0.8% the reverse DCF implies, lifting the price to the DCF base value [IS,CF,RA] without a full multiple re-rating, given the guidance cut."},
    "bear": {"probability": 0.30, "target_price_12m": 99.67, "basis": "U.S. soda volumes keep falling and margins revert from the 16.8% TTM toward FY2025 levels [IS], dragging the stock to the fact sheet's bear fair value; probability raised by the macro overlay's small bear tilt (research/PEP/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

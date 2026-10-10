# Evaluation: Occidental Petroleum Corporation (OXY) — 2026-10-10
## Bear case
OXY is a price-taking commodity producer with no pricing power; returns track oil, not management [Certain]. Through the cycle the quality trend is down: ROIC 6.3% (FY21) to 4.3% (FY25), FCF margin 29.1% to 17.7%, ROE -8.4pp over 5y [Certain]. The TTM rebound (ROIC 8.6%, operating margin 25.8%) is an oil-price bounce, and FCF conversion of 62.4% shows earnings running ahead of cash [Certain]. P/FCF of 13.3x sits above its own 5y maximum of 10.6x, and P/E 17.7x is +20% above peers [Certain]. The cheap EV/EBITDA (5.1x) is cheap on peak-ish TTM EBITDA [Likely]. Shares rose 1.82% YoY, so no buyback support [Certain]. Altman Z 1.83 is grey-zone [Certain]. The macro overlay (primary weight) tilts moderately bear: real yields +56bp/3m and a firmer dollar pressure USD-priced oil [Likely] (research/OXY/2026-10-10-macro.md).

## Bull case
Deleveraging is real: net debt/EBITDA fell from 2.16x (FY21) to 0.76x TTM, which shifts value from creditors to equity [Certain]. EV/EBITDA of 5.1x is 27% below the peer median of 7.0x and at the 30th percentile of its own range; the mechanical base fair value is 74.38, +23.7% [Certain]. Management guides flat 2027 capex and output with continued debt reduction, i.e. disciplined capital allocation (Reuters, 2026-08-06) [Likely]. Q2 2026 brought record free cash flow and a dividend increase (transcript headline) [Likely]. Piotroski F-score of 7 signals improving fundamentals, and low CO2-EOR costs in the Permian are a genuine cost edge [Likely]. Supply shocks (Iran sanctions) could lift oil and push the stock toward the 84.13 bull value [Guessing].

## Decision
```json
{
  "ticker": "OXY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraging Permian producer looks cheap on EV/EBITDA, but that rests on an oil-driven TTM rebound while its through-cycle ROIC and FCF margin are falling and the macro backdrop tilts against oil.",
  "rationale": "Balance-sheet repair is real, but OXY is a price-taker with a falling 5y quality trend, P/FCF above its own 5y max, dilution and a moderate bear macro tilt. Upside to base fair value depends on oil holding, not on the business. Good, not compelling: conviction 3, no position.",
  "price_at_decision": 60.11,
  "price_date": "2026-10-09",
  "research_note": "research/OXY/2026-10-10.md",
  "triggers": [
    {"text": "TTM FCF margin recovers above the FY2024 level of 23.5%, showing cash generation, not just reported earnings, is improving.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 23.5}},
    {"text": "Share count starts shrinking (YoY change below 0%), showing deleveraging has turned into buybacks for equity holders.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": 0}},
    {"text": "FCF conversion (FCF/NI, cash-flow and income statements) returns above the FY2023 level of 133.0% for a full fiscal year, confirming earnings quality."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 84.13, "basis": "EV/EBITDA re-rates toward its 5y range on TTM EBITDA as deleveraging (net debt/EBITDA 0.76x [RA]) and an oil supply shock hold margins, matching the fact-sheet bull fair value 84.13; probability cut from symmetric by the overlay's moderate bear tilt (research/OXY/2026-10-10-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 60.11, "basis": "EV/EBITDA stays near 5.1x [RA] because TTM operating margin 25.8% [IS] is above the FY25 17.2% and likely to fade, offsetting debt reduction; below the 74.38 base fair value because that assumes the 6.2x median on oil-boosted TTM EBITDA, and the overlay's dollar/real-yield headwind caps a re-rating (research/OXY/2026-10-10-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 47.35, "basis": "Oil softens under a stronger dollar and higher real yields (research/OXY/2026-10-10-macro.md), FCF margin reverts toward FY25 17.7% [CF,IS] and EV/EBITDA sits near its 4.2x 5y low [RA], matching the fact-sheet bear fair value 47.35; probability raised by the overlay's moderate bear tilt."}
  },
  "entry_price": 59.5,
  "entry_basis": "valuation file: base 74.38 x 0.8 = 59.50; at that margin of safety the deleveraging story would justify conviction 4 despite commodity exposure.",
  "replaces": null,
  "replacement_reason": null
}
```

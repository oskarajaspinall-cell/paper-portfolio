# Evaluation: Games Workshop Group PLC (LON:GAW) — 2026-11-08
## Bear case
The business is superb but the price already says so [Certain]: P/E 25.8x sits above its 5y median 23.1x and P/FCF 22.5x equals its median, at large premiums to peers, so there is no margin of safety [Certain]. The last 12 months contradict the 5-year rise: ROCE fell from 82.2% to 70.9%, ROIC from 101.3% to 98.6% and FCF margin sits below its 39.0% 2-year high [Certain]. The driver looks like flagged tariff and plastic-cost headwinds (Reuters headline, 2026-07-28) on a higher capital base [Likely]; it does not break the thesis yet, but it removes the margin-expansion leg of any re-rating [Likely]. The price is down 19.5% over six months and below both moving averages, so the market is de-rating a crowded, 89.0% institution-held name [Certain]. Fair value is [data unavailable] and the regional revenue mix (US tariff exposure) is unverified [Certain].
## Bull case
Economics are among the best listed anywhere: gross margin 72.5%, operating margin 41.7%, TTM ROIC 98.6%, FCF conversion 114.4% and net cash [Certain]. Proprietary Warhammer IP, a loyal hobbyist base and vertical control of manufacture and retail form a durable moat [Likely], and licensing adds high-margin royalties [Likely]. Margins are plateauing, not collapsing: operating margin moved only -0.8pp over the year [Certain]. The share count is flat (0.16%), so cash is returned rather than diluted [Certain]. After the six-month fall the multiples are back to their own 5y medians, so a steady compounder bought at a normal price can still compound with earnings [Likely]. Macro is context only: net cash, flat GBP/USD and a steady SONIA (research/LON-GAW/2026-11-08-macro.md) [Likely].
## Decision
```json
{
  "ticker": "LON:GAW",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "An exceptional IP-led, net-cash miniatures franchise with ROIC near 100% trades at its own 5-year median multiples while trailing ROCE and FCF margin are slipping on tariff and input-cost pressure, leaving a fair rather than compelling skew.",
  "rationale": "Quality is outstanding, but multiples sit at their own 5y medians and well above peers, returns are softening over the last year, tariff exposure is unverified and no mechanical fair value exists. Expected value sits only modestly above the price: good but not compelling, so AVOID until a lower price offers a margin of safety.",
  "price_at_decision": 16080.0,
  "price_date": "2026-11-06",
  "research_note": "research/LON-GAW/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 37%, under the FY2023 five-year low of 36.9% area, showing tariffs and plastic costs are eroding pricing power structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 37}},
    {"text": "TTM ROIC falls below 80% (98.6% now), showing the capital-light moat economics are deteriorating.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 80}},
    {"text": "TTM FCF margin falls below 28% (35.7% now), showing cash conversion is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 28}},
    {"text": "Gross margin falls below 68%, under the five-year low of 68.9%, or the company reports a year-on-year decline in core revenue in its January 2027 half-year results."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 19900, "basis": "Tariff costs are absorbed, ROCE recovers toward its 82.2% 2-year high [RA-T] and P/FCF re-rates toward its 5y max 27.8x [RA] on TTM FCF [CF]; no mechanical fair value exists ([data unavailable], no GBP FX rate), so targets are own-history multiples."},
    "base": {"probability": 0.5, "target_price_12m": 16800, "basis": "Margins hold near the flat TTM operating margin of 41.7% [IS-T] and P/FCF stays at its 5y median 22.5x [RA] on modestly higher FCF."},
    "bear": {"probability": 0.25, "target_price_12m": 12500, "basis": "Tariff and plastic-cost headwinds (Reuters headline 2026-07-28 in the fact sheet) keep ROCE falling from 70.9% [RA-T] and P/FCF de-rates to its 5y min 17.5x [RA] on flat FCF."}
  },
  "entry_price": 12500,
  "entry_basis": "No base fair value is computable (fact sheet: [data unavailable]), so anchored on P/FCF back at its 5y low of 17.5x [RA] on TTM FCF, the level where this quality would carry a clear margin of safety and justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

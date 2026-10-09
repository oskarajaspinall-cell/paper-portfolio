# Evaluation: Netflix, Inc. (NFLX) — 2026-10-08
## Bear case
The price still needs more growth than the business is delivering. The reverse DCF implies 30.2% year-one revenue growth, roughly double the ~15% six-month 2026 pace [Certain]. The mechanical fair value is $39.38 base and $64.74 bull, both below the $69.70 close [Certain]. The co-CEO said Netflix is "not growing as fast as I want" [Likely], and that comment came two weeks before Q3 results on Oct 20 [Certain]. A guide-down there would confirm deceleration [Guessing]. On a 1.61 beta, real yields up 0.61pp in three months raise the cost of equity, and the macro overlay tilts moderately toward bear [Certain]. EV/EBITDA of 20.2x is still 47% above peers [Certain]. The WBD deal collapse removes an IP catalyst [Certain]. Momentum is poor: -40.5% over 12 months and below both moving averages [Certain].
## Bull case
This is a best-in-class franchise at its cheapest multiples in five years. P/E of 22.0x, EV/EBITDA of 20.2x and P/FCF of 26.0x all sit below their 5y minimums [Certain]. Quality is still improving: ROIC is 32.4%, operating margin 29.7% and FCF margin 23.1%, all near five-year highs [Certain]. Net debt/EBITDA is 0.51x and the share count fell 1.48% YoY [Certain]. All four regions grew in H1 2026 [Certain]. Disney licensing titles to Netflix shows its platform power [Likely]. If growth only steadies, P/E could return to its 5y minimum of 29.2x, around $92 [Guessing].
## Decision
```json
{
  "ticker": "NFLX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, deleveraging streaming franchise is cheap against its own history, but its price still implies about double the revenue growth it now delivers, with management flagging deceleration and real yields compressing the high-beta multiple.",
  "rationale": "Quality is excellent and the multiples sit below their 5y floors. But the reverse DCF needs 30.2% growth against roughly 15% delivered, and even the bull fair value is below the price. Management has flagged slower growth, Q3 results are due Oct 20 and the macro overlay leans bear. That makes it good but not compelling: conviction 3, so AVOID.",
  "price_at_decision": 69.70,
  "price_date": "2026-10-07",
  "research_note": "research/NFLX/2026-10-08.md",
  "triggers": [
    {"text": "TTM operating margin rises above the current 29.7% while Q3 2026 results (10-Q) show revenue growth at or above the ~15% six-month 2026 pace, showing deceleration is not structural: re-evaluate for BUY.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 29.7}},
    {"text": "TTM ROIC falls below 25%, erasing more than half the improvement since FY2021 (22.0%): the quality case is broken.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "TTM FCF margin falls below 15%, reversing the cash-conversion gains (23.1% TTM): content spend is outrunning monetization.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 92.5, "basis": "Growth steadies after the Oct 20 results and P/E re-rates to its 5y minimum of 29.2x from 22.0x on TTM EPS [RA]. That is above the mechanical bull of $64.74 because the DCF capitalizes a 5.27% risk-free rate and 1.61 beta [ST]."},
    "base": {"probability": 0.40, "target_price_12m": 64.74, "basis": "The multiple stays near its below-floor level while growth slows toward the ~15% H1 2026 pace [IS]. Value converges on the fact sheet's bull fair value of $64.74, since the reverse DCF's 30.2% implied growth is not met (Fair value section)."},
    "bear": {"probability": 0.35, "target_price_12m": 46.83, "basis": "The co-CEO's deceleration comment (fact-sheet headline, 2026-10-01) proves structural and EV/EBITDA de-rates to the fact sheet's bear value of $46.83. Bear weight is raised by the macro overlay's moderate toward-bear tilt from real-yield-driven cost-of-equity pressure on a 1.61 beta (research/NFLX/2026-10-08-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

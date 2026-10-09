# Evaluation: AT&T Inc. (T) — 2026-10-09
## Bear case
The moat is being repriced in real time. SpaceX's low-band spectrum purchase to extend Starlink Mobile puts a well-funded new entrant into a three-player market, and carriers sold off together on the news [Likely] (CNBC, Reuters headlines on fact sheet). AT&T has little room to absorb share or price pressure: ROIC of 8.9% is flat over five years and is roughly at a 5.28% risk-free rate plus a premium [Certain] [RA]. Operating margin is down 4.8pp and FCF margin down 4.2pp, and FCF/NI has fallen from 131.5% to 81.9% [Certain] [IS,CF]. Net debt/EBITDA of 3.30x leaves little slack [Certain] [RA], and Altman Z is 0.95 [Certain] [ST]. Real yields are up 0.61pp in 3 months [Certain] (macro overlay), which hurts a levered, high-payout name. Low multiples look like a value trap until Q3 results on Oct 21 show whether subscribers are leaving [Likely].

## Bull case
The price already discounts a lot. P/E is 8.2x, at the 2nd percentile of its 5-year range, and EV/EBITDA of 6.8x is below its 5-year minimum [Certain] [RA]. The FCF yield is 10.36% [Certain] [ST]. The reverse DCF implies -9.2% year-1 revenue growth, a decline no filing shows [Certain] [OV]. Gross margin has risen 4.6pp, and leverage has eased by 0.43x over five years [Certain] [IS,RA]. Shares fell 2.15% YoY on buybacks [Certain] [ST]. Satellite direct-to-device service is years from matching terrestrial capacity, so the sector sell-off may be overdone [Guessing]. Beta is 0.44 [Certain] [ST].

## Decision
```json
{
  "ticker": "T",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "AT&T's multiples are cheap at a 10.36% FCF yield, but flat ~9% ROIC, falling operating and FCF margins, 3.3x leverage and a newly funded satellite competitor make it a likely value trap rather than a mispriced quality franchise.",
  "rationale": "Cheapness is real, but quality is mediocre and the SpaceX spectrum deal is an unresolved competitive event. Q3 results on Oct 21 will show its effect. Leverage and rising real yields cap the upside. Good but not compelling, so this is an AVOID. Cash is the better holding until subscriber data is in.",
  "price_at_decision": 24.87,
  "price_date": "2026-10-08",
  "research_note": "research/T/2026-10-09.md",
  "triggers": [
    {"text": "TTM FCF margin recovers above the FY2025 level of 15.5%, showing cash conversion is no longer eroding under competitive and capex pressure.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 15.5}},
    {"text": "TTM ROIC rises above the FY2022 5-year high of 9.1%, showing returns are holding despite new entrants.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 9.1}},
    {"text": "Net debt/EBITDA falls below 3.0x, giving balance-sheet room to fund network capex and shareholder returns together.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 3.0}},
    {"text": "Q3 2026 and Q4 2026 results (SEC 8-K) show no wireless subscriber or service-revenue loss attributable to Starlink Mobile competition."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 29.43, "basis": "Q3 shows no subscriber damage and the sell-off reverses toward the 52-week high of 29.43 [HI], as EV/EBITDA re-rates from 6.8x toward its 5y median of 7.4x [RA]; this is below the DCF bull of 57.71 because the DCF assumes growth that flat ROIC does not support."},
    "base": {"probability": 0.5, "target_price_12m": 26.02, "basis": "EV/EBITDA base fair value of 26.02 [fair value table] on stable TTM EBITDA; we use it instead of the 43.36 blended base because the DCF leg (52.03) is far from a business with flat 8.9% ROIC and falling FCF margins [RA,CF]."},
    "bear": {"probability": 0.3, "target_price_12m": 19.89, "basis": "Starlink Mobile share-loss fears deepen and the stock retests its 52-week low of 19.89 [HI], below the EV/EBITDA bear of 23.20; the bear weight is raised by a small amount for the macro overlay's tilt toward bear (DFII10 +0.61pp in 3m on a 3.3x-levered balance sheet, research/T/2026-10-09-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The default anchor (base 43.36 x 0.8 = 34.69) is above the current price, and the blocker is the unresolved SpaceX competitive event plus flat returns and falling FCF margins, so a lower price would not lift conviction to 4. Re-assess on Q3 subscriber data.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Stanley Black & Decker, Inc. (SWK) — 2026-10-12
## Bear case
This is a recovery story, not a quality compounder. TTM ROIC of 6.5% is below FY2021's 11.2% [Certain] and likely below the cost of capital at a 5.22% risk-free rate [Likely]. Operating margin of 8.5% is still well short of FY2021's 12.5%, and the $2bn cost programme that drove the rebound is finished. The next leg relies on platforming and automation that are not yet proven at scale [Likely]. Leverage (net debt/EBITDA 2.58x, Altman Z 2.30 grey zone) amplifies both macro channels. Real yields are up 0.56pp in 3 months, which hits housing-linked tool demand and the discount rate [Certain]. The mechanical bear fair value is negative (-69.63), so the downside is not anchored [Certain]. Tariff and rare-earth sourcing risks are live, and short interest rose 7.5% in a month [Likely]. TTM FCF conversion of 207.8% comes from working capital and is volatile, so the 9.64% FCF yield may not last [Likely].

## Bull case
SWK is cheap on cash and EBITDA. EV/EBITDA of 10.0x is below its 5-year minimum of 11.0x and 26% under peers, and P/FCF of 10.4x is below its 5-year minimum of 16.5x [Certain]. The reverse DCF implies -0.6% year-1 growth, a low bar [Certain]. Margins are recovering off the trough: TTM gross margin is 32.2% against 24.9% in FY2023, and net debt/EBITDA has fallen from 7.38x to 2.58x [Certain]. CAM sale proceeds should cut debt further [Likely]. Piotroski F of 8 signals improving fundamentals [Certain]. If management moves toward its 2028 gross-margin target of 35-37%, EV/EBITDA re-rating toward the peer median adds material upside [Guessing]. A fall in yields would help both housing demand and the DCF [Likely].

## Decision
```json
{
  "ticker": "SWK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A brand-rich tool maker in mid margin recovery trades below its own 5-year EV/EBITDA and P/FCF minimums, but sub-cost-of-capital returns, leverage and a rate-sensitive housing end-market leave the upside too thin and the downside unanchored.",
  "rationale": "The stock is cheap on EBITDA and FCF, but ROIC of 6.5% and an operating margin of 8.5% are still far below FY2021. The easy cost savings are done, and the macro overlay tilts moderately toward bear. The blended base fair value is only +17.3% and the bear case is negative, so the asymmetry is not compelling. This is good but not conviction-4. Wait for a better price or proven margins.",
  "price_at_decision": 88.57,
  "price_date": "2026-10-09",
  "research_note": "research/SWK/2026-10-12.md",
  "triggers": [
    {"text": "TTM operating margin rises above the FY2021 level of 12.5%, showing the margin recovery is moving past the cost-programme phase toward management's 2028 targets.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 12.5}},
    {"text": "TTM gross margin rises above the FY2021 level of 33.5%, evidencing that platforming and automation are lifting gross margin toward the 35-37% target.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 33.5}},
    {"text": "TTM ROIC recovers above the FY2021 level of 11.2%, showing the business earns above its cost of capital again.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 11.2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 110.26, "basis": "Margin recovery continues and yields ease, so the price reaches the mechanical bull fair value of 110.26 [IS,RA]; the probability is cut from a neutral weight for the overlay's moderate bear tilt (research/SWK/2026-10-12-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 92.66, "basis": "The price converges on the DCF base value of 92.66 [IS,CF,RA], below the 103.85 blended base because the EV/EBITDA leg assumes a re-rating to the 13.3x 5y median that sub-cost-of-capital ROIC of 6.5% [RA] does not yet justify."},
    "bear": {"probability": 0.35, "target_price_12m": 65.76, "basis": "Higher-for-longer real yields (+0.56pp in 3m, research/SWK/2026-10-12-macro.md) keep housing-linked demand soft and margins stall after the cost programme ends, so the price retests the 6-month low of 65.76 [HI]; probability raised for the overlay's moderate bear tilt, and the target sits above the negative mechanical bear value because net debt/EBITDA of 2.58x [RA] is not distressed."}
  },
  "entry_price": 83.08,
  "entry_basis": "valuation file: base 103.85 x 0.8 = 83.08 [IS,BS,CF,RA,ST,HI]. At that level the blended base offers a 25% margin of safety on a recovering-margin business.",
  "replaces": null,
  "replacement_reason": null
}
```

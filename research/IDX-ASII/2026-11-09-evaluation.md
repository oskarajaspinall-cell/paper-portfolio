# Evaluation: PT Astra International Tbk (IDX:ASII) — 2026-11-09
## Bear case
The Direction change lines show a decline that is still going, not one that has bottomed. TTM ROIC fell from 10.1% to 8.0% and ROCE from 11.7% to 9.7% in a year, and operating margin is 11.1% against a 2-year high of 14.1% [RA-T, IS-T] [Certain]. ROIC and ROE are below their FY2021 levels of 9.5% and 12.4% [RA], so this is more than a commodity peak fading back to normal [Certain]. Leverage rose while returns fell, from 0.16x net debt/EBITDA in FY2022 to 1.23x [BS,IS] [Certain]. The cause is unidentified. Segment profits are [data unavailable], so the cut can't be split into cyclical (commodities, autos) or structural (lost share, weaker franchises) [Certain], and SOTP is blank. That leaves "temporary" as a [Guessing] call. Altman Z 2.15 and Piotroski F 5 are middling [Certain]. Macro is context only: elevated US volatility and a firmer dollar add EM risk-premium pressure (macro overlay) [Likely].
## Bull case
The pattern fits a cyclical reset more than a broken model. Operating margin of 11.1% sits near its FY2021 level of 11.5%, and gross margin of 19.2% is in its five-year range [IS] [Certain], so pricing has not collapsed. FCF holds up: FCF margin 8.1% is flat over the last year and conversion is 87.7% [CF-T] [Certain]. Shares fell 1.17% YoY [ST] [Certain]. Leverage of 1.23x is moderate, so the balance sheet is intact [Likely]. The price discounts a lot. P/E is 6.7x against a 5y median of 8.0x and a peer median of 10.6x. P/B of 0.7x is below its 5y minimum, the FCF yield is 13.21% [RA,ST], and the reverse DCF implies -12.9% revenue growth [Certain]. Mechanical base fair value is 12,232.38 [Certain]. If returns stabilise, both earnings and multiple can recover [Guessing].
## Decision
```json
{
  "ticker": "IDX:ASII",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A diversified Indonesian conglomerate trades below its own 5-year P/B floor at a 13.21% FCF yield with cash flow and balance sheet intact, but ROIC and margins are still falling, now below FY2021 levels, for a reason the missing segment data cannot show is cyclical.",
  "rationale": "Judged on the cause, not the direction: flat FCF, buybacks and moderate leverage argue the dip is cyclical, but ROIC is still falling and now below its pre-boom FY2021 level, and no segment data or guidance explains why. Cheap, plausibly a value opportunity, but 'temporary' is a guess. Good, not compelling: conviction 3, AVOID.",
  "price_at_decision": 5000.0,
  "price_date": "2026-11-06",
  "research_note": "research/IDX-ASII/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC recovers above 10.1% (its level a year earlier; 8.0% now), showing the decline was a cyclical trough that has turned.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 10.1}},
    {"text": "TTM operating margin recovers above 12.7% (a year earlier; 11.1% now), back toward the 2-year high of 14.1%.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 12.7}},
    {"text": "Net debt/EBITDA falls back below 1.0x (1.23x TTM now), showing leverage is no longer rising while returns fall.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 6400, "basis": "Returns stabilise and P/B re-rates from 0.7x toward its 5y median 0.9x [RA]; far below the mechanical DCF bull of 24,959.99 because that extrapolates cash flows from a business whose ROIC is still falling [RA-T]."},
    "base": {"probability": 0.45, "target_price_12m": 5300, "basis": "ROIC holds near 8.0% [RA-T] while the FCF margin stays near 8.1% [CF-T] and P/E edges from 6.7x toward but not to its 5y median 8.0x [RA]; well below the mechanical base of 12,232.38, which assumes recovery the falling returns and missing SOTP data do not yet support (note section 3)."},
    "bear": {"probability": 0.3, "target_price_12m": 3917.79, "basis": "ROIC and operating margin keep falling from 8.0% and 11.1% [RA-T, IS-T] as leverage rises from 1.23x [BS,IS]: the mechanical bear fair value of 3,917.79 [fact sheet Fair value], near the 52-week low of 3,920.00 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The stock is already below its own 5-year P/B minimum, and base fair value less the 20% margin of safety sits above the price. What blocks conviction 4 is that the return decline is still running and its cause (cyclical vs structural) can't be shown without segment data, so a lower price would not change the decision. Stabilising ROIC or margins would.",
  "replaces": null,
  "replacement_reason": null
}
```

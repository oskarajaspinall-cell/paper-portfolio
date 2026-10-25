# Evaluation: Moncler S.p.A. (BIT:MONC) — 2026-10-25
## Bear case
Growth has stalled: Q3 revenue was flat as Moncler's own stores softened on weaker European tourist spending and warm weather [Likely] (https://www.reuters.com/business/retail-consumer/moncler-reports-flat-q3-revenue-held-back-by-weaker-tourist-spending-europe-2026-10-21/). Returns are already eroding, ROIC from 21.0% in FY2021 to 17.5% TTM and ROE from 19.1% to 18.1% [Certain] [RA]. The business is concentrated in one category and one winter season, so a second weak winter would hit both the top line and operating leverage [Likely]. The mechanical base fair value of 46.96 EUR is only modestly above the 42.66 close, while the bear value of 33.42 is well below it [Certain] [fact sheet]. Luxury is de-rating as a sector, so cheapness against its own history may persist or deepen [Guessing] (https://www.barrons.com/articles/luxury-stocks-lvmh-hermes-kering-outlook-aadabde4). Price momentum is poor: below the 200-day average, with 6-month relative strength -29.5pp vs SPY [Certain] [HI].

## Bull case
This is a top-tier franchise: gross margin 78.2% TTM and operating margin 29.0%, steady through FY2021-25, with FCF conversion of 125.2% of net income and near-zero net debt (0.10x EBITDA) [Certain] [IS, CF, BS]. Every multiple sits below its own 5-year minimum: P/E 18.2x vs a 21.6x low, EV/EBITDA 10.3x vs 13.6x, P/FCF 14.5x vs 17.4x, a 6.89% FCF yield [Certain] [RA, ST]. It is also below peers on P/E and EV/EBITDA [Certain]. The reverse DCF implies only 4.7% year-1 growth, a bar the brand has historically cleared [Likely]. Stone Island is still growing and the new Fifth Avenue flagship shows continued DTC investment [Likely]. If the Q3 softness is weather and tourism rather than brand fatigue, a recovery toward even the bottom of its historical EV/EBITDA range is substantial upside [Guessing].

## Decision
```json
{
  "ticker": "BIT:MONC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A 78%-gross-margin, net-cash outerwear brand trades below its own 5-year minimum on every multiple, but flat Q3 revenue, falling ROIC and only modest base fair-value upside leave the cheapness unproven as an opportunity rather than a de-rating.",
  "rationale": "Quality and balance sheet are excellent and multiples are historically low, but growth has just stalled, returns are drifting lower, the sector is de-rating and base fair value sits only modestly above the price with a deep bear value. Good but not compelling: conviction 3, so AVOID with an entry price.",
  "price_at_decision": 42.66,
  "price_date": "2026-10-23",
  "research_note": "research/BIT-MONC/2026-10-25.md",
  "triggers": [
    {"text": "TTM gross margin falls below 75%, under the FY2021-25 range of 76.4%-78.1%, signalling loss of pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 75}},
    {"text": "TTM operating margin falls below 26%, under every year since FY2021 (28.3% low), showing the Q3 slowdown is deleveraging the cost base structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 26}},
    {"text": "TTM ROIC falls below 14%, extending the slide from 21.0% (FY2021) to 17.5% into clear moat erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 14}},
    {"text": "TTM FCF margin falls below 18%, under the FY2022 five-year low of 18.9%, showing inventory or working-capital stress from a weak season.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 18}}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 52.84, "basis": "Q3 softness proves weather/tourism-driven and EV/EBITDA recovers toward its 5y minimum of 13.6x [RA], matching the EV/EBITDA method's bull value of 52.84 [fact sheet]; below the 70.76 blended bull because the DCF bull's growth is not supported by flat Q3 revenue (Reuters 2026-10-21)."},
    "base": {"probability": 0.45, "target_price_12m": 46.96, "basis": "Margins hold near 29.0% operating [IS] with low growth, and the price drifts to the mechanical base fair value of 46.96 [fact sheet], below the 5y-median multiples as the sector de-rating persists (Barron's 2026-10-07)."},
    "bear": {"probability": 0.25, "target_price_12m": 33.42, "basis": "A second weak winter and continued ROIC decline from 17.5% [RA] push the stock to the mechanical bear fair value of 33.42 [fact sheet], the DCF bear being lower still at 27.46."}
  },
  "entry_price": 37.57,
  "entry_basis": "valuation file: base 46.96 x 0.8; at that level the same quality evidence, with the bear value close by, would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

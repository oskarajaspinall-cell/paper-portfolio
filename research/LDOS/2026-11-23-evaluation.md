# Evaluation: Leidos Holdings, Inc. (LDOS) — 2026-11-23
## Bear case
The market is pricing a shrinking business, and the near-term evidence gives it material: FY26 revenue guidance was cut even as EPS guidance rose, and management says contract-vehicle (VBA) uncertainty will weigh on 2027 bottom-line growth [Likely]. Part of Q3 EPS growth came from a low tax rate, which is non-recurring [company-reported] [Likely]. ROIC fell from 16.6% to 15.2% and ROCE from 19.3% to 17.1% over 12 months, both well below their 2-year highs, while leverage rose to 2.46x from 1.77x to fund Entrust [Certain]; if the acquisition does not earn its capital, the fall is not just a denominator effect [Guessing]. Federal funding runs only to 11 December 2026 under a continuing resolution, so a shutdown is possible [company-reported] [Certain]. The stock is 10.7% below its 200-day average and 35.4% down over 12 months: no trend support [Certain]. The mechanical fair value is flagged unreliable [Certain].

## Bull case
Every earnings multiple sits below its own 5-year minimum and below peers: P/E 10.9x, EV/EBITDA 8.6x, P/FCF 7.6x, with a 13.14% FCF yield [Certain]. The reverse DCF implies -12.5% year-1 revenue growth, while Q3 showed 4% revenue growth and the third consecutive guidance raise [Likely]. Operating margin is flat at 11.8% and FCF margin rose 3.0pp over the year, so the ROIC dip reflects acquisition capital entering the base, not operating erosion [Likely]. Even the bear DCF (131.30) and the EV/EBITDA bear (166.47) sit above the price [Certain]. Incumbency, clearances and recompete switching costs on mission programs protect returns [Likely]; buybacks shrink the share count 3.42% a year [Certain]. With beta 0.55 and ~84% US-government revenue [company-reported], rate moves are background (macro overlay, context weight) [Likely].

## Decision
```json
{
  "ticker": "LDOS",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and ROCE fell over 12 months while operating margin stayed flat at 11.8% and FCF margin rose 3.0pp [IS-T, CF-T]; debt rose to fund the Entrust acquisition [company-reported] (https://www.sec.gov/Archives/edgar/data/1336920/000133692026000293/ldos-20261002.htm), so the capital base grew before the profit contributes.",
    "moat": "narrow",
    "key_risk": "low",
    "key_risk_text": "A federal funding lapse after the continuing resolution (11 December 2026) or the contract-vehicle uncertainty management flags for 2027; a shutdown delays rather than removes work on multi-year contracts, and incumbency on mission programs makes a thesis-breaking recompete loss within 12 months unlikely.",
    "veto": null
  },
  "thesis": "A government-IT incumbent with ROIC well above its FY2021-23 levels and an 11.0% FCF margin trades below its own 5-year minimum on every earnings multiple and below peers, where the price implies a revenue decline that raised EPS guidance does not show.",
  "rationale": "Nothing material has changed since the HOLD at conviction 4 on 2026-11-16: cash generation holds, the ROIC dip is acquisition capital, and multiples sit below their own 5-year lows. Modest value-blend upside and no trend support keep it in the hold band, not an ADD; the position keeps its size.",
  "price_at_decision": 122.21,
  "price_date": "2026-11-20",
  "research_note": "research/LDOS/2026-11-23.md",
  "triggers": [
    {"text": "TTM operating margin falls below 10.5%, reversing most of the five-year expansion from 8.5% to 11.8%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10.5}},
    {"text": "TTM ROIC falls below 13%, showing the decline from 16.6% is no longer an acquisition denominator effect.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 13}},
    {"text": "TTM FCF margin falls below 8%, back to the level of a year earlier.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "Net debt/EBITDA on the ratios page rises above 3.0x (2.46x TTM now) without a visible deleveraging path from the Entrust debt."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 178.85, "basis": "EV/EBITDA moves back toward its 5y range (min 11.2x [RA]) as guidance raises continue; the EV/EBITDA method's base value [fact sheet fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 143.02, "basis": "Multiples stay below their 5y lows but recover part of the gap as FCF margin holds near 11.0% [CF-T]; the blended bear fair value, used instead of the unreliable 265.01 base."},
    "bear": {"probability": 0.30, "target_price_12m": 98.86, "basis": "A shutdown after the continuing resolution lapses or a lost recompete under the VBA uncertainty [note section 6, transcript] sends the stock back to its 52-week low [HI]."}
  },
  "entry_price": 120.5,
  "entry_basis": "The base fair value is flagged unreliable, so the default anchor does not apply; this is about where the value-blend upside reaches the scorecard's next band (15%), adding the one valuation point an ADD needs on the same evidence."
}
```

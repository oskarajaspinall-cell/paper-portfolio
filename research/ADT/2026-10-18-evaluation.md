# Evaluation: ADT Inc. (ADT) — 2026-10-18
## Bear case
This is a leveraged consumer subscription book, not a compounder. Altman Z of 0.65 sits in the distress zone and net debt/EBITDA is still 2.87x on $7.4 billion of long-term debt [company-reported] [Certain]. Gross attrition rose to 13.1% from 12.8%, driven by non-payment disconnects [company-reported] [Certain], and the macro overlay shows fed funds hiked and HY spreads widening, hitting both refinancing cost and household debt service at once [Likely]. Revenue grew only 2% in Q2 2026 per the transcript headline [Likely]; margin and ROIC gains partly reflect the multifamily divestiture and buybacks, not organic growth [Likely]. The 31.2% FCF margin may overstate owner cash if subscriber acquisition spend sits outside reported capex, making the 3.1x P/FCF optically cheap [Guessing]. The stock is -20.1% over 12 months and trails SPY on every horizon [Certain].

## Bull case
ADT trades below its own 5-year minimum on every multiple: 9.5x P/E, 4.7x EV/EBITDA, 3.1x P/FCF and 1.4x P/B [Certain]. The reverse DCF implies -24.2% revenue growth in year 1, against raised 2026 guidance and a Q2 beat [Likely]. Returns have risen for five years (ROIC 0.4% to 8.3%, operating margin 1.2% to 25.4%) and net debt/EBITDA fell from 5.05x to 2.84x [Certain]. Shares outstanding fell 7.45% in a year while leverage kept falling, so buybacks look FCF-funded [Likely]. Even the mechanical bear fair value of 20.36 sits far above the 6.87 close [Certain]. ADT Blu on Walmart.com gives a DIY channel against self-monitoring entrants [Likely]. Short interest is modest at 4.52% and falling [Certain].

## Decision
```json
{
  "ticker": "ADT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraging monitoring franchise trades below its own 5-year minimum on every multiple, but distress-zone balance sheet, rising non-payment attrition and a tightening rate and credit backdrop make the cheapness a risk premium rather than a clear mispricing.",
  "rationale": "Cheap on every own-history multiple with improving returns, but Altman Z in the distress zone, rising attrition, uncertain FCF quality and a bear-tilted macro overlay (hikes, wider spreads) keep this good-but-not-compelling. Conviction 3 is an AVOID; cash is acceptable. Price is not the obstacle: leverage and attrition evidence must improve first.",
  "price_at_decision": 6.87,
  "price_date": "2026-10-16",
  "research_note": "research/ADT/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROIC rises above 10%, showing returns keep compounding beyond divestiture and buyback effects (would raise conviction).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 10}},
    {"text": "TTM FCF margin falls below 20%, showing the ADT+ outright-ownership mix shift is compressing cash conversion (confirms AVOID).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA on the ratios page falls below 2.5x while buybacks continue, materially reducing the distress risk (would raise conviction)."},
    {"text": "Gross customer attrition in the 10-Q MD&A rises above 14.5% (confirms AVOID) or falls back below 12.8% (would raise conviction)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 9.4, "basis": "Deleveraging continues and P/E re-rates to its 5y median 13.0x [RA] on TTM EPS [IS]; far below the mechanical fair value because that DCF does not price distress-zone leverage (Altman Z 0.65 [ST]); probability trimmed for the overlay's moderate bear tilt (research/ADT/2026-10-18-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 8.03, "basis": "Modest growth and buybacks lift P/E only to its 5y minimum 11.1x [RA] on TTM EPS [IS], as leverage and attrition keep the discount to the base fair value of 36.72 [IS,BS,CF,RA,ST,HI]; probability trimmed for the overlay's moderate bear tilt (research/ADT/2026-10-18-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 5.2, "basis": "Rate hikes and wider HY spreads push non-payment attrition past Q2's 13.1% [company-reported] and refinancing costs up, cutting EPS while P/E stays near 9.5x [RA]; probability raised for the overlay's moderate bear tilt (research/ADT/2026-10-18-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its 5-year minimum on every multiple and far below the bear fair value. A lower price would not change the decision; deleveraging (net debt/EBITDA) and attrition evidence must improve first.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: TKO Group Holdings, Inc. (TKO) — 2026-10-12
## Bear case
The stock is not cheap on its own history: EV/EBITDA of 23.5x sits above its 5y range of 18.4x-20.3x and EV/Sales of 7.2x is 54% above peers [Certain]. The price already discounts 9.4% year-1 revenue growth [Certain], which leaves little room for error. Gross long-term debt rose ~$0.86bn in one quarter while shares fell 13.63% YoY, so the buyback looks partly debt-funded [Likely]. TTM ROIC is only 7.8%, well below the FY2022 level of 16.4% [Certain]. That is barely above a cost of equity built on a 5.22% risk-free rate. Endeavor controls ~51% of the vote and has related-party agreements [Certain]. Short interest is 13.95% and rising [Certain], and Altman Z is 1.65 [Certain]. Rising real yields and HY spreads press on a 67% DCF-weighted valuation (macro overlay, small bear tilt) [Likely].

## Bull case
UFC and WWE are scarce global IP with media-rights pricing power [Likely]. The post-merger recovery is real: ROIC went from 3.9% to 7.8%, operating margin from 9.6% to 21.4% and FCF margin from 9.6% to 31.5% between FY2024 and TTM [Certain]. Net debt/EBITDA fell from 4.35x to 2.69x [Certain]. Q2 2026 beat and full-year guidance was raised (headline, [OV]) [Likely]. The stock trades at a 4.96% FCF yield and P/FCF of 20.1x, 30% below peers [Certain]. A 13.63% share-count reduction compounds per-share value [Certain]. Mechanical base fair value is $209.58, +17.7% [Certain]. The stock is near its 52-week low of 171.19 [Certain], and Q3 results on Nov 4 could re-rate it [Guessing].

## Decision
```json
{
  "ticker": "TKO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "TKO owns scarce, improving UFC/WWE media-rights franchises, but at 23.5x EV/EBITDA (above its own 5y range) with debt-funded buybacks, 7.8% ROIC and a controlling shareholder, the price already discounts the recovery.",
  "rationale": "The business is recovering, but the valuation offers no margin of safety. EV/EBITDA is above its own 5y range, the price implies 9.4% growth and the expected 12-month return across the three scenarios is only low single digits. Leverage rose in Q2, governance is controlled and the macro overlay tilts toward bear. That is good but not compelling, so we hold cash rather than take a position.",
  "price_at_decision": 178.01,
  "price_date": "2026-10-09",
  "research_note": "research/TKO/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC rises above 10%, showing post-merger returns clearly clear the cost of capital (TTM 7.8% [RA]).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 10}},
    {"text": "TTM operating margin rises above 25% (TTM 21.4% [IS]), showing media-rights repricing is lifting profitability faster than the price implies.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 25}},
    {"text": "TTM FCF margin falls below 20% (TTM 31.5% [CF,IS]), which would mean cash generation is fading and turn the view outright negative.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "The next 10-Q shows gross long-term debt falling back from $4.583bn, confirming buybacks are funded by free cash flow rather than borrowing (note, sec.gov 10-Q)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 225, "basis": "Guidance is delivered and FCF margin holds above 30% [CF,IS], so the stock re-rates toward the mechanical base fair value of 209.58 and beyond toward the DCF base of 283.62 [Fair value]; the target is capped well below the DCF because EV/EBITDA is already above its 5y max of 20.3x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 185, "basis": "The price implies 9.4% revenue growth [Fair value], and with EV/EBITDA held near today's 23.5x [RA] that is roughly what guidance delivers, so the return is a FCF yield of 4.96% [ST]; this is below base fair value 209.58 because the 33%-weighted EV/EBITDA method (61.49 [Fair value]) argues against the DCF."},
    "bear": {"probability": 0.30, "target_price_12m": 135, "basis": "EV/EBITDA de-rates to its 5y min-to-median range of 18.4x-20.1x [RA] on 2.69x net leverage [RA]; probability is raised by the macro overlay's small bear tilt (rising real yields and HY spreads, research/TKO/2026-10-12-macro.md); this is far above the mechanical bear of 55.85 because that figure lies below even the 5y-min multiple and is not credible for contracted media-rights revenue."}
  },
  "entry_price": 167.66,
  "entry_basis": "valuation file: base 209.58 x 0.8; at that price the 20% margin of safety would offset the leverage and governance risks and justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

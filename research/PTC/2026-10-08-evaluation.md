# Evaluation: PTC Inc. (PTC) — 2026-10-08
## Bear case
PTC is no longer a standalone quality call. It is a pending Schneider Electric cash takeover (8-K Item 1.01, 2026-10-05) [Certain]. The shares jumped 33.5% on 19.8x volume and have held 103% of the move, so the market already prices in completion [Certain]. From 193.60 the upside is capped at the deal terms, while a deal break exposes the stock to standalone value. The fact sheet's own-history fair value is 75.82 / 133.15 / 157.73, and even the bull case sits 18.5% below the last close [Certain]. The reverse DCF implies 23.9% year-1 revenue growth, which standalone fundamentals do not support [Likely]. Regulatory review, shareholder-fairness suits and Schneider's own share-price reaction add timing and completion risk [Likely]. The payoff is asymmetric the wrong way: a small capped gain against a roughly 31% loss to base fair value if the deal fails [Likely].
## Bull case
The business is excellent and still improving. TTM ROIC is 19.7%, gross margin 84.5%, operating margin 39.8% (+14.8pp over 5y) and FCF margin 31.7% [Certain]. Net debt/EBITDA fell to 0.98x from 2.74x, and shares outstanding fell 1.95% YoY [Certain]. A strategic buyer paying a premium confirms the franchise value of embedded CAD/PLM software [Likely]. Most announced US cash deals close, so the shares should converge to the offer with low volatility [Likely]. A competing bid could lift the price towards the 206.82 52-week high [Guessing]. If the deal broke, multiples of 18.8x P/E and 17.4x EV/EBITDA would sit below their 5y minimums, which gives standalone support above the DCF floor [Guessing].
## Decision
```json
{
  "ticker": "PTC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A high-quality industrial software franchise whose price is now pinned to a pending Schneider Electric cash takeover, leaving capped deal-spread upside against a large standalone downside if the deal breaks.",
  "rationale": "The core case for 12-month value creation is gone: the return is a merger-arb spread, capped near the offer, with deal-break downside towards the 133.15 base fair value. The probability-weighted target sits below the 193.60 close. Quality is high, but this is not a core value idea. Conviction 2 means no position.",
  "price_at_decision": 193.60,
  "price_date": "2026-10-07",
  "research_note": "research/PTC/2026-10-08.md",
  "triggers": [
    {"text": "The Schneider Electric merger agreement is terminated (SEC 8-K) while standalone fundamentals hold, which would reopen a standalone core case at a lower price."},
    {"text": "TTM gross margin falls below 75%, signalling pricing or competitive erosion in the CAD/PLM franchise.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 75}},
    {"text": "TTM FCF margin falls below 25%, reversing the cash-conversion improvement from 19.0% in FY2021.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "Net debt/EBITDA rises back above 2.0x, reversing the deleveraging from 2.74x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.10, "target_price_12m": 206.82, "basis": "A competing or raised bid lifts the shares to the 52-week high of 206.82 [HI]; this is a speculative outcome with no evidence in the note."},
    "base": {"probability": 0.75, "target_price_12m": 196.05, "basis": "The Schneider deal (8-K Item 1.01, research/PTC/2026-10-08.md) closes and the shares converge to the deal-pegged level around the 196.05 reaction-day high [HI]; above the 133.15 fair-value base because the price is set by the offer, not standalone cash flow."},
    "bear": {"probability": 0.15, "target_price_12m": 133.15, "basis": "The deal breaks on regulatory or shareholder grounds and the shares revert to the fact sheet's standalone base fair value of 133.15 [IS,BS,CF,RA,ST,HI], near the pre-announcement trading range (swing low 133.67 on 2026-09-28 [HI])."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

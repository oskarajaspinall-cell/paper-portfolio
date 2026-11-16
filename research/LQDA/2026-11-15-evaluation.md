# Evaluation: Liquidia Corporation (LQDA) — 2026-11-15
## Bear case
LQDA is a single-product company: YUTREPIA is the whole business, and the settlement confined it to PAH, giving up PH-ILD [Certain]. The settlement does not bar future UTC patent litigation over L606 or new indications, so the pipeline carries live legal risk [Certain]. Payments of $185.0 million [company-reported] plus $145.4 million [company-reported] through April 2027 absorb much of the cash [Likely]. Profitability is one quarter-scale old: TTM ROIC of 306.2% is an artefact of a tiny capital base, net margin is still -15.1%, and no fair value is computable, so the price has no mechanical anchor [Certain]. The stock is extended on 12 months (+102.8%) yet -20.4% over 3 months; if launch growth slows, a de-rating from 8.0x sales is likely [Likely]. Short interest of 26.61%, an ATR of 6.3% of price and a related-party settlement payment to a director-linked holder add volatility and governance risk [Certain].

## Bull case
The litigation overhang is gone: a global settlement secures YUTREPIA's PAH commercialisation, removing the binary risk that dominated the stock [Certain]. The launch is working: Q3 YUTREPIA sales rose 31% quarter on quarter to $222.7 million, adjusted EBITDA reached $140.5 million (per the stockanalysis.com transcript summary) [Likely]. TTM operating margin is 47.1% vs -155.0% a year earlier and FCF margin 46.8%, with gross margin 92.7% [Certain]. The balance sheet is net cash (net debt/EBITDA -0.77x), Altman Z 4.48 [Certain]. EV/Sales of 8.0x sits below its own 5y minimum and only modestly above the peer median of 7.2x, while the FCF yield is 5.63% and the price is above its 200-day average [Certain]. L606 and other indications offer optionality not in the current numbers [Guessing].

## Decision
```json
{
  "ticker": "LQDA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROIC, operating margin and FCF margin all rose sharply over the last year [RA-T, IS-T, CF-T] as YUTREPIA sales ramped.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Single-product concentration in PAH against a larger incumbent, with L606/new-indication patent litigation not barred by the settlement and an extended 12-month price exposed to de-rating if launch growth slows.",
    "veto": null
  },
  "thesis": "YUTREPIA's PAH launch has turned Liquidia profitable and cash-generative now that the UTC litigation is settled, but a single product with no computable fair value is not yet a high-conviction compounder.",
  "rationale": "Launch economics are strong and the balance sheet is net cash, but one product, a narrowed label, residual patent risk on L606, large settlement payments, governance flags and no mechanical fair value leave the case good but not compelling. Cash is acceptable.",
  "price_at_decision": 57.41,
  "price_date": "2026-11-13",
  "research_note": "research/LQDA/2026-11-15.md",
  "triggers": [
    {"text": "Gross margin (statistics, TTM) falls below 80%", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 80}},
    {"text": "Operating margin (statistics, TTM) falls below 20%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "FCF margin (statistics, TTM) turns negative", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "UTC files new patent litigation over L606 or a new YUTREPIA indication (10-Q / company release)"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 85.0, "basis": "YUTREPIA growth continues (Q3 sales up 31% QoQ per the transcript summary [OV]) and EV/Sales re-rates toward its 5y minimum of 16.0x [RA] as profits prove durable."},
    "base": {"probability": 0.5, "target_price_12m": 60.0, "basis": "Sales growth offsets a multiple held near the current 8.0x EV/Sales [RA], with settlement payments [company-reported, 10-Q] absorbing cash; no mechanical fair value is computable, so this is judgement on the EV/Sales anchor."},
    "bear": {"probability": 0.25, "target_price_12m": 38.0, "basis": "Launch growth slows in a PAH-only label and EV/Sales de-rates below the peer median of 7.2x [P:UTHR,P:HALO,P:SUPN,P:KRYS], as in the 3-month fall of -20.4% [HI]."}
  },
  "entry_price": 46.0,
  "entry_basis": "No base fair value is computable [fact sheet]; anchored instead on EV/Sales falling to the peer median of 7.2x with a margin of safety, near the 2026-11-03 swing low of 41.52 [HI]; at that level the same evidence would be cheap enough on a value basis.",
  "new_evidence": null,
  "replaces": null,
  "replacement_reason": null
}
```

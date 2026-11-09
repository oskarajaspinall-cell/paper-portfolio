# Evaluation: Industrial Securities Co.,Ltd. (SHA:601377) — 2026-11-09
## Bear case
Returns are too low for a good business. ROE is 5.9% TTM against 13.6% in FY2021, and ROIC is 1.5%, below any plausible cost of equity [Certain] (RA). The broking business is commoditised and has no durable pricing power [Likely]. P/E of 15.7x is well above the peer median of 9.4x, so it is not cheap against stronger peers [Certain] (RA). The mechanical base fair value of 3.37 CNY sits below the 5.50 close, though it is flagged unreliable [Certain]. The operating-margin Direction change is cyclical: margin is up over the last 12 months (37.4% to 39.4%) on market activity, yet it is 2.2pp below its 41.6% high of 2026-06-30 [Likely]. The FCF-margin Direction change, 193.1pp below its 2-year high, reflects client and trading balances. It tells us nothing about the business [Likely]. Piotroski F is 4, the shares are 20.6% down over 12 months and dilution is 2.04% [Certain].
## Bull case
P/B of 0.7x is below its own 5y minimum of 0.8x and below peers [Certain] (RA). P/E sits at a 15% position in its own 5y range [Certain]. ROE has recovered from its 4.5% FY2023 low to 5.9%, and operating margin has rebounded to 39.4% TTM [Certain] (IS-T). A sustained pick-up in A-share turnover or supportive capital-market policy would lift earnings with high operating leverage [Guessing]. The P/E fair-value method gives 8.14 CNY [Certain]. Beta is 0.69, and the yuan is stable at 6.6538 per USD (macro overlay, context only) [Certain]. Even so, the upside rests on the market cycle, not on a franchise advantage [Likely].
## Decision
```json
{
  "ticker": "SHA:601377",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "The falling metric is FCF margin over 3 years (-29.1pp, CF-T): for a broker it swings with client funds and trading assets (FY2023 -106.2%, 2026-03-31 TTM 304.1%), a balance-sheet timing effect, not lost share; operating margin is up to 39.4% TTM from 37.4% [IS-T]", "moat": "none", "key_risk": "high", "key_risk_text": "Earnings depend on A-share turnover and Chinese capital-market policy; a renewed activity slump keeps ROE well below the cost of equity", "veto": null},
  "thesis": "A commoditised Chinese broker earning low single-digit ROIC, cheap on book only because returns are poor and dearer than peers on earnings.",
  "rationale": "The business fails the quality bar: ROIC is 1.5% and ROE 5.9%, there is no moat, and earnings depend on the market cycle. On P/E it is dearer than peers, and the mechanical fair value sits below the price. The low P/B reflects low returns. Conviction is below the buy bar, so no position.",
  "price_at_decision": 5.50,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-601377/2026-11-09.md",
  "triggers": [
    {"text": "ROE (statistics page) rises above 10%, showing returns recovering toward the cost of equity", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 10}},
    {"text": "ROE falls below 4.5%, the FY2023 low, confirming the decline", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 4.5}},
    {"text": "Operating margin (TTM) falls below 30%, signalling a renewed activity slump", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 6.38, "basis": "A-share activity improves and the operating margin holds near its 41.6% 2-year high [IS-T], taking the shares back to the 6-month high of 6.38 [HI], still well below the P/E-method fair value of 8.14."},
    "base": {"probability": 0.5, "target_price_12m": 5.50, "basis": "ROE stays around 5.9% [RA] with P/B near 0.7x, so the price holds near the 5.50 close; this is above the unreliable FCFE base fair value of 3.37 because broker FCF is distorted by client balances."},
    "bear": {"probability": 0.25, "target_price_12m": 4.84, "basis": "Activity slumps and ROE slides back toward the 4.5% FY2023 low [RA], so the shares fall to the P/E-method bear fair value of 4.84."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: returns sit far below the cost of equity and there is no moat, so a lower price would not change the decision; only a sustained ROE recovery (trigger 1) would.",
  "replaces": null,
  "replacement_reason": null
}
```

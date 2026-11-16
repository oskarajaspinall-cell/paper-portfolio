# Evaluation: Zabka Group S.A. (WSE:ZAB) — 2026-11-16
## Bear case
This is no longer an investment in the business. It is a merger-arbitrage position. Couche-Tard opened a voluntary cash tender offer for all shares on 2026-08-26 (https://www.reuters.com/business/couche-tard-launches-tender-offer-all-zabka-shares-2026-08-26/) [Certain]. The price is pinned: ATR is 0.3% of the close and the price sits just above its 50-day average [Certain]. If the deal completes, the holder gets roughly today's price, with little upside [Likely]. If it fails, the stock falls back toward the model bear value of 25.90 PLN [Guessing]. The terms, conditions and approvals are unverified because the article fetch was blocked [Certain]. The price is 17.5% above its 200-day average only because of the bid. That is not organic trend strength, and if the bid lapses the de-rating risk is abrupt [Likely]. Fair value is flagged unreliable, since its methods disagree 4.1x [Certain]. P/FCF is above its 5y max [Certain].
## Bull case
The business is working. ROIC is 20.1% TTM, up from 13.6% a year earlier. FCF margin is 9.6%, up from 7.6%, and operating margin is at its 2-year high of 7.7% [Certain]. Net debt/EBITDA has fallen from 4.84x to 2.51x, and Piotroski F is 8 [Certain]. Q3 results show continued network expansion and market-share gains (https://stockanalysis.com/quote/wse/ZAB/transcripts/558122-q3-2026/) [Likely]. The FCF yield is 9.14%, EV/EBITDA of 9.6x is below its 5y minimum, and the reverse DCF implies -1.9% revenue growth [Certain]. That growth is undemanding for a chain that is still expanding [Likely]. A strategic buyer bidding for the company confirms the franchise value [Likely]. A competing or improved bid is possible but unevidenced [Guessing].
## Decision
```json
{
  "ticker": "WSE:ZAB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROIC, operating margin and FCF margin are all rising or flat over the last 1 and 3 years [RA-T, IS-T, CF-T].",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "The Couche-Tard cash tender offer pins the price: completion caps the 12-month return near today's level, and failure risks an abrupt de-rating toward the model bear value.",
    "veto": {"code": "binary_event", "reason": "A pending cash tender offer for all shares (Reuters, 2026-08-26) makes the outcome binary on deal completion. Its terms and conditions are unverified, and the trend strength reflects the bid, not the business."}
  },
  "thesis": "A high-return, deleveraging Polish convenience franchise whose share price is now pinned by a pending Couche-Tard cash tender offer, so the 12-month return depends on the deal outcome rather than the business.",
  "rationale": "The fundamentals are strong, but the pending cash tender offer caps upside near today's price and leaves a binary downside if it fails. That is a deal-arbitrage payoff, not a core thesis on a working business. The binary_event veto holds conviction at 3, so this is an AVOID.",
  "price_at_decision": 31.82,
  "price_date": "2026-11-13",
  "research_note": "research/WSE-ZAB/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15% (20.1% now), reversing the returns step-up.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 6.5% (7.7% now), under the five-year low of 7.1%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 6.5}},
    {"text": "TTM FCF margin falls below 7% (9.6% now), showing the cash conversion was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 7}},
    {"text": "The Couche-Tard tender offer lapses or is withdrawn, per a company or regulatory release (re-research the stand-alone business then)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.15, "target_price_12m": 33.88, "basis": "An improved or competing bid lifts the price back to its 52-week high of 33.88 [HI]; no evidence of one exists yet (bull case)."},
    "base": {"probability": 0.65, "target_price_12m": 31.82, "basis": "The Couche-Tard cash tender completes near the level at which the price is pinned (ATR 0.3% of close [HI]; Reuters 2026-08-26 tender headline [OV])."},
    "bear": {"probability": 0.2, "target_price_12m": 25.9, "basis": "The offer fails and the stock reverts to the mechanical bear fair value of 25.90 [fact sheet Fair value], which is below the unreliable base of 45.30 because the bid premium unwinds."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The pending cash tender offer pins the price and makes the outcome binary, so a lower price would not change the decision until the deal resolves. Re-research then.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: ADT Inc. (ADT) — 2026-11-07
## Bear case
The screen's drift signal is a false positive. The 2026-10-29 jump of +33.2% on 22.3x volume was a definitive all-cash takeover by Thrive Holdings at $10 per share, not an earnings beat [Certain]. A cash bid pins the price, so there is no drift left to capture: the last close of 9.86 sits just under the offer [Certain]. The mechanical 2:1 target of 10.96 is above the offer, so the evidence cannot support it [Likely]. The realistic upside is the small spread to the offer, against a stop near 9.31. Reward:risk is therefore far below 2:1 [Likely]. A deal break would gap the stock through any stop, back toward the pre-bid range (6-month low 6.03) [Likely]. The Altman Z of 0.58 and net debt/EBITDA of 2.85x add financing risk to completion [Likely]. Closing is expected in Q1 2027, after the 8-week time limit [Likely].
## Bull case
The deal looks likely to close. The offer is all-cash and definitive, Q3 results were solid with strong cash generation, and the spread is narrow, which signals that the market expects completion [Likely]. A rival bid is possible because the standalone business looks cheap: P/FCF of 4.5x is below its 5y minimum and the base fair value is 35.39 [Guessing]. Still, that is merger arbitrage on a capped payoff. It is neither a drift setup nor a pullback setup, and neither owner setup applies [Certain].
## Decision
```json
{
  "ticker": "ADT",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 1,
  "thesis": "The drift signal comes from a $10 all-cash takeover, not an earnings beat, so the price is pinned near the offer and no tactical edge or 2:1 reward:risk exists.",
  "rationale": "The setup is invalid: the jump is a cash bid, not a results beat. The honest target is the offer, so reward:risk is far below 2:1 against the volatility stop, and a deal break would gap through the stop. Closing is also beyond the drift time limit. No position.",
  "price_at_decision": 9.86,
  "price_date": "2026-11-06",
  "research_note": "research/ADT/2026-11-07.md",
  "exit_plan": {"target": 10.0, "stop": 9.31, "time_limit": "2027-01-02"},
  "scenarios": {
    "bull": {"probability": 0.1, "target_price_12m": 10.0, "basis": "A rival bid is possible given the low standalone multiples (P/FCF 4.5x below its 5y minimum [RA]), but none is evidenced, so the agreed $10 cash offer is the only supported level [OV]."},
    "base": {"probability": 0.8, "target_price_12m": 10.0, "basis": "The Thrive Holdings all-cash deal closes in Q1 2027 at $10 per share as announced (https://techcrunch.com/2026/10/29/openai-backed-thrive-holdings-acquires-adt/); the base fair value of 35.39 is irrelevant because the offer caps the price."},
    "bear": {"probability": 0.1, "target_price_12m": 6.03, "basis": "The deal breaks on approvals or financing (Altman Z 0.58 [ST], net debt/EBITDA 2.85x [RA]) and the stock returns to its pre-bid 6-month low of 6.03 [HI], still below the mechanical bear fair value of 20.11."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: a pending cash takeover pins the stock, so no lower price recreates a drift or pullback setup; re-research only if the deal breaks.",
  "replaces": null,
  "replacement_reason": null
}
```

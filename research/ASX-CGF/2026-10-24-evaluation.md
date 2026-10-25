# Evaluation: Challenger Limited (ASX:CGF) — 2026-10-24
## Bear case
The 2026-10-19 jump of +19.3% on 4.2x volume was an approach, not a results beat: the same-day headline says Challenger will consider an A$11.80/share offer from a Daiichi Life unit [Likely]. That makes this event risk, not post-earnings drift. A bid sets a ceiling, and the 11.92 close already sits above the offer level, so the upside depends on a higher or competing bid that no evidence supports [Likely]. If talks fail, the price can fall back toward the pre-jump swing lows (9.43 on 2026-10-15) and gap straight through a 10.96 stop [Likely]. RSI(14) is 76.4 and P/B of 2.0x is above its 5y maximum of 1.7x [Certain]. Mechanical base fair value is 4.16 AUD, far below the price [Certain]. Shares outstanding rose 16.61% YoY [Certain].
## Bull case
The price is at a 52-week high of 11.94 with no overhead resistance, 17.9% above its 50-day average, and relative strength versus SPY is +35.8pp over 6 months [Certain]. The same release showed higher Q1 sales and AUM [Likely], ROE rose to 11.8% from 4.3% in FY2025 [Certain], and P/E of 17.2x sits low in its 5y range and below the peer median of 21.1x [Certain]. A strategic buyer could raise its offer or a rival could bid, and the market is already pricing some chance of that [Guessing]. None of this makes a 2:1 drift trade work: the 13.84 target the rule requires has no support beyond speculation on a higher bid [Likely].
## Decision
```json
{
  "ticker": "ASX:CGF",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "The 2026-10-19 jump is a takeover approach at A$11.80 rather than an earnings beat, so there is no drift edge and the price already sits at the bid ceiling.",
  "rationale": "A bid-driven move is binary deal risk, not drift. The close is above the offer level, so the 2:1 target of 13.84 needs a higher or rival bid that no evidence supports, and a failed approach could gap through the 10.96 stop. The reward:risk does not hold, so this is an AVOID.",
  "price_at_decision": 11.92,
  "price_date": "2026-10-23",
  "research_note": "research/ASX-CGF/2026-10-24.md",
  "exit_plan": {"target": 13.84, "stop": 10.96, "time_limit": "2026-12-18"},
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 13.84, "basis": "A raised or competing bid above the A$11.80 approach in the 2026-10-19 headline [OV]; well above the mechanical bull fair value of 9.12 because a control premium is not in the own-history model."},
    "base": {"probability": 0.5, "target_price_12m": 11.8, "basis": "The Daiichi Life unit's A$11.80 approach (2026-10-19 headline [OV], macro overlay) proceeds at the offer; far above base fair value 4.16 because the bid, not the P/B+ROE model, anchors the price."},
    "bear": {"probability": 0.3, "target_price_12m": 9.43, "basis": "Talks fail and the price returns to the pre-approach swing low of 9.43 [HI], below the 50-day average of 10.11 [ST] yet still above the bull fair value of 9.12 given ROE of 11.8% [RA]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

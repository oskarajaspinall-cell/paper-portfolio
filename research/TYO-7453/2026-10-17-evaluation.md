# Evaluation: Ryohin Keikaku Co., Ltd. (TYO:7453) — 2026-10-17
## Bear case
The drift edge rests on a beat we cannot see: the fact sheet shows the Q4 FY2026 filing and the price/volume reaction, not what was reported against expectations [Certain]. The stock had already given back part of the jump one session later, closing at 4,709.00 against a 4,855 high, with 77% held [Certain]. Valuation is a crowding and gap risk, not a footnote: EV/EBITDA 17.2x, EV/Sales 2.6x and P/B 6.0x are all above their 5-year maximums, P/E 32.7x sits at the 97% point of its range, and the reverse DCF implies 20.9% year-1 revenue growth [Certain]. RSI of 70.1 says the move is extended [Certain]. Even the mechanical bull fair value (4,133.84) is below the price [Certain]. A re-rating this stretched can mean-revert sharply on any soft monthly sales print [Likely].

## Bull case
The business is genuinely improving: ROIC rose to 24.1% from 11.6% over five years, operating margin to 11.2% from 6.6%, and FCF conversion is about 101.6% with net cash and a Piotroski F-score of 8 [Certain]. The reaction was large and well-volumed (+9.5% on 4.1x volume) and set a fresh 52-week high, so there is no overhead supply [Certain]. The uptrend is clean: the 50-day sits 14.9% above the 200-day and relative strength versus SPY is positive over 3, 6 and 12 months [Certain]. The volatility stop (4,516.58) leaves a 2:1 target reachable in open air above the high [Likely]. Mechanical fair value, built on history, likely understates a business whose returns have structurally stepped up [Guessing].

## Decision
```json
{
  "ticker": "TYO:7453",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A strongly improving retailer had a large, well-volumed post-results jump, but the beat itself is unverified and the stock already trades above its own 5-year multiple ceilings, so the drift edge is not clear enough to trade.",
  "rationale": "Setup qualifies mechanically and the 2:1 plan is arithmetically valid, but the edge is unproven: no visible beat magnitude, partial fade after one session, RSI extended, and multiples above 5-year maximums create gap-down risk on any disappointment. Good but not compelling; cash is acceptable.",
  "price_at_decision": 4709.00,
  "price_date": "2026-10-16",
  "research_note": "research/TYO-7453/2026-10-17.md",
  "exit_plan": {"target": 5093.85, "stop": 4516.58, "time_limit": "2026-12-12"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 5093.85, "basis": "The re-rating holds as ROIC (24.1% [RA]) and operating margin (11.2% [IS]) keep rising, so the stock extends above its 4,855 52-week high [HI] in line with the reverse-DCF's 20.9% implied growth being met [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 4133.84, "basis": "Multiples partly revert from above their 5-year maximums (EV/EBITDA 17.2x vs 15.7x max [RA]) toward the mechanical bull fair value 4,133.84, which we use as base because improved returns (ROIC 24.1% [RA]) justify more than the own-history base."},
    "bear": {"probability": 0.30, "target_price_12m": 2554.71, "basis": "A sales disappointment pushes multiples back toward 5-year medians (P/E 22.5x, EV/EBITDA 8.3x [RA]), consistent with the mechanical base fair value 2,554.71 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle for this drift trade: a lower price would mean the post-results reaction has failed, which removes the setup rather than improving it; the obstacle is the unverified beat and the stretched multiples.",
  "replaces": null,
  "replacement_reason": null
}
```

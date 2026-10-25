# Evaluation: Samsung E&A Co., Ltd. (KRX:028050) — 2026-10-24
## Bear case
The edge here can't be checked. Q3 results came out 2026-10-22, but the fact sheet has no quarterly revenue, EPS or guidance, so we can't tell a real beat from a one-off [Certain]. The move is already stretched: close 59,800 is +23.7% above the 50-day MA and RSI is 71.6 [Certain]. P/E 17.3x, EV/EBITDA 6.5x and P/B 2.4x all sit above their 5y maximums [Certain]. That means crowding and the risk of the gap partly closing [Likely]. Using the rule-based drift stop (55408), the minimum 2:1 target of 68584 is above the 52-week high of 67,300, so the plan relies on breaking resistance with nothing to back it [Likely]. The screen and the fact sheet also disagree on the reaction day and its low, which makes the stop uncertain [Certain]. Cash quality is weak: FY2025 FCF margin 2.2%, FCF yield -2.03%, Piotroski F 3 [Certain].
## Bull case
The reaction was large and confirmed: +7.9% on 7.2x volume, with 100% of the jump held [Certain]. It follows a 3-month rise of +28.2% and relative strength of +25.2pp vs SPY [Certain]. Profitability is improving. TTM operating margin is 11.2% against 8.8% in FY2025, and gross margin is 16.6%, the best in five years [Certain]. TTM ROIC is 105.6% and the balance sheet holds net cash (-3.13x net debt/EBITDA) [Certain]. On P/E it trades below the peer median of 20.3x [Certain]. If the margin step-up holds, the drift could carry the price back toward the 67,300 high [Guessing].
## Decision
```json
{
  "ticker": "KRX:028050",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A post-earnings gap in a Korean E&C contractor whose results quality is unverified and whose 2:1 target sits above the 52-week high after an extended, overbought run.",
  "rationale": "The setup's edge is unclear because the beat can't be verified from the evidence. The price is overbought and above every 5y multiple maximum. The rule-based 2:1 target needs a break above the 67,300 high, so reward:risk is not supported. Conviction is 2, so no position.",
  "price_at_decision": 59800,
  "price_date": "2026-10-23",
  "research_note": "research/KRX-028050/2026-10-24.md",
  "exit_plan": {"target": 68584, "stop": 55408, "time_limit": "2026-12-18"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 67300, "basis": "The margin gain persists (TTM operating margin 11.2% vs 8.8% FY2025 [IS]) and the price retests its 52-week high of 67,300 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 55200, "basis": "The post-results gap partly closes toward the September swing high of 55,200 [HI], as multiples above their 5y maximums (P/E 17.3x vs 12.1x max [RA]) stall further gains; no mechanical fair value exists to anchor it [data unavailable]."},
    "bear": {"probability": 0.30, "target_price_12m": 41650, "basis": "Weak cash conversion (FY2025 FCF margin 2.2% [CF,IS]) and a reversion of P/E toward its 5y max of 12.1x [RA] send the price back to the October swing low of 41,650 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

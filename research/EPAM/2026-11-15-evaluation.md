# Evaluation: EPAM Systems, Inc. (EPAM) — 2026-11-15
## Bear case
The reaction looks large next to the surprise: a modest EPS and revenue beat with Q4 guidance only in line, and revenue still growing in low single digits [Likely]. The stock had already run +60.7% over 3 months before and through the jump, sits +29.1% above its 50-day average with RSI 70.0, so much of the drift may be spent [Likely]. A 13.12% short interest may have fuelled the jump through covering, which does not repeat [Guessing]. The call flagged North American weakness and a lower Poland tax benefit [Likely]. Fundamentally, ROIC is 11.3pp below its 2-year high and FCF margin 4.0pp below its 2-year high; this looks largely structural (IT-services pricing and AI deflation) rather than a one-off, though ROCE rose over the last year [Guessing]. The plan's reward:risk of 2.04 only just clears 2:1, with the target set at the minimum, not by evidence [Certain].
## Bull case
The beat was real and the reaction strong: +20.6% on 3.4x volume, with 91% of the jump held six sessions later [Certain]. Operating margin expanded and management cited AI-native momentum and large deals supporting 2027 growth [Likely]. The balance sheet is clean: net cash, Altman Z 6.82, Piotroski F 7, shares down 6.08% YoY, and an activist pushing for a larger buyback [Certain]. P/E of 20.5x is below its 5-year minimum of 29.2x, so a re-rating has room [Certain]. Relative strength vs SPY is +63.7pp over 3 months and the 52-week high of 222.53 leaves headroom above the 186.00 target [Certain]. ROCE is rising over the last 12 months (14.4% to 16.8%) and operating margin is flat-to-up, so the 5-year decline may be bottoming [Likely].
## Decision
```json
{
  "ticker": "EPAM",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A post-earnings drift on a real but modest beat with margin expansion, where the stock is already extended and the plan only just reaches 2:1, so the trade's edge is not clear enough.",
  "rationale": "The setup qualifies mechanically, but the jump is large relative to a modest beat and in-line guidance, the stock is extended (RSI 70, far above its 50-day), short covering may have done the work, and the 186.00 target was set at the 2:1 minimum rather than by evidence. Good but not compelling: AVOID.",
  "price_at_decision": 163.15,
  "price_date": "2026-11-13",
  "research_note": "research/EPAM/2026-11-15.md",
  "exit_plan": {"target": 186.00, "stop": 151.94, "time_limit": "2027-01-10"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 222.53, "basis": "Margin expansion and AI-native momentum sustain the re-rating back to the 52-week high [HI], below the mechanical bull fair value of 235.16 (flagged unreliable)."},
    "base": {"probability": 0.45, "target_price_12m": 167.39, "basis": "Low single-digit growth with flat operating margin (11.4% TTM [IS-T]) holds the price near the mechanical base fair value of 167.39, weighed lightly as methods disagree 3.9x."},
    "bear": {"probability": 0.30, "target_price_12m": 124.01, "basis": "North American weakness and a lower tax benefit [transcript, note] stall growth and the jump retraces toward the mechanical bear fair value of 124.01, near the 50-day average of 126.34 [ST,HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: a lower price inside the drift window would mean the earnings jump is failing, which breaks the setup itself, and the 12-month change of -9.4% rules out a pullback-in-uptrend setup; a lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

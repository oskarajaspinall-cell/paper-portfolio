# Evaluation: Shenzhen Transsion Holdings (SHA:688036) — 2026-11-07
## Bear case
The setup's edge is unproven. The only results release was Q3 2026 on 2026-10-30, six days before the 2026-11-05 jump, and no headline links the move to results, so this may not be an earnings reaction at all [Likely]. Volume was only at the 2.0x threshold [Certain]. The fundamentals show no beat: TTM operating margin 5.0% vs 7.7% in FY2024 and TTM FCF margin -19.1% [IS,CF] [Certain]. The minimum 2:1 target of 77.46 sits above the 52-week high of 76.20 and well above the bull fair value of 68.31 [HI] [Certain], so the reward side has no support. RSI 68.9 and a close +18.6% above the 50-day average make the entry stretched and gap-prone [ST] [Likely]. The 50-day average is below the 200-day, so the long trend is not confirmed [ST] [Certain].
## Bull case
Price has strong short-term momentum: +13.2% over 3 months and +17.6pp relative strength vs SPY, with 112% of the jump held and swing high 60.48 cleared [HI] [Certain]. The balance sheet is net cash (net debt/EBITDA -1.99x) and Altman Z is 4.11, so distress risk is low [RA,ST] [Certain]. P/E of 24.4x sits below its 5y median of 25.7x and below the peer median of 29.4x, and P/B of 3.6x is below its 5y minimum [RA] [Certain]. If Q3 marked a margin trough, TTM gross margin back at 21.1% from 18.7% in FY2025 could support a re-rating toward the 6-month high of 71.58 [IS,HI] [Guessing]. That still falls short of the 2:1 target.
## Decision
```json
{
  "ticker": "SHA:688036",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "The 2026-11-05 jump is not clearly tied to a results beat and the minimum 2:1 target lies above the 52-week high and bull fair value, so the drift trade has no supported reward.",
  "rationale": "Post-earnings drift needs a real beat; the Q3 release came six days earlier with falling margins and negative FCF. The volatility stop at 58.77 forces a 77.46 target that no evidence supports (above the 76.20 52-week high and 68.31 bull fair value). Below 2:1 on an honest target, so AVOID.",
  "price_at_decision": 65.00,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-688036/2026-11-07.md",
  "exit_plan": {"target": 77.46, "stop": 58.77, "time_limit": "2027-01-01"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 71.58, "basis": "Margins recover from the FY2025 trough (TTM gross margin 21.1% vs 18.7% [IS]) and price retests the 6-month high of 71.58 [HI], slightly above the bull fair value of 68.31 on EV/EBITDA."},
    "base": {"probability": 0.45, "target_price_12m": 61.18, "basis": "EV/EBITDA settles near its own history, giving the mechanical base fair value of 61.18 [fact sheet fair value]; the jump fades without a confirmed beat (note section 1)."},
    "bear": {"probability": 0.30, "target_price_12m": 49.03, "basis": "TTM FCF margin of -19.1% and falling operating margin [IS,CF] persist, pulling EV/EBITDA toward the low end and the price to the bear fair value of 49.03."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: the obstacle is the absence of a verified earnings-beat catalyst and a supported target, not price; a lower price would not create a drift setup.",
  "replaces": null,
  "replacement_reason": null
}
```

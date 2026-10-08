# Evaluation: Workday, Inc. (WDAY) — 2026-10-08
## Bear case
The trend has been fading since August. Swing highs step down from 227.49 to 211.83 to 201.00, and the close of 184.26 sits right on a support band of 181.47-183.60 [Certain]. That pattern looks like distribution, not a healthy dip [Likely]. To reach the 216.67 target, the stock must climb 17.6% through two supply levels (201.00 and 211.83) before the 2026-11-21 time limit [Certain]. Over roughly six weeks that is a low-odds path for a name with a 3.5% ATR [Likely]. The 12-month change is still -19.8% [Certain], so the "uptrend" is just a six-month rebound [Certain]. The P/E premium to peers (+48%) leaves room for the multiple to compress while real yields rise. The macro overlay tilts small toward bear [Likely]. A second layoff round and a law-firm "fraud" solicitation add headline risk [Guessing].
## Bull case
The setup passes the house filters. The close is 2.3% below the 50-day MA, the 50-day MA is 20.4% above the 200-day, RSI is 48.6 and earnings fall on Nov 24, outside the window [Certain]. Momentum is strong: +28.3% over 3 months and +24.3pp ahead of SPY [Certain]. The 3-month peak at 227.49 is 2.7x the stop distance away [Certain]. Short interest fell 17.0% month on month [Certain]. Fundamentals support buyers on dips: TTM operating margin is 12.0%, ROIC 18.4%, FCF margin 28.0%, P/FCF 15.6x is below its 5-year minimum, and share count is down 4.32% [Certain]. That makes a gap-down below the stop less likely [Likely].
## Decision
```json
{
  "ticker": "WDAY",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A pullback to the 50-day average after a six-month software rebound, but the lower-highs structure since the August peak and a target that must clear two resistance levels in six weeks leave the trade's edge unclear.",
  "rationale": "The filters pass, but price structure argues against the edge. Since August the highs have fallen (227.49, 211.83, 201.00) while the close sits on support. The 2:1 target needs a 17.6% rally through two supply levels before 2026-11-21. The macro overlay's small bear tilt adds to the risk. Conviction is 3, so the decision is AVOID; cash is fine.",
  "price_at_decision": 184.26,
  "price_date": "2026-10-07",
  "research_note": "research/WDAY/2026-10-08.md",
  "exit_plan": {"target": 216.67, "stop": 168.06, "time_limit": "2026-11-21"},
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 247.40, "basis": "Margin expansion continues (operating margin 12.0% TTM, ROIC 18.4% [IS,RA]) and the stock retakes its 52-week high of 247.40 [HI], still below the peer-median P/FCF of 22.4x [RA,P:*]."},
    "base": {"probability": 0.5, "target_price_12m": 196.07, "basis": "P/FCF re-rates from 15.6x to its 5-year minimum of 16.6x [RA] on flat TTM FCF (FCF margin 28.0% [CF,IS]), i.e. 184.26 x 16.6/15.6."},
    "bear": {"probability": 0.3, "target_price_12m": 156.64, "basis": "Lower highs since 227.49 [HI] resolve downward and premium-earnings-multiple compression (P/E +48% vs peers [RA]) takes the price back to the 200-day MA of 156.64 [ST,HI]; bear probability raised slightly per the macro overlay's small bear tilt on rising real yields (research/WDAY/2026-10-08-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: UCB SA (EBR:UCB) — 2026-10-24
## Bear case
The cause of the 2026-10-22 gap is not established: headlines show only a minor ZILBRYSQ autoinjector approval and an investor update, so this may not be a results beat that the market is still pricing in [Likely]. The price is already above every mechanical value. 272.70 sits above the bull fair value of 249.92. EV/Sales of 6.4x is above its 5y max, and P/FCF of 33.6x is +118% vs peers [Certain]. RSI is 80.6 and the close is 28.1% above the 50-day, while the 50-day is still 11.9% below the 200-day, so this is a recovery gap and not a clean uptrend [Certain]. The volatility stop of 227.71 sits far below the close. A 2:1 target of 362.68 would have to clear the 52-week high of 289.50 by a wide margin, and nothing in the evidence supports that [Likely]. FCF conversion has fallen to 70.6% from 129.0% [Certain].

## Bull case
The business has really improved. TTM operating margin is 29.5% vs 11.2% in FY2023, ROIC is 15.0% and ROE is 20.6% [Certain]. Management says BIMZELX is gaining global traction, especially in HS (investor update transcript, 2026-10-01) [Likely]. The price is still holding 100% of the jump, with a further +5.2% on 2.2x volume on 2026-10-23 [Certain]. Above the close there is no overhead until the 52-week high of 289.50 [Certain]. P/E of 24.1x is in line with peers and in the low part of its 5y range [Certain]. Beta is 0.19 and the balance sheet is sound (Altman Z 4.48) [Certain]. Even so, the realistic upside to 289.50 is well short of the stop distance, so the trade does not meet 2:1 [Likely].

## Decision
```json
{
  "ticker": "EBR:UCB",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A real margin and ROIC step-up has been re-rated by an unexplained gap that leaves the price above its bull fair value, and the ATR stop is too wide for any evidence-supported target to give 2:1.",
  "rationale": "The drift catalyst is unverified as a results beat. The volatility stop at 227.71 is far below the close, and the only supported target, the 52-week high of 289.50, gives well under 2:1, while the 362.68 that 2:1 requires has no support. The stock is overbought (RSI 80.6) against a falling 50-day. No position; cash is acceptable.",
  "price_at_decision": 272.70,
  "price_date": "2026-10-23",
  "research_note": "research/EBR-UCB/2026-10-24.md",
  "exit_plan": {"target": 289.50, "stop": 227.71, "time_limit": "2026-12-19"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 289.50, "basis": "BIMZELX traction (investor update transcript, 2026-10-01 [OV]) sustains the TTM operating margin of 29.5% [IS] and the price retests its 52-week high [HI], above the mechanical bull fair value because that EV/Revenue history is anchored on the weaker FY2022-23 margins."},
    "base": {"probability": 0.45, "target_price_12m": 249.92, "basis": "EV/Sales of 6.4x, above its 5y max [RA], eases back to the fact sheet's bull fair value of 249.92 [IS,RA]; the improved margin and ROIC of 15.0% [RA] justify the top of the mechanical range rather than the base."},
    "bear": {"probability": 0.30, "target_price_12m": 197.45, "basis": "The unexplained gap reverses and the price returns to its 52-week low [HI], with P/FCF of 33.6x and +118% vs peers [RA] compressing as FCF conversion stays at 70.6% [CF,IS]; this is still above the mechanical base fair value of 141.06, which ignores the margin step-up."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

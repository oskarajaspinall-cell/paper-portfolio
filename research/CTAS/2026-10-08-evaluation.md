# Evaluation: Cintas Corporation (CTAS) — 2026-10-08

## Bear case
The "strong 12-month trend" is not there: the 52-week change is -0.8% and CTAS lags SPY by 16.5pp over 12 months and 5.0pp over 6 months [Certain]. Swing highs have stepped down from 207.51 to 204.62 to 201.45 since August, and the September swing low of 191.09 undercut the August low of 196.50 [Certain]. That is a series of lower highs, not a healthy dip. The stock failed to rally on a record Q1 and a raised FY2027 guide (no earnings reaction flagged), so good news is not moving it [Likely]. The reward:risk is thin: the 2:1 target sits just under the 219.16 July peak, which is only 2.2x the stop distance away, so there is almost no margin above the minimum [Certain]. Real yields have risen into a 38.9x P/E name (macro overlay, small bear tilt) [Likely]. The next earnings date is unknown and may fall inside the window [Guessing].

## Bull case
The business is strong: ROIC rose from 21.5% to 28.4% and operating margin from 20.2% to 23.6% over five years, with leverage at 0.79x net debt/EBITDA [Certain]. Q1 FY2027 delivered record results and a raised guide [Likely]. The 50-day average is 6.5% above the 200-day and price is 4.7% above the 200-day, with RSI at 49.5: cooled off, not broken [Certain]. The P/E of 38.9x sits in the lower third of its 5-year range [Certain]. Short interest is low (3.28%) and falling [Certain]. Beta is 0.92 and the ATR is 2.0%, so the stop is not likely to be hit by noise alone [Likely]. If real yields ease, the multiple could re-rate back toward the July high [Guessing].

## Decision
```json
{
  "ticker": "CTAS",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A high-quality compounder is back near its 50-day average, but descending swing highs, a 12-month lag versus SPY and a 2:1 target that only just fits under the July peak leave the pullback trade without a clear edge.",
  "rationale": "The setup barely passes: reward:risk is exactly at the 2:1 minimum, with resistance only 2.2x the stop distance away. Lower highs since August and no rally after a beat-and-raise suggest distribution, not a dip in a trend. Rising real yields add a small bear tilt, and the earnings date is unconfirmed. Conviction 3 means AVOID; holding cash is fine.",
  "price_at_decision": 197.19,
  "price_date": "2026-10-07",
  "research_note": "research/CTAS/2026-10-08.md",
  "exit_plan": {"target": 216.69, "stop": 187.44, "time_limit": "2026-12-18"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 219.16, "basis": "Real yields ease and the record Q1 and raised FY2027 guide get rewarded, so the price retakes its 52-week high of 219.16 [HI] as ROIC (28.4%) and operating margin (23.6%) keep rising [RA,IS]."},
    "base": {"probability": 0.45, "target_price_12m": 207.51, "basis": "Fundamentals compound along the 5-year margin trend [IS] while EV/EBITDA holds near today's 26.0x [RA], taking the price back to the August swing high of 207.51 [HI]."},
    "bear": {"probability": 0.3, "target_price_12m": 181.5, "basis": "Following the macro overlay's small bear tilt (research/CTAS/2026-10-08-macro.md), higher real yields compress the P/E from 38.9x to its 5-year median of 35.8x [RA] on TTM EPS implied by the 197.19 close [HI], or about 181.5."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

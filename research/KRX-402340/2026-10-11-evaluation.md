# Evaluation: SK Square Co., Ltd. (KRX:402340) — 2026-10-11

## Bear case
This is not a healthy dip in an uptrend. It is a broken momentum stock trying to form a base. Shares fell from the 2,189,000 KRW high (2026-06-23) to a 901,000 swing low, 3-month momentum is -17.3%, and relative strength vs SPY over 3 months is -20.9pp [Certain]. The minimum 2:1 target of 1,341,790 sits above three recent swing highs (1,199,000, 1,201,000, 1,265,000), each of which has already capped rallies [Certain]. The nearest evidenced resistance at 1,265,000 gives only about 1.5:1 against the 904,107 stop [Likely]. Earnings are almost entirely non-cash stake revaluation (FCF conversion 1.2%, P/FCF 361.3x, P/B 2.5x, above its 5y max), so the price moves with the semiconductor stake, not with this company's own results [Certain]. Beta 2.44 and the macro overlay's moderate bear tilt (real yields up 44bp in a month) raise the risk of a gap through the stop [Likely].

## Bull case
The moving averages still show an uptrend: the 50-day is 19.6% above the 200-day, the price sits within 0.9% of the 50-day, and RSI is 44.5, cooled off rather than broken [Certain]. Higher swing lows (901,000 → 947,000 → 988,000) suggest the selling is exhausted and a base is forming [Likely]. P/E of 4.2x and EV/EBITDA of 3.9x sit in the bottom fifth of their own 5y ranges and well below the peer median [Certain]. There is no dilution (shares -0.65% YoY) and no distress (Altman Z 14.70) [Certain]. If the AI-memory cycle reasserts itself, a 5.6% ATR stock can cover 27.8% within 33 days and retest the 1,502,000 three-month peak [Guessing].

## Decision
```json
{
  "ticker": "KRX:402340",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A pullback to the 50-day in a high-beta holding company whose 12-month uptrend has broken down into a range, with stacked swing-high resistance below the required 2:1 target.",
  "rationale": "The setup's edge is unclear: 3-month momentum and relative strength are negative after a ~59% drawdown, and three swing highs between 1,199,000 and 1,265,000 sit below the 1,341,790 target, so the honest reward:risk is closer to 1.5:1. The macro overlay's moderate bear tilt and beta 2.44 add gap risk inside a 33-day window. Cash is preferable.",
  "price_at_decision": 1050000,
  "price_date": "2026-10-08",
  "research_note": "research/KRX-402340/2026-10-11.md",
  "exit_plan": {"target": 1341790, "stop": 904107, "time_limit": "2026-11-12"},
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 1502000, "basis": "The AI-memory cycle reasserts itself and the stock clears its swing highs to retest the 1,502,000 three-month peak [HI]; that is above the mechanical bull fair value of 1,096,055 because the FCF-based DCF ignores stake value (FCF conversion 1.2% [CF,IS])."},
    "base": {"probability": 0.4, "target_price_12m": 1050000, "basis": "P/E holds near 4.2x [RA] on flat stake-driven earnings and the stock stays in its 901,000-1,265,000 swing range [HI]; the mechanical base fair value of 93,008 is disregarded because a through-cycle FCF DCF does not value a holding company whose profit is equity-method gains (net margin 94.3% vs FCF margin 1.1% [IS,CF])."},
    "bear": {"probability": 0.4, "target_price_12m": 714000, "basis": "P/B de-rates from 2.5x to its 5y max of 1.7x [RA] as real yields compress semiconductor-stake multiples; bear weight raised from 0.30 for the macro overlay's moderate bear tilt (research/KRX-402340/2026-10-11-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

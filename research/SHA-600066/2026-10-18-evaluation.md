# Evaluation: Yutong Bus Co.,Ltd. (SHA:600066) — 2026-10-18

## Bear case
This is a cyclical bus maker priced on what look like peak earnings [Likely]. TTM ROIC of 213.2% and operating margin of 13.7% compare with -0.6% to 0.1% in FY2021-22, so the low 11.7x P/E rests on a margin peak, not on normalised profits [Likely]. P/B of 4.4x sits near the top of its 5y range, against a 1.5x peer median [Certain]. Mechanical base fair value of CNY31.50 is only +9.7% above the close, and the bear value of CNY8.22 shows how badly a margin reversal would hurt [Certain]. FCF conversion swings widely (44.4% in FY2025) [Certain]. The macro overlay tilts slightly toward bear: dollar strength and wider HY spreads weigh on export orders, the swing factor [Likely]. The stock is below its 200-day average with 6-month momentum of -21.2% [Certain]. It would also add to the portfolio's China exposure [Certain].

## Bull case
Returns, margins and cash generation have risen every year: gross margin 25.6% TTM, ROE 38.8%, FCF margin 21.4% [Certain]. Net cash in every year shown (net debt/EBITDA -1.99x TTM) and flat share count give a self-funding balance sheet [Certain]. P/E of 11.7x is below the 5y minimum of 13.0x and P/FCF of 7.3x is near its 5y low, giving a 13.76% FCF yield [Certain]. The reverse DCF implies just 2.9% year-1 growth, a low bar for China's #1 bus maker with a nationwide service network and an export franchise built over a decade [Likely]. The 5y beta of 0.13 limits the hit from global discount-rate moves [Certain]. If the higher margins prove structural (NEV mix, exports), the through-cycle DCF base of CNY37.23 is reachable [Guessing].

## Decision
```json
{
  "ticker": "SHA:600066",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-return Chinese bus leader is cheap on trailing P/E and FCF, but those multiples rest on cyclically elevated margins, and base fair value offers little margin of safety.",
  "rationale": "Quality and cash yield are real, but trailing profits sit at a cyclical high, base fair value is only modestly above the price, the macro tilt leans bear on exports and the name would add China concentration. Good but not compelling, so conviction 3 means AVOID; revisit nearer the entry price.",
  "price_at_decision": 28.71,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-600066/2026-10-18.md",
  "triggers": [
    {"text": "TTM gross margin falls below 20%, reversing the five-year uptrend (25.6% TTM).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 15%, showing the return expansion was transitory.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 7.3%, back to the FY2023 level, confirming a cyclical margin reversal.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 7.3}},
    {"text": "TTM FCF margin falls below 5%, showing cash conversion has broken down.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 44.78, "basis": "Margins prove structural and exports firm as the dollar and spreads ease, so the EV/EBITDA bull value of CNY44.78 [fact sheet fair value; RA,IS] is reached."},
    "base": {"probability": 0.5, "target_price_12m": 31.5, "basis": "Margins hold near the TTM 13.7% operating margin [IS] and the stock moves to the blended base fair value of CNY31.50 [fact sheet fair value]."},
    "bear": {"probability": 0.3, "target_price_12m": 20.05, "basis": "Margins revert from the cyclical high and export orders slip on the dollar and wider HY spreads; bear probability raised by the macro overlay's small tilt toward bear (research/SHA-600066/2026-10-18-macro.md), with the price at the EV/EBITDA base value of CNY20.05 [RA,IS]."}
  },
  "entry_price": 25.2,
  "entry_basis": "valuation file: base 31.50 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

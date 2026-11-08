# Evaluation: Etihad Etisalat Company (TADAWUL:7020) — 2026-11-08
## Bear case
The five-year margin and returns story has stalled: ROIC is flat at 14.7% against 14.8% a year earlier and operating margin is 19.8% against 20.0% [RA-T, IS-T] [Certain]. The Direction change line matters most: FCF margin fell from 20.2% to 16.1% in twelve months, 5.1pp below its 2-year high, and FCF conversion is now 89.9%, below net income [CF-T] [Certain]. The cause (capex or working capital) is unverified [Guessing], so the cheap P/E of 12.4x rests on earnings that are not converting to cash; on cash, P/FCF of 13.8x sits at 98% of its 5y range [RA] [Certain]. The mechanical bear value of 57.37 is just below the price and the base only modestly above it [Certain]. A three-player Saudi market can turn to price competition, and gross margin has fallen over five years [IS] [Likely].

## Bull case
Mobily has rebuilt itself: ROIC up from 5.7% to 14.7%, ROE 18.3%, net debt/EBITDA down from 2.13x to 0.81x, Piotroski F of 7 [RA, ST] [Certain]. P/E and EV/EBITDA both sit below their 5y minimums (13.2x and 6.5x) [RA] [Certain], and the reverse DCF implies only 1.9% year-1 revenue growth [fact sheet Fair value] [Certain]. A licensed three-player market with spectrum and network barriers is a durable structure [Likely], and 5G monetisation is the operators' stated priority (CNBC headline in the fact sheet) [Guessing]. If FCF conversion normalises, the 7.26% FCF yield and low beta of 0.10 offer a defensive, uncorrelated compounder [Likely]. Shares are not being diluted [ST] [Certain].

## Decision
```json
{
  "ticker": "TADAWUL:7020",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A restructured, deleveraged Saudi number-two telecom trades below its own 5-year minimum earnings multiples, but plateaued margins and a sharp fall in FCF conversion make it cheap on earnings and only fair on cash, leaving a modest, not compelling, skew.",
  "rationale": "Quality is real but its improvement has stalled and the last year's FCF margin fall is unexplained. Base fair value sits only modestly above the price, the mechanical bear is near it, and expected value does not clear the high-conviction bar. Good but not compelling: AVOID, with an entry price at a margin of safety.",
  "price_at_decision": 59.05,
  "price_date": "2026-11-05",
  "research_note": "research/TADAWUL-7020/2026-11-08.md",
  "entry_price": 52.79,
  "entry_basis": "valuation file: base 65.99 x 0.8; at that level the earnings-cheap, cash-fair valuation would leave enough margin of safety to carry the FCF-conversion risk.",
  "triggers": [
    {"text": "TTM operating margin falls below 17.5% (19.8% now), showing the post-restructuring margin gains are reversing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17.5}},
    {"text": "TTM ROIC falls below 12% (14.7% now), giving up a large part of the five-year improvement.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 12% (16.1% now), showing cash conversion keeps eroding; conversely a recovery toward its 2-year high of 21.2% would remove the main objection.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA on the ratios page rises above 1.5x (0.81x now), reversing the deleveraging."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 75.0, "basis": "FCF conversion recovers and P/E re-rates partway toward its 5y median 16.1x [RA]; below the mechanical bull of 99.04 because that DCF extrapolates margin gains that have plateaued [RA-T, IS-T]."},
    "base": {"probability": 0.5, "target_price_12m": 63.0, "basis": "Margins hold flat (operating margin 19.8% [IS-T]) and EV/EBITDA recovers modestly from 6.3x toward the EV/EBITDA method's base of 61.60, below the blended base 65.99 because the DCF leg leans on FCF that fell to a 16.1% margin [CF-T]."},
    "bear": {"probability": 0.3, "target_price_12m": 54.0, "basis": "FCF margin keeps falling from 16.1% [CF-T] and EV/EBITDA stays below its 5y minimum 6.5x [RA]: the EV/EBITDA method's bear value of 53.99 [fact sheet Fair value]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

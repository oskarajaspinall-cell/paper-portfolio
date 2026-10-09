# Evaluation: Yum! Brands, Inc. (YUM) — 2026-10-09
## Bear case
At 143.00 the price sits 15.3% above base fair value (121.16) and the reverse DCF needs 10.4% year-1 revenue growth [Certain]. That is a demanding bar for a business whose FY returns are falling: ROIC 46.7%→33.4% and gross margin 48.1%→45.3% [Certain]. "Cheap vs its own history" is misleading: YUM still carries a +14% EV/EBITDA, +30% P/FCF and +52% EV/Sales premium to MCD/QSR/DPZ/WEN [Certain]. Leverage is 4.15x net debt/EBITDA, Altman Z 2.34 and Piotroski 4 [Certain], and rising real yields and HY spreads (macro overlay) add discount-rate and refinancing pressure [Likely]. TTM FCF conversion fell to 75.8% [Certain]. Exiting Pizza Hut leaves two brands and no disclosed use of proceeds [Likely]. With -17 to -25pp relative strength versus SPY [Certain], the market has no catalyst before the November 3 results [Guessing].

## Bull case
KFC and Taco Bell are top-tier global franchise brands with an asset-light royalty model [Likely]. Operating margin has held near 33% for five years [Certain] and FCF margin is 19.3% [Certain]. Every multiple is below its own 5-year minimum (P/E 18.0x vs a 22.9x floor, in line with the 18.3x peer median) [Certain]. Leverage has fallen from 5.38x to 4.15x and shares shrink 1.41% a year [Certain]. The Pizza Hut sale removes a lower-margin drag and frees resources for the two growth brands, per management at Barclays [Likely]. A re-rating to the 19.0x 5-year median EV/EBITDA gives the 163.69 EV/EBITDA base value [Certain]. Beta is 0.55 [Certain]. None of this makes up for paying above base fair value while return and margin trends are still falling [Likely].

## Decision
```json
{
  "ticker": "YUM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality two-brand franchisor trades below its own 5-year multiples but still above base fair value and at a premium to peers on EV/EBITDA and P/FCF, while ROIC and gross margin trend down and leverage stays at 4.15x.",
  "rationale": "The business is good, but the price is not compelling. At 143.00 the stock is 15% above base fair value, the price implies 10.4% growth, return and margin trends are falling, leverage is 4.15x and real yields are rising. The low own-history multiples are offset by the premium to peers. Conviction 3 means no buy under the owner rule.",
  "price_at_decision": 143.00,
  "price_date": "2026-10-08",
  "research_note": "research/YUM/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin rises back above the FY2024 level of 47.5%, reversing the five-year erosion now that Pizza Hut is gone.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 47.5}},
    {"text": "TTM FCF margin rises above the FY2021 level of 22.4%, showing the two-brand portfolio converts better to cash.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 22.4}},
    {"text": "TTM operating margin rises above the FY2024 five-year high of 33.8%, evidencing post-divestiture mix benefit.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 33.8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 163.69, "basis": "Post-divestiture growth re-rates EV/EBITDA back to its 19.0x 5y median [RA], the fact sheet's EV/EBITDA base value of 163.69, above the 152.21 blended bull because the DCF leg ignores the re-rating."},
    "base": {"probability": 0.50, "target_price_12m": 130.00, "basis": "EV/EBITDA stays below its 18.0x 5y floor [RA] and the price drifts toward the blended base fair value of 121.16 [IS,CF,RA], cushioned by the 4.30% FCF yield [ST] and peer-level 18.3x P/E."},
    "bear": {"probability": 0.30, "target_price_12m": 98.02, "basis": "Falling ROIC and gross margin [RA,IS] persist and rising real yields (macro overlay research/YUM/2026-10-09-macro.md, small tilt toward bear, +0.05 moved from bull to bear) compress the premium multiple to the bear fair value of 98.02."}
  },
  "entry_price": 96.93,
  "entry_basis": "valuation file: base 121.16 x 0.8; at that level the same quality evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

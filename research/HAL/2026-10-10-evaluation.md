# Evaluation: Halliburton Company (HAL) — 2026-10-10
## Bear case
Halliburton sells a commoditised, cyclical service with no pricing power once activity falls [Likely]. The cycle is already turning. Gross margin has slipped from 18.9% (FY2023) to 15.1% TTM, ROIC from 20.9% to 13.5%, and ROE from 30.6% to 14.9% [Certain]. Middle East/Asia revenue fell 11.7% YoY in H1 2026, and H1 shareholder returns were cut to $593m from $799m [Certain]. At $32.55 the stock is only 8.2% below base fair value of $35.21, while the bear value of $24.23 is 25.5% lower, so the payoff is skewed the wrong way for a business past its peak [Certain]. The unresolved IRS dispute over the $3.5bn termination-fee deduction is a material contingency with no resolution expected within 12 months [Likely]. The stock trails SPY by 28.1pp over 6 months, short interest rose 12.6% and Q3 results are due on 20 October [Certain]. The Venezuela MOUs are non-binding and carry sanctions risk [Likely].

## Bull case
The price implies just 1.7% revenue growth, a mature-business assumption [Certain]. The stock trades at a discount to peers on P/E (-19%) and EV/EBITDA (-16%), and P/B sits near its 5-year low [Certain]. The balance sheet has de-risked: net debt/EBITDA fell from 2.75x to 1.49x, FCF conversion is 107.7% and the share count is down 3.33% YoY [Certain]. International deepwater wins are broadening the mix away from North American fracking: Eni Cronos, bp Bumerangue, and Latin America +18.1% and Europe/Africa/CIS +17.6% in H1 [Certain]. If the Venezuela MOUs turn into work, they offer optional upside the price ignores [Guessing]. If the cycle re-accelerates, the DCF bull value of $59.38 shows how much operating leverage remains [Likely]. Still, these are cyclical-recovery arguments without a dated catalyst, which is not enough for high conviction [Likely].

## Decision
```json
{
  "ticker": "HAL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraged but thin-moat oilfield-services cycle play trading near its base fair value, with margins and returns rolling over from the FY2023 peak, offers too little margin of safety for a core position.",
  "rationale": "Quality is cyclical and fading: gross margin, ROIC and ROE are all down from the FY2023 peak, and Middle East/Asia is shrinking. The price sits only 8.2% below base fair value, against 25.5% downside to bear, with an IRS contingency and Q3 results imminent. Good but not compelling, so we avoid it and hold cash; we would revisit near the margin-of-safety price.",
  "price_at_decision": 32.55,
  "price_date": "2026-10-09",
  "research_note": "research/HAL/2026-10-10.md",
  "triggers": [
    {"text": "TTM operating margin falls below 11.4%, the FY2021 five-year low, showing the services down-cycle is compressing pricing structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11.4}},
    {"text": "TTM FCF margin falls below 6.1%, the FY2022 five-year low, showing cash generation can no longer fund buybacks and deleveraging.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6.1}},
    {"text": "TTM ROIC falls below 12.7%, the FY2021 trough, showing returns are tracking the cycle down rather than holding up.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12.7}},
    {"text": "An adverse IRS ruling on the Baker Hughes termination-fee deduction, or a widening Middle East/Asia revenue decline, disclosed in an SEC 10-Q/10-K."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 45.07, "basis": "International deepwater awards (Eni Cronos, bp Bumerangue) and H1 Latin America +18.1% re-rate the stock to the bull EV/EBITDA fair value of 45.07 [RA,IS], below the DCF bull of 66.54 because cycle recovery is not yet evident in margins [IS]."},
    "base": {"probability": 0.5, "target_price_12m": 35.21, "basis": "Activity stays flat and the price converges on the blended base fair value of 35.21 (DCF 37.46 / EV/EBITDA 30.71) [IS,BS,CF,RA,ST], consistent with the 1.7% growth the reverse DCF implies."},
    "bear": {"probability": 0.3, "target_price_12m": 24.23, "basis": "Gross margin keeps sliding from 18.9% toward the FY2021 13.2% [IS] as Middle East/Asia (-11.7% H1, SEC 10-Q) and shareholder returns weaken, taking the price to the bear fair value of 24.23 [IS,BS,CF,RA,ST]."}
  },
  "entry_price": 28.17,
  "entry_basis": "valuation file: base 35.21 x 0.8 = 28.17; at that level the margin of safety would compensate for the cyclical margin decline and the IRS contingency.",
  "replaces": null,
  "replacement_reason": null
}
```

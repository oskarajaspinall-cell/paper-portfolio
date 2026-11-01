# Evaluation: Ambev S.A. (BVMF:ABEV3) — 2026-10-31
## Bear case
The stock is cheap for a reason that is not yet resolved: it fell after Lula's surprise runoff win on 2026-10-26, and the policy path (beverage taxes, BRL) is unknown [Likely]. A USD holder carries the BRL unhedged [Certain]. Growth is price-led: Q3 organic volume rose only 0.8% while revenue grew 7.6% [Likely], so margin gains rely on pricing power that a tax or consumer squeeze can erode [Guessing]. TTM FCF conversion of 156.8% sits far above the 97.6% low, so the 10.97% FCF yield may flatter normal cash generation [Likely]. ROIC is flat (25.4% to 25.3%), a mature franchise rather than a compounder [Certain]. The mechanical bear value of 11.33 BRL is about as far below the price as the base 18.03 is above it, and the bull 19.30 adds little beyond base [Certain].

## Bull case
A net-cash (-0.72x net debt/EBITDA), high-return franchise: ROIC 25.3%, operating margin up from 23.7% to 26.1% TTM, Piotroski F 7 [Certain]. It trades near the bottom of its own range (EV/EBITDA 7.1x vs 5y median 8.7x; P/FCF 9.1x at 6% of range) and below peers on P/E 14.5x vs 18.5x [Certain]. The reverse DCF prices -3.9% year-one revenue growth while Q3 grew revenue and normalized EBITDA and kept Brazil beer cost guidance [Likely]. A new 190,000,000-share buyback and shrinking share count (-0.79% YoY) add self-funded returns [Likely]. Beta 0.22 makes it a defensive diversifier [Certain].

## Decision
```json
{
  "ticker": "BVMF:ABEV3",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Ambev is a high-return, net-cash Brazilian brewer trading near the low end of its own multiple range, but an unresolved post-election policy and BRL risk plus price-led, low-volume growth leave the upside to base fair value good rather than compelling.",
  "rationale": "Quality and cash returns are real and the multiple is low, but base fair value upside is moderate, the bear value sits about as far below as base sits above, TTM cash conversion looks elevated, and the election-driven policy/BRL risk is unpriced in measurable terms. Good but not compelling: AVOID, with an entry price below base fair value.",
  "price_at_decision": 14.60,
  "price_date": "2026-10-30",
  "research_note": "research/BVMF-ABEV3/2026-10-31.md",
  "triggers": [
    {"text": "ROIC (statistics page) falls below 20%, showing the franchise's returns are eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Operating margin falls below 22%, showing pricing power lost to taxes or cost inflation.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}},
    {"text": "FCF margin falls below 17%, below the weakest fiscal year shown, showing cash generation has normalised down.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 17}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 19.30, "basis": "Margins keep expanding (operating margin 26.1% TTM [IS]) and policy fears fade, so the price reaches the mechanical bull fair value of 19.30 BRL [fact sheet Fair value]."},
    "base": {"probability": 0.50, "target_price_12m": 16.08, "basis": "Steady ROIC around 25.3% [RA] with EV/EBITDA partly re-rating toward its 5y median 8.7x [RA], i.e. the EV/EBITDA method's 16.08 BRL [fact sheet Fair value]; set below the blended base 18.03 because the post-election policy and BRL risk (https://www.fool.com/investing/2026/10/26/why-ambev-s-a-dropped-today/) argues for a lingering discount."},
    "bear": {"probability": 0.25, "target_price_12m": 11.33, "basis": "Adverse beverage-tax or consumer policy after the election plus FCF conversion falling back from 156.8% toward the 97.6% low [CF,IS] take the price to the mechanical bear fair value of 11.33 BRL [fact sheet Fair value]."}
  },
  "entry_price": 14.42,
  "entry_basis": "valuation file: base 18.03 x 0.8; at that margin of safety the same evidence, including the unresolved policy/BRL risk, would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

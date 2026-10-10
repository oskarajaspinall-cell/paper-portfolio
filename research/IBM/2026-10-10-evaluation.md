# Evaluation: International Business Machines Corporation (IBM) — 2026-10-10
## Bear case
The stock is cheap against its peers and its own P/E history, but not against its own cash flows. Base fair value is 205.24, 9.6% below the 227.13 close, and only the bull case (241.17) clears the price [Certain]. The reverse DCF already prices 5.7% year-1 revenue growth, roughly management's raised guidance, so the price needs a beat to justify itself [Likely]. IBM Z revenue fell 42% y/y in Q2. That is the mainframe cycle rolling over, and the Infrastructure trough could last several quarters [Likely]. Net debt/EBITDA is 3.47x TTM, up from 3.10x at FY2025, and shares grew 1.26% YoY, so there is no buyback support [Certain]. The macro overlay adds pressure: the 10y real yield rose 0.56pp in 3 months, which lifts the discount rate on a leveraged balance sheet [Certain]. Q3 results on Oct 21 carry binary gap risk, and there is a plaintiff-firm overhang [Guessing].

## Bull case
Five years of genuine improvement: ROIC 7.8%→14.0%, operating margin 9.7%→18.5%, gross margin up 3.3pp [Certain]. The FCF margin of 20.0% and the 6.44% FCF yield cover the dividend comfortably [Certain]. P/E of 20.2x sits at the floor of its 5y range, 19% below peers, and P/FCF is 39% below peers [Certain]. The Q2 miss was confined to one segment: Software grew 5% and Distributed Infrastructure 37% [Certain]. If the Z cycle stabilises and real yields plateau, EV/EBITDA can return toward its own base value of 218.10 or its bull value of 275.47 [Likely]. Short interest is low (2.39%), so the stock is not crowded [Certain].

## Decision
```json
{
  "ticker": "IBM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "IBM's quality has improved for five years and its multiples are low against peers and its own P/E history, but the price already sits above its cash-flow-based base fair value while the mainframe cycle declines, leverage rises and real yields climb.",
  "rationale": "The business is good but the setup is not compelling. The price is 9.6% above base fair value, the reverse DCF already embeds guided growth, net debt/EBITDA is rising again, and the shares are being diluted. The macro tilt is moderately bearish and Q3 results land on Oct 21. Conviction 3 is below the buy threshold, so we hold cash.",
  "price_at_decision": 227.13,
  "price_date": "2026-10-09",
  "research_note": "research/IBM/2026-10-10.md",
  "triggers": [
    {"text": "TTM operating margin falls below 17% (vs 18.5% TTM), reversing the five-year margin expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "TTM ROIC falls below 11% (vs 14.0% TTM), giving back most of the five-year improvement from 7.8%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 11}},
    {"text": "TTM FCF margin falls below 15%, the FY2022 five-year low, showing cash generation can no longer carry the leverage and dividend.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Software segment revenue growth in the quarterly earnings release falls below 3% y/y for two consecutive quarters."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 260, "basis": "The Z cycle stabilises and Software keeps growing (Q2 Software +5%, sec.gov 8-K Ex.99.1), lifting value between the fair-value bull of 241.17 and the EV/EBITDA bull of 275.47 [IS,RA]."},
    "base": {"probability": 0.45, "target_price_12m": 212, "basis": "Growth is roughly in line with the 5.7% the reverse DCF implies; value converges between base fair value 205.24 and EV/EBITDA base 218.10 as rising leverage (3.47x vs 3.10x FY2025 [RA]) caps any re-rating."},
    "bear": {"probability": 0.30, "target_price_12m": 150, "basis": "The Infrastructure trough extends after the 42% Q2 IBM Z decline (sec.gov 8-K Ex.99.1) and real yields keep rising, pricing near the fair-value bear of 145.43; the probability is raised for the moderate bear macro tilt (research/IBM/2026-10-10-macro.md)."}
  },
  "entry_price": 164.19,
  "entry_basis": "valuation file: base 205.24 x 0.8 (fact sheet Fair value [IS,BS,CF,RA,ST,HI]).",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Veralto Corporation (VLTO) — 2026-10-10
## Bear case
The price already discounts more than the business has shown. At 96.93 the stock trades above even the bull fair value of 82.12; the base of 76.92 is 20.6% lower, and the reverse DCF implies 12.3% year-1 revenue growth [Certain] (fact sheet, Fair value). Returns are drifting: ROCE has fallen 5.2pp in five years to 20.0% TTM and TTM ROIC of 23.5% sits below FY2025's 26.7% [Certain] (RA). Net debt/EBITDA has risen from 0.10x to 1.06x as acquisitions such as Cleanwater are debt-funded, adding integration risk and a lower return on new capital [Likely] (BS, RA, OV news). Cheap only versus its short post-spin history; P/FCF of 22.6x and a 4.43% FCF yield are not cheap in absolute terms against a 5.22% 10-year Treasury [Likely] (RA, ST, fact sheet). The 12-month change is -6.8% and relative strength vs SPY -22.5pp, so there is no momentum support [Certain] (ST, HI).

## Bull case
This is a high-quality compounder at its own-history lows. Gross margin rose 2.2pp to 60.2%, operating margin is steady near 23%, FCF conversion is 106% and ROIC is still 23.5% [Certain] (IS, CF, RA). EV/EBITDA of 18.1x and EV/Sales of 4.4x are below their 5-year minimums, and P/E of 24.4x is 20% below the peer median of 30.4x [Certain] (RA, peers). Q2 2026 beat estimates and FY26 EPS guidance was raised [Likely] (OV news, 2026-07-28). The EV/EBITDA method gives 95.70-110.04, so a reversion to the median multiple supports modest upside [Likely] (fact sheet, Fair value). A beta of 0.77, net leverage of 1.06x and buybacks (shares -0.40% YoY) cap the downside [Likely] (ST). The weakness is that the upside is a multiple re-rating of a few percent, not a mispricing.

## Decision
```json
{
  "ticker": "VLTO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, razor-and-blade water and product-quality franchise at the bottom of its short own-history multiple range, but priced above every DCF fair value case, with the reverse DCF implying 12.3% year-1 growth, so the margin of safety is missing.",
  "rationale": "The business is good: ROIC 23.5%, FCF conversion 106%, gross margin rising. But the price is 15% above even bull fair value and the reverse DCF needs 12.3% growth. EV/EBITDA reversion offers only single-digit upside, while ROCE is falling and leverage is rising. Good but not compelling, so AVOID and wait for a lower entry.",
  "price_at_decision": 96.93,
  "price_date": "2026-10-09",
  "research_note": "research/VLTO/2026-10-10.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, well under the 5-year range of 25.4%-26.7%, showing installed-base returns are eroding rather than normalising.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 21.5%, under the FY2021 5-year low of 22.1%, showing pricing or mix pressure on the consumables model.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 21.5}},
    {"text": "TTM FCF margin falls below 15%, under the FY2024 5-year low of 15.8%, signalling deteriorating cash conversion.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 110.04, "basis": "EV/EBITDA re-rates from 18.1x (below its 5y minimum) back toward its 5y range on raised FY26 guidance, matching the EV/EBITDA method bull value of 110.04 [RA, fact sheet Fair value]; above the blended bull of 82.12 because the DCF leg is weighed down by a 5.22% risk-free rate."},
    "base": {"probability": 0.5, "target_price_12m": 96.0, "basis": "Steady ~23% operating margin and 106% FCF conversion [IS, CF] hold the multiple near today's 18.1x EV/EBITDA, roughly the peer median of 18.3x [RA, peers], between the EV/EBITDA method's 95.70 bear and 100.49 base; above the blended base of 76.92 because the low-beta franchise has not traded at DCF-implied levels."},
    "bear": {"probability": 0.3, "target_price_12m": 76.92, "basis": "Falling ROCE (-5.2pp 5y) and rising net debt/EBITDA (1.06x) [RA] mean growth undershoots the 12.3% the reverse DCF implies and the price falls to the blended base fair value of 76.92 [fact sheet Fair value]."}
  },
  "entry_price": 61.54,
  "entry_basis": "valuation file: base 76.92 x 0.8 (20% margin of safety; fact sheet Fair value [IS,BS,CF,RA,ST]). The quality case is intact, so price is the only obstacle to conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

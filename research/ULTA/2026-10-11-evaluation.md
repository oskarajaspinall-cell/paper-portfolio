# Evaluation: Ulta Beauty, Inc. (ULTA) — 2026-10-11

## Bear case
The price already assumes things go well. The last close of 570.37 is 22.4% above the base fair value of 442.43 and only 5.8% below the bull case of 603.46 [Certain]. The reverse DCF implies 13.9% year-1 revenue growth, against 8.9% Q2 sales growth [Certain]. Returns keep falling. ROIC went from 40.8% (FY2023) to 25.4% TTM and operating margin from 16.1% to 12.5% [Certain]. Management blames a more promotional market and guides gross margin only roughly flat [Likely]. Net debt/EBITDA has risen from 0.60x to 1.19x as buybacks are partly funded on the revolver [Likely]. P/FCF is 45% above the peer median [Certain]. The macro overlay tilts toward bear (small): rising real yields widen the discount-rate gap [Likely].

## Bull case
This is a high-quality franchise. ROIC is still 25.4%, ROE 46.1%, FCF conversion 95.0% and Piotroski F-score 6 [Certain]. The loyalty program covers about 95% of US sales, and omnichannel members spend about 3x as much, which mass and online rivals find hard to copy [Certain]. Buybacks cut the share count 4.22% YoY [Certain]. In Q2, sales grew 8.9%, operating profit 10.1% and EPS 13.3%, and full-year guidance was raised [Certain]. EV/EBITDA of 13.8x equals its own 5-year median, and the EV/EBITDA fair value (base 553.10) supports roughly today's price [Certain]. Beauty is holding up as an affordable luxury [Likely]. Even so, nothing here offers upside large enough to justify a high-conviction entry at this price [Likely].

## Decision
```json
{
  "ticker": "ULTA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return beauty retailer with a loyalty moat, but returns and margins are eroding and the price sits 22.4% above base fair value and implies 13.9% growth that the 8.9% run-rate does not support.",
  "rationale": "The business is good, but the valuation leaves no margin of safety. The probability-weighted target sits below the 570.37 close, ROIC and operating margin are still falling, and the macro tilt is toward bear. This is good but not compelling, so it is an AVOID. Cash is an acceptable outcome; we revisit at a lower entry price.",
  "price_at_decision": 570.37,
  "price_date": "2026-10-09",
  "research_note": "research/ULTA/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, extending the decline from 40.8% (FY2023) to 25.4% and showing the moat is eroding structurally.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 11%, under the 12.5% TTM low, showing promotional competition is compressing profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11}},
    {"text": "TTM FCF margin falls below 7%, under the five-year low of 8.5%, meaning cash generation can no longer fund the buybacks.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 7}},
    {"text": "Net debt/EBITDA rises above 2.0x (TTM 1.19x) as revolver-funded buybacks lever up the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 603.46, "basis": "Fact-sheet bull fair value (DCF bull 611.85 blended with EV/EBITDA bull 586.66 [IS,RA,ST]), reached if growth meets the raised guidance and margins stabilise; probability trimmed by the macro overlay's small bear tilt (research/ULTA/2026-10-11-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 553.1, "basis": "EV/EBITDA holds near its 5y median of 13.8x [RA], giving the EV/EBITDA base fair value of 553.10; this is above the blended base of 442.43 because the market prices ULTA on multiples rather than on the DCF's growth fade."},
    "bear": {"probability": 0.3, "target_price_12m": 442.43, "basis": "Margin erosion continues (operating margin 16.1% to 12.5% [IS]) and real yields keep rising, pushing ULTA back to the blended base fair value of 442.43, near the 443.60 52-week low [HI]; probability raised by the macro overlay's small bear tilt (research/ULTA/2026-10-11-macro.md)."}
  },
  "entry_price": 353.94,
  "entry_basis": "valuation file: base 442.43 x 0.8 [RA,ST]. With the same evidence, a 20% margin of safety below base fair value would offset the falling-returns risk and justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

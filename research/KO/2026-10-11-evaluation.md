# Evaluation: The Coca-Cola Company (KO) — 2026-10-11
## Bear case
The business is excellent, but at 88.05 the price already assumes it gets even better. EV/EBITDA of 23.9x and EV/Sales of 8.1x sit above their own 5-year maximums (22.4x, 7.4x) and at +60%/+166% premiums to peers [Certain] [RA]. The reverse DCF implies 15.5% year-1 revenue growth, far above what a mature beverage franchise delivers [Likely]. The blended fair value is 62.39 base and even the bull case (69.87) is 20.6% below the close [Certain]. Cash conversion has been erratic: FCF/NI was 40-45% in FY24-25 before recovering to 99.9% TTM [Certain] [CF,IS]. Buybacks are negligible (-0.09% shares YoY) [Certain] [ST]. Under the macro overlay, rising real yields (DFII10 +0.56pp/3m) hurt a bond-proxy staple most [Likely]. The Costa exit and a new North America head add some execution noise [Guessing].
## Bull case
Quality is top-tier and still improving. ROIC is 20.1% (+3.6pp over 5y), operating margin 31.8% and gross margin 61.9%, both rising [Certain] [RA,IS]. Net debt/EBITDA has fallen to 1.64x from 2.45x [Certain] [RA]. Piotroski 8 and Altman Z 4.85 confirm balance-sheet strength [Certain] [ST]. P/E of 26.5x is in line with peers (26.1x) and near its own 5-year median of 25.2x, and P/FCF of 26.5x is close to its 5-year low [Certain] [RA]. TTM FCF margin is back at 28.5% [Certain]. Selling Costa would refocus the company on high-margin concentrate [Likely]. The stock is a beta-0.32 defensive name in a market where staples are leading [Likely]. Still, none of this offers a margin of safety. It means a fair price for a great business, not a compelling one.
## Decision
```json
{
  "ticker": "KO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Coca-Cola is a top-tier, improving franchise (20.1% ROIC, 31.8% operating margin) but trades above its own 5-year EV/EBITDA and EV/Sales ranges with the price implying 15.5% growth, leaving no margin of safety.",
  "rationale": "Quality earns a 3, but every fair-value case sits below the 88.05 close, EV multiples exceed their 5-year maximums, and the macro overlay tilts moderately to bear as real yields rise. Our P/E-based base case is roughly flat to down, so the expected return does not justify conviction 4. Cash is the better holding.",
  "price_at_decision": 88.05,
  "price_date": "2026-10-09",
  "research_note": "research/KO/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin falls below 29.0%, the FY2023 level, reversing the margin expansion that underpins the quality case.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 29.0}},
    {"text": "TTM ROIC falls below 19.1%, the FY2023 level, showing returns are being competed away.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 19.1}},
    {"text": "TTM FCF margin falls back below 21.3% (FY2023 level), showing the TTM cash-conversion recovery was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 21.3}},
    {"text": "Annual revenue growth (income statement) sustains mid-to-high single digits for two consecutive fiscal years, validating part of the growth the price implies."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 95.69, "basis": "Margins keep expanding and P/E re-rates to its 5y max of 28.8x [RA] on TTM EPS. This is above the bull fair value of 69.87 because the DCF is weighed down by FY24-25 FCF of 10-11% margins [CF,IS]."},
    "base": {"probability": 0.45, "target_price_12m": 83.94, "basis": "The P/E method base fair value of 83.94 [fact sheet Fair value]: P/E drifts toward its 5y median of 25.2x [RA] while earnings grow modestly. This sits above the blended 62.39 because the DCF leg relies on depressed FY24-25 FCF."},
    "bear": {"probability": 0.35, "target_price_12m": 76.34, "basis": "The P/E method bear fair value of 76.34 [fact sheet Fair value], near the 5y min P/E of 22.9x [RA]. Probability raised by a moderate bear tilt from the macro overlay (research/KO/2026-10-11-macro.md): DFII10 is up 0.56pp in 3 months, which raises the discount rate on a bond-proxy staple."}
  },
  "entry_price": 49.91,
  "entry_basis": "valuation file: base 62.39 x 0.8. The default margin of safety on the blended DCF/P/E base fair value [fact sheet Fair value].",
  "replaces": null,
  "replacement_reason": null
}
```

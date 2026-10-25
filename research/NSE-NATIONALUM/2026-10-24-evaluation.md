# Evaluation: National Aluminium Company (NSE:NATIONALUM) — 2026-10-24
## Bear case
This is a price-taker at peak margins. Operating margin is 43.5% TTM against 16.2% in FY2024 and 12.9% in FY2023 [Certain]; the Q4 FY2026 call itself said aluminium prices are elevated but expected to normalize and alumina faces oversupply [Likely]. The low P/E of 8.2x is cheap only on peak earnings, which is how cyclicals look at the top [Likely]. Mechanical base fair value of 263.86 INR sits 12.6% below the 301.75 close, and the reverse DCF already needs margins to hold [Certain]. FCF conversion has fallen to 75.9% as capex rises, with a captive power JV adding more [Likely]. State control subordinates capital allocation to government priorities [Likely]. The macro overlay tilts toward bear: a firmer dollar and wider spreads weigh on LME metals [Guessing]. Q2 results on Nov 2, 2026 are a near-term gap risk [Certain].
## Bull case
The cost position is real: captive bauxite gives a 71.3% TTM gross margin and ROIC of 48.1%, with net cash at -0.94x EBITDA, so even a trough (FY2023 ROIC 14.3%) is survivable without dilution [Certain]. Q1 FY2027 delivered record revenue and profit [Likely]. The stock is already -31.3% over six months with RSI 29.8, so much of the aluminium correction is priced [Likely]. It trades below peers on P/E and EV/EBITDA and near the low end of its own 5y P/E range, with a 7.94% FCF yield [Certain]. The through-cycle DCF base of 308.85 is roughly the price, so holding margins near today's level would justify it [Likely]. Beta of 0.74 limits market-driven drawdowns [Certain].
## Decision
```json
{
  "ticker": "NSE:NATIONALUM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-cost, net-cash integrated aluminium producer earning peak-cycle margins trades above its blended base fair value, so the low multiples reflect cyclical earnings rather than mispricing.",
  "rationale": "Quality and balance sheet are strong, but margins sit far above their five-year trough, management expects aluminium to normalize, the price is above base fair value and the macro tilt leans bearish. Good but not compelling: no position. A lower price would give margin of safety against margin normalisation.",
  "price_at_decision": 301.75,
  "price_date": "2026-10-23",
  "research_note": "research/NSE-NATIONALUM/2026-10-24.md",
  "triggers": [
    {"text": "TTM operating margin falls below 30%, showing the commodity-margin normalisation has arrived (TTM 43.5% now).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 25%, giving back most of the rise from 13.6% in FY2024 to 48.1% TTM.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "FCF margin turns negative, as in FY2023 (-2.8%), showing capex is outrunning cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Net debt/EBITDA on the ratios page rises above 0.0x, i.e. the net-cash buffer (-0.94x TTM) is lost to the power-plant and expansion capex."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 368, "basis": "Aluminium holds, margins stay near the 43.5% TTM operating margin [IS] and P/E re-rates from 8.2x toward its 10.0x 5y median [RA] on TTM earnings; below the mechanical bull of 451.88 because that assumes peak margins persist for a decade."},
    "base": {"probability": 0.45, "target_price_12m": 263.86, "basis": "Margins ease partly as the Q4 FY2026 call expected aluminium to normalize (https://stockanalysis.com/quote/nse/NATIONALUM/transcripts/543695-q4-25-26/), in line with the mechanical blended base fair value [valuation file]."},
    "bear": {"probability": 0.30, "target_price_12m": 173.87, "basis": "Aluminium normalises and operating margin trends toward 30% as in the macro overlay's bear path (research/NSE-NATIONALUM/2026-10-24-macro.md, small tilt toward bear lifting this probability), valued at the EV/EBITDA method base of 173.87 on own-history multiples [RA]; well above the 50.95 mechanical bear because net cash and the low-cost position limit trough damage [BS]."}
  },
  "entry_price": 211.09,
  "entry_basis": "valuation file: base 263.86 x 0.8; at that level the price would discount margin normalisation with a margin of safety.",
  "replaces": null,
  "replacement_reason": null
}
```

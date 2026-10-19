# Evaluation: Henan Shenhuo Coal Industry and Electricity Power Co. Ltd (SHE:000933) — 2026-10-19

## Bear case
Shenhuo is a price-taker in globally priced aluminum and coal [Likely], and today's earnings sit near the top of its own cycle: TTM operating margin 27.1% against 18.5% in FY2025 and 15.6% in FY2024, gross margin 31.8% against a FY2024 low of 21.1% [Certain] [IS]. On those TTM numbers the stock is not cheap versus peers: P/E 8.2x vs a 6.8x peer median and EV/EBITDA 4.5x vs 4.1x [Certain] [RA]. The mechanical base fair value of 48.33 CNY leans on the through-cycle DCF; the EV/EBITDA method's base is 23.95 CNY, below the 25.61 CNY close [Certain] [fair value]. Five-year trends in ROIC, ROCE and gross margin are all falling [Certain] [RA]. The macro overlay tilts small toward bear: stronger dollar and higher real yields weigh on USD-priced metals [Likely] (macro overlay). Results land on 2026-10-20, a binary read on whether the margin rebound holds [Certain] [OV].

## Bull case
Cash generation is exceptional: FCF yield 18.83% and P/FCF 5.3x, far below the 9.6x peer median, with FCF conversion above 148% of net income in every year shown [Certain] [ST, RA, CF]. Captive coal and power lower cost volatility versus pure smelters [Likely]. The balance sheet is close to net cash at 0.12x net debt/EBITDA, Altman Z 3.57 and Piotroski F 8 [Certain] [BS, ST]. The reverse DCF implies -18.3% revenue growth in year 1, and the mechanical bear fair value of 25.15 CNY sits almost at the price, so a lot of cyclical downside is already priced [Likely] [fair value]. ROIC never fell below 12.6% across FY2021-25, so even trough returns cover the cost of capital [Likely] [RA].

## Decision
```json
{
  "ticker": "SHE:000933",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A vertically integrated, near-net-cash aluminum producer with an 18.83% FCF yield is cheap on cash flow, but TTM margins sit well above its own five-year norms, it is a commodity price-taker, and on normalised EBITDA the price is roughly fair.",
  "rationale": "Cash yield and balance sheet are strong, but earnings look cyclically elevated, the EV/EBITDA-method base value sits below the price, returns trend lower over five years and macro tilts mildly bearish. Results are due tomorrow. Good but not compelling: conviction 3, no position; cash is acceptable.",
  "price_at_decision": 25.61,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-000933/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, under the FY2021-25 low of 12.6%, showing the captive coal/power cost edge is not holding through the cycle.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM gross margin falls below 20%, under the FY2024 low of 21.1%, showing the integrated cost advantage has eroded.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 15%, under the FY2024 five-year low of 16.7%, showing cash generation no longer backs reported profit.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 39.48, "basis": "TTM margins (operating 27.1% [IS]) hold and the market pays for the 18.83% FCF yield [ST], taking the price back to its 52-week high [HI]; below the through-cycle DCF base 60.53 because that model capitalises cash flow a price-taker cannot be sure to keep."},
    "base": {"probability": 0.45, "target_price_12m": 27.0, "basis": "Margins ease from TTM toward FY2025 levels (operating 18.5% [IS]) while EV/EBITDA drifts toward its 5y median 5.5x [RA]; lands between the EV/EBITDA-method base 23.95 and the DCF bear 30.88 [fair value], well below the blended base 48.33, which leans on the through-cycle DCF."},
    "bear": {"probability": 0.35, "target_price_12m": 20.74, "basis": "Margins revert toward the FY2024 trough (gross 21.1% [IS]) as a stronger dollar and higher real yields weigh on aluminum and coal, a small tilt toward bear per the macro overlay (research/SHE-000933/2026-10-19-macro.md), taking the price back to its 52-week low [HI], within the EV/EBITDA-method range 13.68-23.95 [fair value]."}
  },
  "entry_price": 23.95,
  "entry_basis": "Valuation file: EV/EBITDA-method base fair value 23.95 CNY [RA, IS, BS], not the blended base x 0.8 (which sits above the price because the through-cycle DCF capitalises near-peak cash flow); at that level the 18.83% FCF yield [ST] and near-net-cash balance sheet would justify conviction 4 even if margins normalise.",
  "replaces": null,
  "replacement_reason": null
}
```

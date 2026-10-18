# Evaluation: Qinghai Salt Lake Industry Co.,Ltd (SHE:000792) — 2026-10-18
## Bear case
This is a price-taker in two commodities, potash and lithium carbonate, so earnings follow benchmark prices it does not control [Likely]. ROE fell from 98.0% (FY2022) to 13.2%–20.5% (FY2024–25) and ROCE from 64.1% to 13.6% [Certain]. The cheap TTM P/E of 10.1x rests on a 56.6% net margin that is well above the FY2024 level of 30.8% [Certain]. Valuing a cyclical on peak-ish margins is the classic trap. FCF conversion has slipped to 71.8% TTM [Certain], and P/FCF of 14.1x and P/B of 2.3x are well above peer medians [Certain]. The through-cycle DCF, the best-fit method, puts base value at 20.74, below the 23.06 close [Certain]. The stock is down 40.1% over six months and trades below both moving averages [Certain]. The macro overlay tilts toward the bear case: a firmer dollar and rising real yields weigh on benchmarks [Likely]. Results are due Oct 30, 2026 [Certain].

## Bull case
Qarhan is a scarce, low-cost brine deposit, and China protects domestic potash supply [Likely]. Operating margin never fell below 35.3% over five years [Certain]. The balance sheet is net cash (net debt/EBITDA −2.68x) with Altman Z of 12.07 [Certain]. Shares are flat (0.01% YoY) [Certain]. EV/EBITDA of 7.3x sits at the 9th percentile of its 5-year range and in line with peers [Certain]. The reverse DCF implies only 0.3% year-1 revenue growth [Certain]. A lithium price recovery would lift earnings sharply off a depressed base, and the bull fair value is 33.58 [Likely]. RSI of 31.3 near the 52-week low suggests selling is mature [Guessing].

## Decision
```json
{
  "ticker": "SHE:000792",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, low-cost potash and lithium brine producer trades low in its own multiple range, but on cyclically elevated margins, with base fair value only modestly above the price and a deep bear case.",
  "rationale": "Good but not compelling. The blended base value is only slightly above the price, and the through-cycle DCF is below it. Earnings depend on commodity prices the company cannot control, returns have fallen from the 2022 peak, and the macro tilt leans bear. The low P/E reflects margins near the top of the cycle, not mispricing. Cash is acceptable.",
  "price_at_decision": 23.06,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-000792/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, showing the brine cost advantage no longer earns superior returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM net margin falls below 30%, under the FY2024 level of 30.8%, showing price declines are eroding the cost advantage.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 30}},
    {"text": "TTM FCF margin falls below 25%, under the FY2021 five-year low of 26.9%, showing cash generation is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "Net debt/EBITDA turns positive and exceeds 1x, showing the net-cash buffer has been spent or leveraged.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 33.58, "basis": "Lithium/potash benchmarks firm and margins hold near the TTM 54.4% operating margin [IS], reaching the fact sheet's bull fair value of 33.58 [Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 24.96, "basis": "Margins normalise between the FY2024 and TTM levels [IS], consistent with the blended base fair value of 24.96, where the through-cycle DCF at 20.74 is offset by EV/EBITDA at 33.39 [Fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 13.16, "basis": "Lithium oversupply pushes returns back toward the FY2024 ROE of 13.2% [RA], reaching the bear fair value of 13.16; the probability is raised by the macro overlay's small toward-bear tilt from dollar strength and rising real yields (research/SHE-000792/2026-10-18-macro.md)."}
  },
  "entry_price": 19.97,
  "entry_basis": "valuation file: base 24.96 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

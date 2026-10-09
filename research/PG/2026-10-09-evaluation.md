# Evaluation: The Procter & Gamble Company (PG) — 2026-10-09
## Bear case
At 150.59, PG trades 25.6% above the base fair value of 112.01 and 18.5% above even the bull case of 122.80 [Certain] (factsheet Fair value). The reverse DCF implies 14.0% year-1 revenue growth against FY2026 organic growth of +1% [Certain]. Management now calls pricing "defensive" after share losses in diapers and oral care, and flags a ~$1bn after-tax commodity/tariff headwind [Likely] (Barclays transcript). The stock is a premium-to-peers name on EV/Sales (+33%) and P/FCF (+28%) with only a 4.33% FCF yield, against a 5.28% 10y Treasury [Certain]. Rising real yields and a stronger dollar add discount-rate and FX-translation drag [Likely] (macro overlay). It has lagged SPY by 16.9pp over 12 months with no catalyst to reverse it before the Oct 22 results [Certain].
## Bull case
This is a franchise of rare quality: 21.5% ROIC, 24.6% ROCE (rising), 50.9% gross margin, 94.4% FCF conversion and 1.01x net debt/EBITDA [Certain] (RA, IS, CF). It trades low in its own 5y range: EV/EBITDA at the 10th percentile, P/FCF at the 14th and P/E at 21.7x–26.7x with the current 22.7x near the floor [Certain] (RA). The P/E method values it at 143.57–164.84, close to the price [Certain] (factsheet Fair value). Beta of 0.38 and buybacks (-1.30% shares) make it a defensive compounder [Certain]. China is growing +3-5% [Likely]. But "cheap vs its own history" is not cheap against the cash-flow value, so the upside is a modest re-rating, not mispricing [Likely].
## Decision
```json
{
  "ticker": "PG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A best-in-class staples franchise whose 4.33% FCF yield and 14% implied growth already price more than its +1% organic growth and defensive pricing can deliver.",
  "rationale": "Quality is excellent, but price is 18.5% above even the bull fair value and the reverse DCF needs 14% growth against +1% delivered. Cheapness is only relative to its own rich history. With a 5.28% risk-free rate and a small bearish macro tilt, the reward is a modest re-rating at best. Good but not compelling: AVOID.",
  "price_at_decision": 150.59,
  "price_date": "2026-10-08",
  "research_note": "research/PG/2026-10-09.md",
  "triggers": [
    {"text": "TTM operating margin rises above 26%, beyond the FY2025 peak of 25.6%, showing productivity is more than offsetting commodity and tariff costs.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 26}},
    {"text": "TTM FCF margin rises above 19.7%, the FY2024 high, lifting cash yield toward a level that supports the price.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 19.7}},
    {"text": "TTM gross margin falls below 48%, under the FY2023 level of 47.9% plus a buffer, confirming the cost headwind is not being offset (reinforces AVOID).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 48}},
    {"text": "Annual net sales growth on the income statement re-accelerates above +5% for a fiscal year, showing pricing has turned from defensive back to a growth lever."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 164.84, "basis": "P/E re-rates toward its 5y median of 23.9x [RA], matching the P/E-method bull value of 164.84 [factsheet Fair value]; above the blended 122.80 bull because staples trade on earnings multiples, not the 5.28%-rate DCF; probability trimmed for the small bear macro tilt (research/PG/2026-10-09-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 150.59, "basis": "P/E holds near 22.7x [RA] as +1% organic growth and the ~$1bn cost headwind (Barclays transcript) offset buybacks of -1.30% shares [ST]; sits between the P/E method base 158.02 and DCF base 89.01 [factsheet Fair value]."},
    "bear": {"probability": 0.3, "target_price_12m": 122.8, "basis": "Rising real yields (DFII10 2.92%, macro overlay) and stalled growth push the price toward the blended bull fair value of 122.80 [factsheet Fair value]; probability raised for the overlay's small bear tilt (research/PG/2026-10-09-macro.md)."}
  },
  "entry_price": 89.61,
  "entry_basis": "valuation file: base 112.01 x 0.8; at that level the 21.5% ROIC franchise would trade below its DCF base value with a margin of safety.",
  "replaces": null,
  "replacement_reason": null
}
```

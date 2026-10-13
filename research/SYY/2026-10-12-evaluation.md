# Evaluation: Sysco Corporation (SYY) — 2026-10-12
## Bear case
Sysco has just raised over $18bn of new debt and equity, about half its $38.4bn market cap, to fund the pending JRD Unico acquisition. Nobody can yet see the acquired business's earnings, price or synergies [Certain]. Net debt/EBITDA was already 2.95x before the deal [Certain], so leverage will rise after it closes [Likely]. The ~$1bn share issue at $81.00 reverses the buyback model that drove the 77.7% ROE [Certain]. The 4.2% operating and 2.1% net margins leave little room for integration mistakes or higher coupons [Certain]. US 10y and HY spreads are rising into this financing (macro overlay) [Certain]. At $78.14 the stock trades at its own base fair value of $76.51, with a bear value of $53.84 (-31.1%) [Certain]. Relative strength trails SPY by 16.5pp over 12 months [Certain]. There is no margin of safety [Likely].
## Bull case
The business itself is good: ROIC is 17.1% and ROCE 19.7% and rising, gross margin has held at 18.5% for five years, and FCF conversion is 110.3% [Certain]. Route density and scale make the largest distributor hard to replicate [Likely]. EV/EBITDA of 11.5x is below its 5y minimum of 11.6x and 22% below peers [Certain]. P/E of 21.3x sits at the 22nd percentile of its own range [Certain]. A beta of 0.64 suits a defensive staple [Certain]. If the acquisition is accretive and leverage falls quickly, the multiple could move back toward its 12.0x median, and the EV/EBITDA fair value is $84.19 to $93.16 [Guessing]. The reverse DCF implies only 4.7% growth in year 1, which a larger combined network could exceed [Guessing].
## Decision
```json
{
  "ticker": "SYY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-ROIC, scale-moated food distributor at its 5y-low EV/EBITDA, but priced at base fair value just as an undisclosed, $18bn-financed acquisition resets leverage and the equity story.",
  "rationale": "Quality is real and the multiples are low, but price equals base fair value ($76.51 vs $78.14) with no margin of safety. The acquisition is large, debt-funded and undisclosed, and the macro overlay tilts moderately toward the bear case. That is good but not compelling: conviction 3, so AVOID until the deal economics are known.",
  "price_at_decision": 78.14,
  "price_date": "2026-10-09",
  "research_note": "research/SYY/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC falls below 14% (17.1% now), showing scale advantages or the acquisition are diluting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 14}},
    {"text": "Debt/EBITDA rises above 4.5x after the acquisition closes (2.95x now), so balance-sheet risk displaces the quality thesis.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.5}},
    {"text": "TTM gross margin falls below 17.5%, under the 5y range of 17.9%-18.5%, showing loss of scale or pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 17.5}},
    {"text": "TTM FCF margin falls below 1.7%, the FY2022 five-year low, showing cash generation has broken down.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 1.7}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 93.16, "basis": "The deal proves accretive and EV/EBITDA re-rates from 11.5x toward its 5y median of 12.0x [RA], matching the EV/EBITDA bull fair value of 93.16 [fact sheet fair value]; probability cut from 0.25 by the macro overlay's moderate bear tilt (research/SYY/2026-10-12-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 76.51, "basis": "Stable 17.1% ROIC and 18.5% gross margin [RA, IS] support the blended base fair value of 76.51 [fact sheet fair value], with the reverse DCF's 4.7% implied growth roughly delivered."},
    "bear": {"probability": 0.3, "target_price_12m": 53.84, "basis": "Leverage climbs from 2.95x net debt/EBITDA [RA] on the $18bn financing (SEC 8-K, note section 6) while rates and spreads rise, so the price falls toward the bear fair value of 53.84 [fact sheet fair value]; probability raised from 0.25 by the macro overlay's moderate bear tilt (research/SYY/2026-10-12-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the pending acquisition's price, earnings and post-close leverage are undisclosed (SEC 8-K 2026-10-06), so a lower price alone would not lift conviction to 4. Re-research once filings quantify the deal.",
  "replaces": null,
  "replacement_reason": null
}
```

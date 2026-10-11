# Evaluation: Amgen Inc. (AMGN) — 2026-10-11
## Bear case
The price has run ahead of the fundamentals. AMGN is up 40.8% over 12 months and now trades above its own 5-year maximum on EV/EBITDA (15.5x vs 13.3x), EV/Sales (7.0x vs 6.4x) and P/FCF (22.0x vs 21.8x) [RA] [Certain]. It also sits 9.1% above the base fair value of 376.99, and the reverse DCF implies 8.1% year-1 revenue growth [Certain]. Meanwhile quality is eroding. ROIC fell from 24.8% to 19.8%, gross margin from 75.2% to 71.9% and FCF margin from 32.3% to 26.7% [RA,IS,CF] [Certain]. Prolia/Xgeva lost core patent protection in the US and EU in 2025, and Enbrel protection fades after that (10-K) [Certain]. Net debt/EBITDA is still 2.51x and Altman Z is 1.89 [Certain]. The FDA's TAVNEOS withdrawal request is unresolved [Likely]. Biosimilar erosion could outpace the launches [Likely].
## Bull case
The pipeline is delivering. In the Phase 3 DeLLphi-305 trial, Imdelltra plus Imfinzi showed an overall-survival benefit in first-line small cell lung cancer, and the FDA eased Imdelltra's monitoring requirements (PRNewswire, Sept 2026) [Certain]. Dazodalibep met its Phase 3 endpoint in Sjögren's disease (Reuters, 2026-09-22) [Certain]. MariTide has six Phase 3 studies running (10-K) [Certain]. Quarterly revenue topped $10 billion (Morgan Stanley transcript) [Likely]. On P/E, AMGN still looks reasonable: 25.8x sits at the 34th percentile of its 5-year range and 13% below peers [RA] [Certain]. Piotroski is 8 and deleveraging continues, with net debt/EBITDA down from 3.96x to 2.51x [Certain]. Relative strength is +25.1pp over 12 months, and the beta of 0.41 makes it a defensive compounder [Likely]. The thesis needs pipeline growth to beat the implied 8.1%, which is possible but not proven [Guessing].
## Decision
```json
{
  "ticker": "AMGN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return biopharma with real pipeline wins (Imdelltra OS, dazodalibep, MariTide) but eroding margins and ROIC as Prolia/Xgeva go biosimilar, now priced above its own 5-year maximum EV/EBITDA and P/FCF and 9.1% above base fair value.",
  "rationale": "The pipeline is genuine but already priced in. Multiples sit above their 5-year highs while ROIC, gross margin and FCF margin trend down, and probability-weighted scenarios land below the current price. Healthcare is already held via CI and ZTS. This is good but not compelling, so it is an AVOID at conviction 3, with entry at base fair value less a 20% margin of safety.",
  "price_at_decision": 414.87,
  "price_date": "2026-10-09",
  "research_note": "research/AMGN/2026-10-11.md",
  "triggers": [
    {"text": "TTM net debt/EBITDA rises back above 3.5x, showing post-Horizon deleveraging has stalled (2.51x now, 3.96x FY2023 peak).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}},
    {"text": "TTM gross margin falls below 68%, a new 5-year low (FY2024 68.7%), signalling biosimilar erosion is outpacing new launches.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 68}},
    {"text": "TTM ROIC falls below 15%, under the FY2024 trough of 14.9%, showing returns are converging on the cost of capital.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 20%, under the FY2025 5-year low of 22.0%, showing cash generation is deteriorating with the legacy franchises.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 470, "basis": "Imdelltra's first-line OS win and dazodalibep's Phase 3 success (PRNewswire/Reuters, Sept 2026) drive growth above the 8.1% reverse-DCF implied rate, moving toward the 528.16 bull fair value [fact sheet] but held below it because gross margin is still falling [IS]."},
    "base": {"probability": 0.45, "target_price_12m": 395, "basis": "Launches roughly offset Prolia/Xgeva erosion (10-K), so P/E stays near 25.8x [RA] while the rich EV/EBITDA of 15.5x (above the 13.3x 5y max) drifts lower, leaving the price slightly above the 376.99 base fair value [fact sheet]."},
    "bear": {"probability": 0.30, "target_price_12m": 320, "basis": "Biosimilar erosion pushes gross margin toward its 68.7% FY2024 low [IS] and EV/EBITDA reverts toward its 12.6x 5y median [RA] on 2.51x net leverage, landing between the 288.90 bear fair value and the 344.25 P/E bear [fact sheet]."}
  },
  "entry_price": 301.59,
  "entry_basis": "valuation file: base 376.99 x 0.8; at that level the 5-year-high multiples would have reset and the pipeline optionality would be underpriced.",
  "replaces": null,
  "replacement_reason": null
}
```

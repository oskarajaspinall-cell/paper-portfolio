# Evaluation: Aluminum Corporation of China Limited (HKG:2600) — 2026-10-18
## Bear case
Chalco is a price-taker in alumina and aluminum; every quality metric sits at a cyclical peak: gross margin 23.0% TTM vs 12.1% in FY2021, ROIC 23.6% TTM vs a 10.1% FY2023 trough [IS, RA] [Certain]. A P/E of 6.2x below its 5y floor of 9.2x is what peak-cycle earnings look like, not a mispricing [Likely]. The share price fell 44.7% in six months while TTM figures kept improving, which suggests the market is discounting lower realised prices that trailing statements do not yet show [Guessing]. The macro overlay tilts toward bear: a broad dollar at 121.602 and US real yields at 2.78% pressure USD-priced aluminum benchmarks [macro overlay] [Likely]. Q3 results on Oct 29, 2026 are an imminent binary [ST] [Certain]. State control (insiders 0.01%) limits minority influence [Likely], and the stock would add a fourth China name to the book [Certain].
## Bull case
The balance sheet has been transformed: net debt/EBITDA from 2.12x to 0.18x TTM [RA] [Certain], so a downturn no longer threatens solvency. FCF margin of 15.2% TTM and an FCF yield of 26.63% [CF, ST] mean the company could return a large share of its market cap within a few years if cash flow holds even partially [Likely]. Even the mechanical bear fair value (HK$10.91) sits above the HK$7.27 close, and the reverse DCF implies a -19.2% year-1 revenue decline [fact sheet] [Certain]. It trades below peers on EV/EBITDA (3.8x vs 5.6x) and P/FCF (3.8x vs 17.6x) [RA, peers] [Certain]. Piotroski F of 7 and Altman Z of 3.04 confirm financial health [ST] [Certain]. Shares are flat (+0.23% YoY), so no dilution [ST] [Certain].
## Decision
```json
{
  "ticker": "HKG:2600",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraged, cash-rich Chinese aluminum producer trades below its own 5-year multiple floors, but on peak-cycle margins that a sharp six-month share-price fall suggests are already rolling over.",
  "rationale": "Cheap on every multiple and financially strong, but the cheapness rests on peak-cycle margins in a price-taking commodity business; the price collapse, bearish dollar tilt and Q3 results within two weeks leave earnings visibility too low for conviction 4. Adding a fourth China exposure also concentrates risk. Cash is acceptable.",
  "price_at_decision": 7.27,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-2600/2026-10-18.md",
  "triggers": [
    {"text": "TTM gross margin falls below 15%, showing the cycle has turned against realised prices and costs, the core downside risk behind this AVOID.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 10%, back to the FY2022-23 trough, confirming current returns were cyclical rather than structural.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 5%, showing cash generation is deteriorating faster than reported earnings.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}},
    {"text": "Q3 2026 results (due Oct 29, 2026) show TTM gross margin holding at or above the FY2025 level of 17.8% despite the share-price fall, which would argue the margin gains are more durable and warrant re-research toward a BUY."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 12.22, "basis": "Margins hold near the TTM 23.0% gross margin [IS] and the stock re-rates to the mechanical EV/EBITDA base fair value of HK$12.22 [fact sheet], still below the HK$14.40 blend because peak-cycle EBITDA should not earn a full multiple."},
    "base": {"probability": 0.42, "target_price_12m": 8.5, "basis": "Realised prices soften as the six-month -44.7% move [HI] implies, margins drift back toward the FY2025 17.8% gross margin [IS], and the low EV/EBITDA of 3.8x [RA] re-rates only modestly; below the mechanical bear HK$10.91 because that model is built on peak TTM figures."},
    "bear": {"probability": 0.33, "target_price_12m": 5.6, "basis": "Commodity downturn takes returns back to the FY2023 trough (ROIC 10.1%, gross margin 12.8%) [RA, IS], amplified by the macro overlay's small tilt toward bear from dollar strength and rising real yields (research/HKG-2600/2026-10-18-macro.md), which moved weight from base to bear."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below the mechanical bear fair value of HK$10.91; the obstacle is peak-cycle earnings visibility in a price-taking commodity business, so a lower price on the same evidence would not lift conviction. Q3 2026 results showing margins holding would.",
  "replaces": null,
  "replacement_reason": null
}
```

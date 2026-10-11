# Evaluation: United Airlines Holdings, Inc. (UAL) — 2026-10-11
## Bear case
Profitability is already rolling over: operating margin fell from 9.8% (FY23) to 7.0% TTM, ROIC from 13.8% to 10.3%, gross margin from 34.2% to 31.8% [Certain] (IS, RA). The market pays for it anyway: EV/EBITDA of 7.3x sits above its own 5y max of 7.0x [Certain] (RA), and that multiple is on earnings that are still falling. H1 2026 net debt rose about $1.3bn and buybacks were nearly stopped (10-Q) [Certain]. The Altman Z of 1.31 and beta of 1.30 [Certain] (ST) leave the stock exposed to a fuel or demand shock. So does the status-match war with Delta and American, which costs money to defend loyalty [Likely]. Real yields are up 0.56pp in 3m (macro overlay), which pressures the multiple of a 2.4x-levered cyclical [Likely]. Q3 results are due Oct 20, so the margin trend gets tested within days [Certain].
## Bull case
UAL trades 29-53% below the peer median on P/E, EV/EBITDA and P/FCF, at a 7.29% FCF yield [Certain] (RA, ST). The reverse DCF implies -0.9% year-1 revenue growth, yet H1 2026 passenger revenue rose 16.3% (10-Q) [Certain], and fares are rising on constrained capacity (CNBC headline) [Likely]. Net debt/EBITDA has fallen from 4.30x to 2.40x and the share count fell 1.48% YoY [Certain]. Starlink and the status match could win premium share at hubs where slots are scarce [Guessing]. The through-cycle base fair value is $162.58, 51% above the price [Certain].
## Decision
```json
{
  "ticker": "UAL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A recovered, peer-discounted network carrier whose returns and margins are rolling over from their FY2023 peak while its EV/EBITDA sits above its own 5-year maximum, so the cheap-to-peers headline does not offer a margin of safety.",
  "rationale": "Peer discount and low implied growth are real, but TTM operating margin, ROIC and gross margin are all declining. EV/EBITDA is above its 5y max, leverage and Altman Z are weak, Q3 results land Oct 20 and the macro tilt is toward bear. Probability-weighted value is below the price. That is good but not compelling, so no position.",
  "price_at_decision": 107.45,
  "price_date": "2026-10-09",
  "research_note": "research/UAL/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 9%, back to the FY2023-FY2024 range, showing the margin decline was transitory (would argue for re-research toward a BUY).", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 9}},
    {"text": "TTM ROIC recovers above 12%, back to the FY2024-FY2025 level, showing returns are holding through the cycle.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 12}},
    {"text": "Net debt/EBITDA falls below 2x, evidencing real deleveraging rather than H1 2026 refinancing.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 2}},
    {"text": "TTM FCF margin rises above 6.7%, the FY2024 five-year high, showing cash conversion is improving despite fleet capex.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 6.7}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 162.58, "basis": "Demand strength (H1 passenger revenue +16.3%, 10-Q) and premium share gains restore margins, so the stock re-rates to the through-cycle base fair value of 162.58 (fact sheet Fair value)."},
    "base": {"probability": 0.5, "target_price_12m": 110.0, "basis": "P/E holds near its 5y median of 10.5x [RA] on roughly flat TTM EPS as margin erosion (op margin 7.0% TTM vs 8.6% FY25 [IS]) offsets buybacks; this is below the mechanical base because the DCF assumes through-cycle margins that the TTM trend does not support."},
    "bear": {"probability": 0.3, "target_price_12m": 55.0, "basis": "A fuel/demand shock takes P/E toward its 5y min of 5.2x [RA], near the EV/EBITDA bear value of 41.41 (fact sheet Fair value); probability raised by 0.05 from base for the small toward-bear macro tilt (rising real yields on a 2.4x-levered, high-beta name, research/UAL/2026-10-11-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: TTM operating margin, gross margin and ROIC are all falling from their FY2023-FY2024 levels, and Q3 results on Oct 20 are unresolved. A lower price would not change the decision until the margin trend stabilises (see triggers).",
  "replaces": null,
  "replacement_reason": null
}
```

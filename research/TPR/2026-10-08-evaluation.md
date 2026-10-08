# Evaluation: Tapestry, Inc. (TPR) — 2026-10-08
## Bear case
The cheapness is narrower than the screen suggests. Only P/E (15.6x, 7th percentile) looks low; EV/EBITDA of 12.5x sits above its 5y median of 9.3x and in line with peers, and P/FCF of 12.4x is at its 5y median [Certain]. Margins are at five-year peaks (gross 76.6%, operating 23.3%), so the base effect now works against them: any promotional creep at Coach, which is 86.4% of sales, flows straight to earnings [Likely]. The stock fell 22.5% in three months and lagged SPY by 26.4pp while short interest (8.09%) keeps rising, a sign that informed sellers expect a weaker print on Nov 5 [Guessing]. The 197.1% ROE and 32.8x P/B reflect a buyback-thinned equity base, not better economics [Likely]. Beta of 1.43 adds discretionary-cycle risk [Certain].
## Bull case
This is a best-in-class accessible-luxury franchise: ROIC rose from 20.7% to 43.5%, FCF margin from 11.4% to 22.6%, and net debt/EBITDA fell to 1.39x [Certain]. An 8.05% FCF yield funds a 5.53% annual share-count reduction and a dividend raised 16%, so holders earn a return with no re-rating [Certain]. P/E is a 25% discount to peers despite structurally higher margins [Certain]. Exiting Stuart Weitzman leaves a simpler two-brand portfolio that focuses investment on Coach [Likely]. The macro overlay ties the sell-off to stock-specific sentiment, not rates or credit, so solid results on Nov 5 could reverse it [Likely].
## Decision
```json
{
  "ticker": "TPR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Tapestry is a high-return, cash-generative Coach franchise at peak margins, but at a mid-range EV/EBITDA and P/FCF it is fairly valued rather than mispriced, so the risk/reward is not compelling.",
  "rationale": "Quality is excellent but valuation is only cheap on P/E; EV/EBITDA is above its 5y median and P/FCF at its median. Peak margins, 86% Coach concentration, rising short interest and earnings on Nov 5 leave an asymmetric downside. Good but not compelling: conviction 3, so no position. Macro is context only.",
  "price_at_decision": 113.42,
  "price_date": "2026-10-07",
  "research_note": "research/TPR/2026-10-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 20%, reversing most of the expansion from 17.6% (FY2022) to 23.3%, showing Coach pricing power is eroding.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM gross margin falls below 70%, back to FY2022-FY2023 levels, signalling promotional creep.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 70}},
    {"text": "TTM FCF margin falls below 15%, under the FY2025 level of 15.6%, meaning the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 29%, back to the FY2025 level, showing the post-divestiture returns gain has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 29}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 150.9, "basis": "Margins hold and P/FCF re-rates from 12.4x to its 5y max of 16.5x [RA] on steady TTM FCF [CF] as the sentiment-driven sell-off reverses (Bull case)."},
    "base": {"probability": 0.5, "target_price_12m": 114.0, "basis": "P/FCF stays near its 5y median of 12.5x [RA] on flat TTM FCF [CF], with buybacks (-5.53% shares YoY [ST]) offsetting no re-rating."},
    "bear": {"probability": 0.25, "target_price_12m": 78.7, "basis": "Coach promotional pressure from peak margins (operating margin 23.3% [IS]) compresses P/FCF to its 5y min of 8.6x [RA] (Bear case)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

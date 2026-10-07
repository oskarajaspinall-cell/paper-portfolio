# Evaluation: Barrick Mining Corporation (TSX:ABX) — 2026-10-07

## Bear case
Record returns are mostly gold-price leverage, not a moat: TTM gross margin 56.3% vs 30.4% in FY2023, and a price-taker cannot defend that if gold reverses [Likely]. The low P/E (10.4x) is a peak-earnings multiple; on mid-cycle margins the stock is not cheap [Likely]. P/FCF 12.7x is already 10% above the peer median, and FCF conversion has fallen to 79.5% from ~96-100% as capex rises [Certain]. Concentrated jurisdictional risk: multiple unions issued strike notices at the flagship Loulo-Gounkoto complex in Mali [Likely]. The North American IPO, the main re-rating catalyst, reportedly faces investor opposition and slippage to 2027 [Likely]. Short interest rose 43.5% month-on-month, albeit from a low 0.72% of float [Certain].

## Bull case
Quality has stepped up across every metric: ROIC 23.7% TTM vs 9.4% FY2021, operating margin 51.9%, FCF margin 25.1% [Certain]. The balance sheet is net cash (net debt/EBITDA -0.10x) and shares outstanding fell 3.00% YoY, so cash is being returned [Certain]. Valuation is below ABX's own 5-year floor on P/E (10.4x vs 12.6x min) and EV/EBITDA (5.4x vs 5.9x min), and 24% / 19% below peers on those multiples [Certain]. FCF yield of 7.84% gives a cushion even if margins partly revert [Certain]. Management reports four consecutive quarters of meeting guidance; an IPO of North American assets could crystallise sum-of-parts value [Likely]. Altman Z 3.68 signals low financial-distress risk [Certain].

## Decision
```json
{
  "ticker": "TSX:ABX",
  "decision": "BUY",
  "position_type": "CORE",
  "core_initiation": false,
  "conviction": 3,
  "thesis": "A net-cash, low-cost gold major earning a 23.7% ROIC trades below its own 5-year multiple floor and peers, so the market is over-discounting margin reversion and Mali/IPO risk.",
  "rationale": "Cheap versus own history and peers, net cash, buybacks and 7.84% FCF yield justify a position. Size held at 5%, not higher, because margins are gold-price-driven rather than moat-protected, Mali is a concentrated labour risk, and P/FCF is not cheap versus peers. Empty portfolio: no limit breached, no replacement needed.",
  "price_at_decision": 57.95,
  "price_date": "2026-10-06",
  "research_note": "research/TSX-ABX/2026-10-07.md",
  "triggers": [
    {"text": "Gross margin falls below 40%, signalling reversion toward FY2022-23 margin levels.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
    {"text": "ROIC falls below 10%, erasing the step-change in capital returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "FCF margin falls below 10%, signalling capex overrun or a Mali disruption hitting cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA (fact-sheet net definition) rises above 0.5x, signalling releveraging."}
  ],
  "replaces": null,
  "replacement_reason": null
}
```

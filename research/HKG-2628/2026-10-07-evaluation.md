# Evaluation: China Life Insurance Company Limited (HKG:2628) — 2026-10-07

## Bear case
The 2.7x P/E is an artefact, not a bargain: TTM ROE of 41.3% versus 11.1%-15.8% in FY2021-FY2023 almost certainly reflects mark-to-market investment gains in a strong A-share year, which reverse when markets or bond yields turn [Likely]. On the metric that matters for insurers, P/B, the stock is 1.4x, 36% above the 1.0x peer median, and P/FCF is 47% above peers [Certain]. Earnings are leveraged to China's falling bond yields and equity market, and the September capital-injection package may imply policy-directed balance-sheet use rather than shareholder returns [Guessing]. The share is below its 50- and 200-day averages with negative 3-month momentum, and Q3 results on Oct 29, 2026 could print a sharp normalisation [Likely]. Piotroski F-score of 5 is middling [Certain].

## Bull case
Even if ROE normalises to the FY2021-FY2023 range (11.1%-15.8%), a 1.4x P/B still implies a high earnings yield on book, which is cheap for China's largest, state-backed life franchise [Likely]. P/B sits at its own 5-year low, and P/E and EV/EBITDA are below their 5-year minimums [Certain]. ROIC and ROE have trended up over five fiscal years (ROE 11.1% to 27.7%), so the improvement predates the TTM spike [Certain]. Leverage has fallen (net debt/EBITDA 4.48x to 0.38x TTM, site definition), and there is no dilution (shares -0.00% YoY) [Certain]. The Sept 2026 state capital package signals implicit sovereign support for the sector [Likely]. Beta of 0.90 diversifies an all-cash portfolio [Certain].

## Decision
```json
{
  "ticker": "HKG:2628",
  "decision": "BUY",
  "position_type": "CORE",
  "core_initiation": false,
  "conviction": 2,
  "thesis": "China's largest state-backed life insurer trades at its own 5-year-low P/B with a five-year rising ROE trend, offering value even if TTM investment-driven earnings normalise.",
  "rationale": "Valuation is attractive versus its own history and the franchise is backed by the state, but the earnings spike is likely investment-driven, P/B and P/FCF are above peers, and Q3 results are due Oct 29. Those risks cap conviction at 2 (3% starter). The portfolio is all cash, so no limits bind.",
  "price_at_decision": 27.30,
  "price_date": "2026-10-06",
  "research_note": "research/HKG-2628/2026-10-07.md",
  "triggers": [
    {"text": "ROE (TTM, statistics page) falls below 14.8%, the FY2023 level, showing the improvement was not durable.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 14.8}},
    {"text": "ROIC (TTM, statistics page) falls below 9.0%, the FY2023 level, erasing the FY2021-FY2025 improvement trend.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9.0}},
    {"text": "Debt/EBITDA (statistics page) rises above 2.81x, the FY2023 site-definition level, reversing the deleveraging trend.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.81}},
    {"text": "FCF conversion (FCF/net income, cash flow and income statement pages) turns negative, so cash earnings no longer track reported profit."}
  ],
  "replaces": null,
  "replacement_reason": null
}
```

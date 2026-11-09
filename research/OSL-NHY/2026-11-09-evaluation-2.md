# Evaluation: Norsk Hydro ASA (OSL:NHY) — 2026-11-09
## Bear case
Hydro is a price-taker. Returns are cyclical, not a franchise: ROIC fell from a 38.2% FY2022 peak, and in the last 12 months ROCE dropped 2.7pp and FCF margin fell to 3.2%, 2.4pp below its 2-year high [Certain]. Q3 core profit missed expectations, and management warned of higher costs and lower realised metal prices (Reuters URL in the note) [Likely]. Neither direction change looks one-off. The Alunorte gas problem has an uncertain financial impact and no long-term fix (WSJ, fact sheet) [Likely], and Q3 commentary cites working capital pressure [Likely]. Cash generation is thin: P/FCF is 20.4x, almost double the peer median [Certain]. The fair-value bear case of 28.59 NOK shows how sensitive a through-cycle DCF is to the commodity deck [Certain]. The 6-month fall of -34.9% may be the market pricing an earnings roll-over rather than overreacting [Guessing]. The 25 November Investor Day could reset targets either way [Certain].
## Bull case
EV/EBITDA is 2.9x, near the bottom of its tight 5y range and below peers, and P/B is 1.2x, the 5y low [Certain]. The balance sheet is close to net cash (net debt/EBITDA 0.28x) and Altman Z is 3.51, so a downturn can be ridden out without dilution [Certain]. The share count is shrinking [Certain]. Over three years returns are up: ROIC is up 7.8pp and operating margin up 2.4pp, and TTM ROIC of 23.9% is high for a smelter [Certain]. Low-carbon Norwegian hydropower and integrated alumina give a cost and carbon edge that rivals struggle to copy [Likely]. Q3 still delivered record Norwegian smelter output (fact-sheet transcript summary) [Likely]. The reverse DCF implies only 0.4% year-1 growth, and base fair value is 80.43 NOK [Certain]. The FCF dip comes from working capital and capex timing, given how widely FCF conversion swings, not from lost share [Likely].
## Decision
```json
{
  "ticker": "OSL:NHY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The ROCE and FCF-margin declines are cyclical, not a loss of share. Q3 cites Alunorte gas costs, working capital and lower realised prices (Reuters and WSJ URLs in the note). FCF conversion swings widely year to year [CF], and the balance sheet stays intact at net debt/EBITDA 0.28x [RA].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Lower realised aluminium prices plus unresolved Alunorte gas costs compress EBITDA, turning the low EV/EBITDA into a value trap.",
    "veto": null
  },
  "thesis": "A low-cost, near-net-cash integrated aluminium producer trades near the bottom of its own EV/EBITDA and P/B ranges, but cash generation is thin and falling, and near-term earnings face cost and realised-price headwinds.",
  "rationale": "Cheap on EBITDA and book with a strong balance sheet, but the edge is cyclical. FCF margin and ROCE are falling into a guided cost and price squeeze, and the bear fair value is far below the price. The scorecard gives conviction below the buy bar, so this is an AVOID. Re-research nearer the margin-of-safety price or after the Investor Day.",
  "price_at_decision": 68.38,
  "price_date": "2026-11-06",
  "research_note": "research/OSL-NHY/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, back toward the FY2023 trough of 14.7%, showing the cost advantage is not protecting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 17%, well under the FY2025 five-year low of 19.8%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "Net debt/EBITDA rises above 1.0x (0.28x TTM now), showing the balance-sheet cushion is being used up.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "TTM FCF margin turns negative (3.2% now), meaning working capital and Alunorte costs are consuming cash.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 96.82, "basis": "Alunorte costs normalise and the price recovers to its September swing high of 96.82 [HI], above the EV/EBITDA bull value of 88.85 on a re-rating toward peers at 4.1x [RA,P]."},
    "base": {"probability": 0.45, "target_price_12m": 80.43, "basis": "EBITDA holds near TTM and EV/EBITDA moves back toward its 5y median of 3.3x [RA], in line with the mechanical base fair value of 80.43 NOK [fact sheet Fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 52.0, "basis": "The Q3 warning of higher costs and lower realised prices (Reuters URL in the note) cuts TTM EBITDA while EV/EBITDA stays near its 5y minimum of 2.7x [RA]; the bear target sits above the mechanical bear of 28.59 because net debt/EBITDA of 0.28x [RA] rules out a balance-sheet collapse."}
  },
  "entry_price": 64.34,
  "entry_basis": "valuation file: base 80.43 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

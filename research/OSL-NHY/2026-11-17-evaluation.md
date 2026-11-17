# Evaluation: Norsk Hydro ASA (OSL:NHY) — 2026-11-17
## Bear case
The fall has a fundamental cause, not just sentiment: Q3 core profit missed and management guided higher smelter costs, lower realised metal prices and softer demand [Likely] (Reuters headline, fact sheet). Alunorte gas-supply costs are open-ended [Likely]. Cash is the weak point: FCF margin is 3.2% TTM, down from 4.6% a year earlier and below its 2-year high of 5.6%, and ROCE fell 2.7pp in 12 months [Certain]. Both direction changes stem from costs and working capital at a cyclical producer, so they could deepen if aluminium weakens [Likely]. P/FCF of 19.9x is above peers [Certain]; the low P/E and EV/EBITDA rest on earnings that track a commodity price [Likely]. The fair-value range (bear 28.25 to bull 150.28) is very wide and NAV is unavailable, so the 15.4% base upside is a fragile anchor [Certain]. The price sits 25.2% below its 200-day average, so there is no trend support [Certain].
## Bull case
The balance sheet is strong: net debt/EBITDA 0.28x and Altman Z 3.51 [Certain], so this is a cyclical trough with capacity intact, not a broken model [Likely]. TTM ROIC 23.9% is flat over the year and up 7.8pp over 3 years; operating margin 21.7% is near its 2-year high [Certain]. Q3 brought record Norwegian smelter output and progress in low-carbon and recycled aluminium [Likely] (transcript headline). EV/EBITDA 2.8x is near its 5y low and well below the peer median 6.4x; P/E 10.3x is at the 13% position of its 5y range [Certain]. The reverse DCF implies only 1.0% year-1 revenue growth [Certain]. A weaker real may ease Alunorte's BRL costs (macro overlay, inference). The Investor Day on 2026-11-25 could reset capital returns [Guessing]. A small net buyback (-0.49% shares) adds support [Certain].
## Decision
```json
{
  "ticker": "OSL:NHY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "FCF margin (3.2% TTM vs 4.6% a year earlier) and ROCE are falling on guided cost pressure, Alunorte gas costs and working capital (Reuters 2026-10-23 headline, Q3 transcript headline [OV]), while net debt/EBITDA stays at 0.28x [RA] and ROIC is flat: a cyclical cost squeeze with the balance sheet intact.", "moat": "narrow", "key_risk": "high", "key_risk_text": "Lower realised aluminium prices plus higher smelter and Alunorte gas costs (guided in Q3) squeeze margins and FCF further; impact size is uncertain.", "veto": null},
  "thesis": "A low-cost, low-leverage aluminium producer trading near the bottom of its own multiples, but with guided cost and price headwinds and thin FCF, the cyclical recovery is not yet evidenced.",
  "rationale": "The price fall follows a Q3 miss and guided cost and price headwinds: a cyclical squeeze, not an overreaction that clearly leaves upside. Same evidence as the 2026-11-09 AVOID at a similar price; the scorecard stays below the buy bar. Cash is acceptable.",
  "price_at_decision": 68.14,
  "price_date": "2026-11-16",
  "research_note": "research/OSL-NHY/2026-11-17.md",
  "triggers": [
    {"text": "ROIC TTM falls below 15% (statistics page)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "Operating margin TTM falls below 17%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "FCF margin TTM turns negative", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Net debt / EBITDA (ratios page) rises above 1.0x"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 88.85, "basis": "Costs ease and realised prices recover, so EV/EBITDA moves toward its 5y max 3.6x [RA], in line with the mechanical EV/EBITDA bull value 88.85 [fact sheet fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 75.97, "basis": "Margins hold near today's 21.7% operating margin [IS] and the stock reverts to the through-cycle DCF base 75.97, slightly below the blended base 78.65 because FCF margin is still falling [CF-T]."},
    "bear": {"probability": 0.3, "target_price_12m": 48.0, "basis": "Guided higher smelter and Alunorte gas costs plus lower realised prices (Reuters headline [OV]) cut earnings, P/E compresses toward its 5y low 6.2x [RA]; above the DCF bear 28.25 because leverage is only 0.28x [RA]."}
  },
  "entry_price": 66.85,
  "entry_basis": "valuation file: base 78.65 x 0.85",
  "replaces": null,
  "replacement_reason": null
}
```

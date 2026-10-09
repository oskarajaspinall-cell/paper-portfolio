# Evaluation: Autodesk, Inc. (ADSK) — 2026-10-08
## Bear case
The cheapness is against history, not against the cash flows. The mechanical fair value puts base at 219.04 (-6.8%) and bull at only 259.84 (+10.5%), while the reverse DCF says the price still implies 20.6% year-1 revenue growth [Certain]. Management guided Q3 and FY below expectations at the 2026-08-28 print despite a beat, so the growth path is being reset, not raised [Likely]. The 10-K concedes "limited barriers to entry", and AI-native design tools from Adobe, Bentley, Dassault or PTC could erode seat-based pricing; that is the risk behind the de-rating [Likely]. FCF conversion has fallen from 296.8% to 172.9% as deferred-revenue tailwinds fade [Certain]. Momentum is poor: -27.7% over 12 months, -43.5pp vs SPY, and the 50-day is below the 200-day [Certain]. A new AEC leader adds execution risk [Guessing]. The portfolio already owns AI-disruption software risk via INTU and GDDY [Certain].

## Bull case
This is a high-return franchise: 92.5% gross margin, 28.1% operating margin (+8.0pp over 5y), 57.6% ROIC and a 36.4% FCF margin, with net cash and Piotroski 8 [Certain]. Every multiple is below its own 5-year minimum and 33-44% below peers (P/E 30.5x vs 47.6x minimum; P/FCF 17.3x vs 22.2x), at a 5.78% FCF yield [Certain]. DWG format dominance, embedded workflows and the API ecosystem create real switching costs [Likely]. Q2 beat on revenue and EPS, so the de-rating reflects guidance, not demand [Likely]. Buybacks (-1.62% shares YoY) compound per-share value [Certain]. Agentic AI across Forma/Fusion/Flow and partnerships like Eaton's Workbench 360 could make AI a moat extender rather than a threat [Guessing]. If P/FCF merely returns to its 5y minimum, the stock re-rates materially [Likely].

## Decision
```json
{
  "ticker": "ADSK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A 92%-gross-margin, net-cash design-software franchise trades below its own 5-year multiple floor, but the mechanical fair value (base 219.04) sits below the price and guidance is resetting growth, so the discount looks earned rather than mispriced.",
  "rationale": "Quality is excellent and multiples are historically cheap, but the cash-flow fair value gives little upside (bull +10.5%, base -6.8%), the price still implies 20.6% growth after a guide-down, and AI-disruption risk would stack on INTU and GDDY. Good but not compelling: conviction 3, so AVOID and keep cash.",
  "price_at_decision": 235.05,
  "price_date": "2026-10-07",
  "research_note": "research/ADSK/2026-10-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 23%, the FY2025 level, showing the margin-expansion trend has broken (thesis weaker; stays AVOID).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 23}},
    {"text": "TTM ROIC falls below 40%, below the FY2022-FY2025 range, indicating capital-return erosion from AI competition.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "TTM gross margin falls below 90%, breaking five fiscal years above that level and signalling pricing pressure from AI-native rivals.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 90}},
    {"text": "Reconsider for BUY if next results (est. Nov 24, 2026) beat AND guidance is raised rather than cut, with TTM operating margin above the current 28.1%.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 28.1}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 300, "basis": "AI products (Forma/Fusion/Flow) defend seat pricing and P/FCF recovers to its 5y minimum of 22.2x from 17.3x [RA], above the mechanical bull 259.84 because the 5.78% FCF yield [ST] and buybacks support a floor re-rating."},
    "base": {"probability": 0.5, "target_price_12m": 225, "basis": "Guidance reset (Barrons 2026-08-28 headline) means growth falls short of the 20.6% the reverse DCF implies, so the price drifts toward the mechanical base fair value of 219.04 [fact-sheet Fair value], cushioned by buybacks."},
    "bear": {"probability": 0.25, "target_price_12m": 165, "basis": "AI-native competition the 10-K flags erodes growth and the market re-anchors on the DCF (base 144.84) rather than EV/Revenue, taking the price below the 6-month low of 185.50 [HI] toward the blended bear 125.15 [fact-sheet Fair value]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

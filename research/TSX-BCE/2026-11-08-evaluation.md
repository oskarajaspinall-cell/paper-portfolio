# Evaluation: BCE Inc. (TSX:BCE) — 2026-11-08
## Bear case
The balance sheet is the problem. Net debt/EBITDA has risen every year from 3.53x to 4.67x and Altman Z is 0.75 [Certain]. The **Direction change** line shows FCF margin down 6.1pp in 12 months (16.2% -> 10.1%) while the 5-year view reads flat [Certain]. The likeliest causes are lower operating margin (21.7% vs 22.7% a year earlier) and continued network spend [Likely]. That decline undercuts the thesis because FCF has to fund the dividend and pay down debt [Likely]. ROIC fell 1.9pp to 6.1%, thin for a capital-heavy network [Certain]. Shares rose 0.91% YoY, so holders are being diluted, not paid through buybacks [Certain]. The 2.45bn CAD tower stake sale cuts debt by giving away future tower cash flow [Likely]. P/FCF of 11.3x is above the peer median of 8.7x, so the stock is not cheap on cash [Certain]. The DCF fair value is built on the older, higher FCF base [Likely].
## Bull case
On most measures the stock is priced for decline. EV/EBITDA of 7.6x and P/B of 1.2x are below their 5y minimums. P/E of 11.9x compares with a 5y median of 22.1x [Certain]. The reverse DCF implies revenue shrinking 9.7% in year one, which is too harsh for a subscription oligopoly [Likely]. Q3 revenue and adjusted EBITDA grew, wireless retention improved, and 2026 guidance and the 3.5x leverage target were reaffirmed [Likely]. The tower sale gives a dated path to deleveraging [Likely]. Gross margin has risen to 44.9% from 43.0% [Certain]. The FCF yield is 8.85% [Certain]. Even the mechanical bear fair value of 54.76 CAD sits well above the 30.57 close [Certain]. If FCF margin recovers to its 13.5% FY2025 level, the stock could re-rate sharply [Guessing].
## Decision
```json
{
  "ticker": "TSX:BCE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "BCE is statistically cheap, but rising leverage, a sharp 12-month fall in FCF margin and falling ROIC mean the cheapness may be a value trap until deleveraging and cash flow recovery are visible.",
  "rationale": "Valuation is undemanding, but the thesis depends on FCF and deleveraging, and both are moving the wrong way: net debt/EBITDA is rising, Altman Z is low, the FCF margin fell sharply and dilution continues. That is good-but-not-compelling, not conviction 4. A lower price would not fix it; proof of deleveraging and an FCF recovery would.",
  "price_at_decision": 30.57,
  "price_date": "2026-11-06",
  "research_note": "research/TSX-BCE/2026-11-08.md",
  "triggers": [
    {"text": "Net debt/EBITDA (statistics) falls below 3.95x, its FY2023 level, showing the tower proceeds and cash flow are really deleveraging the business.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 3.95}},
    {"text": "TTM FCF margin recovers above 13.5% (FY2025 level), showing the 12-month fall was temporary.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 13.5}},
    {"text": "TTM ROIC recovers above 7.7% (FY2025 level) with operating margin holding near 22%.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 7.7}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 48.64, "basis": "Tower proceeds and the reaffirmed 3.5x leverage target [OV transcript] lift EV/EBITDA from 7.6x back toward its 5y median of 9.9x [RA], matching the mechanical EV/EBITDA base fair value of 48.64 rather than the DCF, which uses the older, higher FCF base."},
    "base": {"probability": 0.5, "target_price_12m": 33.92, "basis": "FCF margin stays near 10.1% [CF-T,IS-T] while leverage eases only slowly, so EV/EBITDA moves only partly back toward its 5y minimum of 8.3x [RA], in line with the EV/EBITDA bear fair value of 33.92 and well below the blended range because the DCF overstates FCF."},
    "bear": {"probability": 0.3, "target_price_12m": 26.66, "basis": "Net debt/EBITDA keeps rising above 4.67x [BS,IS] and FCF stays depressed, pressuring dividend sustainability [note section 6], and the price retests its 52-week low of 26.66 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below every mechanical fair value (bear 54.76). The obstacles are rising leverage, a falling FCF margin and ROIC, and an Altman Z of 0.75, so a lower price would not change the decision; evidence of deleveraging and a cash-flow recovery would.",
  "replaces": null,
  "replacement_reason": null
}
```

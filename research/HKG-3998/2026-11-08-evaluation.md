# Evaluation: Bosideng International Holdings Limited (HKG:3998) — 2026-11-08
## Bear case
Bosideng is a single-category, single-country, weather-exposed brand: a warm winter or Anta/Li Ning outerwear push hits volume with little cushion [Likely]. Gross margin has slipped from 60.1% to 57.2% over five years; profit growth is cost control, not pricing power [Certain]. The Direction change lines matter: ROCE (28.5%) sits 5.8pp below its 34.3% 2-year high and FCF margin (20.0%) 9.2pp below its 29.2% high. Both reflect FY2024's working-capital release (220.5% conversion) unwinding rather than falling profitability, since ROCE is flat year on year and FCF margin rose 7.8pp; neither threatens the thesis yet, but FCF is lumpy and inventory-sensitive [Likely]. The 50-day average is below the 200-day, Piotroski F is 5 and shares rose 1.14% [Certain]. H1 results on Nov 27, 2026 are a binary read on the season [Likely]. Country risk is context only: CNY steady and HKD pegged (macro overlay) [Certain].
## Bull case
Returns are exceptional and still rising: ROIC 81.2% TTM (53.9% a year earlier), operating margin 19.9% from 16.1% in FY2022, net margin 14.6% [Certain]. Net cash (net debt/EBITDA -2.24x) and FCF conversion of 137.2% fund the business internally [Certain]. Yet EV/EBITDA (4.9x) and EV/Sales (1.2x) are below their 5y minima, P/FCF 8.4x is far under the 13.6x peer median and the FCF yield is 11.92% [Certain]. The reverse DCF prices a -12.9% year-1 revenue fall that reported margins and cash flow do not show [Certain]; even the mechanical bear fair value of 5.02 sits above the 4.49 close [Certain]. Beta 0.53 and Altman Z 5.25 limit downside from leverage or market swings [Certain]. The market is pricing a demand reset that has not appeared; a normal winter season should narrow the gap [Likely].
## Decision
```json
{
  "ticker": "HKG:3998",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "China's leading down-jacket brand, with 81.2% ROIC, net cash and an 11.92% FCF yield, trades below its own 5-year minimum EV/EBITDA and EV/Sales, where the price implies a -12.9% revenue decline its margins and cash flow do not show.",
  "rationale": "Thesis intact: returns rising, net cash, cash conversion recovered, valuation below its own 5y floor. Direction-change lines reflect a FY2024 working-capital peak, not deterioration. Weather, competition and slipping gross margin cap conviction at 4; the position already sits at its volatility-scaled size, and the binary H1 print argues against adding before Nov 27.",
  "price_at_decision": 4.49,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-3998/2026-11-08.md",
  "triggers": [
    {"text": "TTM gross margin falls below 55%, under the five-year low of 57.2%, signalling loss of brand pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}},
    {"text": "TTM net margin falls below 10%, reversing the five-year rise to 14.6% and indicating the brand premium has eroded.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 40%, a reversion toward FY2022 levels that undercuts the moat thesis.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "TTM FCF margin falls below the FY2025 five-year low of 12.2%, signalling inventory or working-capital stress from a demand down-cycle.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12.2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 7.77, "basis": "A normal winter confirms ROIC 81.2% and operating margin 19.9% [RA,IS] and the price closes the reverse-DCF gap (-12.9% implied revenue) to the blended base fair value of 7.77 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 5.57, "basis": "Fundamentals hold flat and EV/EBITDA recovers only toward its 5y minimum 5.6x [RA], matching the EV/EBITDA base value of 5.57; set below the DCF base of 8.87 because a China-discounted multiple may persist."},
    "bear": {"probability": 0.3, "target_price_12m": 3.55, "basis": "A warm winter or Anta/Li Ning competition (note section 2) weakens H1 results and gross margin keeps sliding from 57.2% [IS]; the price revisits its 52-week low of 3.55 [HI], below the mechanical bear of 5.02 because that value assumes margins hold."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the holding is already conviction 4 and at its size; the default anchor (base 7.77 x 0.8) is above the current price, and adding should wait for the H1 results read rather than a lower price.",
  "replaces": null,
  "replacement_reason": null
}
```

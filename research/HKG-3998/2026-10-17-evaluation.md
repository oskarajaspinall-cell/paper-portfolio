# Evaluation: Bosideng International Holdings Limited (HKG:3998) — 2026-10-17
## Bear case
Bosideng is a single-category, single-country, weather-dependent apparel brand [Certain]. Gross margin has slipped from 60.1% to 57.2% over five years, so the operating-margin gain is cost control, not pricing power, and that lever runs out [Likely]. Anta and Li Ning are pushing into outerwear while Moncler and Uniqlo squeeze the premium and value ends [Likely]. Against those peers it is already dearer on EV/EBITDA, EV/Sales and P/B, so "cheap versus own history" may be a structural de-rating of China consumer names [Likely]. The fact sheet shows no revenue-growth figure, so the claim that the reverse-DCF decline (-13.0%) is too pessimistic rests on margins, not demonstrated top-line momentum [Certain]. Relative strength versus SPY is negative over 3, 6 and 12 months [Certain]. It would be the portfolio's third China-exposed holding, concentrating policy and consumer risk [Certain]. A mild winter before the Nov 27, 2026 results could reset earnings [Guessing].

## Bull case
Returns on capital have compounded: ROIC 81.2% TTM from 34.3% in FY2022, ROE 22.8%, operating margin 19.9% from 16.1% [Certain]. Cash is real: FCF conversion 137.2% of net income, FCF yield 12.15%, and net cash at -2.24x EBITDA [Certain]. Yet EV/EBITDA (4.7x) and EV/Sales (1.2x) sit below their five-year minimums and P/E is in the bottom eighth of its range [Certain]. The price implies a -13.0% year-1 revenue decline, a demand collapse nothing in the reported margins or cash flow shows [Likely]. Even the mechanical bear fair value (HKD 4.94) is above the HKD 4.41 close; base is HKD 7.62 [Certain]. Beta 0.57 and Altman Z 5.25 make it a defensive, low-correlation addition, and higher ROIC than peers justifies its peer premium on EV multiples [Likely]. Decades of brand incumbency in down jackets give point-of-purchase recall that newer entrants lack [Likely].

## Decision
```json
{
  "ticker": "HKG:3998",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "China's leading down-jacket brand, with 81.2% ROIC, net cash and a 12.15% FCF yield, trades below its own 5-year minimum EV/EBITDA and EV/Sales, where the price implies a -13.0% revenue decline its margins and cash flow do not show.",
  "rationale": "Quality is rising, the balance sheet is net cash, and even the mechanical bear fair value sits above the price. Single-category weather risk, falling gross margin and added China concentration keep conviction at 4, not 5; standard volatility-scaled core size. Consumer Discretionary stays under the sector cap and holdings well below 15.",
  "price_at_decision": 4.41,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-3998/2026-10-17.md",
  "triggers": [
    {"text": "TTM gross margin falls below 55%, under the five-year low of 57.2%, signalling loss of brand pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}},
    {"text": "TTM net margin falls below 10%, reversing the five-year rise to 14.6% and indicating the brand premium has eroded.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 40%, a reversion toward FY2022 levels that undercuts the moat thesis.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "TTM FCF margin falls below the FY2025 five-year low of 12.2%, signalling inventory or working-capital stress from a demand down-cycle.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12.2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 7.62, "basis": "Margins and FCF hold through the winter season and the stock reaches the fact sheet's blended base fair value of HKD 7.62 [IS,CF,RA], with EV/EBITDA back toward its 5y median 6.8x [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 5.56, "basis": "EV/EBITDA re-rates only to around its 5y minimum 5.6x on TTM EBITDA, the EV/EBITDA base value HKD 5.56 [RA,IS]; set below the DCF base 8.65 because the fact sheet shows no revenue-growth figure to support DCF growth and China consumer names trade at a structural discount to own history."},
    "bear": {"probability": 0.25, "target_price_12m": 3.55, "basis": "A mild winter or Anta/Li Ning outerwear competition cuts the H1 result and the stock revisits its 52-week low of 3.55 [HI], with P/E below its 5y minimum 10.3x [RA]; below the mechanical bear 4.94 because that assumes margins hold."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

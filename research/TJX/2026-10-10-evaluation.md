# Evaluation: The TJX Companies, Inc. (TJX) — 2026-10-10
## Bear case
Quality is not the issue; price is. At 25.7x P/E, 18.1x EV/EBITDA and a 3.85% FCF yield, TJX trades at a premium to off-price peers on every multiple [Certain] (fact sheet [RA]). The reverse DCF needs 17.0% year-1 revenue growth, well above the high-single-digit comps the business delivers [Certain]/[Likely], and the base fair value of $98.57 is 29% below the close [Certain]. Q2 gross margin got help from tariff-cost favourability that management says partly laps out in the back half, and Marmaxx, the largest division, lagged on execution [Likely] (Q2 transcript). Margins at five-year highs leave more room to fall than to rise [Guessing]. The stock is below its 200-day average with -30.4pp relative strength vs SPY over 6 months [Certain], so the market is still repricing consumer risk ahead of the Nov 18 print [Likely].
## Bull case
This is a best-in-class compounder: ROIC 30.1%, ROCE 31.9%, operating margin 12.2% and FCF margin 9.4%, all rising over five years, with net debt/EBITDA down to 0.93x [Certain] (fact sheet [RA], [IS]). FCF conversion of 96.9% funds buybacks (shares -1.10% YoY) and the dividend [Certain]. P/E sits at the 16th percentile and P/FCF at the 2nd percentile of TJX's own five-year range [Certain], so the multiple has de-rated even as returns improved. The EV/EBITDA fair value of $136.02 is close to the price [Certain], suggesting the DCF's growth caps understate a high-ROIC compounder [Guessing]. Comps rose 4% with full-year margin and EPS guidance raised [Certain] (Q2 transcript); if Marmaxx execution is fixed, the multiple can re-rate toward its 27.1x median [Likely].
## Decision
```json
{
  "ticker": "TJX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "TJX is a high-and-rising-ROIC off-price compounder, but at 25.7x P/E and a 3.85% FCF yield, with a price implying 17.0% year-1 growth and a tariff margin tailwind lapping, the valuation leaves no margin of safety.",
  "rationale": "Excellent business, but cheap only against its own rich history, not in absolute terms: base fair value $98.57 sits 29% below the price, peers are cheaper, and near-term margin risk (tariff lap, Marmaxx) precedes the Nov 18 print. Good but not compelling is an AVOID; cash is acceptable.",
  "price_at_decision": 138.76,
  "price_date": "2026-10-09",
  "research_note": "research/TJX/2026-10-10.md",
  "triggers": [
    {"text": "TTM gross margin falls below 29%, giving back the merchandise/tariff gains behind the FY2026 31.0% level (would weaken the thesis further).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 29}},
    {"text": "TTM ROIC falls below 28%, under the FY2023 five-year low of 28.3%, signalling the off-price buying-scale advantage is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 28}},
    {"text": "TTM operating margin falls below 10.7%, the FY2024 level, reversing most of the five-year expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10.7}},
    {"text": "TTM FCF margin falls below 5.3%, the FY2023 level, showing the cash-conversion step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5.3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 160.0, "basis": "Marmaxx execution fixed and margins hold near TTM 12.2% operating margin [IS], so P/E re-rates from 25.7x toward the 5y median 27.1x and above on higher earnings [RA], short of the 170.00 52-week high [HI]."},
    "base": {"probability": 0.5, "target_price_12m": 140.0, "basis": "Multiples stay near the EV/EBITDA 5y median 18.1x [RA] with modest earnings growth, consistent with the EV/EBITDA fair value 136.02 (fact sheet fair value), offsetting the DCF base 79.84."},
    "bear": {"probability": 0.25, "target_price_12m": 110.0, "basis": "Tariff-cost tailwind laps and Marmaxx stays weak (Q2 transcript, https://stockanalysis.com/stocks/tjx/transcripts/562422-q2-2027/), earnings slip and P/E holds near its 5y min 24.8x [RA], moving toward the blended base fair value 98.57."}
  },
  "entry_price": 78.86,
  "entry_basis": "valuation file: base 98.57 x 0.8 (20% margin of safety).",
  "replaces": null,
  "replacement_reason": null
}
```

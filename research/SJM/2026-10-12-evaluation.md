# Evaluation: The J. M. Smucker Company (SJM) — 2026-10-12
## Bear case
The cheapness rests on a TTM FCF margin of 17.3% that sits far above every fiscal year in five years (7.9%-12.8%) [Certain]; part of it is likely working-capital release as coffee costs ease, not a new run-rate [Guessing]. On FY2026's 12.8% margin the 12.4% FCF yield shrinks sharply [Likely]. Sales are guided to decline 1%-2% this fiscal year [Certain], Sweet Baked Snacks (Hostess) sales fell 7% last quarter and the charges behind ROE of -17.9% (FY25) point to a value-destroying acquisition [Likely]. Leverage is still 3.05x net debt/EBITDA with Altman Z at 1.54 [Certain], while the 10y yield rose 68bp in three months, raising refinancing cost (macro overlay) [Certain]. Walmart is 34% of net sales [Certain]. EV/EBITDA of 8.7x is +9% versus peers [Certain], and the stock has already rallied 29.6% in six months [Certain].

## Bull case
Management raised FY2027 guidance after a Q1 that "exceeded expectations", hit leverage targets early and raised the dividend with buybacks possible [Likely]. Net debt/EBITDA has fallen from 4.53x to 3.05x [Certain], Piotroski F is 8 and ROIC rose from 7.0% to 10.4% over five fiscal years [Certain]. Gross (38.0%) and operating (18.6%) margins are at the top of their five-year range [Certain]. P/FCF of 8.1x and EV/EBITDA of 8.7x are both below their five-year minimums [Certain], and the reverse DCF implies a -12.9% revenue decline against guidance of -1% to -2% [Certain]. Uncrustables, coffee and pet snacks are driving volume [Likely]. Low beta (0.27) makes it a defensive compounder of cash if the FCF step-up proves durable [Guessing].

## Decision
```json
{
  "ticker": "SJM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraging branded-food company trades below its own 5-year EV/EBITDA and P/FCF minimums, but the cheapness depends on a TTM FCF margin well above its history while sales shrink and leverage stays near 3x.",
  "rationale": "Cash multiples look cheap, but normalising FCF to FY2026's 12.8% margin and pricing EV/EBITDA near peers leaves a probability-weighted 12-month return of only mid-single digits. Add declining sales, Hostess impairments, 3.05x leverage, Altman Z 1.54 and 34% Walmart concentration, and this is good but not compelling. Conviction 3, no position.",
  "price_at_decision": 119.83,
  "price_date": "2026-10-09",
  "research_note": "research/SJM/2026-10-12.md",
  "triggers": [
    {"text": "TTM FCF margin falls below 12%, under the FY2026 level of 12.8%, showing the TTM 17.3% step-up was working capital, not a durable run-rate.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "TTM gross margin falls below 34%, the five-year low (FY2022 34.0%), signalling lost pricing power against coffee costs and Walmart.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 34}},
    {"text": "TTM ROIC falls below 7%, back to the FY2022 five-year low, reversing the returns improvement.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 7}},
    {"text": "Net debt/EBITDA (ratios page) rises back above 4x instead of continuing to fall from 3.05x TTM, showing deleveraging has stalled."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 172.8, "basis": "Durable FCF and continued deleveraging re-rate EV/EBITDA from 8.7x to its 5y median 11.2x [RA] on TTM EBITDA with net debt held at 3.05x EBITDA [RA,ST]; still below the mechanical base fair value 217.63 because that DCF capitalises a TTM 17.3% FCF margin far above the 5y range [CF,IS]."},
    "base": {"probability": 0.45, "target_price_12m": 132.5, "basis": "Raised FY2027 guidance (sales -1% to -2%, Q1 2027 release) holds and EV/EBITDA recovers only to its 5y minimum 9.3x [RA] on TTM EBITDA and 3.05x net debt/EBITDA [RA,ST], given it already trades +9% vs the 8.0x peer median."},
    "bear": {"probability": 0.35, "target_price_12m": 91.9, "basis": "FCF margin normalises from 17.3% TTM to the FY2026 12.8% [CF,IS] at the 8.4x peer-median P/FCF [P:GIS..HRL], with Sweet Baked Snacks weakness (Barron's 2026-09-04) persisting; probability raised 0.05 from bull for the macro overlay's small bear tilt (rising 10y/real yields on a 3.05x-levered balance sheet, research/SJM/2026-10-12-macro.md)."}
  },
  "valuation_overrides": [
    {"method": "dcf", "scenario": "base", "field": "margin", "value": 0.128, "reason": "TTM FCF margin of 17.3% is above every fiscal year in the 5y record (7.9%-12.8%) [CF,IS]; the FY2026 12.8% level is the highest sustained annual figure and a fairer base run-rate."}
  ],
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: the stock already trades below its 5y minimum P/FCF and EV/EBITDA [RA]; what is missing is evidence that the 17.3% TTM FCF margin is durable and that net debt/EBITDA keeps falling from 3.05x, so a lower price on the same evidence would not lift conviction to 4. The mechanical base fair value (217.63 x 0.8 = 174.10) is above the price and not usable as an anchor.",
  "replaces": null,
  "replacement_reason": null
}
```

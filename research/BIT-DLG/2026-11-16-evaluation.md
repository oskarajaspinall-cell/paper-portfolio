# Evaluation: De'Longhi S.p.A. (BIT:DLG) — 2026-11-16
## Bear case
The price already discounts the recovery. P/E 19.9x and P/B 3.3x sit above their entire 5y ranges, and the mechanical base fair value of 44.19 EUR is below the 47.40 close [Certain]. The reverse DCF needs 5.9% year-1 revenue growth while guidance is only mid-single-digit [Likely]. The stock is extended (+25.0% vs its 200-day, RSI 75.1): if Professional growth slows, a de-rating back toward the 5y median P/E of 17.2x would erase the year's gains [Likely]. The Direction change line matters: ROIC fell over five fiscal years (23.1% to 19.6%), with a 12.6% FY2022 trough that shows how cyclical and tariff-exposed small appliances are [Certain]. Beta 1.51 amplifies any consumer slowdown [Certain]. Insiders hold 70.72%, so minorities have little say over use of the net cash [Certain]. Regional mix is unverified, so tariff/FX exposure is unquantified [Certain].
## Bull case
A high-return, net-cash compounder that is working. ROIC TTM 20.9% and ROCE 18.7% are at their 2-year highs, rising over the last 12 months (17.8% to 20.9%), so the 5-year ROIC decline is the FY2022 trough unwinding, not erosion [Certain]. Gross margin rose to 45.0% on Professional mix [Likely]. Cash conversion is exceptional: FCF margin 13.4%, FCF/NI 149.6%, FCF yield 7.52%, P/FCF 13.3x near the bottom of its 5y range [Certain]. Q3 lifted adjusted EBITDA guidance again after raises earlier in the year (https://stockanalysis.com/quote/bit/DLG/transcripts/671366-q3-2026/) [Likely]. Versus peers P/E and EV/EBITDA sit at discounts (-32%, -19%) [Certain]. Momentum is strong: +35.4% over 12 months, +25.0pp relative strength vs SPY [Certain]. Espresso-machine brand leadership is a real, if narrow, moat [Likely].
## Decision
```json
{
  "ticker": "BIT:DLG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Python lists nothing falling over 1y or 3y: TTM ROIC is rising (17.8% to 20.9%) at its 2-year high [RA-T]; the 5y fiscal-year ROIC fall reflects the FY2022 trough of 12.6% and the recovery since, with gross margin up on Professional mix (https://stockanalysis.com/quote/bit/DLG/transcripts/671366-q3-2026/).", "moat": "narrow", "key_risk": "medium", "key_risk_text": "De-rating: P/E 19.9x is above its 5y max with the price +25.0% over its 200-day; a slowdown in Professional growth or a consumer/tariff hit to Household would compress the multiple.", "veto": null},
  "thesis": "A net-cash, high-ROIC appliance leader whose Professional coffee mix is lifting returns, but whose price already sits above the base fair value and above its own 5y P/E range.",
  "rationale": "Quality, balance sheet and trend are strong, but the price is above the mechanical base fair value and P/E is above its 5y range, so the expected 12-month value offers little upside. Good but not compelling at 47.40; the scorecard sets the conviction.",
  "price_at_decision": 47.40,
  "price_date": "2026-11-13",
  "research_note": "research/BIT-DLG/2026-11-16.md",
  "triggers": [
    {"text": "ROIC TTM falls below 15% (returns no longer above the recovery level)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "Operating margin TTM falls below 11% (mix gains reversing)", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11}},
    {"text": "FCF margin TTM falls below 8% (cash conversion breaks)", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "Net debt/EBITDA rises above 1.5x (net cash spent on leveraged M&A)"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 54.59, "basis": "Mechanical bull fair value 54.59 [IS,BS,CF,RA,ST,HI]: Professional growth and raised EBITDA guidance (https://stockanalysis.com/quote/bit/DLG/transcripts/671366-q3-2026/) sustain the TTM ROIC of 20.9% [RA-T]."},
    "base": {"probability": 0.5, "target_price_12m": 44.7, "basis": "EV/EBITDA base fair value 44.70, near the blended base 44.19 [fact sheet Fair value]: EV/EBITDA holds near its 5y median 10.1x [RA] as margins stay at 13.4% [IS-T]."},
    "bear": {"probability": 0.25, "target_price_12m": 39.38, "basis": "EV/EBITDA bear fair value 39.38 [fact sheet Fair value], a de-rating toward the 5y range as growth slows; the DCF bear of 6.87 is not used because the net-cash balance sheet and FCF yield 7.52% [ST] make it implausible over 12 months."}
  },
  "entry_price": 35.35,
  "entry_basis": "valuation file: base 44.19 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

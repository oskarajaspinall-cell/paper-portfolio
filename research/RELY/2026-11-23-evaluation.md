# Evaluation: Remitly Global (RELY) — 2026-11-23
## Bear case
The stock fell from the 28.00 high on 2026-11-04 to 19.83 straight after a beat-and-raise, and the note found no sourced cause [Certain]; an unexplained sell-off after good news can mean the market sees a slowdown we cannot [Guessing]. It sits below its 200-day average with 3-month relative strength of -10.2pp, so no trend support [Certain]. The TTM ROIC of 51.9% is early operating leverage, not a steady state [Likely]. Remittance volumes hinge on US immigration and remittance-tax policy, which the filing names as a risk [Likely]; the AUSTRAC AML/CTF investigation is unquantified [Certain]. Digital rivals compete on price, so pricing power is limited [Guessing]. Shares still grew 2.75% YoY despite buybacks [Certain]. It trades at a premium to WU, PYPL, FOUR and EEFT on every multiple, and fair value rests on EV/Revenue alone, with a bear value of 15.83 [Certain].
## Bull case
Every quality metric is rising on both the 5-year and the rolling 12-month view: operating margin 13.0% from 2.2% a year earlier, FCF margin 20.8% from 11.1%, gross margin up every year to 62.5% [Certain]. Q3 delivered send volume up 25%, revenue up 22%, raised FY26 guidance and an early FY2027 view of high-teens growth (headline, [OV]) [Likely]. The balance sheet is net cash (net debt/EBITDA -2.45x), Altman Z 7.69 [Certain]. Yet P/FCF of 10.8x sits at 2% of its 5-year range (median 42.3x) and the FCF yield is 9.30% [Certain], pricing a fade the guidance does not show [Likely]. The buyback authorisation rose to $500.0 million [company-reported] [Certain]. Usage is non-discretionary and repeat, and the disbursement network is hard to replicate quickly [Likely]. Base fair value 31.39 is well above the price [Certain].
## Decision
```json
{
  "ticker": "RELY",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "No quality metric is falling: ROIC, operating margin and FCF margin all rise on the 1-year and 3-year trailing view [RA-T, IS-T, CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "US immigration or remittance-tax policy cuts send volumes in the main US corridor, or the AUSTRAC investigation ends in a material penalty; the unexplained post-results fall may be pricing such a slowdown.",
    "veto": null
  },
  "thesis": "A net-cash, newly profitable digital remitter with rising margins and a 9.30% FCF yield trades at the bottom of its own P/FCF range, pricing a fade its raised guidance does not show.",
  "rationale": "Fundamentals improved further since the BUY: margins and returns all rising, guidance raised, net cash. The fall since the high has no sourced cause and does not break the thesis. The position is at its target size, so HOLD; the top-up rule covers drift.",
  "price_at_decision": 19.83,
  "price_date": "2026-11-20",
  "research_note": "research/RELY/2026-11-23.md",
  "triggers": [
    {"text": "TTM operating margin falls below 8%, reversing most of the step-up from 2.2% a year earlier to 13.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}},
    {"text": "TTM ROIC falls below 20%, showing the returns step-up was not durable.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 12%, back near the 11.1% of a year earlier.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "A regulatory outcome (AUSTRAC or US remittance rules) restricts a major corridor or imposes a material penalty, disclosed in a filing."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 33.95, "basis": "High-teens FY2027 growth holds and EV/Sales re-rates toward its 5y median 3.3x [RA], matching the mechanical bull fair value 33.95."},
    "base": {"probability": 0.45, "target_price_12m": 28.00, "basis": "Margins keep rising as guided and the price recovers to the 2026-11-04 high of 28.00 [HI], below the base fair value 31.39 because EV/Revenue is the only method that ran."},
    "bear": {"probability": 0.30, "target_price_12m": 15.83, "basis": "Remittance policy or pricing competition slows send volumes and EV/Sales stays near its 5y low 1.5x [RA], the mechanical bear fair value 15.83."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is already 4 at today's price; price is not the obstacle, so no separate entry level applies to this holding.",
  "replaces": null,
  "replacement_reason": null
}
```

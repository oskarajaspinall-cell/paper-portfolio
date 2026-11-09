# Evaluation: F.N.B. Corporation (FNB) — 2026-11-09
## Bear case
ROE is 9.0% TTM and has stayed between 7.5% and 8.7% for five fiscal years [Certain]. That is likely below its cost of equity, so the 0.9x P/B, already above its 5y max, is not a bargain [Likely]. The discount to peers (P/B 1.3x, P/E 13.1x) probably reflects lower returns rather than mispricing [Likely]. Non-interest expense grew 5.5% against revenue growth of 2.6% [company-reported], so operating leverage was negative in the quarter [Certain]. The macro overlay tilts toward the bear case (small): HY spreads are up 0.77pp in 3m and VIX is 28.18, which threatens provisions from a low 0.12% charge-off rate and the multiple [Likely]. The Direction change line (FCF margin down over 5 fiscal years, up from 35.0% to 41.0% over 12 months) is working-capital noise in bank cash flow, not a change in the thesis [Likely]. The fair value is flagged unreliable (3.6x method gap) [Certain].

## Bull case
Q3 brought record net interest income. NIM was 3.29%, loans grew 8.5% and deposits 8.9% annualized, and credit is clean (NPLs plus OREO 0.33%) [company-reported] [Certain]. Management guides to positive operating leverage for the year [Likely]. P/E 10.8x sits near its 5y median of 10.6x and well below peers, the reverse DCF implies -5.2% revenue growth (undemanding), and buybacks cut shares 1.13% YoY on top of the $0.13 quarterly dividend [Certain]. If ROE keeps edging up and spreads retrace, the stock can rerate toward the bull fair value of 20.99 [Guessing]. Still, this is a steady compounder, not a mispriced one [Likely].

## Decision
```json
{
  "ticker": "FNB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years; FCF margin rose from 35.0% to 41.0% over 12 months [CF-T], and its 5-fiscal-year fall is bank working-capital noise. ROE (+0.6pp) and net margin (+0.8pp) are flat [RA,IS].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Credit-cycle turn: widening HY spreads (+0.77pp in 3m, macro overlay) push provisions up from a low 0.12% charge-off rate and compress a P/B already above its 5y max.",
    "veto": null
  },
  "thesis": "A steady regional bank earning a 9% ROE at a fair, not cheap, multiple of its own history; the discount to peers matches its lower returns.",
  "rationale": "ROE of 9.0% is below the quality bar, P/B sits above its 5y max, the fair value is unreliable with little upside, and the macro tilt is toward the bear case. Good but not compelling, so AVOID; cash is an acceptable outcome.",
  "price_at_decision": 17.90,
  "price_date": "2026-11-06",
  "research_note": "research/FNB/2026-11-09.md",
  "triggers": [
    {"text": "ROE TTM rises above 12%, i.e. returns move toward peers (statistics page)", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 12}},
    {"text": "ROE TTM falls below 7.5%, i.e. earnings power deteriorates (statistics page)", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 7.5}},
    {"text": "Net margin TTM falls below 30%, i.e. spread or credit pressure (statistics page)", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 30}},
    {"text": "Non-performing loans plus OREO above 0.60% of loans in a quarterly 10-Q (sec.gov)"}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 20.99, "basis": "Spreads retrace, NIM rises above 3.29% [company-reported] and ROE keeps edging up, lifting the price to the bull fair value of 20.99 [IS,BS,CF,RA,ST]."},
    "base": {"probability": 0.5, "target_price_12m": 18.6, "basis": "P/E holds near its 5y median of 10.6x [RA], with modest EPS growth from buybacks (shares down 1.13% YoY [ST]) and mid-single-digit balance-sheet growth (Q3 transcript); below the unreliable 19.47 base fair value, which weighs the FCFE method heavily."},
    "bear": {"probability": 0.3, "target_price_12m": 15.54, "basis": "Macro overlay tilt toward bear (small, research/FNB/2026-11-09-macro.md): wider credit spreads lift provisions and P/B falls back toward its 5y median of 0.8x [RA], close to the P/B + ROE base of 15.54; bear weight raised for the tilt."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: ROE of 9.0% [RA] is below the quality bar, so a lower price would not reach conviction 4 without returns improving (see the ROE > 12% trigger).",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: YTO Express Group Co.,Ltd. (SHA:600233) — 2026-11-09
## Bear case
Chinese express parcels are a price-taking network business: gross margin of 11.7% TTM and operating margin of 9.2% leave little cushion if the price war resumes [Likely]. The TTM rebound (ROIC 16.2% vs 12.0% a year earlier) follows a FY ROIC slide from 20.5% in FY2022 to 13.9% in FY2025, and the 3-year change is still flat, so it may be a cyclical pricing upswing rather than a new level [Likely]. Cash conversion is poor: FCF was negative in FY2024 and FY2025 and P/FCF of 25.2x is far above the peer median of 11.1x [Certain]. The mechanical base fair value of 14.52 sits below the 18.79 price, though flagged unreliable [Certain]. Net cash is shrinking (-1.19x to -0.24x) as capex absorbs earnings [Certain]. The Q3 result is not yet in the data [Certain]. China risk premium applies; macro weight is context only [Certain].
## Bull case
On earnings the stock is cheap: P/E of 10.5x is below its 5y minimum of 11.4x and EV/EBITDA of 6.1x sits near the bottom of its range [Certain]. The last year shows broad improvement with no Direction change flag: operating margin 9.2% vs 6.6%, FCF margin 3.2% vs -2.6%, ROIC at its 2-year high [Certain]. The balance sheet is net cash with Altman Z 4.32 and a slightly shrinking share count [Certain]. Returns stayed positive through the price war, implying a cost-efficient scale network [Likely]. The DCF base looks too harsh on volatile FCF; the EV/EBITDA base is 21.96 [Likely]. If pricing discipline holds, a re-rating toward the 5y median P/E of 13.0x is plausible [Guessing].
## Decision
```json
{
  "ticker": "SHA:600233",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "No metric is falling on the 1-year view: ROIC, ROCE, operating and FCF margin are all at their 2-year highs [RA-T, IS-T, CF-T]; the 3-year change is flat.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A renewed parcel price war compresses the thin margin back toward FY2025 levels, reversing the TTM return rebound.",
    "veto": null
  },
  "thesis": "A net-cash Chinese parcel network trading below its own 5-year minimum P/E with recovering returns, but its thin, price-war-exposed margins and weak cash conversion leave the cheapness unproven on cash.",
  "rationale": "Cheap on earnings and improving, but cash conversion is weak, the margin rebound is not yet proven through a cycle, and the mechanical base fair value sits below the price. Good but not compelling: conviction 3, so AVOID with an entry price.",
  "price_at_decision": 18.79,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-600233/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, back to the level of a year earlier, showing the return rebound was a pricing blip.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM operating margin falls below 7%, under the FY2024-FY2025 level of 7.1%, signalling the price war has resumed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 7}},
    {"text": "TTM FCF margin turns negative again, showing capex still absorbs all earnings.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Net debt/EBITDA on the ratios page moves above 0.0x, ending the net-cash balance sheet."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 23.77, "basis": "Pricing discipline holds and the market re-rates toward the 5y median P/E of 13.0x [RA], matching the fact sheet's bull fair value of 23.77."},
    "base": {"probability": 0.45, "target_price_12m": 19.86, "basis": "TTM earnings hold and P/E moves to the peer median of 11.1x [RA], between the DCF base of 10.80 and EV/EBITDA base of 21.96, since the blended base 14.52 is flagged unreliable."},
    "bear": {"probability": 0.30, "target_price_12m": 14.09, "basis": "Price war resumes and net margin reverts from 7.6% TTM to the FY2025 5.7% [IS] at an unchanged 10.5x P/E, near the 52-week low of 14.90 [HI]."}
  },
  "entry_price": 11.62,
  "entry_basis": "valuation file: base 14.52 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Gedeon Richter PLC (BUD:RICHTER) — 2026-11-15
## Bear case
The Q3 2026 results published on 2026-11-10 were not read, so the latest quarter is unreviewed [Certain]. FCF margin fell to 26.8% TTM from 29.3% a year earlier while operating margin rose, and the cause (working capital or capex) is not established [Guessing]. Revenue by country is [data unavailable]; a material Russia/CIS or other emerging-market exposure, and HUF translation against a USD portfolio, cannot be excluded, and the Q1 call cited FX headwinds that cut reported growth well below constant-currency growth [Likely]. The moat is a regional generics/specialty mix rather than one protected franchise [Likely]. The price is up 36.9% in 12 months and sits 9.9% above its 200-day average, with P/B at 92% of its 5y range: if growth slows, a de-rating toward the 5y median multiples could erase gains [Likely]. The mechanical bear fair value of 7,297.79 HUF shows how sensitive the DCF is [Certain].

## Bull case
Quality is high and improving on both the fiscal and rolling views: TTM ROIC 22.5% (17.4% a year earlier), operating margin 34.5% (28.7%), gross margin 67.8% from 55.4% in FY2021 [Certain]. The balance sheet is net cash (net debt/EBITDA -0.61x), Altman Z 6.64, and the share count is flat [Certain]. FCF conversion is 103.6% of net income, so profits are cash [Certain]. Yet the stock trades at 5.7x EV/EBITDA (23% of its 5y range, below the 6.4x median), 9.8x P/FCF (5y median 12.2x) and a 10.23% FCF yield, far below peers [Certain]. The reverse DCF implies -5.6% year-1 revenue growth while management guided high single-digit growth for 2026 [Likely]. The uptrend is healthy and not overextended, with relative strength vs SPY of +26.5pp over 12 months and a 0.31 beta [Certain].

## Decision
```json
{
  "ticker": "BUD:RICHTER",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only TTM FCF margin is falling (29.3% -> 26.8%, still above every fiscal year before FY2024 [CF-T,IS-T]); over the same 12 months operating margin rose 5.8pp and ROIC 5.1pp [IS-T,RA-T], and FCF conversion is still 103.6% of net income [CF,IS], so it is a cash-timing gap from a high base, not lost pricing or share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Unreviewed Q3 2026 results and unknown country/HUF exposure (note sections 1 and 6; macro overlay country_risk) could reveal a growth slowdown that de-rates a stock up 36.9% in 12 months.",
    "veto": null
  },
  "thesis": "A net-cash pharmaceutical franchise with ROIC and operating margin at their 2-year highs and a 10.23% FCF yield trades below its own 5-year median EV/EBITDA and P/FCF, but the value-blend upside is moderate and the latest quarter and country exposure are unverified.",
  "rationale": "Scorecard total 8 gives conviction 3: quality, direction and balance sheet are full marks, but the value-blend upside is only moderate, the moat narrow and the key risk medium (unread Q3, unknown country/HUF mix). Good but not compelling at this price, so AVOID; cash is acceptable.",
  "price_at_decision": 13540.00,
  "price_date": "2026-11-13",
  "research_note": "research/BUD-RICHTER/2026-11-15.md",
  "entry_price": 12680.00,
  "entry_basis": "Base fair value 18,321.90 x 0.8 is above the price, so it can't serve; instead the level where the scorecard's value-blend upside (+22% at 13,540) reaches its 30% band for a third valuation point, roughly at the 50-day average of 12,728.40 [ST,HI], on the same fundamentals.",
  "triggers": [
    {"text": "TTM ROIC falls below 16%, giving up the rise from 17.4% a year earlier to 22.5%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 16}},
    {"text": "TTM operating margin falls below 28%, under the 28.7% of a year earlier, showing the mix gains reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "TTM FCF margin falls below 20%, showing the cash gap is structural rather than timing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA rises above 1.5x (-0.61x now), signalling a large debt-funded acquisition.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 18321.90, "basis": "Rising ROIC and margins [RA-T,IS-T] close the gap to the mechanical base fair value of 18,321.90 HUF (DCF/EV-EBITDA blend), still below the bull of 21,387.39."},
    "base": {"probability": 0.5, "target_price_12m": 14574.46, "basis": "EV/EBITDA returns to its 5y median 6.4x [RA] on TTM EBITDA, the EV/EBITDA method's base of 14,574.46 HUF; the DCF base is set aside as too sensitive given the wide bear/base spread."},
    "bear": {"probability": 0.25, "target_price_12m": 11141.92, "basis": "Q3 or country/FX exposure shows slowing growth and the multiple de-rates to the EV/EBITDA bear of 11,141.92 HUF; the DCF bear of 7,297.79 is not used because net cash and ROIC 22.5% [RA] do not support that collapse."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: RELX PLC (LON:REL) — 2026-11-16
## Bear case
Generative AI is the live threat: if legal research and scientific content become cheaper to synthesise, RELX's pricing power erodes before the reported margins show it, and the multiple compresses further [Guessing]. The de-rating to below the 5y minimum P/E (24.6x vs 26.6x) says the market already doubts terminal value [Certain]. The shares are up 23.2% in 3 months and sit 19.9% above the 200-day average with RSI 65.0 [Certain]: much of the rebound from the 2,001.00 July low is done, so a growth slowdown would bring a de-rating back toward that trough [Likely]. Leverage rose from 2.23x to 2.64x net debt/EBITDA while buybacks continue [Certain]. There is no mechanical fair value (no GBP FX rate), so valuation rests on own-history multiples alone [Certain]. Exhibitions faced Middle East disruption [Likely]. No direction change is flagged; every rolling metric is flat or rising [Certain].

## Bull case
A compounding information franchise with rising returns on every horizon: ROIC 23.6% TTM vs 16.4% in FY2021, operating margin 31.7% vs 25.5%, both at or near their 2-year highs on a rolling basis [Certain]. FCF margin is 29.4% and FCF conversion 126.4%, so earnings are cash [Certain]. Underlying revenue growth improved to 7% for nine months with full-year guidance reaffirmed, and STM growth accelerated with AI-enabled products gaining use (https://stockanalysis.com/quote/lon/REL/transcripts/655652-q3-2026-tu/) [Likely]. Yet P/E and EV/EBITDA are below their 5y minimums and P/FCF is near its 5y low of 18.5x, a 5.36% FCF yield [Certain]. Proprietary data embedded in professional workflows makes AI a tool RELX deploys rather than a substitute [Likely]. Shares fall 2.63% a year via buybacks [Certain]. Beta 0.27 makes it defensive [Certain]. The trend has turned: price above both moving averages, 50-day 7.2% above the 200-day [Certain].

## Decision
```json
{
  "ticker": "LON:REL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Nothing is falling: ROIC, operating margin and FCF margin are flat or rising over the last year on the rolling table [RA-T, IS-T, CF-T].", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Generative AI substitutes for legal research and scientific content, eroding pricing power and de-rating the multiple, with the shares already extended above the 200-day average after a 23.2% 3-month rally.", "veto": null},
  "thesis": "A high-return, cash-generative information franchise with improving margins and growth trades below its own 5-year minimum P/E and EV/EBITDA because the market prices AI disruption.",
  "rationale": "Quality and direction are excellent, but after the 3-month rally the expected value offers little upside, no mechanical fair value exists, and AI disruption is an unresolved medium risk. The scorecard gives conviction 3: good but not compelling, so AVOID and wait for a lower entry.",
  "price_at_decision": 3069.00,
  "price_date": "2026-11-13",
  "research_note": "research/LON-REL/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 18% (23.6% now), reversing most of the five-year improvement.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "TTM operating margin falls below 28% (31.7% now), showing AI or competition is compressing profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "TTM FCF margin falls below 25% (29.4% now), showing cash generation is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "Net debt/EBITDA rises above 3.5x (2.64x TTM now), showing buybacks are outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 3930, "basis": "P/E re-rates to its 5y median 31.5x [RA] on TTM earnings as improving underlying growth and AI-enabled products ease disruption fears (Q3 transcript, OV)."},
    "base": {"probability": 0.5, "target_price_12m": 3318, "basis": "P/E recovers only to its 5y minimum 26.6x [RA] on TTM earnings: growth holds but the AI debate keeps the multiple at the low end; no mechanical fair value exists to reconcile (no GBP FX rate)."},
    "bear": {"probability": 0.25, "target_price_12m": 2001, "basis": "AI-disruption fears return and the shares revisit the 6-month low of 2,001.00 [HI] set in July, undoing the rally despite intact fundamentals."}
  },
  "entry_price": 2418,
  "entry_basis": "No mechanical fair value (no GBP FX rate), so anchored on the 2,418.00 swing low of 2026-10-01 [HI], before the rally, where the expected-value upside on these same scenarios would be large enough for conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Paycom Software (PAYC) — 2026-11-15
## Bear case
The price has already re-rated: up 84.5% in six months and 47.2% above the 200-day average, close to the overextended line, with base fair value only +5.0% above the close [Certain]. An extended price is exposed to a de-rating if growth slows; the reverse DCF already asks for 9.4% year-1 revenue growth [Certain]. Part of the TTM margin step-up (operating margin 33.9% vs 27.9% a year earlier) is cost-driven via lower headcount, not growth, and may not repeat [Likely]. The 5y FY ROIC was flat, so the TTM jump is one year of evidence, not a trend [Certain]. Buybacks (shares -12.61% YoY) are partly revolver-funded, with $750.0 million outstanding [company-reported], moving net debt / EBITDA from -0.44x to 0.75x [Certain]. Higher real yields pressure software multiples (macro overlay, context only) [Likely]. Piotroski F of 5 is middling [Certain].

## Bull case
A high-quality, cash-generative payroll franchise that is working: TTM ROIC 39.3%, operating margin 33.9%, FCF margin 30.1%, gross margin 88.4%, all at their 2-year highs and rising over 1 and 3 years [Certain]. Q3 results drove raised FY26 guidance [Likely]. Despite the run, valuation is low against its own history and peers: P/E 24.0x at 5% of its 5y range, EV/EBITDA 14.0x at 1% and 31% below peers, P/FCF 16.7x below its 5y minimum, FCF yield 5.98% [Certain]. Payroll switching costs and a single-database product support the returns [Likely]. Leverage stays modest at 0.75x and the share count is shrinking fast, compounding per-share value [Certain]. Higher short rates lift client-fund interest income [Likely]. Relative strength vs SPY is +38.0pp over 12 months [Certain].

## Decision
```json
{
  "ticker": "PAYC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds ROIC, operating margin and FCF margin all rising over 1 and 3 years (RA-T, IS-T, CF-T); nothing is falling.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "De-rating of an extended price (47.2% above the 200-day average) if the partly cost-driven margin step-up fades and growth slows below the 9.4% the reverse DCF implies.",
    "veto": null
  },
  "thesis": "A high-return, cash-generative payroll software franchise whose margins are stepping up while trading low in its own multiple history.",
  "rationale": "Quality and trend are strong, but base fair value sits barely above the close after a sharp re-rating, the margin step-up is one year old and partly cost-driven, and buybacks are now debt-funded. The scorecard gives conviction 3: good but not compelling, so AVOID (owner rule: high conviction only) and watch the entry price.",
  "price_at_decision": 248.86,
  "price_date": "2026-11-13",
  "research_note": "research/PAYC/2026-11-15.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 28%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "ROIC (TTM) falls below 30%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "FCF margin (TTM) falls below 20%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Net debt / EBITDA rises above 2.0x (debt-funded buybacks overreach).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 357.13, "basis": "Margin step-up holds and the multiple recovers toward its 5y median EV/EBITDA 22.8x [RA]; anchored on the DCF bull 357.13 rather than the blended 424.59, which leans on an EV/Revenue multiple well above today's."},
    "base": {"probability": 0.5, "target_price_12m": 261.42, "basis": "Mechanical base fair value 261.42 (DCF 67% + EV/Revenue 33%) with TTM margins sustained and growth near the reverse-DCF 9.4% [IS,CF,RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 170.86, "basis": "Cost-driven margin gains fade and the extended price de-rates; EV/Revenue bear 170.86 [RA], above the DCF bear 65.51, which assumes a collapse the rising quality trend does not support."}
  },
  "entry_price": 209.14,
  "entry_basis": "valuation file: base 261.42 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Remitly Global (RELY) — 2026-11-15
## Bear case
Profitability is new: operating margin was 2.2% a year ago and -3.0% in FY2024, so TTM ROIC of 45.5% is an early, unproven level, and net margin above operating margin hints at a non-recurring tax benefit [Likely]. The price is dearer than peers on EV/EBITDA (16.2x vs 6.6x) and P/FCF (12.2x vs 5.1x), so any slowdown toward the high-teens growth management flags for 2027 could de-rate it; the stock already fell from 28.00 after a beat-and-raise quarter, with 3-month momentum -12.0% [Likely]. Price competition from Wise, Western Union and banks is the durable threat [Likely]. AUSTRAC anti-money-laundering inquiries in Australia carry an inestimable loss [company-reported], and US immigration or remittance-tax policy is an unquantified exposure [Guessing]. Share count still rose 2.75% despite buybacks [Certain]. The fair value rests on EV/Revenue alone, so it is soft [Likely].
## Bull case
Every rolling-12-month metric is rising: operating margin 13.0%, FCF margin 20.8%, ROIC 45.5%, with no direction change [Certain]. Gross margin expanded from 48.3% to 62.5%, so scale is passing through without a price war [Likely]. Earnings are cash-backed (FCF conversion 108.5%) and the FCF yield is 8.18% at P/FCF in the bottom 5% of its 5y range [Certain]. Net cash (net debt/EBITDA -2.45x) and Altman Z 7.69 make the balance sheet strong [Certain]. Q3 2026 beat and the company raised FY2026 guidance, with send volume growing faster than revenue [Likely]. The board lifted the buyback authorisation to 500.0 million USD [company-reported]. Remittance demand is non-discretionary and the price sits above its 200-day average after a +84.8% year [Certain]. Base fair value of 31.39 sits well above the price [Certain].
## Decision
```json
{
  "ticker": "RELY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "No ROIC, operating or FCF margin decline over 1 or 3 years: all rolling-12-month metrics rising [RA-T, IS-T, CF-T].", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Price competition (Wise, Western Union, banks) or a growth slowdown de-rating a multiple dearer than peers; AUSTRAC AML inquiry outcome.", "veto": null},
  "thesis": "A newly profitable digital remittance leader compounding margins and cash flow with a net-cash balance sheet, priced low against its own history.",
  "rationale": "Scorecard gives conviction 3: top-tier quality, rising direction and net cash, but valuation earns only two points (upside to the value blend just short of the top band; trend strength rather than a deep discount) and competition plus the AUSTRAC inquiry keep key risk medium. Good but not compelling at 22.55, so AVOID; cash is acceptable.",
  "price_at_decision": 22.55,
  "price_date": "2026-11-13",
  "research_note": "research/RELY/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 8%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}},
    {"text": "Gross margin falls below 58%, signalling price competition", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 58}},
    {"text": "TTM FCF margin falls below 12%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "Annual revenue growth falls below 15% on the income-statement page"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 33.95, "basis": "Margins keep expanding and EV/Sales re-rates toward the mechanical bull fair value 33.95 [IS, RA]."},
    "base": {"probability": 0.5, "target_price_12m": 28.0, "basis": "Growth guided to high-teens for 2027 holds margins; price returns to the 28.00 52-week high [HI], below the 31.39 base fair value because that rests on EV/Revenue alone [IS, RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 15.83, "basis": "Price competition or an AUSTRAC/remittance-policy hit slows growth and EV/Sales falls toward the mechanical bear fair value 15.83 [RA]."}
  },
  "entry_price": 19.52,
  "entry_basis": "Base 31.39 x 0.8 sits above the price, so anchored instead on the recent swing low 19.52 (2026-09-23) [HI], where the discount to the value blend would add the missing valuation point.",
  "replaces": null,
  "replacement_reason": null
}
```

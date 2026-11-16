# Evaluation: Masco Corporation (MAS) — 2026-11-16
## Bear case
The price is the bear's best argument: 84.68 sits well above the mechanical base fair value of 60.48 and even the bull value of 64.38, and the reverse DCF needs 8.2% year-1 revenue growth while management assumes no major market rebound for 2027 [Certain]. The trend-strength case carries a de-rating risk: the stock is 18.2% above its 200-day average with EV/Sales above its 5y max, so slowing growth would hit the multiple and the price together [Likely]. ROIC is down 7.0pp in 12 months to 26.7%, 10.1pp below its 2-year high, and ROCE is 4.2pp below its high [Certain]. Reported margin includes a non-recurring tariff refund of about $90 million [company-reported], so underlying margin is lower [Likely]. Real yields rose 0.47pp in ~3m (macro overlay), weighing on housing turnover and volumes [Likely]. Heavy buybacks keep net debt/EBITDA at 1.98x [Certain].

## Bull case
Masco is a high-return branded franchise: ROCE 35.3%, gross margin 36.6% and operating margin 16.9%, flat over the last year, with FCF margin up 2.5pp to 13.6% [Certain]. The ROIC drop came with flat margins and rising cash margins, so it looks like a larger capital base rather than weaker profitability [Guessing]. Pricing power is visible: Q3 net pricing added about five points to sales on mixed volumes [company-reported] [Likely]. Q3 EPS beat and FY26 adjusted EPS guidance was raised to $4.65-$4.75 [Likely]. P/E of 18.4x is 20% up its 5y range and 23% below peers; the FCF yield is 6.39% [Certain]. Shares fell 4.95% YoY and FCF conversion is 112.6% [Certain]. The stock has beaten SPY by 25.1pp over 12 months: a good business that is working [Certain].

## Decision
```json
{
  "ticker": "MAS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Python finds TTM ROIC falling (-7.0pp in 12 months, RA-T) while operating margin is flat (16.9% vs 17.0%, IS-T) and FCF margin rose 2.5pp (CF-T,IS-T); the note reads the fall as a larger invested-capital base, not lost pricing or share (research/MAS/2026-11-16.md), and Q3 guidance was raised.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A de-rating from an extended price: the stock trades well above mechanical fair value and the reverse DCF needs 8.2% growth while rising real yields keep repair-and-remodel volumes flat.",
    "veto": null
  },
  "thesis": "A high-return branded plumbing and paint franchise with flat margins and rising cash conversion is working, but the price already discounts a housing recovery management does not assume.",
  "rationale": "Scorecard conviction is 3: quality and trend strength are real, but the price sits well above every mechanical fair value and assumes growth the company does not guide to, with rising real yields tilting the odds toward the bear. Good but not compelling; cash is an acceptable outcome.",
  "price_at_decision": 84.68,
  "price_date": "2026-11-13",
  "research_note": "research/MAS/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 15.0% (16.9% now), showing pricing no longer offsets tariff and commodity costs.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 22% (26.7% now), showing the decline is eroding returns, not just a larger capital base.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 22}},
    {"text": "TTM FCF margin falls below 10% (13.6% now), showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 2.8x (1.98x now), showing buybacks are outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 96, "basis": "Raised FY26 guidance carries into 2027 and P/E moves toward the peer median of 23.9x [RA,P:FBIN,P:OC,P:AOS,P:ALLE] as mortgage costs ease (macro overlay bull)."},
    "base": {"probability": 0.45, "target_price_12m": 84, "basis": "Earnings grow modestly on pricing with flat volumes and the P/E holds near 18.4x [RA], so return comes mostly from buybacks; above the mechanical base fair value because the DCF is blind to the FCF yield of 6.39% [ST] and the trend."},
    "bear": {"probability": 0.30, "target_price_12m": 64, "basis": "Rising real yields keep housing frozen (macro overlay, small bear tilt raises this probability), margin slips as the tariff refund drops out [company-reported, note] and the stock de-rates toward the mechanical bull fair value of 64.38 [fact sheet]."}
  },
  "entry_price": 48.38,
  "entry_basis": "Valuation file: base 60.48 x 0.8 (research/MAS/2026-11-16-valuation.md); the obstacle is price, not quality, so a real discount to fair value would lift the scorecard to 4.",
  "replaces": null,
  "replacement_reason": null
}
```

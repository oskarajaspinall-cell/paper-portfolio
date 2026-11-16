# Evaluation: Medpace Holdings, Inc. (MEDP) — 2026-11-16
## Bear case
The price already discounts acceleration: the reverse DCF implies 23.1% year-1 revenue growth while backlog grew only 5.6% [company-reported] [Certain]. The close of 653.94 sits above the mechanical base fair value of 458.31 and near the bull case of 684.07 [Certain]. EV/Sales of 6.3x is at 81% of its 5y range and +88% vs peers [Certain]. The stock is 22.9% above its 200-day average after +54.3% in six months; an extended price like this risks a sharp de-rating if Q4 awards or cancellations disappoint, which management flagged as the swing factor for 2027 [Likely]. Direction change: FCF margin fell from 28.7% to 23.5% and ROCE from 108.1% to 75.3% over 12 months [Certain]; if this is more than working-capital timing, the cash story weakens [Guessing]. Biotech funding cycles make awards cyclical [Likely]. Buybacks at 36.3x earnings earn modest returns [Likely].

## Bull case
A high-quality, net-cash CRO that is working: gross margin rose from 61.4% to 72.2% and operating margin holds at 21.4% [Certain]. FCF conversion is still 128.9% of net income, so the FCF-margin dip reads as advance-billing and receivable timing, not a broken model, with operating margin flat [Likely]. Q3 brought record awards of $873.4 million [company-reported] and a raised FY2026 guide [Likely]. Mid-trial switching costs and a biotech-focused niche give a narrow moat [Likely]. Shares fell 5.07% YoY on buybacks and a new $1.0 billion authorisation is in place [company-reported] [Certain]. The trend is healthy, not euphoric: +3.9% over the 50-day with RSI 52.0, beating SPY by 15.4pp over 3 months, FCF yield 3.65% [Certain]. Piotroski 7 and Altman Z 7.00 show a clean balance sheet [Certain].

## Decision
```json
{
  "ticker": "MEDP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin 28.7% -> 23.5% and ROCE 108.1% -> 75.3% over 12 months [CF-T, RA-T] while operating margin is flat at 21.4% [IS-T] and FCF/NI is 128.9%; the 10-Q says receivable and advance-billing timing can vary significantly (https://www.sec.gov/Archives/edgar/data/1668397/000166839726000036/medp-20260930.htm).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "The price implies 23.1% year-1 growth versus 5.6% backlog growth; weak Q4 awards or higher cancellations would de-rate an extended stock.",
    "veto": null
  },
  "thesis": "A high-quality net-cash CRO with record awards, but the price already implies growth well above backlog growth.",
  "rationale": "Quality and trend are real, but the price sits near the mechanical bull value and implies growth the backlog does not yet show. Good but not compelling at this price; the scorecard sets conviction, and below 4 is an AVOID under the owner rule.",
  "price_at_decision": 653.94,
  "price_date": "2026-11-13",
  "research_note": "research/MEDP/2026-11-16.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 19%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 19}},
    {"text": "FCF margin (TTM) falls below 18%, i.e. not just timing", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 18}},
    {"text": "Backlog in the 10-Q falls below $2,900 million, or quarterly net awards fall below $700 million, for two quarters running"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 710.56, "basis": "Awards keep accelerating after record Q3 awards [company-reported, sec.gov 10-Q], supporting the DCF bull value of 710.56 [fact sheet fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 600, "basis": "Earnings grow while P/E drifts toward its 5y median 33.3x [RA] from 36.3x, leaving the price modestly lower; above the mechanical base because margins and buybacks have improved the business beyond its history."},
    "bear": {"probability": 0.25, "target_price_12m": 458.31, "basis": "Weak Q4 awards or cancellations (Q3 call, /stocks/medp/transcripts/714073-q3-2026/) de-rate the stock to the mechanical base fair value 458.31 [fact sheet fair value]."}
  },
  "entry_price": 366.65,
  "entry_basis": "valuation file: base 458.31 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

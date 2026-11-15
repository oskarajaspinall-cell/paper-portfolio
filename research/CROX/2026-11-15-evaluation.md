# Evaluation: Crocs, Inc. (CROX) — 2026-11-15
## Bear case
The price has run ahead of the business. At 163.72 the stock sits at a 52-week high, 44.1% above its 200-day average, RSI 73.0, up 119.9% in a year [Certain]; an extended price risks a de-rating if growth slows, and underlying Q3 growth was modest (Crocs Brand +4.4%, HEYDUDE +6.1% [company-reported]) [Certain]. P/E of 12.3x is at 98% of its 5y range, and trailing earnings are flattered by 630bp of one-off IEEPA tariff refunds in Q3 gross margin [company-reported], so the real multiple is higher [Likely]. The direction change is real: ROIC fell 8.3pp in 12 months to 23.6% and operating margin 2.0pp to 21.1%, 5.1pp below its 2-year high [Certain]. Crocs is a fashion-cycle brand; HEYDUDE already needed a write-down [Likely]. Base fair value of 173.74 leaves little room; bear 115.83 [Certain]. Buybacks at a re-rated price earn less [Likely].
## Bull case
Cash generation is exceptional: FCF yield 10.07%, P/FCF 9.9x versus a 20.9x peer median, FCF/net income 113.5% [Certain]. The reverse DCF implies only 1.6% year-1 revenue growth, so the price still assumes little [Certain]. Q3 beat with growth at both brands, adjusted operating margin up 150 bps and raised FY26 guidance (earnings call transcript [OV]) [Likely], suggesting the margin dip reflects tariff and HEYDUDE costs rather than a broken model [Likely]. Shares are down 10.71% YoY on aggressive buybacks with $1.7bn authorised [company-reported] [Certain]. Balance sheet is sound: net debt/EBITDA 1.58x, Piotroski F 7, Altman Z 4.08 [Certain]. A sustained HEYDUDE recovery would open the DCF bull value of 387.24 [Guessing].
## Decision
```json
{
  "ticker": "CROX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and operating margin fell over the last year on tariff costs and HEYDUDE weakness (the FY2025 impairment); Q3 2026 adjusted operating margin rose 150 bps with growth at both brands and raised FY26 guidance (Q3 2026 transcript, https://stockanalysis.com/stocks/crox/transcripts/719818-q3-2026/), balance sheet intact at 1.58x net debt/EBITDA [ST].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A fashion-cycle fade in the Crocs Brand or a stalled HEYDUDE recovery, with the extended price (44.1% above its 200-day average) de-rating if growth slows.",
    "veto": null
  },
  "thesis": "A highly cash-generative footwear brand at a low P/FCF, but the price has already re-rated on Q3 and trailing margins are flattered by one-off tariff refunds.",
  "rationale": "Strong cash generation and buybacks, but the base fair value sits barely above the price, P/E is at the top of its 5y range, ROIC and operating margin are falling and Q3 was lifted by one-off refunds. Good but not compelling at a 52-week high; cash is acceptable.",
  "price_at_decision": 163.72,
  "price_date": "2026-11-13",
  "research_note": "research/CROX/2026-11-15.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 18%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18}},
    {"text": "ROIC (TTM) falls below 18%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "Debt/EBITDA rises above 2.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "Crocs Brand revenue (10-Q segment note) declines year on year for two consecutive quarters"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 230.0, "basis": "HEYDUDE recovery sustains growth above the 1.6% reverse-DCF implied rate [ST,IS], moving toward the DCF/blend bull values (304.32 blend) but discounted for the fashion-cycle risk in the Bear case."},
    "base": {"probability": 0.5, "target_price_12m": 173.74, "basis": "Modest growth (Crocs Brand +4.4%, HEYDUDE +6.1% [company-reported]) with buybacks supports the mechanical base fair value of 173.74 [IS,BS,CF,RA,ST]."},
    "bear": {"probability": 0.25, "target_price_12m": 115.83, "basis": "Tariff refunds roll off and growth slows, so the P/E at 98% of its 5y range [RA] de-rates toward the bear fair value of 115.83 [IS,BS,CF,RA,ST]."}
  },
  "entry_price": 138.99,
  "entry_basis": "valuation file: base 173.74 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

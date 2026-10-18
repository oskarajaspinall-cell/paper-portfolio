# Evaluation: Genpact Limited (G) — 2026-10-18
## Bear case
The low multiple may be correct, not a mispricing. Genpact sells people-based process work. Agentic AI could shrink the billable work it charges for, and the CEO himself says enterprise AI readiness lags ambition [Guessing]. The price implies -2.8% year-1 revenue growth [Certain], and close peers (EXLS, WNS) are not cheap enough to suggest a sector-wide overreaction; G is cheap even against them [Certain]. Cash quality is slipping: FCF margin fell to 10.9% TTM from 14.5% in FY2025, FCF conversion is 98.2% TTM, and net debt/EBITDA rose back to 1.02x from 0.66x [Certain]. A new CFO and a new Chief Product Officer within two months add execution risk just before Q3 results on Nov 5, 2026 [Likely]. A 12-month change of -5.5% against SPY's +14.8% shows the market is not yet convinced [Certain]. Technology is already the portfolio's largest sector through GDDY, INTU and JKHY [Certain].
## Bull case
On the numbers, quality is improving. ROIC rose to 17.7% from 12.7%, operating margin to 15.0% from 12.7%, and Piotroski F is 7 [Certain]. The price is below its own 5-year minimum on EV/EBITDA (8.1x vs 10.1x), EV/Sales, P/FCF and P/B. It sits at a large discount to peers on every multiple and offers a 9.14% FCF yield [Certain]. Shares fell 2.80% YoY, so buybacks return cash [Certain]. Even the mechanical bear fair value of 39.20 is above the 37.26 close; base is 50.60 [Certain]. Q2 2026 segment growth was positive in every vertical (Financial Services +3.3%, Consumer/Healthcare +9.5%, High Tech/Manufacturing +7.6%) [company-reported] (https://www.sec.gov/Archives/edgar/data/1398659/000139865926000014/g-20260630.htm), which contradicts the implied revenue decline [Likely]. With a beta of 0.58, a re-rating toward the 5-year median EV/EBITDA of 10.6x would be a large gain [Likely].
## Decision
```json
{
  "ticker": "G",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A rising-ROIC, deleveraged process-outsourcing franchise trades below its own 5-year minimum EV/EBITDA at a 9.14% FCF yield, but the price is a bet that agentic AI does not shrink its labour-based revenue, which the evidence cannot yet settle.",
  "rationale": "Cheap and improving on paper, but the key risk is AI substituting for billable work, which the mechanical fair value cannot capture. Slipping FCF margin, two new senior executives and Q3 results within three weeks keep conviction at 3. Adding it would also push Technology toward the sector cap. Good but not compelling: AVOID.",
  "price_at_decision": 37.26,
  "price_date": "2026-10-16",
  "research_note": "research/G/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROIC falls below 14%, reversing the five-year rise from 12.7% to 17.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 14}},
    {"text": "TTM operating margin falls below 13%, erasing the expansion from 12.7% to 15.0% and signalling AI-driven price deflation.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 13}},
    {"text": "TTM FCF margin falls below 9%, under the FY2022 five-year low of 9.0%, showing cash conversion is deteriorating structurally.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 9}},
    {"text": "Reported revenue (10-Q/10-K or earnings release) declines year on year for two consecutive quarters, confirming the AI-substitution decline the price implies; conversely, sustained positive growth across all verticals would argue for re-research."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 50.60, "basis": "Positive segment growth persists [company-reported] and EV/EBITDA re-rates toward its 5y median 10.6x [RA], consistent with the base fair value of 50.60 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.45, "target_price_12m": 42.00, "basis": "Revenue roughly flat and margins near 15.0% [IS], with the multiple only partly closing the gap to the 5y EV/EBITDA minimum 10.1x [RA]; below the mechanical base because AI-substitution doubts keep a discount."},
    "bear": {"probability": 0.30, "target_price_12m": 30.00, "basis": "Agentic AI cuts billable volumes, so the price-implied -2.8% revenue decline [HI] proves right and the stock returns toward its 6-month low of 26.85 [HI]; this is below the mechanical bear of 39.20, which assumes no revenue decline."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock is already below its mechanical bear fair value. What holds conviction at 3 is unresolved evidence on whether agentic AI shrinks revenue, so a lower price would not change the decision. Q3 2026 results (Nov 5, 2026) and the triggers above would.",
  "replaces": null,
  "replacement_reason": null
}
```

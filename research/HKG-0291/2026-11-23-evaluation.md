# Evaluation: China Resources Beer (Holdings) Company Limited (HKG:0291) — 2026-11-23
## Bear case
Returns are slipping: rolling ROIC fell to 10.8% from 12.6% a year earlier, its 2-year high, and ROE is down to 6.3% from 20.1% [Certain]. Net margin fell to 7.2% while operating margin rose, and the cause of the below-the-line drag is still not identified [Certain]; if it is recurring (impairments, weaker other income), operating gains never reach shareholders [Guessing]. ROIC near 10% is only moderate for a claimed scale moat [Likely]. Revenue is essentially all mainland China, and the reverse DCF already prices -6.6% year-1 revenue growth; a real volume contraction could still outrun premiumisation [Likely]. The trend is weak: 10.1% below the 200-day average, the 50-day 15.8% below the 200-day, 12-month change -25.6% [Certain]. P/E of 21.2x is above the peer median of 16.7x, so on earnings it is not cheap [Certain]. Capital returns were not checked [Certain].
## Bull case
The operating franchise is improving: operating margin rose from 9.0% in FY2021 to 14.9% TTM and gross margin to 42.3% [Certain]. On a rolling basis operating margin is up 0.6pp and ROCE up 0.5pp over the year, and FCF margin is at its 2-year high of 15.3% [Certain]. FCF/net income is 213.2% and the balance sheet is net cash at -1.55x net debt/EBITDA [Certain]. EV/EBITDA of 6.1x, P/FCF of 10.0x, EV/Sales of 1.3x and P/B of 1.6x all sit below their own 5-year minimums, and P/FCF is far below peers at 20.5x, for a 10.04% FCF yield [Certain]. The price implies shrinking revenue that rising margins do not show [Likely]. Scale and distribution in a consolidated market give a narrow moat [Likely]. The mechanical base fair value of 34.20 HKD sits well above the price [Certain]. CNY and HKD are stable (macro overlay, context only) [Certain].
## Decision
```json
{
  "ticker": "HKG:0291",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only ROIC is falling (10.8% TTM vs 12.6% a year earlier [RA-T]). Over the same year operating margin rose 0.6pp [IS-T], ROCE rose 0.5pp [RA-T] and FCF margin reached its 2-year high of 15.3% [CF-T], with net cash intact (-1.55x [BS,IS]); no sign of lost share or a price cap, so the drag sits below the operating line rather than in the business model.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Mainland China beer volumes contract and the unexplained fall in net margin and ROE proves to be recurring charges, so the operating gains do not reach shareholders.",
    "veto": null
  },
  "thesis": "A net-cash Chinese brewer with rising operating and FCF margins trades below its own 5-year minimum cash multiples, pricing shrinkage that its improving operations do not show.",
  "rationale": "Same evidence as the 2026-11-16 HOLD 4: cash multiples below their 5-year minimums, net cash and improving operating and FCF margins, against slipping ROIC, an unexplained net-income fall and a weak trend. The position is near its target size and cash is near the floor, so no ADD.",
  "price_at_decision": 20.78,
  "price_date": "2026-11-20",
  "research_note": "research/HKG-0291/2026-11-23.md",
  "triggers": [
    {"text": "TTM operating margin falls below 12.0% (14.9% now), reversing the mix and pricing gains.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12.0}},
    {"text": "TTM FCF margin falls below 10.0% (15.3% now), showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10.0}},
    {"text": "TTM ROIC falls below 9.0% (10.8% now), below the FY2024 low of 10.3%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9.0}},
    {"text": "Net debt/EBITDA (debt minus cash and short-term investments) turns positive from -1.55x TTM, i.e. net cash is gone."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 34.20, "basis": "Margins hold and the market prices stable rather than shrinking revenue, reaching the mechanical blended base fair value of 34.20 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 28.14, "basis": "Operating margin stays near 14.9% [IS-T] and FCF margin near its 2-year high [CF-T], moving the price toward the DCF base of 28.14 while EV/EBITDA stays below its 5y median [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 16.74, "basis": "China volumes contract and charges keep depressing net income (ROE 6.3% [RA]), taking the price to the mechanical bear fair value of 16.74 [IS,BS,CF,RA,ST,HI]."}
  },
  "entry_price": null,
  "entry_basis": "Held at conviction 4, so no entry price is needed; the position is near its size and an ADD is not the question.",
  "replaces": null,
  "replacement_reason": null
}
```

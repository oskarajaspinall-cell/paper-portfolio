# Evaluation: Open Text Corporation (OTEX) — 2026-11-09
## Bear case
This is an ex-growth, acquisition-built software estate in managed decline: Q1 revenue fell 4.0% reported, with Cybersecurity, ITOM and Analytics shrinking [company-reported] (https://www.sec.gov/Archives/edgar/data/1002638/000100263826000098/otex-20260930.htm) [Certain]. AI could erode content and IT-operations seats faster than Content Cloud grows [Guessing]. FCF margin is falling over the last year, 16.3% TTM against 17.5% a year earlier [CF-T], and the refinanced notes carry higher coupons, so interest keeps eating cash [Likely]. Leverage is high for a shrinking business: net debt/EBITDA 3.10x and Altman Z 1.35 [ST] [Certain]. ROIC of 9.9% [RA] is not moat-grade, so the discount to peers (P/E 9.4x vs 21.8x) is partly deserved [Likely]. The mechanical fair value is flagged unreliable, with methods disagreeing 2.3x, so the cheapness case rests on multiples rather than a robust intrinsic value [Certain]. The February multi-year plan is a binary-ish reset risk [Likely].

## Bull case
The price already discounts collapse: the reverse DCF implies -13.4% year-1 revenue growth [OV] against a Core revenue rise of 2.7% in constant currency and an FY27 outlook maintained (transcript headline, /stocks/otex/transcripts/726164-q1-2027/) [Likely]. Every multiple sits at the floor of its 5-year range: EV/EBITDA 6.8x (3% position), P/FCF 7.0x (3%), FCF yield 14.34% [RA, ST] [Certain]. Profitability is improving on a rolling basis: operating margin 23.0% at its 2-year high, up from 20.5% a year earlier, and ROCE up to 11.3% [IS-T, RA-T] [Certain]. The FCF dip is small and explained by financing and divestiture effects; Q1 FCF was $138.5m vs $101.2m a year earlier [company-reported] (same 10-Q) [Likely]. Shares fell 5.26% YoY [ST] and the 2027 maturities are refinanced, removing the near-term funding wall [Certain]. Switching costs in embedded records systems give a narrow moat [Likely].

## Decision
```json
{
  "ticker": "OTEX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only FCF margin is falling (16.3% TTM vs 17.5% a year earlier [CF-T]) while operating margin rose to a 2-year high of 23.0% [IS-T]; the dip reflects higher coupons on the refinanced notes and divestitures, and Q1 FCF rose to $138.5m from $101.2m [company-reported] (https://www.sec.gov/Archives/edgar/data/1002638/000100263826000098/otex-20260930.htm).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Organic revenue decline accelerates (AI substitution in ITOM, cybersecurity and content) while leverage stays near 3.10x net debt/EBITDA, forcing a guidance cut in the February multi-year plan.",
    "veto": null
  },
  "thesis": "A switching-cost information-management franchise with a rising operating margin and a 14.34% FCF yield trades at the floor of its own 5-year multiples, but sub-10% ROIC, shrinking reported revenue and 3.10x leverage make it cheap for a reason rather than a high-conviction buy.",
  "rationale": "Python scorecard gives 3: the deep own-history and peer discount and rising operating margin are offset by ROIC below 10% and 3.10x leverage with Altman Z 1.35, which gate a buy. Same evidence and verdict as the 2026-11-08 AVOID 3; cash is an acceptable outcome.",
  "price_at_decision": 24.85,
  "price_date": "2026-11-06",
  "research_note": "research/OTEX/2026-11-09.md",
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the quality level (ROIC 9.9%) and leverage (3.10x net debt/EBITDA) cap the score and the base fair value is flagged unreliable, so a lower price alone would not lift conviction to 4.",
  "triggers": [
    {"text": "TTM operating margin falls below 20% (23.0% now, 20.5% a year earlier), showing the margin gains were cost cuts on a shrinking base rather than durable.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 13% (16.3% now), turning the explained FCF dip into structural cash erosion from interest and organic decline.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 13}},
    {"text": "Net debt/EBITDA rises above 3.75x (3.10x TTM now), showing leverage is building rather than falling.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.75}},
    {"text": "Company-reported Core revenue growth turns negative in constant currency in a quarterly release, or the FY27 outlook is cut, including in the February multi-year plan."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 45.0, "basis": "February plan confirms stable Core revenue and EV/EBITDA re-rates from 6.8x toward its 5y median 9.9x [RA]; well below the mechanical bull of 132.27, which the fact sheet flags unreliable."},
    "base": {"probability": 0.45, "target_price_12m": 33.0, "basis": "Operating margin holds near 23.0% [IS-T] and P/FCF recovers partway from 7.0x toward its 5y median 10.9x [RA], close to the EV/Revenue base of 36.56 rather than the unreliable blended base of 68.50."},
    "bear": {"probability": 0.30, "target_price_12m": 19.77, "basis": "Reported revenue keeps falling (4.0% in Q1 [company-reported], 10-Q) and leverage at 3.10x [ST] keeps multiples below their 5y minimums, revisiting the 52-week low of 19.77 [HI]; below the EV/Revenue bear of 22.10."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

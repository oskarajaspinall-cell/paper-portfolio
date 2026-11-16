# Evaluation: Dropbox, Inc. (DBX) — 2026-11-16
## Bear case
Dropbox is a mature franchise that has stopped growing and is levering up to shrink its share count. Paying users are barely up at 18.20 million [company-reported], the 10-Q adds language that growth "has declined" and users may fall, and the Q3 call points to flat preliminary FY2027 revenue [Likely]. Net debt/EBITDA has risen from 2.09x in FY2024 to 3.41x TTM, before the $1.1bn convertible priced on 2026-11-10, adding dilution risk and interest [Certain]. Altman Z is 0.53 [Certain]. The **Direction change**: ROIC fell from 64.9% to 33.7% and ROCE from 74.5% to 41.4% in a year, and FCF margin is 2.7pp below its 2-year high; the 10-Q says FCF fell on higher term-loan interest [Certain]. The price fell after results and the convert, not on noise; short interest is 19.01% of float and rising [Certain]. The workforce cut and unproven DBX Agent Cloud spend add execution risk [Likely].
## Bull case
The business throws off cash at a 36.1% FCF margin and 26.6% operating margin, both flat over the last 12 months, so the core is stable, not eroding [Certain]. The ROIC fall is mostly a capital-structure effect of debt-funded buybacks (shares down 18.02% YoY), not weaker unit economics [Likely]. At 8.1x P/FCF (11% of its own 5-year range), 12.4x EV/EBITDA (14%) and a 12.31% FCF yield, the reverse DCF prices -6.1% year-1 revenue growth, while Q3 was a beat with raised FY2026 guidance [Certain]. Mechanical base fair value is 47.53, well above the 33.53 close [Certain]. Switching costs and habit in the installed base protect margins [Likely]. Insiders own 40.24%, aligning management with per-share value [Certain]. Price remains above its 200-day average [Certain].
## Decision
```json
{
  "ticker": "DBX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC/ROCE fell 64.9% -> 33.7% / 74.5% -> 41.4% while operating margin (26.3% -> 26.6%) and FCF margin (36.2% -> 36.1%) were flat over the same 12 months [IS-T, CF-T]; the fall tracks debt-funded buybacks (shares -18.02% YoY [ST]) rather than weaker unit economics (note section 2).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Flat-to-shrinking revenue (flat FY2027 preview, paying users barely growing) combined with rising leverage (3.41x net debt/EBITDA plus a $1.1bn convertible) could erode FCF per share through interest and dilution.",
    "veto": null
  },
  "thesis": "A highly cash-generative but ex-growth file-sync franchise trades at the bottom of its own cash multiples, but flat revenue, rising leverage and a new convertible keep the skew balanced rather than compelling.",
  "rationale": "Cheap on FCF with stable margins, but revenue is flat, leverage is rising into a new convertible and the price fell on results and financing, not noise. The scorecard does not reach the buy bar; price is not the obstacle, so no entry level.",
  "price_at_decision": 33.53,
  "price_date": "2026-11-13",
  "research_note": "research/DBX/2026-11-16.md",
  "triggers": [
    {"text": "TTM FCF margin falls below 30%, under the FY2023 five-year low of 30.4%, showing interest and investment are eroding cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "TTM operating margin falls below 22%, reversing most of the post-FY2024 margin step-up.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}},
    {"text": "TTM ROIC falls below 20%, showing returns erosion beyond the buyback denominator effect.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA on the ratios page rises above 4.5x, or paying users in the 10-Q fall below 17 million."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 47.53, "basis": "Stable margins and buybacks re-rate cash multiples toward the 5y median P/FCF of 10.4x [RA], reaching the mechanical base fair value of 47.53 (fact sheet Fair value)."},
    "base": {"probability": 0.5, "target_price_12m": 37.0, "basis": "Flat FY2027 revenue (Q3 call headline [OV]) caps re-rating; P/FCF drifts only partway from 8.1x toward its 5y median while buybacks lift FCF per share [RA, ST]."},
    "bear": {"probability": 0.25, "target_price_12m": 25.0, "basis": "Paying users decline and interest on the convertible and term loan squeezes FCF (10-Q, note section 5), pushing value toward the mechanical bear of 22.81 (fact sheet Fair value)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades well below base fair value; the obstacles are flat revenue, rising leverage and the new convertible, so a lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

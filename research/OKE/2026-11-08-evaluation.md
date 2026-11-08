# Evaluation: ONEOK, Inc. (OKE) — 2026-11-08
## Bear case
Cash is not following earnings. FCF margin fell from 9.3% to 5.9% and operating margin from 18.0% to 14.2% over the last 12 months, well below the 2-year highs of 13.7% and 22.9% [Certain]. That contradicts the 5-year "rising" operating-margin read. The 10-Q blames higher operating costs and a build in unfractionated NGL inventory [company-reported] [Likely]. Neither is proven to reverse, and growth capex continues [Likely]. FCF conversion is 62.2% against 94.5% in FY24 [Certain]. The low P/E of 13.2x is flattered by a one-off non-cash tax benefit, and P/FCF of 21.2x sits above its 5y max of 20.5x [Certain], so the stock is cheap on EBITDA, not on cash. Brazos debt is not yet in the 3.68x leverage figure [Certain]. Apollo's Class B units rank ahead of common equity [Likely]. Shares rose 2.75% YoY [Certain]. The mechanical bear value of 77.94 is below the price [Certain].
## Bull case
The network is hard to replicate and about 90% fee-based [company-reported] [Likely]. Q3 volumes rose and 2026 guidance was raised again [Likely]. S&P and Fitch upgraded the credit to BBB+ [company-reported] [Certain]. TTM ROIC of 8.8% is at its 2-year high and up 0.9pp on a year earlier [Certain]. EV/EBITDA of 10.7x is at its 5y minimum and below the peer median of 13.1x [Certain]. The reverse DCF needs only 3.3% year-1 revenue growth [Certain]. The base fair value of 101.12 is above the 85.19 close [Certain]. Brazos adds Permian Midland scale [Likely]. If inventory and working capital unwind, FCF could recover quickly [Guessing]. Macro is context only: the business is domestic with no country risk [Likely].
## Decision
```json
{
  "ticker": "OKE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A fee-based US midstream network trades at the bottom of its own EV/EBITDA range after a guidance raise, but falling 12-month operating and FCF margins mean the cheapness rests on EBITDA rather than cash, so the upgrade to conviction 4 is not earned.",
  "rationale": "Guidance raise, credit upgrade and a low EV/EBITDA do not offset a sharp fall in FCF and operating margin over the last year, P/FCF above its 5y range and leverage that excludes Brazos. Base upside is modest against a bear value below the price. Conviction stays 3: AVOID, no position.",
  "price_at_decision": 85.19,
  "price_date": "2026-11-06",
  "research_note": "research/OKE/2026-11-08.md",
  "triggers": [
    {"text": "TTM FCF margin falls below 4% (5.9% now, 9.3% a year earlier), showing the cash-conversion slide is structural rather than working capital.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 4}},
    {"text": "TTM operating margin falls below 12% (14.2% now), showing cost pressure is eroding the fee-based model.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "TTM ROIC falls below 7% (8.8% now) once Brazos is consolidated, showing the acquisition dilutes returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 7}},
    {"text": "Net debt/EBITDA rises above 4.5x (3.68x before Brazos debt) once the acquisition is in the TTM numbers.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 110.0, "basis": "FCF margin recovers toward its 13.7% 2-year high [CF-T] as NGL inventory unwinds and EV/EBITDA re-rates toward its 5y median 12.6x [RA]; set far below the mechanical bull of 381.97, which the note judges not credible."},
    "base": {"probability": 0.5, "target_price_12m": 95.0, "basis": "Raised guidance and Brazos volumes (Q3 release) lift EBITDA while EV/EBITDA recovers partway from its 5y minimum 10.7x [RA]; set below the mechanical base of 101.12 because FCF conversion of 62.2% [CF,IS] does not yet support the DCF's cash flows."},
    "bear": {"probability": 0.3, "target_price_12m": 77.94, "basis": "Operating and FCF margins keep falling from 14.2% and 5.9% [IS-T,CF-T] and Brazos debt lifts leverage from 3.68x [RA]: the mechanical bear fair value of 77.94 [fact sheet Fair value]."}
  },
  "entry_price": 80.9,
  "entry_basis": "valuation file: base 101.12 x 0.8 (fact sheet Fair value [IS,BS,CF,RA,ST,HI]); at that level the margin of safety would compensate for the unresolved cash-conversion question, provided the FCF-margin trigger has not fired.",
  "replaces": null,
  "replacement_reason": null
}
```

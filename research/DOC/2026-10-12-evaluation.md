# Evaluation: Healthpeak Properties, Inc. (DOC) — 2026-10-12
## Bear case
The upside is thin for a levered REIT: the P/FFO base fair value of 21.53 is only +14.5% above the 18.80 close, and the bull value (21.69) barely adds to it [Certain]. Leverage is high and rising on the fact sheet's own measure, from 6.15x (FY2023) to 6.57x TTM net debt/EBITDA, with bridge debt awaiting permanent capital [Certain]. Returns are weak: ROIC 2.5% TTM and ROE 3.0%, Piotroski 5 [Certain]. The macro overlay tilts moderately toward bear: active Fed hikes and rising real yields push up cap rates and refinancing costs, which could keep the multiple near its trough [Likely]. Janus Living consolidation makes the 5y-low multiples not fully like-for-like, so "cheap vs history" may partly be an accounting artefact [Likely]. Momentum is negative: -8.5% vs the 50-day and -16.4pp vs SPY over 3m [Certain].
## Bull case
DOC trades at 13.9x EV/EBITDA, the 3rd percentile of its 5y range, and below its 5y minimum EV/Sales, at a 29-36% discount to healthcare REIT peers [Certain]. Q2 2026 beat and raised FY26 adjusted FFO guidance to $1.73-$1.77 [Certain]. Capital recycling via the Brookfield JV and the Janus Living IPO is being done without issuing DOC shares; the share count fell 0.69% YoY [Certain]. The JV sale at scale suggests private-market values support book value, with P/B 1.7x near its 5y median [Likely]. If real yields stabilise, the multiple could re-rate toward the 21.53-21.69 fair-value range quickly, and the monthly dividend continues [Likely]. The rate headwind looks largely priced after a -12.8% 3-month move [Guessing].
## Decision
```json
{
  "ticker": "DOC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A healthcare REIT at the bottom of its own 5-year EV/EBITDA range with a raised FFO guide, but low returns, rising leverage and a rate headwind cap the upside at about the 21.53 base fair value.",
  "rationale": "Cheap versus history and peers, but the mechanical upside is only +14.5% to base fair value. Leverage is high (6.57x) and rising, ROIC is 2.5%, and the macro overlay tilts moderately toward bear. Good but not compelling: conviction 3 means no position. I would revisit at a 20% margin of safety.",
  "price_at_decision": 18.80,
  "price_date": "2026-10-09",
  "research_note": "research/DOC/2026-10-12.md",
  "triggers": [
    {"text": "Net debt/EBITDA (statistics) rises above 7.0x, showing the acquisition-funded leverage build is not being repaid with recycling proceeds.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 7.0}},
    {"text": "TTM ROIC falls below 2.0%, below the FY2021 five-year low of 2.5%, indicating structurally deteriorating returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 2.0}},
    {"text": "Total same-store cash NOI growth in the next earnings release turns negative, against the guided 0%-1.5%."},
    {"text": "FY2026 adjusted FFO per share guidance is cut below the raised $1.73-$1.77 range in a company earnings release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 21.69, "basis": "Real yields stabilise and the multiple re-rates to the P/FFO-proxy bull fair value of 21.69 [IS,BS,CF,RA,ST], helped by the raised FY26 FFO guidance [OV]."},
    "base": {"probability": 0.45, "target_price_12m": 19.54, "basis": "FFO guidance is delivered but, with the macro overlay's moderate tilt toward bear (research/DOC/2026-10-12-macro.md), the multiple stays near trough at the P/FFO-proxy bear fair value of 19.54 [IS,BS,CF,RA,ST] rather than the 21.53 base."},
    "bear": {"probability": 0.30, "target_price_12m": 15.70, "basis": "Further Fed hikes and wider credit spreads (research/DOC/2026-10-12-macro.md) raise refinancing costs on 6.57x net debt/EBITDA [BS,IS] and push the stock back to its 52-week low of 15.70 [HI], below the mechanical bear value."}
  },
  "entry_price": 17.22,
  "entry_basis": "valuation file: base 21.53 x 0.8 = 17.22, a 20% margin of safety that would compensate for the leverage and rate risk.",
  "replaces": null,
  "replacement_reason": null
}
```

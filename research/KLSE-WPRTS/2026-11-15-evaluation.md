# Evaluation: Westports Holdings Berhad (KLSE:WPRTS) — 2026-11-15
## Bear case
The price already pays for quality [Certain]: P/E 19.2x sits at 94% of its 5y range, EV/EBITDA 13.3x at 91%, P/B 5.7x is above its 5y maximum, and both earnings multiples are well above the peer median 15.4x / 10.3x [Certain]. The value comes from trend strength, not a discount, so an extended price risks a de-rating if volume growth or margins slow [Likely]. Operating margin is down 3.0pp in the last 12 months (49.1% to 46.1%) and 10.0pp over five fiscal years, with no guided reset or one-off identified; carrier bargaining power or rival ports are a plausible cause [Guessing]. FCF margin is 11.1pp below its 2-year high. Leverage rose from 0.35x to 1.23x [Certain]. The mechanical base fair value 6.89 is below the price (flagged unreliable) [Certain]. Concession terms, revenue mix and MYR translation are unchecked [Certain].
## Bull case
A scarce concession-backed port with infrastructure-like returns: TTM ROIC 19.8% and ROCE 22.3%, both at their 2-year highs and rising over the last 12 months (ROIC 16.6% to 19.8%), so the 5-year slide has reversed for now [Certain]. Cash conversion is exceptional, FCF/net income 131.9% and FCF margin 44.2%, giving a 6.80% FCF yield; P/FCF 14.7x sits at only 24% of its 5y range [Certain]. Beta 0.12 and Altman Z 3.98 make it a low-risk compounder [Certain]. The trend is healthy: +34.3% over 12 months, +15.8% above the 200-day average, not overextended [Certain]. The reverse DCF needs only 4.6% year-1 revenue growth [Certain], modest for a hub port that has just finished debt-funded expansion now being paid down [Likely].
## Decision
```json
{
  "ticker": "KLSE:WPRTS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "structural", "decline_evidence": "Operating margin is down 3.0pp over the last 12 months (49.1% -> 46.1%) and 10.0pp over five fiscal years [IS, IS-T]; neither the note nor the fact sheet identifies a guided reset, one-off or investment phase, and the note flags carrier bargaining power or rival ports as the open question, so no temporary cause can be cited.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "De-rating from the top of its own 5y P/E and EV/EBITDA ranges (and P/B above its 5y max) if the operating-margin slide continues or volume growth slows.", "veto": null},
  "thesis": "A high-return, cash-generative Port Klang concession with rising rolling ROIC trades at the top of its own earnings-multiple history while operating margin keeps eroding, so the trend is good but the price leaves little margin for error.",
  "rationale": "Quality and cash conversion are excellent and the trend is healthy, but valuation points come only from momentum, multiples sit near 5y highs and above peers, and the operating-margin slide is unexplained. Good but not compelling: AVOID, with an entry price where a margin of safety returns.",
  "price_at_decision": 7.32,
  "price_date": "2026-11-13",
  "research_note": "research/KLSE-WPRTS/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, giving up the rolling recovery from 16.6% to 19.8%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 42%, extending the slide from 51.1% (2-year high) and pointing to lost pricing power.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 42}},
    {"text": "TTM FCF margin falls below 35%, showing the cash conversion is no longer holding.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 35}},
    {"text": "Net debt/EBITDA rises above 2.5x (1.23x TTM now), reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 8.42, "basis": "Rolling ROIC keeps rising and the market accepts the DCF base value of 8.42 [IS,CF,ST] as margins stabilise; above the blended base because the EV/EBITDA leg (flagged unreliable) penalises the current premium."},
    "base": {"probability": 0.45, "target_price_12m": 7.32, "basis": "P/FCF holds near 14.7x [RA] with FCF margin flat at 44.2% [CF-T]; above the blended base fair value 6.89 because the reverse DCF's 4.6% growth looks achievable for a hub port."},
    "bear": {"probability": 0.30, "target_price_12m": 5.21, "basis": "Operating margin keeps sliding from 46.1% [IS-T] and the P/E de-rates from the top of its 5y range towards its median 17.7x [RA], toward the DCF bear 5.21 [IS,CF,ST]."}
  },
  "entry_price": 5.51,
  "entry_basis": "valuation file: base 6.89 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

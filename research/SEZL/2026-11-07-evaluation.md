# Evaluation: Sezzle Inc. (SEZL) — 2026-11-07
## Bear case
The drift setup has already failed: the 2026-11-06 close of 149.43 sits below the reaction-day low of 152.116, so the market gave back most of the post-results move within one session [Certain]. The mechanical stop (reaction low − 0.25 × ATR) lands a fraction of a dollar under the close, inside ordinary noise for a stock with an ATR of 12.25 (8.2%) and a 5y beta of 6.60; a first-session stop-out is the likely outcome, so the 2:1 ratio is an artefact, not an edge [Likely]. Crowding and gap risk are high: P/E 28.9x is above its 5y max of 18.3x, P/B 18.2x against a peer median of 3.3x, base fair value 81.24 sits far below the price, and short interest is 23.26% of float and rising [Certain]. VIX and high-yield spreads are widening (macro overlay, context only) [Likely].

## Bull case
The quarter was a genuine beat-and-raise: revenue grew faster than transaction volume, subscribers neared one million and FY26 and FY27 earnings guidance were raised (https://www.globenewswire.com/news-release/2026/11/04/3395777/0/en/sezzle-reports-third-quarter-2026-results.html) [Likely]. Fundamentals are exceptional and improving: operating margin 60.0% TTM, FCF margin 51.2%, ROIC 94.4%, Piotroski 8, Altman Z 14.25, shares shrinking 1.26% [Certain]. The uptrend is intact (price above both the 50-day and 200-day averages, 12-month +125.6%), and heavy short interest could fuel a squeeze if the results keep being digested [Guessing]. EV/EBITDA of 14.5x is below the peer median of 21.9x [Certain].

## Decision
```json
{
  "ticker": "SEZL",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A strong Q3 beat-and-raise did not produce a usable post-earnings drift: the price already closed below the reaction-day low, leaving a noise-level stop on an 8%-ATR, high-short-interest stock.",
  "rationale": "The setup's edge has gone: the close is under the reaction-day low, so the volatility stop sits inside one day's noise and the 2:1 ratio is meaningless. Valuation far above own history and fair value adds gap risk. Business quality is excellent but conviction rates the trade, not the company; cash is preferable.",
  "price_at_decision": 149.43,
  "price_date": "2026-11-06",
  "research_note": "research/SEZL/2026-11-07.md",
  "exit_plan": {"target": 178.55, "stop": 149.05, "time_limit": "2026-12-31"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 195.71, "basis": "Delivery on the raised FY26/FY27 guidance (GlobeNewswire Q3 release) and margin expansion (operating margin 60.0% TTM [IS]) carry the stock back to its 52-week high of 195.71 [HI], well above the mechanical bull fair value 96.90, which extrapolates own-history multiples that predate the profit step-up."},
    "base": {"probability": 0.45, "target_price_12m": 149.43, "basis": "Growth roughly matches the 37.6% year-1 growth the reverse DCF implies [fact sheet Fair value], so the multiple holds and the price stays near today's close; above base fair value 81.24 because the FCFE model anchors on a loss-making history [RA]."},
    "bear": {"probability": 0.3, "target_price_12m": 81.24, "basis": "Credit or regulatory stress (bank-charter execution, widening HY spreads per macro overlay) de-rates P/E from 28.9x toward its 5y range [RA], taking the price to base fair value 81.24 [fact sheet Fair value]; the mechanical bear of -152.23 is not meaningful for a net-cash-generative business."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

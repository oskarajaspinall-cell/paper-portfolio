# Evaluation: ADNOC Logistics & Services plc (ADX:ADNOCLS) — 2026-11-02
## Bear case
The fall has no identified cause: no filing, results or headline after 2026-08-24, so it removed no obstacle and confirmed no overreaction [Certain]. TTM operating margin of 26.0% sits far above FY2025's 18.1%, so earnings may be near a cyclical peak and the low P/E of 8.9x flatters [Likely]. FCF conversion is only 39.4% TTM as fleet purchases absorb cash, and P/FCF of 22.6x is a premium to the peer median of 12.9x [Certain]. Hormuz tensions are a direct operational risk to a Gulf-based fleet [Likely]. ADNOC controls the equity (institutions 4.6%), so minority holders have little say on capital allocation [Likely]. Results on Nov 11, 2026 are a binary event; buying ahead of them on an unexplained dip is speculation [Likely].

## Bull case
Quality is improving on every line: ROIC rose from 3.6% to 19.4% TTM, net debt/EBITDA is 0.13x and Piotroski F is 8 [Certain]. Contracted revenue with parent ADNOC underpins visibility, consistent with a beta of 0.42 [Likely]. Multiples are below their 5y minimums (EV/EBITDA 6.5x vs 9.1x), and base fair value of 8.18 AED sits above the 6.84 close [Certain]. Reuters reported a third guidance raise with Q2 results (headline only) and the fleet is growing [Guessing]. The dip leaves the price under its 50-day average with RSI 37.8 inside a rising 12-month trend [Certain].

## Decision
```json
{
  "ticker": "ADX:ADNOCLS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A steadily improving, contract-backed ADNOC shipping franchise trading below its own multiple history, but with possibly peak margins, weak cash conversion and Hormuz risk that leave only a modest margin of safety.",
  "rationale": "The fall has no identified cause: nothing broke the thesis and nothing removed the AVOID's obstacle (thin margin of safety against possibly peak margins and low FCF conversion). Base fair value upside is modest and results are imminent. Conviction stays 3; a lower price closer to the margin-of-safety level would justify a BUY.",
  "price_at_decision": 6.84,
  "price_date": "2026-10-30",
  "research_note": "research/ADX-ADNOCLS/2026-11-02.md",
  "triggers": [
    {"text": "TTM operating margin (statistics page) falls below 15%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC (statistics page) falls below 10%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin (statistics page) turns negative", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Debt/EBITDA (statistics page) rises above 2.0x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 10.28, "basis": "EV/EBITDA re-rates toward its 5y range (min 9.1x [RA]) on sustained TTM EBITDA, matching the EV/EBITDA bull fair value of 10.28 [fact sheet fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 8.18, "basis": "Contracted ADNOC revenue holds TTM margins roughly steady and the price converges on the blended base fair value of 8.18 AED [IS,CF,RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 4.8, "basis": "Operating margin reverts toward FY2025's 18.1% [IS] or Hormuz disruption hits the fleet, sending the price back to its 52-week low of 4.80 [HI]; the mechanical negative bear fair value is a DCF artefact of negative historical FCF and is not used."}
  },
  "entry_price": 6.54,
  "entry_basis": "valuation file: base 8.18 x 0.8 (20% margin of safety), which would offset the peak-margin and cash-conversion risk.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Hermès International (EPA:RMS) — 2026-11-21
## Bear case
The fall to 1,225.50 is a growth de-rating, not a dislocation: Q3 growth slowed to 6% at constant exchange rates and ready-to-wear turned negative for the first time in years [Certain] (https://www.reuters.com/business/retail-consumer/hermes-third-quarter-growth-slows-ready-to-wear-turns-negative-2026-10-22/). China footfall and currency are named uncertainties; the yuan is ~5.7% weaker against the euro over ~3m (macro overlay) [Likely]. Direction change: ROIC is down 2.5pp and ROCE 2.9pp over 12 months, ROIC 6.9pp below its 2-year high [Certain]; margins are flat, so this is a growing capital base earning less, not lost pricing [Likely]. Still the dearest in its peer set (P/E +34%, EV/EBITDA +72% vs peers) and the reverse DCF needs 20.6% year-1 revenue growth, far above the delivered pace [Certain]. The price merely sits at the mechanical base fair value (+0.4%), itself flagged unreliable, and the trend is broken (-23.2% vs the 200-day) [Certain].
## Bull case
Hermès has the clearest moat in luxury: rationed supply, in-house craft and own stores held operating margin between 40.0% and 42.9% every year since FY2021, 41.8% TTM [Certain]. Net cash (net debt/EBITDA -1.42x), no dilution (shares 0.03% YoY) and FCF margin recovering to 31.4% from 26.5% a year earlier [Certain]. Every multiple is below its own 5-year minimum: P/E 28.5x vs a 44.9x floor, EV/EBITDA 15.9x vs 28.7x, FCF yield 3.94% [Certain]. The P/E method alone gives a base of 2,114.48 [Certain]. Growing 6% at constant currency while peers report declines suggests share gains [Likely]; a China stabilisation could re-rate it toward its own range [Guessing].
## Decision
```json
{
  "ticker": "EPA:RMS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and ROCE fell over the last year while operating margin rose to 41.8% TTM from 41.2% a year earlier and FCF margin rose to 31.4% [IS-T, CF-T]; the capital base is growing with continued investment in production and retail capacity per the Q3 2026 call (https://stockanalysis.com/quote/epa/RMS/transcripts/655488-q3-2026-tu/), not a loss of pricing power.",
    "moat": "wide",
    "key_risk": "medium",
    "key_risk_text": "Luxury demand, led by China footfall, keeps slowing (ready-to-wear already negative in Q3 2026, Reuters 2026-10-22), so growth stays far below the 20.6% the price implies and the multiple compresses further.",
    "veto": null
  },
  "thesis": "A wide-moat, net-cash luxury house with stable 41.8% operating margins trades below its own 5-year multiple floor, but the price still implies growth well above the slowing constant-currency run-rate and only sits at the mechanical base fair value.",
  "rationale": "The fall since the last review is the market pricing the Q3 slowdown, not new damage to the business, but it leaves no margin of safety: price at base fair value, reverse DCF far above delivered growth, broken trend. Exceptional quality, not a compelling price: AVOID, watched at base fair value less the margin of safety.",
  "price_at_decision": 1225.50,
  "price_date": "2026-11-20",
  "research_note": "research/EPA-RMS/2026-11-21.md",
  "triggers": [
    {"text": "TTM operating margin falls below 38%, breaking the five-year band of 40.0%-42.9% and showing brand pricing power is eroding.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 38}},
    {"text": "TTM FCF margin falls below 25%, under the FY2024 low of 26.8%, showing capacity investment or inventory is eating cash.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "TTM ROIC falls below 40%, well under the 50.1% now, showing new capital earns structurally lower returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "Revenue growth at constant exchange rates below 3% in the next two quarterly releases, with leather goods turning negative (earnings release)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1508.24, "basis": "China stabilises and growth holds near the Q3 6% constant-currency pace (transcript summary [OV]), taking the price to the blended bull fair value of 1,508.24 [fact sheet fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 1230.29, "basis": "Growth stays near the Q3 pace with the multiple below its 5y floor [RA], so the price holds around the blended base fair value of 1,230.29, weighted lightly as flagged unreliable."},
    "bear": {"probability": 0.25, "target_price_12m": 1029.83, "basis": "Ready-to-wear weakness spreads to leather goods and China footfall falls further (Reuters 2026-10-22; macro overlay yuan drag), taking the price to the blended bear fair value of 1,029.83."}
  },
  "entry_price": 1045.75,
  "entry_basis": "valuation file: base 1,230.29 x 0.85; at that level the price would no longer need growth far above the delivered run-rate.",
  "replaces": null,
  "replacement_reason": null
}
```

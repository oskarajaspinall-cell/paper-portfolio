# Evaluation: Hermès International (EPA:RMS) — 2026-11-09
## Bear case
The de-rating is about growth, not price dislocation. Q3 2026 growth slowed to 6% at constant exchange rates and ready-to-wear and accessories turned negative for the first time in years [Certain] (Reuters, 2026-10-22). China footfall is a named uncertainty and CNY per EUR fell from about 7.61 to about 7.43 in a month, a translation drag (macro overlay) [Likely]. Direction change: ROIC is down 2.5pp and ROCE 2.9pp over 12 months, ROIC 6.9pp below its 2-year high [Certain]; margins are flat, so this is a larger capital base (capacity investment, cash) rather than pricing loss, but returns on new capital are lower [Likely]. Even at 31.7x P/E it trades at a +64% premium to peers, and the reverse DCF needs 23.0% year-1 revenue growth, far above the delivered 6% [Certain]. The mechanical base fair value sits below the price [Certain], though it is flagged unreliable.
## Bull case
Hermès is the clearest wide moat in luxury: rationed supply, in-house craftsmanship and own stores have held operating margin between 40.0% and 42.9% every year since FY2021, 41.8% TTM [Certain]. Net cash (net debt/EBITDA -1.42x), no dilution and FCF margin rising over 12 months to 31.4% [Certain]. Every multiple is below its 5-year minimum: P/E 31.7x vs a 44.9x floor, EV/EBITDA 17.8x vs 28.7x [Certain]. The P/E method alone gives a base of 2,114.48, and growth at 6% constant currency in a sector posting declines suggests share gains [Likely]. A China stabilisation could re-rate it toward the lower end of its own range [Guessing].
## Decision
```json
{
  "ticker": "EPA:RMS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and ROCE fell over the last year while operating margin is flat (41.8% TTM vs 41.2% a year earlier) and FCF margin rose to 31.4% [IS-T, CF-T]; the denominator is growing with continued investment in production and retail capacity per the Q3 2026 call (https://stockanalysis.com/quote/epa/RMS/transcripts/655488-q3-2026-tu/), not a loss of pricing power.",
    "moat": "wide",
    "key_risk": "medium",
    "key_risk_text": "Luxury demand, led by China footfall, keeps slowing (ready-to-wear and accessories already negative in Q3 2026, Reuters 2026-10-22), so growth stays far below the 23.0% the price implies and the multiple compresses further.",
    "veto": null
  },
  "thesis": "A wide-moat, net-cash luxury house with stable 41.8% operating margins trades below its own 5-year multiple floor, but the price still implies growth well above the slowing 6% constant-currency run-rate and sits above the mechanical base fair value.",
  "rationale": "Quality and moat are exceptional, but the valuation is not attractive on its own fundamentals: the base fair value is below the price, the reverse DCF needs far faster growth than delivered, and growth is slowing. Cheap only against its own inflated history. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 1362.50,
  "price_date": "2026-11-06",
  "research_note": "research/EPA-RMS/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 38%, breaking the five-year band of 40.0%-42.9% and showing brand pricing power is eroding.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 38}},
    {"text": "TTM FCF margin falls below 24%, under the FY2024 low of 26.8%, showing capacity investment or inventory is eating cash.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 24}},
    {"text": "TTM ROIC falls below 40%, well under the 50.1% now, showing new capital earns structurally lower returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "Revenue growth at constant exchange rates below 3% in the next two quarterly releases, with leather goods turning negative (earnings release)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1929.11, "basis": "China stabilises and the P/E returns to its 5-year minimum of 44.9x [RA], matching the P/E-method bear value of 1,929.11 in the fact sheet's fair-value section."},
    "base": {"probability": 0.5, "target_price_12m": 1241.13, "basis": "Growth stays near the Q3 2026 6% constant-currency pace (transcript summary [OV]), so the price converges to the blended base fair value of 1,241.13 (DCF 67% + P/E 33%), weighted lightly as flagged unreliable."},
    "bear": {"probability": 0.25, "target_price_12m": 1037.22, "basis": "Ready-to-wear weakness spreads to leather goods and China footfall falls further (Reuters 2026-10-22; macro overlay CNY drag), taking the price to the blended bear fair value of 1,037.22."}
  },
  "entry_price": 992.90,
  "entry_basis": "valuation file: base 1,241.13 x 0.8; at that level the price would no longer need growth far above the delivered run-rate.",
  "replaces": null,
  "replacement_reason": null
}
```

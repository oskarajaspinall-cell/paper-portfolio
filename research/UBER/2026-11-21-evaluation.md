# Evaluation: Uber Technologies (UBER) — 2026-11-21
## Bear case
The price is in a downtrend, not a dip in an uptrend: 12.3% below its 200-day average, -29.1% over 12 months and -33.2pp behind SPY [Certain]. TTM ROIC fell from 16.8% to 14.9%, 5.9pp below its 2-year high, while operating margin rose; the Q3 10-Q shows a $476 million equity revaluation loss and a $342 million rise in legal, tax and regulatory reserves [company-reported] (https://www.sec.gov/Archives/edgar/data/1543151/000154315126000041/uber-20260930.htm), so earnings quality is noisy and reserves can recur [Likely]. The real threat is structural: Waymo, Tesla and Zoox building their own networks could disintermediate the aggregator, and Uber itself says AVs may meaningfully change its industries [company-reported] (same URL) [Likely]. The mechanical bear fair value is negative and the DCF swing is wide, so the valuation anchor is weak [Certain]. Rising real yields and VIX 28.4 pressure a beta-1.31 multiple (macro overlay, context) [Likely].
## Bull case
Operating margin is at its 2-year high of 12.4% and FCF margin 18.4%, both rising or flat on the rolling view; the ROIC dip coincides with one-off revaluation losses and reserves rather than lost share [Likely]. At 12.4x P/FCF and 17.1x EV/EBITDA the stock trades below its own 5-year minimums and 32% and 36% below peers, with an 8.04% FCF yield [Certain]. The reverse DCF implies only 7.8% year-1 revenue growth against bookings growth of 20% in the quarter [company-reported] (https://www.sec.gov/Archives/edgar/data/1543151/000154315126000041/uber-20260930.htm) [Likely]. Shares fell 2.79% YoY on buybacks and net debt/EBITDA is 0.98x [Certain]. Network density in rides and delivery is a real, if not unassailable, advantage, and AV partnerships could make Uber the demand layer rather than the victim [Guessing].
## Decision
```json
{
  "ticker": "UBER",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "TTM ROIC fell 16.8% -> 14.9% [RA-T] while operating margin rose to a 2-year high of 12.4% [IS-T]; the Q3 10-Q attributes the earnings hit to a $476 million equity revaluation loss and a $342 million reserve increase [company-reported] (https://www.sec.gov/Archives/edgar/data/1543151/000154315126000041/uber-20260930.htm), not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Autonomous-vehicle owners (Waymo, Tesla, Zoox) build direct networks and disintermediate Uber's aggregation in top markets.",
    "veto": null
  },
  "thesis": "A cash-generative ride and delivery network with rising operating margins trades below its own 5-year minimum cash multiples, but in a downtrend with an unresolved autonomous-vehicle threat to the moat.",
  "rationale": "The scorecard gives conviction 3: cheap cash multiples and a sound balance sheet, but the price is below its 200-day average (no trend points), ROIC is off its high and the AV threat to a narrow moat is unresolved. The entry hit is a falling price, not an overreaction that clears the bar, so AVOID; cash is acceptable.",
  "price_at_decision": 63.47,
  "price_date": "2026-11-20",
  "research_note": "research/UBER/2026-11-21.md",
  "triggers": [
    {"text": "TTM operating margin falls below 10%, reversing the margin expansion to 12.4%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 14%, showing the cash step-up is not durable.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "TTM ROIC falls below 12%, showing the decline from 16.8% is more than one-off charges.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Trips growth in the 10-Q drops below 8% YoY, or a named AV partner or competitor launches a rival ride network in a top US market without Uber."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 116.88, "basis": "Margins keep rising and AV partnerships keep Uber as the demand layer, so the price reaches the mechanical bull fair value of 116.88 [IS,CF,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 82.35, "basis": "Operating margin holds near 12.4% [IS-T] and the one-off charges fade, so the price converges on the base fair value of 82.35, still below its 5y median P/FCF of 28.1x [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 44.89, "basis": "AV disintermediation fears deepen and reserves recur, so the price falls to the EV/Revenue bear value of 44.89; the negative DCF bear is ignored as an artefact of a wide DCF swing [RA,IS]."}
  },
  "entry_price": 62.0,
  "entry_basis": "Valuation file base 82.35 x 0.85 sits above today's price, so the anchor is instead the level where the value-blend upside clears the scorecard's top discount band, adding the valuation point the same evidence needs for conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

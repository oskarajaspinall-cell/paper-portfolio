# Evaluation: RingCentral, Inc. (RNG) — 2026-11-15
## Bear case
The pullback is not a clean dip to support. The stock has given back the entire post-Q3 jump: it fell from the 98.14 high to 75.39, below where it traded before the beat, so the market has so far rejected the raised guide [Likely]. The trend is stretched: the 50-day sits 48.8% above the 200-day and the close 45.7% above the 200-day (51.74), leaving a long way to mean-revert if momentum breaks [Certain]. The 2:1 target is just the mechanical minimum, below the 98.14 high, with no evidence-based level above it [Certain]. Rolling ROCE fell from 33.0% to 18.5% and ROIC is below its 35.4% high; margins are at 2-year highs, so this looks like a capital-base effect rather than an operating decline [Guessing]. Altman Z 2.22, short interest 8.81% and a 4.7% ATR add gap risk [Certain].
## Bull case
Q3 was a genuine beat with FY26 revenue and EPS guidance raised [Certain]. Operating margin (8.4%) and FCF margin (25.5%) are at their 2-year highs and still rising, ROIC rose over the last year to 24.0%, and shares outstanding are shrinking [Certain]. FCF yield is 10.48% and P/FCF sits near the bottom of its 5y range, so valuation is no crowding risk [Certain]. The price is back near the 50-day average (77.00) with RSI cooled to 46.0, the 70.61 swing low sits above the 66.48 stop, and relative strength versus SPY remains strongly positive over 3 and 6 months [Certain]. The reverse DCF asks for only 4.3% growth [Certain], so a retest toward the 98.14 high is plausible [Likely].
## Decision
```json
{
  "ticker": "RNG",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A strongly trending, cash-generative UCaaS name has pulled back to its 50-day average after a beat-and-raise, but the fade erased the entire earnings reaction, so the pullback edge is unclear.",
  "rationale": "The setup qualifies mechanically, but the full reversal of the post-beat jump reads more like a rejected breakout than a healthy dip, the trend is extended far above its 200-day, and the target only meets the 2:1 minimum with no supporting level above it. Good but not compelling; cash is acceptable.",
  "price_at_decision": 75.39,
  "price_date": "2026-11-13",
  "research_note": "research/RNG/2026-11-15.md",
  "exit_plan": {"target": 93.21, "stop": 66.48, "time_limit": "2027-02-05"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 93.05, "basis": "Raised FY26 guidance and record margins carry the stock back toward the blended bull fair value 93.05 [IS,CF,RA], below the 98.14 high [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 73.46, "basis": "Price settles at the mechanical base fair value 73.46 (DCF 67% + EV/Revenue 33%) as the reverse-DCF 4.3% growth bar is roughly met [IS,RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 54.5, "basis": "Momentum breaks and EV/Sales reverts toward its 5y median 2.2x [RA], i.e. the EV/Revenue base 54.50; the blended bear is negative because the DCF bear is not meaningful, so it is not used."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle for this tactical trade: a deeper fall would take the stock out of the pullback band around its 50-day average and break the setup; the obstacle is the unclear edge after the full reversal of the earnings jump.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: BBB Foods Inc. (TBBB) — 2026-11-07
## Bear case
The stock has already moved a long way. It is up 136.2% over 12 months and +61.3% over 3 months, sits +20.4% above its 50-day average, and its RSI(14) is 76.5, overbought [Certain]. The reaction day's low is far below the close, so the volatility stop (57.18) is 12.8% away. That forces a 2:1 target of 82.50, which needs another large leg up inside 8 weeks, beyond anything the setup itself evidences [Likely]. Valuation is a gap risk: EV/EBITDA is 100.8x against a peer median of 18.3x, base DCF fair value is 33.21, and the price implies 35.3% year-1 revenue growth [Certain]. Any stumble in the store rollout could re-rate the shares fast [Likely]. Net debt/EBITDA is 6.17x, TTM net margin is -2.0% and shares rose 4.22% YoY [Certain].

## Bull case
This is a real operating beat. The Q3 transcript headline describes accelerating revenue, double-digit same-store sales growth, faster EBITDA growth and unchanged opening guidance, after a second strong positive reaction in August [Likely] (https://stockanalysis.com/stocks/tbbb/transcripts/732716-q3-2026/). The 2026-11-03 reaction was +10.5% on 4.0x volume, and 144% of the jump is still held, at the 52-week high with no overhead supply [Certain]. Relative strength against SPY is +65.7pp over 3 months, and the 5y beta of -0.01 makes the trade stock-specific [Certain]. Gross margin is rising (16.5% TTM) and the TTM FCF margin of 4.7% is the best in five years, so the rollout is funding itself [Certain]. The bull DCF value of 88.13 sits above the 82.50 target [Certain].

## Decision
```json
{
  "ticker": "TBBB",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A genuine Q3 beat at a fast-growing Mexican hard discounter, but the drift is already extended and overbought, so a 2:1 target that needs another large leg in 8 weeks is not a clear edge.",
  "rationale": "The setup is real, but the wide reaction-day stop forces a target the evidence only reaches on the bull DCF case, with RSI 76.5 and a 100.8x EV/EBITDA adding gap risk. Reward:risk passes on paper but not on probability. That makes this good, not compelling, so it is an AVOID and cash is the outcome. Macro is context only.",
  "price_at_decision": 65.62,
  "price_date": "2026-11-06",
  "research_note": "research/TBBB/2026-11-07.md",
  "exit_plan": {"target": 82.50, "stop": 57.18, "time_limit": "2027-01-02"},
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 88.13, "basis": "Rollout and same-store momentum keep compounding, as the Q3 transcript describes (/stocks/tbbb/transcripts/732716-q3-2026/), and the price reaches the mechanical bull DCF value of 88.13 [IS,CF,ST]."},
    "base": {"probability": 0.45, "target_price_12m": 62.0, "basis": "Growth roughly delivers the 35.3% year-1 revenue growth the reverse DCF implies [ST] while EV/EBITDA compresses from 100.8x toward peers' 18.3x [RA], leaving the price a little below the current close and well above the base DCF of 33.21 because growth keeps lifting EBITDA."},
    "bear": {"probability": 0.25, "target_price_12m": 33.21, "basis": "A rollout or same-store slowdown de-rates the stock to the base DCF value of 33.21 [IS,CF,ST], with 6.17x net debt/EBITDA [BS,IS] and negative net margin [IS] giving no valuation floor (the bear DCF is negative)."}
  },
  "entry_price": null,
  "entry_basis": "A lower price would not create conviction 4 for this trade: the drift edge expires within 8 weeks, and a close below the 57.69 reaction-day low voids it. A later dip toward the 50-day average would be a new pullback setup, screened mechanically and researched afresh.",
  "replaces": null,
  "replacement_reason": null
}
```

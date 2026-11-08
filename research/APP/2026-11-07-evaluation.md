# Evaluation: AppLovin Corporation (APP) — 2026-11-07
## Bear case
The setup is weaker than the screen suggests. The flagged 2026-11-06 session is follow-through on the prior day's earnings gap, so the stop sits under a second-day low rather than a clean reaction-day low [Likely]. RSI 76.3 and a close 33.4% above the 50-day show the move is extended [Certain]. The 50-day sits 28.3% below the 200-day, so this is a rebound inside a downtrend, with the 200-day at 409.30 and the 437.79 swing high directly overhead [Certain]. The minimum 2:1 target of 486.92 requires breaking both. The honest resistance-based target gives roughly 1:1 [Likely]. Beta 2.50 in a tape where VIX rose 13.2 points in a month adds gap risk (macro overlay) [Certain]. A pending securities class action is an unquantified overhang [Likely]. The price implies 35.8% year-1 growth, against a mechanical base value of 200.36 [Certain].

## Bull case
The beat looks real. Headlines report earnings and guidance ahead, and the stock rose while the Nasdaq-100 fell, so the move is company-specific [Likely]. The fundamentals are exceptional: TTM operating margin 77.8%, ROIC 137.6%, FCF margin 64.4%, near-zero net leverage (0.06x) and a shrinking share count (-1.75%) [Certain]. P/E of 26.2x sits below its own 5y minimum of 37.8x, so the multiple is not crowded on earnings [Certain]. The stock held 100% of the jump on 2.3x volume, which is consistent with institutions still adding [Likely]. After a -36.6% 12-month drawdown, positioning is light and short interest fell 3.9% [Likely]. The edge is not good enough, though. The required target needs a break through two resistance levels inside 8 weeks, which the evidence does not show.

## Decision
```json
{
  "ticker": "APP",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A genuine Q3 beat on exceptional fundamentals, but the drift entry is extended into heavy overhead resistance, so the volatility stop and a 2:1 target are not both supported by the evidence.",
  "rationale": "The honest target is the 437.79 swing high, about 1:1 against the ATR stop at 343.37. Reaching 486.92 needs a break above the 200-day and the August high inside 8 weeks, with RSI 76.3, beta 2.50 and a risk-off tape. The edge is unclear, so we avoid and hold cash.",
  "price_at_decision": 391.22,
  "price_date": "2026-11-06",
  "research_note": "research/APP/2026-11-07.md",
  "exit_plan": {"target": 486.92, "stop": 343.37, "time_limit": "2027-01-02"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 534.79, "basis": "Growth keeps pace with the 35.8% the reverse DCF implies and margins hold at 77.8% operating [IS], reaching the fact sheet's bull fair value of 534.79."},
    "base": {"probability": 0.4, "target_price_12m": 391.22, "basis": "Earnings growth offsets some multiple fade with P/E already below its 5y minimum of 37.8x [RA], so the price holds near 391.22, above the mechanical base of 200.36 because the DCF's fade understates a business with ROIC of 137.6% [RA]."},
    "bear": {"probability": 0.35, "target_price_12m": 200.36, "basis": "Growth slows toward the mechanical base fair value of 200.36 [IS,CF,RA] while a beta-2.50 multiple compresses in a risk-off tape. The bear weight is raised a little for the macro overlay's small bear tilt (research/APP/2026-11-07-macro.md) and the class action (newsfilecorp URL in the note)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

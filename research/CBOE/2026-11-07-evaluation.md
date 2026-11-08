# Evaluation: Cboe Global Markets (CBOE) — 2026-11-07
## Bear case
The drift is already spent. The close of 353.27 sits +18.3% above the 50-day average with RSI 68.1, and the jump is 183% held, so most of the reaction is behind us [Certain]. The volatility-stop at 316.65 puts the risk at 10.4%. A 2:1 trade then needs 426.52, well above the 52-week high of 371.18, which is the only overhead reference the evidence offers [Certain]. A low-beta (0.36) exchange rarely rallies that far in 8 weeks [Likely]. Valuation is a crowding and gap risk: the price is above bull fair value (283.81), and EV/EBITDA 17.6x and P/B 6.2x are above their 5y maxima [Certain]. The VIX spike that lifted volumes may fade, and the CFTC perpetuals challenge plus higher technology costs add regulatory and cost uncertainty [Likely].
## Bull case
The beat is real. Q3 revenue rose 18%, adjusted EPS rose 36% and FY26 organic revenue guidance went up to "high teens" (PRNewswire, TheFly via fact sheet) [Likely]. Operating margin TTM is 36.4% against 32.3% in FY2025, and the FCF margin is 47.9%, so the leverage is showing up in cash [Certain]. On earnings the stock is not stretched: P/E 25.1x is near its 5y low and close to peers' 24.3x, and P/FCF 14.6x is below its 5y minimum [Certain]. The balance sheet is net cash, with Piotroski 7 [Certain]. Elevated volatility (VIX 28.18, macro overlay) supports Q4 volumes [Likely]. Even so, the bull case only supports a retest of 371.18, not the 2:1 level [Guessing].
## Decision
```json
{
  "ticker": "CBOE",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A genuine Q3 beat and raised guidance, but the post-earnings drift is already extended and the 2:1 target sits far above the only evidenced resistance, the 52-week high.",
  "rationale": "The volatility stop at 316.65 implies a 2:1 target of 426.52, well beyond the 371.18 52-week high, with price +18.3% above the 50-day and above bull fair value. The honest target cannot reach 2:1, so per owner rules this is an AVOID. Macro is context only.",
  "price_at_decision": 353.27,
  "price_date": "2026-11-06",
  "research_note": "research/CBOE/2026-11-07.md",
  "exit_plan": {"target": 371.18, "stop": 316.65, "time_limit": "2027-01-02"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 400.0, "basis": "High-teens organic growth guidance (TheFly headline in fact sheet) and a 36.4% TTM operating margin [IS] carry earnings higher while P/E holds near its 5y median 26.4x [RA], above the mechanical bull fair value of 283.81 because that model misses the margin step-up."},
    "base": {"probability": 0.5, "target_price_12m": 340.0, "basis": "Earnings growth is offset by EV/EBITDA drifting back from 17.6x toward its 5y median 16.1x [RA] as the VIX-driven volume boost (macro overlay) normalises; above base fair value 249.92 because the DCF does not capture the 47.9% FCF margin [CF,IS]."},
    "bear": {"probability": 0.25, "target_price_12m": 260.0, "basis": "Volumes fade and regulatory pressure (CFTC perpetuals challenge, PRNewswire 2026-11-03) pushes multiples back to their 5y medians [RA], toward the base fair value of 249.92 and the 52-week low of 227.15 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

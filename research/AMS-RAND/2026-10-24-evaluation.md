# Evaluation: Randstad N.V. (AMS:RAND) — 2026-10-24
## Bear case
The 2:1 plan needs a 49.57 target, well beyond the 52-week high of 42.18. No price history or valuation evidence points to that level [Certain]. The last close of 41.23 is already above base fair value 38.44, and the reverse DCF already prices a flat top line [Certain]. RSI 70.5 and +60.7% over 6 months mean the recovery is crowded, which raises gap risk [Likely]. Adecco rose on the same day, so part of the jump was a sector re-rating rather than a Randstad-specific surprise that could keep drifting [Likely]. The fundamentals are weak: operating margin 2.4% TTM against 4.2% in FY2021, ROIC 6.7%, and net debt/EBITDA up to 2.36x [Certain]. A Q3 beat at a 3.5% EBITA margin is only an early cyclical turn [Likely]. The 4.17 EUR stop distance (10.1%) is wide for a target with no anchor [Certain].
## Bull case
This is a real results beat. Revenue growth of 3.9% and EBITA up 10% YoY, plus management flagging improving trends and a stable sequential gross margin into Q4, are the kind of guidance-led surprise that drifts [Likely]. The reaction came on 3.1x volume and 100% of the jump held, which shows institutional acceptance [Certain]. The price sits near its 3-month high, so there is little overhead supply [Certain]. Valuation still leaves room: EV/EBITDA 10.7x is below its 5y median of 11.5x and well below the peer median of 19.5x, and the FCF yield is 8.86% [Certain]. The DCF bull case of 72.78 shows how much operating leverage a staffing recovery carries [Guessing].
## Decision
```json
{
  "ticker": "AMS:RAND",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A genuine Q3 beat on improving staffing trends, but the price already sits above base fair value at a 52-week high, so the 2:1 drift target has no evidence-backed level behind it.",
  "rationale": "The ATR stop below the reaction-day low makes the minimum 2:1 target 49.57. That is far above the 52-week high and base fair value, so it depends on the bull case within eight weeks. The entry is overbought after a partly sector-wide jump. The honest target does not reach 2:1, so this is an AVOID with no position.",
  "price_at_decision": 41.23,
  "price_date": "2026-10-23",
  "research_note": "research/AMS-RAND/2026-10-24.md",
  "exit_plan": {"target": 49.57, "stop": 37.06, "time_limit": "2026-12-18"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 60.14, "basis": "Improving trends from the Q3 2026 call carry margins back toward the FY2021-22 4.2% operating margin [IS], reaching the mechanical bull fair value of 60.14 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 40.24, "basis": "A modest recovery in line with the DCF base of 40.24 [fact sheet Fair value], with EV/EBITDA near its 5y median of 11.5x [RA]; the reverse DCF's flat growth is roughly what is already priced."},
    "bear": {"probability": 0.25, "target_price_12m": 27.58, "basis": "The cyclical turn stalls, the operating margin stays near 2.4% with net debt/EBITDA of 2.36x [IS,BS], and the price reverts to the mechanical bear fair value of 27.58 [fact sheet Fair value]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

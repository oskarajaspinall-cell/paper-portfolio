# Evaluation: Bangkok Bank PCL (BKK:BBL) — 2026-10-17
## Bear case
The "pullback" looks more like a three-month downtrend than a dip in an uptrend [Likely]: 3-month momentum is -6.3% and relative strength vs SPY over 3m is -8.0pp, against a still-positive 6m/12m record [Certain]. Swing lows are stepping down (186.50, 186.00, then 181.50 on 2026-10-07) and the close of 186.00 is below the 50-day MA of 190.12 [Certain], so the 50-day is a level being lost, not tested. The 198.86 target needs the stock to clear the 198.00 swing high of 2026-09-22, the ceiling of the recent range, with no catalyst before the 19-Jan-2027 results [Likely]. The note itself concedes the setup is a bet on trend continuation, not a re-rating catalyst [Certain]. With 27.0% institutional ownership and 0.13 beta, there is little flow to push it through resistance [Guessing].

## Bull case
The long trend is intact [Certain]: 12-month change +24.0%, 50-day MA 7.9% above the 200-day, positive 6m/12m relative strength, and RSI 45.4 is cooled rather than broken. Volatility is low (ATR 1.4% of price), so the 179.57 stop sits below every recent swing low and is unlikely to be hit by noise [Likely]. The 204.00 three-month high leaves room above the target without assuming a breakout [Certain]. Valuation offers no crowding risk: 8.4x P/E and 0.6x P/B are well below the Thai peer medians of 11.7x and 1.1x, and the reverse DCF implies -7.4% year-1 revenue growth, so there is little gap-down risk from a de-rating [Certain]. No adverse news: the latest headline is a routine credit facility [Likely].

## Decision
```json
{
  "ticker": "BKK:BBL",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A cheap, low-volatility Thai bank in a 12-month uptrend has dipped below its 50-day average, but stepping-down swing lows and negative 3-month relative strength make this a fading range rather than a clean pullback.",
  "rationale": "Reward:risk meets the minimum only on paper: the target must clear the 198.00 swing high that capped September with no catalyst before January results, while lower lows and negative 3-month relative strength weaken the uptrend edge. Good but not compelling; cash is acceptable.",
  "price_at_decision": 186.00,
  "price_date": "2026-10-15",
  "research_note": "research/BKK-BBL/2026-10-17.md",
  "exit_plan": {"target": 198.86, "stop": 179.57, "time_limit": "2027-01-17"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 247.31, "basis": "Blended base fair value (P/B + ROE with FCFE DCF) is reached as ROE holds near its FY2024-25 level of 8.2%-8.4% [RA] and the P/B discount to peers (0.6x vs 1.1x) narrows [RA,P]."},
    "base": {"probability": 0.50, "target_price_12m": 210.01, "basis": "P/B + ROE base value [fair value section]; the FCFE leg is down-weighted because bank FCF swings wildly (FCF margin -347.3% to 155.2% [CF,IS]) and P/B already sits at its 5y max of 0.6x [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 160.30, "basis": "Mechanical bear fair value as TTM ROE of 7.3% slips back from the FY2024 peak of 8.4% [RA] and the dividend discount value of 126.54 [fair value section] anchors sentiment."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the weakness is the setup's edge (lower swing lows, negative 3-month relative strength); a lower price would push it toward the stop zone and break the uptrend rather than improve the trade.",
  "replaces": null,
  "replacement_reason": null
}
```

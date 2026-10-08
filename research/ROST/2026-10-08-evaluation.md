# Evaluation: Ross Stores, Inc. (ROST) — 2026-10-08
## Bear case
This looks less like a healthy dip and more like a failed breakout. The stock has given back the whole 2026-08-20 beat-and-raise reaction: it closed at 225.53, below the 228.05 post-earnings swing low [Certain]. Swing lows are falling (228.05, 224.50, 222.15) and swing highs are lower too (257.00, then 233.45 and 239.73) [Certain]. Six-month relative strength is -17.4pp against SPY [Certain]. To reach the 249.563 target, the stock must get back above the 50-day (236.09) and the 239.73 high within about six weeks, before the 2026-11-19 print [Likely]. EV/EBITDA (19.8x), EV/Sales and P/B are all above their 5y max, and the premium to peers is +12-62%. The overlay shows real yields up 48bp in a month and money rotating into staples. Both raise the risk of de-rating and gaps [Likely].
## Bull case
The long-term trend is intact. The stock is +50.0% over 12 months, the 50-day is +7.9% above the 200-day and price is +3.1% above the 200-day [Certain]. RSI of 40.2 and -4.5% to the 50-day put it inside the pullback band [Certain]. The fundamentals back the trend: the 2026-08-20 quarter was a beat-and-raise (Reuters) [Likely], TTM ROIC is 33.6%, FCF margin is rising to 11.4% and Piotroski F is 8 [Certain]. Ross is gaining traffic share from rivals as shoppers trade down (Barron's, 2026-09-18) [Likely], which partly hedges the same inflation that is pushing yields up [Likely]. P/FCF of 25.8x is below its 5y minimum [Certain]. Short interest is only 3.04% [Certain]. The 257.00 resistance is 2.6x the stop distance away, so reward:risk clears 2:1 [Certain].
## Decision
```json
{
  "ticker": "ROST",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A quality off-price retailer in a 12-month uptrend has pulled back toward its 50-day average, but the dip has erased the post-earnings gain with lower lows while macro pressure builds on a multiple above its 5y range.",
  "rationale": "The setup passes the mechanical filters, but the edge is unclear. Price has broken below the post-earnings swing low with lower highs and lower lows. Six-month relative strength is -17.4pp. The target needs the 50-day and the 239.73 high reclaimed before the November print, while real yields rise against an above-range multiple. Conviction 3, so AVOID; cash is acceptable.",
  "price_at_decision": 225.53,
  "price_date": "2026-10-07",
  "research_note": "research/ROST/2026-10-08.md",
  "exit_plan": {"target": 249.56, "stop": 213.51, "time_limit": "2026-11-18"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 250.9, "basis": "Comps and share gains (Barron's 2026-09-18) re-rate P/FCF from 25.8x to its 5y median 28.7x [RA] on TTM FCF, back toward the 257.00 52-week high [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 225.5, "basis": "The multiple holds at 27.3x P/E [RA] on flat TTM earnings: P/FCF below its 5y min (25.8x vs 27.6x) offsets EV/EBITDA above its 5y max (19.8x vs 19.3x) [RA]."},
    "bear": {"probability": 0.3, "target_price_12m": 201.6, "basis": "Rising real yields and the rotation into staples (macro overlay 2026-10-08, small tilt toward bear, which lifted this probability) compress P/E from 27.3x to the 24.4x peer median [RA,P:TJX,P:BURL,P:DLTR]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

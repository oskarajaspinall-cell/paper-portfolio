# Evaluation: Hasbro, Inc. (HAS) — 2026-10-24
## Bear case
The trade is late and the plan does not work. The stop from the reaction-day low (101.4 less 0.25 x ATR 3.424) sits about 14.4% below the close, so the 2:1 target lands near 151.2, above even the bull fair value of 132.40 [Certain]. RSI(14) of 87.5 and a close +25.0% over the 50-day MA mean the drift is largely spent; the stock already holds 172% of the jump [Certain]. Base fair value 102.12 is below the price and EV/Sales sits above its 5y max, so a gap back toward the reaction-day range is plausible [Likely]. Short interest rose 14.2% on the month [Certain]. No nearby support: the nearest swing low is 85.37 [Certain].
## Bull case
The beat is real: Q3 revenue grew on Magic: The Gathering, management raised full-year revenue and EBITDA outlooks and doubled the buyback target (https://www.reuters.com/technology/hasbro-raises-annual-revenue-forecast-strong-demand-digital-games-toys-2026-10-20/; https://www.barrons.com/articles/hasbro-earnings-stock-price-c1e76416) [Likely]. Quality is rising: ROIC 34.0%, operating margin 25.9%, FCF margin 23.7%, net debt/EBITDA down to 1.42x [Certain]. P/E 17.5x is below its 5y minimum and the reverse DCF implies -2.1% year-1 growth, so post-earnings drift could carry further into the holiday season [Likely]. Relative strength vs SPY is +31.5pp over 3m [Certain].
## Decision
```json
{
  "ticker": "HAS",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A genuine Magic-led Q3 beat and raised outlook, but the stock is extremely overbought and the volatility stop is so far away that no supportable target reaches 2:1.",
  "rationale": "The drift setup qualifies, but the honest target (bull fair value 132.40) is well short of the roughly 151.2 needed for 2:1 against a stop near 100.54; RSI 87.5 adds gap risk. The trade fails the reward:risk rule, so no position.",
  "price_at_decision": 117.44,
  "price_date": "2026-10-23",
  "research_note": "research/HAS/2026-10-24.md",
  "exit_plan": {"target": 132.40, "stop": 100.54, "time_limit": "2026-12-19"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 132.40, "basis": "Raised outlook and Magic strength sustain rising ROIC (34.0% TTM [RA]), lifting the price to the bull fair value of 132.40 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 115.54, "basis": "Momentum fades and the price settles at the DCF base value of 115.54 [fact sheet Fair value], above the blended base of 102.12 because the margin step-up (operating margin 25.9% TTM [IS]) looks durable."},
    "bear": {"probability": 0.30, "target_price_12m": 75.27, "basis": "Holiday demand or Magic sales disappoint and the stock de-rates to the EV/EBITDA method's base value of 75.27 [fact sheet Fair value], with no support above the 85.37 swing low [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2 on the trade; no entry price required.",
  "replaces": null,
  "replacement_reason": null
}
```

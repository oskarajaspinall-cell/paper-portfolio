# Evaluation: Swancor Advanced Materials Co., Ltd. (SHA:688585) — 2026-11-07
## Bear case
The "drift" has no evidenced results beat behind it: TTM operating margin is -25.2% and net margin -25.6% against 4.0% and 2.3% in FY2025, with ROIC at -137.3% [IS,RA] [Certain]. The 2026-11-05 reaction (+6.8% on 2.2x volume) barely clears the screen thresholds and no news or guidance is available, so the move looks sentiment-led [Likely]. Valuation is a gap risk: EV/Sales 41.6x and P/B 78.0x sit far above their 5y maxima of 28.4x and 38.0x and peer medians of 3.0x and 1.8x [RA] [Certain]. The volatility stop at 157.55 is 12.5% below the close (ATR 22.14, 12.3%), and the 2:1 minimum target of 224.97 sits above the 52-week high of 223.24 after a +75.0% year, so the required reward is not supported [Likely]. Piotroski F 3, net debt/EBITDA back to 1.95x and institutions owning only 2.4% add fragility [ST] [Certain].
## Bull case
Momentum is strong: +39.2% over 6 months, relative strength vs SPY +39.0pp, and the price is 27.0% above its 50-day average with RSI 64.5, not yet overbought [HI,ST] [Certain]. The reaction day held 74% of its jump, consistent with buyers still absorbing news [Likely]. The stock previously traded at 223.24 in May, so a retest is not unprecedented for a name with ATR of 12.3% [HI] [Guessing]. Losses could be a one-off charge, given positive FY gross margins (13.8% TTM) [IS] [Guessing].
## Decision
```json
{
  "ticker": "SHA:688585",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A thin, unexplained post-results jump in a loss-making stock at extreme multiples, where the volatility stop is wide and the required 2:1 target sits above the 52-week high, offers no clear drift edge.",
  "rationale": "No evidenced earnings beat (TTM margins collapsed to losses), a barely-qualifying reaction, and a minimum target above the 52-week high make the reward:risk unsupported; extreme EV/Sales and P/B add gap risk. Conviction 2: AVOID, no position.",
  "price_at_decision": 180.02,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-688585/2026-11-07.md",
  "exit_plan": {"target": 223.24, "stop": 157.546, "time_limit": "2026-12-31"},
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 223.24, "basis": "Momentum (+39.2% 6m [HI]) carries the price back to its 52-week high of 223.24 [HI]; no fair value is computable (negative FCF and EBITDA), so targets are anchored on price history."},
    "base": {"probability": 0.45, "target_price_12m": 142.58, "basis": "With TTM operating margin at -25.2% [IS] and EV/Sales of 41.6x far above its 5y max [RA], the sentiment premium fades back toward the 200-day average of 142.58 [ST,HI]; fair value is [data unavailable]."},
    "bear": {"probability": 0.35, "target_price_12m": 93.01, "basis": "Continued losses (ROIC -137.3% [RA], Piotroski F 3 [ST]) and multiples reverting toward peers (P/B peer median 1.8x [RA]) take the price back to its 52-week low of 93.01 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: no entry price required; the obstacle is the absence of an evidenced results beat and loss-making fundamentals, not price.",
  "replaces": null,
  "replacement_reason": null
}
```

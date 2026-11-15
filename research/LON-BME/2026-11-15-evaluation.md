# Evaluation: B&M European Value Retail (LON:BME) — 2026-11-15
## Bear case
The drift rule puts the stop at 300.17 GBX, below the reaction-day low of 303.344. That is 14.5% of risk, so the trade needs +29% (452.66) in 8 weeks to reach 2:1 [Certain]. The entry is already stretched: RSI 82.3, +33.3% over the 50-day and +67.2% over the 200-day, +114.0% over 12 months, closing at the 52-week high [Certain]. A pullback toward the gap before any drift is the likelier path [Likely]. P/E of 18.1x is above its 5y maximum of 14.9x, so the target needs estimate upgrades as well as a re-rating [Likely]. Fundamentals are still weak: TTM operating margin 6.9% vs 10.2% at the 2-year high, ROCE down 3.4pp in a year, leverage 4.08x [Certain]. The H2 weighting of investment leaves the margin repair unproven until full-year results [Likely]. Macro is context only: SONIA rising is a mild headwind with this leverage (macro overlay) [Likely].
## Bull case
This is a real results catalyst, not noise. The stock closed +20.9% on 4.6x volume and held 123% of the jump [Certain]. UK like-for-likes turned positive in Q2 after July's decline, France and Heron grew, and FY EBITDA guidance of GBP 450m-500m sits around last year's £459m adjusted EBITDA (transcript summary) [Likely]. Cash backs the story: FCF margin is rising (11.7% TTM, its 2-year high), FCF yield is 19.46% and P/FCF of 5.1x sits at 21% of its 5y range [Certain]. EV/EBITDA of 7.9x is near the bottom of its own range [Certain]. A Poundland site pickup could add upside [Guessing]. There is no overhead resistance [Certain], and relative strength vs SPY is +52.0pp over 3m [Certain].
## Decision
```json
{
  "ticker": "LON:BME",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A genuine H1 turn in UK like-for-likes triggered a post-earnings drift setup, but the entry is overextended and the volatility stop sits so far below that the 2:1 target needs a further re-rating from a P/E already above its 5-year maximum.",
  "rationale": "The setup is real, but reward:risk only works on paper. The 452.66 target is the bare 2:1 minimum, not a level the evidence supports. With RSI 82.3 and the price far above its averages, the 14.5% stop is likely to be tested before any drift. The edge is unclear, so we avoid.",
  "price_at_decision": 351.00,
  "price_date": "2026-11-13",
  "research_note": "research/LON-BME/2026-11-15.md",
  "exit_plan": {"target": 452.66, "stop": 300.17, "time_limit": "2027-01-10"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 452.66, "basis": "Margin repair continues toward the 10.2% 2-year-high operating margin [IS-T] and guidance is met, on top of the 19.46% FCF yield [ST]; this is the drift target from the note."},
    "base": {"probability": 0.45, "target_price_12m": 351.00, "basis": "The price holds near the close: P/E 18.1x is already above its 5y max [RA] while P/FCF 5.1x sits low in its range [RA], so earnings recovery and the de-rating offset each other."},
    "bear": {"probability": 0.30, "target_price_12m": 263.24, "basis": "The extended move (RSI 82.3 [ST], +33.3% over the 50-day [ST,HI]) mean-reverts to the 50-day average if H2 refit investment delays margin repair with leverage at 4.08x [BS,IS]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not a clean obstacle. A fall toward 303.344 would test the reaction-day low and break the drift setup rather than improve it. No fair value is computable [valuation file], and the setup expires in the drift window.",
  "replaces": null,
  "replacement_reason": null
}
```

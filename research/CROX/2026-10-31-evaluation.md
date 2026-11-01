# Evaluation: Crocs, Inc. (CROX) — 2026-10-31
## Bear case
The trade's edge is mostly spent. The stock closed +25.5% on 2026-10-29 and then rose again to 150.52, so it now sits +25.0% over its 50-day average with RSI 77.7 [Certain]. A gap that large leaves the volatility stop 137.77 a long way below the price (risk 12.75 per share, 8.5%) [Certain]. The only target the evidence supports, 177.00 just under base fair value 178.19, clears the minimum 2:1 by a hair [Certain]. P/E of 11.3x is already 81% of the way up its 5y range (6.7x-12.4x), so the re-rating has happened [Certain]. Beta 1.50 makes a market wobble a likely gap through the stop [Likely]. HEYDUDE's recovery is one quarter old and unproven [Guessing]. The FY2025 negative ROIC and net margin have no confirmed cause [Guessing].
## Bull case
This is a real beat and raise: Q3 growth at both brands, HEYDUDE back to growth and a third consecutive full-year guidance raise (https://www.prnewswire.com/news-releases/crocs-inc-reports-strong-third-quarter-2026-results-raises-full-year-2026-outlook-302922644.html) [Likely]. The reaction came on 4.6x volume and 101% of the jump was held, with the close at the 52-week high of 154.05, so there is no overhead supply [Certain]. Quality is sound: Piotroski F 8, Altman Z 4.12, FCF yield 10.96%, TTM FCF conversion 113.5% [Certain]. The reverse DCF still implies -0.8% revenue growth and EV/EBITDA of 8.3x is below the peer median of 11.1x [Certain]. Short interest of 9.86% of float could add buying pressure [Guessing]. Shares down 10.71% YoY show buybacks supporting the stock [Certain].
## Decision
```json
{
  "ticker": "CROX",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A genuine Q3 beat and third full-year raise make CROX a valid post-earnings drift setup, but after a +25.5% gap and a further rise the honest target near base fair value only just clears 2:1 against an ATR stop far below the price.",
  "rationale": "The setup qualifies, but the edge is thin: reward:risk barely above the minimum, a target capped by base fair value, RSI 77.7 and the stock far above its 50-day average, with a high-beta gap risk through a distant stop. Good but not compelling, so AVOID; a pullback holding above the reaction-day low would improve the plan.",
  "price_at_decision": 150.52,
  "price_date": "2026-10-30",
  "research_note": "research/CROX/2026-10-31.md",
  "exit_plan": {"target": 177.00, "stop": 137.77, "time_limit": "2026-12-24"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 208.89, "basis": "HEYDUDE recovery and repeated guidance raises sustain growth so the DCF base value of 208.89 [IS,CF] is earned, against a reverse DCF that implies -0.8% growth (fact sheet Fair value)."},
    "base": {"probability": 0.45, "target_price_12m": 178.19, "basis": "Raised FY26 outlook holds and the stock settles at the blended base fair value 178.19 [IS,BS,CF,RA,ST,HI], consistent with EV/EBITDA 8.3x staying below the 11.1x peer median [RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 116.78, "basis": "HEYDUDE stalls and P/E of 11.3x, already 81% up its 5y range, reverts toward the 8.8x median, in line with the P/E-method base 116.78 [RA,IS]."}
  },
  "entry_price": 142.55,
  "entry_basis": "From the valuation file: base 178.19 x 0.8; a pullback to this level while above the 137.77 drift stop would give the same evidence a clearly better reward:risk to the 177.00 target.",
  "replaces": null,
  "replacement_reason": null
}
```

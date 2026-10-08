# Evaluation: Cboe Global Markets, Inc. (CBOE) — 2026-10-08
## Bear case
The "cheap" signal rests on peak margins. TTM operating margin of 36.0% and net margin of 26.7% are five-year highs [Certain] [IS], driven by volume-sensitive transaction revenue [Likely]. On EBITDA the stock is mid-range (EV/EBITDA 14.8x, 45% of its 5y range) and EV/Sales of 5.7x sits above its 5y maximum [Certain] [RA], so only P/E and P/FCF look cheap, and only because earnings are elevated. The macro overlay shows a low, cooling VIX (15.01, -1.12 over 3m) and rising real yields [Certain] (research/CBOE/2026-10-08-macro.md). Falling volatility would cut volumes and margins together [Likely]. Kalshi is contesting Cboe's KPI and event-contract launches at the SEC, a regulatory overhang on its main new growth line [Likely]. The 52-week range of 371.18 to 227.15 [HI] shows earnings sensitivity can swing the price hard despite a beta of 0.41 [Certain].
## Bull case
This is a structural-moat exchange: SPX and VIX options are proprietary [Likely]. ROIC rose from 12.7% to 26.9% TTM and FCF margin from 15.6% to 37.0% [Certain] [RA, CF]. FCF conversion has exceeded 100% every year (138.5% TTM) [Certain]. The balance sheet is net cash (-0.40x net debt/EBITDA) [Certain] [RA]. P/E of 22.0x is below its 5y minimum of 24.0x, P/FCF of 15.7x sits at the bottom of its range and is 37% below peers, and the FCF yield is 6.38% [Certain] [RA, ST]. The 19% dividend increase and the Cboe Australia sale point to disciplined capital recycling toward derivatives, data and clearing [Certain] (prnewswire.com). A volatility spike would flow through at high incremental margins [Likely].
## Decision
```json
{
  "ticker": "CBOE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, rising-ROIC proprietary-derivatives exchange looks cheap on P/E and P/FCF, but that cheapness relies on record, volume-driven margins, while EV/EBITDA is only mid-range and EV/Sales sits above its 5-year maximum.",
  "rationale": "The business quality is clear, but the valuation discount exists only on peak-margin earnings. EV/EBITDA is mid-range and EV/Sales is above its 5-year maximum. A low and falling VIX, rising real yields and the Kalshi/SEC overhang make this good but not compelling. Conviction 3 is below the buy threshold, so AVOID and keep the cash.",
  "price_at_decision": 281.57,
  "price_date": "2026-10-07",
  "research_note": "research/CBOE/2026-10-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 28%, under the FY2024 level of 28.9%, showing the margin step-up was cyclical volume, not structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "TTM ROIC falls below 15%, reversing the five-year improvement from 12.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 25%, under the FY2024 level of 25.4%, showing cash generation reverted with volumes.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "The SEC blocks or materially delays Cboe's KPI/event-contract launches following Kalshi's objection, as disclosed by Cboe on cboe.com or in an SEC filing."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 338, "basis": "Margins hold and P/E re-rates from 22.0x to its 5y median of 26.4x [RA] on unchanged TTM earnings [IS], helped by the overlay's volatility-spike upside; bull probability trimmed for the overlay's small bear tilt."},
    "base": {"probability": 0.45, "target_price_12m": 292, "basis": "Multiples hold near P/FCF 15.7x [RA] with the 6.38% FCF yield [ST] and dividend growth supporting a modest gain, as recurring data and clearing offset a cooling VIX."},
    "bear": {"probability": 0.30, "target_price_12m": 226, "basis": "Low and falling VIX (macro overlay research/CBOE/2026-10-08-macro.md; small bear tilt adds probability here) pushes operating margin back from 36.0% to the FY2024 level of 28.9% [IS] at an unchanged 22.0x P/E [RA], close to the 52-week low of 227.15 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

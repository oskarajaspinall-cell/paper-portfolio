# Evaluation: Corpay, Inc. (CPAY) — 2026-10-11
## Bear case
The stock has already re-rated: P/E 24.2x is above its own 5y max of 23.5x [Certain] [RA], P/B 7.4x sits at 95% of its range, and the price is +36.1% over 12 months [Certain] [ST]. Earnings quality is drifting: net margin fell 6.0pp over 5y to 22.7% and FCF margin 9.6pp to 32.6% [Certain] [IS,CF]. Leverage of 2.70x net debt/EBITDA (3.23x FY2025) funds M&A and buybacks [Certain] [RA], and Altman Z of 1.52 flags it [Certain] [ST]. The macro overlay tilts toward bear: a 10y Treasury at 5.22% with rising real yields and HY spreads pressures a premium, leveraged multiple [Likely] (research/CPAY/2026-10-11-macro.md). The FTC settlement terms are undisclosed, so residual compliance cost is unknown [Guessing]. Short interest rose 24.1% in a month [Certain] [ST]. Base fair value is only +13.4% away: thin margin of safety [Certain].
## Bull case
This is a high-quality, asset-light payments franchise: gross margin 80.5%, operating margin 49.0% and rising (+3.5pp over 5y), ROCE 21.8% [Certain] [IS,RA]. Q2 2026 revenue grew 21% with cash EPS up 36% and guidance raised [Likely] (https://stockanalysis.com/stocks/cpay/transcripts/662696-q2-2026/). The reverse DCF implies just 3.3% year-1 revenue growth [Certain] [fact sheet], far below delivery. EV/EBITDA 12.0x sits at 22% of its 5y range, below the 13.7x median, and P/FCF 15.9x is under its median and 10% below peers [Certain] [RA]. FCF yield is 6.27% and shares fell 3.27% YoY [Certain] [ST]. The FTC settlement removes a long-running overhang [Likely] (https://www.businesswire.com/news/home/20260917736158/en/Corpay-Agrees-to-Settle-FTC-Matter/).
## Decision
```json
{
  "ticker": "CPAY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-margin, 21.8%-ROCE B2B payments franchise growing fast, but priced above its own 5-year P/E range with leverage, falling net and FCF margins and a macro headwind, leaving too little margin of safety for a high-conviction buy.",
  "rationale": "Quality and growth are real, but P/E sits above its 5y max, base fair value is only 13.4% above the price, leverage is 2.70x with Altman Z 1.52, and net/FCF margins are trending down. Macro tilts toward bear. Good but not compelling: conviction 3, AVOID; revisit nearer the 20% margin-of-safety entry price.",
  "price_at_decision": 397.92,
  "price_date": "2026-10-09",
  "research_note": "research/CPAY/2026-10-11.md",
  "triggers": [
    {"text": "Net debt/EBITDA rises above 3.5x (vs 2.70x TTM, 3.23x FY2025), showing M&A/buybacks are outrunning earnings.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}},
    {"text": "TTM operating margin falls below 44%, the FY2023 level, breaking the 5-year expansion to 49.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 44}},
    {"text": "TTM FCF margin falls below 25%, extending the 5-year decline from 38.3% to 32.6%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "A further FTC or other regulatory action against Corpay's marketing or disclosure practices beyond the proposed September 2026 settlement, disclosed in an SEC filing or company release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 480, "basis": "Growth near the 21% Q2 2026 pace (transcript) re-rates EV/EBITDA from 12.0x toward its 13.7x 5y median [RA], close to the DCF base of 477.45; below the 824.33 blended bull because that DCF bull extrapolates growth for a decade."},
    "base": {"probability": 0.45, "target_price_12m": 425, "basis": "Earnings grow at a constant 12.0x EV/EBITDA [RA] toward the 6-month high of 427.46 [HI], a little under the 451.17 base fair value because P/E is already above its 5y max of 23.5x [RA]; probability shaded down for the overlay's small bear tilt (research/CPAY/2026-10-11-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 300, "basis": "Rising real yields and HY spreads compress the premium multiple on 2.70x leverage (macro overlay, small bear tilt raises this probability) toward the EV/Revenue bear value of 303.15 and the 6-month low of 297.70 [HI]; above the 188.13 blended bear since margins and FCF hold."}
  },
  "entry_price": 360.94,
  "entry_basis": "valuation file: base 451.17 x 0.8 (20% margin of safety); at that level EV/EBITDA would sit near its 5y low of 11.2x [RA] and the quality case would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

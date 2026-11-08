# Evaluation: Otis Worldwide Corporation (OTIS) — 2026-11-08
## Bear case
The re-rating has happened: at 78.96 the price now sits above the base fair value of 70.99 and the bull of 71.64, and implies 6.7% year-1 revenue growth, about what Q3's 6% organic growth delivers [Certain]. Earnings are not following sales: adjusted EPS was flat in Q3 and TTM operating margin fell from 16.5% to 15.5% (Direction change), with Q3 gross margin down 120bp on labour and material costs [company-reported] (https://www.sec.gov/Archives/edgar/data/1781335/000178133526000127/otis-20260930.htm); that sits just above the 15.2% FY2021 low [Likely]. ROIC and ROCE are far below their 2024 highs of 95.6% and 107.5%; those peaks were distortions of a small capital base, but they flatter quality [Likely]. Leverage has risen to 3.12x net debt/EBITDA, so buybacks are partly debt-funded [Likely]. China is about one fifth of New Equipment sales [company-reported]; the macro overlay rates this small for group earnings (context weight) [Likely]. CEO succession lands in H1 2027 [Certain].

## Bull case
Service is 65% of sales and about 91% of segment profit [company-reported] (https://www.sec.gov/Archives/edgar/data/1781335/000178133526000011/otis-20251231.htm): an installed-base annuity [Likely]. Q3 showed 20% modernization growth and New Equipment back to growth, with FY26 guidance held [Certain]. The FCF margin Direction change is favourable: 11.1% TTM from 9.2%, FCF conversion 107.5% [Certain]. ROIC is up 6.8pp on a year earlier, so the gap to the 2024 high is an outlier base effect, not erosion [Likely]. Every multiple is still below its 5y minimum (P/E 19.6x vs 22.5x; EV/EBITDA 15.1x vs 16.4x) and below the peer median, and the EV/EBITDA method gives 92.18 [Certain]. Shares shrink 2.60% a year [Certain].

## Decision
```json
{
  "ticker": "OTIS",
  "decision": "TRIM",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A service-led elevator franchise with high and recovering returns and improving cash conversion still trades below its own 5-year multiple range, but after the rebound the price sits above the mechanical fair value while operating margin is falling and leverage rising, leaving a balanced rather than compelling skew.",
  "rationale": "The quality thesis holds (Service annuity, FCF recovery, guidance held), but the price has rebounded above base fair value, implies growth in line with delivery, and the operating margin is falling toward its trigger with flat EPS and higher leverage. Expected value sits near the price: conviction 3, trimmed to the conviction-3 size.",
  "price_at_decision": 78.96,
  "price_date": "2026-11-06",
  "research_note": "research/OTIS/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2021 5-year low of 15.2% (15.5% now), showing the labour and material cost squeeze is structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15.2}},
    {"text": "TTM FCF margin falls below the FY2025 5-year low of 10.0% (11.1% now), showing the cash recovery was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10.0}},
    {"text": "Net debt/EBITDA on the ratios page rises above 3.5x (3.12x TTM now), showing capital returns are outrunning cash generation."},
    {"text": "Service organic sales growth in the 10-Q MD&A falls below 3% in any quarter, or FY26 adjusted free cash flow guidance is cut below 1.4bn USD."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 92.0, "basis": "Service-led growth and margin recovery let the multiple return toward its 5y EV/EBITDA minimum of 16.4x [RA], in line with the EV/EBITDA fair value of 92.18 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 76.0, "basis": "Organic growth near Q3's 6% with FY26 guidance held (Q3 2026 transcript [OV]) and margin flat near 15.5% [IS-T]; set above the blended base of 70.99 because the DCF leg of 60.40 ignores the FCF recovery to 11.1% [CF-T], but below the price as EPS is flat."},
    "bear": {"probability": 0.25, "target_price_12m": 56.96, "basis": "The cost squeeze (Q3 gross margin down 120bp [company-reported], 10-Q) pushes operating margin through 15.2% [IS] while leverage rises from 3.12x [RA]: the mechanical bear fair value of 56.96 [fact sheet Fair value]."}
  },
  "entry_price": 56.79,
  "entry_basis": "valuation file: base 70.99 x 0.8; at that price the same Service-led evidence and FCF recovery would justify conviction 4 despite the margin squeeze.",
  "replaces": null,
  "replacement_reason": null
}
```

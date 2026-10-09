# Evaluation: VICI Properties Inc. (VICI) — 2026-10-09
## Bear case
The macro overlay carries primary weight and tilts moderately toward bear. The 10y real yield is 2.92% and has risen +0.61pp over 3 months, with the trend still rising [Certain]. Cap rates and VICI's multiple are direct functions of that rate [Likely]. Net debt/EBITDA has risen from 3.47x to 4.90x [Certain], so higher refinancing costs eat into FFO growth while the escalators are fixed [Likely]. Caesars and MGM pay 74% of rent [Certain]. VICI's EV/EBITDA is also 17% below its peers' median, a stock-specific discount the note never explains [Certain]; tenant-credit worry is the obvious candidate [Guessing]. Data is thin: margins, FFO and P/FCF are all [data unavailable], and Piotroski F is only 3 [Certain]. The 50-day average is 8.3% below the 200-day, RS vs SPY is -44.4pp, and Q3 results are due Oct 28 [Certain].
## Bull case
Every multiple is below its 5y minimum: P/E 8.8x, EV/EBITDA 11.7x vs a 13.1x floor, P/B 0.9x [Certain]. FCF yield is 10.42% [Certain]. ROIC (7.7%) and ROE (9.8%) are flat over five years [Certain], so the de-rating comes from rates, not from the business [Likely]. The mechanical fair value is 27.89 bear, 33.78 base and 48.02 bull vs a 22.79 close, so even the bear case implies +22% [Certain]. Leases run 15-32 years, 15 of 17 are CPI-linked and tenants bear property costs [Certain], which makes rent highly visible [Likely]. Beta is 0.67 and short interest is 2.46% [Certain]. If real yields roll over, the multiple could re-rate toward its 5y median of 15.1x [Guessing].
## Decision
```json
{
  "ticker": "VICI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A triple-net gaming REIT with flat returns trades below its own 5-year minimum multiples and at a peer discount, but the de-rating tracks still-rising real yields and unexplained tenant-concentration risk rather than a mispricing we can confirm.",
  "rationale": "Valuation is compelling but the dominant driver, real yields, is still rising (primary macro tilt toward bear). The 17% peer discount is unexplained, leverage has risen, and margin/FFO data are unavailable. Good but not compelling: conviction 3 is below the buy threshold, so AVOID and revisit after Q3 results.",
  "price_at_decision": 22.79,
  "price_date": "2026-10-08",
  "research_note": "research/VICI/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 6% (now 7.7%), showing rent escalators no longer cover the cost of capital.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 6}},
    {"text": "TTM ROE falls below 7% (now 9.8%), showing financing costs are overtaking rent growth.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 7}},
    {"text": "Net debt/EBITDA (site definition, ratios page) rises above 6.0x from 4.82x, threatening the investment-grade cost of capital."},
    {"text": "Q3 2026 results (Oct 28, 2026) or a 10-Q disclose rent deferral, lease restructuring or rent-coverage deterioration at Caesars or MGM, which together pay 74% of rent."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 33.78, "basis": "Real yields roll over (overlay macro_bull, research/VICI/2026-10-09-macro.md) and EV/EBITDA re-rates toward its 15.1x 5y median [RA], which on net debt/EBITDA of 4.90x [BS,IS] lands at the mechanical base fair value of 33.78; this stops short of the 48.02 bull because the overlay's moderate bear tilt argues against a full re-rating."},
    "base": {"probability": 0.45, "target_price_12m": 25.5, "basis": "Flat ROIC/ROE [RA] support a partial re-rating of EV/EBITDA from 11.7x to about 12.5x, still below the 13.1x 5y minimum [RA]; this sits below the 27.89 fair-value bear because the overlay (primary weight, moderate tilt toward bear) holds the multiple down while DFII10 is still rising."},
    "bear": {"probability": 0.35, "target_price_12m": 19.4, "basis": "Real yields extend higher (overlay macro_bear; DFII10 +0.61pp/3m) and tenant-concentration fears (Caesars+MGM 74% of rent, 10-K) cut EV/EBITDA by about one turn from 11.7x [RA] on 4.90x net leverage [BS,IS]; probability raised a moderate amount for the overlay's bear tilt."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

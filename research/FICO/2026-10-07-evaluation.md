# Evaluation: Fair Isaac Corporation (FICO) — 2026-10-07
## Bear case
The cheapness is a reaction to news that the trailing numbers have not caught up with yet. The FHFA mortgage-pricing simplification on 2026-10-01 goes straight at the mortgage Scores toll-booth. It drove a >20% drop and is not resolved [Likely]. Bureau-distributed Scores were 51% of FY2025 revenue, and the three bureaus own VantageScore, a competing score [Certain]. The trailing ROIC of 65.0% and operating margin of 52.1% therefore describe the old regime, not the new one [Likely]. Net debt/EBITDA is 4.23x, up from 2.60x, so buybacks have been funded with debt that a fall in Scores pricing would expose [Certain]. Short interest is 9.28% and rose 8.0% in a month [Certain]. The macro overlay tilts toward the bear case: higher real yields hold back both origination volumes and the multiple [Likely]. A 15% headcount cut points to defensive restructuring [Guessing].

## Bull case
FICO is a franchise with 85.1% gross margin, 41.6% FCF margin and ROIC that has doubled since FY2021 [Certain]. At 695.46 the shares trade at 19.6x P/E, 16.1x EV/EBITDA and 15.1x P/FCF. That is 10-13% below FICO's own 5-year minimums, 23% below the peer median on P/E and a 6.63% FCF yield [Certain]. Under 12 CFR Part 1254, the FHFA must validate any replacement score for GSE mortgages, so displacement is slow and procedural [Certain]. UWM, the largest mortgage lender, has just reaffirmed FICO on all credit pulls [Certain]. The share count is shrinking 4.5% a year [Certain]. Software and non-mortgage Scores are untouched by the FHFA action [Likely]. If the regulatory outcome turns out milder than feared, a return to even the 5-year trough P/E means about 40% upside [Likely].

## Decision
```json
{
  "ticker": "FICO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A 65%-ROIC credit-scoring franchise trades below its own 5-year minimum multiples, but the discount reflects an unresolved FHFA/VantageScore threat to the mortgage Scores moat that the trailing financials cannot yet show, on a balance sheet levered at 4.23x net debt/EBITDA.",
  "rationale": "Valuation is compelling only if the regulatory moat holds. That is unresolved and binary, and the trailing data predates the shock. Rising leverage, growing short interest and the overlay's moderate bear tilt from rates add downside. Conviction 3 is below the buy threshold. Cash is preferred until the FHFA outcome and the Nov 4 results show how much Scores economics have changed.",
  "price_at_decision": 695.46,
  "price_date": "2026-10-06",
  "research_note": "research/FICO/2026-10-07.md",
  "triggers": [
    {"text": "TTM ROIC falls below 35%, near its FY2021 level of 32.3%, showing the regulatory moat is eroding in the reported economics.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 35}},
    {"text": "TTM gross margin falls below 75%, below the 5-year range low of 74.7%-79.7%, indicating loss of Scores pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 75}},
    {"text": "Debt/EBITDA rises above 5x, meaning leverage is outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 5}},
    {"text": "FHFA/GSEs formally adopt VantageScore alongside or instead of FICO Score for conforming mortgages, or formally confirm FICO's role, as disclosed in an SEC filing or FHFA release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 990, "basis": "FHFA risk resolves mildly and P/E re-rates to its 5-year minimum of 27.9x from 19.6x on unchanged TTM earnings [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 705, "basis": "The regulatory overhang persists and EV/EBITDA holds near the peer median of 16.3x vs 16.1x now [RA, P:MCO/SPGI/VRSK/EFX]; probability cut from a symmetric split by the macro overlay's moderate bear tilt (research/FICO/2026-10-07-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 505, "basis": "The FHFA action erodes mortgage Scores pricing, FCF margin falls from 41.6% to its FY2023 level of 30.3% [CF,IS] at an unchanged 15.1x P/FCF [RA]; probability raised by the overlay's moderate bear tilt from higher real yields and weak origination (research/FICO/2026-10-07-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

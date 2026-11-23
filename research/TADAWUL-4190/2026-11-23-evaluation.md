# Evaluation: Jarir Marketing Company (TADAWUL:4190) — 2026-11-23
## Bear case
The price already pays for the business: base fair value 17.46 SAR sits barely above the 17.05 close, so there is no margin of safety, and the bear value is 10.03 [Certain]. The ROIC rise to 57.9% is turnover-led while gross margin (-1.1pp) and operating margin (-1.2pp) drifted down over five fiscal years, a thin 13.1% retail gross margin with little room for error [Certain]. EV/EBITDA 15.1x is 67% above peers and P/B 11.8x is at the 67th percentile of its range [Certain]. Any valuation points come from trend strength (price +7.2% over the 200-day, 12-month change +18.9%): if Saudi consumer demand or growth slows, a de-rating toward peer multiples is the main risk [Likely]. The FCF direction change (falling over five years, rising over the last 12 months) rests on working capital that can swing back, as FY2023's 6.1% showed [Likely]. Segment and country mix are unverified [Certain].
## Bull case
Returns are exceptional and still rising: ROIC 57.9% TTM, up from 48.9% a year earlier, ROE 65.0% [Certain]. Operating margin is flat at 10.1% on the year, and FCF margin rose to 11.9%, so the five-year FCF decline looks like a FY2023 working-capital dip that has reversed rather than a structural break [Likely]. Cash backs earnings (FCF conversion 123.5%), net debt / EBITDA is 0.14x and Altman Z 7.47, so the balance sheet is near-unlevered [Certain]. P/E 16.0x sits at the 16th percentile of its own 5y range and below the peer median, with a 6.74% FCF yield [Certain]. The reverse DCF needs only 4.1% year-1 revenue growth, a modest bar [Likely]. Beta 0.27 gives the portfolio a low-correlation consumer name [Certain]. Scale and brand in the home market probably sustain the returns [Guessing].
## Decision
```json
{
  "ticker": "TADAWUL:4190",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Over the last 1 and 3 years ROIC and FCF margin are rising and operating margin is flat at 10.1% [RA-T, IS-T, CF-T]; the five-year FCF margin decline traces to a FY2023 working-capital dip (6.1%) that recovered to 12.1% in FY2025 [CF].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A slowdown in Saudi consumer spending compresses a thin 13.1% gross margin and de-rates a stock priced at base fair value with a premium to peers on EV/EBITDA.",
    "veto": null
  },
  "thesis": "A near-unlevered Saudi specialty retailer with ROIC near 58% and cash-backed earnings, priced at its mechanical base fair value.",
  "rationale": "Quality, balance sheet and recent direction are strong, but the price sits at base fair value with no margin of safety and a large peer premium on EV/EBITDA; country mix and moat are unverified. Good but not compelling at this price, so no position.",
  "price_at_decision": 17.05,
  "price_date": "2026-11-22",
  "research_note": "research/TADAWUL-4190/2026-11-23.md",
  "triggers": [
    {"text": "ROIC (ratios page, TTM) falls below 40%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "Operating margin (TTM) falls below 8.5%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8.5}},
    {"text": "Net debt / EBITDA rises above 1.5x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "FCF conversion (FCF / net income, TTM) falls below 80%."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 21.96, "basis": "ROIC keeps rising with FCF margin back toward its 13.3% 2-year high and multiples re-rate toward their 5y medians, matching the mechanical bull fair value 21.96 [IS,BS,CF,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 17.46, "basis": "Operating margin flat near 10.1% and growth near the 4.1% the reverse DCF implies, matching the mechanical base fair value 17.46 [IS,CF,RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 14.23, "basis": "A Saudi consumer slowdown de-rates EV/EBITDA to the mechanical bear 14.23 [RA]; above the 10.03 blended bear because the DCF bear 7.93 assumes a margin collapse that a 0.14x net debt balance sheet and flat TTM operating margin do not show [IS-T,BS]."}
  },
  "entry_price": 14.84,
  "entry_basis": "valuation file: base 17.46 x 0.85."
}
```

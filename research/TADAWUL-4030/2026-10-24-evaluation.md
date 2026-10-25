# Evaluation: The National Shipping Company of Saudi Arabia (TADAWUL:4030) — 2026-10-24
## Bear case
The cheapness is a cyclical mirage. TTM operating margin of 39.0% and ROIC of 24.7% sit far above every fiscal year (FY2025: 26.3% and 10.9%), which looks like a tanker-rate peak, not a new level [Likely]. On the stock's own history the mechanical EV/EBITDA fair value is 21.53 SAR base and 16.81 SAR bear, both well below the 34.80 close [Certain]. P/B of 1.6x is at the top of its 1.3x–1.6x five-year range, so on assets the stock is already full [Certain]. Fleet capex drove FCF margin to -21.8% in FY2024 and -9.9% in FY2025; cash conversion through a cycle is unproven [Certain]. Shipping has no moat: high rates attract new tonnage [Likely]. The Saudi-relationship edge and segment mix are unverified from a primary source [Guessing]. Results on Nov 1, 2026 could show rates rolling over [Guessing].
## Bull case
Even a partial fade leaves the stock cheap: P/E 5.0x and EV/EBITDA 4.3x are below their five-year minimums (8.9x, 7.3x) and well below the tanker peer medians of 7.5x and 7.2x [Certain]. FCF yield is 13.82% and net debt/EBITDA has fallen from 5.79x to 0.80x, so the balance sheet can absorb a downturn [Certain]. Quality has risen every year since FY2021, with Piotroski F at 7 [Certain]. The 2024 VLCC purchase enlarged the earning fleet just as rates rose [Likely]. A dollar-linked currency and low beta of 0.39 limit macro noise; the macro overlay is context only [Likely]. If rates stay elevated, the mechanical bull value of 77.57 SAR shows the upside [Guessing].
## Decision
```json
{
  "ticker": "TADAWUL:4030",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "Optically cheap TTM multiples rest on peak tanker-cycle earnings, while the stock's own-history fair value and its top-of-range P/B say the price already discounts more than normalised earnings support.",
  "rationale": "Low multiples and a repaired balance sheet are real, but TTM margins far above any fiscal year look cyclical, base and bear fair values sit well below the price, FCF has been negative in two of the last two fiscal years, and there is no verified moat. Good but not compelling: AVOID, no position.",
  "price_at_decision": 34.80,
  "price_date": "2026-10-22",
  "research_note": "research/TADAWUL-4030/2026-10-24.md",
  "triggers": [
    {"text": "TTM FCF margin holds above 25% (26.1% TTM now), showing the fleet capex cycle is over and earnings convert to cash; would raise conviction.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 25}},
    {"text": "TTM ROIC stays above 20% (24.7% now) after the Nov 1, 2026 results, suggesting returns are more durable than a single-cycle peak.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 20}},
    {"text": "A full fiscal year (income statement) reports operating margin above 30%, confirming the TTM step-up rather than a transient spike."},
    {"text": "Net debt/EBITDA on the ratios page rises above 2.5x, signalling another debt-funded fleet expansion that would further weaken the case.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 45.00, "basis": "Tanker rates stay high so TTM earnings hold and P/E moves toward the 7.5x peer median [RA,P:FRO]; still well below the mechanical bull value of 77.57 SAR because peak earnings rarely earn a full re-rating."},
    "base": {"probability": 0.5, "target_price_12m": 28.00, "basis": "TTM operating margin of 39.0% fades toward the FY2025 26.3% [IS]; above the mechanical base of 21.53 SAR because the 0.80x net debt/EBITDA [RA] and 13.82% FCF yield [ST] support the multiple."},
    "bear": {"probability": 0.3, "target_price_12m": 16.81, "basis": "Rates mean-revert and EV/EBITDA earnings fall back to the five-year average, matching the mechanical bear fair value of 16.81 SAR [IS,BS,CF,RA,ST]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Sands China Ltd. (HKG:1928) — 2026-10-19
## Bear case
Profitability is rolling over, not recovering: operating margin fell from 19.6% (FY2024) to 17.5% (FY2025) to 16.2% TTM, and net margin from 14.8% to 11.3% [IS] [Certain]. The stock is down -38.2% over 12 months and -34.6% over six [ST,HI], yet the note gives no business explanation for the fall; an unexplained drawdown alongside shrinking margins points to share loss or cost pressure we cannot yet see [Guessing]. The balance sheet is levered: net debt/EBITDA 2.75x, Altman Z 2.49 (grey zone), and P/B 9.2x with ROE 73.2% shows thin equity, so a modest EBITDA fall hits the equity hard [Certain]. Mainland demand is weak, with retail sales +1.1% YoY and the NBS calling domestic demand insufficient (macro overlay) [Certain]. The "below 5y minimum" multiples compare with pandemic-depressed earnings years, so the cheapness is overstated [Likely]. Dividend data is unavailable [data unavailable].

## Bull case
Sands China holds one of six Macau concessions, a regulatory moat with capital-heavy Cotai assets that are hard to replicate [Likely]. ROIC is 18.3% TTM, gross margin 79.2% and FCF margin 21.8% [RA,IS] [Certain]. At 6.9x P/FCF and a 14.42% FCF yield, cash generation alone can keep cutting leverage, which fell from 3.44x in FY2023 to 2.75x TTM [Certain]. The price implies -15.8% year-one revenue growth in the reverse DCF, far worse than the recovered margins suggest [Likely]. EV/EBITDA of 8.5x sits below the peer median of 9.0x and below its own 5y minimum of 12.9x [RA] [Certain]. The macro overlay judges weak mainland consumption already priced in, so any stimulus-led recovery in visitation is upside [Likely]. The Londoner Grand adds non-gaming capacity [Likely].

## Decision
```json
{
  "ticker": "HKG:1928",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A concession-protected Macau resort operator with 18.3% ROIC and a 14.42% FCF yield is cheap on cash flow, but falling margins, leverage, weak mainland demand and an unexplained -38.2% fall make it good rather than compelling.",
  "rationale": "Cash yield and the concession moat are real, but operating margin has fallen for two periods, leverage leaves thin equity, and the note cannot explain the drawdown. The scenario-weighted value sits only modestly above the price, short of conviction 4. Cash is preferable; revisit if margins stabilise.",
  "price_at_decision": 11.49,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-1928/2026-10-19.md",
  "triggers": [
    {"text": "TTM operating margin recovers above the FY2024 level of 19.6%, showing the margin compression has reversed (would raise conviction).", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 19.6}},
    {"text": "TTM net margin recovers above the FY2024 level of 14.8%, confirming earnings are rebuilding rather than eroding (would raise conviction).", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 14.8}},
    {"text": "TTM FCF margin falls below the FY2024 level of 17.4%, showing cash generation is following margins down (would cut conviction further).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 17.4}},
    {"text": "The next half-year results (company release) show year-on-year revenue growth with a stable operating margin, showing no structural share loss."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 18.8, "basis": "Margins stabilise and P/FCF re-rates from 6.9x to its 5y minimum of 11.3x [RA] on TTM FCF [CF]; still below the mechanical EV/EBITDA bear of 20.04 because the 5y multiples are anchored on pandemic-depressed earnings; macro overlay tilt neutral/small, probabilities unchanged."},
    "base": {"probability": 0.45, "target_price_12m": 12.5, "basis": "TTM EBITDA flat and EV/EBITDA moves from 8.5x to the peer median 9.0x [RA, peers], levered through net debt/EBITDA of 2.75x [BS,IS]; far below the mechanical base of 56.72 because the DCF growth extrapolates the recovery from the FY2021-22 trough [IS]."},
    "bear": {"probability": 0.30, "target_price_12m": 9.8, "basis": "Operating margin keeps sliding from 16.2% TTM [IS] as mainland retail sales stay near +1.1% (macro overlay, NBS), cutting EBITDA while EV/EBITDA holds at 8.5x [RA], and net debt of 2.75x EBITDA magnifies the equity hit."}
  },
  "valuation_overrides": [
    {"method": "dcf", "scenario": "base", "field": "growth", "value": 0.03, "reason": "The mechanical base growth uses the 3y/5y revenue CAGR, which starts from the FY2021-22 pandemic trough (operating margin -17.1% and -72.6% [IS]); a recovery rebound is not sustainable growth, and the macro overlay reports mainland retail sales at +1.1% YoY (stats.gov.cn)."}
  ],
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: operating and net margins are falling and the cause of the -38.2% fall is unexplained, so a lower price on the same evidence would not justify conviction 4; re-research when a release shows margins stabilising (triggers).",
  "replaces": null,
  "replacement_reason": null
}
```

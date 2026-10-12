# Evaluation: L3Harris Technologies, Inc. (LHX) — 2026-10-12
## Bear case
Returns are mediocre: ROIC of 8.1% TTM sits below a cost of equity built on a 5.22% risk-free rate, so growth creates little value [Likely]. Gross margin has fallen 4.5pp in five years to 25.5% [Certain]. The 16% operating-margin target is a management aspiration from a 12.9% base [Likely]. Leverage of 2.29x net debt/EBITDA, which management itself calls "slightly elevated versus peers", plus ~$1.8bn of maturities, meets 10y real yields up 0.56pp in 3 months (macro overlay) [Likely]. The share price has fallen 33.8% in 6 months and lags SPY by 48.3pp [Certain]. A CEO transition and a plaintiff-firm "fraud investigation" solicitation are unexplained overhangs [Guessing]. Short interest rose 28.2% month-on-month [Certain]. Q3 results on Oct 29 could reset expectations [Likely]. The base fair value is only +14.1% away, not a wide margin of safety [Certain].
## Bull case
Every cash multiple is below its own 5y minimum: EV/EBITDA 12.9x vs 13.2x, P/FCF 15.7x vs 17.8x [Certain]. The FCF yield is 6.36% and FCF conversion 149.8% [Certain]. The reverse DCF prices only 3.2% year-1 growth [Certain]. New propulsion awards (THAAD, PAC-3 MSE) and prime status on the Golden Dome tranches support demand for years [Likely]. ROIC and operating margin are trending up and Piotroski F is 7 [Certain]. Buybacks, debt paydown and a 24-year dividend-growth record show disciplined capital allocation [Likely]. The bull fair value is +31.0% [Certain].
## Decision
```json
{
  "ticker": "LHX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cheap-on-history defense franchise with growing missile and space demand, but low returns on capital, above-peer leverage and an unexplained sell-off cap the margin of safety at the current price.",
  "rationale": "Cash multiples are below 5y lows, but base fair value is only +14.1%, ROIC is 8.1%, leverage is elevated as real yields rise, and the 33.8% six-month fall coincides with a CEO change ahead of Oct 29 results. Good but not compelling. Conviction 3, so AVOID with an entry price at base fair value less 20%.",
  "price_at_decision": 236.97,
  "price_date": "2026-10-09",
  "research_note": "research/LHX/2026-10-12.md",
  "triggers": [
    {"text": "Operating margin falls back to or below its FY2023 trough of 11.0% (TTM 12.9%), which breaks the margin-expansion path toward management's 16% target", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11.0}},
    {"text": "ROIC reverses its 5-year uptrend to below the FY2021 level of 6.3% (TTM 8.1%)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 6.3}},
    {"text": "FCF margin falls below its FY2023 low of 8.5% (TTM 12.2%), which undermines the cash-conversion case", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8.5}},
    {"text": "Loss of prime or sole-source status on a major program (a Golden Dome tranche, or the THAAD or PAC-3 MSE propulsion contracts), disclosed in a filing or company release"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 310.34, "basis": "Missile-propulsion awards and Golden Dome work lift growth above the 3.2% implied by the reverse DCF and EV/EBITDA re-rates from 12.9x toward its 5y median of 15.9x [RA], reaching the fact sheet's bull fair value of 310.34."},
    "base": {"probability": 0.45, "target_price_12m": 255.52, "basis": "Steady execution with operating margin near 12.9% [IS], valued at the DCF base of 255.52 rather than the 270.27 blend, because the macro overlay's small tilt toward bear (real yields +0.56pp/3m, above-peer leverage; research/LHX/2026-10-12-macro.md) argues against the higher EV/EBITDA leg."},
    "bear": {"probability": 0.30, "target_price_12m": 170.48, "basis": "Gross-margin erosion (-4.5pp in 5y [IS]) continues, leverage stays elevated at 2.29x [RA] as rates rise, and the CEO-transition overhang persists, so the price falls to the bear fair value of 170.48; the probability is raised by the macro overlay's small tilt toward bear (research/LHX/2026-10-12-macro.md)."}
  },
  "entry_price": 216.22,
  "entry_basis": "valuation file: base 270.27 x 0.8 (fact-sheet fair value [IS,BS,CF,RA,ST,HI]). At this price the same evidence gives a 20% margin of safety, which justifies conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

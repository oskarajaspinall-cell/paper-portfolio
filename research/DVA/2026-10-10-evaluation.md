# Evaluation: DaVita Inc. (DVA) — 2026-10-10
## Bear case
The cheapness belongs to the equity, not the business. At the enterprise level DVA trades at 8.5x EV/EBITDA, in line with peers (8.4x) and only at the 30th percentile of its own range [Certain]. The 7.1x P/FCF reflects 4.5x net debt/EBITDA used to fund buybacks (shares -14.73% YoY), and the Altman Z of 1.64 sits in the distress zone [Certain]. The profit pool hangs on commercial payers: about 11% of patients bring about 26% of US dialysis revenue [Certain]. Q2 revenue per treatment fell as patients left ACA plans [Likely], and that mix loss could last [Guessing]. P/E of 15.3x is above its 5y max [Certain]. Short interest is 12.67% and rising [Certain]. Real yields are up 56bp in 3 months. With this much leverage, that hits both the discount rate and interest cost (macro overlay) [Likely]. Q3 results on Oct 28 are a binary near-term test [Likely].

## Bull case
DVA is a scale dialysis franchise with ROIC rising to 12.3% (+1.7pp over 5y), operating margin steady near 15%, and a 14.08% FCF yield [Certain]. Patients need dialysis whatever the economy does, and volumes rose in Q2 on lower mortality and competitor clinic closures [Likely]. Management reaffirmed 2026 guidance despite the mix hit [Likely]. The reverse DCF implies -11.7% revenue growth in year 1, far worse than current volume trends [Certain]. Even the mechanical bear fair value (226.10) is 26% above the close [Certain]. The 6.9% gap between the 50-day and 200-day averages and the +40.2% 12-month return show the long-term trend is intact after a -21.9% 3-month drawdown [Certain]. Buybacks shrinking the share count by about 15% a year compound per-share value quickly if FCF holds [Likely].

## Decision
```json
{
  "ticker": "DVA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A scale dialysis franchise with rising ROIC and a 14% FCF yield, but the equity cheapness is leverage-driven (EV/EBITDA in line with peers at 4.5x net debt/EBITDA) while commercial-mix erosion in revenue per treatment is unresolved.",
  "rationale": "Good but not compelling. On EV/EBITDA it is not cheap versus peers or its own median. The equity discount depends on 4.5x leverage while the commercial-payer mix, the profit driver, is eroding, and the macro overlay tilts moderately to bear. Conviction 3, below the buy bar. Re-test after Q3 results on Oct 28 or at a lower price.",
  "price_at_decision": 179.25,
  "price_date": "2026-10-09",
  "research_note": "research/DVA/2026-10-10.md",
  "triggers": [
    {"text": "Q3 2026 or later results (SEC 8-K) show US revenue per treatment stable or rising year on year, evidence that the ACA-driven commercial-mix loss was one-off rather than structural."},
    {"text": "TTM FCF margin rises above 12.3%, the 5y high (FY2023), showing cash generation is strengthening despite the mix headwind.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 12.3}},
    {"text": "Debt/EBITDA falls below 4.0x, showing deleveraging that cuts the rate and refinancing risk behind the equity discount.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 4.0}},
    {"text": "TTM ROIC falls below 10%, reversing the five-year improvement and confirming the avoid.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 247.49, "basis": "Commercial mix stabilises and guidance holds, so the stock retakes its 52-week high of 247.49 [HI]. That is still below the DCF-led blended base fair value (428.13) because the DCF capitalises a 190% FCF conversion [CF,IS] that the leverage makes fragile."},
    "base": {"probability": 0.45, "target_price_12m": 198.29, "basis": "EV/EBITDA moves back toward its 5y median of 9.4x [RA], which gives the EV/EBITDA method's base fair value of 198.29 [IS,BS,RA]. The base probability is cut by 0.05 for the moderate bear macro tilt from rising real yields on a 4.5x-levered balance sheet (research/DVA/2026-10-10-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 140.89, "basis": "Revenue per treatment keeps falling on ACA commercial-mix loss (Reuters Q2 headline, https://www.reuters.com/legal/litigation/davita-flags-lower-revenue-per-treatment-reaffirms-annual-forecast-2026-08-04/), taking the stock to the EV/EBITDA bear fair value of 140.89 [RA]. Probability is raised by 0.05 for the macro overlay's moderate bear tilt (research/DVA/2026-10-10-macro.md)."}
  },
  "entry_price": 140.89,
  "entry_basis": "The default anchor (valuation file: base 428.13 x 0.8 = 342.50) is above the price because the DCF capitalises leverage-flattered FCF. Instead, use the EV/EBITDA method's bear fair value of 140.89 [RA], near the 6-month low of 143.07 [HI], where the commercial-mix risk is priced at the low end of its own EV/EBITDA history.",
  "replaces": null,
  "replacement_reason": null
}
```

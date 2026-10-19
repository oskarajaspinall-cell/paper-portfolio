# Evaluation: SBM Offshore N.V. (AMS:SBMO) — 2026-10-19
## Bear case
The headline cheapness is largely an artefact of a non-repeating year. TTM FCF conversion of 354.3% and a 56.0% FCF margin are flattered by asset sales and project-financing receipts [RA, CF] [Likely], so the 2.1x P/FCF and 48.74% FCF yield overstate sustainable cash [Likely]. On the enterprise basis that captures the debt, SBMO trades at 8.1x EV/EBITDA, above the 6.2x peer median [RA] [Certain]. Net debt/EBITDA is still 3.26x and Altman Z is 1.38 [ST] [Certain]; the group stays leverage-intensive and exposed to new-build execution and Petrobras concentration [Guessing]. The mechanical fair value is unusable (DCF bear -112.42, base 372.28), and the EV/EBITDA method's base of 34.77 sits just below the 35.32 close [Certain]. Rising real yields (2.78%) and HY spreads (3.23%) lift financing costs for a long-duration lessor (macro overlay) [Certain].
## Bull case
Quality has stepped up: ROIC rose from 6.6% (FY2021) to 12.9% TTM and operating margin from 19.1% to 30.5% [RA, IS] [Certain], while net debt/EBITDA fell from 8.28x to 3.26x [RA] [Certain]. Contracted 15-20 year lease-and-operate revenue gives long visibility [Likely], with a record pro-forma backlog cited in the Q2 2026 release (https://www.globenewswire.com/news-release/2026/08/06/3339924/0/en/SBM-Offshore-Half-Year-2026-Earnings.html) [Likely]. Shares fell 3.13% YoY with buybacks still running [ST] [Certain]. P/E of 7.5x sits in the bottom fifth of its 5y range and far below the 29.3x peer median [RA] [Certain]; Piotroski F is 7 [ST] [Certain]. Continued deleveraging should shift value from debt to equity even at a flat EV multiple [Likely].
## Decision
```json
{
  "ticker": "AMS:SBMO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraging FPSO lessor with rising returns looks cheap on equity multiples, but cash flow is flattered by asset sales and it is not cheap on EV/EBITDA versus peers or its own-history EV/EBITDA fair value.",
  "rationale": "Real improvement in returns and leverage, but the cheapness rests on a non-repeating FCF year; the EV/EBITDA premium to peers, still-meaningful leverage, an unusable DCF and a small bearish macro tilt leave the skew balanced. Good but not compelling: conviction 3, no position.",
  "price_at_decision": 35.32,
  "price_date": "2026-10-16",
  "research_note": "research/AMS-SBMO/2026-10-19.md",
  "triggers": [
    {"text": "Debt/EBITDA rises above 6x, reversing the deleveraging that underpins the equity case.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 6}},
    {"text": "TTM ROIC falls below 8%, back toward FY2021-2022 levels, signalling fading project returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "TTM FCF margin turns negative, reverting to the FY2021-2023 pattern of capex outspending operating cash flow.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "TTM gross margin falls below 24%, reversing the margin recovery since FY2024.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 24}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 48.0, "basis": "Deleveraging continues and EV/EBITDA moves back toward its 5y median 10.8x [RA] from 8.1x, short of the EV/EBITDA method's bull 75.20 because the TTM EBITDA includes asset-sale-driven revenue (Q2 2026 release); probability trimmed for the small bearish macro tilt (2026-10-19-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 37.0, "basis": "EV/EBITDA holds near 8.1x [RA] while buybacks (shares -3.13% YoY [ST]) and debt reduction add modestly, consistent with the EV/EBITDA method base 34.77; the DCF base 372.28 is rejected as extrapolating a 354.3% FCF conversion year [CF,IS]."},
    "bear": {"probability": 0.30, "target_price_12m": 24.0, "basis": "EBITDA normalises after the asset-sale year and the multiple compresses toward the 6.2x peer median [RA], near the EV/EBITDA method bear 19.91; probability raised for rising real yields and HY spreads lifting financing costs (2026-10-19-macro.md)."}
  },
  "entry_price": 27.82,
  "entry_basis": "valuation file: EV/EBITDA method base 34.77 x 0.8 [RA]; the blended base 259.77 is driven by an unusable DCF, so the second method is used.",
  "replaces": null,
  "replacement_reason": null
}
```

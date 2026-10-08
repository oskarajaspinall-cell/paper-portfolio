# Evaluation: CF Industries Holdings (CF) — 2026-10-07
## Bear case
The 8.6x P/E looks cheap only on above-cycle earnings. TTM ROIC (24.5%), operating margin (38.6%) and net margin (27.1%) all sit above every fiscal year except the FY2022 spike. If margins revert to FY2024 levels (29.1% operating, 15.4% ROIC), earnings fall sharply and the multiple stops looking cheap [Likely]. Cash tells a weaker story than earnings: FCF margin fell from 36.1% to 24.7%, FCF/NI from 257% to 91%, and P/FCF (9.2x) and P/B (3.1x) both sit above their own 5y maximum [Certain]. Q2 2026 EPS and revenue missed, and the share is -13.3% over 6 months, below its 50-day MA [Certain]. Blue Point capex rises before any output arrives in 2029, and new capacity could compress the nitrogen spread [Likely]. Short interest is rising (+5.8%) [Certain].

## Bull case
Low-cost North American gas gives CF a durable feedstock advantage over European and Asian producers [Likely]. The balance sheet is very strong: net debt/EBITDA is 0.29x, Altman Z 3.34 and Piotroski 7 [Certain]. Shareholder returns are heavy: share count fell 8.51% YoY and the dividend was raised 20% [Certain]. At a 10.88% FCF yield and 4.8x EV/EBITDA, below its 5y median of 5.7x and the 7.0x peer median, the share needs no re-rating to compound [Likely]. Beta of 0.53 adds portfolio ballast [Certain]. The Belarus potash headline concerns potash, not nitrogen, so the September sell-off looks overdone for CF [Likely]. A return to the median multiple on TTM EBITDA would add about 20% [Guessing].

## Decision
```json
{
  "ticker": "CF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-cost, low-leverage nitrogen producer returning heavy cash, but its cheap earnings multiple rests on near-peak cyclical margins while free-cash conversion is falling and P/FCF and P/B sit above their own 5-year maximum.",
  "rationale": "Quality and the balance sheet are real. But TTM margins and ROIC are above every year except FY2022, so the 8.6x P/E is a cyclical-peak multiple. FCF conversion is falling as Blue Point capex rises, and Q2 missed. The risk/reward is fair, not compelling. Conviction 3 is below the buy threshold, so we AVOID and hold cash.",
  "price_at_decision": 116.02,
  "price_date": "2026-10-06",
  "research_note": "research/CF/2026-10-07.md",
  "triggers": [
    {"text": "TTM FCF margin recovers above 30% (back toward the FY2023-FY2024 range), showing Blue Point capex is not eroding cash conversion; this would raise conviction.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 30}},
    {"text": "TTM gross margin falls below 30% (under the FY2024 low of 34.6%), confirming the nitrogen spread is mean-reverting and the AVOID case.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 10%, showing returns no longer clear a reasonable cost of capital through the cycle.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Debt/EBITDA rises above 1.5x, showing buybacks or Blue Point capex are being funded with leverage.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 140, "basis": "TTM margins hold (operating margin 38.6% [IS]) and EV/EBITDA re-rates from 4.8x to its 5y median of 5.7x [RA], with net debt at only 0.29x EBITDA [RA], taking the share back to its 52-week high area of 141.96 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 108, "basis": "Margins partly revert from the 38.6% TTM operating margin toward the FY2025 level of 33.1% [IS] at a constant 4.8x EV/EBITDA [RA], partly offset by the 8.51% YoY share-count reduction [ST]."},
    "bear": {"probability": 0.30, "target_price_12m": 85, "basis": "The nitrogen spread mean-reverts to FY2024 economics (operating margin 29.1%, ROIC 15.4% [IS][RA]) while Blue Point capex keeps compressing FCF margin (24.7% TTM vs 36.1% FY2021 [CF,IS]), at an unchanged 4.8x EV/EBITDA [RA]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

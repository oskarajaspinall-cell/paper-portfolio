# Evaluation: FactSet Research Systems Inc. (FDS) — 2026-10-08
## Bear case
The cheapness may be deserved. FY2026 operating margin fell from 32.2% to 28.3% and gross margin from 54.1% (FY2024) to 50.6%, while ROIC slid from 23.2% to 17.5% over five years [Certain] (fact sheet, IS/RA). The 10-K itself flags AI letting rivals such as Bloomberg, LSEG and S&P erode demand for workstation-style data [Likely] (SEC 10-K). Short interest is 10.86% of float and rising 7.0% month-on-month, so informed capital is betting on structural, not cyclical, erosion [Likely] (ST). The stock lagged SPY by 16.5pp over 12 months [Certain] (fact sheet). The thesis is a re-rating, and the macro overlay shows real yields up 61bp in 3m, capping that re-rating [Likely] (macro overlay). A 7.29% FCF yield is fair, not a bargain, if margins keep falling and the BCC acquisition adds lower-margin real-time data [Guessing].

## Bull case
Retention is sticky. ASV retention is above 95% and client retention is 91% [Certain] (SEC 10-K). FY2026 delivered a record 7.0% organic ASV growth [Likely] (Q4 release, fact sheet news). Every multiple sits about 11% below its own 5-year minimum: P/E 18.7x, EV/EBITDA 12.5x and P/FCF 13.7x. P/E is 29% below the peer median of 26.3x [Certain] (RA). Cash conversion is improving, with FCF margin up 2.2pp to 28.6% and FCF/NI at 132.6% [Certain] (CF/IS). The share count fell 4.62% YoY, so buybacks compound returns without a re-rating [Certain] (ST). Net debt/EBITDA is 1.45x, about half its FY2022 level [Certain] (RA). New enterprise wins (Scotia Wealth expansion) show no sign of client attrition [Likely] (fact sheet news).

## Decision
```json
{
  "ticker": "FDS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-retention financial-data franchise trades below its own 5-year minimum multiples at a 7.29% FCF yield, but falling margins and returns plus credible AI-driven competitive risk make the discount look partly earned.",
  "rationale": "The valuation is attractive, but FY2026 operating margin fell 3.9pp and ROIC has declined for five years. Short interest is rising and the macro overlay tilts against the re-rating leg. The value case is good but not compelling, so conviction is 3, below the buy threshold of 4. Cash is acceptable.",
  "price_at_decision": 272.78,
  "price_date": "2026-10-07",
  "research_note": "research/FDS/2026-10-08.md",
  "triggers": [
    {"text": "TTM gross margin falls below 48%, extending the FY2024-FY2026 decline from 54.1% to 50.6% and confirming structural pricing/mix erosion.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 48}},
    {"text": "TTM ROIC falls below 15%, extending the five-year decline from 23.2% to 17.5% and showing the moat is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 24%, reversing the current 28.6% and removing the cash-conversion support for the valuation case.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 24}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 315, "basis": "Margins stabilise on record 7.0% organic ASV growth (Q4 FY2026 release, fact sheet news) and P/FCF returns to its 5y minimum of 15.8x from 13.7x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 285, "basis": "Multiples stay near current levels (P/E 18.7x [RA]) while the 7.29% FCF yield [ST] and a 4.62% falling share count [ST] lift per-share value modestly."},
    "bear": {"probability": 0.30, "target_price_12m": 240, "basis": "Operating margin repeats FY2026's fall from 32.2% to 28.3% [IS] on AI competition at a flat multiple; probability raised by a small bear tilt from the macro overlay (research/FDS/2026-10-08-macro.md) as rising real yields cap the re-rating."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

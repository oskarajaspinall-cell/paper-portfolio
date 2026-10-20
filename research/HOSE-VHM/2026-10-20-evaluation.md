# Evaluation: Vinhomes JSC (HOSE:VHM) — 2026-10-20
## Bear case
The cheapness rests on a TTM peak: gross margin is 43.8% TTM against 30.2% in FY2025 and 57.0% in FY2021, and ROIC fell from 28.7% to 10.3% over five fiscal years [Certain] (fact sheet Quality, IS/RA). Handover-driven revenue is lumpy, so TTM earnings and the 13.45% FCF yield are unlikely to recur [Likely]. FCF conversion swung from -103.9% (FY2024) to 61.5% (FY2025) while net debt/EBITDA rose from 0.22x to 2.38x [Certain]; Altman Z of 1.22 sits in the distress zone [Certain] (ST). The mechanical bear fair value is negative and the EV/EBITDA method's base is far below the price, so the DCF base of +91.4% leans on a cash spike [Certain] (fact sheet Fair value). It is a Vingroup subsidiary in a distressed local property sector where peers trade at 0.7x book [Certain]; related-party and refinancing risk is unquantifiable from allowed sources [Guessing].

## Bull case
At 6.2x P/E and 6.7x EV/EBITDA, VHM trades below its own 5y minimum EV/EBITDA and far below peers (15.2x / 19.3x) [Certain] (RA, peers). The reverse DCF implies -6.9% year-1 revenue growth, a severe outcome for Vietnam's largest land bank [Likely]. TTM ROE of 33.5% and FCF margin of 28.2% show the franchise still earns heavily at cycle points [Certain]. Shares fell 5.10% YoY, a capital return [Certain] (ST). RSI of 32.1 and the price near its 6-month low of 58,800 suggest selling is mature [Likely]. Results due Oct 28, 2026 could confirm TTM margins are holding [Guessing].

## Decision
```json
{
  "ticker": "HOSE:VHM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "Vinhomes looks cheap on TTM multiples, but those rest on a lumpy handover-driven earnings peak while five-year returns and margins fall, leverage rises and the Altman Z sits in the distress zone.",
  "rationale": "Multiples are low, but the earnings base is unreliable: FY margins and ROIC have fallen for five years, leverage has risen, the mechanical bear value is negative and the EV/EBITDA method sits far below the price. Probability-weighted scenarios do not clear the price. Quality and balance-sheet risk, not price, are the obstacle. No position.",
  "price_at_decision": 60300.00,
  "price_date": "2026-10-19",
  "research_note": "research/HOSE-VHM/2026-10-20.md",
  "triggers": [
    {"text": "Net debt/EBITDA (statistics/ratios page) falls below 1.0x, showing the FY2021-25 leverage build is reversing rather than the TTM cash inflow being handover timing.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 1.0}},
    {"text": "TTM gross margin rises above 45% after the FY2026 results, evidencing that the margin recovery is durable and not a one-off handover mix.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 45}},
    {"text": "FCF/NI conversion (cash flow + income statement) stays above 50% for a second consecutive fiscal year, showing cash generation is structural."},
    {"text": "Altman Z-score (statistics page) rises above 1.8, out of the distress zone."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 75000, "basis": "FY2026 results confirm TTM margins (gross 43.8% [IS]) and EV/EBITDA moves back toward its 5y median 8.5x [RA]; far below the DCF base because that rests on a single TTM FCF spike (FCF/NI -103.9% in FY2024 [CF,IS])."},
    "base": {"probability": 0.45, "target_price_12m": 60000, "basis": "Earnings normalise toward FY2025 margins (gross 30.2% [IS]) while P/E sits near 6.2x [RA], leaving the price flat; between the DCF base and the far lower EV/EBITDA-method base [fact sheet Fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 42000, "basis": "Margins revert to FY2025 levels, net debt/EBITDA keeps rising from 2.38x [BS,IS] with Altman Z 1.22 [ST], and P/E drops to its 5y minimum 5.2x [RA], back near the 52-week low of 43,450 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: base fair value x 0.8 is above the price, yet falling FY margins and ROIC, rising leverage and distress-zone Altman Z keep conviction low; a lower price would not change the decision until the triggers show deleveraging and durable margins.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: UnitedHealth Group Incorporated (UNH) — 2026-10-12
## Bear case
Returns are still eroding: ROIC fell from 16.8% (FY2023) to 10.2% (FY2025) and ROE from 25.0% to 12.5% [Certain] [RA]. Leverage rose with them; site net debt/EBITDA went from 0.94x to 2.44x (FY2025) [Certain] [RA]. Narrower 2027 Medicare Advantage networks show medical-cost trend is stronger than the moat [Likely] (Reuters, 2026-10-01). A new Texas AG investigation [Likely] (WSJ, 2026-10-05) and Q3 results on Oct 13 [Certain] [ST] are binary events whose outcome is unknown. The price is already at base fair value ($385.28 vs $379.30, +1.6%) [Certain], and UNH trades at a premium to peers on P/E (+19%) and EV/EBITDA (+22%) [Certain] [RA]. The skew is symmetric (bear -10.9%, bull +12.1%), so the investor is not paid for the falling-returns risk [Likely].
## Bull case
UNH is the scale leader in Medicare Advantage, and Optum's integration of insurance, PBM and care delivery is a structural advantage [Likely] [OV]. TTM ROIC (11.4%) and ROE (14.2%) are already above their FY2025 lows, which hints that the trough has passed [Likely] [RA]. Cash conversion is strong: FCF/NI was 167.2% TTM, a 6.94% FCF yield [Certain] [CF,ST]. EV/EBITDA and P/FCF sit below their own 5-year minimums, and P/E is at the 25th percentile of its range [Certain] [RA]. Buybacks continue (-1.47% shares YoY) [Certain] [ST], and the WellMed stake sale can fund deleveraging [Likely]. Narrower networks in 2027 could rebuild margin [Guessing].
## Decision
```json
{
  "ticker": "UNH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A scale managed-care and Optum franchise with strong cash conversion, but ROIC and ROE are still well below their 5-year levels and the price already sits at base fair value, so there is no margin of safety for the falling-returns, regulatory and earnings risk.",
  "rationale": "Good franchise, not compelling at this price. The price is near base fair value with a symmetric range. ROIC and ROE recovery is unproven. Leverage has risen, the Texas AG probe is unresolved and Q3 results land tomorrow. That is conviction 3, below the buy bar. Cash is acceptable, and the portfolio already holds managed-care exposure through CI.",
  "price_at_decision": 379.30,
  "price_date": "2026-10-09",
  "research_note": "research/UNH/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC recovers above the FY2024 level of 14.4% (statistics/ratios page), showing the 2027 Medicare Advantage margin actions are restoring returns.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 14.4}},
    {"text": "TTM ROE recovers above the FY2024 level of 15.1%, confirming the FY2025 low of 12.5% was the trough.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 15.1}},
    {"text": "Net debt/EBITDA (site definition, ratios page) falls back below the FY2024 level of 1.48x from 1.68x TTM, showing the WellMed sale and FCF are deleveraging the balance sheet."},
    {"text": "The Texas Attorney General's Deceptive Trade Practices Act investigation is resolved or disclosed (SEC filing) as immaterial, removing the regulatory overhang."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 425.01, "basis": "ROIC/ROE keep recovering from their FY2025 lows [RA] as the 2027 narrow-network MA plans (Reuters 2026-10-01) rebuild margin, so P/E re-rates toward the fact sheet's bull fair value of 425.01 [IS,RA]."},
    "base": {"probability": 0.50, "target_price_12m": 385.28, "basis": "Returns stabilise near TTM ROIC 11.4% / ROE 14.2% [RA] and P/E stays near its 24.8x 5y median, in line with the fact sheet's base fair value of 385.28 [IS,RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 337.96, "basis": "Medical-cost pressure persists and ROIC falls below the FY2025 low of 10.2% [RA] while the Texas AG probe (WSJ 2026-10-05) adds cost, so P/E falls toward the 21.8x 5y minimum and the fact sheet's bear fair value of 337.96 [RA]."}
  },
  "entry_price": 308.22,
  "entry_basis": "valuation file (fact-sheet fair value [IS,RA]): base 385.28 x 0.8, a 20% margin of safety. At that price the symmetric fair-value range turns into a skew that pays for the unproven ROIC/ROE recovery.",
  "replaces": null,
  "replacement_reason": null
}
```

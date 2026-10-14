# Evaluation: Crown Castle Inc. (CCI) — 2026-10-14
## Bear case
Why it fell: no new filing, release or news item since the 2026-09-14 CFO/COO change [Certain]. The 77.85 print is a ~2% pullback, 0.65x ATR, after the 2026-10-09 +15.6% reaction [Certain]. Noise, not news [Likely]. The real headwind is rates: the 10y real yield is up 59bp in 3 months and fed funds is still rising (macro overlay, FRED DFII10/DFF) [Certain]. That hits CCI harder than its peers because net debt/EBITDA is 8.31x TTM, up from 7.39x in FY2021 [RA] [Certain]. ROIC is flat near 6% [RA] [Certain], so the ROE jump to 37.2% comes from leverage, not a better business [Likely]. The management leverage figure (~6.3x) cannot be reconciled with the site's 8.31x [Certain]. Organic growth is guided to bottom in 2026 [Likely]. The CFO leaves in March 2027 [Certain]. Q3 results come out in 7 days, on 2026-10-21 [Certain].
## Bull case
The towers are a triopoly with high switching costs and contracted escalators [Likely]. P/E (32.5x) and EV/EBITDA (20.7x) are both below their 5-year minimums and 28%/9% below peers [RA] [Certain]. FCF yield is 7.25% [ST] [Certain]. The P/FFO-proxy base fair value is 97.83, +23.0% [Certain]. Management says organic growth troughs in 2026, with spectrum releases supporting demand afterwards [Likely] (Goldman/BofA transcripts [OV]). Short interest is only 2.24% and falling [ST] [Certain]. If the fiber-sale proceeds show up as lower leverage at Q3, the leverage discount should narrow [Guessing].
## Decision
```json
{
  "ticker": "CCI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A pure-play US tower REIT trades below its own 5-year minimum P/E and EV/EBITDA. But 8.31x leverage, ~6% ROIC and rising real yields make the discount look partly deserved until Q3 shows deleveraging.",
  "rationale": "Today's dip to the entry price was a 0.65x-ATR pullback with no new information. The cheapness is real, but leverage is high and unreconciled, ROIC is flat, and the macro overlay tilts moderately bearish via real yields. Q3 results in seven days test the deleveraging thesis directly. Good but not compelling: conviction 3, no position.",
  "price_at_decision": 79.56,
  "price_date": "2026-10-13",
  "research_note": "research/CCI/2026-10-14.md",
  "triggers": [
    {"text": "ROIC (statistics) rises above 6.9%, the FY2022 five-year high, showing the towers-only model is lifting returns rather than just leverage.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 6.9}},
    {"text": "ROE (statistics) falls back below 20% from 37.2% in FY2024, confirming the profitability jump was leverage-driven and temporary.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA (site definition, ratios page) falls below 8.0x at the FY2026 Q3 results (2026-10-21), showing fiber-sale proceeds are deleveraging the balance sheet."},
    {"text": "Piotroski F-Score (statistics page) falls below 4 from 6, signalling broad financial deterioration."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 97.83, "basis": "Q3 confirms deleveraging and real yields roll over (overlay macro_bull), so the price reaches the fact sheet's P/FFO-proxy base fair value of 97.83 [IS,BS,CF,RA,ST]."},
    "base": {"probability": 0.45, "target_price_12m": 81.52, "basis": "P/E returns only to its 5y minimum of 33.3x from 32.5x [RA]; this sits below the 97.83 base fair value because the overlay's moderate bear tilt (DFII10 +59bp/3m, research/CCI/2026-10-14-macro.md) argues against re-rating to history."},
    "bear": {"probability": 0.35, "target_price_12m": 62.23, "basis": "Real yields keep rising on 8.31x net debt/EBITDA [RA] and the growth trough extends, compressing the price to the fact sheet's bear fair value of 62.23; probability raised for the overlay's moderate bear tilt (research/CCI/2026-10-14-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock just traded at the old 78.26 entry (base 97.83 x 0.8) and the evidence still only supports conviction 3. What decides it is unresolved: the 8.31x vs ~6.3x leverage conflict and the Q3 deleveraging test on 2026-10-21. Re-research on those results, not on a lower price.",
  "replaces": null,
  "replacement_reason": null
}
```

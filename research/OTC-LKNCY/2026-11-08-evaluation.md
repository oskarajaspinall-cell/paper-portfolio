# Evaluation: Luckin Coffee Inc. (LKNCY) — 2026-11-08
## Bear case
Growth now comes from opening stores, not from existing ones: the Q2 and Q3 call summaries describe same-store sales declining against subsidy-driven comparisons [Likely]. The Direction change lines confirm it: ROIC fell from 26.7% to 24.7% over 12 months, 2.8pp below its 2-year high, and FCF margin slipped from 10.5% to 9.4% [Certain]. Operating margin is flat at 11.0% [Certain]. That fits a China coffee price war that uses up the unit-growth runway rather than a one-off [Likely]. The multiples sit below their 5y minimums because the old growth premium is unwinding, and a de-rating stock is not automatically a cheap one [Likely]. The mechanical bear fair value is negative (-27.70), so the model has no floor [Certain]. Piotroski F of 4, the 2020 fraud, the OTC-only listing and the yuan exposure of a CNY reporter add risks that cash flow does not offset [Certain].
## Bull case
This is a net-cash business (net debt/EBITDA -0.24x) with ROIC of 24.7%, ROCE rising to 26.4% and a 60.8% gross margin [Certain]. Cash is real: FCF conversion is 125.6% of net income and the FCF yield is 7.45% [Certain]. P/E of 16.7x and P/FCF of 13.4x sit below their own 5y minimums (20.2x, 21.6x) and below the peer medians [Certain]. The reverse DCF needs only 7.8% year-1 revenue growth, which is modest for a chain still adding stores at home and abroad [Likely]. Base fair value of 45.09 already includes a 3.5% CNY country-risk premium [Certain]. Shares are shrinking and the buyback was upsized in September [Certain]. Even with the price war, operating margin has held and ROCE has risen [Certain].
## Decision
```json
{
  "ticker": "OTC:LKNCY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-return China coffee chain trades below its own 5-year minimum P/E and P/FCF, but growth now relies on new stores while same-store sales fall in a subsidy-driven price war and ROIC and FCF margin are rolling over.",
  "rationale": "The valuation is attractive and cash is real, but falling same-store sales, ROIC and FCF margin over the last 12 months, a negative mechanical bear value, weak Piotroski and governance history make the skew good rather than compelling. Conviction 3 means AVOID. Proof that the comps have stabilised would matter more than a lower price.",
  "price_at_decision": 34.00,
  "price_date": "2026-11-06",
  "research_note": "research/OTC-LKNCY/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC climbs back above its 2-year high of 27.5% (24.7% now), showing that store-level returns survive the price war (would raise conviction).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 27.5}},
    {"text": "TTM FCF margin recovers above 10.5%, the level of a year earlier (9.4% now), reversing the 12-month decline (would raise conviction).", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 10.5}},
    {"text": "TTM operating margin falls below 8% (11.0% now), confirming that the subsidy war is structurally compressing profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}},
    {"text": "The quarterly earnings release or call shows same-store sales growth turning positive again, so growth is no longer only from new units."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 50.0, "basis": "Comps stabilise and P/E re-rates from 16.7x back toward its 5y minimum of 20.2x [RA] on store-driven earnings growth; below the mechanical bull of 75.11 because ROIC is falling from its 27.5% 2-year high [RA-T]."},
    "base": {"probability": 0.45, "target_price_12m": 40.0, "basis": "Unit growth offsets falling same-store sales (Q3 2026 transcript, fact sheet news) and P/E holds near 16.7x [RA]; below the mechanical base of 45.09 because FCF margin has slipped from 10.5% to 9.4% [CF-T,IS-T]."},
    "bear": {"probability": 0.30, "target_price_12m": 25.0, "basis": "The price war pushes operating margin back below the FY2024 9.9% [IS] and P/E de-rates further, taking the price below the 52-week low of 27.22 [HI]; the mechanical bear of -27.70 is unusable as a floor."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below base fair value 45.09 x 0.8. The obstacle is the 12-month decline in ROIC and FCF margin and falling same-store sales, so a lower price would not change the decision. Evidence that comps and returns have stabilised would.",
  "replaces": null,
  "replacement_reason": null
}
```

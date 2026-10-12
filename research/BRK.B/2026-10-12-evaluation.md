# Evaluation: Berkshire Hathaway Inc. (BRK.B) — 2026-10-12
## Bear case
Nothing here is mispriced. P/B 1.5x is at the 83rd percentile of its 5y range (1.3x–1.5x) and 29% above the peer median of 1.1x [Certain]. For a balance sheet made mostly of marked-to-market securities and insurance liabilities, that leaves little margin of safety [Likely]. P/E 12.9x sits above its 5y median of 9.5x [Certain]. Returns are fading: ROE fell from 18.8% (FY2021) to 9.8% (FY2025), operating margin from 41.7% to 26.1%, and ROCE from 12.6% to 8.4% [Certain]. Piotroski F is 4 [Certain]. Flat share count (−0.00% YoY) means no buyback support at this price [Certain]. The macro overlay tilts toward bear (small): real yields are up 0.56pp in 3m, which threatens the equity marks and BRK's own multiple [Likely]. Capital allocation under a new CEO is still unproven at this scale [Likely]. The stock has lagged SPY by 12.5pp over 12 months, and nothing obvious will close that gap [Certain].

## Bull case
This is a fortress. Net debt/EBITDA of −1.81x TTM gives it a net-cash position that peers lack [Certain]. With fed funds at 3.88% and a market pricing higher-for-longer, that cash earns real investment income [Likely]. ROIC is still 19.3% TTM [Certain]. Float, BNSF's rail duopoly and GEICO's scale are durable moats [Likely]. Management is deploying cash, for example the repeated Lennar purchases [Likely]. Beta of 0.59 makes it a defensive diversifier for a book that leans on Technology and Healthcare [Certain]. EV/EBITDA of 6.7x is in line with peers (6.6x) [Certain]. If markets fall, the cash pile becomes an option on cheap assets [Guessing]. Even so, this is "good but not compelling": there is no valuation dislocation to exploit [Likely].

## Decision
```json
{
  "ticker": "BRK.B",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A net-cash, moat-rich conglomerate whose returns are fading, priced near the top of its own 5-year P/B range and above its median P/E, so it offers quality without a margin of safety.",
  "rationale": "The quality is real but the returns trend is down (ROE 18.8% to 9.8%, operating margin 41.7% to 26.1%) and there is no dislocation: P/B is at the 83rd percentile of its 5y range, P/E is above its median, there are no buybacks, and the macro tilt is toward bear. Good but not compelling, so no position.",
  "price_at_decision": 515.62,
  "price_date": "2026-10-09",
  "research_note": "research/BRK.B/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12% (vs 19.3% TTM, 17.0% FY2025), showing core operating and underwriting returns eroding beyond cyclicality.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 3%, under the 5y low of 3.1% (FY2024), showing structurally weaker operating cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 3}},
    {"text": "TTM operating margin falls below 20% (vs 30.3% TTM, 5y FY low ex-FY2022 of 26.1%), showing the earnings base itself is shrinking.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 600, "basis": "Cash redeployment (e.g. Lennar) and higher-for-longer cash yields lift earnings, and P/E re-rates to about 15x, inside its 5y range of 7.4x–16.2x [RA]. That is above the P/E-method bull of 437.03 because the mechanical P/B+ROE blend is unusable (a Class A share-count mismatch, per the note)."},
    "base": {"probability": 0.5, "target_price_12m": 515, "basis": "P/E holds near its current 12.9x and the peer median of 13.1x [RA] on flat TTM earnings with no buybacks (shares −0.00% YoY [ST]). That is above the P/E-method base of 379.06 [Fair value], which assumes reversion to the 5y median."},
    "bear": {"probability": 0.3, "target_price_12m": 379, "basis": "Fading returns (ROE 9.8% FY2025 [RA]) and the overlay's small bear tilt (real-yield rise, research/BRK.B/2026-10-12-macro.md) push P/E back to its 5y median of 9.5x [RA], matching the P/E-method base fair value of 379.06. The overlay raised this scenario's weight."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is 2, below the entry-price threshold. The mechanical base fair value (728,393) is unusable because of a Class A/B share-count mismatch, and declining returns, not just price, are what keep conviction low.",
  "replaces": null,
  "replacement_reason": null
}
```

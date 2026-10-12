# Evaluation: Camden Property Trust (CPT) — 2026-10-12
## Bear case
This is a low-return, commodity rental business: ROIC has sat at 3.2%-3.7% for five years and ROE is 7.9% TTM [Certain]. Leverage is at its five-year high, with net debt/EBITDA (site definition) at 5.40x TTM against 3.92x in FY2024 [Certain]. Management's ~4.5x pro forma figure is not yet visible in reported numbers [Likely]. FCF yield is -2.06% and FCF margin is [data unavailable], so cash generation cannot be checked [Certain]. The macro overlay is primary with a moderate bear tilt. The 10y real yield is up 0.56pp in 3 months and the 2y yield sits above fed funds, which points to higher-for-longer cap rates and refinancing costs [Likely]. Base fair value is only +9.6% above the price, which is thin for a stock with no moat and a co-founder retirement. Relative strength is -21.0pp vs SPY over 12 months [Certain].
## Bull case
The stock is cheap against its own history and its peers. EV/EBITDA of 16.8x sits at the 4th percentile of its 5y range and 12% below the peer median, while EV/Sales and P/B are 18% and 20% below peers [Certain]. Exiting California for ~$1.6bn simplifies the portfolio, funds buybacks (shares -2.43% YoY) and paid off credit lines and commercial paper [Likely]. Management says Sun Belt supply has passed its peak [Likely]. Q2 Core FFO beat guidance and occupancy improved [Likely]. The bear fair value is only -9.2% below the price and the bull is +54.5%, so the payoff is asymmetric if real yields stabilise [Guessing]. With a beta of 0.81, the stock offers defensive ballast [Certain].
## Decision
```json
{
  "ticker": "CPT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Camden is a cheap Sun Belt apartment REIT relative to its history and peers, but low returns, peak leverage and a rising real-yield backdrop make the re-rating a rate bet rather than a high-conviction value case.",
  "rationale": "Valuation is undemanding but base fair value is only +9.6% away, quality is low and flat (ROIC 3.2%), leverage is at a 5y high (5.40x) and the primary macro overlay tilts moderately bearish on rising real yields. Good but not compelling: conviction 3, no position; revisit nearer base fair value less margin of safety.",
  "price_at_decision": 97.58,
  "price_date": "2026-10-09",
  "research_note": "research/CPT/2026-10-12.md",
  "triggers": [
    {"text": "Net debt/EBITDA (site definition) rises above 5.6x, showing leverage is climbing rather than converging toward management's ~4.5x pro forma level", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 5.6}},
    {"text": "ROE falls below 5%, giving back the recovery from the FY2024 3.5% trough", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 5}},
    {"text": "ROIC falls below 3.0%, below its five-year range", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 3.0}},
    {"text": "Quarterly filings show Sun Belt new-supply deliveries in Camden's core markets re-accelerating to new multi-year highs, reversing management's past-peak view"}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 119.81, "basis": "Real yields stabilise and EV/EBITDA moves from 16.8x toward its 5y median 18.2x [RA], taking the price back to the 52-week high [HI]; set below the 150.80 mechanical bull because leverage at 5.40x [RA] limits the re-rating."},
    "base": {"probability": 0.45, "target_price_12m": 106.96, "basis": "Supply passes its peak per the Q2 2026 call (https://stockanalysis.com/stocks/cpt/transcripts/659238-q2-2026/) and the price converges on the P/FFO-proxy base fair value [IS,BS,CF,RA,ST]; probability cut from the bull/base toward the bear because of the macro overlay's moderate bear tilt (research/CPT/2026-10-12-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 88.64, "basis": "Real yields keep rising (DFII10 +0.56pp over 3 months, research/CPT/2026-10-12-macro.md), widening cap rates on 5y-high leverage of 5.40x [RA], taking the price to the P/FFO-proxy bear fair value; weight raised under the overlay's moderate bear tilt."}
  },
  "entry_price": 85.57,
  "entry_basis": "valuation file: base 106.96 x 0.8 (20% margin of safety); at that level the asymmetry would compensate for low ROIC and peak leverage",
  "replaces": null,
  "replacement_reason": null
}
```

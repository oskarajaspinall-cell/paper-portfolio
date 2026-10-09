# Evaluation: NVIDIA Corporation (NVDA) — 2026-10-09
## Bear case
The price already assumes near-perfection. The reverse DCF implies 54.4% year-1 revenue growth, fading over a decade [Certain] (fact sheet). The mechanical fair value is $81.20 base and $202.05 bull, both below the $230.48 close [Certain] (fact sheet). Concentration in "a limited number of partners and distributors", hyperscaler in-house silicon, and foreclosure from China's data-center market, which cost a $4.5bn H20 charge, all threaten that growth path [Certain] (10-K, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm). FCF conversion has fallen to 65.8% TTM [Certain] (CF,IS), and demand is increasingly debt-funded, as the reported SpaceX chip-loan talks show [Likely] (fact sheet news). The 10y real yield is up 49bp in a month [Certain] and beta is 2.22, so a higher discount rate hits the multiple hard [Likely] (macro overlay).
## Bull case
This is one of the highest-quality businesses listed: TTM ROIC 92.0%, operating margin 65.2% and net cash [Certain] (RA, IS, BS). CUDA lock-in and the integrated GPU-plus-networking stack keep switching costs high [Likely] (10-K). P/E of 30.0x, EV/EBITDA of 27.5x and P/FCF of 43.8x are all below NVIDIA's own 5-year minimums [Certain] (RA), and P/E is 23% below the peer median [Certain]. Shares outstanding fell 1.04% YoY [Certain] (ST). Momentum and relative strength against SPY are positive over 3, 6 and 12 months [Certain] (HI). If AI capex keeps compounding, earnings can grow into the price, and the multiple could re-rate toward its 5-year floor [Guessing].
## Decision
```json
{
  "ticker": "NVDA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A world-class, net-cash AI-compute franchise whose $230.48 price already discounts 54.4% year-1 revenue growth, above even its mechanical bull fair value of $202.05, leaving no valuation margin of safety against concentration, China and rising-real-yield risks.",
  "rationale": "Quality is exceptional, but this is a core sleeve for good businesses at attractive valuations. The price sits above every mechanical fair-value case, the implied growth is heroic, and the macro overlay tilts moderately bearish for a stock with a 2.22 beta. Being cheap against its own history is not the same as being cheap. Conviction 2, so AVOID, with no position.",
  "price_at_decision": 230.48,
  "price_date": "2026-10-08",
  "research_note": "research/NVDA/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin falls below 65%, reversing the multi-year pricing-power expansion (TTM 74.7%).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 65}},
    {"text": "TTM ROIC falls below 50%, more than halving from 92.0% and signalling moat or cycle erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 50}},
    {"text": "TTM FCF margin falls below 35%, under the FY2026 44.8% level, showing capex and inventory are outrunning cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 35}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 291.9, "basis": "AI capex keeps compounding and P/E re-rates from 30.0x to its 5y minimum of 38.0x [RA] on TTM EPS, sitting above the $202.05 bull fair value because it assumes the growth the reverse DCF implies is actually delivered."},
    "base": {"probability": 0.45, "target_price_12m": 202.05, "basis": "The price converges to the fact sheet's bull fair value of $202.05 [IS,BS,CF,RA,ST,HI]; the macro overlay's moderate bear tilt (10y real yield +49bp in 1m, research/NVDA/2026-10-09-macro.md) lifts the discount rate on a 2.22-beta stock [ST], so the base is set below the current price."},
    "bear": {"probability": 0.30, "target_price_12m": 97.04, "basis": "AI-capex digestion plus tighter financing for debt-funded buyers (macro overlay, moderate bear tilt, research/NVDA/2026-10-09-macro.md) and China foreclosure (10-K) take EV/EBITDA to the method's base fair value of $97.04 [IS,BS,CF,RA,ST], still above the $81.20 blended base."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

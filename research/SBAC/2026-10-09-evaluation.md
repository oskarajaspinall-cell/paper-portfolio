# Evaluation: SBA Communications Corporation (SBAC) — 2026-10-09
## Bear case
SBAC carries 8.12x net debt/EBITDA [Certain] and management prefers buybacks over debt repayment [Likely]. That leaves it exposed to a rate tape that is moving against it. The 10y Treasury yield is 5.28% and the 10y real yield rose +0.61pp in 3 months, per the macro overlay [Certain]. Management itself calls this a post-5G "harvest phase" [Likely]. Trading below the 5y-minimum P/E, EV/EBITDA and EV/Sales may therefore reflect a structural re-rating, not an anomaly [Likely]. Quality can't be verified: margins, ROIC and ROE are all [data unavailable] and the Piotroski score is only 4 [Certain]. The fair value uses one method (P/FFO proxy) with no NAV cross-check [Certain]. The stock has lagged SPY by -36.8pp over 6 months and trades below both moving averages [Certain]. Nothing visible marks the end of the de-rating [Guessing].

## Bull case
Tower leases are long-term, carry escalators and have high switching costs, inside a three-player oligopoly [Likely]. Every available multiple sits below its 5-year minimum: EV/EBITDA is 18.0x against a 5y minimum of 19.5x and a median of 23.4x, and P/E is 35% below the peer median [Certain]. The FCF yield is 5.83% [Certain]. Leverage has fallen from 9.35x to 8.12x over five years [Certain]. The mechanical fair value puts even its bear case (188.19) above the 170.01 close, and the base case (276.15) is +62% [Certain]. The Q2 2026 call raised the full-year site-leasing and FFO outlook [Likely]. Edge-compute and AI-inference deployments on towers add optionality [Guessing]. Lower real yields would re-rate the whole REIT group [Likely].

## Decision
```json
{
  "ticker": "SBAC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A tower-REIT oligopolist trades below its 5-year minimum multiples, but 8.12x leverage, buybacks prioritised over delevering, rising real yields and unverifiable margins/returns keep this cheap rather than compelling.",
  "rationale": "The valuation is attractive, but quality data (margins, ROIC) is unavailable, leverage is high and the macro overlay tilts moderately toward bear as real yields and spreads rise. Management describes a harvest phase. Good but not compelling: AVOID. Conviction 3 reflects real value, offset by unresolved rate and balance-sheet risk.",
  "price_at_decision": 170.01,
  "price_date": "2026-10-08",
  "research_note": "research/SBAC/2026-10-09.md",
  "triggers": [
    {"text": "Net debt/EBITDA (ratios page, site definition) rises back above 9.0x from 8.12x TTM, reversing the five-year deleveraging trend."},
    {"text": "Shares outstanding grow year on year (statistics page), meaning the buyback has stopped and equity is being issued.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "Site leasing revenue (income statement) declines year on year for two consecutive fiscal years, showing the harvest phase is a structural decline rather than a plateau."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 230, "basis": "Real yields ease, so EV/EBITDA recovers from 18.0x through its 5y minimum of 19.5x toward the 23.4x median [RA]; levered by 8.12x net debt/EBITDA [RA], that lands below the mechanical bull of 318.18 because the macro overlay sees rates pricing further tightening (research/SBAC/2026-10-09-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 185, "basis": "EV/EBITDA returns to roughly its 5y minimum of 19.5x [RA] on TTM EBITDA with 8.12x net debt [RA]; this sits near the mechanical bear fair value of 188.19 rather than the 276.15 base, because the harvest-phase commentary (BofA transcript [OV]) and the overlay's moderate bear tilt argue against a return to median multiples."},
    "bear": {"probability": 0.35, "target_price_12m": 145, "basis": "Real yields keep rising (DFII10 +0.61pp in 3m, research/SBAC/2026-10-09-macro.md), so EV/EBITDA de-rates further below its 5y minimum, amplified by 8.12x leverage [RA]; the macro overlay's moderate bear tilt raised this probability from 0.25 to 0.35 and the stock is near its 52-week low of 156.60 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its own 5y-minimum multiples and the fact sheet's bear fair value (188.19). The decision hinges on unverifiable margins and returns ([data unavailable]), 8.12x leverage with buybacks favoured over delevering, and rising real yields, so a lower price would not change it.",
  "replaces": null,
  "replacement_reason": null
}
```

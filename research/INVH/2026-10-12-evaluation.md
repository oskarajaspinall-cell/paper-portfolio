# Evaluation: Invitation Homes Inc. (INVH) — 2026-10-12
## Bear case
The cheapness is mostly a rate story, and rates are still moving against it. The 10y real yield is up 56bp in 3 months and fed funds rose 25bp in a month; the macro overlay tilts toward bear (moderate) [Certain]. The own-history fair value (base 41.16) rests on multiples set in a lower-rate era (5y median P/E 43.2x), so its +53.6% upside overstates the case at a 5.22% risk-free rate [Likely]. Leverage of 5.65x net debt/EBITDA means refinancing costs feed straight into FFO [Certain]. ROE of 7.1% is thin for equity priced at 1.7x book [Certain]. A new law curbs institutional purchases of existing homes, which caps external growth [Likely]. Momentum is weak: -12.4pp vs SPY over 3 months, and short interest is up 20.9% in a month [Certain]. Q3 results on Oct 28 test the H2 turnover and property-tax risks management flagged [Likely].
## Bull case
Every multiple is below its own 5-year minimum and below the peer median: P/E 24.6x vs a 29.0x minimum and a 29.7x peer median, P/B 1.7x vs a 2.3x peer median [Certain]. Fundamentals are improving, not deteriorating. ROE rose from 2.9% to 7.1% and net debt/EBITDA fell from 6.72x to 5.65x [Certain]. Q2 showed 97.1% occupancy, faster renewal growth and raised core FFO/AFFO guidance [Likely]. Management is buying back stock at around $26.30, and shares outstanding are down 1.17% YoY [Likely]. Weak starter-home affordability supports structural rental demand [Likely]. A pause in yields would re-rate the stock toward peers [Guessing].
## Decision
```json
{
  "ticker": "INVH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "The largest US single-family rental REIT trades below its own 5-year minimum and peer multiples with improving ROE and falling leverage, but rising real yields and a new institutional-purchase law cap the re-rating within 12 months.",
  "rationale": "The stock is cheap on paper, but the discount mostly reflects a 5.22% risk-free rate and rising real yields, which hit a 5.65x-levered REIT directly. The mechanical fair value leans on low-rate-era multiples. Expected 12-month value is only modestly above the price, with Q3 results imminent. Good but not compelling, so conviction is 3 and the decision is AVOID.",
  "price_at_decision": 26.79,
  "price_date": "2026-10-09",
  "research_note": "research/INVH/2026-10-12.md",
  "triggers": [
    {"text": "ROE falls back below 5%, reversing the five-year rise from 2.9% to 7.1% [RA].", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 5}},
    {"text": "Debt/EBITDA rises above 6.5x, reversing the deleveraging from 6.72x to 5.65x [RA].", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 6.5}},
    {"text": "Management cuts full-year occupancy, same-store revenue or core FFO guidance at the Q3 2026 release (Oct 28) or later, confirming the H2 execution risks it flagged."},
    {"text": "Management states in a filing or call that the new institutional homebuying law materially restricts its acquisition or ResiBuilt pipeline."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 32.35, "basis": "Yields roll over and P/E re-rates to the 29.7x peer median [RA, P:AMH/EQR/MAA/AVB] on TTM earnings. This is below the mechanical bull fair value of 41.78 because the 5y median multiples were set when rates were lower."},
    "base": {"probability": 0.45, "target_price_12m": 28.37, "basis": "Occupancy and buybacks hold (Q2 transcript) and P/B recovers only to its 5y minimum of 1.8x [RA]. This is below the 41.16 base fair value because the macro overlay's rising real yields (DFII10 +56bp in 3m) keep cap rates high."},
    "bear": {"probability": 0.30, "target_price_12m": 24.25, "basis": "Real yields and fed funds keep rising (macro overlay tilt toward bear, moderate, which raised this probability from 0.20 to 0.30), so the stock retests its 52-week low of 24.25 [HI] as refinancing costs on 5.65x leverage [RA] weigh on FFO."}
  },
  "entry_price": 24.04,
  "entry_basis": "Base fair value x 0.8 (32.93) is above the current price, because the rate-driven discount is the obstacle and the base model is not. Anchored instead on the valuation file's bear fair value 30.05 x 0.8 = 24.04, just below the 52-week low of 24.25 [HI], where even the higher-rate scenario would leave a margin of safety.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: McDonald's Corporation (MCD) — 2026-10-11
## Bear case
The de-rating reflects slowing growth, so it is not a mispricing. Q2-26 comps were only +0.8% in the US and +1.5% in International Operated [Certain], yet the price still implies 9.4% year-1 revenue growth on the reverse DCF [Certain]. The mechanical fair value base of 218.53 sits 7.1% below the 235.23 close, and the bull case of 244.18 offers just +3.8% [Certain]. Cash conversion is slipping: FCF margin fell from 30.6% to 28.0% and FCF/NI from 94.1% to 88.3% as capex rises [Certain]. With net debt/EBITDA at 3.60x and a beta of 0.45, MCD trades like a levered bond proxy. Real yields up 56bp in three months push its discount rate higher (macro overlay) [Likely]. The new federal antitrust suit over AI pricing adds legal risk that is not yet quantified, and it could cause franchisee friction [Guessing]. Momentum is poor: -20.1% over 12 months and below both moving averages [Certain].
## Bull case
This is a 95%-franchised, real-estate-backed royalty machine. ROIC is 17.8%, ROCE 22.7%, operating margin 45.7% and rising, and the Piotroski F-score is 7 [Certain]. Every own-history multiple is below its 5-year minimum: P/E 19.1x vs 25.3x, EV/EBITDA 14.8x vs 18.6x, P/FCF 21.4x vs 28.2x [Certain]. On EV/EBITDA it is 11% cheaper than peers despite better margins [Certain]. The EV/EBITDA method alone values the shares at 323.14 base [Certain]. The DCF leans on a 5.22% risk-free rate and is probably harsh for a business this stable [Likely]. Capital returns stay heavy: $2.6bn of dividends and $1.3bn of buybacks in H1-26, with the share count down 0.73% [Certain]. Comps are still positive, and menu moves (chicken, value) could re-accelerate traffic [Guessing].
## Decision
```json
{
  "ticker": "MCD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A best-in-class franchise royalty business now trades below its own 5-year minimum multiples, but slowing comps, falling cash conversion, 3.60x leverage into rising real yields and a new antitrust suit leave the price above the mechanical base fair value, so the edge is not compelling.",
  "rationale": "Quality is excellent and the multiples are historically low, but the business is cheap for a reason. US comps are +0.8%, FCF conversion is falling, leverage sits at 3.60x while real yields rise, and the price is above the 218.53 base fair value. The probability-weighted upside is negligible. That makes the stock good but not compelling: conviction 3, so AVOID and hold cash.",
  "price_at_decision": 235.23,
  "price_date": "2026-10-09",
  "research_note": "research/MCD/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, under the five-year range of 17.0%-19.7%, showing the franchise returns are eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 43%, under the FY2021 five-year low of 43.7%, showing the royalty margin expansion has reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 43}},
    {"text": "Debt/EBITDA rises above 4.5x, above the five-year range of 3.54x-3.78x, so royalties no longer comfortably carry the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.5}},
    {"text": "US comparable sales (10-Q MD&A) turn negative for two consecutive quarters; or, positively, they re-accelerate clearly above the Q2-26 +0.8% while FCF conversion recovers toward 94%."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 278.7, "basis": "Comps re-accelerate and part of the de-rating reverses (EV/EBITDA 14.8x vs the 5y minimum of 18.6x [RA]), taking the shares back to the July 2026 swing high of 278.70 [HI], still below the EV/EBITDA-method base of 323.14; the probability is cut for the macro overlay's moderate tilt toward bear (research/MCD/2026-10-11-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 235.23, "basis": "Multiples already sit below their 5y minimum (P/E 19.1x vs 25.3x [RA]), which limits further de-rating, while +0.8% US comps (10-Q) limit any re-rating; this is above the mechanical base of 218.53 because the DCF at a 5.22% risk-free rate is harsher than the EV/EBITDA method's 323.14."},
    "bear": {"probability": 0.35, "target_price_12m": 172.2, "basis": "Rising real yields (+56bp 3m, macro overlay research/MCD/2026-10-11-macro.md, which moves probability toward this case) on 3.60x leverage [BS,IS], plus falling FCF conversion (88.3% vs 94.1% [CF,IS]) and antitrust risk, pull the price to the fair-value bear case of 172.20."}
  },
  "entry_price": 174.82,
  "entry_basis": "valuation file: base 218.53 x 0.8, a 20% margin of safety that also prices in the comp slowdown and the leverage/real-yield risk.",
  "replaces": null,
  "replacement_reason": null
}
```

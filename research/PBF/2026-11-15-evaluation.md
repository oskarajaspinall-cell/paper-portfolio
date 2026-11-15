# Evaluation: PBF Energy Inc. (PBF) — 2026-11-15
## Bear case
PBF is a commodity margin business with no pricing power, and the TTM figures are a cyclical peak, not a new base [Likely]. ROIC went from 60.2% (FY2022) to -9.8% (FY2025) and back to 25.3% TTM; the Direction change lines (ROIC, ROCE, operating and FCF margin rising over 12 months against falling 5-year trends) reflect tight product markets and Iran-driven crude discounts, both reversible [Likely]. P/E 3.1x and a 29.61% FCF yield are the classic cheap-on-peak trap [Likely]. The mechanical base fair value of 73.08 is barely above the 71.28 close, with a negative bear value, so the model gives no margin of safety [Certain]. Valuation points from trend strength carry de-rating risk: the price is +28.3% above its 200-day average, and a margin fade would unwind the +84.1% year [Likely]. Shares rose 5.39% YoY and fuel-price politics before the midterms add a cap risk [Likely].
## Bull case
The balance sheet has been rebuilt: net debt/EBITDA 0.05x, Altman Z 3.80, Piotroski 8 [Certain]. Q3 adjusted EBITDA of ~$2.3 billion cut net debt by more than $1.2 billion and the dividend rose 18% (fact-sheet headlines) [Likely]. Refinancing into 0% exchangeable notes lowers interest cost [company-reported] [Certain]. Freight-driven heavy-crude discounts favour US Gulf Coast refiners while the conflict lasts [Guessing]. EV/EBITDA 2.9x sits at 6% of its 5y range and 46% below peers, and the reverse DCF already implies revenue falling 4.2% in year 1, so the price assumes a fade [Certain]. The trend is intact above the 200-day average [Certain]. Even so, there is no moat: the upside depends on how long margins stay elevated, which we cannot forecast with confidence [Guessing].
## Decision
```json
{
  "ticker": "PBF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "ROIC and ROCE fall over 3 years only because FY2023 was near the 2022 cycle peak; the last 12 months rose sharply (ROIC -11.8% to 25.3% [RA-T]) with the balance sheet intact (net debt/EBITDA 0.05x [ST]): a cyclical swing, not lost share.", "moat": "none", "key_risk": "high", "key_risk_text": "Refining margins revert from the Q3 2026 peak (tight product markets, Iran-driven crude discounts), collapsing TTM earnings and de-rating a stock trading well above its 200-day average.", "veto": null},
  "thesis": "A deleveraged refiner on peak-cycle earnings whose low multiples reflect margins the market expects to fade, with no moat to sustain them.",
  "rationale": "Cheap multiples rest on cyclical peak margins with no durable advantage; the mechanical base fair value sits near the price and the bear value is negative. Balance sheet strength limits downside to the business but not to the share price. Scorecard conviction is below the buy bar, so AVOID.",
  "price_at_decision": 71.28,
  "price_date": "2026-11-13",
  "research_note": "research/PBF/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 3%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 3}},
    {"text": "ROIC falls below 10%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 1.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "TTM FCF margin turns negative", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 92.46, "basis": "Margins stay elevated on freight-driven crude discounts (Reuters 2026-11-06 headline) and the price retests its 52-week high of 92.46 [HI]; the mechanical bull of 560.03 is ignored as unreliable."},
    "base": {"probability": 0.4, "target_price_12m": 73.08, "basis": "Margins fade toward the cycle average, as the reverse DCF already implies, leaving the price near the through-cycle base fair value of 73.08 [fact sheet Fair value]."},
    "bear": {"probability": 0.35, "target_price_12m": 34.84, "basis": "Refining margins revert to FY2024-FY2025 levels (operating margin -2.5% FY2025 [IS]), taking the price to the EV/EBITDA bear value of 34.84 [fact sheet Fair value]; the negative DCF bear is floored there by the near-zero net debt."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the business has no moat and its earnings are at a cyclical peak, so a lower price on the same peak earnings would not lift conviction to 4; a re-look needs through-cycle evidence.",
  "replaces": null,
  "replacement_reason": null
}
```

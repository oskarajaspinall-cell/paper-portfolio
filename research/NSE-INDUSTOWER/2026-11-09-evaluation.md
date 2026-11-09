# Evaluation: Indus Towers Limited (NSE:INDUSTOWER) — 2026-11-09
## Bear case
There is no margin of safety: the close of 381.90 sits just below the mechanical base fair value of 397.09, and the bear value of 160.22 shows how wide the range is [Certain]. Every rolling-12-month measure is falling: ROIC 19.9% to 14.1%, operating margin 43.2% to 32.1%, FCF margin 36.8% to 23.6%, with operating margin 17.1pp below its 2-year high [Certain]. Part of this is an inflated FY2025 base from prior-period write-backs, but write-backs imply the carriers had earlier failed to pay, so counterparty credit among Indian operators is the core risk, and customer concentration could not be verified [Likely]. The Africa rollout is new capital with variable timing and costs and no record of returns [Likely]. EV/Sales at 83% and P/B at 69% of their 5y ranges show the stock is not cheap against its own history on those measures [Certain].
## Bull case
Towers are costly to replicate and tenancies are sticky, giving contracted, infrastructure-like economics: gross margin has held near 56.0% [Likely]. The rolling decline mostly reflects one-off write-backs flattering the year-ago base; the latest calls describe growing adjusted EBITDA, strong tower and tenancy orders and lower diesel use (https://stockanalysis.com/quote/nse/INDUSTOWER/transcripts/716786-q2-26-27/) [Likely]. Cash backs earnings: FCF conversion 110.3% TTM, a 7.76% FCF yield, flat share count and net debt/EBITDA of 1.17x [Certain]. EV/EBITDA of 6.7x is at 29% of its 5y range and P/FCF of 12.9x at 26%, far below peers [Certain]. The reverse DCF implies only 1.6% year-1 revenue growth, an undemanding bar for a lessor adding tenancies [Likely]. Beta 0.18 makes it a low-correlation diversifier [Certain].
## Decision
```json
{
  "ticker": "NSE:INDUSTOWER",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The year-ago TTM base was flattered by prior-period write-backs cited on the Q3 FY26 call (https://stockanalysis.com/quote/nse/INDUSTOWER/transcripts/403726-q3-25-26/); the Q2 call reports adjusted EBITDA growth and strong tenancy orders (https://stockanalysis.com/quote/nse/INDUSTOWER/transcripts/716786-q2-26-27/), gross margin is stable at 56.0% [IS] and net debt/EBITDA 1.17x [BS,IS].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Credit and concentration risk on Indian carrier tenants (write-backs signal past collection issues; concentration unverified), plus unproven Africa capital deployment.",
    "veto": null
  },
  "thesis": "A contracted Indian tower lessor with cash-backed earnings and modest leverage trades near its mechanical base fair value after a rolling decline in returns that is largely a one-off base effect, so the business is sound but the price offers no margin of safety.",
  "rationale": "Quality and balance sheet are solid and the rolling decline looks mainly temporary, but the price sits close to base fair value, EV/Sales and P/B are mid-to-high in their own ranges, and carrier credit plus Africa capex are unresolved. The scorecard gives no valuation points; good but not compelling: AVOID.",
  "price_at_decision": 381.90,
  "price_date": "2026-11-08",
  "research_note": "research/NSE-INDUSTOWER/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12% (14.1% now), showing the decline is structural rather than a write-back base effect.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM operating margin falls below 28% (32.1% now), signalling tenant exits or rent pressure.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "Net debt/EBITDA rises above 2.0x (1.17x now), showing Africa capex is being debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "TTM FCF conversion (FCF/NI, cash-flow statement) falls below 80%, signalling receivables or collection stress at carrier tenants."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 481.50, "basis": "Adjusted EBITDA growth and tenancy orders from the Q2 call (https://stockanalysis.com/quote/nse/INDUSTOWER/transcripts/716786-q2-26-27/) lift EV/EBITDA toward its 5y median 7.5x [RA], retesting the 52-week high [HI]; below the mechanical bull 659.45 because that DCF case assumes growth the record does not yet show."},
    "base": {"probability": 0.50, "target_price_12m": 397.09, "basis": "Rents grow slowly and margins stabilise near TTM levels [IS], so the stock converges on the mechanical base fair value [valuation, fact sheet]."},
    "bear": {"probability": 0.25, "target_price_12m": 269.99, "basis": "Carrier credit stress or costly Africa rollout (https://stockanalysis.com/quote/nse/INDUSTOWER/transcripts/716786-q2-26-27/) cuts EBITDA and the stock trades at the EV/EBITDA bear value [fact sheet]; above the blended bear 160.22 because the DCF bear ignores contracted rents."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

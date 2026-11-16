# Evaluation: Yangzijiang Shipbuilding (Holdings) Ltd. (SGX:BS6) — 2026-11-16
## Bear case
Shipbuilding is a deep-cycle business and margins sit at a peak: gross margin rose from 13.8% (FY2021) to 35.2% TTM [IS] [Certain]; the reverse DCF needs 33.2% year-1 revenue growth to justify the price [Certain], and the mechanical base fair value is 2.12 SGD against a 4.32 close [Certain]. Earnings are not turning into cash: FCF margin fell from 21.5% to 8.5% over the last 12 months and FCF conversion is 28.7% of net income [CF-T,IS-T] [Certain]; the cause is unverified [Guessing]. ROIC fell from 65.9% to 40.1% over the year, far below its 2-year high (Direction change) [RA-T] [Certain]. P/FCF 31.7x and P/B 2.7x are above their 5y maxima [RA] [Certain]. The price is 3.2% above its 200-day average after a +29.0% year; if margins slow, a de-rating toward own-history multiples is likely [Likely]. Q3 2026 results were not reviewed [Certain]; China policy risk is unverified [Likely].
## Bull case
Profitability is still rising where it matters: operating margin 32.1% TTM, up 2.4pp in the last year, and ROCE 30.5%, its 2-year high [IS-T,RA-T] [Certain]. That suggests the ROIC and FCF falls reflect the capital base, investment and working-capital timing on a growing order book rather than weaker ship pricing [Guessing]. The balance sheet is net cash (net debt/EBITDA -1.05x), Altman Z 4.16 [Certain], and there is no dilution (shares -0.29% YoY) [Certain]. On earnings it is cheap against peers: P/E 9.3x vs a peer median 13.5x, EV/EBITDA 6.4x vs 8.3x [Certain]. Long-dated order books give revenue visibility [Likely], and the stock is in an uptrend (50-day 18.1% above the 200-day) [Certain]. A re-rating toward peer multiples would be a large gain [Guessing].
## Decision
```json
{
  "ticker": "SGX:BS6",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "ROIC and FCF margin fall while operating margin (+2.4pp) and ROCE (to a 2-year high of 30.5%) rose over the same 12 months [IS-T,RA-T], pointing to capital base and working-capital timing rather than lost pricing; the cash-conversion cause itself is unverified.", "moat": "narrow", "key_risk": "high", "key_risk_text": "Peak-cycle margins mean-revert and the price, priced for 33.2% growth by the reverse DCF, de-rates toward own-history multiples; cash conversion at 28.7% may not recover.", "veto": null},
  "thesis": "A net-cash, high-return shipbuilder cheap versus peers on earnings, but priced well above its own-history and cash-flow value at a likely cyclical margin peak.",
  "rationale": "Quality and balance sheet are strong, but the price sits far above mechanical fair value, cash conversion has collapsed for unverified reasons and margins are cyclical. Peer discount alone does not make the opportunity compelling; the scorecard is well below the buy bar. Cash is acceptable.",
  "price_at_decision": 4.32,
  "price_date": "2026-11-13",
  "research_note": "research/SGX-BS6/2026-11-16.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 26%: the margin cycle is turning.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 26}},
    {"text": "ROIC (TTM) falls below 25%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "Debt/EBITDA (statistics page) rises above 1.5x: leverage builds on a cyclical earnings base.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "FCF conversion does not recover in the next two reported periods (FCF margin stays at or below 8.5%)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 6.27, "basis": "P/E re-rates toward the peer median 13.5x on TTM earnings [RA,P:KRX:329180] as operating margin holds at 32.1% [IS-T]; above the mechanical base because the model assumes reversion the order book may delay."},
    "base": {"probability": 0.45, "target_price_12m": 3.99, "basis": "P/E settles at its 5y median 8.6x [RA] on flat TTM earnings; above the mechanical base 2.12 because margins stay elevated within 12 months on the order book [Likely]."},
    "bear": {"probability": 0.30, "target_price_12m": 2.6, "basis": "Margins and cash conversion keep slipping (FCF margin 8.5% [CF-T]) and multiples fall toward the 5y low P/E 6.7x [RA] on lower earnings, moving toward the mechanical bear-base range 1.73-2.12."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: price is not the only obstacle; the unexplained cash-conversion collapse at a likely cyclical margin peak must resolve first, so a lower price alone would not make it a BUY.",
  "replaces": null,
  "replacement_reason": null
}
```

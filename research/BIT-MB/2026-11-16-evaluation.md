# Evaluation: Mediobanca Banca di Credito Finanziario S.p.A. (BIT:MB) — 2026-11-16
## Bear case
The price is a deal price, not a business price. P/E of 19.1x sits far above its 5y max of 14.0x and the peer median of 11.4x, and P/B of 1.9x is above its 5y max of 1.4x [Certain]. Every mechanical fair-value case (bear 12.28, base 16.74, bull 18.24 EUR) is well below the 27.37 close [Certain]. The trend points come from takeover speculation, and an extended price risks a sharp de-rating if Intesa's offer stalls or is priced on the failed MPS terms, which effectively caps the upside [Likely]. MPS shareholders already rejected one merger route [Likely]. Piotroski F of 3 is weak [Certain]. The Direction change line (FCF margin falling over 5 fiscal years, rising over the last 12 months) is bank funding noise, not a signal either way [Likely]. ROE of 11.8% is only middling [Certain].
## Bull case
ROE has risen from 8.3% to 11.8% and net margin to 41.8% TTM, so the franchise is improving [Certain]. The stock is in a healthy uptrend: 16.2% above its 200-day average, up 52.1% over 12 months, beating SPY by 41.7pp [Certain]. Two credible acquirers (MPS, now Intesa) value the franchise strategically, and a contested process could lift terms [Guessing]. The share count is shrinking slightly (-0.49% YoY) [Certain], and the ECB deposit rate edging up to 2.5% is a minor earnings tailwind (macro overlay, context only) [Likely].
## Decision
```json
{
  "ticker": "BIT:MB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROE is rising over five years (8.3% to 11.8%) [RA]; FCF margin is not a meaningful bank metric and is rising over the last 12 months (-39.2% to 113.3%) [CF-T].",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "The price reflects the MPS/Intesa takeover contest; if the offer fails or is set at the failed MPS terms, the stock de-rates toward a standalone value far below the price.",
    "veto": {"code": "binary_event", "reason": "An unresolved Intesa buyout offer (Reuters 2026-11-11, https://www.reuters.com/legal/transactional/intesas-offer-mediobanca-keep-terms-failed-mps-bid-document-shows-2026-11-11/) drives the price; the outcome is binary and not a fundamental thesis."}
  },
  "thesis": "An improving but middling-return Italian merchant bank priced as a takeover target, far above its own-history and peer multiples and every mechanical fair-value case.",
  "rationale": "The price is driven by a binary takeover process, not the business: multiples sit above their 5y max and above peers, and the base fair value is far below the price. Quality is middling. No position; a lower price would not help while the deal is unresolved.",
  "price_at_decision": 27.37,
  "price_date": "2026-11-13",
  "research_note": "research/BIT-MB/2026-11-16.md",
  "triggers": [
    {"text": "Fiscal-year ROE (ratios page) falls below 9%, giving up most of the rise from 8.3% to 11.8%.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9}},
    {"text": "TTM net margin falls below 35%, under the FY2023 level of 35.3%.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 35}},
    {"text": "Shares change YoY rises above +3%, a sign of dilutive issuance.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}},
    {"text": "The Intesa offer is withdrawn or completed (company or regulatory filing), ending the takeover overhang and allowing a standalone thesis."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 29.22, "basis": "A contested or improved bid lifts the stock back to its 52-week high of 29.22 [HI]; above every fair-value case, so only a deal premium explains it."},
    "base": {"probability": 0.45, "target_price_12m": 26.89, "basis": "Intesa's offer keeps the failed MPS terms (Reuters 2026-11-11) and the price drifts to around its 50-day average of 26.89 [ST,HI]; deal-anchored, which is why it differs from the 16.74 base fair value."},
    "bear": {"probability": 0.30, "target_price_12m": 18.24, "basis": "The offer stalls and the stock de-rates to the mechanical bull fair value of 18.24 [valuation file], still above the 5y median P/B of 1.0x [RA]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the unresolved Intesa takeover makes the outcome binary, so a lower price would not change the decision until the offer is completed or withdrawn.",
  "replaces": null,
  "replacement_reason": null
}
```

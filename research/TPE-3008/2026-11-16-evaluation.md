# Evaluation: Largan Precision (TPE:3008) — 2026-11-16
## Bear case
The price has run far ahead of the business. P/E is 28.0x against a 5y range of 12.0x–21.4x, and EV/EBITDA is 18.8x against a 5y max of 11.8x [RA] [Certain]. Even the mechanical bull fair value (4,790.84 TWD) sits below the 5,310.00 close, and the reverse DCF needs 32.4% year-1 revenue growth [Certain]. Fundamentals are moving the other way: TTM operating margin fell 5.7pp in 12 months to 35.5% and ROIC 7.7pp to 29.7%, 15.6pp below its 2-year high [IS-T, RA-T] [Certain]. This is the latest step in a five-year slide in gross margin from 59.9% to 47.2%, which points to eroding lens pricing power rather than a one-off [Likely]. The extended price risks a sharp de-rating if growth disappoints; the shares already sit 14.7% below the 50-day average after a 7,995.00 peak [HI] [Certain]. Higher real yields add pressure on the multiple (macro overlay, context only) [Likely].
## Bull case
Largan is still a very high-return, cash-rich business: TTM ROIC 29.7%, net debt/EBITDA -4.13x (net cash), Altman Z 11.86 [RA, ST] [Certain]. Cash earnings are holding up better than accounting margins: FCF margin rose 1.3pp in 12 months to 32.5% and FCF conversion is 89.0% [CF-T] [Certain]. The trend is strong, with the price 29.7% above its 200-day average and up 137.6% in 12 months, and the market may be pricing a new product cycle in optics that the trailing figures do not yet show [Guessing]. Buybacks cut the share count 1.82% YoY [ST] [Certain], and insiders own 14.72%, aligning management [Likely].
## Decision
```json
{
  "ticker": "TPE:3008",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "structural",
    "decline_evidence": "ROIC and operating margin falling over 1 year continue a five-year slide in gross margin from 59.9% to 47.2% [IS], pointing to weakening lens pricing power; no guided reset or one-off is documented in the note.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "De-rating: P/E 28.0x and EV/EBITDA 18.8x sit above their own 5y max while margins fall; the price needs 32.4% year-1 growth (reverse DCF), so any growth miss compresses the multiple.",
    "veto": null
  },
  "thesis": "A high-return, net-cash optics leader whose margins are eroding while the share price discounts a strong growth recovery the reported numbers do not show.",
  "rationale": "Quality and balance sheet are excellent, but returns and margins are falling and the multiple sits far above its own history; even the mechanical bull fair value is below the price. The scorecard gives no valuation or trend-strength points, so conviction is well below the buy bar. Cash is the better outcome.",
  "price_at_decision": 5310.00,
  "price_date": "2026-11-13",
  "research_note": "research/TPE-3008/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 33%, confirming the margin slide is continuing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 33}},
    {"text": "TTM ROIC falls below 25%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "TTM FCF margin falls below 25%, ending the cash-earnings resilience.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 7995.00, "basis": "Momentum resumes on a product cycle and the price retests its 2026-09-01 high of 7,995.00 [HI], requiring the 32.4% growth the reverse DCF implies [OV]."},
    "base": {"probability": 0.45, "target_price_12m": 4790.84, "basis": "Partial de-rating toward the mechanical bull fair value of 4,790.84 [valuation file] as falling TTM operating margin (35.5% [IS-T]) caps the multiple."},
    "bear": {"probability": 0.35, "target_price_12m": 2818.68, "basis": "EV/EBITDA reverts toward its own 5y range (median 8.2x [RA]), giving the EV/EBITDA base fair value of 2,818.68 [valuation file]; above the 1,899.09 blended bear since net cash and FCF margin of 32.5% [CF-T] cushion the downside."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the only obstacle: ROIC and operating margin are falling on a structural-looking gross-margin slide, so a lower price alone would not lift conviction to 4; a re-check needs margins to stabilise.",
  "replaces": null,
  "replacement_reason": null
}
```

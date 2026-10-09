# Evaluation: Synchrony Financial (SYF) — 2026-10-09
## Bear case
SYF is not cheap against its own history: 7.5x P/E sits at the 70th percentile of its 5.0x–8.7x 5-year range, and P/B of 1.6x is a 35% premium to peers [Certain]. Returns are normalising downward: ROE fell from 32.0% to 20.8% and net margin from 44.6% to 35.5% [Certain]. Current earnings are flattered by a $174M H1 reserve release while allowance coverage slipped to 10.09%; that tailwind cannot repeat [Likely]. The 109.56 DCF fair value rests on cash-flow inputs the fact sheet cannot show for a lender (FCF [data unavailable]); the P/E method gives only 48.62–72.13, at or below the price [Certain]. Beta of 1.34 and the macro overlay's tightening signal (2y above fed funds) put charge-offs at risk of turning back up [Likely]. Q3 results on Oct 20 are an imminent binary event [Certain].
## Bull case
Credit is improving: net charge-offs fell to 5.43% in H1 2026 from 6.04%, and management guides full-year 2026 below its 5.5–6.0% target range [Certain]. Capital return is heavy: shares outstanding are down 9.79% YoY, with $5.7B of buyback authorisation left and a raised dividend [Certain]. At 7.5x P/E SYF trades 30% below the peer median of 10.8x, and the reverse DCF implies a -7.1% year-one revenue decline that high-single-digit purchase-volume growth does not support [Likely]. Partner wins (Lowe's, PayPal network-wide financing, 30+ renewals) and OpenAI-linked commerce distribution add optionality [Likely]. A 20.8% ROE still supports the P/B premium [Likely].
## Decision
```json
{
  "ticker": "SYF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A 20.8%-ROE card lender with improving charge-offs and 9.79% annual share shrinkage trades at 7.5x P/E, but that is upper-range for its own history, earnings are flattered by reserve releases, and the macro rate path tilts risk to credit.",
  "rationale": "Good, not compelling. The discount is versus peers, not versus its own 5-year range (70th percentile), and the P/E fair value (48.62-72.13) brackets the price. ROE is trending down, reserve releases flatter earnings, and Q3 results land Oct 20. Conviction 3 is below the buy threshold, so cash is the better holding.",
  "price_at_decision": 73.72,
  "price_date": "2026-10-08",
  "research_note": "research/SYF/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE rises above 25% while net charge-offs stay inside management's 5.5-6.0% range, showing returns are re-expanding rather than normalising (would raise conviction).", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 25}},
    {"text": "TTM net margin falls below 29%, under the FY2023 trough of 29.2%, confirming the credit-cost reversal the bear case fears.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 29}},
    {"text": "Net charge-off rate (10-Q) rises above the 6.0% upper bound of management's long-term range for two consecutive quarters while allowance coverage keeps falling."},
    {"text": "A top sales-platform partner (10-Q platform disclosure) is lost or not renewed."}
  ],
  "scenarios": {
    "bull": {"probability": 0.22, "target_price_12m": 88.0, "basis": "Charge-offs fall below the 5.5-6.0% range (note, 10-Q) and P/E re-rates to its 5y max 8.7x [RA] on buyback-boosted EPS (shares -9.79% [ST]), near the 88.77 52-week high [HI]; below the 109.56 DCF base because FCF-based inputs are [data unavailable] for a lender."},
    "base": {"probability": 0.50, "target_price_12m": 75.0, "basis": "P/E holds near its 5y median 7.2x [RA] while buybacks offset normalising ROE (20.8% TTM [RA]), consistent with the 70.28-76.38 band from the P/E base and DCF bear fair values [IS,RA]."},
    "bear": {"probability": 0.28, "target_price_12m": 50.0, "basis": "Rate tightening raises consumer stress, NCOs reverse higher and reserve builds resume, pushing P/E to its 5y min 5.0x [RA], matching the P/E bear fair value 48.62 [IS,RA]; bear probability raised slightly per the macro overlay's small toward-bear tilt (research/SYF/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

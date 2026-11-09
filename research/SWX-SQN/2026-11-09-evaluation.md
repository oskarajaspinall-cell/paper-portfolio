# Evaluation: Swissquote Group Holding SA (SWX:SQN) — 2026-11-09
## Bear case
The last year is falling. ROIC dropped from 20.7% to 18.0% and operating margin from 49.4% to 46.3% [RA-T, IS-T] [Certain], and management lowered 2026 guidance between the March and August calls while H1 revenue barely grew [Likely]. The likely cause is lower Swiss rates squeezing net interest income on client deposits. That is a cyclical headwind, not a broken model, but rate cuts can last for years and nothing yet shows them reversing [Likely]. The FCF margin fall from 296.6% to 159.6% is a deposit-flow artefact and says nothing either way [Likely]. Valuation is the bigger problem. The FCFE base of CHF 41.49 rests on that distorted cash flow. The earnings-based P/E method puts base value at CHF 25.09, below the price [Certain]. P/E of 14.1x is only in line with peers at 14.6x, and it is struck on TTM earnings that the lowered guidance suggests will fall [Likely].
## Bull case
The franchise is not broken. ROE is still 28.0% and operating margin 46.3% [RA, IS] [Certain]. Client assets and net new money kept growing strongly in H1 and the 2028 targets were kept [Likely], so the decline looks like a rate-driven reset on a growing asset base rather than lost share. Insiders own 22.56% and the share count is stable [ST] [Certain]. The stock is down 29.0% over 12 months and P/E sits at the 20th percentile of its 5-year range, below the 15.4x median [RA] [Certain]. The reverse DCF implies only 4.2% year-1 growth [Likely]. A pickup in trading volumes from higher market volatility (macro overlay, context only), or a stabilising rate path, could restore operating leverage quickly [Guessing].
## Decision
```json
{
  "ticker": "SWX:SQN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return Swiss online bank whose falling returns look rate-driven and temporary rather than structural, but whose earnings-based valuation is only fair once lowered guidance is considered, so the skew is positive but not compelling.",
  "rationale": "The dip looks cyclical: lower rates squeeze interest income while client assets keep growing and the balance sheet is intact. But the cheapness comes from deposit-distorted FCF. On earnings the stock trades near peers and its P/E fair value sits below the price, and guidance was lowered. Good, not compelling: conviction 3, no position.",
  "price_at_decision": 33.80,
  "price_date": "2026-11-06",
  "research_note": "research/SWX-SQN/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 42% (46.3% now), showing the rate squeeze is turning into structural margin loss.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 42}},
    {"text": "TTM ROIC falls below 15% (18.0% now), extending the five-year decline from 32.3%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM ROE falls below 22% (28.0% now), undermining the premium P/B against peers.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 22}},
    {"text": "Management cuts 2026 guidance again or withdraws the 2028 targets, or next annual net revenue declines year on year on the income statement."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 45.0, "basis": "Client-asset growth and the kept 2028 targets (H1 2026 transcript) restore earnings growth and P/E re-rates from 14.1x toward the upper half of its 5y range up to 19.9x [RA]; below the mechanical bull of 67.08 because that FCFE value extrapolates deposit-driven FCF."},
    "base": {"probability": 0.5, "target_price_12m": 35.0, "basis": "Earnings dip in line with the lowered 2026 guidance (H1 2026 transcript) and P/E drifts back toward its 5y median 15.4x [RA]; set between the P/E base of 25.09 and the FCFE base of 41.49 because the FCFE base relies on a 159.6% FCF margin that reflects client-deposit flows [CF-T]."},
    "bear": {"probability": 0.25, "target_price_12m": 25.98, "basis": "Swiss rates stay low, operating margin keeps sliding from its 50.2% 2-year high [IS-T] and P/E moves to its 5y low of 12.7x [RA] on lower earnings: the mechanical bear fair value of 25.98 [fact sheet Fair value]."}
  },
  "entry_price": 30.44,
  "entry_basis": "P/E back at its 5y low of 12.7x [RA] on TTM EPS: the price falls in line with the multiple from 14.1x, which on the earnings-based evidence would justify conviction 4; the default FCFE base x 0.8 is not used because that base relies on deposit-distorted FCF.",
  "replaces": null,
  "replacement_reason": null
}
```

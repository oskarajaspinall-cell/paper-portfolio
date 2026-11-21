# Evaluation: Cullen/Frost Bankers, Inc. (CFR) — 2026-11-21
## Bear case
The dip has no company cause: Q3 results, raised guidance and the listing move all date to 2026-10-29, before the fall [Certain]. It looks like a risk-premium de-rating, with VIX 28.4 and the HY spread 3.52% both up over three months (macro overlay) [Certain]. The fall has not made CFR cheap. P/B is 2.3x, 83% above the peer median and 59% of the way up its own 5y range [Certain]. Wider spreads or a falling 2y yield could compress P/B toward its 1.8x low and cut NII guidance [Likely]. Fair value is flagged unreliable (methods disagree 3.2x) and its base of 148.46 is close to the price, so there is no margin of safety [Certain]. The FCF margin Direction change (falling over 5 years, rising to 25.2% TTM) is noisy bank cash flow, not a thesis break [Likely]. Net margin slipped 2.7pp over five years [Certain]. Price sits below its 200-day average [Certain].
## Bull case
CFR is a high-quality deposit franchise. ROE is 16.3% TTM, up from 10.1% in FY2021, and non-interest-bearing deposits are 32.9% of total deposits [company-reported] (https://www.sec.gov/Archives/edgar/data/39263/000003926326000056/cfr-20260930.htm) [Certain]. Q3 brought loan growth, a record pipeline, and raised loan-growth and NII guidance [Likely]. Higher rates help an asset-sensitive bank, and the 2y yield prices hikes (macro overlay) [Likely]. The share count fell 2.26% YoY through buybacks [Certain]. P/E of 13.5x sits 24% of the way up its 5y range, below the 15.1x median [Certain]. The reverse DCF implies -1.6% revenue growth, which raised guidance contradicts [Likely]. The 12-month change is still +19.2%, and RSI 26.3 shows the stock oversold [Certain]. A calmer VIX could re-rate P/E toward its median [Guessing].
## Decision
```json
{
  "ticker": "CFR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROE is rising (16.3% TTM vs 10.1% FY2021). The FCF margin decline is bank cash-flow noise: FCF/NI swung between 19.6% and 147.9% across FY2024-25 and the TTM FCF margin rose from 0.8% to 25.2% over the last 12 months [CF-T]. Q3 guidance was raised (https://stockanalysis.com/stocks/cfr/transcripts/720163-q3-2026/).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "P/B de-rating from a premium to peers (2.3x vs 1.3x) if credit spreads widen or the rate path reverses and NII guidance is cut (macro overlay).",
    "veto": null
  },
  "thesis": "A high-ROE Texas deposit franchise with raised guidance, but the dip has not removed the premium valuation, and with the price below its 200-day average there is no trend strength.",
  "rationale": "The fall has no company-specific cause and the business case is intact, but the stock is still at a large P/B premium to peers. Fair value is unreliable and the base is near the price, and the trend has broken. Good but not compelling: AVOID at conviction 3, with the entry price at base fair value less the margin of safety.",
  "price_at_decision": 144.56,
  "price_date": "2026-11-20",
  "research_note": "research/CFR/2026-11-21.md",
  "triggers": [
    {"text": "TTM ROE (statistics page) falls below 12%, showing the deposit franchise's returns are eroding.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "TTM net margin (statistics page) falls below 26%, showing funding costs or credit losses are compressing profitability.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 26}},
    {"text": "Shares change YoY (statistics page) turns positive: buybacks replaced by dilution.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "Non-interest-bearing deposits fall below 28% of total deposits in the next 10-Q, showing the low-cost funding edge is eroding."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 165, "basis": "Risk appetite recovers and P/E re-rates toward its 15.1x 5y median [RA] on raised NII guidance (macro overlay macro_bull); still below the mechanical bull of 178.64."},
    "base": {"probability": 0.45, "target_price_12m": 148, "basis": "Earnings grow with raised guidance while the P/B premium to peers caps the multiple; in line with the mechanical base fair value of 148.46 [IS,BS,CF,RA,ST,HI]."},
    "bear": {"probability": 0.30, "target_price_12m": 113, "basis": "Credit spreads widen and P/B compresses toward its 1.8x 5y low [RA]; probability raised from a neutral split because the macro overlay's tilt is toward bear (small) as the risk premium rises."}
  },
  "entry_price": 126.19,
  "entry_basis": "valuation file: base 148.46 x 0.85; the obstacle is price, since the business case is intact.",
  "replaces": null,
  "replacement_reason": null
}
```

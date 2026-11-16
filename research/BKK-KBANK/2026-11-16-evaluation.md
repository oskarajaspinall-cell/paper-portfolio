# Evaluation: Kasikornbank PCL (BKK:KBANK) — 2026-11-16
## Bear case
Returns are ordinary: ROE is 8.5% TTM and has sat between 6.9% and 8.6% for five years [RA] [Certain], likely at or below a cost of equity built on a 5.10% risk-free rate plus a 1.5% country premium [Likely]. The stock has re-rated beyond its own history: P/E 12.1x vs a 5y max of 9.8x, P/B 1.0x vs a 0.7x max [RA] [Certain], with no matching rise in ROE. Even the bull fair value of 236.77 THB sits below the 254.00 close [Certain]. The price is extended (+16.7% over its 200-day, +41.8% in 12 months) [ST,HI], so a de-rating toward the 5y median would hurt if Thai growth slows, which the CEO flags alongside fraud risk [Likely]. The Direction change line (FCF margin 94.0pp below its 2-year high) is bank deposit/loan flow noise, so the 12.68% FCF yield is no support [Likely]. Q3 2026 results were not read [Certain].
## Bull case
KBANK is Thailand's second-largest lender with a deposit franchise and digital leadership [Likely]. Net margin has edged up to 33.0% TTM [IS] [Certain], shares are shrinking (-0.60% YoY) [ST] and management cites strong CET1 and active shareholder returns [Likely]. The reverse DCF implies only 0.7% year-1 growth, an undemanding bar [Certain]. The re-rating is sector-wide: P/E and P/B are in line with Thai peers (+1% / -3%) [Certain], so this looks like a sector moving off depressed multiples rather than a stock-specific bubble [Likely]. Momentum is strong, +31.4pp ahead of SPY over 12 months, with the 50-day 12.2% above the 200-day [ST,HI] [Certain]. A low-beta (0.10) domestic bank could keep compounding dividends while Thai banks rerate [Guessing].
## Decision
```json
{
  "ticker": "BKK:KBANK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "scorecard": {"decline_cause": "none", "decline_evidence": "ROE flat over five years (+0.2pp) [RA]; the rolling FCF-margin gap to its 2-year high is bank deposit/loan cash-flow noise, not a decline in earnings power (net margin 33.0% TTM rising) [IS,CF-T].", "moat": "narrow", "key_risk": "high", "key_risk_text": "De-rating: P/E and P/B sit above their 5-year maxima with ROE flat at 8.5%; a slowing Thai economy could send multiples back toward the 5y median.", "veto": null},
  "thesis": "A sound but ordinary-return Thai bank whose shares have re-rated above every point of their own history without any rise in ROE.",
  "rationale": "ROE of 8.5% fails the quality bar, P/E and P/B are above their 5-year maxima and even the bull fair value is below the price. The trend is strong but the extended price carries de-rating risk. Good but not compelling: AVOID.",
  "price_at_decision": 254.00,
  "price_date": "2026-11-13",
  "research_note": "research/BKK-KBANK/2026-11-16.md",
  "triggers": [
    {"text": "ROE TTM falls below 7.0%, the bottom of its five-year range (franchise weakening).", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 7.0}},
    {"text": "Net (profit) margin TTM falls below 29%, signalling credit costs or margin pressure.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 29}},
    {"text": "Shares outstanding rise more than 2% YoY (dilution / capital need).", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 261.00, "basis": "Sector re-rating holds and the stock retests its 52-week high of 261.00 [HI], above the bull fair value of 236.77 because peer multiples (P/E 12.0x median) support the current level [ST]."},
    "base": {"probability": 0.45, "target_price_12m": 216.69, "basis": "Price drifts to the mechanical base fair value of 216.69 [fact sheet Fair value] as ROE stays flat at 8.5% [RA] and the multiple partly normalises."},
    "bear": {"probability": 0.30, "target_price_12m": 166.49, "basis": "Thai slowdown and fraud-related credit costs flagged by the CEO (Reuters, 2025-11-13) push multiples back toward the 5y median P/E 8.8x [RA], near the bear fair value of 166.49."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the only obstacle: ROE of 8.5% sits below the quality bar, so a lower price would not lift this to conviction 4 without higher returns."
}
```

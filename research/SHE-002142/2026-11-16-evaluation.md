# Evaluation: Bank of Ningbo (SHE:002142) — 2026-11-16
## Bear case
Returns are eroding every year: ROE has fallen from 14.6% in FY2021 to 11.9% TTM [Certain] (RA), and nothing in the inputs shows a guided reset or a turn, so this looks like the sector-wide margin squeeze of Chinese banks rather than a one-off [Likely]. Asset quality and capital adequacy are not visible on the fact sheet, so the main bank risk (property and SME credit) is unmeasured [Certain]. The FCF margin direction change (TTM 255.4% vs 313.9% a year earlier) is deposit and loan flow noise, not a signal either way [Likely]. Piotroski F of 4 is mediocre [Certain] (ST). The valuation points come partly from trend strength: price is 6.0% above its 200-day average after a +16.4% year [Certain] (HI); if earnings growth stalls, a re-rating back toward the 5y P/B median of 0.7x is the risk [Likely]. Fair value is flagged unreliable (methods disagree 4.4x) [Certain].

## Bull case
At P/B 0.8x, the 14th percentile of its 5y range, and P/E 7.5x, the price implies -6.6% year-1 revenue growth in the reverse DCF, an undemanding bar [Certain] (RA, fact sheet). Net margin has risen from 48.3% to 53.2% TTM, so profitability per unit of revenue is holding up even as ROE drifts [Certain] (IS). ROE of 11.9% is still respectable for a bank at under book value [Likely]. The P/B + ROE method (the industry's best) gives a base of 41.59 CNY, above the close of 34.15 [Certain]. Momentum is positive: relative strength vs SPY +8.8pp / +4.9pp / +6.0pp over 3m / 6m / 12m with a low beta of 0.58 [Certain] (HI, ST). Dilution is mild at 0.95% YoY [Certain] (ST).

## Decision
```json
{
  "ticker": "SHE:002142",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The falling metric is FCF margin (TTM 255.4% vs 313.9% a year earlier [CF-T]); for a bank it swings with deposit and loan flows (FY2021 -116.6%, FY2025 409.4% [CF,IS]) and is not a business decline (note section 2). The real erosion, ROE 14.6% to 11.9% [RA], is weighed in key_risk.",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "Continued ROE erosion from margin compression and unmeasured asset-quality risk (asset quality not on the fact sheet); a de-rating if growth slows after the trend-driven move above the 200-day average.",
    "veto": null
  },
  "thesis": "A cheap, profitable Chinese regional bank whose returns are steadily eroding, with asset-quality risk the inputs cannot measure.",
  "rationale": "Cheap on P/B and P/E with a positive trend, but ROE falls every year with no evidence of a turn, the moat is unproven and the fair value is unreliable. Good but not compelling: below the buy bar, so AVOID and keep cash.",
  "price_at_decision": 34.15,
  "price_date": "2026-11-13",
  "research_note": "research/SHE-002142/2026-11-16.md",
  "triggers": [
    {"text": "ROE (TTM) falls below 10%, confirming the return erosion is accelerating", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "Net margin (TTM) falls below 48%, ending the margin support", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 48}},
    {"text": "Shares change YoY rises above 3%, signalling a recapitalisation", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}},
    {"text": "A filing shows ROE stabilising or rising year on year with no deterioration in asset quality (would make the erosion temporary and could lift conviction)"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 45.66, "basis": "ROE stabilises and the market pays the mechanical base fair value of 45.66 [fact sheet fair value], supported by the P/B + ROE base of 41.59 and FCFE base of 53.81."},
    "base": {"probability": 0.5, "target_price_12m": 38.0, "basis": "Net margin holds near 53.2% [IS] while ROE drifts; price moves toward the fair-value bear of 37.99, below the base because that base is flagged unreliable (methods disagree 4.4x)."},
    "bear": {"probability": 0.25, "target_price_12m": 29.9, "basis": "ROE keeps falling toward the trigger and P/B de-rates from 0.8x to its 5y median of 0.7x [RA], near the 6-month low of 29.29 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the default anchor (base 45.66 x 0.8) is above the current price, and the issue is falling ROE with no evidence of a turn and unmeasured asset quality; a lower price would not change the decision without a stabilising ROE.",
  "replaces": null,
  "replacement_reason": null
}
```

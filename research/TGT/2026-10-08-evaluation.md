# Evaluation: Target Corporation (TGT) — 2026-10-08
## Bear case
The pullback has broken structure, not just cooled: the close of 150.92 sits below both recent swing lows (153.55, 153.96), so the clean "bounce off the 50-day" pattern has already failed [Certain]. The trigger for the dip was Target's own cut of prices on nearly 2,000 items, which points at margin, and margin has been falling for five years: operating margin 8.5% to 5.0% TTM, ROIC 31.8% to 13.2% [Certain]. Short interest rose 22.3% in a month, so more traders are betting on this risk [Certain]. The macro overlay finds real yields up 61bp and HY spreads up 36bp over 3m. That is a moderate headwind for exactly the budget-constrained shopper the cuts target [Likely]. The 167.83 target needs a near-retest of the 170.75 August high within 41 sessions, before Nov 18 earnings [Likely].
## Bull case
The long trend is intact: +70.5% over 12 months, the 50-day MA 20.5% above the 200-day, and +54.8pp of relative strength versus SPY [Certain]. RSI of 42 and a 3.6% discount to the 50-day MA sit squarely in the pullback band [Certain]. Valuation is not crowded: 15.7x P/E sits at the 18th percentile of its own 5y range and 57% below the peer median, so gap risk from de-rating is limited [Certain]. Traffic data reportedly show Target winning shoppers from rivals, and the price cuts pressured Walmart, which suggests share gains [Likely]. ATR at 2.2% keeps the volatility-based stop reasonable [Certain].
## Decision
```json
{
  "ticker": "TGT",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A strong 12-month uptrend has pulled back below the 50-day average, but the dip is driven by margin-dilutive price cuts and has already broken recent swing lows, so the bounce edge is unclear.",
  "rationale": "The setup qualifies mechanically, but the edge is weak. Price has broken both recent swing lows, the dip comes from Target's own margin-dilutive price cuts, short interest is rising, and the macro overlay tilts moderately bearish. The 2:1 target needs a near-retest of the August high within 41 sessions. Conviction 3: below the buy threshold, so AVOID.",
  "price_at_decision": 150.92,
  "price_date": "2026-10-07",
  "research_note": "research/TGT/2026-10-08.md",
  "exit_plan": {"target": 167.83, "stop": 142.47, "time_limit": "2026-11-18"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 170.75, "basis": "Price cuts win share from rivals and the uptrend resumes to retest the 52-week high of 170.75 [HI], helped by a P/E of 15.7x that sits at only the 18th percentile of its 5y range [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 150.92, "basis": "EV/EBITDA stays near its 5y median of 9.7x against a current 9.6x [RA], and operating margin holds near 5.0% TTM [IS], leaving the price roughly flat."},
    "bear": {"probability": 0.30, "target_price_12m": 124.0, "basis": "Price cuts extend the five-year margin decline (operating margin 8.5% to 5.0% [IS]) and P/E falls to its 5y minimum of 12.9x [RA]; bear probability raised moderately per the macro overlay's tilt toward bear (real yields +61bp/3m, HY spreads +36bp/3m, research/TGT/2026-10-08-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

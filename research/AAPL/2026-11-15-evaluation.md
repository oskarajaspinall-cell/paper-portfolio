# Evaluation: Apple Inc. (AAPL) — 2026-11-15
## Bear case
The price is the problem. P/E of 39.7x and EV/EBITDA of 29.9x sit above their 5y maximums; the reverse DCF needs 33.0% year-1 revenue growth [Certain]. An extended price risks a de-rating if growth slows: per the macro overlay, a P/E back at its 5y median of 33.8x costs about -15% with no earnings change, and the 10y real yield is up 0.47pp in 3m [Likely]. Part of the bid is a safe-haven rotation out of AI names, which can reverse [Guessing]. The 10-K adds risks on rising chip and memory costs, tariffs and a semiconductor investigation, with Greater China about 17% of sales [company-reported] [Likely]. ROIC is 10.4pp below its 2-year high and ROCE slipped over the last 12 months (68.7% -> 67.4%) [Certain]; a growing capital base, not lost share, appears to drive it, so it does not yet threaten the thesis [Likely].

## Bull case
Apple is a very good business that is working. TTM ROIC is 93.9%, gross margin rose from 43.3% to 48.8% over five years, operating margin is 33.0% and the FCF margin rose from 23.7% to 28.4% over the last year [Certain]. Services carries a 76.2% gross margin [company-reported] and the ecosystem's switching costs protect it [Likely]. The balance sheet is near net cash on either definition and the share count fell 1.90% [Certain]. The trend is healthy, not severely overextended: +18.3% over the 200-day average, +30.3% over 12 months and +19.9pp ahead of SPY, with a 2.63% FCF yield [Certain]. The mechanical fair value of 180.00 is flagged unreliable (methods disagree 2.5x); its DCF ignores how buybacks and a rising services mix compound per-share value, while the EV/EBITDA method alone gives 298.03 [Likely].

## Decision
```json
{
 "ticker": "AAPL",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "ROIC, operating margin and FCF margin all rose over the last 1 and 3 years [RA-T, IS-T, CF-T]; ROIC sits below its 2-year high and ROCE dipped as the capital base grew, with margins still rising.",
  "moat": "wide",
  "key_risk": "medium",
  "key_risk_text": "De-rating: P/E and EV/EBITDA sit above their 5y maximums and the price implies 33.0% year-1 growth, so slower growth or higher real yields could compress the multiple toward its 5y median with no change in earnings.",
  "veto": null
 },
 "thesis": "An exceptionally profitable, near-net-cash ecosystem franchise with rising margins and a strong uptrend, priced above its own 5-year multiple range.",
 "rationale": "Scorecard conviction 4: top quality, near-net-cash, wide moat and trend strength in place of a discount. The skew is modest and the de-rating risk real, so the evidence supports only the standard core size, which Python sets from volatility.",
 "price_at_decision": 356.27,
 "price_date": "2026-11-13",
 "research_note": "research/AAPL/2026-11-15.md",
 "triggers": [
  {
   "text": "TTM operating margin falls below 30%, reversing the five-year expansion to 33.0%.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 30
   }
  },
  {
   "text": "TTM ROIC falls below 75%, back under the FY2023 level of 75.2%.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 75
   }
  },
  {
   "text": "TTM FCF margin falls below 23%, under the FY2025 low of 23.7%.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 23
   }
  },
  {
   "text": "Greater China net sales fall year on year in a 10-Q while iPhone net sales also fall."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 400,
   "basis": "Margins keep rising [IS-T] and the trend holds, so the P/E stays near 39.7x [RA] while buybacks shrink the share count [ST]."
  },
  "base": {
   "probability": 0.45,
   "target_price_12m": 350,
   "basis": "Earnings grow but the multiple drifts from above its 5y max toward the top of its range [RA]; well above the unreliable mechanical base of 180.00, nearer the EV/EBITDA method's 298.03 [fact sheet fair value]."
  },
  "bear": {
   "probability": 0.3,
   "target_price_12m": 290,
   "basis": "P/E falls to its 5y median of 33.8x [RA] on higher real yields or a rotation back into AI; probability raised a little for the macro overlay's small bear tilt (research/AAPL/2026-11-15-macro.md)."
  }
 },
 "replaces": null,
 "replacement_reason": null,
 "second_opinion": {
  "file": "research/AAPL/2026-11-15-evaluation-2.md",
  "conviction": 4
 }
}
```

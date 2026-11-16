# Evaluation: Toyo Suisan Kaisha (TYO:2875) — 2026-11-16
## Bear case
The margin step-up is unexplained: operating margin went from 8.2% (FY2022) to 16.6% TTM [IS] and the cause (pricing, mix, input costs) is not verified, so part of it may be a cost tailwind that reverses [Guessing]. ROIC at 23.4% TTM sits 2.6pp below its 2-year high of 26.0% [RA-T]; it is +0.7pp on a year ago, a plateau rather than a decline, but it says peak returns may be behind [Likely]. FCF conversion is lumpy (61.7% in FY2026, 86.1% TTM) [CF] [Certain]. P/B 2.0x is at the top of its 5y range [RA] [Certain]. There is no trend support: price is 0.8% below its 200-day average and lags SPY by 4.6pp over 12 months [HI] [Certain]. Overseas exposure is unquantified, so yen and US-consumer risk can't be sized (macro overlay) [Likely]. The mechanical bear value is -22.6% [Certain].
## Bull case
A net-cash staple (net debt/EBITDA -2.23x, Altman Z 9.38) with ROIC 23.4% and operating margin and ROCE at 2-year highs [RA-T,IS-T] [Certain]. Valuation is undemanding: P/E 14.3x at the 6th percentile of its 5y range and 42% below peers; P/FCF 16.3x below its 5y minimum; FCF yield 6.14% [RA,ST] [Certain]. The reverse DCF needs only 0.8% year-1 revenue growth [Likely]. Shares fell 2.66% YoY from buybacks [ST] [Certain]. Base fair value 12,653.89 JPY is +18.8% above the close [Likely]. Beta 0.25 makes it a low-risk diversifier [Certain].
## Decision
```json
{
 "ticker": "TYO:2875",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "new_evidence": {
  "type": "method_change",
  "text": "The earlier AVOID 3 (2026-11-07) predates the scorecard (2026-11-09); conviction is now set by scripts/scorecard.py on the 2026-11-16 fact sheet."
 },
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "ROIC is +0.7pp on a year ago and +5.9pp over 3 years; operating and FCF margin are at 2-year highs [RA-T, IS-T, CF-T]. The gap to the 2-year ROIC high is a plateau, not a decline.",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "The unexplained margin expansion (operating margin 8.2% to 16.6%) partly reverses if input costs or price competition normalise, taking ROIC back toward its pre-2024 level.",
  "veto": null
 },
 "thesis": "A net-cash, high-ROIC Japanese noodle and food maker trading at the low end of its own P/E range and well below peers.",
 "rationale": "High and stable returns, net cash, buybacks and a P/E near its 5y low give scorecard conviction 4 on a real own-history discount; no trend support is needed. Sized by Python at the conviction-4 core size, vol-scaled. Cash, holdings count and the staples sector have room, so no replacement.",
 "price_at_decision": 10655.0,
 "price_date": "2026-11-13",
 "research_note": "research/TYO-2875/2026-11-16.md",
 "triggers": [
  {
   "text": "ROIC (TTM) falls below 18%",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 18
   }
  },
  {
   "text": "Operating margin (TTM) falls below 14%",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 14
   }
  },
  {
   "text": "FCF margin (TTM) falls below 6%",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 6
   }
  },
  {
   "text": "Balance sheet levers up: debt/EBITDA (statistics page) rises above 1x, ending the net cash position",
   "check": {
    "source": "statistics",
    "field": "debtEbitda",
    "op": ">",
    "value": 1
   }
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 14116.31,
   "basis": "Margins hold at 2-year highs and P/E re-rates toward its 5y median 17.1x [RA], matching the mechanical bull fair value [valuation file]."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 12653.89,
   "basis": "ROIC plateaus near 23.4% [RA-T] and the price converges on the DCF/P/E base fair value; the reverse DCF's 0.8% growth is undemanding."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 8249.82,
   "basis": "Bear case: the unexplained margin gain [IS] partly reverses and the mechanical bear fair value applies."
  }
 },
 "replaces": null,
 "replacement_reason": null,
 "second_opinion": {
  "file": "research/TYO-2875/2026-11-16-evaluation-2.md",
  "conviction": 4
 }
}
```

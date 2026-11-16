# Evaluation: Rolls-Royce Holdings plc (LON:RR) — 2026-11-16
## Bear case
The turnaround is priced in. EV/EBITDA of 20.3x sits at 96% of its 5y range and EV/Sales and P/FCF are above their 5y maxima [Certain] [RA]; at a 3.96% FCF yield [ST], any slowdown in margin gains could de-rate the multiple toward its 5y median of 15.5x [Likely]. Trend strength is thin: the close is only +0.8% above the 200-day average, and the stock is down 11.4% over 3 months after Safran and GE Aerospace flagged aviation risks [Certain] [HI]. No mechanical fair value is computable [Certain], so the margin of safety cannot be checked. Net margin fell from 27.5% (FY2025) to 13.1% TTM, though operating and FCF margins are still rising [Certain] [IS]. A narrowbody re-entry adds development cost and execution risk [Likely]. Revenue by country is unverified, so USD exposure is unknown [Guessing]. Results due Nov 20 add a near-term event [Certain].
## Bull case
The quality is real and still improving: operating margin rose from 4.1% (FY2021) to 20.7% TTM, FCF margin to 19.3%, ROCE to 24.8%, and every rolling-12-month metric is rising [Certain] [IS-T, RA-T]. The balance sheet moved from 5.28x net debt/EBITDA to net cash (-0.41x) [Certain] [BS]. The installed base of widebody engines on long-term service agreements gives decades of aftermarket revenue rivals cannot easily take [Likely]. The 12 November update reaffirmed guidance, reported an engine backlog of around 2,500 and launched a multi-year buyback [Likely] (https://www.reuters.com/business/aerospace-defense/rolls-royce-announces-15-billion-buyback-engine-demand-grows-2026-11-12/). P/FCF is -7% vs peers and P/E sits at 36% of its own 5y range [Certain] [RA]. The 12-month change of +21.5% beats SPY [Certain] [ST].
## Decision
```json
{
 "ticker": "LON:RR",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "Python finds no falling ROIC, operating margin or FCF margin; the rolling-12-month table shows all rising [RA-T, IS-T, CF-T].",
  "moat": "wide",
  "key_risk": "medium",
  "key_risk_text": "De-rating: EV/EBITDA at 96% of its 5y range with only a thin uptrend, so a slowdown in margin gains or a soft aviation outlook (Nov 20 results) compresses the multiple.",
  "veto": null
 },
 "thesis": "A net-cash, wide-moat engine franchise with every rolling margin and return still rising is a good business that is working, in an uptrend above its 200-day average with a real FCF yield and a multi-year buyback.",
 "rationale": "Scorecard conviction 4: top quality, rising direction, net cash, a wide moat and trend strength outweigh a full multiple, which the medium key risk reflects. Standard core size, volatility-scaled by Python. Cash after the pending order covers it and Industrials stays well under the cap, so nothing is replaced. [Second opinion: conviction 3; a  BUY needs both evaluations at 4+.]",
 "price_at_decision": 1350.6,
 "price_date": "2026-11-13",
 "research_note": "research/LON-RR/2026-11-16.md",
 "triggers": [
  {
   "text": "TTM operating margin falls below 16% (20.7% now), reversing the turnaround.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 16
   }
  },
  {
   "text": "TTM FCF margin falls below 14% (19.3% now), showing service cash generation weakening.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 14
   }
  },
  {
   "text": "Net debt/EBITDA rises above 1.0x (-0.41x now), ending the net-cash position.",
   "check": {
    "source": "statistics",
    "field": "debtEbitda",
    "op": ">",
    "value": 1.0
   }
  },
  {
   "text": "TTM ROCE on the ratios page falls below 18% (24.8% now), or guidance is cut in a results release."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 1650,
   "basis": "Margins keep rising and EV/EBITDA holds near its 5y max of 20.7x [RA] on higher TTM EBITDA [IS], with the buyback shrinking the share count."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 1400,
   "basis": "EBITDA growth is offset by modest multiple compression from 20.3x toward peers at 16.6x [RA]; no fair value is computable, so this rests on the stock's own multiples."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 1030,
   "basis": "Aviation risks flagged by Safran and GE Aerospace bite and EV/EBITDA reverts to its 5y median of 15.5x [RA] on flat TTM EBITDA [IS]."
  }
 },
 "replaces": null,
 "replacement_reason": null,
 "second_opinion": {
  "file": "research/LON-RR/2026-11-16-evaluation-2.md",
  "conviction": 3
 },
 "entry_price": null,
 "entry_basis": "Second opinion at conviction 3: no entry price set."
}
```

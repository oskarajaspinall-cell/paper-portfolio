# Evaluation: Nordex SE (ETR:NDX1) — 2026-11-09
## Bear case
Nordex is a cyclical onshore turbine OEM priced off its best-ever year. Four of the last five fiscal years were losses or near-zero profit, and the 10.1% TTM operating margin is a peak, not a proven through-cycle level [Certain]. FCF at 200.6% of net income likely rests on customer prepayments that reverse when orders slow [Guessing]. The mechanical bear fair value is negative, so the downside if margins revert is large [Certain]. P/B and EV/Sales sit above their 5y maxima, and the P/E history is distorted by loss years, so "below its 5y P/E range" flatters the cheapness [Certain]. Shareholders were diluted 12.14% in a year [Certain]. The 103.0% rolling ROIC reflects a tiny invested-capital base, not franchise economics [Likely]. Management cites execution, permitting and policy uncertainty, and Turkish and US exposure is unsized per the macro overlay [Likely]. Nothing is falling; the risk is reversal.

## Bull case
The turnaround is real and still accelerating: every rolling metric is at its 2-year high, operating margin up from 4.3% a year earlier to 10.1%, FCF margin to 11.7% [Certain]. Q3 2026 revenue rose and FY2026 EBITDA margin guidance was raised to 11.5%-12.5%, with order intake and backlog growing [Likely] (Q3 2026 transcript headline in fact sheet). The balance sheet is net cash at -2.41x net debt/EBITDA [Certain]. At 8.4x EV/EBITDA and a 9.71% FCF yield the stock trades well below the peer median of 18.4x and at a discount on P/E and P/FCF [Certain]. The reverse DCF implies -5.9% year-1 revenue growth, i.e. the price already discounts a downturn the order book does not show [Likely]. A growing service fleet adds recurring, higher-margin revenue [Likely]. Base fair value 55.81 EUR sits well above the 42.98 close [Certain].

## Decision
```json
{
 "ticker": "ETR:NDX1",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "Python finds no falling metric: ROIC, operating margin and FCF margin are all rising on the 1y and 3y rolling view [RA-T, IS-T, CF-T].",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Cyclical margin and working-capital reversal: peak-like margins and prepayment-driven FCF in a competitive turbine market with a loss-making history; management flags execution, permitting and policy risk.",
  "veto": null
 },
 "thesis": "A recovered, net-cash onshore wind OEM with margins still rising and raised guidance trades well below peers on EV/EBITDA and at a high FCF yield, while the price implies a revenue decline its growing backlog does not show.",
 "rationale": "Scorecard conviction 4: strong and rising returns, net cash and a discount to peers and to base fair value outweigh the cyclical peak-margin risk and dilution. Bear target reflects that downside. Python sizes the position, scaled for volatility; no cap is breached, so no replacement. [Second opinion: conviction 3; a  BUY needs both evaluations at 4+.]",
 "price_at_decision": 42.98,
 "price_date": "2026-11-06",
 "research_note": "research/ETR-NDX1/2026-11-09.md",
 "triggers": [
  {
   "text": "TTM operating margin falls below 6%, giving up most of the recovery from 2.3% in FY2024 to 10.1% TTM.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 6
   }
  },
  {
   "text": "TTM gross margin falls below 20%, back under the FY2024 level of 20.5%, signalling turbine pricing has cracked.",
   "check": {
    "source": "statistics",
    "field": "grossMargin",
    "op": "<",
    "value": 20
   }
  },
  {
   "text": "TTM FCF margin falls below 3%, under the FY2024 level of 3.6%, showing prepayment-driven cash has reversed.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 3
   }
  },
  {
   "text": "Net debt/EBITDA rises above 1.0x, losing the net-cash position (-2.41x TTM).",
   "check": {
    "source": "statistics",
    "field": "debtEbitda",
    "op": ">",
    "value": 1.0
   }
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 62.81,
   "basis": "Guidance-raised margins hold and backlog converts, reaching the mechanical bull fair value 62.81 EUR [IS,CF,RA] (fact sheet fair value table)."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 48.0,
   "basis": "Margins plateau near TTM; below the 55.81 EUR mechanical base because the DCF capitalises prepayment-flattered FCF (FCF/NI 200.6% [CF,IS]), so weighted toward the EV/EBITDA value of 39.80 EUR [RA]."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 30.0,
   "basis": "Orders slow, working capital reverses and margins fall back toward FY2024 levels (operating 2.3% [IS]); mechanical DCF bear is negative, so this sits below the EV/EBITDA bear 37.82 EUR and the 6-month low 33.24 EUR [HI]."
  }
 },
 "replaces": null,
 "replacement_reason": null,
 "second_opinion": {
  "file": "research/ETR-NDX1/2026-11-09-evaluation-2.md",
  "conviction": 3
 },
 "entry_price": null,
 "entry_basis": "Second opinion at conviction 3: no entry price set."
}
```

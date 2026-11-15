# Evaluation: Visa Inc. (V) — 2026-11-15
## Bear case
The price has run ahead of the business. P/E of 34.8x, EV/EBITDA of 25.5x and P/FCF of 36.4x all sit above their 5y maximums, and the FCF yield is only 2.75% [Certain]. The reverse DCF needs 23.6% year-one revenue growth, far above Visa's recent pace [Likely]. Even the mechanical bull fair value of 290.25 is below the close [Certain]. The price is 22.7% above its 200-day average after a 6-month gain of 32.9%: an extended stock like this de-rates hard if growth slows [Likely]. The direction change is real: FCF margin fell 5.9pp to 48.1% in the last 12 months and conversion to 93.8% [Certain], for a cause the note could not pin down [Guessing]. The 10-K expanded risk factors on the Reg II debit cap, a Fed proposal for further cuts and the Credit Card Competition Act [Certain]. Rising real yields are a multiple headwind (macro overlay, context only) [Likely].
## Bull case
This is a good business that is working. ROIC rose from 40.1% to 56.4% and is at its 2-year high on a rolling basis; ROCE is up 7.0pp in a year [Certain]. Gross margin 97.7% and operating margin 66.3% are flat over five years, so the FCF slip sits between earnings and cash (legal settlements, tax items, one-off event marketing), not in pricing power [Likely]. Net debt/EBITDA is 0.28x, Altman Z 8.32, and the share count fell 3.00% YoY [Certain]. The two-sided network is being extended into agentic commerce (OpenAI's wallet accepts Visa) and value-added services [Likely]. The trend is strong: +25.6% over 12 months and +15.2pp vs SPY [Certain]. The P/E-method fair value of 339.31 to 351.60 is far closer to the price than the DCF, which is harsh on a capital-light compounder [Likely].
## Decision
```json
{
 "ticker": "V",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "temporary",
  "decline_evidence": "FCF margin fell to 48.1% while operating margin (66.3%) and net margin are flat and ROIC is at its 2-year high [RA-T, IS-T]; the 10-K links the year's cash/tax items to legal settlements and one-off event marketing (https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm), though no single cause is confirmed.",
  "moat": "wide",
  "key_risk": "medium",
  "key_risk_text": "US interchange regulation (a lower Reg II debit cap, the Credit Card Competition Act) cutting network economics, combined with a de-rating from multiples above their 5y maximums if growth slows.",
  "veto": null
 },
 "thesis": "Visa is a wide-moat, unlevered network with ROIC at a 2-year high, flat margins and a strong uptrend, a good business that is working, bought on trend strength rather than a discount.",
 "rationale": "The scorecard reaches 4 on quality, balance sheet, moat and trend strength, not on value: every multiple is above its 5y range, so the bear case's de-rating and interchange-regulation risks are real. Conviction 4 gives the standard core size, volatility-scaled by Python; no cap is breached, so nothing is replaced.",
 "price_at_decision": 425.76,
 "price_date": "2026-11-13",
 "research_note": "research/V/2026-11-15.md",
 "triggers": [
  {
   "text": "TTM ROIC falls below 45%, giving up most of the rise from 40.1% (FY2022) to 56.4% and signalling network pricing erosion.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 45
   }
  },
  {
   "text": "TTM FCF margin falls below 42%, extending the slide from 53.9% a year earlier to 48.1% and showing the cash gap is structural.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 42
   }
  },
  {
   "text": "TTM operating margin falls below 62%, under the flat five-year band around 66.3%-67.2%, showing client incentives or regulation compressing network economics.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 62
   }
  },
  {
   "text": "A final US rule or court decision materially lowers the Reg II debit interchange cap, or the Credit Card Competition Act is enacted."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 470.0,
   "basis": "ROIC keeps rising (56.4% TTM [RA-T]) and value-added services and agentic commerce extend growth, so P/E holds near today's 34.8x [RA] on higher earnings, above the 52-week high of 442.23 [HI]."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 400.0,
   "basis": "Earnings keep compounding but P/E eases back toward its 5y max of 33.0x [RA] as rising real yields weigh (macro overlay, context only), leaving the price near the 50-day average of 390.36 [ST,HI]; above the DCF base of 222.83 because that model ignores the moat and buybacks (-3.00% shares [ST])."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 339.31,
   "basis": "Interchange regulation advances (10-K risk factors, https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm) and the FCF slide continues, compressing P/E toward its 5y median of 27.8x [RA], the P/E-method base fair value of 339.31 [fact sheet]."
  }
 },
 "replaces": null,
 "replacement_reason": null,
 "second_opinion": {
  "file": "research/V/2026-11-15-evaluation-2.md",
  "conviction": 4
 }
}
```

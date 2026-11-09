# Evaluation: China Resources Beer (Holdings) Company Limited (HKG:0291) — 2026-11-09
## Bear case
Earnings below the operating line are eroding and the cause is unexplained: net margin fell from 13.7% to 7.2% TTM and ROE from 20.1% to 6.3% while operating margin held [Certain]. Until the charges are identified, P/E of 21.4x sits 23% above peers, so the stock is not cheap on earnings [Certain]. ROIC is down from 16.0% (FY2022) to 11.9% TTM, with a flat last year [Certain]. The 52-week change is -21.5% and the reverse DCF prices -6.9% year-1 revenue growth, consistent with a China beer volume or pricing-war risk that could prove structural [Guessing]. The CNY reporter carries a 3.5% country premium [Certain]. Results are due Nov 13, 2026, an event within days of any entry [Certain]. The 50-day average sits 18.1% below the 200-day [Certain].
## Bull case
The operating business is improving: gross margin rose from 39.2% to 42.3% and operating margin from 9.0% to 14.9% TTM; the rolling FCF margin is at its 2-year high of 15.3%, up from 12.9% [Certain]. The balance sheet is net cash (net debt/EBITDA -1.55x) [Certain]. Cash multiples are below their own 5y minimums: EV/EBITDA 6.1x, EV/Sales 1.3x and P/FCF 10.0x, all below peers, with a 9.96% FCF yield [Certain]. The mechanical base fair value of 34.56 HKD is well above the 20.92 close, and the price implies shrinkage that rising margins and cash flow do not show [Likely]. Scale and distribution density in a regional oligopoly give a narrow moat [Likely]. The ROIC dip looks temporary: it has turned back up from 10.4% (FY2025) with the balance sheet intact [Likely].
## Decision
```json
{
 "ticker": "HKG:0291",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "Nothing is falling on the 1y/3y view: ROIC is below its FY2022 16.0% but recovered from 10.4% (FY2025) to 11.9% TTM, while operating margin (14.9%) and rolling FCF margin (15.3%, 2-year high) are rising and the balance sheet is net cash [RA, IS-T, CF-T, BS].",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "China beer volume or price competition plus unexplained below-the-line charges (net margin 7.2% TTM vs 13.7% FY2021) keep earnings depressed, so the cash-multiple discount persists.",
  "veto": null
 },
 "thesis": "A net-cash Chinese brewer with rising operating and FCF margins trades below its own 5-year minimum cash multiples, pricing shrinkage that its improving operations do not show.",
 "rationale": "Scorecard conviction 4: net cash, rising operating and FCF margins and cash multiples below their 5y minimums outweigh unexplained net-margin erosion and results due within days. Python sizes it; it would breach the China/HK cap, so it replaces HKG:2076.",
 "price_at_decision": 20.92,
 "price_date": "2026-11-06",
 "research_note": "research/HKG-0291/2026-11-09.md",
 "triggers": [
  {
   "text": "TTM operating margin falls below 12.0% (14.9% now), reversing the mix and pricing gains.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 12.0
   }
  },
  {
   "text": "TTM FCF margin falls below 10.0% (15.3% now), showing the cash step-up was transitory.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 10.0
   }
  },
  {
   "text": "TTM ROIC falls below 10.0% (11.9% now), below the FY2025 low of 10.4%.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 10.0
   }
  },
  {
   "text": "Net debt/EBITDA rises above 0.0x (net cash lost).",
   "check": {
    "source": "statistics",
    "field": "debtEbitda",
    "op": ">",
    "value": 0.0
   }
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.2,
   "target_price_12m": 34.56,
   "basis": "Results explain the below-the-line charges as one-offs and cash multiples recover toward history, reaching the blended base fair value of 34.56 HKD (fact sheet Fair value)."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 28.65,
   "basis": "Operating and FCF margins hold near 14.9% and 15.3% [IS-T, CF-T] and the price moves to the DCF base of 28.65 HKD, below the blend because the EV/EBITDA method assumes a re-rating to a 5y median the stock has not traded near."
  },
  "bear": {
   "probability": 0.3,
   "target_price_12m": 16.82,
   "basis": "China volume or price competition plus continued net-margin erosion (7.2% TTM [IS]) keep EV/EBITDA below its 5y minimum, toward the mechanical bear of 16.82 HKD (fact sheet Fair value)."
  }
 },
 "replaces": "HKG:2076",
 "replacement_reason": "Adding this name would take China/HK combined above the 25% country cap. HKG:2076 has risen the most of the China/HK holdings since entry, while this idea trades below its own 5y minimum cash multiples with net cash and a low-beta (0.38) staples profile, a better skew from here.",
 "second_opinion": {
  "file": "research/HKG-0291/2026-11-09-evaluation-2.md",
  "conviction": 4
 }
}
```

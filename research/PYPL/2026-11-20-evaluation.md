# Evaluation: PayPal Holdings, Inc. (PYPL) — 2026-11-20

## Bear case
Branded checkout, the high-margin core, is losing ground: the Q3 10-Q shows PayPal-branded revenue falling on mix, merchant incentives and lower FX fees while lower-margin Braintree grows [Certain]. Gross margin has fallen 5.5pp over five years and rolling operating margin is down 1.0pp year on year [Certain]. The fall to the entry price came with the 2026-11-20 leadership overhaul: the CFO is replaced and the Chief Risk Officer departs with only an interim head, mid-reorganisation, just as the 10-Q adds a cyberattack risk factor [Likely]. Leverage has crept from 0.28x to 0.61x after the May 2026 debt issue; Altman Z is 1.93 [Certain]. The price is still 11.8% above its 200-day average after a +27.0% six-month run; if branded share keeps slipping, that trend can unwind and the multiple stay at its floor [Likely]. A low multiple may be a value trap [Guessing].

## Bull case
PayPal is a high-return cash machine priced for no growth: TTM ROIC 21.8%, FCF yield 13.45%, P/E 10.5x at its 5-year minimum and P/FCF 7.4x below it [Certain]. The reverse DCF implies roughly zero year-1 revenue growth [Certain]. The FCF-margin direction change favours the bull: rolling FCF margin rose from 16.9% to 18.4% in the last year; the 5-year fall reflects the 2024 peak of 22.4%, not a broken model [Certain]. The rolling operating-margin dip is largely restructuring charges the 10-Q names, a temporary cost, backed by a cost programme of at least $1.5 billion run-rate savings [company-reported] [Likely]. Buybacks cut the share count 8.79% in a year [Certain]. The fall on the leadership news is small and touches no reported fundamental; a former Goldman risk chief joining the board partly addresses the controls gap [Likely]. Base fair value 67.80 sits above the price [Certain].

## Decision
```json
{
 "ticker": "PYPL",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {
  "decline_cause": "none",
  "decline_evidence": "Python finds no ROIC, operating-margin or FCF-margin decline over 1 or 3 years; the rolling operating-margin dip of 1.0pp sits in the flat band and the Q3 10-Q ties it to restructuring charges (https://www.sec.gov/Archives/edgar/data/1633917/000163391726000088/pypl-20260930.htm), while rolling FCF margin rose from 16.9% to 18.4% [CF-T].",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Continued PayPal-branded checkout share loss erodes the high-margin core faster than Braintree, Venmo and buybacks offset, with execution risk raised by the CFO and CRO turnover mid-reorganisation; it would also de-rate a price still 11.8% above its 200-day average.",
  "veto": null
 },
 "new_evidence": {
  "type": "trigger_fired",
  "text": "The entry-price watch set by the 2026-11-19 AVOID was hit intraday on 2026-11-20 as the stock fell on the leadership reshuffle (https://www.prnewswire.com/news-releases/paypal-announces-executive-leadership-appointments-to-advance-three-year-strategy-302946916.html, 2026-11-20); at the lower price the value-blend discount reaches the scorecard's next band, the obstacle that made it an AVOID. The reshuffle changes no reported fundamental."
 },
 "thesis": "A high-return, lowly levered payments franchise with a 13.45% FCF yield and heavy buybacks trades at or below its own 5-year minimum multiples, pricing near-zero growth while branded checkout is contested.",
 "rationale": "Yesterday's AVOID was price-only; the fall to the entry price removed that obstacle and the scorecard now gives 4 on top quality, direction and balance-sheet points and a real discount. The leadership change adds execution risk but breaks no fundamental. Conviction-4 core size, set by Python; cash is at the floor, so it replaces a below-bar holding. [Second opinion: conviction 3; a  BUY needs both evaluations at 4+.]",
 "price_at_decision": 56.37,
 "price_date": "2026-11-19",
 "research_note": "research/PYPL/2026-11-20.md",
 "triggers": [
  {
   "text": "TTM ROIC falls below 18%, giving up the five-year gain and signalling branded-checkout erosion is hitting returns.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 18
   }
  },
  {
   "text": "TTM operating margin falls below 15%, near the FY2022 five-year low of 14.7%, showing the mix shift is structural.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 15
   }
  },
  {
   "text": "TTM FCF margin falls below 14%, under the FY2023 low of 14.2%, showing the cash recovery was transitory.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 14
   }
  },
  {
   "text": "Net debt/EBITDA (ratios page) rises above 1.5x from 0.61x, showing buybacks are being debt-funded."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 85.0,
   "basis": "Branded checkout stabilises and the P/E re-rates toward its 5-year median 20.6x [RA] while buybacks shrink the share count, near the mechanical bull fair value 88.66."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 66.0,
   "basis": "FCF margin holds near the rolling 18.4% [CF-T] and the price drifts toward the mechanical base fair value 67.80, with multiples still well below peers [RA]."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 42.0,
   "basis": "Branded revenue keeps falling per the Q3 10-Q and the leadership turnover slows execution, unwinding the six-month run toward the mechanical bear fair value 38.17 and the 6-month low 40.20 [HI]."
  }
 },
 "replaces": "JKHY",
 "replacement_reason": "Cash sits at the 1.5% floor, so the buy needs funding. JKHY is held below the buy bar at conviction 3 (HOLD on 2026-11-15) and was bought on 2026-10-09; PYPL scores 4 on the same scorecard with a deeper own-history discount, so it is the better use of the capital.",
 "second_opinion": {
  "file": "research/PYPL/2026-11-20-evaluation-2.md",
  "conviction": 3
 },
 "entry_price": null,
 "entry_basis": "Second opinion at conviction 3: no entry price set."
}
```

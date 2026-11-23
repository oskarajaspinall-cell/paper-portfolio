# Evaluation: Yifeng Pharmacy Chain (SHA:603939) — 2026-11-23
## Bear case
The discount may be correct. Gross margin has slipped from 40.1% to 38.5% [Certain], consistent with drug-pricing and reimbursement pressure across Chinese pharmacy retail; regulation, not store execution, sets the ceiling [Likely]. FCF margin sits 3.9pp below its 2-year high of 17.9% and the 3-year change is falling; conversion near 197% of net income likely leans on working capital and lease accounting that will not repeat [Guessing]. Peers trade far cheaper on P/FCF (3.6x), EV/Sales and P/B [Certain], so on a sector basis the stock is not cheap; the own-history discount may simply reflect a permanent sector de-rating [Likely]. The price is 13.5% above its 200-day average after a +25.6% six-month run [Certain]; if growth slows, the trend points evaporate and the multiple can fall further. Q3 2026 filing contents were not reviewed [Certain], so a guidance cut is unseen.
## Bull case
Returns are rising, not peaking: ROIC is 24.9% TTM, up from 21.2% a year earlier and 14.0% in FY2021, and operating margin is at its 2-year high of 10.4% [Certain]. The balance sheet is net cash (net debt/EBITDA -1.89x) with shares down 1.25% year on year [Certain]. P/E of 17.8x sits at 7% of its 5-year range and EV/EBITDA of 6.2x is below its 5-year minimum of 8.9x, with an 11.28% FCF yield [Certain]. The reverse DCF implies -7.4% year-1 revenue growth, which a business growing profit does not show [Likely]. The stock is in a healthy uptrend with +32.5pp relative strength over six months and a beta of 0.17 [Certain], so it diversifies the book. The FCF dip vs its 2-year high is partly recovered (+2.9pp over the last year) [Certain], pointing to timing rather than a broken model [Likely].
## Decision
```json
{
 "ticker": "SHA:603939",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "temporary",
  "decline_evidence": "Only FCF margin's 3-year change is falling (-3.8pp); over the last year it rose +2.9pp to 14.0% [CF-T,IS-T] while ROIC (24.9% from 21.2%) and operating margin (10.4%, 2-year high) rose [RA-T,IS-T] and net cash grew (-1.89x) [BS], so it reads as working-capital timing, not a broken model.",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Chinese drug-pricing and reimbursement regulation plus online competition compress gross margin (already 40.1% to 38.5%) and de-rate the sector further; an extended price after a +25.6% six-month run would de-rate if growth slows.",
  "veto": null
 },
 "thesis": "A net-cash Chinese pharmacy chain with rising ROIC trades low in its own P/E range and below its 5-year minimum EV/EBITDA while in a healthy uptrend, though peers are cheaper on cash multiples and regulation caps margins.",
 "rationale": "Scorecard gives 4: high and rising ROIC, net cash, a deep own-history discount with a healthy uptrend; regulation and cheaper peers keep it at the standard size, which Python sets. Cash is at the floor and China/HK is near its cap, so it replaces a China holding.",
 "price_at_decision": 26.26,
 "price_date": "2026-11-20",
 "research_note": "research/SHA-603939/2026-11-23.md",
 "triggers": [
  {
   "text": "TTM ROIC falls below 15%, giving up most of the rise from 14.0% in FY2021 to 24.9%.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 15
   }
  },
  {
   "text": "TTM operating margin falls below 8.5%, under the five-year low of 8.9%.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 8.5
   }
  },
  {
   "text": "TTM gross margin falls below 36%, showing drug-pricing or reimbursement pressure.",
   "check": {
    "source": "statistics",
    "field": "grossMargin",
    "op": "<",
    "value": 36
   }
  },
  {
   "text": "TTM FCF margin falls below 8%, under the FY2021 level of 8.6%.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 8
   }
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 43.46,
   "basis": "Rising ROIC re-rates EV/EBITDA from 6.2x back toward its 5-year range (min 8.9x) [RA], reaching the mechanical base fair value 43.46 [valuation file]."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 32.0,
   "basis": "Profit keeps growing but peers' far lower P/FCF (3.6x) and EV/Sales [P:SHA:603883,P:SHA:603233,P:SHA:605266] cap the re-rating below the mechanical base fair value; P/E drifts up from 17.8x, still well under its 28.7x median [RA]."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 22.0,
   "basis": "Gross margin keeps sliding from 38.5% [IS] on pricing regulation and P/E falls toward its 5-year low of 15.7x [RA], below the mechanical bear fair value 24.92 and toward the 52-week low 17.68 [HI]."
  }
 },
 "replaces": "HKG:0291",
 "replacement_reason": "Same CNY consumer exposure and net cash, but Yifeng earns roughly double the ROIC with rising returns and a similar own-history discount; selling the brewer frees the China/HK room and cash this buy needs.",
 "second_opinion": {
  "file": "research/SHA-603939/2026-11-23-evaluation-2.md",
  "conviction": 4
 }
}
```

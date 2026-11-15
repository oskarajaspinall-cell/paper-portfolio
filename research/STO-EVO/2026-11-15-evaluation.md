# Evaluation: Evolution AB (STO:EVO) — 2026-11-15
## Bear case
Growth has stalled and the margin is drifting down: operating margin is 57.0% TTM vs 59.1% a year earlier and 62.1% at the 2024 peak, and ROIC is 2.5pp below its 2-year high [Certain]. The causes are regulatory, which tends to be permanent: Q1 revenue fell on European headwinds, Asia is volatile on cybercrime, and a post-quarter Brazil ban clouds Q4 [Likely]. Brazil's revenue share is [data unavailable], so the size of that hit is unknown [Certain]. Candle Lake crossed the Swedish mandatory-bid threshold and bid 695 SEK; with insiders at 36.32%, a controlling holder could squeeze free float or minorities [Guessing]. The stock is +33.9% over 12 months and 23.7% above its 200-day average; if Brazil and Europe turn revenue negative, the rebound can de-rate back toward the bottom of the range [Likely]. Piotroski F of 4 is middling [Certain].
## Bull case
This is an exceptional, net-cash cash machine: ROIC 32.1%, FCF margin 59.3%, FCF conversion 116.5% of net income, net debt/EBITDA -0.44x [Certain]. The operating-margin dip looks like depreciation on studio investment rather than pricing erosion: adjusted EBITDA margin held at 65.4%, 65.9% and 65.8% in Q1-Q3 2026 and FY margin guidance is unchanged [Likely]. Yet P/E 14.3x, EV/EBITDA 10.5x and P/FCF 11.3x sit in the bottom tenth of their 5-year ranges, with an 8.87% FCF yield [Certain]. The reverse DCF implies -1.4% revenue growth, while Q3 grew 3.7% with broad regional growth [Likely]. Buybacks cut the share count 4.06% YoY and are accretive at these multiples [Certain]. The base fair value of 1,320.92 SEK sits well above the price, and the trend is working: +18.1% over 3 months, beating SPY [Certain].
## Decision
```json
{
 "ticker": "STO:EVO",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {
  "decline_cause": "temporary",
  "decline_evidence": "Operating margin (57.0% TTM vs 59.1%) and 3-year ROIC/FCF margin are lower, but adjusted EBITDA margin held at 65.4%/65.9%/65.8% in Q1-Q3 2026 with FY margin guidance unchanged (https://stockanalysis.com/quote/sto/EVO/transcripts/552836-q3-2026/), pointing to studio investment and regional regulatory resets rather than lost pricing power; net cash intact (-0.44x).",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Regulatory market losses (the post-quarter Brazil ban, European headwinds, Asia) turn revenue growth negative and keep compressing margins, de-rating a stock that has already rebounded above its 200-day average.",
  "veto": null
 },
 "new_evidence": {
  "type": "new_results",
  "text": "Q3 2026 results (2026-10-23, after the 2026-10-18 AVOID) showed revenue growth of 3.7%, a stable 65.8% adjusted EBITDA margin and unchanged FY margin guidance (https://stockanalysis.com/quote/sto/EVO/transcripts/552836-q3-2026/); the earlier verdict also predates the scorecard."
 },
 "thesis": "A net-cash live-casino supplier with ROIC 32.1% and a 59.3% FCF margin trades in the bottom tenth of its own 5-year multiple ranges, pricing a revenue decline that stable Q3 margins and buybacks do not show.",
 "rationale": "Quality and cash returns are exceptional and the balance sheet is net cash; the margin dip is explained by investment and regional resets with EBITDA margin stable. Multiples near 5-year lows and a rising trend support a core position at conviction size; Brazil and the Candle Lake stake are the risks to watch. [Second opinion: conviction 3; a  BUY needs both evaluations at 4+.]",
 "price_at_decision": 871.0,
 "price_date": "2026-11-13",
 "research_note": "research/STO-EVO/2026-11-15.md",
 "triggers": [
  {
   "text": "TTM operating margin falls below 52% (57.0% now), showing regulatory losses are compressing profitability structurally.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 52
   }
  },
  {
   "text": "TTM ROIC falls below 25% (32.1% now), giving up most of the rise from the FY2021 level of 22.7%.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 25
   }
  },
  {
   "text": "TTM FCF margin falls below 50% (59.3% now), signalling cash generation is eroding.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 50
   }
  },
  {
   "text": "Revenue declines year on year for two consecutive reported quarters (e.g. after the Brazil ban), or Candle Lake gains control and moves to delist or restrict minority returns."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 1453.08,
   "basis": "EV/EBITDA re-rates toward its 5y median 18.6x [RA] as growth stays positive, matching the EV/EBITDA bull fair value of 1,453.08 SEK (below the blended bull of 1,814.22)."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 1150.0,
   "basis": "Margins hold with EBITDA margin stable (Q3 call transcript) and buybacks continue, so multiples recover part of the way to the base fair value of 1,320.92 SEK [valuation file]; held below it for the unquantified Brazil ban."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 647.18,
   "basis": "Brazil and Europe turn revenue negative and EV/EBITDA stays near its 5y min 8.7x [RA], in line with the EV/EBITDA bear value of 647.18 SEK."
  }
 },
 "second_opinion": {
  "file": "research/STO-EVO/2026-11-15-evaluation-2.md",
  "conviction": 3
 },
 "entry_price": null,
 "entry_basis": "Second opinion at conviction 3: no entry price set."
}
```

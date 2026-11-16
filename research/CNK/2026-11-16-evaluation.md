# Evaluation: Cinemark Holdings, Inc. (CNK) — 2026-11-16
## Bear case
TTM results are flattered by a blockbuster-heavy slate: U.S. film rentals rose to 60.1% of admissions from 58.4% [company-reported] (https://www.sec.gov/Archives/edgar/data/1385280/000119312526444406/cnk-20260930.htm), so margins swing with the slate, not management [Likely]. The moat is modest: earnings depend on studios keeping an exclusive theatrical window, and the CEO is already fighting a streaming-first release (https://deadline.com/2026/11/cinemarko-netflix-cliff-booth-theatrical-release-1237212191/) [Likely]. The balance sheet is still stretched: net debt/EBITDA 3.21x and Altman Z 1.71 [Certain]. The trend points come from an extended price: 27.0% above the 200-day average, +55.2% over six months, at the 52-week high [Certain]; a softer 2027 slate would de-rate a 16.7x P/E that already sits at 72% of its 5y range [Likely]. The bear fair value is 14.87 [Certain]. Latin American currencies weakened against the dollar (macro overlay), a translation drag [Likely].

## Bull case
Every rolling-12-month measure is rising or flat: ROIC 12.9%, operating margin 15.1% (a 2-year high), FCF margin 9.6% [Certain]. Q3 U.S. attendance rose 12.7% and ticket price 6.3% [company-reported] (https://www.sec.gov/Archives/edgar/data/1385280/000119312526444406/cnk-20260930.htm), with premium formats and concessions as durable levers [Likely]. Cash conversion is strong (FCF 117.5% of net income, 7.28% FCF yield) and funds deleveraging from 4.87x to 3.21x plus an 18.66% cut in shares outstanding [Certain]. EV/EBITDA of 9.5x is 23% below peers and P/FCF 13.7x below its 5y median 15.2x [Certain]. The reverse DCF implies only 1.3% revenue growth, against a base fair value of 58.26 [Certain].

## Decision
```json
{
  "ticker": "CNK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "No ROIC, operating-margin or FCF-margin decline: the rolling table shows ROIC +1.5pp, operating margin +3.5pp and FCF margin +0.7pp over the last year [RA-T, IS-T, CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Peak-slate earnings: a weaker film slate or a shorter theatrical window would cut margins at a 3.21x-levered company and de-rate a price trading well above its 200-day average.",
    "veto": null
  },
  "thesis": "A deleveraging, buyback-shrinking cinema operator with record results and a 7.28% FCF yield, whose returns depend on the film slate and theatrical window and whose price has already run hard.",
  "rationale": "Scorecard conviction 3: rising returns and trend strength are offset by net debt/EBITDA of 3.21x, mid-level ROIC and slate-dependent, modest-moat earnings. Good but not compelling, so AVOID; cash is an acceptable outcome.",
  "price_at_decision": 40.80,
  "price_date": "2026-11-13",
  "research_note": "research/CNK/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 9% (12.9% now), giving up the post-pandemic recovery.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "TTM operating margin falls below 11% (15.1% now), back to the FY2025 level, showing the margin gain was slate-driven.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11}},
    {"text": "Net debt/EBITDA rises back above 4.5x (3.21x TTM now), reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.5}},
    {"text": "Management or a major studio reports the exclusive theatrical window shortened or abandoned for tentpole films, or TTM FCF margin falls below 6% on the cash-flow page."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 58.26, "basis": "Rising returns and deleveraging hold and the stock reaches the mechanical base fair value 58.26 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 45.0, "basis": "Slate normalises from a record Q3 (film rentals 60.1% of admissions [company-reported], SEC 10-Q) and P/FCF drifts toward its 5y median 15.2x [RA] on flat FCF, below the DCF base because TTM margins are peak-slate."},
    "bear": {"probability": 0.25, "target_price_12m": 28.45, "basis": "A weaker slate or window erosion takes EV/EBITDA to the bear case of the EV/EBITDA method, 28.45 [IS,BS,CF,RA,ST]; the DCF bear 8.07 is not used as it assumes a collapse with no deleveraging."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: even full valuation points would not lift the score to 4 while leverage sits at 3.21x and ROIC at 12.9%; a lower price would not change the decision, only further deleveraging or higher returns would.",
  "replaces": null,
  "replacement_reason": null
}
```

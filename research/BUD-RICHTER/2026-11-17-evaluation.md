# Evaluation: Gedeon Richter (BUD:RICHTER) — 2026-11-17
## Bear case
The price is up 40.9% over 12 months and sits 11.0% above its 200-day average, with P/E at the 64th percentile and P/B at the 96th percentile of their 5y ranges [Certain]; if growth slows, that extended price risks a de-rating [Likely]. FCF margin is falling on a rolling basis (29.3% to 26.8%) even as operating margin rises, so cash is lagging reported profit [Certain]. Gross margin of 67.8% is high for a generics-exposed group and may be a mix peak [Guessing]. The Q3 2026 results of 10 November were not read, so the latest quarter is unverified [Certain]. Regional mix is [data unavailable]; CIS/EU and HUF exposure cannot be checked, and Q1 2026 commentary cited currency headwinds that cut reported EBIT growth [Likely]. The mechanical bear fair value of 7,281.63 HUF shows how sensitive the DCF is [Certain].
## Bull case
Returns and margins are at their best: TTM ROIC 22.5% (2-year high), operating margin 34.5% against 21.5% in FY2021, net cash at -0.61x net debt/EBITDA, Altman Z 6.64 [Certain]. FCF conversion is 103.6% and the FCF yield 10.11% [Certain]. Yet EV/EBITDA is 5.8x, at the 25th percentile of its own range and below peers, and P/FCF 9.9x is near its 5y low [Certain]. The reverse DCF implies -5.1% year-1 revenue growth while management guided high single-digit growth for 2026 (Q4 2025 transcript) [Likely]. The uptrend is healthy rather than overextended: 50-day above 200-day, RSI 65.5, beta 0.31 [Certain]. The FCF dip looks like timing after an exceptional prior year, still far above the 14.9% of FY2021 [Likely].
## Decision
```json
{
 "ticker": "BUD:RICHTER",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "temporary",
  "decline_evidence": "Only TTM FCF margin is falling (29.3% to 26.8%, CF-T,IS-T) while operating margin and ROIC rose to 2-year highs (IS-T, RA-T) and FCF conversion is 103.6%; management flagged continued R&D investment (Q4 2025 transcript, https://stockanalysis.com/quote/bud/RICHTER/transcripts/411350-q4-2025/), consistent with timing/investment rather than a broken model.",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "A gross-margin mix peak or generics pricing pressure, combined with a price up 40.9% in 12 months that would de-rate if growth slows; Q3 2026 results unread.",
  "veto": null
 },
 "thesis": "A net-cash pharma with rising returns and margins trades low in its own EV/EBITDA and P/FCF ranges while in a healthy uptrend.",
 "rationale": "Scorecard gives conviction 4: high, rising returns, net cash, and trend strength with a real FCF yield. Python sets the volatility-scaled size; cash after the pending order cannot fund it above the 1.5% floor, so the conviction-3 OTIS holding is sold to fund it.",
 "price_at_decision": 13700.0,
 "price_date": "2026-11-16",
 "research_note": "research/BUD-RICHTER/2026-11-17.md",
 "triggers": [
  {
   "text": "TTM operating margin falls below 28%, reversing most of the rise from 28.7% a year earlier to 34.5%.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 28
   }
  },
  {
   "text": "TTM ROIC falls below 16%, back to the FY2021 level and erasing the returns improvement.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 16
   }
  },
  {
   "text": "TTM FCF margin falls below 18%, showing the rolling slide from 29.3% is structural, not timing.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 18
   }
  },
  {
   "text": "Net debt/EBITDA (ratios page) rises above 1.0x from -0.61x, signalling a debt-funded deal."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 18245.16,
   "basis": "The base mechanical fair value (DCF 67% / EV/EBITDA 33%) is reached as margins hold at 34.5% and the reverse-DCF decline of -5.1% proves too pessimistic [IS-T, fact sheet Fair value]."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 14574.46,
   "basis": "EV/EBITDA method base on TTM EBITDA, near its 5y median of 6.4x, as margins plateau and the uptrend's gains are mostly in the price [RA, fact sheet Fair value]."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 11141.92,
   "basis": "EV/EBITDA bear as a gross-margin mix peak and HUF headwinds de-rate the stock toward its 5y low multiple; the DCF bear of 5,351.49 is excluded as it implies a collapse no fact-sheet trend shows [RA, fact sheet Fair value]."
  }
 },
 "replaces": "OTIS",
 "replacement_reason": "OTIS is held at conviction 3 with its price above the mechanical fair value and a balanced skew (its own thesis); Richter clears the buy bar with higher returns, net cash and a lower EV/EBITDA, and cash cannot fund a full position above the 1.5% floor.",
 "new_evidence": {
  "type": "method_change",
  "text": "The 2026-11-15 AVOID 3 predates the 2026-11-17 scorecard change (strength_at_value_points) and the 2026-11-16 overvaluation guards; the same evidence re-scored under the current rules reaches 4."
 },
 "second_opinion": {
  "file": "research/BUD-RICHTER/2026-11-17-evaluation-2.md",
  "conviction": 4
 }
}
```

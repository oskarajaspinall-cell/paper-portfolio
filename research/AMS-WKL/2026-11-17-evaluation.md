# Evaluation: Wolters Kluwer N.V. (AMS:WKL) — 2026-11-17
## Bear case
The low multiple is the market pricing AI substitution of content and seat-based software: P/E 15.0x and EV/EBITDA 11.9x sit below their own 5-year minimums, and the reverse DCF implies only 2.2% year-1 growth [Certain]; if generative AI commoditises UpToDate or CCH content, the 5-year history is the wrong anchor [Guessing]. The price has already run: +32.6% over 3 months and 33.7% above its 200-day average, so a de-rating could resume if organic growth slows from the 6% reported for nine months [Likely]. Leverage has crept up to 2.08x from 1.50x as buybacks and bolt-ons outrun cash, and FCF conversion fell to 104.2% from 144.5% [Certain]. The latest dip to the entry price has no identified stock-specific cause, which means it is not a fresh discount either [Likely]. Regional mix and US exposure are unverified [Certain].

## Bull case
A wide-margin, high-return franchise: ROIC 24.8% TTM (from 18.6% in FY2021), gross margin 74.1%, operating margin 25.5%, all at or near 2-year highs on the rolling view, with no direction break [Certain]. It trades below its own 5-year minimum on P/E, EV/EBITDA and P/FCF and at a 34-49% discount to peers REL, TRI and VRSK, with a 7.01% FCF yield [Certain]. Shares fell 3.36% year on year, compounding per-share value [Certain]. Nine-month organic growth of 6% (trading update headline) contradicts the 2.2% growth the price implies [Likely]. Embedded regulated workflows carry high switching costs, and the company is shipping agentic tax, MCP-server and clinical decision tools (AgileMD) rather than being displaced [Likely]. The mechanical base fair value is 115.98 EUR [Certain]. Macro is context only (overlay 2026-11-17).

## Decision
```json
{
  "ticker": "AMS:WKL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Rolling-12-month ROIC +1.6pp, operating margin +0.2pp and FCF margin -0.1pp (flat) [RA-T, IS-T, CF-T]; no metric in the scorecard set is falling.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Generative AI erodes paid professional content and seat-based software, showing up as slowing organic growth and a renewed de-rating from an already extended price.",
    "veto": null
  },
  "thesis": "A high-return professional-information franchise trading below its own 5-year minimum multiples, where the price implies growth well under its reported organic growth, with AI substitution the open question.",
  "rationale": "Quality and direction are full marks, but the scorecard totals 8: medium AI-substitution risk, 2.08x leverage and a value-blend upside short of the top band leave conviction 3. The entry-price hit came with no stock-specific news, so it is a small pullback after a sharp rally, not a new discount. Good but not compelling: AVOID.",
  "price_at_decision": 90.84,
  "price_date": "2026-11-16",
  "research_note": "research/AMS-WKL/2026-11-17.md",
  "triggers": [
    {"text": "TTM ROIC falls below 18%, giving up the five-year improvement from 18.6% (FY2021) to 24.8%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "TTM operating margin falls below 23%, reversing the five-year expansion to 25.5%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 23}},
    {"text": "Net debt/EBITDA rises above 3.0x (2.08x TTM now), showing buybacks and M&A outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}},
    {"text": "Organic growth in a trading update or results release turns negative, i.e. AI substitution showing up in revenue."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 127.82, "basis": "Organic growth holds and multiples recover toward their own history, matching the mechanical bull fair value 127.82 [IS,RA,ST]."},
    "base": {"probability": 0.5, "target_price_12m": 115.98, "basis": "Steady growth above the 2.2% the reverse DCF implies, valued at the mechanical base fair value 115.98 (DCF 98.71 / EV/EBITDA 150.53 blend) [IS,RA,ST]."},
    "bear": {"probability": 0.25, "target_price_12m": 79.19, "basis": "AI substitution fears deepen and the extended rally (33.7% above the 200-day average [ST,HI]) de-rates to the mechanical bear fair value 79.19."}
  },
  "entry_price": 86.8,
  "entry_basis": "The default (valuation file: base 115.98 x 0.85) sits above the price, so it cannot serve. My judgement: the level at which the scorecard's value-blend upside reaches its top band (30%), lifting the total to the conviction-4 threshold on the same evidence.",
  "replaces": null,
  "replacement_reason": null
}
```

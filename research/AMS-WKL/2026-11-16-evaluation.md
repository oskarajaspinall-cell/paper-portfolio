# Evaluation: Wolters Kluwer N.V. (AMS:WKL) — 2026-11-16
## Bear case
The market is pricing generative AI as a threat to paid professional content and per-seat workflow software, and the 12-month change of -2.9% despite rising returns says that fear has not gone away [Likely]. If AI assistants commoditise tax, legal and clinical answers, today's multiples are not a discount but a new, lower normal, and the reverse DCF's 2.1% implied growth could prove right [Guessing]. The stock has already run hard: 3-month +33.0%, 17.7% above its 50-day and 34.1% above its 200-day average, RSI 65.6. Much of the discount has closed, and an extended price risks a fast de-rating if organic growth slows [Likely]. Leverage has crept from 1.50x to 2.08x net debt/EBITDA to fund buybacks and M&A, and FCF conversion has fallen from 144.5% to 104.2% [Certain]. The nine-month trading update could not be read, so growth and guidance are unverified [Certain].

## Bull case
This is a high-return franchise that keeps improving: TTM ROIC 24.8% (from 18.6% in FY2021), ROCE 27.6%, gross margin 74.1% and operating margin 25.5% at 5-year highs, and the rolling-12-month view confirms it, with ROIC up 1.6pp and margins flat, not falling [Certain]. Yet P/E of 15.5x sits at the bottom of its 5-year range (median 30.7x) and EV/EBITDA of 12.1x below its 5-year minimum, far below peers RELX, Thomson Reuters, S&P Global and Verisk [Certain]. The 6.87% FCF yield funds buybacks that cut the share count by 3.36% a year [Certain]. Embedded regulatory and clinical content plus workflow lock-in make the product hard to replace [Likely], and the company is shipping AI itself (agentic tax, an MCP server, the AgileMD acquisition) [Likely]. Mechanical base fair value of 116.24 EUR is well above the price [Certain].

## Decision
```json
{
  "ticker": "AMS:WKL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Nothing is falling: TTM ROIC 24.8% vs 23.2% a year earlier, operating margin 25.5% vs 25.4%, FCF margin flat at 22.8% [RA-T, IS-T, CF-T].", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Generative AI commoditises professional content and workflow seats, slowing organic growth and turning today's low multiples into a permanent de-rating; after a 33.0% 3-month run, a growth wobble would hit an extended price.", "veto": null},
  "thesis": "A high-return professional-information franchise with rising ROIC and stable margins trades at the bottom of its own 5-year multiple range and far below peers, but after a sharp run the remaining discount only partly compensates for an unresolved AI-disruption risk.",
  "rationale": "Quality and direction are top marks, but the balance sheet scores only partly, the moat is narrow and the AI risk real; after the run the discount to fair value no longer reaches the top band. Scorecard conviction 3 is below the buy bar (owner rule: high conviction only), so AVOID and wait for the entry price.",
  "price_at_decision": 90.84,
  "price_date": "2026-11-13",
  "research_note": "research/AMS-WKL/2026-11-16.md",
  "entry_price": 83.26,
  "entry_basis": "The 2026-10-29 swing low of 83.26 [HI]: at that level the same fair value would put the discount in the scorecard's top band, lifting this evidence to conviction 4. The default base 116.24 x 0.8 sits above today's price, so it cannot serve.",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, giving up most of the rise from 18.6% (FY2021) to 24.8% and signalling AI or competitive erosion of returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 23%, under the FY2022 level of 23.5%, showing pricing pressure on content and software.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 23}},
    {"text": "TTM FCF margin falls below 19%, under the five-year low of 21.9%, showing cash generation is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 19}},
    {"text": "Net debt/EBITDA rises above 3.0x (2.08x TTM now), showing buybacks and M&A are outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 128.12, "basis": "Results keep confirming the moat against AI and multiples recover toward their 5y medians (P/E 30.7x, EV/EBITDA 19.7x [RA]), consistent with the mechanical bull fair value of 128.12 [valuation file]."},
    "base": {"probability": 0.5, "target_price_12m": 116.24, "basis": "Stable margins and ROIC 24.8% [RA] with continued buybacks close part of the gap to peers, in line with the mechanical base fair value of 116.24 (DCF 99.10, EV/EBITDA 150.53) [valuation file]."},
    "bear": {"probability": 0.25, "target_price_12m": 79.39, "basis": "AI-disruption fear returns and the recent run reverses, leaving multiples at their 5y floor, consistent with the mechanical bear fair value of 79.39 [valuation file] and the Bear case."}
  },
  "new_evidence": {"type": "price_move", "text": "The price rose from 81.52 at the 2026-10-18 BUY 4 evaluation to 90.84, shrinking the discount; that verdict also predates the 2026-11-09 scorecard."},
  "replaces": null,
  "replacement_reason": null
}
```

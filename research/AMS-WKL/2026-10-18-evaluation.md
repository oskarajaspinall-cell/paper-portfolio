# Evaluation: Wolters Kluwer N.V. (AMS:WKL) — 2026-10-18
## Bear case
The stock fell 25.7% over 12 months despite a beta of 0.18 and no explanatory headline [Certain]; the most plausible driver is a market view that generative AI commoditises professional legal, tax and clinical content, which would hit pricing power before it shows in reported margins [Guessing]. The reverse DCF already prices roughly flat revenue (-0.4%) [Certain], yet the fact sheet carries no revenue-growth series to prove growth is holding up, so we cannot rule out a slowdown [Certain]. Leverage has crept from 1.50x to 2.08x net debt/EBITDA to fund buybacks and the capital reduction [Certain], and FCF conversion has fallen from 144.5% to 104.2% [Certain]. After a +30.0% three-month rebound and an RSI of 77.3 [Certain], near-term entry is stretched, and the mechanical bear fair value (EUR80.48) offers no cushion below the price [Certain].

## Bull case
This is a top-tier compounder at a bottom-of-range price: ROIC 24.8% and ROCE 27.6% are rising, and gross, operating and net margins are all at five-year highs [Certain]. Every earnings multiple sits below its own five-year minimum (P/E 13.9x vs a 15.3x low; P/FCF 13.1x vs 14.6x) and a third or more below RELX, Thomson Reuters, S&P Global and Experian [Certain]. A 7.66% FCF yield plus a 3.36% annual share-count reduction gives a strong cash return while the market waits [Certain]. The steady stream of AI launches embedded in installed products (Libra drafting, agentic TaxWise, hCue Expert AI) suggests AI is being monetised as a feature of the moat, not a substitute for it [Likely]. Base fair value EUR117.66 is well above the price and the bear case roughly equals it, an asymmetric skew [Certain]. Macro is context-only given low beta [Likely].

## Decision
```json
{
  "ticker": "AMS:WKL",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A professional-information franchise with rising ROIC (24.8%) and five-year-high margins trades below its own 5-year minimum on every earnings multiple and well below peers at a 7.66% FCF yield, pricing AI-disruption fears that its reported fundamentals do not yet show.",
  "rationale": "Quality is rising, cash returns are strong and the mechanical bear value sits at the price, so the skew is favourable. The unexplained drawdown (likely AI-disruption fear), rising leverage, missing revenue-growth data and a stretched three-month rebound hold conviction at 4, not 5: standard volatility-scaled core size. Industrials stays well under the sector cap.",
  "price_at_decision": 81.52,
  "price_date": "2026-10-16",
  "research_note": "research/AMS-WKL/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, giving up most of the five-year rise from 18.6% to 24.8% and signalling moat erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 18%, under the 22-24% range it has held for five years, showing cash generation is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 18}},
    {"text": "TTM gross margin falls below 70%, under the five-year low of 71.1%, signalling AI-driven price pressure on content and software.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 70}},
    {"text": "Net debt/EBITDA rises above 3.0x (2.08x TTM now), showing capital returns are becoming balance-sheet risk.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 129.73, "basis": "AI launches prove additive and the multiple re-rates towards its own history, reaching the mechanical bull fair value of EUR129.73 [fact sheet Fair value; RA]."},
    "base": {"probability": 0.5, "target_price_12m": 101.22, "basis": "Margins and ROIC hold at five-year highs [IS, RA] and the price converges on the DCF base of EUR101.22, below the blended base because the EV/EBITDA leg assumes a full return to the 19.7x five-year median that AI-disruption fear makes unlikely within 12 months [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 64.86, "basis": "AI-substitution fear deepens or revenue growth turns negative, and the rebound unwinds back to the September swing low of 64.86 [HI], below the mechanical bear fair value of EUR80.48 because that model does not capture a narrative de-rating."}
  },
  "entry_price": null,
  "entry_basis": null,
  "replaces": null,
  "replacement_reason": null
}
```

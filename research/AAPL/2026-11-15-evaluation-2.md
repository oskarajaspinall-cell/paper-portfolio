# Evaluation: Apple Inc. (AAPL) — 2026-11-15
## Bear case
The price is the problem. P/E of 39.7x and EV/EBITDA of 29.9x sit above their 5y maxima, and the reverse DCF implies 33.0% year-1 revenue growth, far beyond the record [Certain]. The points come from trend strength, so an extended price risks a de-rating if growth slows: the macro overlay notes the 10y real yield up 0.47pp in 3m, and a P/E return to its 5y median of 33.8x would cost about 15% with unchanged earnings [Likely]. Part of the bid is a safe-haven rotation out of AI that can reverse [Guessing]. The new 10-K warns memory and chip costs will intensify and price rises may not offset them, plus tariff risk [Likely]. ROIC is 10.4pp below its 2-year high and ROCE slipped (68.7% to 67.4%) on a larger capital base, not erosion, but returns are no longer accelerating [Likely]. Greater China is about 17% of sales [company-reported].

## Bull case
A wide-moat ecosystem that is still improving: TTM ROIC 93.9%, operating margin 33.0% and FCF margin 28.4%, each higher than a year earlier, and gross margin up from 43.3% to 48.8% over five years as Services (76.2% gross margin [company-reported]) grows in the mix [Certain]. The balance sheet is effectively unlevered on either net-debt definition, Altman Z is 11.08, and the share count fell 1.90% in a year [Certain]. The stock is working: +18.3% over its 200-day average, not overextended, +30.3% in 12 months and +19.9pp ahead of SPY, with a 2.63% FCF yield [Certain]. Results drove the 2026-11-04 move (+5.3% on 2.2x volume, more than fully held) [Certain]. The mechanical fair value is flagged unreliable (methods 2.5x apart), so it understates a business whose returns have structurally risen [Likely].

## Decision
```json
{
  "ticker": "AAPL",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {"decline_cause": "none", "decline_evidence": "ROIC, operating margin and FCF margin are all higher than a year earlier and over 3 years [RA-T, IS-T, CF-T]; ROIC is below its 2-year high and ROCE slipped on a larger capital base, not lost share or pricing.", "moat": "wide", "key_risk": "medium", "key_risk_text": "De-rating: P/E and EV/EBITDA above their 5y maxima with real yields rising (macro overlay); a slower year compresses the multiple toward its 5y median with no business damage.", "veto": null},
  "thesis": "Apple is an exceptional, unlevered, improving franchise in a strong uptrend, a good business that is working, bought on trend strength rather than a discount.",
  "rationale": "The scorecard reaches 4 on quality, direction, balance sheet, moat and trend strength, not on value: multiples sit above their 5y range, so the de-rating risk in the bear case is real and the scenario skew is roughly flat. Standard core size, volatility-scaled by Python; no cap clearly breached, so nothing is replaced.",
  "price_at_decision": 356.27,
  "price_date": "2026-11-13",
  "research_note": "research/AAPL/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 30%, reversing the five-year expansion from 30.3%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 75%, back to FY2023 levels, showing the returns step-up has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 75}},
    {"text": "TTM FCF margin falls below 23%, under the FY2025 low of 23.7%, showing memory and chip cost inflation is eating cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 23}},
    {"text": "Greater China net sales fall year on year in a 10-Q while iPhone net sales also fall."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 390, "basis": "P/E holds near 39.7x [RA] while operating and FCF margins keep rising [IS-T, CF-T] and buybacks shrink the share count [ST]; real yields ease (macro overlay)."},
    "base": {"probability": 0.45, "target_price_12m": 355, "basis": "P/E eases toward its 5y max of 37.7x [RA] and earnings growth offsets it; the mechanical base of 180.00 is ignored as unreliable (methods 2.5x apart) [fact sheet]."},
    "bear": {"probability": 0.30, "target_price_12m": 300, "basis": "Macro overlay tilt toward bear (small) raises this weight: real yield rises or money rotates back to AI and P/E compresses to its 5y median 33.8x [RA] with unchanged earnings."}
  },
  "new_evidence": null,
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: ConocoPhillips (COP) — 2026-11-16
## Bear case
The last year's recovery (ROIC 11.3% to 14.6%, FCF margin 11.6% to 16.1%) is price-led: the filing ties it to Middle East supply disruption, not structural change [Certain]. Over five fiscal years ROIC, operating and FCF margin all fell, and the 3-year change is still negative [Certain]. The stock is up +59.7% in 12 months and P/E 15.0x, EV/EBITDA 6.1x and EV/Sales 2.6x all sit above their 5y maxima; the price is above even the mechanical bull fair value of 130.02 [Certain]. That extension is the risk: if the disruption eases and crude falls, earnings and the multiple de-rate together [Likely]. The macro overlay tilts toward bear (moderate): real yields up 0.47pp in ~3m add multiple pressure [Likely]. The pending Kirkuk, Iraq stake adds geopolitical tail risk [Guessing]. The moat is cost and scale, not pricing power [Likely].

## Bull case
The balance sheet is strong: net debt/EBITDA 0.45x, Altman Z 3.28 [Certain]. The FY2022-FY2025 decline was a commodity-cycle normalisation with leverage intact, not lost share, and the rolling-12-month table shows every return metric rising again [Certain]. Q3 beat, the dividend rose 11% and buybacks shrank the share count 2.43% YoY [Certain]. FCF conversion is 96.2% TTM and FCF yield 6.61% [Certain]. The trend is healthy, not extreme: 15.4% above the 200-day average with relative strength vs SPY of +49.4pp over 12 months [Certain]. Management targets over $1bn of run-rate cost gains by year-end 2026 [company-reported], cushioning margins if prices soften [Likely]. EV/EBITDA is below the peer median [Certain].

## Decision
```json
{
  "ticker": "COP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The FY2022-FY2025 fall in ROIC and margins tracked the commodity cycle with net debt/EBITDA flat around 0.45x-0.79x [BS,IS]; rolling-12-month ROIC, operating and FCF margin are all rising again [RA-T, IS-T, CF-T], though the note says the rebound is price-led (SEC 10-Q).",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Realised crude falls as the Middle East disruption eases, reversing the price-led ROIC/FCF recovery while the multiple de-rates from above its 5y range.",
    "veto": null
  },
  "thesis": "A strong-balance-sheet, low-cost E&P in a healthy uptrend whose recovered returns depend on elevated crude, priced above its own 5-year multiple range and mechanical fair value.",
  "rationale": "Quality, balance sheet and trend strength are real, but the return recovery is price-led and the stock trades above every own-history multiple and the bull fair value, with the macro overlay tilting toward bear. The scorecard does not reach the buy bar, so no position; cash is acceptable.",
  "price_at_decision": 142.28,
  "price_date": "2026-11-13",
  "research_note": "research/COP/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, back to the FY2025 trough, showing the recovery has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 11%, under the year-earlier 11.6%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 11}},
    {"text": "TTM operating margin falls below 21%, back to the FY2025 level of 20.9%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 21}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.45x TTM), showing distributions or the Iraq deal outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 154.28, "basis": "Supply disruption persists and FCF margin holds near 16.1% [CF-T]; the price revisits its 52-week high of 154.28 [HI] with the multiple held above its 5y range."},
    "base": {"probability": 0.45, "target_price_12m": 130.02, "basis": "EV/EBITDA drifts back toward the top of its 5y range (6.0x max [RA]), matching the mechanical bull fair value of 130.02 [valuation]; cost gains offset some price normalisation."},
    "bear": {"probability": 0.35, "target_price_12m": 96.85, "basis": "Disruption eases, ROIC returns toward 10% and the multiple compresses to the mechanical bear fair value of 96.85 [valuation]; probability raised for the macro overlay's moderate tilt toward bear (research/COP/2026-11-16-macro.md)."}
  },
  "entry_price": 99.11,
  "entry_basis": "valuation file: base 123.89 x 0.8; at that level the discount would supply the valuation points the extended price now lacks.",
  "replaces": null,
  "replacement_reason": null
}
```

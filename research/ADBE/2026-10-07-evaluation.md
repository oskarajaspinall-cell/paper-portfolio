# Evaluation: Adobe Inc. (ADBE) — 2026-10-07

## Bear case
Generative-AI-first and free creative tools attack Creative and Document Cloud pricing, a risk Adobe's own 10-K names [Certain]. The early signs are already there: operating margin has stayed flat near 36% for five years while returns on capital rose, and FCF margin slipped from 43.6% to 40.8% TTM [Certain]. Rising ROIC and ROE are partly flattered by buybacks: shares are down 6.22% YoY and net debt/EBITDA turned positive at 0.12x [Certain]. A P/E of 13.3x may be a fair price for a former compounder whose terminal value is now in doubt, so it is not necessarily cheap [Guessing]. The stock is down 31.3% over 12 months versus SPY +16.4%, and short interest rose 6.5% month on month, so sentiment is still weakening [Certain]. A value trap is plausible if seat or price erosion begins [Likely].

## Bull case
This is a 89.3%-gross-margin, 57.2%-ROIC subscription franchise with Piotroski 7 and Altman Z 8.01 [Certain]. It trades below its own 5-year minimum on every cash multiple: P/E 13.3x (min 18.8x), EV/EBITDA 9.5x, P/FCF 8.7x, and an 11.45% FCF yield, which is 34-49% below peer medians [Certain]. The fundamentals have not broken. Gross margin is rising, operating margin is stable at 36.3%, and FCF conversion is 145.4% [Certain]. An FCF yield that high, returned through buybacks, compounds per-share value even if growth is flat [Likely]. The multiple compression looks far larger than the fundamental deterioration so far [Likely]. Embedded workflows and file-format lock-in should slow any switching to AI tools [Likely].

## Decision
```json
{
  "ticker": "ADBE",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, cash-generative subscription franchise priced below its own 5-year valuation floor for AI disruption that has not yet shown up in margins or returns.",
  "rationale": "The valuation is exceptional: 11.45% FCF yield and every cash multiple below its 5-year minimum. Quality is intact (89.3% gross margin, 57.2% ROIC). AI competitive risk is real and flagged in the 10-K, and operating and FCF margins are not expanding, so the size is a moderate 5%, not 7-10%. The portfolio is all cash, so no limit binds.",
  "price_at_decision": 238.12,
  "price_date": "2026-10-06",
  "research_note": "research/ADBE/2026-10-07.md",
  "triggers": [
    {"text": "Gross margin falls below 85%, indicating commoditisation of Creative/Document Cloud by AI tools.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 85}},
    {"text": "Operating margin falls below 34%, indicating sustained pricing or margin erosion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 34}},
    {"text": "ROIC falls below 40%, indicating loss of the pricing power underpinning the thesis.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}}
  ],
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Baycurrent, Inc. (TYO:6532) — 2026-11-15
## Bear case
The price has run far ahead of the business: 86.3% above its 200-day average after a 138.5% six-month rise, with P/E 43.4x and EV/EBITDA 29.0x both above their 5y maxima (31.5x, 20.4x) [Certain]. Even the mechanical bull fair value of 9,951.46 JPY sits below the 12,325.00 close, and the reverse DCF needs 35.0% year-1 revenue growth [Certain]. Meanwhile the last 12 months weakened: operating margin 36.6% to 33.3%, FCF margin 26.8% to 22.1%, ROIC 85.1% to 80.6% [Certain]. The cause looks like cost and wage pressure in a talent business rather than lost share, but no primary source confirms it [Guessing]. An extended price with slipping margins is the classic setup for a de-rating if growth slows; returning only to the 5y max multiples would mean a large fall [Likely]. FCF yield is just 2.10% [Certain]. Macro is context only (overlay).

## Bull case
This is an exceptional business: TTM ROIC 80.6%, ROCE 52.7% (up from 44.1% a year ago), gross margin 58.0% and net cash (net debt/EBITDA -0.75x) [Certain]. FCF conversion of 89.0% and modest buybacks (shares -0.87% YoY) show cash returns are real [Certain]. Margins remain far above consulting peers, so the last-year dip is from a high base and may reflect hiring ahead of demand, a temporary investment [Guessing]. Momentum is very strong, beating SPY by +77.6pp over 12 months, and the market may be pricing a durable step-up in Japanese corporate DX spending [Likely]. P/E is only +11% vs the peer median 39.1x [Certain].

## Decision
```json
{
  "ticker": "TYO:6532",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating margin (36.6% -> 33.3%), FCF margin (26.8% -> 22.1%) and ROIC (85.1% -> 80.6%) fell over the last 12 months [IS-T, CF-T, RA-T] while gross margin rose to 58.0% and ROCE rose to 52.7% [IS, RA-T]; the pattern points to cost/investment pressure from a high base, not lost share or a broken model, though no primary source confirms the cause.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "De-rating: the price is 86.3% above its 200-day average with every multiple above its 5y max and the reverse DCF implying 35.0% growth [ST, HI]; a slowdown in growth or further margin slippage would likely compress the multiple sharply.",
    "veto": null
  },
  "thesis": "A superb high-return, net-cash consultancy whose price already discounts far more growth than its slipping margins support.",
  "rationale": "Quality is outstanding, but the price is severely overextended above its 200-day average and above every own-history multiple, with even the mechanical bull fair value below the close while margins fell over the last year. No discount and no healthy-trend credit; the scorecard gives conviction 2, well below the buy bar. Cash is the better choice.",
  "price_at_decision": 12325.00,
  "price_date": "2026-11-13",
  "research_note": "research/TYO-6532/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 30%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 60%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 60}},
    {"text": "TTM FCF margin falls below 18%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 18}},
    {"text": "Shares outstanding grow more than 2% YoY (dilution).", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 14000, "basis": "Growth stays strong enough to justify the reverse-DCF 35.0% implied growth and the multiple holds near the current P/E 43.4x [RA, fact sheet fair value]; above the mechanical bull because the model is blind to the momentum re-rating."},
    "base": {"probability": 0.45, "target_price_12m": 9951.46, "basis": "Margins stabilise near TTM 33.3% [IS-T] and multiples drift back toward their 5y max (P/E 31.5x, EV/EBITDA 20.4x [RA]), consistent with the mechanical bull fair value 9,951.46 [fact sheet]."},
    "bear": {"probability": 0.35, "target_price_12m": 6742.05, "basis": "Margin slippage continues (FCF margin 26.8% -> 22.1% [CF-T]) and the stock de-rates to the mechanical base fair value 6,742.05 [fact sheet], still above its 5y median multiples."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2 is below the entry-price threshold of 3; a re-research would be needed at any lower price.",
  "replaces": null,
  "replacement_reason": null
}
```

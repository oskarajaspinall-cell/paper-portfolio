# Evaluation: Vodacom Group (JSE:VOD) — 2026-11-15
## Bear case
Returns are falling on a bigger capital base: ROIC dropped from 18.4% to 14.7% and ROCE from 20.4% to 15.3% over the last 12 months while net debt/EBITDA rose to 1.74x from 1.16x [Certain]. That is the Safaricom consolidation, and its payback is unproven [Likely]. The cheap P/E of 7.8x rests on an inflated TTM net margin of 24.3% vs 12.3% in FY2026 [Likely]; on EV/EBITDA (6.6x vs a 5y median of 6.4x) and P/FCF (8.8x vs 8.6x) the stock is merely fair, and P/B at 3.2x is the top of its range [Certain]. The price is extended: 17.7% above its 200-day average with RSI 79.1 [Certain], so a growth slowdown would de-rate it [Likely]. The Safaricom deal still faces a Kenyan legal proceeding, and the macro overlay could not verify the EM currency or policy-rate exposure [Likely]. No mechanical fair value is available [Certain].
## Bull case
The H1 2027 results show the business accelerating: pro forma service revenue, EBITDA and operating free cash flow all grew strongly, led by fintech and prepaid data, and management expects H2 acceleration [Likely] (transcript 686215). TTM operating margin rose to 26.0% from 22.6% and FCF margin is 20.8%, a 2-year high [Certain]. FCF yield of 11.30% is a real cash return, and FCF conversion exceeded 100% in each of the last five fiscal years [Certain]. The ROIC dip reflects the Safaricom consolidation enlarging invested capital, not a weaker franchise: margins are rising, not falling [Likely]. Licences, spectrum and network scale give a durable local moat, and Safaricom adds East African fintech scale [Likely]. The stock is working: +30.0% over 12 months and ahead of SPY over 3, 6 and 12 months, with beta 0.30 [Certain].
## Decision
```json
{
  "ticker": "JSE:VOD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "ROIC and ROCE fell over the last 12 months while operating margin rose to 26.0% from 22.6% and FCF margin to 20.8% [IS-T, CF-T]; the fall tracks the Safaricom consolidation enlarging the capital base and debt (net debt/EBITDA 1.74x vs 1.16x [BS,IS]), per the H1 2027 call (https://stockanalysis.com/quote/jse/VOD/transcripts/686215-h1-2027/).", "moat": "narrow", "key_risk": "medium", "key_risk_text": "The Safaricom deal's Kenyan legal proceeding and integration payback, with the price 17.7% above its 200-day average and RSI 79.1 leaving it exposed to a de-rating if growth slows.", "veto": null},
  "thesis": "A cash-generative African telecom whose margins are rising after the Safaricom consolidation, trading at an 11.30% FCF yield in an uptrend.",
  "rationale": "Margins and cash flow are improving and the decline in returns looks deal-driven, but valuation is only fair on EV/EBITDA and P/FCF, the price is extended, the Kenyan proceeding is unresolved and no fair value is computable. Good but not compelling: AVOID.",
  "price_at_decision": 17993.0,
  "price_date": "2026-11-13",
  "research_note": "research/JSE-VOD/2026-11-15.md",
  "triggers": [
    {"text": "ROIC falls below 12% (statistics page).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Operating margin falls below 22% (statistics page).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}},
    {"text": "FCF margin falls below 16% (statistics page).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 16}},
    {"text": "Net debt/EBITDA rises above 2.5x (statistics page).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 21500, "basis": "H2 acceleration guided on the H1 2027 call (transcript 686215) lifts EBITDA while EV/EBITDA holds near today's 6.6x, above its 5y median 6.4x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 18000, "basis": "EBITDA growth offsets EV/EBITDA drifting back to its 5y median 6.4x [RA] and P/FCF to 8.6x [RA]; no mechanical fair value to reconcile with (no ZAR FX rate)."},
    "bear": {"probability": 0.30, "target_price_12m": 13000, "basis": "An adverse Kenyan ruling or growth slowdown de-rates EV/EBITDA towards its 5y minimum 5.2x [RA] and peer median 5.2x on leverage of 1.74x [BS,IS]."}
  },
  "entry_price": 15300,
  "entry_basis": "No fair value is computable (no ZAR FX rate), so the anchor is the 200-day average of 15,283.30 [ST,HI]: there the extension is gone and FCF yield would be well above today's, the obstacle being price, not quality.",
  "new_evidence": {"type": "new_results", "text": "H1 2027 results released 2026-11-10 (https://stockanalysis.com/quote/jse/VOD/filings/3972822/) and a price move from 16267 to 17993 since the 2026-11-08 evaluation."},
  "replaces": null,
  "replacement_reason": null
}
```

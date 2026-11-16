# Evaluation: Konami Group Corporation (TYO:9766) — 2026-11-16
## Bear case
The price already capitalises peak results. TTM ROIC (43.4%), operating margin (33.2%) and FCF margin (23.3%) all sit at their 2-year highs [Certain], yet FY2023 shows how fast a hit-driven publisher can fall (ROIC 17.9%, FCF margin -2.4%) [Certain]. P/E of 30.5x is at 89% of its 5y range and EV/Sales and P/B are above their 5y maxima [Certain]; the reverse DCF needs 18.4% year-one revenue growth [Certain]. The mechanical base fair value of 19,284.86 JPY is far below the 29,180.00 close and even the bull value sits below it [Certain]. The stock is 40.7% above its 200-day average with RSI 70.1 [Certain]: an extended price risks a sharp de-rating if the release slate or eFootball monetisation slows [Likely]. The 5-year FCF-margin decline is FY2023-driven and has reversed in the last 12 months, but cash conversion is lumpy [Likely]. Country mix and capital returns are unverified [Guessing].

## Bull case
Konami is a high-return, net-cash IP owner whose economics are improving, not just recovering: ROIC rose from 30.1% to 43.4% and operating margin from 26.4% to 33.2% in a year [Certain]. Net debt/EBITDA of -1.40x, Altman Z 11.71 and Piotroski 7 give a fortress balance sheet [Certain]. The catalogue (Silent Hill, Castlevania, eFootball) can be re-monetised across platforms, and the new Castlevania was well reviewed [Likely]. FCF conversion of 101.2% TTM shows profits are turning into cash [Certain], and P/FCF of 29.5x is mid-range in its own history [Certain]. The Q2 results drew a +10.9% reaction on 2.3x volume that has fully held [Certain], so the trend is earnings-backed [Likely]. Low beta (0.38) adds diversification [Certain].

## Decision
```json
{
  "ticker": "TYO:9766",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Nothing falls over 1 or 3 years; the 5-year FCF-margin decline is the FY2023 trough (-2.4%) and the rolling 12 months show it rising from 11.7% to 23.3% [CF-T,IS-T], with ROIC and operating margin at 2-year highs [RA-T,IS-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Peak margins and an extended price (40.7% above the 200-day average, P/E at 89% of its 5y range) de-rate if the hit-driven release slate slows, as in FY2023.",
    "veto": null
  },
  "thesis": "A high-return, net-cash IP publisher at peak margins whose price already discounts sustained high growth.",
  "rationale": "Quality, direction and balance sheet are excellent, but the price sits above even the bull fair value and near the top of its own multiple ranges, so the scorecard gives no valuation points. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 29180.00,
  "price_date": "2026-11-13",
  "research_note": "research/TYO-9766/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 30% (statistics page)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "TTM operating margin falls below 26% (statistics page)", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 26}},
    {"text": "TTM FCF margin falls below 12% (statistics page)", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "Debt/EBITDA rises above 3x (statistics page), ending the net-cash balance sheet", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 30519, "basis": "Margins hold at 2-year highs [RA-T] and P/E re-rates to its 5y max of 31.9x [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 25736, "basis": "P/E eases to the peer median of 26.9x [RA] as growth normalises from the reverse-DCF 18.4% bar; above the mechanical base fair value because ROIC has structurally improved [RA-T]."},
    "bear": {"probability": 0.25, "target_price_12m": 18083, "basis": "A softer slate as in FY2023 [RA] takes P/E to its 5y low of 18.9x [RA], near the mechanical base fair value of 19,284.86."}
  },
  "entry_price": 15427.89,
  "entry_basis": "valuation file: base 19,284.86 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

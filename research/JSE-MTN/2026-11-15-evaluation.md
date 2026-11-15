# Evaluation: MTN Group Limited (JSE:MTN) — 2026-11-15
## Bear case
The price has run ahead of the evidence. P/FCF of 8.4x and P/B of 3.3x are above their 5y maxima, EV/Sales is above its range, and P/E of 24.4x is far above the 10.3x peer median [Certain]. RSI is 78.9 and the price is 18.0% above its 50-day average, so an extended price risks a de-rating if growth slows or margins stall [Likely]. The two Direction change lines share one cause: the FCF-margin and ROIC rebound is a recovery from a naira-driven FY2023-24 trough (ROE -7.6%, net margin -5.0% in FY2024), not a new structural level; ROIC is still 2.4pp below its 2-year high [Likely]. The naira, policy rate and politics cannot be verified from official sources (macro overlay) [Certain]. No fair value is computable [Certain]. The pending IHS tower deal could add leverage [Likely].
## Bull case
Q3 2026 showed the business working: 9M service revenue and EBITDA growth with margin expansion and strong cash generation (Q3 transcript) [Likely]. TTM operating margin of 32.2%, ROCE of 26.9% and FCF margin of 21.7% are at 2-year highs, all rising over the last 12 months [Certain]. The FCF yield is 11.95% on 1.13x net debt/EBITDA with Piotroski F of 7 [Certain]. EV/EBITDA of 5.2x is 15% below peers [Certain]. The trend is strong: +14.9% above the 200-day average, +43.0% over 12 months, beating SPY by +32.6pp [Certain]. Licensed spectrum and scale in concentrated markets support pricing [Likely]. The rand is stable (macro overlay) [Certain]. Fintech and towers under Ambition 2030 could add value the group multiple does not show [Guessing].
## Decision
```json
{
  "ticker": "JSE:MTN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cash-generative pan-African mobile and fintech leader whose margins have recovered strongly from a currency-driven trough, now priced above its own 5-year P/FCF and P/B ranges on cash flow whose main risk, the naira, cannot be verified.",
  "rationale": "Quality, balance sheet and trend are real, but the price sits above its own 5y P/FCF and P/B ranges with RSI overbought, no fair value anchor and unverifiable naira risk. The scorecard gives conviction 3, unchanged from 2026-11-08: good, not compelling, so AVOID, with an entry at the 5y-low P/FCF.",
  "price_at_decision": 23459.0,
  "price_date": "2026-11-13",
  "research_note": "research/JSE-MTN/2026-11-15.md",
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Nothing is falling over 1 or 3 years; the 5-fiscal-year FCF-margin dip reflects the naira-driven FY2024 trough (FCF margin 11.5% [CF,IS]), and over the last 12 months FCF margin rose from 15.5% to 21.7% [CF-T,IS-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A repeat naira devaluation (FY2024: net margin -5.0% [IS]) that the allowed official sources cannot track, compounded by a de-rating of a price already above its 5y P/FCF and P/B ranges [RA] if growth slows.",
    "veto": null
  },
  "triggers": [
    {"text": "TTM operating margin falls below 28% (32.2% now), showing the margin recovery was a currency or cyclical peak.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "TTM ROIC falls below 12% (15.5% now), heading back toward the FY2023 trough of 8.3%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 15% (21.7% now), back below the level of a year earlier.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA rises above 2.0x (1.13x now), above the FY2024 stress level of 1.81x, e.g. from the IHS tower deal.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 27000, "basis": "Q3 momentum continues (transcript /quote/jse/MTN/transcripts/797249-q3-2026/), FCF margin holds near its 21.7% 2-year high [CF-T] and EV/EBITDA moves from 5.2x toward the 6.1x peer median [RA]; no mechanical fair value exists to reconcile against (no ZAR FX rate)."},
    "base": {"probability": 0.45, "target_price_12m": 23500, "basis": "Margins hold near TTM levels (operating 32.2% [IS]) while P/FCF of 8.4x, already above its 5y max of 7.7x [RA], drifts back toward its range, so cash growth is offset by de-rating; set without a mechanical fair value, which is data unavailable."},
    "bear": {"probability": 0.30, "target_price_12m": 15000, "basis": "A naira-led shock repeats the FY2023-24 trough (FCF margin 11.5%, net margin -5.0% in FY2024 [IS,CF]), the unverified country risk in the macro overlay (research/JSE-MTN/2026-11-15-macro.md), taking the price back toward its 52-week low of 14,950 [HI]."}
  },
  "entry_price": 17594,
  "entry_basis": "No fair value is computable (no ZAR FX rate), so the anchor is P/FCF back at its 5y low of 6.3x [RA] on TTM FCF, against 8.4x now: at that level the FCF yield would compensate for the unverified naira risk.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: MTN Group Limited (JSE:MTN) — 2026-11-08
## Bear case
The cash flow is cheap only if this is not a peak. P/FCF is 7.6x, 95% of its 5y range, and P/B 2.5x is 90% of range and above peers; P/E 22.1x is well above the peer median 13.5x [Certain]. The two Direction change lines share one cause. FY2023-24 was a currency-driven trough (ROIC 8.3%, net margin -5.0%), and the macro overlay names a naira devaluation as the likely driver [Likely]. The last 12 months' jump in FCF margin (15.5% to 21.7%) and ROIC is a cyclical recovery, not a structural gain: ROIC is still 2.4pp below its 2024 high and flat over five years [Likely]. Nigeria's currency, policy rate and politics cannot be verified from the allowed sources, so the main risk is open [Certain]. No fair value is computable [Certain]. The price is 9.3% above its 50-day average with RSI 67.3, so entry is not washed out [Certain].
## Bull case
Operating margin of 32.2% TTM and FCF margin of 21.7% are at 2-year highs, and ROCE of 26.9% is a 5y high [Certain]. The FCF yield is 13.15% on moderate leverage (1.13x net debt/EBITDA), with Piotroski F of 7 [Certain]. EV/EBITDA of 4.8x is 17% below the peer median 5.8x [Certain]. The Q2 2026 call cited strong commercial momentum in Nigeria and Ghana. The fintech separation and the Ambition 2030 framework could unlock value in mobile money that the group multiple does not show [Guessing]. Gross margin is rising (70.3% TTM) and leading spectrum positions give pricing power in concentrated markets [Likely]. If the naira stays stable, today's cash generation may be the new run-rate rather than a peak [Guessing].
## Decision
```json
{
  "ticker": "JSE:MTN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cash-generative pan-African mobile and fintech leader whose margins have recovered from a currency-driven trough, but the price already sits near the top of its own 5-year P/FCF and P/B ranges, so it assumes the recovery lasts while the naira risk that caused the trough cannot be verified.",
  "rationale": "Quality and cash yield are real, but multiples sit at the top of their own range on what may be peak, FX-sensitive cash flow. There is no fair value anchor, the price has run up and Nigeria risk is unverifiable. Good, not compelling: AVOID at conviction 3, with an entry where P/FCF returns to its 5y low.",
  "price_at_decision": 21317.0,
  "price_date": "2026-11-06",
  "research_note": "research/JSE-MTN/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 27% (32.2% now), showing the margin recovery was a cyclical or currency peak.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 27}},
    {"text": "TTM ROIC falls below 12% (15.5% now), heading back toward the FY2023 trough.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 15% (21.7% now), back to the level of a year earlier.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA rises above 2.0x (1.13x now), above the FY2024 stress level of 1.81x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 26000, "basis": "FCF margin holds near its 21.7% 2-year high [CF-T] and EV/EBITDA re-rates from 4.8x toward the 5.8x peer median [RA, peers]; there is no mechanical fair value to reconcile against (fact sheet: data unavailable, no ZAR FX rate)."},
    "base": {"probability": 0.45, "target_price_12m": 22000, "basis": "Margins stay near TTM levels (operating 32.2% [IS]) and P/FCF stays near 7.6x, at the top of its 5y range [RA], so returns come mainly from modest cash growth; set without a mechanical fair value, which is data unavailable."},
    "bear": {"probability": 0.30, "target_price_12m": 15000, "basis": "A naira-led currency shock repeats the FY2023-24 trough (FCF margin 11.5%, net margin -5.0% in FY2024 [IS,CF]), the open country risk in the macro overlay (research/JSE-MTN/2026-11-08-macro.md), taking the price back toward its 52-week low of 14,950 [HI]."}
  },
  "entry_price": 17670,
  "entry_basis": "No fair value is computable (no ZAR FX rate), so the anchor is P/FCF back at its 5y low of 6.3x [RA] on TTM FCF, against 7.6x now: at that level the high FCF yield would compensate for the unverified Nigeria currency risk.",
  "replaces": null,
  "replacement_reason": null
}
```

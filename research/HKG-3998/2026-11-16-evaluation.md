# Evaluation: Bosideng International Holdings Limited (HKG:3998) — 2026-11-16
## Bear case
Bosideng is a single-category, single-country, weather-exposed brand [Certain]. Gross margin has slipped from 60.1% to 57.2% over five years, the one sign that pricing power is softening and growth is being bought with mix or promotion [Certain]. ROCE sits 5.8pp below its 2-year high of 34.3% and FCF margin is well below its 2-year high of 29.2%, so returns and cash have come off their peak; FCF is lumpy (29.2% to 12.2% to 20.0%) and depends on inventory timing [Certain]. Shares rose 1.14% year on year, mild dilution [Certain]. The 12-month change is -10.1% and the 50-day average is below the 200-day, so the market is not yet confirming the value [Certain]. Results land on Nov 25, 2026; a warm winter or weak order book could push the multiple to its 5y low [Guessing]. The China risk premium may still be too low if domestic consumption stalls [Guessing].

## Bull case
ROIC is 81.2% TTM and rising, operating margin rose from 16.1% to 19.9% and net margin to 14.6%, with net cash at -2.24x EBITDA and Altman Z 5.25 [Certain]. The direction flags look temporary: ROCE is flat over the last year and FCF margin is up 7.8pp year on year, so the 2-year highs were a peak working-capital year, not a broken model [Likely]. EV/EBITDA 5.1x and EV/Sales 1.2x sit below their 5y minimums, P/FCF 8.7x is 36% below peers, and the FCF yield is 11.54% [Certain]. The reverse DCF implies revenue falls 11.7% in year 1, which rising margins and cash flow do not show [Likely]. Mechanical base fair value is 7.63 against a 4.57 close, even with a 3.5% China premium [Certain]. The price is 3.9% above its 200-day average with 6-month momentum of +9.9% [Certain]. The yuan is stable, so macro is context only [Likely].

## Decision
```json
{
  "ticker": "HKG:3998",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years. ROCE (28.5%) and FCF margin (20.0%) sit below their 2-year highs of 34.3% and 29.2%, but over the last year ROCE was flat (-0.2pp) and FCF margin rose 7.8pp [RA-T, CF-T]; the highs reflect a peak working-capital year (FCF conversion 220.5% in FY2024 [CF,IS]) while operating margin is flat at 19.9% and ROIC rose to 81.2% [IS-T, RA-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Brand pricing power erodes (gross margin already down from 60.1% to 57.2% [IS]) or a warm winter hits the Nov 25, 2026 results and order book, compressing margins in a single-category, China-only business.",
    "veto": null
  },
  "thesis": "China's leading down-apparel brand, with 81.2% ROIC, net cash and an 11.54% FCF yield, trades below its own 5-year minimum EV/EBITDA and EV/Sales, where the price implies an 11.7% revenue decline its margins and cash flow do not show.",
  "rationale": "The thesis is intact: returns and margins rose, the direction flags trace to a peak cash year, and the stock still trades below its own minimum cash multiples. The position sits near its target size, so HOLD rather than ADD; gross-margin slippage and a China-only, weather-exposed model keep the risk at medium.",
  "price_at_decision": 4.57,
  "price_date": "2026-11-13",
  "research_note": "research/HKG-3998/2026-11-16.md",
  "triggers": [
    {"text": "TTM gross margin falls below 55%, under the five-year low of 57.2%, signalling loss of brand pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}},
    {"text": "TTM operating margin falls below 17%, reversing most of the five-year rise from 16.1% to 19.9%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "TTM ROIC falls below 40%, a reversion toward FY2022 levels that undercuts the moat thesis.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "TTM FCF margin falls below 12%, under the FY2025 five-year low of 12.2%, signalling inventory or working-capital stress from a demand down-cycle.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 7.63, "basis": "The market stops pricing an 11.7% revenue decline [reverse DCF] and the price reaches the mechanical base fair value of 7.63 [fair value: IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 5.57, "basis": "EV/EBITDA recovers from 5.1x toward its 5y range [RA] as margins hold, matching the EV/EBITDA method's base value of 5.57 [fair value]; below the DCF because the China risk and weather cyclicality cap the re-rating (my judgement)."},
    "bear": {"probability": 0.25, "target_price_12m": 3.96, "basis": "A weak winter or gross-margin erosion in the Nov 25, 2026 results takes P/E to its 5y minimum of 10.3x [RA] on TTM earnings, below the mechanical bear of 4.95 because the bear case's margin hit is not in the history-based model."}
  },
  "entry_price": null,
  "entry_basis": "The holding already meets the buy bar at conviction 4 at today's price; price is not the obstacle, and the position is at its target size, so no lower re-entry level is needed.",
  "replaces": null,
  "replacement_reason": null
}
```

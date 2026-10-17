# Evaluation: RemeGen Co., Ltd. (HKG:9995) — 2026-10-17
## Bear case
The trailing profits are probably not recurring. Operating margin ran at -153.6%, -142.7% and -83.0% in FY2022-24 before turning to 61.2% TTM, and that turn lines up with the January 2026 AbbVie licensing deal [Likely]. The P/E of 5.5x and EV/EBITDA of 8.3x therefore rest on a one-off "E", not on real cheapness [Likely]. The mechanical fair value (base 359.42) is 100% EV/Revenue on that same inflated revenue, because rNPV is [data unavailable]. It cannot be relied on [Certain]. Rivals with deeper pockets and NRDL price talks threaten the two lead biologics [Likely]. The shares are in a clear downtrend: 21.8% below the 200-day average and down 44.2% over six months [Certain]. Q3 results on Oct 29, 2026 could show the profit fading [Guessing].

## Bull case
RemeGen has net cash (net debt/EBITDA -0.94x) and a Piotroski F-score of 7 [Certain]. Its upfront licensing cash pays for the pipeline, so dilution has been modest: shares up 3.88% YoY [Certain]. Two approved franchises, telitacicept in autoimmune disease and disitamab vedotin in HER2 oncology, have Phase 3 data in myasthenia gravis and Sjögren's [Likely]. Big-pharma interest (AbbVie, Vor Bio) supports the value of the platform [Likely]. EV/Sales of 5.4x sits below its 5-year minimum of 8.6x and below the peer median [Certain]. Beta is low at 0.46, so the stock is driven by its own news rather than the market [Certain].

## Decision
```json
{
  "ticker": "HKG:9995",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "RemeGen's swing to profit looks driven by one-off licensing income rather than recurring China product economics, so its low trailing multiples and model fair value do not show a durable, mispriced quality business.",
  "rationale": "This is not a quality business on the evidence: it lost money deeply in three of five years, and the TTM profit is likely licensing-driven. The fair value rests only on EV/Revenue of distorted revenue, with rNPV unavailable. Binary clinical and NRDL risks cannot be quantified. Good optionality, not a compelling core position.",
  "price_at_decision": 65.90,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-9995/2026-10-17.md",
  "triggers": [
    {"text": "TTM operating margin stays above 20% once the AbbVie upfront payment drops out of the trailing window, showing product sales alone are profitable.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 20}},
    {"text": "TTM FCF margin stays above 15% after the licensing payment rolls off, showing cash generation is structural rather than one-off.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 15}},
    {"text": "Company-reported product revenue for telitacicept and disitamab vedotin grows year on year in two consecutive reports with no new licensing income in the period."},
    {"text": "Dilution resumes: shares outstanding grow more than 8% YoY, showing the cash cushion is being spent.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 100.0, "basis": "Product sales prove recurring and EV/Sales of 5.4x re-rates toward the peer median of 8.6x [RA]; still well below the mechanical fair-value bear of 154.83, which values licensing-inflated revenue at the stock's own history."},
    "base": {"probability": 0.45, "target_price_12m": 70.0, "basis": "Margins normalise as licensing income fades (note section 6), so the shares trade sideways near the 50-day average of 76.61 and the 6-month low of 63.30 [HI]; the fair-value base of 359.42 is set aside because rNPV is [data unavailable] and EV/Revenue uses distorted revenue."},
    "bear": {"probability": 0.35, "target_price_12m": 52.0, "basis": "Q3 results on Oct 29, 2026 [ST] confirm losses on product economics like FY2022-24 (operating margin -83.0% to -153.6% [IS]) and the downtrend (6-month momentum -44.2% [HI]) breaks the 52-week low of 60.85."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

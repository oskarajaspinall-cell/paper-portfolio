# Evaluation: OBIC Co.,Ltd. (TYO:4684) — 2026-11-16
## Bear case
The price already discounts far more than the business delivers. The reverse DCF implies 24.3% year-1 revenue growth, and the mechanical base fair value of 4,205.92 JPY sits 32.2% below the 6,205.00 close; even the bull fair value of 4,573.86 is below it [Certain]. EV/Sales is at 99% of its 5y range and EV/EBITDA is +88% above peers [Certain]. The stock is 38.4% above its 200-day average after +34.6% in three months, so the valuation points come only from trend strength; an extended price like this risks a sharp de-rating toward the 5y P/E low of 22.2x if growth merely stays steady [Likely]. ROIC has slid from 27.5% to 22.4% and is 0.6pp below a year ago, and FCF margin is 2.0pp below its 2-year high of 55.2% [Certain]; Piotroski F is only 4 [Certain]. Capital return is modest relative to FCF [Likely].

## Bull case
OBIC is among the most profitable software businesses anywhere: operating margin 66.6% and FCF margin 53.2% TTM, both at or near records and rising over five years [Certain]. The ROIC slide reflects a growing cash pile, not operating weakness, since margins kept expanding [Likely]; the FCF margin dip below its 2-year high is small and the last year is still rising (+1.5pp) [Certain]. Net cash (net debt/EBITDA -2.08x), Altman Z 13.17 and beta 0.48 make the balance sheet a fortress [Certain]. Embedded accounting/ERP systems carry real switching costs [Guessing]. The trend is strong (above its 200-day average, RSI 61.3, 12-month change +24.4%) and P/E of 33.0x sits below its 5y median of 34.5x, so the multiple is not at an extreme on its own history [Certain].

## Decision
```json
{
  "ticker": "TYO:4684",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC is falling (27.5% FY2022 to 22.4% TTM [RA]) while operating margin (60.5% to 66.6%) and FCF margin (41.5% to 53.2%) rose [IS,CF]: the decline reflects accumulated net cash (net debt/EBITDA -2.08x [RA]) diluting invested capital, not lost share or pricing; the FCF margin sits 2.0pp below its 2-year high but rose 1.5pp over the last year [CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Valuation de-rating: the price implies 24.3% year-1 revenue growth (reverse DCF) and sits 38.4% above its 200-day average after +34.6% in three months; steady rather than accelerating growth could compress the multiple toward its 5y low.",
    "veto": null
  },
  "thesis": "A fortress-balance-sheet, 66.6%-operating-margin Japanese ERP franchise whose price already discounts growth well beyond its record, after a sharp rally.",
  "rationale": "Superb quality and a strong trend, but the price sits well above every mechanical fair value and implies growth the business has not shown; the scorecard does not reach the buy bar. Good but not compelling at this price: AVOID, with an entry price anchored on base fair value less the margin of safety.",
  "price_at_decision": 6205.00,
  "price_date": "2026-11-13",
  "research_note": "research/TYO-4684/2026-11-16.md",
  "triggers": [
    {"text": "ROIC (TTM, ratios page) falls below 20%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Operating margin (TTM) falls below 62%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 62}},
    {"text": "FCF margin (TTM) falls below 45%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 45}},
    {"text": "Net cash position lost: net debt/EBITDA (site definition) rises above 0x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 0.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 7000, "basis": "Margins keep expanding (operating margin 66.6% TTM, rising [IS-T]) and P/E moves toward its 5y max of 37.6x [RA]; well above the mechanical bull fair value of 4,573.86, which is blind to the trend strength."},
    "base": {"probability": 0.5, "target_price_12m": 6000, "basis": "P/E holds near its 5y median of 34.5x [RA] on modestly higher earnings, giving back a little of the +34.6% 3-month run [HI]; above the base fair value of 4,205.92 because the DCF ignores the sustained margin expansion."},
    "bear": {"probability": 0.25, "target_price_12m": 4100, "basis": "Growth disappoints the 24.3% implied by the reverse DCF and the multiple de-rates to the EV/Revenue bear value of 4,100.63 [fact sheet fair value], close to the base fair value of 4,205.92."}
  },
  "entry_price": 3364.74,
  "entry_basis": "valuation file: base 4,205.92 x 0.8 (base fair value less the 20% margin of safety).",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Qualys, Inc. (QLYS) — 2026-11-15
## Bear case
The price already asks more than the business delivers: the reverse DCF implies 12.9% year-1 revenue growth, above the low-double-digit growth reported, and the price sits above the mechanical base fair value of 154.59 [Certain]. The valuation case rests on trend strength, not a discount: the stock is +99.9% over 6 months and +25.7% above its 200-day average, so if growth slows the multiple de-rates, and management already flagged lumpy Q4 billings (https://stockanalysis.com/stocks/qlys/transcripts/724061-q3-2026/) [Likely]. The 3-month move is -11.7% and the price is 9.4% below its 50-day average, so the trend is cracking [Certain]. ROIC is 45.5pp below its 2-year high and ROCE 3.6pp below its high; I read both as normalisation from a peak, not erosion, but vulnerability scanning is contested by larger platforms [Likely]. Short interest of 8.84% shows a sizeable sceptical camp [Certain].

## Bull case
A franchise-quality software business: gross margin 83.3%, operating margin 34.5% and FCF margin 45.0%, all rising, with ROIC 107.5% and net cash (-1.80x net debt/EBITDA) [Certain]. The last 12 months improved: operating margin +1.9pp and FCF margin +3.4pp, ROIC +12.7pp on a year earlier [Certain]. Q3 beat and FY26 revenue and EPS guidance were raised (https://www.prnewswire.com/news-releases/qualys-announces-third-quarter-2026-financial-results-302933782.html) [Likely]. Own-history multiples are low: P/E at 9% and EV/EBITDA at 15% of their 5y ranges, a 5.37% FCF yield, and shares down 3.01% YoY from buybacks [Certain]. The stock is above its 200-day average with a positive 12-month change of 15.3%: a good business that is working [Certain].

## Decision
```json
{
  "ticker": "QLYS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python lists no metric falling over 1 or 3 years; the Direction-change lines (ROIC 45.5pp below its 2024-09-30 peak, ROCE 3.6pp below its high) reflect normalisation from a peak, with ROIC +12.7pp on a year earlier and operating and FCF margins rising [RA-T, IS-T, CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Growth slows (management flagged lumpy Q4 billings) and the extended price de-rates toward the mechanical base fair value, which sits below the price.",
    "veto": null
  },
  "thesis": "A net-cash, 45%-FCF-margin security-software franchise with rising margins trades low in its own multiple range but above its mechanical fair value, so the case rests on trend strength rather than a discount.",
  "rationale": "Quality and balance sheet are excellent and the trend is positive, but the price sits above base fair value and implies growth above what is reported, while the 3-month trend is weakening after a sharp run. Good but not compelling at this price; cash is acceptable.",
  "price_at_decision": 172.94,
  "price_date": "2026-11-13",
  "research_note": "research/QLYS/2026-11-15.md",
  "triggers": [
    {"text": "TTM gross margin falls below 80%, reversing the five-year rise to 83.3%.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 80}},
    {"text": "TTM operating margin falls below 28%, giving up the five-year expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "TTM FCF margin falls below 38%, back under the FY2024 level of 38.1%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 38}},
    {"text": "TTM ROIC falls below 60%, a break from the normalised range that would signal competitive erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 60}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 205.0, "basis": "Raised FY26 guidance is delivered and the multiple holds near its 5y median (EV/EBITDA 23.3x [RA]), consistent with the mechanical bull fair value of 202.88 [valuation]."},
    "base": {"probability": 0.5, "target_price_12m": 165.0, "basis": "Margins hold but growth stays below the 12.9% the reverse DCF implies [valuation], so the price drifts between the base fair value of 154.59 and the EV/Revenue estimate of 180.55 [valuation]."},
    "bear": {"probability": 0.25, "target_price_12m": 115.0, "basis": "Billings lumpiness becomes a slowdown and the extended price de-rates toward the mechanical bear fair value of 112.39 [valuation], with P/E near its 5y low of 24.0x [RA]."}
  },
  "entry_price": 123.67,
  "entry_basis": "valuation file: base 154.59 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

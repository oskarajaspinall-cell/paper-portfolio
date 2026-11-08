# Evaluation: H&R Block, Inc. (HRB) — 2026-11-08
## Bear case
The valuation leg of the entry thesis has largely played out: the stock has rallied from a 6-month low of 29.12 to 52.69, and P/E (9.3x), EV/EBITDA (7.4x) and P/FCF (8.6x, above its 7.5x median) now sit mid-range in their own 5-year history, not in the bottom fifth [Certain]. The EV/EBITDA fair-value leg (54.02) is about at the price; the 95.54 base rests on a DCF that extrapolates FCF [Certain]. **Direction change:** ROCE fell from 42.1% to 40.1% in 12 months, 8.7pp below its 48.8% 2-year high; the note blames capital growth, not weaker margins [Likely]. FCF conversion is 103.1% against 134.8% in FY2022, and the 18.6% net margin is flattered by a one-off IRS tax settlement [Certain]. Free filing is suspended, not ended. AI substitution and DIY regulatory inquiries are new 10-K risks; short interest is 16.40% [Certain]. No material foreign-country exposure; macro is context [Likely].
## Bull case
The business shows no sign of the decline the price implies: the reverse DCF prices -12.8% year-1 revenue growth, but operating margin rose to 23.0% and TTM ROIC held flat at 46.6% [Certain]. **Direction change:** TTM FCF margin rose from 15.9% to 19.2%, reversing the 5-year slide, so cash funding is improving [Certain]. An 11.64% FCF yield funds share shrinkage of 6.17% a year and a dividend raised 12.0% [company-reported], with net debt/EBITDA flat at 1.11x [Certain]. The assisted-preparation habit (11.3m US assisted returns [company-reported]) and brand are a real moat [Likely]. The December 3 Investor Day could reset the AI narrative [Guessing]. Even at a flat multiple, buybacks plus the dividend compound per-share value [Likely].
## Decision
```json
{
  "ticker": "HRB",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, cash-rich assisted tax-prep franchise whose fundamentals remain stable, but whose multiples have re-rated from the bottom of its own 5-year range to the middle, so the remaining upside is mostly shareholder yield rather than re-rating.",
  "rationale": "Quality is intact (operating margin 23.0%, ROIC flat, FCF margin recovering), but the valuation case that justified conviction 4 has mostly played out: own-history multiples are mid-range and the EV/EBITDA leg sits at the price. Free-filing, AI and short-interest risk remain. Good, not compelling: hold at the conviction-3 size.",
  "price_at_decision": 52.69,
  "price_date": "2026-11-06",
  "research_note": "research/HRB/2026-11-08.md",
  "triggers": [
    {"text": "TTM gross margin falls below 43%, breaking the five-year range (44.3%-45.7%), signalling price pressure from free/AI filing alternatives.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 43}},
    {"text": "TTM operating margin falls below 20%, under the FY2022 five-year low of 21.5%, showing the margin expansion has reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 15%, under the FY2025 low of 15.9%, meaning cash generation no longer funds buybacks and the dividend.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Trailing ROCE on the ratios page falls below 35%, or annual revenue declines year on year, or management discloses a loss of assisted-category share."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 72.0, "basis": "The Investor Day and stable filing-season results ease the free-filing/AI fear and P/E re-rates toward its 5y max of 12.8x from 9.3x [RA]; just above the mechanical bear fair value of 67.22 and below the 114.26 bull, which extrapolates DCF cash flows."},
    "base": {"probability": 0.5, "target_price_12m": 58.0, "basis": "EV/EBITDA drifts to its 5y median 7.9x from 7.4x [RA] with share count shrinking 6.17% a year [ST]; set well below the mechanical base 95.54 because its DCF leg extrapolates FCF that the EV/EBITDA leg (54.02) does not support."},
    "bear": {"probability": 0.25, "target_price_12m": 37.58, "basis": "AI substitution or a revived free-filing programme (10-K risk factors, note section 2) pushes the multiple back toward its 5y lows: the EV/EBITDA bear leg of 37.58 [fact sheet Fair value], below the blended bear of 67.22."}
  },
  "entry_price": 46.0,
  "entry_basis": "P/FCF back at its 5y median 7.5x from 8.6x [RA] on unchanged TTM FCF; base fair value 95.54 x 0.8 sits above the price, and the DCF-led base overstates value relative to the EV/EBITDA leg, so the own-history P/FCF median is the anchor.",
  "replaces": null,
  "replacement_reason": null
}
```

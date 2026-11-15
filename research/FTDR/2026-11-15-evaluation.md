# Evaluation: Frontdoor, Inc. (FTDR) — 2026-11-15
## Bear case
The price already discounts more than the business is delivering. P/E 24.4x and EV/EBITDA 13.5x sit above their 5-year maxima (24.2x, 12.7x) and about a third above peers [Certain]. The reverse DCF implies 14.2% year-1 revenue growth against roughly 6 percent reported growth [company-reported] [Certain]; the mechanical base fair value is 57.55 USD against a 96.64 close [Certain]. Trading +35.8% above the 200-day average after +88.5% in 12 months, the stock risks a sharp de-rating if growth merely stays mid-single-digit [Likely]. ROIC is 21.5pp below its 2-year high of 60.1% and ROCE 16.3pp below its 40.8% high; the drop from the 2024 peak shows returns are volatile with claims costs [Likely]. Beta 1.60, repair-cost inflation and weak home turnover (MD&A still cites elevated rates and cost inflation) are live risks [Certain]. A $1 billion buyback near highs could destroy value [Guessing].

## Bull case
A recurring, capital-light franchise that is working: renewals are 75 percent of nine-month revenue [company-reported], operating margin is at a 2-year high of 20.3% and FCF margin 18.0%, with FCF conversion of 137.9% of net income [Certain]. The ROIC/ROCE direction change is a normalisation from an unusually high 2024 base, not a fresh decline: both rose over the last 12 months (ROIC 32.9% to 38.5%) [Certain]. Q2 saw member count rise for the first time in five years and Q3 beat with FY26 guidance given [Likely]. Cash multiples are not stretched: P/FCF 16.6x sits at its 5-year median and below the 22.6x peer median, a 6.02% FCF yield [Certain]. Net debt/EBITDA 1.12x, shares down 5.51% YoY and a new $1 billion authorisation compound per-share value [Certain]. The 10-Q drops the "declining" real-estate wording [Certain].

## Decision
```json
{
  "ticker": "FTDR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and ROCE are down over 3 years only from an unusually high 2024 peak (60.1% / 40.8%); both rose over the last 12 months (ROIC 32.9% to 38.5%, ROCE 22.2% to 24.5%) while operating margin is at its 2-year high of 20.3% [RA-T, IS-T], i.e. a normalisation, not lost share or a broken model.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "De-rating: P/E and EV/EBITDA sit above their 5-year maxima and the price implies 14.2% year-1 growth against ~6 percent reported [company-reported]; if growth stays mid-single-digit the multiple compresses, compounded by claims-cost inflation.",
    "veto": null
  },
  "thesis": "A recurring, capital-light home-warranty franchise with record margins and a 6.02% FCF yield is working, but earnings multiples above their own 5-year range already price growth well beyond what is being delivered.",
  "rationale": "Quality, balance sheet and trend are strong, but the earnings multiples are above their 5-year maxima and the price implies growth more than double the reported rate; the skew is balanced, not compelling. Python's scorecard sets the conviction.",
  "price_at_decision": 96.64,
  "price_date": "2026-11-13",
  "research_note": "research/FTDR/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 17% (20.3% now), showing claims-cost inflation is outrunning pricing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "TTM FCF margin falls below 14% (18.0% now), showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "TTM ROIC falls below 28% (38.5% now), below the FY2021 level, showing returns erosion rather than normalisation.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 28}},
    {"text": "Net debt/EBITDA rises above 2.5x (1.12x now), showing buybacks are being debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 115, "basis": "P/E holds near its current 24.4x [RA] as margins stay at the 20.3% 2-year high [IS-T] and buybacks (shares -5.51% YoY [ST]) lift per-share earnings; above the mechanical bull of 76.90 because the own-history model misses the margin step-up."},
    "base": {"probability": 0.45, "target_price_12m": 92, "basis": "P/FCF stays near its 5y median 16.6x [RA] on modestly growing FCF while P/E drifts toward its 24.2x max; above the 57.55 mechanical base because the DCF's history-based growth ignores the 18.0% FCF margin [CF-T]."},
    "bear": {"probability": 0.30, "target_price_12m": 64, "basis": "Growth stays near the ~6 percent reported [company-reported] versus the 14.2% the price implies (reverse DCF), so EV/EBITDA reverts toward its 5y median 11.0x [RA], near the mechanical bull of 76.90 less claims-cost pressure."}
  },
  "entry_price": 46.04,
  "entry_basis": "valuation file: base 57.55 x 0.8 (default margin of safety)."
}
```

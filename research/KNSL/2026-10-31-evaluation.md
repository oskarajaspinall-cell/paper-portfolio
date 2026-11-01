# Evaluation: Kinsale Capital Group (KNSL) — 2026-10-31
## Bear case
The E&S cycle is turning against Kinsale. Third-quarter gross written premiums fell 4.8%, with property down 19.3% on "heightened competition" and casualty up only 0.9% [company-reported] (https://www.sec.gov/Archives/edgar/data/1669162/000166916226000050/knsl-20260930.htm) [Certain]. The historical 26.1x median P/E [RA] was paid for growth that is now fading, so the multiple floor has likely reset lower [Likely]. Even after de-rating, the stock trades above base fair value of 296.59 and at a premium to peers: +18% on P/E and +82% on P/B [RA] [Certain]. Adverse construction liability development in the 2017 and 2018 accident years shows reserve risk in long-tail casualty [Certain]. Softening pricing tends to hit underwriting margins with a lag, so the 27.8% ROE [RA] is likely near a peak [Guessing]. A CFO transition adds execution noise [Certain].

## Bull case
This is a best-in-class underwriter: ROIC 24.3% and ROE 27.8% TTM, both higher than five years ago [RA] [Certain]. Every multiple sits below its own 5y minimum: P/E 15.9x versus 18.1x, P/B 4.3x versus 4.6x, P/FCF 8.5x with an 11.82% FCF yield [RA,ST] [Certain]. Leverage is negligible (net debt/EBITDA 0.33x) and buybacks cut shares 1.83% YoY [BS,ST] [Certain]. Net income fell 30.7% mainly from investment repositioning that raises future yields, not from underwriting [company-reported] (https://www.sec.gov/Archives/edgar/data/1669162/000166916226000050/knsl-20260930.htm) [Certain]. Prior years still developed favorably overall by $19.7 million [company-reported] [Certain]. The low-cost platform should let Kinsale take share once the soft market washes out weaker carriers [Guessing].

## Decision
```json
{
  "ticker": "KNSL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A best-in-class E&S underwriter is cheap against its own history, but falling premiums in a softening market leave it above base fair value and at a steep peer premium, so the skew is not yet compelling.",
  "rationale": "Quality is excellent and multiples sit below their 5y lows, but the price still exceeds mechanical base fair value and peers, and premium declines suggest the historical multiples no longer apply. Probability-weighted scenarios sit below the price. Good but not compelling: AVOID, entry price set at base fair value less the margin of safety.",
  "price_at_decision": 365.71,
  "price_date": "2026-10-30",
  "research_note": "research/KNSL/2026-10-31.md",
  "triggers": [
    {"text": "TTM ROE falls below 20% (27.8% now), showing soft-market pricing is eroding underwriting returns.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 18% (24.3% now, FY2022 low 19.3%), signalling the cost/data edge is no longer protecting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "Gross written premiums in a 10-Q fall more than 10% year on year in any quarter, showing the soft market is shrinking the franchise, not just property."},
    {"text": "Adverse prior-year reserve development exceeds favorable development in any quarter (10-Q MD&A), showing casualty reserving risk."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 453.55, "basis": "Premiums stabilise and the multiples, now below their 5y minimums (P/E 15.9x vs 18.1x [RA]), recover toward their range, matching the fact sheet's bull fair value."},
    "base": {"probability": 0.5, "target_price_12m": 320.0, "basis": "Soft-market premium declines (property down 19.3% [company-reported], note) keep multiples near current lows; set between the mechanical base 296.59 and the P/E-method base 345.45 because ROE 27.8% [RA] still supports some premium to book."},
    "bear": {"probability": 0.3, "target_price_12m": 237.13, "basis": "Pricing pressure spreads to casualty and reserves weaken (adverse 2017-2018 construction development [company-reported], note), compressing P/B toward peers and matching the fact sheet's bear fair value."}
  },
  "entry_price": 237.27,
  "entry_basis": "valuation file: base 296.59 x 0.8, a margin of safety that would compensate for the softening E&S cycle.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Jack Henry & Associates (JKHY) — 2026-11-07
## Bear case
The entry thesis was mispricing: the price implied 0.4% growth. That gap has closed. The reverse DCF now needs 11.9% year-1 revenue growth, above what has been reported, and the price sits above even the mechanical bull fair value of 141.70 (base 129.12) [Certain]. Q1 FY2027 growth is flattered by lumpy deconversion fees; services and support grew 5.1% without them [company-reported]. R&D is growing faster than revenue, and cloud, AI and security spending weighs on margins [company-reported]. The stock trades well above peers on EV/EBITDA (+93%) [Certain], and RSI of 64.9 after a 21.2% six-month gain leaves little cushion if results slow [Likely]. Over 12 months, most of the upside is likely already in the price [Likely].

## Bull case
The business has improved since entry, so the old fair value is out of date. ROIC recovered from 19.1% in FY2024 to a TTM 24.3%, operating margin to 25.6% and FCF conversion to 138.2% [Certain]. Q1 FY2027 brought processing revenue +10.7% [company-reported], record revenue, nine core wins and higher FY27 guidance [Likely]. Even after the rally, P/E of 23.8x and P/FCF of 17.4x sit in the lower part of their own 5y ranges (medians 31.7x and 23.7x) [Certain]. The P/E method gives a base of 230.66 [Certain]. The balance sheet is essentially unlevered (net debt/EBITDA 0.10x) and buybacks cut the share count 2.22% [Certain]. Core-system switching costs keep churn low [Likely]. The thesis is still running, but less of the upside is left.

## Decision
```json
{
  "ticker": "JKHY",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, unlevered core-banking franchise whose returns and margins have improved since entry still trades below its own 5-year median multiples, but the price now implies growth above what has been delivered, so the remaining upside is modest.",
  "rationale": "Quality is improving and multiples are still below their own history, so the thesis has not broken. But the mispricing that justified entry has largely closed: the reverse DCF now needs above-trend growth and the DCF range sits below the price. Conviction falls to 3. Hold the existing position; no add, and no forced sale while fundamentals keep improving.",
  "price_at_decision": 173.23,
  "price_date": "2026-11-06",
  "research_note": "research/JKHY/2026-11-07.md",
  "triggers": [
    {"text": "TTM ROIC falls below 19%, the FY2024 trough, evidencing moat erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 19}},
    {"text": "TTM operating margin falls below 22%, under the FY2024 low of 22.1%, showing cloud/AI/security investment or renewal pricing is compressing profitability structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}},
    {"text": "TTM FCF margin falls below 20%, reversing the 5-year rising trend (FY2026 27.3%).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Processing revenue growth in the 10-Q MD&A falls below 5% year on year for two consecutive quarters."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 205, "basis": "Continued core wins and raised FY27 guidance [note, prnewswire Q1 release] let P/E move partway from 23.8x toward its 5y median 31.7x [RA]. This is below the P/E-method base of 230.66 and above the DCF bull of 141.70, because the DCF does not capture the improved ROIC and margins [IS,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 180, "basis": "P/E holds near 23.8x [RA] while earnings compound on 25.6% TTM operating margin and 2.22% share shrinkage [IS,ST]. This is above the DCF base of 129.12, which uses own-history growth below the improved recent trend."},
    "bear": {"probability": 0.25, "target_price_12m": 142, "basis": "Growth falls short of the 11.9% the price implies [fact sheet reverse DCF] and P/E drops to its 5y low of 19.5x [RA], which lands near the DCF bull value of 141.70."}
  },
  "entry_price": 103.30,
  "entry_basis": "valuation file: base 129.12 x 0.8 (fact sheet Fair value [IS,BS,CF,RA,ST]). At that price the same improving-quality evidence would again justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

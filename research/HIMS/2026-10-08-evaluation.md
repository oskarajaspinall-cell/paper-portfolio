# Evaluation: Hims & Hers Health, Inc. (HIMS) — 2026-10-08
## Bear case
Profitability has reversed: TTM operating margin -3.8% vs +5.2% FY2025, ROE -32.0% vs +25.2%, and gross margin has slid from 82.0% (FY2023) to 69.5% [Certain]. The growth engine, compounded GLP-1s, sits in the FDA's crosshairs, with warning letters in September and December 2025 and a February 2026 FDA statement naming Hims [Certain]. FCF margin has fallen to 3.2% from 14.2%, and FCF conversion is -58.5% [Certain]. Piotroski F 2/9 and Altman Z 1.98 flag a weak, deteriorating balance of fundamentals [Certain]. Yet the stock trades at 78.4x P/FCF and 21.3x P/B, above its 5-year P/B max and far above telehealth peers [Certain]. A securities class action is pending [Likely]. The 10-K cites no switching costs [Certain]. With beta 2.43, rising real yields add a second headwind [Likely].
## Bull case
The brand has scale: FY2024-FY2025 showed the model can earn positive operating margins (4.5%, 5.2%) and a 14.2% FCF margin [Certain]. Shares outstanding fell 7.33% YoY, so management is buying back stock [Certain]. EV/Sales of 2.8x sits below its 5-year median of 3.4x [Certain]. Short interest is 24.76% of float and fell 9.8% last month, so any clean quarter or regulatory clarity could squeeze the stock sharply [Likely]. Vertical integration (owned 503A/503B pharmacies, peptide facility) and international clinical hires suggest optionality beyond GLP-1s [Guessing]. A rebound to positive TTM margins would quickly reverse the ROE and ROCE optics [Guessing].
## Decision
```json
{
  "ticker": "HIMS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A DTC telehealth platform with no evident moat, reversing margins and live FDA risk to its main growth line trades at 78.4x P/FCF and above its 5-year P/B max, so the price does not compensate for the deterioration.",
  "rationale": "This fails both core tests. Quality is deteriorating (negative TTM operating margin, gross-margin slide, F-score 2), and valuation is rich against its own history and peers, with no computable fair-value anchor. Regulatory and litigation risk plus a small macro bear tilt skew the outcomes down. Conviction 2 is below the buy threshold, so: AVOID.",
  "price_at_decision": 29.54,
  "price_date": "2026-10-07",
  "research_note": "research/HIMS/2026-10-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above the FY2025 level of 5.2%, showing profitability has turned back up.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 5.2}},
    {"text": "TTM gross margin recovers above 75%, showing the slide from 82.0% (FY2023) to 69.5% has stopped.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 75}},
    {"text": "TTM FCF margin recovers above the FY2024 level of 14.2%, restoring cash conversion.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 14.2}},
    {"text": "No new FDA warning letters or compounding-restriction actions against Hims's GLP-1 products are disclosed in the next two 10-Q/10-K filings."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 35.87, "basis": "Margins turn positive again and EV/Sales re-rates from 2.8x to its 5y median of 3.4x [RA], with high short interest of 24.76% [ST] amplifying the move; the fact sheet has no mechanical fair value [data unavailable], so this targets the stock's own EV/Sales history."},
    "base": {"probability": 0.4, "target_price_12m": 29.54, "basis": "EV/Sales holds near its current 2.8x [RA] while TTM margins stay near breakeven (operating margin -3.8% [IS]); there is no mechanical fair value to reconcile to, so the base case holds the multiple flat."},
    "bear": {"probability": 0.4, "target_price_12m": 20.04, "basis": "FDA compounding restrictions hit the GLP-1 line (note, SEC 10-K) and EV/Sales compresses to its 5y min of 1.9x [RA]; the macro overlay's small toward-bear tilt (research/HIMS/2026-10-08-macro.md: rising real yields on a beta-2.43 stock) lifts this scenario's probability from 0.35 to 0.4 at base's expense."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

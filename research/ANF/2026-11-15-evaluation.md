# Evaluation: Abercrombie & Fitch Co. (ANF) — 2026-11-15
## Bear case
The returns are cyclical, not compounding: ROIC fell to 1.3% in FY2023 before recovering [Certain], and TTM ROIC has fallen from 29.7% to 26.7% in a year, 12.2pp below its 2-year high [Certain]. TTM margins are flattered by about $100 million of non-recurring tariff refunds [company-reported] (https://www.sec.gov/Archives/edgar/data/1018840/000101884026000047/anf-20260801.htm), so the 12.8x P/E is less cheap than it looks [Likely]. The moat is brand heat that must be re-earned each season [Likely]. The price is +38.5% above its 200-day average after a 109.0% 12-month gain: if growth slows at the Nov 24 results, an extended stock with 12.09% short interest can de-rate hard [Likely]. EV/Sales and P/B sit near the top of their 5y ranges [Certain], buybacks now execute at doubled prices [Likely], and the fair-value methods disagree widely with a negative DCF bear [Certain]. The 10-Q flags Middle East freight and EMEA demand pressure, unquantified [Guessing].

## Bull case
This is a good business that is working: TTM ROIC 26.7%, operating margin 14.1% (flat over the year) and FCF margin 10.6% (up 3.8pp) [Certain]. The ROIC dip reflects normalisation from a peak and a larger capital base, not margin erosion [Likely]. Net debt/EBITDA is 0.71x and Altman Z 4.98, so the balance sheet carries no risk [Certain]. An 8.97% FCF yield funds a share count down 9.81% YoY [Certain]. Q2 sales rose to a record and full-year guidance was raised (https://www.wsj.com/business/retail/abercrombie-lifts-outlook-as-profit-sales-rise-dc5bf32f) [Likely], yet the reverse DCF implies only 0.8% year-1 revenue growth [Certain]. EV/EBITDA of 7.6x is below the 9.7x peer median [Certain]. Relative strength vs SPY is strong across 3, 6 and 12 months [Certain]. Macro is context only: the euro's fall is a modest translation drag on EMEA (macro overlay) [Likely].

## Decision
```json
{
  "ticker": "ANF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Python flags TTM ROIC falling (29.7% -> 26.7%) and ROCE (31.5% -> 30.1%), but operating margin is flat (+0.1pp) and FCF margin rose 3.8pp [RA-T, IS-T, CF-T]: normalisation from the FY2025 peak and a larger capital base, not lost share or margin erosion (note section 2).",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "Brand heat fades as the non-recurring tariff refund rolls off, and a stock +38.5% above its 200-day average with 12.09% short interest de-rates on slower growth at the Nov 24 results.",
    "veto": null
  },
  "thesis": "A high-return, lightly levered specialty apparel retailer with flat margins, rising FCF and heavy buybacks trades on a 8.97% FCF yield after doubling, but its returns are fashion-cyclical and TTM profits are flattered by a one-off tariff refund.",
  "rationale": "Quality and cash generation are strong and the price implies little growth, but the moat is brand heat rather than structural, TTM margins include a non-recurring refund, the fair-value methods disagree widely and the stock has doubled into a results date. Good but not compelling: AVOID, consistent with the 2026-11-09 verdict on the same evidence.",
  "price_at_decision": 148.88,
  "price_date": "2026-11-13",
  "research_note": "research/ANF/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20% (26.7% now), showing returns are mean-reverting toward the FY2023 trough rather than normalising.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 11% (14.1% now), showing margin gains reverse once the tariff refund rolls off.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11}},
    {"text": "TTM gross margin falls below 58% (63.7% now), signalling markdowns and fading brand heat.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 58}},
    {"text": "Net debt/EBITDA rises above 2.0x (0.71x TTM now), showing buybacks outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 245.11, "basis": "Raised guidance holds ex-refund and buybacks continue, reaching the mechanical bull fair value of 245.11 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.45, "target_price_12m": 170.30, "basis": "Margins hold near the flat TTM 14.1% operating margin [IS-T] while the refund rolls off, consistent with the mechanical base fair value of 170.30 [IS,BS,CF,RA,ST,HI]."},
    "bear": {"probability": 0.30, "target_price_12m": 85.62, "basis": "Brand heat fades and EBITDA normalises ex-refund, taking value to the EV/EBITDA bear of 85.62 [RA]; the negative DCF bear is unreliable and not used."}
  },
  "entry_price": 136.24,
  "entry_basis": "valuation file: base 170.30 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

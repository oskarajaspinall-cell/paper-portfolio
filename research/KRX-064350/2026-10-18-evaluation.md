# Evaluation: Hyundai Rotem Company (KRX:064350) — 2026-10-18
## Bear case
The stock has fallen from a 282,000 KRW 52-week high to 96,900 KRW, -54.6% over 12 months and -39.1% over three months, while reported fundamentals still look excellent [Certain]. A collapse of that size in a contract-driven defense and rail manufacturer usually means the market sees a backlog, export-order or margin reset that FY2025/TTM figures do not yet show; neither the note nor the fact sheet explains the cause [Likely]. Cash generation is lumpy: FCF margin swung -3.7% → 21.6% → 1.4% → 13.3% in five years, so the 15.76% FCF yield may be a working-capital peak [Certain]. TTM ROIC of 187.2% is not a repeatable level [Likely]. Piotroski F is only 4, insider ownership 0.01% [Certain]. Results are due Oct 19, 2026, one trading day away; buying ahead of an unexplained re-rating is a gamble, not a thesis [Certain]. Mechanical bear fair value is 22,143 KRW [Certain].
## Bull case
Five years of rising quality: operating margin 2.8% → 17.2% (FY25), ROE 3.9% → 30.5%, and net debt/EBITDA from 7.89x to net cash at -2.30x TTM [Certain]. Valuation sits below its own 5-year minimum on P/E (13.1x vs 13.3x) and EV/EBITDA (7.6x vs 10.3x), and far below the Korean defense peer median (EV/EBITDA 25.6x, P/E 43.8x) [Certain]. The reverse DCF implies -14.1% revenue growth in year 1, harsher than any trend in the reported numbers [Certain]. Base fair value 180,828 KRW, +86.6% above the close [Certain]. If tomorrow's results confirm margins hold, the gap to peers and its own history could close sharply given beta 1.67 [Guessing]. Defense procurement is budget-driven and largely insulated from US macro (overlay: context weight) [Likely].
## Decision
```json
{
  "ticker": "KRX:064350",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash rail and defense manufacturer with five years of rising margins trades below its own 5-year minimum P/E and EV/EBITDA, but an unexplained collapse from its 52-week high one day before results means the market may be pricing a fundamental reset the reported numbers do not yet show.",
  "rationale": "Cheap on every multiple with improving quality, but the cause of the -54.6% drawdown is unresearched, cash flow is contract-lumpy, Piotroski F is 4, and results land Oct 19, 2026. Good but not compelling: conviction 3, so AVOID and re-research after results confirm or refute the margin trend.",
  "price_at_decision": 96900.00,
  "price_date": "2026-10-16",
  "research_note": "research/KRX-064350/2026-10-18.md",
  "triggers": [
    {"text": "TTM operating margin rises back above 15.9% after the Oct 19, 2026 results would support conviction 4; a fall below 10% (around the FY2024 10.4% level) confirms the margin expansion was a peak.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10}},
    {"text": "TTM FCF margin turns negative, as in FY2021 (-3.7%), showing the cash surge was a working-capital unwind, not earnings power.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "TTM gross margin falls below 18%, under the FY2024 level of 18.9%, signalling contract pricing or export-mix deterioration.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 18}},
    {"text": "Net debt/EBITDA (ratios page) turns positive again from net cash (-2.30x TTM), indicating contract losses or working-capital strain."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 232644.56, "basis": "Results confirm margins hold and EV/EBITDA re-rates toward its 5y median 18.3x [RA], matching the mechanical EV/EBITDA bull value 232,644.56 KRW; below the DCF bull because DCF extrapolates lumpy contract FCF [CF]."},
    "base": {"probability": 0.4, "target_price_12m": 115000, "basis": "EBITDA holds but EV/EBITDA recovers only partly toward its 5y minimum 10.3x [RA] while the drawdown's cause stays unresolved; below the 180,828 KRW mechanical base because that DCF capitalises a TTM FCF margin of 26.4% [CF,IS] that has swung widely."},
    "bear": {"probability": 0.4, "target_price_12m": 62350.13, "basis": "The -54.6% fall [ST] reflects a real backlog or margin reset and EBITDA falls, in line with the EV/EBITDA bear value 62,350.13 KRW; above the blended bear 22,143 KRW, which leans on an extreme DCF bear of 2,039 KRW."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: base fair value less the margin of safety sits above the current price, and the issue is the unexplained collapse plus imminent Oct 19, 2026 results; a lower price would not change the decision until results show whether margins and cash flow hold.",
  "replaces": null,
  "replacement_reason": null
}
```

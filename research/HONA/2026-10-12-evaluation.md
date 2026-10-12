# Evaluation: Honeywell Aerospace Inc. (HONA) — 2026-10-12
## Bear case
Profitability is deteriorating fast: operating margin fell from 24.8% (FY2023) to 17.3% TTM and net margin from 20.9% to 10.9% [Certain] (fact sheet, IS). TTM ROIC has dropped to 18.3% from 33.6% in FY2025 [Certain] (RA). The August guidance cut and ~20% one-day fall point to supply-chain problems that are not yet fixed; revised guidance still cites constraints [Likely] (fact sheet headlines). Leverage built at the spin-off leaves net debt/EBITDA at 4.27x with no parent support [Certain] (BS, IS). Several securities class actions are pending and short interest rose 61.9% in a month [Certain] (ST). Valuation cannot be shown: every multiple and both fair-value methods are [data unavailable] [Certain]. Q3 results on Oct 28 could bring another reset [Guessing]. Piotroski F-score is 3 [Certain] (ST).
## Bull case
This is a franchise aerospace supplier with high-margin aftermarket exposure on a large installed base, protected by certification and switching costs [Likely] (note). Cash generation holds up: FCF margin is 13.9% TTM and FCF conversion is 128.3% [Certain] (CF, IS). The stock is 47% below its 52-week high of 297.50, with a 4.99% FCF yield [Certain] (HI, ST). Management reports strong commercial and defense demand, and investments are easing bottlenecks [Likely] (fact sheet transcripts). The spin-off debt is fixed-rate and long-dated, so the macro rise in yields does not reach it [Likely] (macro overlay). If margins stabilise, a de-rated, newly separated name could re-rate as supply normalises [Guessing].
## Decision
```json
{
  "ticker": "HONA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A quality aerospace aftermarket franchise whose post-spin margins, returns and leverage are deteriorating, with no computable valuation anchor to prove the 47% drawdown makes it cheap.",
  "rationale": "A core BUY needs a good business at a demonstrably attractive price. Margins and TTM ROIC are falling, leverage is 4.27x, class actions are pending, and every multiple and fair-value method is unavailable, so cheapness cannot be shown. Q3 results land Oct 28. Conviction 2 means no position; cash is acceptable.",
  "price_at_decision": 157.94,
  "price_date": "2026-10-09",
  "research_note": "research/HONA/2026-10-12.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 20.7% (the FY2025 level), showing the supply-chain margin squeeze was transitory; this would reopen the case.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 20.7}},
    {"text": "TTM operating margin falls below 15%, confirming structural margin erosion and keeping the stock an AVOID at any price.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA falls below 4.27x (current TTM) on a sustained basis with a stated deleveraging path, reducing post-spin balance-sheet risk.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 4.27}},
    {"text": "TTM FCF margin falls below 13.3% (the FY2024 level), showing cash conversion no longer offsets the earnings decline.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 13.3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 222.54, "basis": "Supply bottlenecks ease and operating margin recovers toward FY2025's 20.7% [IS], retracing to the Aug 5 swing high of 222.54 [HI]; no fair value is computable on the fact sheet, so the target is anchored to price history."},
    "base": {"probability": 0.45, "target_price_12m": 160.0, "basis": "Margins stabilise near the 17.3% TTM operating margin [IS] and the 4.99% FCF yield [ST] holds, so the stock stays around its 150-176 range of recent swing lows and highs [HI]; fair value is [data unavailable]."},
    "bear": {"probability": 0.3, "target_price_12m": 125.0, "basis": "A further guidance cut on Oct 28 and the class-action overhang push the stock below its 149.19 52-week low [HI] as operating margin slides toward 15% with leverage at 4.27x [BS,IS]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is 2, so no entry price is required. Price is also not the main obstacle: margins and TTM ROIC are falling, litigation is pending and no valuation anchor exists. A lower price alone would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Cognizant Technology Solutions (CTSH) — 2026-10-08
## Bear case
This is cheap for a reason. ROIC has fallen every year, from 20.5% (FY2021) to 14.8% TTM, and gross margin from 37.3% to 33.4% [Certain] (fact sheet RA/IS). That is the profile of a people-intensive service losing pricing power, and generative AI threatens the labour-based billing model directly [Likely]. Management's severance-led "Project Leap" restructuring admits the cost base needs self-disruption [Likely] (note, 10-Q). Net debt/EBITDA has moved from net cash (-0.19x) to 0.26x as bolt-on M&A begins [Certain]. Piotroski F is only 4 [Certain]. Q3 results on Oct 29 could show further deterioration [Guessing]. Multiples below their 5-year minimums can stay there while returns decline. Real yields up +48bp in a month cap any re-rating (macro overlay) [Likely].
## Bull case
Every multiple is below its 5-year minimum and the peer median: EV/EBITDA 6.6x vs 8.1x min and 8.6x peers, P/FCF 9.9x, FCF yield 10.11% [Certain] (fact sheet RA/ST). Cash generation is improving, not breaking: FCF conversion is 117% and FCF margin 12.0% TTM, while operating margin has risen to 16.3% [Certain]. Shares are down 3.24% YoY, so buybacks return value even without a re-rating [Certain]. The balance sheet is sound (Altman Z 5.91) [Certain]. Recent wins (Gilead extension, SITA) suggest AI-led demand is real [Likely]. Stable returns alone could lift the multiple back toward its 5-year floor [Guessing].
## Decision
```json
{
  "ticker": "CTSH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Cognizant is statistically cheap, below every 5-year minimum multiple at a 10.11% FCF yield, but falling ROIC and gross margin plus AI pressure on labour-based IT services make it a possible value trap rather than mispriced quality.",
  "rationale": "Valuation and cash conversion are attractive, but the thesis needs returns to stabilise, and five years of falling ROIC and gross margin, the Project Leap restructuring and AI disruption risk show no sign of that yet. Q3 results are due Oct 29. Good but not compelling: conviction 3, so AVOID under the owner rule.",
  "price_at_decision": 57.07,
  "price_date": "2026-10-07",
  "research_note": "research/CTSH/2026-10-08.md",
  "triggers": [
    {"text": "TTM ROIC recovers above the FY2024 level of 17.9%, showing the five-year decline in returns has reversed.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 17.9}},
    {"text": "TTM gross margin recovers above the FY2024 level of 34.3%, evidence that pricing pressure from AI and offshore peers is easing.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 34.3}},
    {"text": "Q3 2026 or later results (SEC 10-Q/8-K) show Project Leap restructuring lifting margins without further loss of gross margin, i.e. the AI productivity gains are kept, not passed on to clients."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 70.0, "basis": "Returns stabilise and EV/EBITDA re-rates from 6.6x to its 5-year minimum of 8.1x [RA], with net debt only 0.26x EBITDA [BS,IS], roughly 70."},
    "base": {"probability": 0.45, "target_price_12m": 59.0, "basis": "Multiples stay near P/E 12.5x [RA] as slow ROIC erosion offsets the 10.11% FCF yield [ST] and 3.24% share shrink [ST], a small gain from buybacks."},
    "bear": {"probability": 0.30, "target_price_12m": 45.0, "basis": "ROIC (14.8% TTM) and gross margin (33.4%) keep falling [RA,IS] on AI-driven pricing pressure, and the multiple de-rates toward the June low of 37.08 [HI]; the macro overlay's neutral/small tilt (real yields +48bp/1m cap re-rating) leaves these probabilities unchanged (research/CTSH/2026-10-08-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

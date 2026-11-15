# Evaluation: Eli Lilly and Company (LLY) — 2026-11-15
## Bear case
The price is extended: a record close 30.1% above its 200-day average, RSI 69.7, and a 1.53% FCF yield [Certain]. The reverse DCF needs 40.3% year-1 revenue growth and the mechanical bull fair value sits below the price [Certain]; any slowdown in incretin growth would de-rate a stock priced for compounding [Likely]. Concentration is high: Mounjaro, Zepbound and Foundayo were 66 percent of nine-month revenue [company-reported] [Certain], and U.S. realised prices are already falling, with voluntary pricing agreements, a Medicare bridge, IRA price-setting from 2028 and compounders in the MD&A [Certain]. Debt rose $7.0 billion this year [company-reported] [Certain]. The five-year FCF-margin decline is capacity build, not erosion: it reversed over the last 12 months (15.6% to 22.7%) [Certain], but continued plant spending caps cash conversion [Likely]. EV/EBITDA is more than double the peer median [Certain].
## Bull case
This is the best-performing large pharma franchise and it is still improving on a rolling basis: TTM ROIC 42.7% (from 38.3%), operating margin 51.3% (from 43.8%), FCF margin 22.7% (from 15.6%), all at or near 2-year highs [Certain]. Net debt/EBITDA is 0.96x and Altman Z 7.27 [Certain]. The pipeline widens the lead: the first GLP-1 pill approved in China, retatrutide capacity under construction and combination data at ObesityWeek [Likely]. Volume is offsetting price cuts [company-reported] [Likely]. On its own history the stock is not expensive: P/E 46.8x and P/FCF 65.4x sit at 4% of their 5-year ranges as earnings caught up with the price [Certain]. The trend is strong (+41.8% over 12 months, beating SPY by +31.4pp) with low beta 0.39 [Certain]. The mechanical fair value, built on history, cannot see a business growing this fast [Likely].
## Decision
```json
{
  "ticker": "LLY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Nothing is falling over 1 or 3 years; the 5-year FCF-margin dip came from FY2023's 2.3% on heavy manufacturing build, and FCF margin rose over the last 12 months from 15.6% to 22.7% with ROIC and operating margin at 2-year highs [CF-T, RA-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "U.S. incretin price erosion (voluntary pricing agreements, Medicare bridge, IRA selection, compounders; 10-Q 2026-09-30) slowing growth while the price sits at a record 30.1% above its 200-day average, inviting a de-rating.",
    "veto": null
  },
  "thesis": "The leading incretin franchise with rising returns and margins is working, but at a record price that already discounts sustained hyper-growth while U.S. pricing pressure builds.",
  "rationale": "Scorecard conviction 3: top-tier quality, improving direction and a strong trend score fully, but a narrow moat under medium U.S. pricing risk, with the price at a record implying 40.3% growth, leaves it short of the buy bar. Good but not compelling, so no position.",
  "price_at_decision": 1443.50,
  "price_date": "2026-11-13",
  "research_note": "research/LLY/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 45%, reversing the FY2025-to-TTM expansion and showing price cuts outpace volume.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 45}},
    {"text": "TTM ROIC falls below 35%, back under the FY2024 level of 35.5%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 35}},
    {"text": "TTM FCF margin falls below 15%, back to the level of a year earlier, showing capacity spending is outrunning cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Quarterly revenue in the 10-Q turns negative year on year as U.S. realised incretin price declines outpace volume growth."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1750, "basis": "Earnings keep compounding (operating margin 51.3% and rising [IS-T]) and P/E moves back toward its 5y median 55.7x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 1500, "basis": "P/E holds near the bottom of its 5y range (46.8x vs 44.9x min [RA]) as earnings grow, offset by U.S. price erosion in the 10-Q; well above the mechanical base 547.40, which history-based DCF cannot reconcile with 40.3% implied growth [IS,RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 979, "basis": "Pricing policy or slower incretin growth de-rates the stock toward its 6-month low 978.87 [HI], still above the mechanical base fair value 547.40 and near its bull 1,206.26 [fact-sheet fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: valuation already scores via trend strength, and a lower price would lose those points long before it reached a discount to the mechanical base 547.40. The score stays at 3 because of the U.S. pricing risk and the narrow moat, so only new evidence (pricing stabilising, or volume clearly outrunning price erosion in the 10-Q) would change the decision, not a lower price."
}
```

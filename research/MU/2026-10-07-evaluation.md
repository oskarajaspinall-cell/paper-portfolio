# Evaluation: Micron Technology, Inc. (MU) — 2026-10-07
## Bear case
Memory is a commodity cycle, and every TTM figure shows a cycle at its peak. Gross margin is 80.7% against 2.7% in FY2023, and ROIC is 93.4% against -7.4% [Certain]. A P/E of 14.1x is only cheap if peak earnings last. P/B of 8.5x and EV/Sales of 8.4x are above their 5-year maxima, so the market is already paying for durability [Certain]. Supply additions from the oligopoly and Chinese entrants (CXMT, YMTC) are the usual way these cycles end [Likely]. Headlines describe a "make-or-break year" as production rises, and investors appear to be selling into blowout results [Likely]. A beta of 2.23 and a +456.6% 52-week move leave no room for error [Certain]. Shares grew 1.60% YoY, so there is no net buyback support [Certain]. FCF conversion of 69.4% means capex is absorbing a lot of the profits [Certain].

## Bull case
AI/HBM demand may have reset the earnings base, and management points to an "even stronger fiscal 2027" [Likely]. The valuation is low on cash generation: FCF yield is 4.99%, P/FCF is 20.0x (bottom of its 5-year range) and EV/EBITDA is 10.2x, about 70% below peers [Certain]. The balance sheet is net cash (net debt/EBITDA -0.35x), with Altman Z of 9.72 and Piotroski F of 8 [Certain]. The industry is a three-player oligopoly, so pricing discipline is better than in earlier cycles [Likely]. The Netlist settlement removes a litigation overhang [Likely]. Short interest is low at 2.46% and falling [Certain]. If margins stay near current levels through FY2027, the stock is cheap [Guessing].

## Decision
```json
{
  "ticker": "MU",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "thesis": "Micron is a high-quality memory franchise at peak-cycle margins, so a low P/E on peak earnings combined with record P/B and EV/Sales gives no margin of safety over a 12-month core horizon.",
  "rationale": "Core needs a good business at an attractive valuation through the cycle. TTM gross margin of 80.7% and ROIC of 93.4% are far above any prior year, and P/B and EV/Sales are above their 5-year maxima. Mean reversion would make today's P/E optically cheap only. Net cash limits the downside to the business, but not to valuation. No position.",
  "price_at_decision": 1045.56,
  "price_date": "2026-10-06",
  "research_note": "research/MU/2026-10-07.md",
  "triggers": [
    {"text": "Gross margin rises further above the current 80.7% peak (above 82%), evidence the HBM-driven earnings base is structural rather than cyclical", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 82}},
    {"text": "FCF margin rises above 50% (from 44.3%), showing capex intensity falling while pricing holds, which would undercut the peak-cycle thesis", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 50}},
    {"text": "Share count turns to net shrinkage (shares change YoY below 0%), signalling management is returning peak cash rather than funding a supply build", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": 0}}
  ],
  "replaces": null,
  "replacement_reason": null
}
```

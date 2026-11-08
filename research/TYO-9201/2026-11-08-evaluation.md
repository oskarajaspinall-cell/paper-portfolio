# Evaluation: Japan Airlines Co., Ltd. (TYO:9201) — 2026-11-08
## Bear case
The recovery has peaked and the last year is rolling over: TTM operating margin 7.8% vs 9.3% a year earlier and 2.2pp below its 10.0% 2-year high, ROIC 9.8% vs 11.0%, ROCE 7.3% vs 8.4% [IS-T, RA-T] [Certain]. The Direction change is driven by costs (labour, fuel, yen) outpacing yield, since H1 profit fell while revenue rose (https://www.nasdaq.com/articles/japan-airlines-h1-profit-declines-revenue-117) [Likely]; that directly undermines any quality-compounder thesis. Earnings are not cheap: P/E 13.5x sits above its 5y median 11.9x [RA] on falling profits [Certain]. The low EV/EBITDA of 3.3x reflects heavy fleet depreciation and recurring capex, not mispricing [Likely]. The mechanical fair value is unusable (DCF bear -44,753.09) [Certain]. Altman Z 1.63 is weak, airlines are cyclical, and the stock sits near its 52-week high of 3,433.00 [HI] [Certain]. Amadeus data breach exposure adds minor reputational risk [Likely].
## Bull case
Balance sheet is net cash (net debt/EBITDA -0.97x TTM) and Piotroski F is 8 [RA, ST] [Certain]. Cash generation is holding while accounting profit slips: FCF margin 7.4% TTM vs 7.1% a year earlier, FCF conversion 145.9%, FCF yield 11.29% [CF-T, ST] [Certain]. EV/EBITDA 3.3x is near its 5y low of 3.1x and below the peer median 4.7x; P/B 0.9x vs a 5y median 1.2x and peers 1.9x [RA] [Certain]. Haneda slot constraints and the ANA duopoly give a moderate moat [Likely]. A reversion of EV/EBITDA toward its 5y median, as in the mechanical EV/EBITDA base of 4,436.85, would rerate the shares, and buybacks (shares -1.24% YoY) support per-share value [Likely]. Low beta (0.42) and a weak yen (157.47 per USD, macro overlay) help inbound travel demand [Guessing].
## Decision
```json
{
  "ticker": "TYO:9201",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A net-cash, post-recovery Japanese flag carrier that looks cheap on EV/EBITDA and P/B, but whose margins and returns are falling over the last year while the P/E sits above its own 5-year median, so the cheapness reflects a cyclical peak rather than mispricing.",
  "rationale": "Profits and returns are falling on a rolling basis while the stock trades near its 52-week high and above its median P/E; the low EV/EBITDA is capex-driven and the mechanical fair value is unreliable. Expected value is close to the price for a cyclical with weak Altman Z. Good balance sheet, not compelling: AVOID.",
  "price_at_decision": 3277.00,
  "price_date": "2026-11-06",
  "research_note": "research/TYO-9201/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above its 10.0% 2-year high, showing yields again outpace cost inflation and reversing the Direction change.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 10}},
    {"text": "TTM ROIC rises back above 12%, above the 11.9% 2-year high, evidencing returns are structurally higher than the cycle peak.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 12}},
    {"text": "TTM FCF margin falls below 4% (7.4% now), confirming cash generation is following profits down and the thesis against stays intact.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 4}},
    {"text": "Net debt / EBITDA on the ratios page rises above 1.0x (-0.97x TTM now), signalling fleet capex is consuming the net-cash buffer."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 4436.85, "basis": "EV/EBITDA reverts toward its 5y median 4.7x [RA] on TTM EBITDA, matching the mechanical EV/EBITDA base of 4,436.85 [fact sheet Fair value], as margins stabilise; the DCF-led blended base is ignored because the through-cycle DCF yields a negative bear."},
    "base": {"probability": 0.45, "target_price_12m": 3300.00, "basis": "P/E holds near 13.5x [RA] on roughly flat earnings as the operating-margin fall from 9.3% to 7.8% [IS-T] stabilises, close to the EV/EBITDA method's bear value of 3,197.81 [fact sheet Fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 2500.00, "basis": "Cost inflation keeps compressing margins (ROIC 11.0% to 9.8% [RA-T]) and P/E de-rates toward its 5y minimum 8.2x [RA], taking the price back toward the 52-week low of 2,406.50 [HI]; below the EV/EBITDA bear because falling EBITDA lowers the base the multiple applies to."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

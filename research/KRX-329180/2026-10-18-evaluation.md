# Evaluation: HD Hyundai Heavy Industries Co., Ltd. (KRX:329180) — 2026-10-18

## Bear case
This is a shipbuilder at peak-cycle earnings, not a compounder [Likely]. Gross margin was -2.6% in FY2021 and operating margin -9.7%; today's 19.1% and 14.1% rest on vessel prices, productivity and FX, all cyclical [Certain]. TTM EBITDA sits well above its 5-year median, so the low P/E of 13.7x and EV/EBITDA of 9.3x flatter a cyclical peak [Likely]. Against shipbuilding peers it is dearer on P/FCF (+123%), P/B (+32%) and P/E (+20%) [Certain]. Shares grew 10.65% YoY, diluting the per-share gain [Certain]. The mechanical bear fair value is 52,249.62 KRW, showing how badly a downturn can hit [Certain]. The price is down 30.7% over 12 months, 35.5% below its 200-day average, with RSI 25.2: the market is pricing a turn in the cycle, and Q3 results on Oct 30, 2026 could confirm it [Likely]. Chinese yards competing on price threaten the moat [Likely].

## Bull case
Returns have been transformed: ROIC 39.3%, ROE 30.1%, FCF margin 16.3% with FCF conversion of 141.7% [Certain]. The balance sheet is net cash (net debt/EBITDA -1.42x), Altman Z 3.00 and Piotroski F 7 [Certain], so the yard can survive a downturn. FCF yield is 9.66% [Certain]. The reverse DCF says the price already implies -5.8% revenue growth in year 1 [Certain], while Q2 2026 order intake nearly met the annual target, with a focus on high-value gas carriers [Likely]. Base fair value of 581,386.95 KRW is +65.4% above the close [Certain]. The macro overlay finds the dollar/KRW move a modest earnings tailwind that the sell-off does not credit [Likely]. Backlog-based revenue recognition gives visibility for several years of deliveries [Guessing].

## Decision
```json
{
  "ticker": "KRX:329180",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash Korean shipbuilder with transformed returns trades well below its mechanical base fair value, but its earnings are peak-cycle and the market is actively pricing a downturn ahead of Q3 results.",
  "rationale": "Quality and cash generation are real, but margins are cyclical and at a peak, the bear fair value is far below the price, peers are cheaper on P/FCF and P/B, dilution is high and momentum is collapsing into the Oct 30 results. Good but not compelling: conviction 3, no position; cash is acceptable.",
  "price_at_decision": 351500.0,
  "price_date": "2026-10-16",
  "research_note": "research/KRX-329180/2026-10-18.md",
  "triggers": [
    {"text": "TTM operating margin falls below 5%, back to the FY2024 level of 4.8%, confirming the upcycle has reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 5}},
    {"text": "TTM FCF margin turns negative, as in FY2022-23, confirming a cyclical downturn in cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Shares outstanding growth YoY rises above 15%, diluting per-share value faster than earnings grow.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 15}},
    {"text": "Positive trigger: Q3 2026 and Q4 2026 results show operating margin holding at or above the TTM 14.1% with order intake meeting the annual target, evidence that margins are durable rather than peak-cycle."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 581386.95, "basis": "Margins and order intake hold, so the price re-rates to the mechanical base fair value of 581,386.95 KRW [IS,BS,CF,RA,ST,HI]; probability nudged up by the macro overlay's small toward-bull tilt from dollar/KRW strength (research/KRX-329180/2026-10-18-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 394657.01, "basis": "Earnings normalise toward the 5-year average and the stock trades on the EV/EBITDA base leg of 394,657.01 KRW [IS,BS,CF,RA,ST], below the DCF-led blend because TTM EBITDA is peak-cycle (note section 2)."},
    "bear": {"probability": 0.3, "target_price_12m": 325171.84, "basis": "The cycle turns and Chinese price competition squeezes margins, putting the stock on the EV/EBITDA bear leg of 325,171.84 KRW [IS,BS,CF,RA,ST]; above the 52,249.62 KRW blended bear because the negative DCF bear ignores the net-cash balance sheet (net debt/EBITDA -1.42x [BS,IS])."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the base-fair-value-less-20% level is already above the price, and the open question is whether peak-cycle margins and order intake hold, which the Oct 30, 2026 results will show; a lower price alone would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

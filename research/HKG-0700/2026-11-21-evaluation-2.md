# Evaluation: Tencent Holdings Limited (HKG:0700) — 2026-11-21
## Bear case
The cash engine has stalled: TTM FCF margin fell from 28.5% to 3.6% and FCF conversion to 12.3% as AI capex surged [Certain]. P/FCF is 90.8x with a 1.10% FCF yield, so the stock is cheap on earnings only [Certain]. Q3 revenue growth slowed to 8% and non-IFRS operating profit fell, a miss per Reuters (fact-sheet headlines) [Likely]. US remote-access chip rules will delay model training, so the capex may earn less, later [Likely]. The trend is broken: price is 25.7% below its 200-day average, the 50-day sits below the 200-day and the 12-month change is -44.7% [Certain], so there are no trend-strength points and the de-rating can run further. The only working fair-value method is EV/Revenue (the DCF fails on a negative base cash-flow margin), a single, revenue-based estimate that cannot see the cash problem [Certain]. Piotroski F of 4 confirms deteriorating fundamentals [Certain].

## Bull case
This is a temporary, investment-driven cash dip, not a broken model: ROIC is 16.5% TTM, operating margin 32.2% is flat on the year and up from 22.1% in FY2021, and gross margin has risen to 56.6% [Certain]. Excluding new AI products, operating profit grew 8% per the Q3 transcript headline [Likely]. The balance sheet funds the build-out easily (net debt/EBITDA 0.25x, Altman Z 3.86) and shares fell 1.04% YoY [Certain]. WeChat's network effects are a durable moat [Likely]. P/E 11.5x and EV/EBITDA 9.1x sit below their own 5-year minimums and well below peers at 15.1x and 13.9x [Certain]; the mechanical base fair value is 557.55 HKD [Certain]. Management says cloud revenue is not substantially hurt by the chip rules [Likely]. If capex normalises and FCF recovers, the multiple has ample room [Guessing].

## Decision
```json
{
  "ticker": "HKG:0700",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only FCF margin is falling (28.5% to 3.6% TTM) while operating margin is flat at 32.2%; the cause is a step-up in AI infrastructure capex (SCMP, https://www.scmp.com/tech/big-tech/article/3374902/tencent-profit-dips-sixfold-increase-ai-infrastructure-spending-sacrifices-margin) funded by a net debt/EBITDA of 0.25x [BS,IS], i.e. heavy investment, not lost share.",
    "moat": "wide",
    "moat_text": "WeChat/Weixin social and payments network effects across games, ads, fintech and cloud.",
    "key_risk": "high",
    "key_risk_text": "The AI capex step-up fails to earn its cost of capital, made likelier by US chip rules delaying model training (Fortune, https://fortune.com/2026/11/20/tencent-alibaba-us-chip-curbs-cloud-ai/), leaving FCF depressed and the earnings multiple de-rating further.",
    "veto": null
  },
  "new_evidence": {"type": "price_move", "text": "The price fell to 344.00 HKD after Q3 2026 results on 2026-11-18, below the entry price set by the earlier AVOID."},
  "thesis": "A wide-moat platform with flat 32.2% operating margins trades below its own 5-year minimum P/E and EV/EBITDA, where the price assumes AI capex that has temporarily collapsed FCF never earns a return.",
  "rationale": "Scorecard conviction 4: high returns, a strong balance sheet and a deep earnings discount, against a high key risk that AI capex stays uneconomic. Sized by Python. Cash and the China/HK cap are full, so it replaces the overlapping China games holding.",
  "price_at_decision": 344.00,
  "price_date": "2026-11-20",
  "research_note": "research/HKG-0700/2026-11-21.md",
  "triggers": [
    {"text": "TTM operating margin falls below 28% (32.2% now), showing AI costs are eroding core profitability, not just cash flow.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "TTM ROIC falls below 12% (16.5% now), showing the build-out is diluting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin (cash-flow page, trailing) is still below 10% after two further quarterly reports, showing the capex is not converting to cash."},
    {"text": "Revenue growth stays below 8% YoY for two consecutive quarters (income statement), or a US rule cuts cloud revenue per a company release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 560, "basis": "FCF recovers as capex normalises and the multiple moves toward the mechanical base fair value of 557.55 HKD (EV/Revenue, fact sheet Fair value) with P/E back near its 5y minimum 14.8x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 420, "basis": "Operating margin holds near 32.2% [IS] but FCF stays weak, so the price recovers only toward the mechanical bear fair value of 423.59 HKD, below the base because revenue-based value ignores the 1.10% FCF yield [ST]."},
    "bear": {"probability": 0.30, "target_price_12m": 280, "basis": "Chip curbs delay AI returns (Fortune headline) and revenue growth stays below 8% (Reuters headline), so the P/E of 11.5x [RA] de-rates further on flat earnings, below the mechanical bear because the model cannot see the cash collapse."}
  },
  "replaces": "HKG:9999",
  "replacement_reason": "The buy would breach the cash floor and the China/HK cap; HKG:9999 is the overlapping exposure (same sector and country, China games), and Tencent adds ads, fintech and cloud on a deeper discount to its own 5-year multiples."
}
```

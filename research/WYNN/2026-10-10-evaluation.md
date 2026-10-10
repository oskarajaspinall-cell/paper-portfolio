# Evaluation: Wynn Resorts, Limited (WYNN) — 2026-10-10
## Bear case
This is a leveraged equity bet, not a cheap franchise. Net debt/EBITDA is 5.66x and Altman Z is 1.20 (distress zone) [Certain] [ST,RA]. The Q2-2026 10-Q shows a $906.7m stockholders' deficit and a 0.91 current ratio [Certain] (SEC 10-Q). At these levels equity is only about 4.2x of the 9.9x EV/EBITDA, so a small de-rating cuts the share price far more [Certain] [RA,ST]. On EV/EBITDA, P/E and P/FCF WYNN trades +19%, +28% and +42% above peers (LVS, MGM, MLCO, CZR) [Certain] [RA]. "Below own 5y minimum" reflects a pandemic-distorted history, not a bargain [Likely]. The Al Marjan budget rose by $600m [Certain] [OV transcript], and the $900m of 6.875% notes came as real yields rose +56bp and HY spreads +45bp over 3 months [Certain] (macro overlay). The price is down 38.2% over 12 months, 26.2% below its 200-day average, and short interest is 11.2% [Certain] [ST,HI].
## Bull case
The operating recovery is real. ROIC has gone from -2.1% (FY22) to 9.4% TTM, operating margin is 16.0%, and FCF conversion is 176% [Certain] [RA,IS,CF]. Q2 revenue grew, with strong EBITDA in Las Vegas, Boston and Macau [Certain] [OV transcript]. The 10.38% FCF yield funds buybacks (shares -3.24% YoY) and deleveraging [Certain] [ST]. The reverse DCF implies -8.6% year-1 revenue growth, which is harsher than the trend shows [Certain] [fair value]. Scarce Macau concessions and Strip assets are a durable moat [Likely]. Because the equity is leveraged, a re-rating of EV/EBITDA toward its 12.5x 5y median would lift the equity far more than the business value [Likely]. RSI of 25.5 shows the stock is oversold [Certain] [ST]. Al Marjan opening in 2027 adds a new growth leg [Guessing].
## Decision
```json
{
  "ticker": "WYNN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A recovering, cash-generative casino franchise whose equity is a thin, distress-zone sliver of enterprise value (5.66x net debt/EBITDA, negative book equity) and still trades at a premium to peers while financing conditions tighten.",
  "rationale": "The operating recovery and 10.38% FCF yield are real. But a negative-equity, Z-1.20 balance sheet, multiples above the peer median, a $600m Al Marjan budget increase and a macro overlay tilted toward bear make the risk-reward not compelling. The mechanical fair value is distorted by leverage. Below conviction 4, so AVOID.",
  "price_at_decision": 75.15,
  "price_date": "2026-10-09",
  "research_note": "research/WYNN/2026-10-10.md",
  "triggers": [
    {"text": "Leverage is worked down: Debt/EBITDA (statistics page) falls below 4.5x, from 5.66x net TTM, so the equity is no longer a distress-zone sliver.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 4.5}},
    {"text": "TTM FCF margin rises above 14%, back to the FY2024 level of 14.1%, showing cash generation is strong enough to fund Al Marjan and deleveraging together.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 14}},
    {"text": "A 10-Q shows the stockholders' deficit (-$906.7m at Q2-2026) eliminated, together with a current ratio back above 1.0.", "check": {"source": "statistics", "field": "currentRatio", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 121, "basis": "EV/EBITDA re-rates from 9.9x to its 5y median 12.5x [RA] with net debt held at 5.66x EBITDA [RA], which lifts equity per share by ~61%; this assumes real yields and spreads stabilise (macro overlay bull)."},
    "base": {"probability": 0.45, "target_price_12m": 80, "basis": "EV/EBITDA holds near 9.9x [RA] while the 10.38% FCF yield [ST] goes to deleveraging and buybacks (shares -3.24% YoY [ST]); this sits well below the mechanical base fair value of 256.98, which is inflated by the leverage gearing of the DCF (its bear is negative)."},
    "bear": {"probability": 0.35, "target_price_12m": 47, "basis": "EV/EBITDA compresses to the 8.3x peer median [RA] with net debt still 5.66x EBITDA [RA], cutting equity per share by ~38%; probability raised by a moderate toward-bear tilt from the macro overlay (research/WYNN/2026-10-10-macro.md: real yields +56bp, HY spreads +45bp over 3m)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: the balance sheet is (negative equity, Altman Z 1.20, 5.66x net debt/EBITDA [ST,RA]). The mechanical base fair value x 0.8 sits above the price and is unreliable under this leverage. A lower price would not change the decision until leverage falls.",
  "replaces": null,
  "replacement_reason": null
}
```

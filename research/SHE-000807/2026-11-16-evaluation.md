# Evaluation: Yunnan Aluminium Co., Ltd. (SHE:000807) — 2026-11-16
## Bear case
The cheapness comes from peak profits. TTM operating margin is 26.8% against 11.1% in FY2024, and ROIC is 59.1% against a 17.0% FY2023 trough [Certain] [IS-T, RA]. That jump is the aluminium price, not a better business. A commodity smelter has no pricing power [Likely]. The 6.0x P/E sits below its own 5-year low because the market expects margins to fall back [Likely]. On EV/EBITDA the mechanical fair value is 20.84, below today's price [Certain] [fact sheet]. The price is 19.3% below its 200-day average, with negative 6-month momentum, and nobody has verified why it fell. A weaker aluminium price or lower China demand would fit [Guessing]. The Q3 filing was not read [Certain]. China policy and power-cost risk sit outside the model [Likely]. The Direction change lines show a cyclical upswing, not a lasting gain in quality [Likely].
## Bull case
Even on through-cycle numbers the stock looks cheap. The normalised DCF gives a base of 35.22 and the blended base fair value is 30.43, against 23.04 [Certain] [fact sheet]. The reverse DCF already prices revenue falling 8.3% in year 1 [Certain]. The balance sheet is net cash (net debt/EBITDA -1.05x), with Altman Z 10.53 and Piotroski 8 [Certain] [ST]. FCF yield is 19.13% and FCF conversion is 114.2% [Certain] [ST, CF]. EV/EBITDA of 3.1x is a discount to the 4.4x peer median [Certain]. The 5-year fall in ROCE and operating margin turned into a sharp rise over the last 12 months. That rise is cyclical, but cash builds up while margins are high [Likely]. Beta of 0.69 and a stable CNY limit the macro risk [Certain] [macro overlay].
## Decision
```json
{
  "ticker": "SHE:000807",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Over the last 1 and 3 years ROIC, operating margin and FCF margin are all rising [RA-T, IS-T, CF-T]. The 5-year fiscal fall in ROCE and operating margin reversed in the last 12 months on the aluminium price.", "moat": "none", "key_risk": "medium", "key_risk_text": "Margins at twice their history fall back with the aluminium price and China demand, so earnings normalise and the low multiple turns out to be fair. The reverse DCF already prices part of this.", "veto": null},
  "thesis": "A net-cash Chinese aluminium producer trading below even its through-cycle fair value, but its earnings sit at a commodity peak and the cause of the recent fall is unverified.",
  "rationale": "The stock is cheap on normalised cash flow and the balance sheet is excellent. But TTM returns are a commodity-price peak, there is no moat, and the cause of the latest fall was not checked against the Q3 filing. The evidence matches the earlier AVOID, so the verdict and the conviction stay the same.",
  "price_at_decision": 23.04,
  "price_date": "2026-11-13",
  "research_note": "research/SHE-000807/2026-11-16.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 18%: the cycle has turned", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "Operating margin (TTM) falls below 14%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 14}},
    {"text": "FCF margin (TTM) falls below 12%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA (site definition) rises above 1.0x, i.e. the company moves from net cash to net debt"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 35.22, "basis": "Aluminium holds up and the price re-rates to the through-cycle DCF base of 35.22 [fact sheet fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 26.45, "basis": "Margins ease from the 26.8% TTM peak [IS-T], and the price only recovers to the mechanical bear fair value of 26.45, below the 30.43 base, because the blend still leans on peak-flattered cash flow."},
    "bear": {"probability": 0.30, "target_price_12m": 20.59, "basis": "Earnings normalise, the cheap P/E proves fair, and the price settles at the EV/EBITDA bear value of 20.59 [fact sheet fair value]."}
  },
  "entry_price": 21.22,
  "entry_basis": "The 52-week low of 21.22 [HI]. Base fair value 30.43 x 0.85 sits above today's price, so it can't serve. The obstacle is peak earnings more than price, and only a deeper discount to the EV/EBITDA value would offset it.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: APA Corporation (APA) — 2026-11-07
## Bear case
APA is a commodity price-taker with no durable moat [Likely]. ROIC swung from 43.8% in FY2023 to 14.0% in FY2025 and back to 23.0% TTM [RA], so today's 7.3x P/E sits on a TTM earnings level well above FY2024-25 [Certain]. The cheap EV/EBITDA of 2.9x [RA] is cheap on near-peak cash flow, which is how E&Ps usually look before a downturn [Likely]. The stock is up 106.0% in 12 months [ST], so the recovery is largely priced. North Sea volumes are in natural decline and Egypt net volumes fall as prices rise under the PSC [Certain] (sec.gov 10-Q). Decommissioning liabilities are a tail risk and the 10-Q dropped its dedicated risk factor [Guessing]. The reserve NAV is [data unavailable], so fair value rests on EV/EBITDA alone, with the bear value of 38.46 below the price and only modest upside to base 48.80 [Certain].
## Bull case
The balance sheet is the best it has been in five years: net debt/EBITDA fell from 1.67x in FY2021 to 0.53x TTM [BS,IS], and debt is down $4.2 billion since year-end 2021 [company-reported] (https://www.sec.gov/Archives/edgar/data/1841666/000184166626000071/apa-20260930.htm) [Certain]. A 13.91% FCF yield [ST] funds buybacks (shares down 2.69% YoY [ST]) and dividends [Certain]. Piotroski F of 8 and a beta of 0.28 [ST] point to solid fundamentals and low market correlation [Likely]. EV/EBITDA is 41% below the peer median and P/FCF 42% below [RA, peers] [Certain]. Suriname (GranMorgu), Alaska and Uruguay exploration offer optionality the multiple ignores [Guessing].
## Decision
```json
{
  "ticker": "APA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraged, cash-generative E&P trades cheaply against peers, but on near-cycle-high returns with no moat, so the discount mostly reflects commodity risk rather than mispricing.",
  "rationale": "Strong balance sheet and FCF yield, but returns track the oil price, TTM earnings are above FY2024-25 levels, the stock has already doubled and the mechanical bear value sits below the price with modest upside to base. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 44.63,
  "price_date": "2026-11-06",
  "research_note": "research/APA/2026-11-07.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, under the FY2024-25 levels of 14.4%/14.0%, showing returns have reset below cost of capital territory.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 10%, near the FY2023-24 lows (9.8%, 7.5%), meaning cash no longer funds buybacks and debt reduction.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Shares change YoY turns positive, ending the buyback-driven share shrinkage.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "Net debt/EBITDA on the ratios page rises above 1.5x (0.53x TTM now), reversing the deleveraging."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 52.86, "basis": "EV/EBITDA re-rates toward the bull fair value of 52.86 [IS,BS,RA] as TTM EBITDA holds and buybacks continue (shares -2.69% YoY [ST])."},
    "base": {"probability": 0.45, "target_price_12m": 48.8, "basis": "Mechanical base fair value of 48.80 on EV/EBITDA [RA] near its 5y median 3.2x, with no change since NAV is [data unavailable]."},
    "bear": {"probability": 0.35, "target_price_12m": 38.46, "basis": "Returns revert toward FY2024-25 ROIC of 14.4%/14.0% [RA] as commodity prices ease, giving the bear fair value of 38.46 on EV/EBITDA [IS,BS,RA]."}
  },
  "entry_price": 39.04,
  "entry_basis": "valuation file: base 48.80 x 0.8 (20% margin of safety), which would offset the commodity-cycle risk to earnings.",
  "replaces": null,
  "replacement_reason": null
}
```

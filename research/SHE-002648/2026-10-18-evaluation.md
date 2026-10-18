# Evaluation: Satellite Chemical Co.,Ltd. (SHE:002648) — 2026-10-18
## Bear case
This is a commodity petrochemical producer priced on what looks like near-peak earnings [Likely]. TTM gross margin of 27.8% and ROIC of 23.8% sit well above the FY2022-FY2025 range of 16.5%-23.5% and 9.6%-14.1%, close to the FY2021 peak [Certain] (IS, RA). In FY2022 gross margin fell from 31.7% to 16.5% in one year [Certain] (IS), so a P/E of 7.8x on TTM earnings likely overstates how cheap the stock is [Likely]. The mechanical bear fair value of 3.52 CNY and the EV/EBITDA base of 22.96 CNY, below the 24.90 close, show how much depends on margins holding [Certain] (fair value table). Results were due on Oct 17, 2026 and are not yet in the fact sheet [Certain] (ST). Six-month momentum is -11.7% [Certain] (HI). There is no company-reported spread or capacity data to show whether the cycle is turning [Certain] (note).
## Bull case
Cash generation has really improved. FCF margin rose from -1.4% to 23.6% TTM, and FCF/NI conversion has been above 116.7% in every year since FY2023 [Certain] (CF, IS). Net debt/EBITDA fell from 4.11x to 0.29x, Piotroski F-score is 8, and shares outstanding fell 1.81% YoY [Certain] (RA, ST). The stock trades below its own 5-year minimum on P/E, EV/EBITDA and P/FCF, and at roughly half the peer median EV/EBITDA and P/FCF, with a 16.30% FCF yield [Certain] (RA, peers). The reverse DCF implies a -14.1% year-1 revenue decline, and the DCF base is 59.37 CNY [Certain] (fair value table). Even FY2025's mid-cycle margins (gross 22.3%, FCF 15.1%) look cheap at this price [Likely]. Macro is context only [Certain] (macro overlay).
## Decision
```json
{
  "ticker": "SHE:002648",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraged, cash-generative Chinese petrochemical producer trades below its own 5-year multiple range, but on TTM margins near the FY2021 cycle peak, so the cheapness depends on spreads holding.",
  "rationale": "The balance sheet and cash conversion are strong and the multiples are low, but the earnings base is cyclical. TTM margins and ROIC are near the prior peak, the EV/EBITDA base sits below the price, and the October results are not yet visible. Good but not compelling, and it would add more China exposure. AVOID.",
  "price_at_decision": 24.90,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-002648/2026-10-18.md",
  "triggers": [
    {"text": "TTM gross margin falls below 16%, at or under the FY2022 trough of 16.5%, confirming the spread cycle has reset and removing the case.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 16}},
    {"text": "Net debt/EBITDA rises above 3x toward the FY2022 peak of 4.11x, signalling renewed over-investment or a spread collapse.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3}},
    {"text": "TTM ROIC falls below 10%, back near the FY2022 low of 9.6%, showing returns no longer clear the cost of capital through the cycle.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Full-year FY2026 results show gross margin holding at or above the TTM 27.8% with FCF margin above FY2025's 15.1%, which would show the TTM margins are structural rather than peak and could justify conviction 4."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 47.23, "basis": "TTM margins (gross 27.8%, FCF 23.6% [IS,CF]) prove durable and the price converges on the blended base fair value of 47.23 CNY [fair value table]."},
    "base": {"probability": 0.45, "target_price_12m": 26.65, "basis": "Margins drift back toward FY2025 levels (gross 22.3% [IS]) while low leverage and buybacks (shares -1.81% YoY [ST]) support the price near its 50-day average of 26.65 CNY [HI], between the EV/EBITDA base of 22.96 and the DCF base of 59.37, which extrapolates near-peak FCF."},
    "bear": {"probability": 0.30, "target_price_12m": 15.70, "basis": "A FY2022-type spread collapse (gross margin 31.7% to 16.5% [IS]) takes EBITDA lower, and the stock is valued at the EV/EBITDA bear of 15.70 CNY [fair value table], close to the 52-week low of 16.20 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below the mechanical base fair value and its own 5-year multiple floor. The open question is whether TTM margins near the FY2021 peak are sustainable, which the October results and FY2026 margins must answer. A lower price on the same evidence would not raise conviction.",
  "replaces": null,
  "replacement_reason": null
}
```

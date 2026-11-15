# Evaluation: EOG Resources, Inc. (EOG) — 2026-11-15
## Bear case
The recovery is a commodity call, not a better business [Likely]. TTM ROIC of 22.7% and operating margin of 35.5% are rebuilt on higher oil prices and record volumes, and the three-year change is still falling (ROIC -7.1pp, operating margin -6.2pp) [Certain]. The note itself calls FCF margin above 25% mid-cycle-plus, not a floor [Likely]. There is no discount: the mechanical base fair value of 154.15 sits below the 158.32 close, and EV/EBITDA of 5.3x has barely moved across its 5y range, so the price only holds if earnings stay near today's level [Certain]. The valuation case rests on trend strength: the stock is 13.7% above its 200-day average after a +45.6% year; an extended price risks a de-rating back toward the 127.30 six-month low if crude retreats and returns revert toward FY2025's 16.0% ROIC [Likely]. A CFO change lands in January [Certain].
## Bull case
EOG is a low-cost, near-net-cash producer that converts the cycle into shareholder cash [Likely]. Net debt/EBITDA is 0.16x, Piotroski 7, Altman Z 3.86 [Certain]. The last 12 months rose across the board (ROIC 17.6% to 22.7%, FCF margin 17.2% to 25.3%, a 2-year high) and Q3 delivered record production with guidance held and an 8% dividend rise [Certain]. FCF yield of 8.99%, P/FCF at 10% of its 5y range and P/E 21% below the peer median price a cash machine cheaply [Certain]. Shares fell 3.50% YoY under a $20 billion authorisation [company-reported], and disposals of Barnett and Woodford Oil Window concentrate capital on premium plays [Certain]. Relative strength of +35.2pp vs SPY over 12 months with a 0.27 beta shows a business that is working and diversifies the book [Certain].
## Decision
```json
{
  "ticker": "EOG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The three-year fall in ROIC and operating margin is normalisation from the FY2022-23 commodity peak with the balance sheet intact (net debt/EBITDA 0.16x [BS,IS]); the last 12 months rose (ROIC 17.6% to 22.7% [RA-T]) on record Q3 volumes and held guidance (https://www.reuters.com/business/energy/us-shale-producer-eog-resources-beats-third-quarter-profit-estimates-2026-11-05/).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "An oil-price retreat pulls returns back toward FY2025 levels (ROIC 16.0% [RA]) and de-rates a stock trading 13.7% above its 200-day average after a +45.6% year.",
    "veto": null
  },
  "thesis": "A low-cost, near-net-cash shale producer converting a cyclical earnings recovery into buybacks and dividends at an 8.99% FCF yield, but priced at its mechanical fair value with returns tied to commodity prices.",
  "rationale": "Quality, balance sheet and cash returns are strong and the trend is working, but the scorecard does not reach the buy bar: no discount to fair value and returns that follow oil prices. Good but not compelling; cash is acceptable.",
  "price_at_decision": 158.32,
  "price_date": "2026-11-13",
  "research_note": "research/EOG/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, under the FY2025 level of 16.0%, showing returns have lost the recovery.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 15%, under the FY2025 low of 15.2%, showing the cash step-up was price-driven and transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 28%, under the FY2025 level of 28.7%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "Net debt/EBITDA rises above 1.0x (0.16x TTM), showing capital returns or acquisitions are outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 175.0, "basis": "Record production and held guidance keep TTM EBITDA near current levels while EV/EBITDA moves to its 5y max of 5.5x [RA] and buybacks shrink the share count (shares -3.50% YoY [ST]), above the mechanical bull 155.69 because buybacks and the dividend rise are not in the model."},
    "base": {"probability": 0.5, "target_price_12m": 154.15, "basis": "EV/EBITDA holds near its 5y median of 5.3x [RA] on TTM EBITDA, matching the mechanical base fair value 154.15 [IS,BS,CF,RA,ST,HI]."},
    "bear": {"probability": 0.25, "target_price_12m": 127.3, "basis": "Crude retreats and returns revert toward FY2025 (ROIC 16.0%, operating margin 28.7% [RA,IS]), taking the price back to its six-month low of 127.30 [HI], below the mechanical bear 154.09 because that method assumes TTM EBITDA holds."}
  },
  "entry_price": 123.32,
  "entry_basis": "valuation file: base 154.15 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

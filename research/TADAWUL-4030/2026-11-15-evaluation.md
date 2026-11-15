# Evaluation: The National Shipping Company of Saudi Arabia (TADAWUL:4030) — 2026-11-15
## Bear case
The TTM numbers look like a charter-rate peak, not a new level: ROIC jumped to 37.1% from 7.4% a year earlier and operating margin to 37.7% from 20.9% [IS-T, RA-T] [Certain]; shipping rates are cyclical and Bahri shows no moat [Likely]. P/E 3.0x and EV/EBITDA 3.0x, below their 5y minimums [RA], are the market pricing a fall in earnings, the classic cyclical trap [Likely]. The mechanical base fair value of 19.86 SAR sits well below the 35.30 close, and the best method (NAV) is [data unavailable] [Certain]. Cash conversion is weak: FCF margin was -9.9% in FY2025 and 11.1% TTM is 15.0pp below its 2-year high (fleet capex) [CF-T] [Certain]. The trend points come from a price above its 200-day average; if rates roll over, that support would go and the shares would de-rate [Likely]. The cause of the jump is unverified since the Q3 release was not readable [Certain].

## Bull case
Profitability has risen for five years, not just one: ROIC went from 1.9% (FY2021) to 10.9% (FY2025) and operating margin from 7.9% to 26.3% [RA, IS] [Certain]. The 2024 VLCC purchase added fleet that is now earning [Likely]. The balance sheet improved: net debt/EBITDA 0.65x TTM against 2.18x in FY2025, Piotroski F 7, Altman Z 3.08 [ST] [Certain]. Even if earnings halve, P/E 3.0x and FCF yield 10.05% leave room [Likely]. The stock is in an uptrend, 6.1% above its 200-day average with a +12.6% 12-month change [ST] [Certain], and a 0.35 beta adds diversification [Certain]. The FCF dip is investment in ships, not lost share [Likely].

## Decision
```json
{
  "ticker": "TADAWUL:4030",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell over 3 years because of fleet capex (FCF conversion -95.1% FY2024, -42.3% FY2025 [CF]) while ROIC and operating margin rose; FCF margin is back to 11.1% TTM [CF-T].",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "TTM earnings are a tanker charter-rate peak; a rate normalisation would cut margins and ROIC sharply and de-rate an extended price, and the cause of the jump is unverified.",
    "veto": null
  },
  "thesis": "A low-leverage Saudi tanker owner on peak-cycle earnings: cheap on TTM multiples but with no moat and earnings likely to fall from a charter-rate high.",
  "rationale": "Multiples below their 5y minimums reflect peak earnings in a cyclical business with no moat; the cause of the TTM jump is unverified and the mechanical base fair value sits well below the price. Good balance sheet and an uptrend do not make it compelling, so no position.",
  "price_at_decision": 35.30,
  "price_date": "2026-11-12",
  "research_note": "research/TADAWUL-4030/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 25% (charter-rate upcycle fading)", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}},
    {"text": "TTM ROIC falls below 12%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA rises above 2.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "FCF margin turns negative again", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 45.00, "basis": "Rates stay high and P/E re-rates partly toward its 5y minimum of 8.9x [RA] on earnings well below TTM; the mechanical bull of 121.26 [fact sheet fair value] assumes TTM EBITDA persists and is not credible."},
    "base": {"probability": 0.45, "target_price_12m": 32.00, "basis": "Earnings ease from the TTM peak (operating margin back toward the FY2025 26.3% [IS]) and the low multiple holds, so the price drifts slightly lower; above the mechanical base of 19.86 because the 5y margin gains look partly durable."},
    "bear": {"probability": 0.30, "target_price_12m": 19.86, "basis": "Charter rates normalise and EV/EBITDA on lower EBITDA returns to the mechanical base fair value of 19.86 SAR [fact sheet fair value]."}
  },
  "entry_price": 15.89,
  "entry_basis": "valuation file: base 19.86 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

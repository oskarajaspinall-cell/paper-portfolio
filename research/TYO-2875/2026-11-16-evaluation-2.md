# Evaluation: Toyo Suisan Kaisha (TYO:2875) — 2026-11-16
## Bear case
The margin step-up is unexplained: operating margin went from 8.2% to 16.6% TTM in a packaged-food business, and the note could not verify whether pricing, mix or a cost/FX tailwind drove it [Certain]. If part of it is translation of overseas noodle profit at a weak yen (158.23 per USD), a stronger yen or input-cost inflation would reverse it; the overseas share is [data unavailable] [Guessing]. ROIC is 2.6pp below its 2-year high of 26.0%, so returns have plateaued [Certain]. Cash conversion is lumpy: FCF/NI fell to 61.7% in FY2026 [Certain]. The latest quarterly results (2026-11-03) were not read, so the evidence is thinner than usual [Certain]. The price is below its 200-day average with the 50-day under the 200-day, and it has lagged SPY over 12 months: no trend support [Certain]. The peer discount may reflect a lower-growth mix [Guessing].

## Bull case
A net-cash staple (net debt/EBITDA -2.23x, Altman Z 9.38) with ROIC of 23.4% TTM and ROCE and operating margin at their 2-year highs trades at P/E 14.3x, the 6th percentile of its own 5-year range, and 42% below the peer median [Certain]. P/FCF 16.3x is below its 5-year minimum and the FCF yield is 6.14% [Certain]. The last year is improving, not fading: FCF margin rose +5.4pp to 11.5% and operating margin +1.7pp on a rolling basis [Certain]. The reverse DCF implies only 0.8% year-1 revenue growth, undemanding for a business with rising margins [Likely]. Shares fell 2.66% YoY, so buybacks add per-share value [Certain]. Beta of 0.25 makes it a low-correlation diversifier [Certain]. Mechanical base fair value is 12,653.89 JPY, above the 10,655.00 close [Likely]. The Maruchan brand and distribution scale give durable shelf position [Likely].

## Decision
```json
{
  "ticker": "TYO:2875",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "On the rolling view ROIC is +0.7pp on a year ago and +5.9pp over 3 years; ROCE, operating margin and FCF margin are at 2-year highs [RA-T, IS-T, CF-T]. ROIC sitting 2.6pp below its 2024-12-31 high is a plateau, not a fall.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "The doubling of operating margin since FY2022 has no verified cause; if it rests on a weak-yen translation of overseas profit or a passing input-cost tailwind, margins and ROIC revert toward the FY2022-23 levels.",
    "veto": null
  },
  "thesis": "A net-cash, high-ROIC Japanese noodle and food franchise with margins and cash generation still rising on a rolling basis trades near the bottom of its own P/E range and below its 5-year P/FCF minimum, pricing near-zero growth.",
  "rationale": "Scorecard conviction 4: top-tier quality, a rising rolling trend, net cash and a low position in its own multiple range outweigh an unverified margin driver and no trend support. That risk argues for the standard core size only, which Python volatility-scales. Holdings stay under 15 and no cap is breached, so nothing is replaced.",
  "price_at_decision": 10655.00,
  "price_date": "2026-11-13",
  "research_note": "research/TYO-2875/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 18%, giving up much of the rise from 11.4% (FY2022) to 23.4%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "TTM operating margin falls below 14%, reversing the step-up toward the FY2024 level of 13.6%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 14}},
    {"text": "TTM FCF margin falls below 6%, back near the FY2022 level of 5.7%, showing the cash gains were transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "Net debt/EBITDA (debt minus cash and short-term investments, balance sheet / ratios page) turns positive from -2.23x TTM, i.e. net cash is spent without a matching rise in returns."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 14116.31, "basis": "Margins hold at the TTM 16.6% and the multiple returns toward its 5y median P/E of 17.1x [RA], matching the mechanical bull fair value 14,116.31 [IS,BS,CF,RA,ST]."},
    "base": {"probability": 0.5, "target_price_12m": 12653.89, "basis": "Margins plateau with ROIC around 23.4% and the P/E drifts up from the 6th percentile of its 5y range, in line with the mechanical base fair value 12,653.89 (DCF 67%, P/E 33%) [IS,BS,CF,RA,ST]."},
    "bear": {"probability": 0.25, "target_price_12m": 8249.82, "basis": "The unexplained margin gain partly reverses (a stronger yen from 158.23 per USD or input costs, macro overlay) and the DCF bear assumptions apply, the mechanical bear fair value 8,249.82 [IS,BS,CF,RA,ST]."}
  },
  "new_evidence": {"type": "method_change", "text": "The earlier AVOID 3 (2026-11-07) predates the scorecard (2026-11-09); conviction is now set by Python from the fundamentals, and this evaluation follows it."},
  "replaces": null,
  "replacement_reason": null
}
```

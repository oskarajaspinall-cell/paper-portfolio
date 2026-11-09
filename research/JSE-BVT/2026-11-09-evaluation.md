# Evaluation: The Bidvest Group (JSE:BVT) — 2026-11-09
## Bear case
Returns are adequate, not superior: ROIC of 11.5% TTM is flat-to-down over five years (-0.7pp) and ROE fell 2.5pp [Certain] (RA). For a ZAR reporter whose discount rate carries an owner-set 1.5% country premium, that is close to the cost of capital, so growth creates little value [Likely]. The headline cheapness leans on FCF: conversion of 152.9% of net income is far above its 5-year path and probably includes working-capital release, so the 11.16% FCF yield and 9.0x P/FCF overstate steady-state cash [Likely]. On earnings, P/E of 13.7x sits inside its narrow 13.1x–15.2x range and EV/EBITDA is in line with peers [Certain], leaving little rerating room. Gross margin fell 1.7pp, net debt/EBITDA of 2.33x is above FY2022's 2.01x, and Altman Z of 2.53 is in the grey zone [Certain]. Mechanical fair value is unavailable and the foreign revenue mix is unverified, so the evidence is thin [Certain].

## Bull case
FY2026 was a clean year: management cites all divisions contributing, strong cash conversion and lower leverage and costs [Likely] (transcript H2 2026, OV). The rolling-12-month table shows no deterioration: ROCE rose 1.8pp to 15.0%, operating margin is at its 2-year high of 9.3% and FCF margin rose 2.3pp to 7.2% [Certain] (RA-T, IS-T, CF-T). Leverage fell from 2.71x to 2.33x [Certain]. The stock is cheap against its own history on assets and cash: EV/EBITDA of 7.4x is below its 5-year minimum of 8.3x, P/B of 1.9x and P/FCF of 9.0x sit at the bottom of their ranges, and P/E is 12% below peers [Certain] (RA). The share count is not diluted (-0.11% YoY) and beta of 0.24 makes it a low-volatility compounder [Certain]. If hygiene and terminals investments keep delivering, a rerating toward the 5-year P/E median or above is plausible [Guessing].

## Decision
```json
{
  "ticker": "JSE:BVT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Rolling 12 months: ROIC +0.7pp, operating margin +0.4pp, FCF margin +2.3pp (RA-T, IS-T, CF-T); none of the scored metrics is falling over the last year.",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "FCF conversion of 152.9% reverts as working capital rebuilds, while ROIC near a ZAR cost of capital caps value creation; South African economic and rand exposure is unverified.",
    "veto": null
  },
  "thesis": "A steady, deleveraging South African services conglomerate that is cheap on cash and assets but only fairly priced on earnings, with returns close to its cost of capital.",
  "rationale": "Quality is solid but unexceptional, earnings multiples sit inside a narrow own-history range, the cash-based cheapness relies on an unrepeatable conversion spike, and no mechanical fair value exists. Scorecard conviction 2: AVOID; cash is acceptable.",
  "price_at_decision": 24778.0,
  "price_date": "2026-11-06",
  "research_note": "research/JSE-BVT/2026-11-09.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 10.0%, showing returns slipping under the cost of capital", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10.0}},
    {"text": "Operating margin (TTM) falls below 8.5%, breaking the narrow margin band", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8.5}},
    {"text": "Net debt/EBITDA rises above 3.0x, reversing the deleveraging", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}},
    {"text": "FCF conversion (FCF/net income, FY) falls below 80% in the FY2027 report"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 27490, "basis": "P/E rerates to its 5y high of 15.2x [RA] on TTM earnings as hygiene and terminals investments keep lifting ROCE (transcript H2 2026, OV)."},
    "base": {"probability": 0.5, "target_price_12m": 25320, "basis": "P/E returns to its 5y median of 14.0x [RA] on flat TTM earnings, consistent with flat ROIC and operating margin [RA, IS]."},
    "bear": {"probability": 0.25, "target_price_12m": 23690, "basis": "P/E slips to its 5y low of 13.1x [RA] as FCF conversion of 152.9% reverts [CF, IS] and the market looks through the cash spike."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

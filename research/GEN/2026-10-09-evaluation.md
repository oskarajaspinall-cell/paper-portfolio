# Evaluation: Gen Digital Inc. (GEN) — 2026-10-09
## Bear case
The balance sheet is the problem. Net debt/EBITDA is 3.17x and Altman Z is 1.42, in the distress zone [Certain] [BS,IS,ST]. Returns are getting weaker: ROIC fell from 20.5% to 14.4% and ROCE from 26.7% to 16.8% [Certain] [RA]. Gross margin is down 6.9pp to 78.0% as lower-margin Engine marketplace revenue grows [Certain] [IS]. The stock fell from its 31.65 high (2026-09-03) to a 20.34 low (2026-09-29), and neither the note nor the fact sheet explains why [Certain] [HI]. Until that drop is explained, a low multiple may be a value trap rather than a mispricing [Likely]. Short interest is 7.80% and rising (+1.5%), and shareholders voted down executive pay at the AGM [Certain] [ST,OV]. Macro: real yields are up +0.61pp in 3m, which squeezes a leveraged equity first (macro overlay) [Likely].

## Bull case
The price implies -2.6% revenue growth in year 1. Q1 FY27 delivered 11% bookings growth, and the FY27 guide was raised to 9-11% [Certain] [fact sheet Fair value; Q1 FY27 transcript]. The FCF yield is 11.38%, P/FCF is 8.8x and EV/EBITDA is 8.8x, in the 9th percentile of its 5-year range [Certain] [ST,RA]. Revenue is recurring auto-renewing subscriptions, with eleven straight quarters of paid-customer growth and 90% LifeLock retention [Likely] (transcript). Operating margin is 42.8% and still rising, and FCF conversion is 147% [Certain] [IS,CF]. The share count is shrinking 1.52% a year while debt is paid down [Certain] [ST]. Even the mechanical bear fair value (24.83) is above the last close [Certain] [fact sheet Fair value].

## Decision
```json
{
  "ticker": "GEN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cash-generative consumer-security subscription franchise trades at an 11.38% FCF yield and implies shrinking revenue against 9-11% guided growth, but leverage, falling returns and an unexplained September collapse leave the discount possibly deserved.",
  "rationale": "The valuation is compelling, but the evidence does not reach conviction 4. Leverage of 3.17x with a 1.42 Altman Z, ROIC and gross margin both trending down, and a September drop from 31.65 to 20.34 that the research does not explain together make this good but not compelling. Cash is the better outcome than a 7% position.",
  "price_at_decision": 22.75,
  "price_date": "2026-10-08",
  "research_note": "research/GEN/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin rises back above 80% (FY2025 level 80.3%), showing the Engine mix shift is not structurally eroding profitability.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 80}},
    {"text": "Net debt/EBITDA falls below 2.5x, removing the balance-sheet constraint that caps conviction.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 2.5}},
    {"text": "TTM ROIC rises above 16.8% (FY2023 level), reversing the five-year downtrend.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 16.8}},
    {"text": "Next earnings (Nov 5, 2026) confirm paid-customer growth for a twelfth straight quarter with the FY27 9-11% revenue guide held and the cause of the September de-rating identified as non-fundamental."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 42.0, "basis": "EV/EBITDA re-rates from 8.8x to its 5y median 13.8x [RA] with net debt held at 3.17x EBITDA [RA], consistent with the mechanical base fair value of 42.15 rather than the 97.48 DCF bull, which needs growth the leverage-constrained history does not support."},
    "base": {"probability": 0.45, "target_price_12m": 29.0, "basis": "Guided 9-11% growth (Q1 FY27 transcript) holds and P/FCF recovers only partway from 8.8x toward its 5y median 13.5x [RA]; this is below the mechanical base of 42.15 because the 3.17x leverage and 1.42 Altman Z [ST] cap the re-rating within 12 months."},
    "bear": {"probability": 0.30, "target_price_12m": 18.0, "basis": "The unexplained September de-rating proves fundamental and P/FCF falls to its 5y minimum 7.0x [RA], below the mechanical bear of 24.83; bear probability was raised by 0.05 from base for the small toward-bear macro tilt from rising real yields on a leveraged balance sheet (research/GEN/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: First Solar, Inc. (FSLR) — 2026-10-07
## Bear case
The cheap multiple prices peak, policy-dependent earnings. TTM gross margin of 44.0% and operating margin of 33.6% sit at or near five-year highs [Certain] (IS), and the profit pool leans on Section 45X credits and tariff protection, not on technology alone [Likely]. The fact sheet cannot split 45X from operating profit, so the "11.1x P/E" may overstate durable earnings [Likely]. A securities class action alleging false statements is live, and short interest of 10.35% rose 11.6% month-on-month [Certain] (ST). The stock is -22.9% over 3m and -39.6pp vs SPY over 12m, with Q3 results on Oct 29 able to reset guidance [Certain] (HI, OV). The macro overlay flags rising real yields (DFII10 2.95%) and widening HY spreads, which raise developer financing costs, putting orders and ASPs at risk [Likely] (2026-10-07-macro.md). FY2022's -10.7% operating margin shows how fast this business can swing [Certain] (IS).

## Bull case
FSLR is a net-cash (-0.64x net debt/EBITDA), high-return business trading below its own five-year floor: P/E 11.1x vs 14.6x minimum and EV/EBITDA 7.5x vs 10.1x minimum [Certain] (RA). Returns have stepped up for good: ROIC rose from 8.2% (FY21) to 20.6% TTM, and FCF margin turned from -7.3% (FY24) to 27.9% TTM [Certain] (RA, CF). That gives a 7.76% FCF yield with no dilution (+0.12% shares YoY) [Certain] (ST). CdTe sits outside crystalline-silicon duty regimes and its US output earns 45X credits, a structural edge over CSIQ/JKS [Likely] (note, sec.gov 10-Q). Altman Z of 6.65 and Piotroski F of 7 rule out distress [Certain] (ST). Elevated short interest could fuel a sharp re-rating if Q3 confirms margins [Guessing].

## Decision
```json
{
  "ticker": "FSLR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-ROIC module maker trades below its five-year P/E and EV/EBITDA floors, but those earnings rest on peak, policy-supported margins facing rising real rates, legal overhangs and a near-term earnings reset risk.",
  "rationale": "The valuation is attractive, but durable earnings are unproven: margins are at five-year highs and lean on 45X and tariffs, short interest is rising, a class action is live and the macro tilt is moderately bearish. That makes it good but not compelling, so conviction is 3 and the owner rule says AVOID. Cash is preferable until Q3 confirms margins.",
  "price_at_decision": 179.80,
  "price_date": "2026-10-06",
  "research_note": "research/FSLR/2026-10-07.md",
  "triggers": [
    {"text": "TTM gross margin falls below the FY2025 level of 40.6%, signalling the margin step-down the market is pricing has begun.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40.6}},
    {"text": "TTM ROIC falls below the FY2023 level of 19.0%, reversing the step-up in returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 19.0}},
    {"text": "TTM FCF margin falls below the FY2025 level of 22.7%, showing cash conversion fading as 45X monetization timing or pricing weakens.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 22.7}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 236.00, "basis": "Q3 confirms TTM margins (gross 44.0% [IS]) and P/E re-rates from 11.1x to its 5y minimum 14.6x [RA] on flat earnings (179.80 x 14.6/11.1); probability cut by 0.05 for the macro overlay's moderate bear tilt on rising real yields (2026-10-07-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 180.00, "basis": "Earnings hold near TTM and the multiple stays at 11.1x P/E [RA] while the policy, legal and real-rate overhangs (note section 6; macro overlay) persist, so the price stays flat."},
    "bear": {"probability": 0.30, "target_price_12m": 143.00, "basis": "Operating margin reverts from 33.6% TTM to the FY2023 level of 26.7% [IS] at an unchanged 11.1x P/E [RA] (179.80 x 26.7/33.6); probability raised by 0.05 per the macro overlay's moderate bear tilt (2026-10-07-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: DexCom, Inc. (DXCM) — 2026-10-09
## Bear case
The price already discounts the growth story. The reverse DCF implies 28.7% year-1 revenue growth [Certain] (fact sheet). Recent reported growth is well below that [Likely] (note/10-Q). The blended own-history fair value is $64.89 base, -23.1% vs the $84.41 close [Certain]. DXCM trades at a premium to peers on every multiple (P/E +31%, EV/EBITDA +41%, EV/Sales +88%) [Certain] (RA). Gross margin has fallen 8.5pp over five years to 62.5% TTM [Certain] (IS), which points to structural Libre competition and lower-margin Stelo mix [Likely]. Unquantified securities and G6/G7 product class actions add a tail risk [Certain] (10-Q). Beta is 1.48 with the 10y at 5.28%, and real yields are up 0.61pp over 3m, so the discount-rate headwind keeps building [Certain] (macro overlay). Q3 earnings on Oct 29 add binary risk [Certain] (ST).

## Bull case
This is an elite, compounding franchise. ROIC has risen to 44.5% from 18.5% (FY2021), the FCF margin is 28.3% and the balance sheet is net cash (-0.39x) [Certain] (RA/CF). Multiples are near five-year lows (P/E 33.3x vs a 31.0x minimum; P/FCF 22.7x is below its 24.0x minimum), and the FCF yield is 4.41% [Certain] (RA/ST). Buybacks shrank the share count 2.61% YoY [Certain] (ST). Q2 brought a beat and raised guidance [Likely] (Reuters 2026-07-30). CONNECT trial data and wider coverage, with CMS decisions expected by mid-2027, could widen the type-2 market [Guessing] (Wells Fargo transcript). Relative strength vs SPY is positive over 3m/6m/12m [Certain] (HI). The P/E method alone gives a $109.30 base value [Certain] (fair value).

## Decision
```json
{
  "ticker": "DXCM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, net-cash CGM duopolist whose price still implies 28.7% year-1 growth and sits 23% above its own-history base fair value, so quality is fully paid for.",
  "rationale": "Quality is excellent, but multiples near five-year lows mostly reflect maturing growth. The price still implies growth well above what is being delivered, at a peer premium, while gross margin erodes and litigation remains unquantified. Rising real yields hurt a beta-1.48 name. Good but not compelling: conviction 3, below the buy bar, so cash is preferred.",
  "price_at_decision": 84.41,
  "price_date": "2026-10-08",
  "research_note": "research/DXCM/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin recovers above 65% (back above the FY2022 64.7%), showing Libre/Stelo mix pressure was transitory rather than structural, which would raise conviction.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 65}},
    {"text": "TTM operating margin rises above 27%, extending the five-year expansion from 10.9% and showing operating leverage strong enough to justify the implied growth.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 27}},
    {"text": "TTM gross margin falls below 58%, confirming structural competitive erosion and reinforcing the AVOID.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 58}},
    {"text": "CMS issues a coverage decision broadening CGM reimbursement to non-insulin type 2 patients (expected by mid-2027 per the Wells Fargo conference transcript), materially lifting the growth runway."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 109.30, "basis": "Growth and margins keep compounding (ROIC 44.5%, FCF margin 28.3% [RA/CF]) and the stock re-rates to the P/E-method base fair value of 109.30 [fair value]; probability cut 0.05 for the macro overlay's small bear tilt from rising real yields (research/DXCM/2026-10-09-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 80.00, "basis": "Multiples stay near five-year lows (P/E 33.3x vs 31.0x min [RA]) and earnings growth plus 2.61% buybacks [ST] roughly offset mild de-rating toward the 64.89 blended fair value [fair value], which is DCF-heavy at a 5.28% risk-free rate and beta 1.48."},
    "bear": {"probability": 0.30, "target_price_12m": 64.89, "basis": "Delivered growth stays far below the 28.7% the reverse DCF implies and gross margin keeps eroding (-8.5pp in 5y [IS]), so the price converges to the blended own-history base fair value of 64.89 [fair value]; probability raised 0.05 for the macro overlay's bear tilt (research/DXCM/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

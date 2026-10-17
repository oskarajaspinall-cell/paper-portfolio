# Evaluation: Aritzia Inc. (TSX:ATZ) — 2026-10-17
## Bear case
The 2:1 target of 180.34 needs the stock to clear both the 164.04 swing high (2026-07-10) and the 174.52 52-week high (2026-06-15) inside eight weeks [HI] [Certain]. The evidence supports a run back to 174.52, which falls short of 2:1 against the 133.45 volatility stop [Certain]. The move is already extended: RSI 70.2, +14.5% above the 50-day, and the jump held at 109%, so much of the drift may already be in the price [Likely]. Valuation is a gap risk: EV/Sales 4.0x and P/B 11.3x sit above their 5-year maxima, the reverse DCF needs 29.1% year-1 growth, and mechanical base fair value is 71.43 [Certain]. Beta 1.73 with real yields up 43bp over 3 months adds multiple pressure (macro overlay) [Likely]. Short interest rose 22.3% month on month [Certain].
## Bull case
This is a genuine beat, not a pop: Q2 FY27 drove a +20.5% day on 3.5x volume, and management raised its FY27 revenue and gross-margin outlook on US demand (WSJ, Financial Post headlines [OV]) [Likely]. Fundamentals confirm it: TTM gross margin 46.9%, operating margin 16.5% and ROIC 25.2% are all at or above every fiscal year shown [IS, RA] [Certain]. Net debt/EBITDA is 0.78x and Altman Z 6.29, so there is no balance-sheet risk [Certain]. P/E of 30.1x sits at only 22% of its 5-year range, so earnings growth, not just multiple expansion, carries the price [Certain]. Post-earnings drift after a guidance raise often persists for weeks, and VIX at 16.46 supports risk appetite (macro overlay) [Likely].
## Decision
```json
{
  "ticker": "TSX:ATZ",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A real Q2 FY27 beat and guidance raise drove a held +20.5% reaction, but the evidence-supported target is the 174.52 prior high, which does not reach 2:1 against the ATR-based drift stop.",
  "rationale": "The drift setup is genuine, but the honest target is the 52-week high of 174.52. Only the mechanical minimum of 180.34 reaches 2:1, and it needs a fresh all-time high in eight weeks from an overbought RSI, at a stretched multiple, with a small bear macro tilt. A trade that is good but not compelling is an AVOID.",
  "price_at_decision": 149.08,
  "price_date": "2026-10-16",
  "research_note": "research/TSX-ATZ/2026-10-17.md",
  "exit_plan": {"target": 180.34, "stop": 133.45, "time_limit": "2026-12-11"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 195.0, "basis": "The raised FY27 outlook delivers the 29.1% year-1 growth the reverse DCF implies, and P/E re-rates toward its 5y median of 36.4x [RA] on higher earnings, above the mechanical bull fair value of 154.03 because that model's history includes the FY2024 trough margin of 6.8% [IS]."},
    "base": {"probability": 0.45, "target_price_12m": 155.0, "basis": "Earnings growth from record TTM margins (operating 16.5% [IS]) offsets a P/E drift from 30.1x toward the low end of its 24.7x-36.4x range [RA]; this sits well above the mechanical base fair value of 71.43, which extrapolates the weaker 3y/5y history rather than the current US-led growth."},
    "bear": {"probability": 0.30, "target_price_12m": 115.0, "basis": "Growth decelerates and EV/EBITDA falls from 18.4x to its 5y minimum of 15.1x [RA], back near the 114.90 September low [HI]; the bear weight is raised a small amount for the overlay's bear tilt (real yields up 43bp on a beta-1.73, above-range multiple, research/TSX-ATZ/2026-10-17-macro.md)."}
  },
  "entry_price": 147.14,
  "entry_basis": "Not base fair value x 0.8 (that is a core anchor, irrelevant to a drift trade): at or below 147.14, with the drift stop unchanged at 133.45 (reaction-day low 135 less 0.25 x ATR 6.186 [HI]), a run back to the 174.52 52-week high [HI] alone delivers 2:1, provided the reaction day is still held.",
  "replaces": null,
  "replacement_reason": null
}
```

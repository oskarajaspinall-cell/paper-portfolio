# Evaluation: CTF Services Limited (HKG:0659) — 2026-10-11
## Bear case
The 2:1 target of 10.51 HKD needs +17.9% in eight weeks from a 0.42-beta stock whose ATR is only 2.1% of price, roughly 8.5 ATRs away. [Certain] It also has to clear the 52-week high of 9.58, so overhead supply is not "clear" above that level. [Certain] The catalyst is modest: AOP +3% and net profit +11% read as a steady print, not a re-rating beat, and the transcript summary is third-party. [Likely] The stock is already stretched: RSI 77.6, P/B 1.0x above its 5y max of 0.8x, EV/Sales above its 5y max, EV/EBITDA 40% over peers, and the base fair value of 6.97 sits 21.9% below the close. [Certain] Holding 201% of the jump with 3.3% institutional ownership points to a thin-float squeeze that is prone to mean reversion rather than steady drift. [Guessing] The stop is 8.9% away, so the reward depends on an unusually large move. [Certain]
## Bull case
The reaction was real: +6.5% on 11.5x average volume, extended rather than faded nine sessions later. [Certain] Results improved the balance sheet: net debt/EBITDA fell to 0.28x from 1.17x in FY2025, and dividends went up. [Certain] ROE rose for five years to 6.3% and net margin to 9.5%. [Certain] P/E of 17.2x is at the 47th percentile of its own range and 27% below peers, so the earnings multiple is not crowded. [Certain] 3-month relative strength of +12.4pp vs SPY and a fresh 6-month high show momentum that could carry a retest of 9.58. [Likely] Low beta limits gap risk from the broad market. [Likely]
## Decision
```json
{
  "ticker": "HKG:0659",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A genuine post-results volume spike in a low-volatility HK conglomerate, but the ATR-based plan needs an outsized +17.9% move through the 9.58 52-week high from overbought levels within eight weeks.",
  "rationale": "The setup qualifies mechanically, but the trade's edge is weak. The 2:1 target is about 8.5 ATRs away and above the 52-week high, for a 0.42-beta stock with RSI 77.6 that already trades at a record P/B. A modest +3% AOP print does not support that much drift. Cash is the better outcome.",
  "price_at_decision": 8.92,
  "price_date": "2026-10-09",
  "research_note": "research/HKG-0659/2026-10-11.md",
  "exit_plan": {"target": 10.51, "stop": 8.12, "time_limit": "2026-12-04"},
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 11.4, "basis": "P/E re-rates to its 5y max of 22.1x [RA], still below the 23.5x peer median [RA], as ROE keeps rising (6.3% TTM [RA]); this sits between the base and bull fair values (6.97/13.07)."},
    "base": {"probability": 0.5, "target_price_12m": 7.6, "basis": "P/E reverts to its 5y median of 14.7x [RA] from 17.2x as the post-results spike (RSI 77.6 [ST]) fades; slightly above the 6.97 base fair value because ROE and net margin are rising [RA,IS]."},
    "bear": {"probability": 0.3, "target_price_12m": 6.6, "basis": "P/E falls to its 5y min of 12.7x [RA] as P/B (1.0x, above its 0.8x 5y max [RA]) mean-reverts; well above the 2.94 bear fair value because that DCF leans on volatile FCF, now [data unavailable] TTM [CF], while earnings are growing [IS]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

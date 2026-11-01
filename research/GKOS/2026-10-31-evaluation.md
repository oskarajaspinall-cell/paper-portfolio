# Evaluation: Glaukos Corporation (GKOS) — 2026-10-31
## Bear case
The 2:1 target is not supported by evidence. With the stop at 204.73 (reaction-day low 207.41 less a quarter ATR of 10.73), risk is 13.8% of the 237.60 close. The trade then needs a second leg to 303.50 within eight weeks, after a +33.6% day, with RSI at 82.6 and the price +37.1% above its 50-day average [Certain]. The note marks the target [Guessing]: no level above the 248.75 high anchors it. The valuation leaves no cushion: EV/Sales is 20.0x, 91% of its 5y range, against a peer median of 3.2x, and P/B is above its 5y max [Certain]. That makes a gap through the stop on any reimbursement news plausible. The iDose LCD scenarios flagged on the call are exactly that risk [Likely]. Short interest of 7.61% is rising, and the S&P 400 move on 11/4 could mark the top of flows rather than start them [Guessing].
## Bull case
This is a textbook beat-and-raise. Record Q3 sales were led by Epioxa and iDose, and FY26 and preliminary FY27 revenue guidance went well above consensus (https://stockanalysis.com/stocks/gkos/transcripts/718649-q3-2026/) [Likely]. The reaction was +33.6% on 6.1x volume, and 92% of the jump held into the next close, so the market is still digesting it rather than fading it [Certain]. There is no overhead supply: the price is at its 52-week high, with the last pre-gap swing high at 191.62 [Certain]. Fundamentals are inflecting: TTM gross margin is 81.1%, FCF margin has turned positive at 5.2%, and operating margin has improved to -9.0% [Certain]. The move from the S&P 600 to the S&P 400 at the open on 11/4 adds index demand [Likely]. Altman Z of 16.41 shows no balance-sheet stress despite net debt/EBITDA of 11.57x [Certain].
## Decision
```json
{
  "ticker": "GKOS",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A genuine beat-and-raise drift setup, but after a +33.6% gap to 20.0x EV/Sales the evidence cannot support a 2:1 target above a volatility stop 13.8% below the price.",
  "rationale": "The drift signal is real, but the trade's edge is not clear. Reaching the 2:1 target needs an unanchored second leg from an overbought (RSI 82.6), near-max-multiple level, and an iDose reimbursement headline could gap the price through a wide stop. Good but not compelling, so we hold cash.",
  "price_at_decision": 237.60,
  "price_date": "2026-10-30",
  "research_note": "research/GKOS/2026-10-31.md",
  "exit_plan": {"target": 303.50, "stop": 204.73, "time_limit": "2026-12-26"},
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 310, "basis": "Revenue compounds toward the raised preliminary FY27 guidance (transcript, https://stockanalysis.com/stocks/gkos/transcripts/718649-q3-2026/) while EV/Sales holds near today's 20.0x, inside its 5y max of 21.3x [RA]; no mechanical fair value is computable [Fair value section]."},
    "base": {"probability": 0.45, "target_price_12m": 240, "basis": "Guided growth is delivered but EV/Sales de-rates from 20.0x (91% of its 5y range) toward the middle of the range as growth is priced in [RA], leaving the price roughly flat."},
    "bear": {"probability": 0.25, "target_price_12m": 150, "basis": "An adverse iDose LCD outcome flagged on the Q3 call (https://stockanalysis.com/stocks/gkos/transcripts/718649-q3-2026/) sends EV/Sales back to its 5y median of 12.4x [RA] on similar revenue."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle that can be fixed by a lower level: no fair value is computable [Fair value section], and a fall toward the 207.41 reaction-day low would break the drift setup itself rather than make it a BUY; the obstacle is the unsupported 2:1 target and iDose reimbursement gap risk.",
  "replaces": null,
  "replacement_reason": null
}
```

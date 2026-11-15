# Evaluation: JFrog Ltd. (FROG) — 2026-11-15
## Bear case
The drift is already spent. The stock has gone past the reaction: it holds 148% of the 2026-11-06 jump and closed at its 52-week high, +19.7% over its 50-day and +53.9% over its 200-day average [Certain]. The volatility stop (87.02, the reaction-day low 89.317 less 0.25 × ATR) sits about 23% below the close, so 2:1 needs 166.77 inside 8 weeks, a second move bigger than the record earnings gap with no new results due in the window [Likely]. Valuation is a real gap risk: EV/Sales 20.8x is above its 5y maximum and 249% above peers, and the FCF yield is 1.47% [Certain]. Short interest is up 7.0% on the month, the share count rose 5.79% and GAAP operating margin is still negative at -6.8% [Certain]. Higher real yields (DFII10 2.86%, macro overlay, context only) put pressure on long-duration multiples [Likely].
## Bull case
This was a real beat, not noise. Q3 revenue grew 31% with cloud up 60%, and FY guidance rose to $680M-$682M, driven by AI-coding usage and security adoption (transcript headline [OV]; Business Wire release) [Likely]. Each item in the rolling-12-month table is improving: operating margin is up 11.0pp to -6.8%, FCF margin is up 4.3pp to 32.3% and ROCE is up 6.3pp [Certain]. Relative strength against SPY is +75.4pp over 6m, and RSI 61.7 is not stretched [Certain]. Upgrades to estimates after a guidance raise can drive drift for weeks [Guessing]. The balance sheet is not a risk (Altman Z 7.63) [Certain].
## Decision
```json
{
  "ticker": "FROG",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A genuine Q3 beat and guidance raise, but the price has already run past the reaction and the volatility stop is so wide that an honest 8-week target cannot reach 2:1.",
  "rationale": "The setup qualifies, but the ATR stop at 87.02 means 2:1 needs 166.77 within 8 weeks, with no results in the window and the stock already at its 52-week high and EV/Sales above its 5y maximum. The evidence does not support that target, so this is an AVOID. Cash is acceptable.",
  "price_at_decision": 113.60,
  "price_date": "2026-11-13",
  "research_note": "research/FROG/2026-11-15.md",
  "exit_plan": {"target": 166.77, "stop": 87.02, "time_limit": "2027-01-11"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 140, "basis": "Raised FY guidance and 60% cloud growth (transcript headline [OV]) keep FCF margin rising from 32.3% [CF-T], so the market holds P/FCF near today's 68.3x [RA] on higher FCF; this sits above the mechanical bull of 70.18 because the EV/Revenue history misses the margin step-up."},
    "base": {"probability": 0.45, "target_price_12m": 100, "basis": "P/FCF drifts back toward its 5y median 51.9x [RA] while FCF growth partly offsets it; this stays above the mechanical base 54.11 because the FCF margin of 32.3% [CF-T] and operating margin of -6.8% [IS-T] are well above the history the EV/Revenue method is built on."},
    "bear": {"probability": 0.30, "target_price_12m": 54.11, "basis": "Growth slows and EV/Sales falls from 20.8x back toward its 5y median 9.0x [RA], which is the mechanical EV/Revenue base fair value of 54.11 in the fact sheet."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

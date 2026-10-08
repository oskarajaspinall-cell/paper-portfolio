# Evaluation: Carnival Corporation Ltd. (CCL) — 2026-10-08
## Bear case
The 2:1 target (30.9275) sits above the 2026-08-05 swing high of 30.22 and only just below the 31.59 June high, so the trade needs to clear two resistance levels inside 8 weeks [Certain]. The honest first target, 30.22, gives under 2:1 against the 23.7613 volatility stop [Certain]. The stock is in a downtrend: price is 4.6% below the 200-day MA (27.42) and the 50-day MA is 8.2% below the 200-day, with -26.4pp relative strength vs SPY over 12 months [Certain]. At beta 2.38 with an Altman Z of 1.42 and 3.28x net debt/EBITDA, the macro overlay's rising real yields (+0.61pp ~3m) and widening HY spreads tilt toward bear [Likely]. The same-day automatic shelf filing is a supply overhang [Likely]. Short interest rose 30.9% month on month [Certain].
## Bull case
The beat looks real: +13.4% on 3.7x volume, a raised outlook, and the stock still holds 135% of the jump six sessions later. That is continuation, not a fade [Likely]. Fundamentals back it up. TTM ROIC is 11.6%, operating margin 15.9% and FCF margin 11.5%, all at five-year highs, and net debt/EBITDA has fallen from 4.55x to 3.28x [Certain]. Valuation leaves room to re-rate: P/E 11.5x and EV/EBITDA 8.1x sit below their 5-year minimums and 16%/14% below peers, so crowding is not a risk [Certain]. RSI 58.9 is not overbought [Certain]. Equity volatility is calm (VIX 15.01), so the drift may not be disrupted [Guessing].
## Decision
```json
{
  "ticker": "CCL",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A genuine earnings beat is still being digested, but the drift runs into a 200-day downtrend and layered resistance that cap the honest target below 2:1 against the volatility stop.",
  "rationale": "The setup is real, but the evidence-supported target is the 30.22 swing high. That gives about 1.7:1 against the 23.7613 ATR stop, below the 2:1 rule. Reaching 30.93 needs a break through the 200-day MA and 30.22 within 8 weeks, against a small macro bear tilt on a beta-2.38 levered name. Conviction 3 means AVOID; cash is acceptable.",
  "price_at_decision": 26.15,
  "price_date": "2026-10-07",
  "research_note": "research/CCL/2026-10-08.md",
  "exit_plan": {"target": 30.22, "stop": 23.7613, "time_limit": "2026-12-03"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 34.03, "basis": "Rising ROIC (11.6%) and FCF margin (11.5%) re-rate EV/EBITDA from 8.1x toward its 5y median 10.1x [RA,IS,CF], capped at a retest of the 52-week high of 34.03 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 27.74, "basis": "P/E moves only from 11.5x back to its 5y minimum of 12.2x [RA] on flat TTM earnings while the 200-day MA (27.42) [HI] caps the downtrend repair."},
    "bear": {"probability": 0.30, "target_price_12m": 21.45, "basis": "The macro overlay's small bear tilt (rising real yields and HY spreads; research/CCL/2026-10-08-macro.md) raised the bear probability: with beta 2.38, Altman Z 1.42 [ST] and a possible shelf draw, the stock retests its 52-week low of 21.45 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

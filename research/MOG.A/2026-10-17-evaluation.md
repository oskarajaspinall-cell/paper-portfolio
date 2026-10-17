# Evaluation: Moog Inc. (MOG.A) — 2026-10-17
## Bear case
The plan needs about five ATRs of gain in 34 days, into overhead supply. The 3-month peak of 448.85 is only about 2.4x the stop distance away, short of the 2.5x room rule [Certain]. The swing highs are falling, from 448.85 to 399.45 [HI], and relative strength over 3 months is -5.3pp [HI], so the pullback looks like distribution rather than a simple dip to the 50-day average [Likely]. Short interest rose 34.1% month on month [ST]. P/E 31.3x, EV/EBITDA 20.2x and P/B 5.3x all sit above their 5-year maximums [RA], and the reverse DCF prices 23.2% year-one growth, so a guide-down risk would hit a crowded multiple [Likely]. Swing lows at 349.71 and 354.21 [HI] sit close to the stop, so a retest could hit the stop before the trend resumes [Guessing].
## Bull case
The uptrend is real: the stock is up 77.3% over 12 months, the 50-day average is 9.7% above the 200-day and relative strength is +62.6pp over 12 months [ST,HI] [Certain]. Price is -3.6% below the 50-day average with RSI 45.7, so it has cooled off without breaking down [Certain]. Fundamentals support the move. Record Q3 FY2026 sales and EPS came with raised guidance (https://www.businesswire.com/news/home/20260731950193/en/Moog-Inc.-Achieves-Record-Third-Quarter-2026-Results-Through-Operational-Excellence-and-Raises-Full-Year-Guidance/) [Certain]. TTM ROIC is 13.6% and operating margin 12.0%, both rising, with FCF conversion back to 92.9% and net debt/EBITDA down to 1.71x [RA,IS,CF] [Certain]. Multiples remain below the peer medians of 35.6x P/E and 24.0x EV/EBITDA [RA,P] [Certain]. Earnings on Nov 20, 2026 fall after the time limit [Certain].
## Decision
```json
{
  "ticker": "MOG.A",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A valid pullback-in-uptrend on a fundamentally improving defense supplier, but the 2:1 target sits just under the 448.85 peak with lower swing highs in between, so the trade's edge is not clear enough.",
  "rationale": "The setup qualifies, but the room to the 3-month peak is about 2.4x the stop distance, below the 2.5x rule. The target needs roughly five ATRs in 34 days through falling swing highs, while short interest rises and multiples sit above their 5y max. The plan's reward:risk is only marginal. Conviction 3, so AVOID; cash is acceptable.",
  "price_at_decision": 368.60,
  "price_date": "2026-10-16",
  "research_note": "research/MOG.A/2026-10-17.md",
  "exit_plan": {"target": 434.35, "stop": 335.73, "time_limit": "2026-11-19"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 448.85, "basis": "Raised FY2026 guidance converts into continued margin gains (TTM operating margin 12.0% [IS]), and the multiples close part of the gap to the peer medians of 35.6x P/E and 24.0x EV/EBITDA [RA,P], so the stock retakes its 52-week high of 448.85 [HI]."},
    "base": {"probability": 0.5, "target_price_12m": 370, "basis": "Earnings growth roughly offsets some multiple compression from above the 5y max P/E of 30.7x [RA]. This sits far above the mechanical base fair value of 148.95 because that DCF capitalises a 5y FCF history depressed by the FY2023 -1.1% FCF margin [CF,IS], not the TTM 8.1%."},
    "bear": {"probability": 0.25, "target_price_12m": 260, "basis": "EV/EBITDA de-rates from 20.2x toward its 5y max of 15.5x [RA] if growth falls short of the 23.2% the reverse DCF implies. This is still above the mechanical bull fair value of 216.05, which we treat as too punitive given rising ROIC [RA]."}
  },
  "entry_price": 354.21,
  "entry_basis": "Retest of the 2026-10-08 swing low of 354.21 [HI] while the 50-day average stays above the 200-day. That would widen the room below the 448.85 peak past the 2.5x rule with a stop under the 349.71 swing low. Base fair value x 0.8 is not used because it is irrelevant to a tactical setup.",
  "replaces": null,
  "replacement_reason": null
}
```

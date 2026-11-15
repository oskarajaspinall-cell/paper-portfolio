# Evaluation: Procore Technologies, Inc. (PCOR) — 2026-11-15
## Bear case
The plan's reward:risk does not hold. The rule stop is 66.15 (reaction-day low 66.93 less 0.25 × ATR 3.127), so 2:1 needs 100.56 [Certain]. Nothing in the evidence supports that level: it is above the bull fair value of 94.77 and well above the 52-week high of 79.80, which is the only overhead reference [Certain]. The move is already stretched: price is +31.4% above its 50-day and +44.2% above its 200-day average, RSI 83.6, so much of the drift may be spent and a reversion toward the 50-day (59.08) would go through the stop [Likely]. Short interest of 14.10% adds gap risk both ways [Likely]. GAAP profit is still negative (net margin -2.3%), Piotroski F 3 [Certain]. Rising real yields (DFII10 2.86%) weigh on software multiples, context only [Likely].
## Bull case
The setup is genuine: +19.7% on 3.2x volume on 2026-11-04, with 116% of the jump held and a new high the next day [Certain]. The Q3 call summary describes accelerating organic growth and raised guidance, and a new buyback was authorised the same week [Likely]. Fundamentals are inflecting: TTM operating margin rose 10.4pp in a year to -1.2% and FCF margin reached 21.1% [Certain]. P/FCF of 37.0x is below its own 5-year minimum and EV/Sales sits at the bottom of its 5-year range, so the re-rating has room if margins keep expanding [Likely]. Relative strength vs SPY is +27.9pp over 3 months [Certain]. Upside to the base fair value of 86.38 is plausible within eight weeks [Guessing], but it is not enough to pay for an ATR-based stop this wide.
## Decision
```json
{
  "ticker": "PCOR",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A real post-earnings drift on an inflecting margin story, but the volatility stop is so far below an overbought price that no evidence-supported target reaches 2:1.",
  "rationale": "The drift setup is real, but the honest ceiling is the bull fair value 94.77, short of the 100.56 a 2:1 plan needs from a 66.15 stop. Price is far above its 50-day with RSI 83.6, so the edge looks largely priced. The owner's 2:1 tactical rule makes this an AVOID; no size.",
  "price_at_decision": 77.62,
  "price_date": "2026-11-13",
  "research_note": "research/PCOR/2026-11-15.md",
  "exit_plan": {"target": 94.77, "stop": 66.15, "time_limit": "2027-01-10"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 94.77, "basis": "Margin inflection continues (TTM operating margin up 10.4pp to -1.2% [IS-T], FCF margin 21.1% [CF-T]) and EV/Sales re-rates toward its 5y median 9.0x [RA], matching the bull fair value 94.77 (fact sheet Fair value)."},
    "base": {"probability": 0.45, "target_price_12m": 86.38, "basis": "Raised guidance on the Q3 call (https://stockanalysis.com/stocks/pcor/transcripts/719864-q3-2026/) supports the mechanical base fair value 86.38 on EV/Revenue (fact sheet Fair value)."},
    "bear": {"probability": 0.30, "target_price_12m": 59.08, "basis": "The overbought move (RSI 83.6 [ST], +31.4% above the 50-day [ST,HI]) fades back to the 50-day average 59.08 as rising real yields (macro overlay, DFII10 2.86%) weigh on software multiples."}
  }
}
```

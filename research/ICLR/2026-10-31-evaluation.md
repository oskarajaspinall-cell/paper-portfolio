# Evaluation: ICON Public Limited Company (ICLR) — 2026-10-31
## Bear case
The 2026-10-28 reaction (+17.0% on 4.5x volume) looks like a re-rating, not a beat still being digested: the Q3 call summary credits pass-throughs for the higher 2026 outlook, which lift sales but not profit, and no 2027 guidance was given [Likely]. The price is already extended: 22.9% above the 50-day MA, RSI 74.1, 91% of the jump held [Certain]. EV/EBITDA of 38.1x sits above its 5y maximum and 62% above peers, so any wobble risks a gap down [Certain]. Fundamentals are weakening: TTM operating margin 2.7% vs 12.7% in FY2024, ROIC 1.6%, net debt/EBITDA 5.55x, Altman Z 1.78 [Certain]. The base fair value of 199.43 sits below the price [Certain]. The 250 target needs a clean break above the 219.04 high within the drift window, and the note itself calls that support [Guessing].
## Bull case
Record net wins and improving margins in Q3 (call summary) are the leading indicator a CRO's revenue follows, so the market may keep repricing the recovery [Likely]. Momentum is strong: 6-month relative strength vs SPY +73.5pp and the stock is at its 52-week high with no overhead supply [Certain]. The cash story is better than earnings: FCF margin 12.2%, FCF yield 6.34%, P/FCF 15.8x near its 5y low and shares down 3.44% YoY [Certain]. The EV/Revenue fair value base of 243.47 sits near the target [Certain]. A stop at 193.23 below the reaction-day low of 195.8 gives a defined risk [Certain].
## Decision
```json
{
  "ticker": "ICLR",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A record-bookings Q3 sparked a post-earnings jump, but the drift edge is weak: the raise is pass-through-led, the stock is overbought and priced above its own EV/EBITDA history, and the 2:1 target needs a further break to new highs.",
  "rationale": "The setup qualifies mechanically, but the beat is low quality (pass-throughs, no 2027 guidance), RSI 74.1 and EV/EBITDA above its 5y max raise gap risk, and the 250 target is only marginally above the 2:1 minimum with no firm evidence behind it. Good but not compelling: AVOID, cash is acceptable.",
  "price_at_decision": 211.36,
  "price_date": "2026-10-30",
  "research_note": "research/ICLR/2026-10-31.md",
  "exit_plan": {"target": 250, "stop": 193.23, "time_limit": "2026-12-25"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 243.47, "basis": "Record net wins (Q3 call, /stocks/iclr/transcripts/714459-q3-2026/) convert and margins recover, valuing the stock at the EV/Revenue base fair value [IS,RA]; below the mechanical bull because a 2.7% TTM operating margin [IS] cannot yet justify the DCF bull."},
    "base": {"probability": 0.45, "target_price_12m": 199.43, "basis": "Pass-through-led growth with slow margin repair settles the stock at the blended base fair value [IS,BS,CF,RA,ST,HI], as EV/EBITDA above its 5y maximum [RA] eases."},
    "bear": {"probability": 0.3, "target_price_12m": 177.42, "basis": "Operating margin stays near 2.7% [IS] with net debt/EBITDA 5.55x [BS,IS], so the earnings jump fades to the DCF base value [IS,BS,CF,RA,ST]."}
  },
  "entry_price": 159.54,
  "entry_basis": "valuation file: base 199.43 x 0.8; at that level the same record-bookings evidence would come with a margin of safety against the weak margins and leverage.",
  "replaces": null,
  "replacement_reason": null
}
```

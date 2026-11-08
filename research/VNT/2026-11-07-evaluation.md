# Evaluation: Vontier Corporation (VNT) — 2026-11-07
## Bear case
The required 2:1 target of 49.03 sits above the 52-week high of 48.20 [HI], so the plan needs a new high just to break even on its own rules [Certain]. RSI(14) is 87.9 and the close is 27.2% above the 50-day average [ST,HI]: the stock is extremely extended, and gap-down risk on any market wobble is high with VIX at 28.18 (macro overlay) [Likely]. P/E of 17.2x is already above its 5y maximum of 14.1x [RA], and the price is above the mechanical bull fair value of 40.55 [Certain], so the rerating looks crowded [Likely]. The 50-day average is still below the 200-day [ST], so there is no established uptrend behind the drift [Certain]. The Q4 revenue outlook came in below consensus (note §1) [Likely]. The volatility stop is wide (8.1% below the close), which makes the reward:risk fragile [Certain].
## Bull case
The beat looks real: Q3 sales, margins and EPS beat guidance and full-year adjusted EPS guidance was raised, per the company release cited in the note [Likely]. The reaction was strong (+5.8% on 3.2x volume) and fully held, a textbook drift signature [Certain]. Relative strength against SPY is +24.0pp over 3 months [HI] [Certain]. Fundamentals are improving: operating margin rose to 19.8% TTM, ROCE to 19.8%, leverage fell to 2.35x and shares fell 5.69% YoY [IS,RA,ST] [Certain]. Peers trade far richer on EV/EBITDA (18.1x vs 10.2x) [RA,P] [Certain], and short interest of 9.17% could fuel a squeeze [Guessing].
## Decision
```json
{
  "ticker": "VNT",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A genuine Q3 beat and guidance raise triggered a post-earnings drift, but an extremely overbought stock already above its bull fair value cannot honestly reach the 2:1 target above its 52-week high.",
  "rationale": "The beat is real but the trade fails: the honest target is the 52-week high of 48.20, short of the 2:1 level of 49.03 against a volatility stop at 38.83. RSI of 87.9 and a P/E above its 5y maximum add gap risk. No position; cash is acceptable.",
  "price_at_decision": 42.23,
  "price_date": "2026-11-06",
  "research_note": "research/VNT/2026-11-07.md",
  "exit_plan": {"target": 48.20, "stop": 38.83, "time_limit": "2027-01-01"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 48.20, "basis": "Raised guidance and margin expansion (transcript, note §1) carry the stock back to its 52-week high of 48.20 [HI], helped by the wide discount to peers on EV/EBITDA (18.1x vs 10.2x) [RA,P]; above the mechanical bull value because that model ignores the guidance raise."},
    "base": {"probability": 0.5, "target_price_12m": 38.54, "basis": "The rerating fades back to the mechanical base fair value of 38.54 (DCF 67% + EV/EBITDA 33%) [IS,BS,CF,RA,ST,HI], as P/E above its 5y maximum of 14.1x [RA] normalises."},
    "bear": {"probability": 0.25, "target_price_12m": 27.88, "basis": "The weak Q4 revenue outlook (note §1) and a risk-off tape reverse the move to the EV/EBITDA bear value of 27.88 [RA], near the 52-week low of 27.25 [HI]; above the DCF bear of 15.25 because FCF margin has held steady near 14% [CF,IS]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

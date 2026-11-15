# Evaluation: IDEXX Laboratories, Inc. (IDXX) — 2026-11-15
## Bear case
The drift is real but already extended: the close of 704.23 sits +25.2% above the 50-day and +23.0% above the 200-day average with RSI 71.6 [Certain]. The volatility stop (reaction-day low 620.2 less 0.25 × ATR) is 612.12, so 2:1 needs about 890, above the 52-week high of 769.98 and the latest swing high of 713.74 [Certain]. Nothing in the evidence supports a break to new highs within 8 weeks; the note itself tags that path [Guessing]. Valuation is a crowding and gap risk: P/E 47.5x is +32% above peers, the reverse DCF implies 40.3% year-1 revenue growth, and short interest rose 22.0% on the month [Certain]. CoVet brings near-term margin dilution and vet visits are weak, per the Q3 call [Likely]. Rising real yields are a multiple headwind for a long-duration name (macro overlay, context only) [Likely].
## Bull case
The setup is textbook post-earnings drift: +21.9% on 3.9x volume on 2026-11-02, and the price still holds 127% of the jump nine sessions later [Certain]. The beat was operational, not accounting: Q3 organic revenue grew 10% and FY2026 revenue and EPS guidance were raised, with diagnostic use per visit offsetting weaker visits [Likely]. Fundamentals are improving on a rolling basis: TTM ROIC 47.0% vs 41.9% a year earlier, operating margin 32.5% at its 2-year high, FCF margin 28.0% [Certain]. The balance sheet is pristine (net debt/EBITDA 0.46x, Piotroski F 8, share count down 2.19%) [Certain]. P/FCF of 42.6x sits at the bottom of its own 5-year range [Certain], so the multiple is not stretched against its own history.
## Decision
```json
{
  "ticker": "IDXX",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A genuine Q3 beat-and-raise is driving post-earnings drift, but with the price already near its post-results high the volatility stop leaves a 2:1 target above the 52-week high that the evidence does not support.",
  "rationale": "The drift setup is valid and the business is strong, but the honest target is the 52-week high of 769.98, well short of the roughly 890 needed for 2:1 against the 612.12 ATR stop. A sub-2:1 trade fails the owner's tactical rule; the stop is not tightened to fit. AVOID; cash is acceptable.",
  "price_at_decision": 704.23,
  "price_date": "2026-11-13",
  "research_note": "research/IDXX/2026-11-15.md",
  "exit_plan": {"target": 890, "stop": 612.12, "time_limit": "2027-01-08"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 769.98, "basis": "Raised FY2026 guidance and rising TTM ROIC and FCF margin [RA-T] carry the stock back to its 52-week high of 769.98 [HI]."},
    "base": {"probability": 0.5, "target_price_12m": 736.37, "basis": "Price tracks the EV/Revenue base fair value of 736.37 (second method) [IS,RA,ST]; the DCF base of 185.94 is ignored because the fair value is flagged unreliable (methods disagree 4.0x)."},
    "bear": {"probability": 0.25, "target_price_12m": 508.39, "basis": "Weak vet visits and CoVet margin dilution (Q3 call transcript, https://stockanalysis.com/stocks/idxx/transcripts/723646-q3-2026/) de-rate the stock to the EV/Revenue bear value of 508.39, near the 2026-09-11 low of 500.61 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Lear Corporation (LEA) — 2026-11-09
## Bear case
Lear earns a thin spread on OEM volumes: operating margin 4.6% and gross margin 7.8% have been flat for five years, so OEMs, not Lear, hold pricing power [Certain]. Every multiple is below its 5-year minimum, but the whole peer group is cheap (EV/EBITDA only -6% vs peers), so this may be a sector de-rating, not a mispricing [Likely]. FY26 revenue guidance was cut for China and FX; Europe and Africa plus Asia are most of sales, the euro is weaker, and Chinese EV makers are pushing into export markets [Likely]. The USMCA non-extension starts rolling reviews over Mexico-sourced content [Certain]; tariff damage could show up in 2027 [Guessing]. The rolling FCF margin is 2.9% against a 3.6% 2-year high, and short interest rose +43.2% in a month [Certain]. The mechanical bear value of 31.11 shows how much operating leverage hangs on a small margin [Certain].
## Bull case
Returns are rising on a rolling basis: ROIC is 11.4% and ROCE 12.9%, both at their 2-year highs [Certain]. Q3 revenue and core operating earnings grew for a fourth straight quarter despite lower industry production, and core operating earnings guidance held [Likely]. FCF conversion of 119.9%, a 13.19% FCF yield and a -5.53% share count, with authorization raised to $1.5B, make buybacks at 9.7x P/E accretive [Certain]. Leverage is moderate at 1.54x net debt/EBITDA and Piotroski F is 7, so this is a cyclical discount with an intact balance sheet [Certain]. The reverse DCF prices a -8.4% revenue fall in year 1, which Q3 growth does not show [Likely]. The FCF-margin slip is small and in line with the guided China/FX revenue cut, not lost share [Likely]. A partial re-rating toward the 5-year median EV/EBITDA of 6.6x gives material upside [Likely].
## Decision
```json
{
  "ticker": "LEA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Rolling ROIC rose to 11.4% from 9.6% and ROCE to 12.9% from 11.1% [RA-T]; operating margin is flat and the FCF margin slip from 3.2% to 2.9% is flagged flat [CF-T], consistent with the guided China/FX revenue cut (Q3 2026 release), not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A global production downturn, Chinese competition or tariff/USMCA costs compress the thin operating margin below 4.0%, where operating leverage turns the cheap multiples into a value trap.",
    "veto": null
  },
  "thesis": "A cash-generative seating and E-Systems supplier with rising rolling returns and accretive buybacks trades below every 5-year minimum multiple, but its thin, OEM-dictated margin and only mid-level ROIC make it a cheap cyclical rather than a high-conviction compounder.",
  "rationale": "The cheapness is real and the balance sheet intact, but ROIC of 11.4% is only mid-level, the moat is narrow and the margin is thin against China, FX and USMCA risk. The scorecard gives conviction 3, below the buy bar, matching the 2026-11-08 verdict on the same evidence. Cash is an acceptable outcome.",
  "price_at_decision": 110.28,
  "price_date": "2026-11-06",
  "research_note": "research/LEA/2026-11-09.md",
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: valuation already scores its maximum and the base fair value less the margin of safety sits above the price. What holds conviction at 3 is the mid-level ROIC, narrow moat and margin risk, so a lower price would not change the decision; a sustained step-up in returns would.",
  "triggers": [
    {"text": "TTM ROIC rises above 15% (11.4% now), showing returns are moving to a high-quality level that would lift conviction.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 15}},
    {"text": "TTM operating margin falls below 4.0%, close to the FY2022 five-year low of 3.8%, showing OEM pricing or Chinese competition is compressing profitability structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 4.0}},
    {"text": "TTM FCF margin falls below 2.0% (2.9% now), showing cash generation can no longer fund the buybacks.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 2.0}},
    {"text": "Management cuts full-year core operating earnings guidance, a 10-Q discloses that tariffs or USMCA terms materially reduce gross profit, or net debt/EBITDA on the ratios page rises above 2.0x."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 190.86, "basis": "Core earnings growth continues and EV/EBITDA re-rates toward its 5y median 6.6x [RA]: the EV/EBITDA method's bull value of 190.86 [fact sheet Fair value], below the blended bull of 219.36 because the DCF is unstable on a thin margin."},
    "base": {"probability": 0.5, "target_price_12m": 140.0, "basis": "Rolling ROIC holds near 11.4% [RA-T] and buybacks continue, so EV/EBITDA recovers only partway from 4.6x toward its 6.6x median [RA]; set well below the mechanical base of 200.42 because the DCF and EV/EBITDA methods disagree and peers are also cheap at 4.9x."},
    "bear": {"probability": 0.25, "target_price_12m": 99.0, "basis": "A production downturn plus China/FX and USMCA pressure push margin toward the FY2022 low of 3.8% [IS] and the stock back to its 52-week low of 99.00 [HI]; not the mechanical bear of 31.11, whose negative DCF value reflects margin sensitivity rather than the 1.54x leverage [BS,IS]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

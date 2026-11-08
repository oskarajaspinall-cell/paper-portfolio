# Evaluation: Elisa Oyj (HEL:ELISA) — 2026-11-08
## Bear case
Returns are leaking fast. On a rolling basis ROIC fell from 15.5% to 12.6%, ROCE from 21.2% to 17.0% and operating margin from 22.3% to 20.0% in one year [RA-T, IS-T] [Certain]. These Direction change lines rule out a "stable utility" reading. The cause is mobile competition and a lower-margin mix that transformation savings no longer offset: Q3 revenue was flat and comparable EBITDA fell (Q3 2026 transcript) [Likely]. That hits the core of a return-on-capital thesis. FCF margin sits 2.2pp below its 2-year high [CF-T] [Certain]. Net debt/EBITDA rose from 1.75x to 2.14x [BS,IS], with no buyback (shares change 0.01%) [Certain]. Falling returns explain the de-rating below the 5y minimum multiples. It still trades at a premium to peers on EV/EBITDA, P/FCF and P/B [RA,P] [Certain]. The bear value of 29.12 is roughly as far below the price as the base is above it [Certain].
## Bull case
This is a three-player Finnish market with spectrum and scale moats, recurring service revenue and beta of 0.45 [ST] [Likely]. Cash conversion is strong: TTM FCF/NI is 112.4% and the FCF yield is 6.79% [CF,ST] [Certain]. Every multiple is below its own 5-year minimum: P/E 16.5x vs a 17.7x low, EV/EBITDA 9.4x vs 10.4x [RA] [Certain]. The reverse DCF implies only 1.1% year-one revenue growth, an undemanding bar [Likely]. Management kept FY guidance and expects mobile service revenue to recover as fixed-term contracts expire. Software and data-centre connectivity orders add growth (Q2/Q3 2026 transcripts) [Likely]. If margins stabilise, EV/EBITDA moving back toward 11.0x supports the mechanical EV/EBITDA value of 39.08 [Guessing]. Macro is context only: euro rates are stable and Estonia shares the euro (research/HEL-ELISA/2026-11-08-macro.md) [Likely].
## Decision
```json
{
  "ticker": "HEL:ELISA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, low-beta Finnish telecom trades below its own 5-year multiple floor, but rolling returns and margins are falling under mobile competition while it still carries a premium to peers, so the modest upside to fair value does not compensate for the deterioration.",
  "rationale": "The cheapness against its own history mostly reflects a real one-year fall in ROIC, ROCE and operating margin, plus higher leverage. Base upside is modest and the downside to the bear value is similar in size. Good but not compelling, so AVOID. It would become a BUY nearer the bear value, or once margins stabilise.",
  "price_at_decision": 34.00,
  "price_date": "2026-11-06",
  "research_note": "research/HEL-ELISA/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 22% (20.0% now, 22.3% a year earlier), showing that mobile pricing and transformation savings have restored profitability; this would raise conviction.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 22}},
    {"text": "TTM ROIC recovers above 15% (12.6% now, 15.5% a year earlier), showing the returns erosion was transitory; this would raise conviction.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 15}},
    {"text": "Net debt/EBITDA rises above 2.5x (2.14x now), which would confirm that leverage is building while returns fall and would lower conviction further.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "Management reports mobile service revenue growth returning in Q4 2026 results as fixed-term contracts expire, as guided on the Q2 2026 call."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 42.13, "basis": "Mobile service revenue recovers as guided (Q2 2026 transcript) and margins return toward the 22.5% 2-year high [IS-T], reaching the DCF bull value of 42.13 [fact sheet Fair value]; this is below the blended bull of 44.19 because falling ROIC argues against a full EV/EBITDA re-rating."},
    "base": {"probability": 0.5, "target_price_12m": 36.78, "basis": "Flat revenue with operating margin near the TTM 20.0% [IS-T] and the guidance kept (Q3 2026 transcript) gives the DCF base value of 36.78 [fact sheet Fair value]; this is below the blended base of 37.55 because the EV/EBITDA leg assumes a re-rating toward the 11.0x median [RA] that falling returns do not yet support."},
    "bear": {"probability": 0.3, "target_price_12m": 29.12, "basis": "Mobile competition keeps eroding margins, with ROCE already 5.2pp below its 2-year high [RA-T] and leverage rising to 2.14x [BS,IS]: the mechanical bear fair value of 29.12 [fact sheet Fair value]."}
  },
  "entry_price": 30.04,
  "entry_basis": "valuation file: base 37.55 x 0.8 (fact sheet Fair value [IS,BS,CF,RA,ST,HI]). At that price the stock sits close to the bear value of 29.12, so the downside left is small even with the deteriorating returns, which would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

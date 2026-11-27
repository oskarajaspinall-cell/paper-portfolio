# Evaluation: China Oilfield Services Limited (HKG:2883) — 2026-11-27
## Bear case
Returns are still sub-par: ROIC 8.8% TTM, below the 9.6% FY2025 high, and ROE 8.5%, under a cost of equity loaded with a 3.5% country premium [Certain]. The business is a cyclical, captive supplier to its controlling shareholder, so pricing and capex volumes are set by CNOOC group, with related-party and minority-shareholder risk [Likely]. The FCF margin rise to 11.5% (the Direction change line) is partly capex deferral against guidance; with vessel purchases planned, capex should catch up and the margin fall back toward its 3-year declining path [Likely]. 9M FX losses of CNY 720 million show earnings volatility outside operations [Likely]. The cause of the fall since 2026-10-26 is not identified; it may reflect weaker oil/offshore spending expectations the statements don't yet show [Guessing]. The price is below both its 50-day and 200-day averages, so there is no trend support [Certain]. The fair value is flagged unreliable [Certain].

## Bull case
Every multiple sits below its own 5-year minimum: P/E 6.9x vs a 13.8x low, EV/EBITDA 4.5x vs 5.8x, P/B 0.9x, and a 12.71% FCF yield [Certain]. The reverse DCF implies revenue falling 17.8% in year 1, against Q3 revenue growth of 3% and guidance of slight full-year growth [Likely]. Fundamentals are improving, not breaking: operating margin 12.4% TTM vs 11.3% a year earlier, net debt/EBITDA 0.66x from 2.00x in FY2022, Piotroski F 7, share count down 0.51% [Certain]. Q3 margins and day rates held steady and the macro overlay finds CNY and HKD stable, so the FX loss is company-specific rather than a currency trend [Likely]. Technology segments carried 55% of 2025 revenue and 72% of profit, a mix shift supporting returns [Likely]. No company announcement explains the fall, so it looks like de-rating, not a broken business [Guessing].

## Decision
```json
{
  "ticker": "HKG:2883",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin is down over 3 years but rose from 6.2% to 11.5% in the last 12 months [CF-T]; the dip reflects a cyclical trough and capex timing with leverage falling to 0.66x net debt/EBITDA [BS], not lost share (Q3 call: margins and day rates steady, https://stockanalysis.com/quote/hkg/2883/transcripts/739591-q3-2026/).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Dependence on CNOOC-group offshore capex: a cut in the parent's spending or related-party pricing would hit day rates and utilisation, and capex catch-up would pull FCF margin back down.",
    "veto": null
  },
  "new_evidence": {"type": "price_move", "text": "The price fell 15.1% since the 2026-10-25 AVOID at conviction 3 (dip radar), with no company announcement after the Q3 results."},
  "thesis": "A deleveraging offshore oilfield-services firm trades below its own 5-year minimum on every multiple, but sub-10% ROIC and captive dependence on its parent keep it short of a high-conviction buy.",
  "rationale": "The fall looks like de-rating, not a broken business, and the stock is very cheap, but ROIC of 8.8% gives no quality points, the price is below its 200-day average, and the fair value is unreliable. The scorecard gives 3; cheapness alone does not reach the buy bar, so AVOID.",
  "price_at_decision": 6.47,
  "price_date": "2026-11-26",
  "research_note": "research/HKG-2883/2026-11-27.md",
  "triggers": [
    {"text": "TTM operating margin falls below 9%, reversing the rise to 12.4% and showing day rates or utilisation breaking.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 9}},
    {"text": "TTM ROIC falls below 6%, back toward FY2022 levels.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 6}},
    {"text": "TTM FCF margin falls below 6%, back under the level of a year earlier.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "Net debt/EBITDA rises above 2.0x, reversing the deleveraging (vessel purchases debt-funded).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 11.74, "basis": "Steady margins and stable revenue re-rate the stock back to its 52-week high of 11.74 [HI], still below the mechanical bear fair value of 13.70, which is flagged unreliable."},
    "base": {"probability": 0.5, "target_price_12m": 8.03, "basis": "Earnings hold at the Q3 run-rate and the de-rating partly reverses to the recent swing-high zone around 8.03 [HI], still below the 5y-minimum P/E of 13.8x [RA]; the +235% base fair value is discounted as unreliable."},
    "bear": {"probability": 0.25, "target_price_12m": 5.5, "basis": "Capex catch-up pulls FCF margin back down and parent spending softens, so the P/E 6.9x [RA] stays compressed on lower earnings, below the 52-week low of 6.09 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: ROIC of 8.8% TTM [RA] is below the 10% quality bar, so the scorecard cannot reach 4 at any price; a lower price would not change the decision."
}
```

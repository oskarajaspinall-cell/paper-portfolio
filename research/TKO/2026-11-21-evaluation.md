# Evaluation: TKO Group Holdings (TKO) — 2026-11-21
## Bear case
Returns are still mediocre: ROIC TTM 9.2% and ROE 9.4% sit far below FY2022's 16.4% and 42.3% [RA] [Certain]. The 5-year fall reflects the WWE/IMG consolidation into a lower-margin mix (operating margin 47.7% to 23.9%), and the last-12-month rebound is a recovery from post-merger lows, not proof of a new level [Likely]. EV/EBITDA 21.0x and EV/Sales 6.8x sit above their own 5-year max [RA], so a slower WWE (down on fewer premium live events, [company-reported] per the note) or lumpy event calendars could de-rate the shares [Likely]. Buybacks (shares -24.48% YoY [ST]) are partly debt-funded via the new senior secured notes, Altman Z is 1.70, and short interest is 13.04% [ST] [Certain]. The price is below its 200-day average (-7.5%), so there is no trend support, and the cause of the fall since 2026-11-11 is unidentified [Certain].
## Bull case
The fall does not look results-driven: Q3 beat on earnings and FY revenue guidance was raised a second time (Deadline/TheFly headlines [OV]) [Likely]. Owned, scarce live-sports IP with long media-rights contracts (UFC–Skydance, WWE–Netflix/ESPN, per the 10-Q) is a durable advantage [Likely]. The last 12 months are rising on every flagged metric: ROIC 6.5% to 9.2%, operating margin 20.6% to 23.9%, FCF margin 20.3% to 31.1% [RA-T, IS-T, CF-T] [Certain]. FCF yield is 5.13% and P/FCF 19.5x sits below its peers' 36.3x [RA] [Certain]. Net debt/EBITDA has fallen from 4.35x to 2.40x over five years [RA] [Certain]. The reverse DCF implies only 7.9% year-1 revenue growth, below what the UFC deal is delivering [Likely].
## Decision
```json
{
  "ticker": "TKO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "The 3-year operating-margin fall reflects the WWE merger and IMG consolidation adding lower-margin events and hospitality, not lost share; the last 12 months are rising (operating margin 20.6% to 23.9% [IS-T], ROIC 6.5% to 9.2% [RA-T]) with UFC revenue up 60% in Q3 [company-reported] per the note's 10-Q.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "WWE slows and the event calendar stays lumpy while EV/EBITDA sits above its 5-year max, de-rating the shares as debt-funded buybacks lift leverage.", "veto": null},
  "thesis": "Scarce owned sports IP with recovering returns and a real FCF yield, but ROIC is still below 10% and the price has no trend support, so it is not a high-conviction buy.",
  "rationale": "The fall after a beat-and-raise quarter looks like an overreaction, but it does not remove the obstacle: ROIC TTM 9.2% is below the quality bar, the fair value is flagged unreliable and the shares are below their 200-day average. Good business, not compelling: AVOID.",
  "price_at_decision": 177.99,
  "price_date": "2026-11-20",
  "research_note": "research/TKO/2026-11-21.md",
  "triggers": [
    {"text": "ROIC TTM falls back below 6% (statistics page)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 6}},
    {"text": "FCF margin TTM falls below 20%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA rises above 3.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}},
    {"text": "UFC or WWE segment revenue declines year on year in two consecutive quarters (10-Q)"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 226.94, "basis": "UFC media-rights growth keeps FCF margin near its 2-year high of 33.5% [CF-T] and the shares regain the 52-week high of 226.94 [HI], close to the unreliable base fair value of 223.34."},
    "base": {"probability": 0.5, "target_price_12m": 195.0, "basis": "P/FCF holds near 19.5x [RA] as FCF grows with the raised FY guidance [OV]; set below the base fair value 223.34 because the methods disagree 4.9x and EV/EBITDA is already above its 5-year max."},
    "bear": {"probability": 0.25, "target_price_12m": 145.0, "basis": "WWE slowdown and debt-funded buybacks de-rate EV/EBITDA toward its 5-year min of 18.4x [RA] and below the 52-week low of 170.14 [HI]; above the mechanical bear 60.55, which rests on the merger-distorted EV/EBITDA method."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: ROIC TTM 9.2% sits below the quality bar, so a lower price would not lift the scorecard to 4; a re-look needs ROIC back above 10%.",
  "replaces": null,
  "replacement_reason": null
}
```

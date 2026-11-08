# Evaluation: DaVita Inc. (DVA) — 2026-11-08
## Bear case
The thesis rests on payer and state economics that DaVita does not control. HHS's Kidney Care National Plan recommends a charitable-activity review, an unresolved threat to the commercial mix that drives profit [Likely]. ACA exchange enrolment already fell after enhanced tax credits expired, hurting revenue per treatment (10-Q) [Certain]. The **Direction change** is real: TTM FCF margin of 9.1% is 4.4pp below its 2-year high of 13.6% and below a year ago, driven by higher technology spend and ACA mix pressure [Certain]. That threatens the thesis because the DCF leg (67% of the 380.01 base) sits on that falling FCF base. The EV/EBITDA leg gives only 205.51 [Certain]. Leverage of 4.51x is above FY2024's 4.19x while buybacks continue, and Altman Z is 1.68 [Certain]. Short interest of 14.67% is rising [Certain]. P/E of 14.1x is above its 5y max [Certain].

## Bull case
Dialysis demand is chronic and non-discretionary, and DaVita has scale in a two-player oligopoly [Likely]. Q3 beat: adjusted EPS of $3.82, the low end of FY26 guidance raised, census-led volume growth, and management guiding tech-spend growth lower [Likely]. TTM ROIC (12.2%) and ROCE (14.4%) are up on a year earlier and operating margin is steady at 15.2% [Certain]. The FCF yield is 10.74% and P/FCF of 9.3x is far below the peer median of 17.0x [Certain]. The reverse DCF implies -8.4% year-1 revenue growth, so a policy hit is already largely priced [Certain]. Buybacks cut shares 14.08% in a year, compounding per-share value [Certain]. If the HHS review stalls, the stock could re-rate toward the bear fair value of 249.50 or above [Guessing].

## Decision
```json
{
  "ticker": "DVA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cash-generative dialysis oligopolist on a low cash multiple, but its profits depend on commercial mix that a pending HHS charitable-assistance review and ACA enrolment losses directly threaten, while FCF margin is falling.",
  "rationale": "Cheap on FCF, with steady returns and a Q3 beat, but the binding risk is regulatory and unresolved. FCF margin is falling, leverage is high, and the EV/EBITDA leg shows limited upside. The evidence has not improved enough since the last review to justify conviction 4, so it stays an AVOID at 3.",
  "price_at_decision": 191.35,
  "price_date": "2026-11-06",
  "research_note": "research/DVA/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 13.5% (reimbursement or mix squeeze)", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 13.5}},
    {"text": "TTM FCF margin falls below 7% (cash conversion deteriorating further)", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 7}},
    {"text": "Net debt / EBITDA rises above 5.0x (buybacks outrunning EBITDA)", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 5.0}},
    {"text": "Text: a final federal rule or law restricting charitable premium assistance, or a 10-Q showing exchange enrolment losses cutting revenue per treatment further; conversely, the HHS review being dropped would prompt a re-research for an upgrade."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 249.5, "basis": "The HHS charitable-activity review stalls and tech spend decelerates as guided (10-Q), lifting the stock to the mechanical bear fair value of 249.50 [IS,BS,CF,RA,ST,HI], near its 52-week high of 247.49 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 205.51, "basis": "Policy overhang persists and FCF margin stays near 9.1% [CF-T,IS-T], so value tracks the EV/EBITDA leg of 205.51 [RA,IS] rather than the FCF-driven DCF leg."},
    "bear": {"probability": 0.3, "target_price_12m": 145.95, "basis": "A charitable-assistance restriction or deeper ACA mix loss (10-Q; HHS plan headline [OV]) cuts EBITDA at 4.51x leverage [BS,IS], taking value to the EV/EBITDA bear of 145.95 [RA]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already screens cheap on FCF (P/FCF 9.3x) and the reverse DCF prices a revenue decline. The obstacle is the unresolved HHS charitable-activity review and the falling FCF margin, so a lower price on the same evidence would not justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Paychex, Inc. (PAYX) — 2026-10-09
## Bear case
The core is slowing while the balance sheet has lost its cushion. Management flagged Management Solutions trending toward the low end of guidance on the Q1 FY27 call, and the stock fell ~8% on the print [Certain]. ROIC has fallen from 55.7% (FY2023) to 27.4% TTM and net debt/EBITDA went from net cash to 1.20x after the debt-funded Paycor deal [Certain]. The low multiple is not the gift it looks like: the reverse DCF already implies 7.7% year-1 revenue growth, above the guided range, and the blended fair-value base of 109.72 is only 5.0% above the 104.46 close [Certain]. A payroll franchise tied to small-business hiring, with Paycor integration risk and float income exposed to any rate cuts, can de-rate further toward the 82.87 bear value [Likely]. Short interest of 6.20% shows sceptics are positioned for that [Likely].

## Bull case
This is a 74.4% gross-margin, 39.9% operating-margin, 30.5% FCF-margin franchise with 47.1% ROE and FCF conversion of 111.7% [Certain]. P/E 20.7x and EV/EBITDA 13.3x sit at the 7th percentile of their own 5-year ranges and 25-29% below peer medians [Certain]. Payroll-tax compliance makes switching painful, so retention should hold [Likely]. Q1 FY27 still delivered double-digit EPS growth, with PEO and Insurance growing [Certain]. The macro overlay notes that the recent fed-funds rise came after the guidance, which gives a modest boost to float income [Likely]. If Paycor cross-selling lifts growth, the P/E could move back toward its 25.6x five-year median [Guessing].

## Decision
```json
{
  "ticker": "PAYX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-margin payroll franchise trades near the bottom of its own 5-year multiple range, but slowing core growth, rising leverage and a reverse DCF already above guided growth leave too little mispricing to own.",
  "rationale": "Quality is real, but the fair-value base is only 5.0% above the price. The reverse DCF (7.7%) already prices more growth than the guide delivers, while ROIC and leverage are moving the wrong way after Paycor. Good but not compelling, so conviction is 3 and the decision is AVOID. Cash is acceptable.",
  "price_at_decision": 104.46,
  "price_date": "2026-10-08",
  "research_note": "research/PAYX/2026-10-09.md",
  "triggers": [
    {
      "text": "TTM operating margin rises above the FY2025 five-year peak of 41.8%, showing Paycor synergies are lifting combined economics rather than diluting them.",
      "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 41.8}
    },
    {
      "text": "TTM ROIC falls below 20%, confirming that returns on the post-Paycor capital base are deteriorating, not just changing mix (this would rule out any re-look).",
      "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}
    },
    {
      "text": "Management Solutions segment revenue growth (10-Q segment note) reaccelerates to the top of the FY27 guided range for two consecutive quarters, showing the core payroll slowdown was cyclical, not structural."
    }
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 129.24, "basis": "Paycor cross-sell and float income from higher rates (macro overlay research/PAYX/2026-10-09-macro.md, small tilt toward bull that moved 0.05 probability from bear to bull) re-rate P/E toward its 25.6x 5y median [RA], taking the price back to the 52-week high [HI], below the 142.46 fair-value bull because guided growth limits the full re-rating."},
    "base": {"probability": 0.50, "target_price_12m": 109.72, "basis": "Growth tracks the guide with Management Solutions at the low end (research note, TheFly Q1 call URL), so the price converges on the blended DCF/EV-Revenue fair-value base [IS,BS,CF,RA,ST]."},
    "bear": {"probability": 0.25, "target_price_12m": 82.87, "basis": "Core payroll deceleration plus Paycor leverage (net debt/EBITDA 1.20x [RA]) and rate cuts eroding float income push the price to the fair-value bear case [IS,BS,CF,RA,ST]; probability trimmed by 0.05 for the macro overlay's small bull tilt."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

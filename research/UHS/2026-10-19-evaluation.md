# Evaluation: Universal Health Services, Inc. (UHS) — 2026-10-19
## Bear case
The low P/E is not a cash yield: TTM FCF conversion is 55.4% and FCF margin 4.7%, so on P/FCF (12.9x) UHS is above the peer median (11.8x), not cheap [Certain]. The multiple sits below its 5-year minimum because the payor regime is changing: UHS cut FY2026 guidance on Medicaid supplemental-payment changes, and the 10-Q newly names OBBBA work requirements and provider-fee caps as specific risks [Certain]. Those caps hit the supplemental payments that lift current margins, so TTM earnings may be near a peak [Likely]. Event risk is stacked: the Cumberland jury verdict, the DC Attorney General review that could force an unwind, debt-funded Talkspace (approximately $835m [company-reported]) and Q3 results on Oct 27, 2026 [Certain]. The DCF bear value of 26.22 shows how thin FCF leaves the mechanical case [Certain]. The stock is up 20.6% in three months, so much of the rerating may be gone [Likely].

## Bull case
Quality is improving: ROIC 10.6%→12.4%, ROE 15.7%→20.9%, gross margin up 3.9pp over five years [Certain]. At 7.5x P/E and 5.9x EV/EBITDA, UHS trades below its own 5-year minimum and well below HCA/CYH/THC/ACHC [Certain]. The reverse DCF implies only 3.7% year-1 revenue growth [Certain]. Shares fell 6.69% YoY while net debt/EBITDA fell to 1.90x, so buybacks are not straining the balance sheet [Certain]. Certificate-of-need rules and the largest US behavioral network give a durable local moat [Likely]. Base fair value 218.79 sits above the 185.10 close, and the EV/EBITDA method alone gives 242.19 [Certain]. If the Q3 print shows the Medicaid hit is contained, the multiple can drift back toward its 5-year median 7.5x EV/EBITDA [Guessing].

## Decision
```json
{
  "ticker": "UHS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A rising-ROIC hospital and behavioral-health operator trades below its own 5-year minimum earnings multiples, but weak cash conversion and a live Medicaid/OBBBA reimbursement reset make the discount look deserved rather than mispriced.",
  "rationale": "Cheap on earnings, not on cash: P/FCF is above the peer median and FCF conversion is volatile. Base fair value upside is modest, policy risk to supplemental payments is specific and dated, and litigation, the DC review and Q3 results are imminent. Good but not compelling: conviction 3, no position.",
  "price_at_decision": 185.10,
  "price_date": "2026-10-16",
  "research_note": "research/UHS/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROIC falls below 9%, reversing the five-year rise to 12.4% and showing reimbursement cuts are eroding returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "TTM operating margin falls below 9%, showing Medicaid/OBBBA cuts are overwhelming cost control.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 9}},
    {"text": "Net debt/EBITDA rises above 3.0x (1.90x TTM now), showing Talkspace and capex are eroding balance-sheet discipline.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}},
    {"text": "TTM FCF margin falls below 2%, back to the FY2022 level, showing earnings are not converting to cash.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 242, "basis": "Q3 shows the Medicaid supplemental hit contained and EV/EBITDA returns to its 5y median 7.5x [RA], matching the EV/EBITDA base value of 242.19 in the fact-sheet fair value."},
    "base": {"probability": 0.5, "target_price_12m": 195, "basis": "Multiples stay below their 5y minimum (P/E 9.2x [RA]) while OBBBA provider-fee risk is unresolved; per-share earnings grow modestly on buybacks (shares -6.69% YoY [ST]), below the blended base 218.79 because the DCF leans on FCF conversion of only 55.4% [CF,IS]."},
    "bear": {"probability": 0.25, "target_price_12m": 150, "basis": "Supplemental-payment cuts compress the 11.4% operating margin [IS] and P/E holds near 7.5x [RA], taking the stock back toward the 52-week low of 140.08 [HI]; above the DCF bear value because leverage of 1.90x [RA] and positive FCF do not support a negative DCF."}
  },
  "entry_price": 175.03,
  "entry_basis": "valuation file: base 218.79 x 0.8; at that level the same evidence would offer enough margin of safety for the reimbursement and litigation risks to justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

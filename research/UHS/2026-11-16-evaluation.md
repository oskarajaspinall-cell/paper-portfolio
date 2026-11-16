# Evaluation: Universal Health Services, Inc. (UHS) — 2026-11-16
## Bear case
UHS is payer-dependent: the filing adds One Big Beautiful Bill Act provider-fee and enrollment limits, and Medicaid supplemental payments are material across many states [Certain]; that is a policy price cap, not a cycle [Likely]. Rolling returns have rolled over: ROCE fell from 16.0% to 13.7% and operating margin slipped to 10.8% while leverage rose from 1.92x to 2.27x after the debt-funded Talkspace deal, a bet outside the hospital franchise [Certain]. California psychiatric staffing standards add cost, and the DC hospital arrangement is under Attorney General review [Certain]. The stock has already jumped +10.9% on the midterm result and sits 10.0% above its 200-day average; if policy hopes fade or volumes slow, that rally can de-rate [Likely]. The mechanical DCF bear of 10.37 shows how fragile cash-flow assumptions are [Certain].
## Bull case
At 8.3x earnings and 6.5x EV/EBITDA UHS trades below its own 5-year minimums and EV/EBITDA is 29% below peers, with a 9.82% FCF yield [Certain]. The reverse DCF prices -1.2% revenue growth, yet ROIC is 11.5% and ROE 19.7%, both above FY2021 [Certain]. The last-year dip is modest and has an identified, partly one-off cause: three loss-making facilities that management says could become a 2027 tailwind [Likely]. FCF margin is actually up over the year to 6.1% [Certain], and shares are down 6.83% year on year from buybacks at low multiples [Certain]. Licensed-bed scarcity and hard-to-replicate behavioral capacity give a local moat [Likely]. The Q3 reaction held 88% of its jump and relative strength vs SPY is positive over 3 and 6 months [Certain].
## Decision
```json
{
  "ticker": "UHS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds none of ROIC, operating margin or FCF margin falling over 1 or 3 years; the fact sheet's Direction change is ROCE only (16.0% to 13.7%), which management ties to three loss-making facilities (https://stockanalysis.com/stocks/uhs/transcripts/789940-ubs-global-healthcare-conference/) and California staffing costs.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Federal Medicaid provider-fee limits (One Big Beautiful Bill Act, per the 10-Q https://www.sec.gov/Archives/edgar/data/352915/000119312526451866/uhs-20260930.htm) cut supplemental payments and compress margins faster than facility recovery offsets them, de-rating a stock that has rallied on policy hopes.",
    "veto": null
  },
  "thesis": "A buyback-led hospital and behavioral-health operator with ROIC above FY2021 and a 9.82% FCF yield trades below its own 5-year minimum multiples and peers, but mid-level returns and Medicaid policy risk keep it short of high conviction.",
  "rationale": "Scorecard conviction 3: a real discount to its own history and peers, but returns are only mid-level, leverage is moderate and Medicaid policy is a live risk to margins. Good but not compelling, so no position; cash is an acceptable outcome.",
  "price_at_decision": 194.07,
  "price_date": "2026-11-13",
  "research_note": "research/UHS/2026-11-16.md",
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: valuation already scores full points; conviction is held at 3 by mid-level ROIC, moderate leverage and Medicaid policy risk, so a lower price alone would not make it a BUY.",
  "triggers": [
    {"text": "TTM ROIC falls below 9%, giving up the post-FY2023 recovery and showing Medicaid cuts are structural.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "TTM operating margin falls below 9.5%, showing payer and labor pressure outrun facility recovery.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 9.5}},
    {"text": "Net debt/EBITDA rises above 3.0x after the Talkspace borrowings.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}},
    {"text": "TTM FCF margin falls below 3%, reversing the cash-conversion gains.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 269.70, "basis": "Facility recovery and buybacks lift earnings and the multiple returns toward its own history, reaching the mechanical base fair value 269.70 [IS,BS,CF,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 226.36, "basis": "EV/EBITDA moves back toward its 5y minimum of 7.2x [RA] on steady TTM EBITDA, the fact sheet's EV/EBITDA base of 226.36; the DCF base is not used alone because its bear of -91.26 shows unstable cash-flow inputs."},
    "bear": {"probability": 0.25, "target_price_12m": 150.0, "basis": "Medicaid provider-fee limits in the 10-Q (https://www.sec.gov/Archives/edgar/data/352915/000119312526451866/uhs-20260930.htm) cut earnings and the midterm rally unwinds toward the 6-month low of 140.08 [HI], the DCF bear of 10.37 being an unreliable model artifact."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Assurant, Inc. (AIZ) — 2026-10-09
## Bear case
The stock already prices the good news. At $272.86 it trades 3.3% above the fact sheet's own-history base fair value ($263.95) and only 4.1% below the bull case ($283.91) [Certain] (fact sheet: Fair value). P/B of 2.2x sits above its 5y maximum (2.1x) and 31% above peers, and P/E of 13.1x is 68% above the peer median of 7.8x [Certain] (fact sheet: RA, P:ALL/PGR/KMPR/CINF). TTM ROE of 18.3% is a 5y high. If ROE slips back toward FY2022's 5.7% after a catastrophe year in Housing, a premium P/B on that ROE has room to compress [Likely]. The mechanical bear value of $91.23 is extreme, but it shows how sensitive the P/B+ROE method is to ROE [Certain]. Piotroski is a middling 5, and short interest rose 14.9% month on month [Certain] (fact sheet: ST). Q3 results on Nov 3 bring hurricane-season loss risk [Likely].
## Bull case
The business keeps getting better. ROE has risen from 10.6% to 18.3% and ROIC from 9.0% to 14.4% over five years [Certain] (fact sheet: RA). FCF conversion has stayed above 140% of net income since FY2022, giving a 12.30% FCF yield, and P/FCF of 8.1x sits at the 7th percentile of its 5y range [Certain] (fact sheet: CF, ST, RA). Q2 2026 was a record quarter: adjusted EBITDA rose 18% and EPS 19% ex-catastrophes, and full-year guidance was raised [Certain] (transcript /stocks/aiz/transcripts/661339-q2-2026/). Buybacks cut the share count 1.49% y/y, and site net debt/EBITDA is 0.29x [Certain] (fact sheet: ST, RA). Beta is 0.53 [Certain]. Embedded B2B contracts make earnings sticky [Likely]. If ROE holds, the P/E method gives $291.20–$303.46 [Certain] (fact sheet: Fair value).
## Decision
```json
{
  "ticker": "AIZ",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A rising-ROE embedded-protection insurer with a 12.30% FCF yield, but at $272.86 it trades at its own-history base fair value, above its 5-year maximum P/B and at a large premium to peers, so the improvement is already priced.",
  "rationale": "The business is high quality and improving, but the valuation gives almost no margin of safety. The price sits between the base ($263.95) and bull ($283.91) fair values, and P/B is above its 5-year maximum just as ROE peaks. With cat-season Q3 results due Nov 3, the case is good but not compelling, so AVOID and keep the cash.",
  "price_at_decision": 272.86,
  "price_date": "2026-10-08",
  "research_note": "research/AIZ/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE falls below 12%, under the FY2024 level of 15.3%, showing the return expansion was cyclical rather than structural.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "TTM ROIC falls below 9%, back to the FY2021 level, giving up the five-year improvement to 14.4%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "FCF conversion (FCF/net income, cash-flow and income-statement pages) falls below 100%, versus 155.7% TTM, undermining the cash-return case."},
    {"text": "Share count stops shrinking (shares change YoY turns positive, versus -1.49%), signalling buybacks have stalled.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 303.46, "basis": "ROE holds near the TTM 18.3% [RA] and guidance-raising growth continues, so the price reaches the P/E-method bull value of $303.46 (fact sheet Fair value), near the 52-week high of 303.94 [HI]."},
    "base": {"probability": 0.5, "target_price_12m": 263.95, "basis": "P/B of 2.2x, now above its 5y max [RA], drifts back as ROE normalises, converging on the fact sheet's blended base fair value of $263.95 (P/B+ROE 67%, P/E 33%)."},
    "bear": {"probability": 0.25, "target_price_12m": 218.04, "basis": "A catastrophe-heavy Housing quarter (FY2022 ROE was 5.7% [RA]) pushes P/B back toward its 5y median of 1.8x [RA], back to the 6-month low of 218.04 [HI]; this is above the mechanical bear of $91.23 because that value assumes ROE collapses permanently, while ROIC and FCF conversion have improved for five years [RA, CF]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

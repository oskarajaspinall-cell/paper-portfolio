# Evaluation: Northrop Grumman Corporation (NOC) — 2026-10-10
## Bear case
At $480.72 the stock already sits above its base fair value of $465.24, with only 6.1% to bull fair value and 59.0% down to bear [Certain] (factsheet). Returns have fallen hard: ROIC 25.4% to 15.0% and operating margin 21.0% to 13.4% since FY2021 [Certain] (RA, IS). FY2023's 6.7% operating margin shows that fixed-price development charges on B-21/Sentinel can recur [Likely] (note §2). Net debt/EBITDA rose from 1.27x to 2.03x [Certain] (BS, IS). The CAS pension civil investigation carries an unquantified "reasonably possible" material adverse effect [Certain] (10-Q). Buybacks are small, so shareholders get little help from capital returns [Certain] (10-Q). Real yields are up 56bp in 3 months and weigh on a long-duration DCF [Certain] (macro overlay). The price trend is weak, -30.4% over 6m, and Q3 results land on Oct 20 [Certain] (HI, ST).
## Bull case
Backlog of $104.7bn is 1.6x revenue, and management calls demand the strongest in more than 20 years [Likely] (Laguna transcript). Classified-program clearances make B-21 and Sentinel hard to compete for [Likely]. Cash quality is improving: FCF margin went from 4.0% to 8.5% and FCF conversion from 29.9% to 81.1% [Certain] (CF, IS). The stock trades 31% below peers on P/E and 19% below on EV/EBITDA, and below its own 5y minimum on P/FCF, EV/Sales and P/B [Certain] (RA). The 10-Q shows no new reach-forward loss [Likely]. A return to the 5y median EV/EBITDA of 12.6x supports $538.70 [Certain] (fair value). Piotroski 8 and Altman Z 3.33 point to sound fundamentals [Certain] (ST). Still, the DCF says the price already needs 5.7% growth, so the upside is real but not compelling [Likely].
## Decision
```json
{
  "ticker": "NOC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A franchise prime contractor with a record $104.7bn backlog and improving cash conversion, but its price already sits slightly above the $465.24 base fair value and implies 5.7% growth, while fixed-price and CAS-litigation risks leave a deep bear tail.",
  "rationale": "The business is good, but this is not a compelling buy. The peer discount is offset by the DCF: price is above base fair value, upside to bull is only 6.1%, and an FY2023-style charge or the CAS outcome could cut value sharply. Probability-weighted return is roughly flat, so conviction is 3 and the decision is AVOID. Cash is acceptable.",
  "price_at_decision": 480.72,
  "price_date": "2026-10-09",
  "research_note": "research/NOC/2026-10-10.md",
  "triggers": [
    {"text": "TTM operating margin falls below 10%, signalling a recurrence of FY2023-style fixed-price development charges (FY2023 6.7%).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 6%, reversing the FY2022-TTM improvement from 4.0% to 8.5%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "TTM ROIC falls below 10%, back toward the FY2023 trough of 8.4%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Total backlog in the 10-Q/earnings release declines year over year, undermining the record-demand thesis."}
  ],
  "scenarios": {
    "bull": {"probability": 0.22, "target_price_12m": 538.70, "basis": "EV/EBITDA returns to its 5y median 12.6x [RA] on TTM EBITDA as record backlog and FCF conversion of 81.1% [CF,IS] earn a re-rating, matching the EV/EBITDA method's base fair value of 538.70 [fair value]."},
    "base": {"probability": 0.50, "target_price_12m": 465.24, "basis": "Price converges on the blended base fair value of 465.24 [fair value], since the reverse DCF already prices 5.7% year-1 growth and operating margin holds near 13.4% TTM [IS]."},
    "bear": {"probability": 0.28, "target_price_12m": 313.15, "basis": "A renewed fixed-price charge on B-21/Sentinel like FY2023's 6.7% operating margin [IS], or an adverse CAS outcome [10-Q], drives EV/EBITDA toward its bear value of 313.15 [fair value]; bear probability is raised a small amount for the macro overlay's small tilt toward bear, as rising real yields hit long-duration value (research/NOC/2026-10-10-macro.md)."}
  },
  "entry_price": 372.19,
  "entry_basis": "valuation file: base 465.24 x 0.8 (20% margin of safety); at that price the same evidence would offset the fixed-price and CAS litigation tail.",
  "replaces": null,
  "replacement_reason": null
}
```

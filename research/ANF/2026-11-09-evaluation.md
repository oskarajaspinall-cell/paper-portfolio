# Evaluation: Abercrombie & Fitch Co. (ANF) — 2026-11-09
## Bear case
The returns rest on brand heat, not structure: FY2023 ROIC was 1.3% and operating margin 2.9% [Certain], so a fashion miss can wipe them out [Likely]. TTM margins include a tariff refund of approximately $100 million booked in cost of sales [company-reported] (https://www.sec.gov/Archives/edgar/data/1018840/000101884026000047/anf-20260801.htm), so run-rate earnings are lower than TTM shows [Likely]. Direction change: ROIC fell from 29.7% to 26.7% over 12 months and sits 12.2pp below its 2-year high of 38.9%, and ROCE is 4.4pp below its high [Certain]. Part of that is the FY2025 peak fading rather than lost share; the cause is the brand cycle rolling over, and it can't be called temporary yet [Likely]. The stock is up 112.4% in 12 months, EV/Sales sits at 89% and P/B at 83% of their 5y ranges [Certain], and Q3 results are due Nov 24, 2026 [Certain]. Fair value is unreliable: the bear case is negative and DCF and EV/EBITDA differ widely [Certain].

## Bull case
ANF earns high returns with a clean balance sheet: TTM ROIC 26.7%, operating margin 14.1% and net debt/EBITDA 0.71x [Certain]. Cash is strong: TTM FCF margin 10.6% (up 3.8pp in a year), FCF conversion 105.7% and an 8.93% FCF yield [Certain]. Buybacks shrank the share count by 9.81% YoY [Certain]. Q2 sales were a record, and full-year guidance for sales, operating margin and EPS was raised (transcript listed on the fact sheet) [Likely]. P/FCF of 11.2x is near its 5y low and EV/EBITDA is 18% below peers [Certain]. The reverse DCF implies roughly no revenue growth [Certain], which is undemanding if the brands hold [Likely]. Macro is context only: the weaker euro is a small translation drag on about 16% of sales (macro overlay) [Likely].

## Decision
```json
{
  "ticker": "ANF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Rolling ROIC is down from 29.7% to 26.7% and below its FY2025 peak, but operating margin is flat at 14.1%, FCF margin rose 3.8pp, leverage stays at 0.71x and guidance was raised in Q2 (fact sheet RA-T, IS-T, CF-T; transcript on the fact sheet): a fade from a peak, not lost share, though the tariff refund also flatters TTM.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Brand-heat reversal in fashion apparel: FY2023 showed returns can collapse (ROIC 1.3%), and TTM margins are flattered by a non-recurring tariff refund.",
    "veto": null
  },
  "thesis": "A high-return, low-leverage apparel retailer trades at a cash-flow multiple near its 5-year low, but its margins are flattered by a one-off tariff refund and depend on fashion brand heat after a doubling of the share price.",
  "rationale": "Quality, cash returns and buybacks are real, but the moat is brand heat with a recent history of collapse, TTM earnings include a non-recurring refund, the fair value range is unreliable and the stock has doubled ahead of Q3 results. Good but not compelling: AVOID, with an entry price at the fair-value margin of safety.",
  "price_at_decision": 149.54,
  "price_date": "2026-11-06",
  "research_note": "research/ANF/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 11%, showing the brand cycle has turned beyond the refund unwind.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11}},
    {"text": "TTM ROIC falls below 20%, a break from the post-FY2023 recovery.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM gross margin falls below 58%, signalling markdowns and lost full-price selling.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 58}},
    {"text": "Net debt/EBITDA rises above 2.0x (0.71x TTM now).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 202.27, "basis": "Brands keep momentum and margins hold ex-refund, so the DCF base of 202.27 on TTM FCF [IS,CF] is reached, helped by the 9.81% YoY share shrink [ST]."},
    "base": {"probability": 0.45, "target_price_12m": 150.0, "basis": "Margins ease as the tariff refund [company-reported, sec.gov 10-Q] drops out, so value sits between the EV/EBITDA base of 123.04 and the DCF base of 202.27, below the blended base of 175.86 that uses refund-inflated TTM figures [IS]."},
    "bear": {"probability": 0.30, "target_price_12m": 85.62, "basis": "Brand heat cools as in FY2023 (ROIC 1.3%, operating margin 2.9% [RA,IS]); the EV/EBITDA bear value of 85.62 [RA] applies, the negative DCF bear being an artefact of near-zero margins."}
  },
  "entry_price": 140.69,
  "entry_basis": "valuation file: base 175.86 x 0.8; at that price the cash yield on a sustainable margin would compensate for brand-cycle risk.",
  "replaces": null,
  "replacement_reason": null
}
```

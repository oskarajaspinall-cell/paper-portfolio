# Evaluation: United Integrated Services Co., Ltd. (TPE:2404) — 2026-11-07
## Bear case
Today's returns look like the top of a fab-capex cycle, not a steady state. Gross margin was 10.9% in FY2023 and is 21.3% TTM, so margins swing with the cycle [Certain]. FCF has run far ahead of net income (230.4% TTM, 320.5% FY2025), which most likely reflects customer prepayments that reverse when project awards slow [Likely]. The mechanical base fair value of 2,164.43 TWD comes from a DCF that extrapolates a peak 44.0% FCF margin; the EV/EBITDA method gives only 587.47 [Certain]. P/B sits at 9.2x, at the top of its 5y range [Certain]. The stock has fallen 24.3% in three months with no headline explaining it, and results are due Nov 12, 2026 [Certain]. Backlog and segment mix were not researched, so the evidence cannot rule out a slowdown in awards [Likely].

## Bull case
This is a net-cash contractor (net debt/EBITDA -4.21x TTM) earning 79.8% ROCE and 81.3% ROE, with operating margin up from 12.3% to 17.7% over five years [Certain]. On cash it is cheap: P/FCF 5.8x (peers 8.7x), FCF yield 17.25% and EV/EBITDA 6.6x, below its 5y median of 7.2x and peers at 9.4x [Certain]. The reverse DCF says the price implies year-1 revenue falling 26.7%, so the market already prices in a sharp downturn [Certain]. RSI of 23.3 shows the stock is oversold [Certain]. If fab-qualification relationships keep margins near current levels, the gap to the mechanical value is large [Guessing]. There is no dilution (shares -0.10% YoY), and insiders own 9.93% [Certain].

## Decision
```json
{
  "ticker": "TPE:2404",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-return cleanroom contractor trades cheaply on peak cash flow, but its margins and prepayment-driven FCF are cyclical and the unexplained sell-off ahead of results leaves durability unproven.",
  "rationale": "Cheap on current cash flow, but current cash flow is probably peak: FCF far exceeds earnings, margins are cyclical, backlog is unresearched and results are days away after an unexplained sell-off. Good but not compelling, so conviction is 3 and the decision is AVOID. Macro is context only.",
  "price_at_decision": 886.00,
  "price_date": "2026-11-06",
  "research_note": "research/TPE-2404/2026-11-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below 12%, back to the FY2021 level, showing the margin step-up was cyclical.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 15%, signalling customer prepayments are reversing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "TTM ROE falls below 40%, giving back most of the rise from 28.3% in FY2021.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 40}},
    {"text": "Net debt/EBITDA on the ratios page turns positive, ending the net-cash balance sheet."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1450.00, "basis": "Margins hold near TTM levels (operating 17.7% [IS]) and the stock re-rates back to its 52-week high of 1,450.00 [HI], still well below the DCF-led mechanical bull because that extrapolates peak FCF margin."},
    "base": {"probability": 0.45, "target_price_12m": 900.00, "basis": "Earnings plateau and P/E stays near its 5y median of 12.5x [RA] versus 13.5x now; we sit far below the mechanical base 2,164.43 because its DCF capitalises the 44.0% FY2025 FCF margin [CF,IS], while the EV/EBITDA method gives 587.47."},
    "bear": {"probability": 0.30, "target_price_12m": 636.13, "basis": "Fab-capex awards slow, margins revert towards FY2023 (gross 10.9% [IS]) and prepayments unwind, taking the price to the mechanical bear fair value of 636.13 [fact sheet Fair value]."}
  },
  "entry_price": 636.13,
  "entry_basis": "Valuation file: bear fair value 636.13 [IS,BS,CF,RA,ST,HI]; base x 0.8 would sit above the price because the DCF capitalises peak FCF, so the stock is a BUY only once the price already discounts margin mean reversion.",
  "replaces": null,
  "replacement_reason": null
}
```

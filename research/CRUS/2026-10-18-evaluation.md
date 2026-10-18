# Evaluation: Cirrus Logic, Inc. (CRUS) — 2026-10-18
## Bear case
The stock has fallen 34.6% in six months and sits 22.6% below its 200-day average while margins held, so the market is likely pricing a content loss at the dominant smartphone customer that trailing numbers cannot yet show [Likely]. Nothing in our research identifies or refutes that cause; buying ahead of the Nov 4, 2026 results is buying blind into the one risk that matters [Certain]. The mechanical base fair value ($111.01) is barely above the $107.87 close, while the through-cycle DCF bear is $27.45 and the blended bear $58.18 [Certain]. The confirmed Synaptics approach signals appetite for large M&A that could dilute returns [Likely]. The IRS transfer-pricing dispute (roughly $168.3m tax plus $63.7m penalties proposed [company-reported]) and a fixed GlobalFoundries wafer commitment through 2028 add downside if volumes soften [Likely].

## Bull case
Quality is at a five-year high: ROIC 28.4%, operating margin 23.0% (rising), FCF margin 27.9%, FCF conversion 132.9%, and net cash [Certain]. The stock trades below its own 5-year minimum on every multiple — P/E 13.2x, EV/EBITDA 8.3x, P/FCF 9.4x — and at a steep discount to peers, with a 10.58% FCF yield funding a share count down 3.79% YoY [Certain]. The reverse DCF implies only 5.1% year-1 growth, after record Q1 FY2027 revenue and EPS [Certain]. HPMS diversification (PC content, NVIDIA RTX Spark design wins [company-reported]) could reduce concentration and re-rate the shares toward the EV/EBITDA method's $135.39 base [Likely]. Bull fair value is $149.68 [Certain].

## Decision
```json
{
  "ticker": "CRUS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 28%-ROIC mixed-signal franchise trades below its own 5-year minimum multiples, but the price already sits near base fair value and the unexplained drawdown likely reflects customer-concentration risk we cannot yet assess.",
  "rationale": "Quality and multiples are compelling, but base fair value offers almost no margin of safety, the bear case is deep, and the cause of the six-month slide (likely design-win/content risk at the main customer) is unresolved with results due Nov 4. Good but not compelling: conviction 3, no position; revisit at the entry price or after results.",
  "price_at_decision": 107.87,
  "price_date": "2026-10-16",
  "research_note": "research/CRUS/2026-10-18.md",
  "triggers": [
    {"text": "TTM gross margin falls below 50%, signalling an unfavourable mix shift or pricing pressure.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 50}},
    {"text": "TTM ROIC falls below 15%, signalling the design-cycle moat has eroded.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "A disclosed design-win or content loss at the primary smartphone customer (10-Q risk factors or earnings call)."},
    {"text": "Net sales growth decelerates below high-single digits for two consecutive quarters as HPMS/PC content fails to offset audio declines (10-Q MD&A)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 149.68, "basis": "HPMS/PC diversification eases concentration fears and multiples recover toward history, matching the fact sheet's bull fair value [IS,BS,CF,RA] and the EV/EBITDA method's range."},
    "base": {"probability": 0.5, "target_price_12m": 111.01, "basis": "Margins hold near TTM levels (operating margin 23.0% [IS]) but concentration keeps the stock discounted, consistent with the blended base fair value [IS,BS,CF,RA,ST]."},
    "bear": {"probability": 0.25, "target_price_12m": 58.18, "basis": "A content loss at the main smartphone customer compresses through-cycle cash flows, matching the blended bear fair value where the through-cycle DCF bear is far lower [IS,BS,CF,RA,ST]."}
  },
  "entry_price": 88.81,
  "entry_basis": "valuation file: base 111.01 x 0.8 (20% margin of safety on the blended base fair value).",
  "replaces": null,
  "replacement_reason": null
}
```

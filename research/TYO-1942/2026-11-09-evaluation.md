# Evaluation: Kandenko Co.,Ltd. (TYO:1942) — 2026-11-09
## Bear case
The 43.3% six-month fall came alongside the 30 Oct Q2 results, and we cannot see why: guidance and order intake are unverified and the IR page was blocked [Certain]. A contractor whose operating margin doubled from 6.2% to 11.8% in five years is plausibly at a cyclical peak in a tight labour market and data-centre build-out, not a new steady state [Guessing]. FCF is lumpy: margins of 0.3-0.5% in FY2023-25, now 11.9% on a working-capital inflow (conversion 135.6%), so the 10.81% FCF yield overstates normal cash [Likely]. On earnings the stock is not cheap: P/E 12.8x sits at its 5y median and below peers only slightly, while P/B 2.0x is double its median [Certain]. The fair value is flagged unreliable (methods disagree 3.5x; EV/EBITDA base 2,414.03 JPY sits below the price) [Certain]. No moat evidence [Likely].
## Bull case
Every return metric is still rising on the rolling view: ROIC 19.7% TTM, up 4.9pp in a year, operating margin at its 2-year high of 11.8%, FCF margin up 13.1pp; there is no Direction change line [Certain]. The balance sheet is net cash (-0.92x net debt/EBITDA), Altman Z 6.37, and shares fell 1.65% YoY [Certain]. The reverse DCF implies -12.0% year-one revenue growth, a harsh outcome for a business still improving [Certain]. P/FCF 9.2x is at the bottom of its 5y range and well below peers [Certain]. Beta 0.56 and RSI 26.9 point to a de-rating of a crowded theme rather than a broken business, if the Q2 results held up [Guessing].
## Decision
```json
{
  "ticker": "TYO:1942",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "No ROIC, operating-margin or FCF-margin decline: all rising over 1 and 3 years [RA-T, IS-T, CF-T].",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Margins at a cyclical peak reverse; the unexplained 43.3% six-month fall around the 30 Oct Q2 report may reflect weaker guidance or orders that we could not verify.",
    "veto": null
  },
  "thesis": "A net-cash Japanese electrical contractor with sharply higher returns, de-rated hard for a reason we cannot yet verify.",
  "rationale": "Quality and balance sheet are strong, but on earnings multiples the stock is only at its own and peers' median, the mechanical fair value is unreliable, cash conversion is lumpy, and the cause of the fall around Q2 results is unknown. Scorecard conviction 2: AVOID; cash is acceptable.",
  "price_at_decision": 4062.00,
  "price_date": "2026-11-06",
  "research_note": "research/TYO-1942/2026-11-09.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 12%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Operating margin (TTM) falls below 9%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 9}},
    {"text": "FCF margin (TTM) falls below 3% while net income holds", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 3}},
    {"text": "Net debt/EBITDA rises above 0.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 0.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 6404.50, "basis": "Margins hold near the TTM 11.8% operating margin [IS-T] and the market drops the -12.0% revenue decline the reverse DCF implies, reaching the mechanical base fair value 6,404.50 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 4294.98, "basis": "P/E stays near its 5y median 12.9x [RA] as returns plateau; target set at the EV/EBITDA method's bull value 4,294.98 rather than the DCF, which the fact sheet flags unreliable."},
    "bear": {"probability": 0.30, "target_price_12m": 2414.03, "basis": "Margins revert toward the FY2022-24 range of 6.0-6.8% [IS], giving the EV/EBITDA base 2,414.03 [fact sheet Fair value], consistent with the market's de-rating."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2 needs no entry price; the obstacle is also the unverified cause of the fall around the Q2 report and the lack of a moat, which a lower price alone would not resolve.",
  "replaces": null,
  "replacement_reason": null
}
```

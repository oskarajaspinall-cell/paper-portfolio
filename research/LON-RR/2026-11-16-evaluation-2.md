# Evaluation: Rolls-Royce Holdings plc (LON:RR) — 2026-11-16
## Bear case
The turnaround is in the price. EV/EBITDA of 20.3x sits at 96% of its 5y range (max 20.7x) and EV/Sales 4.8x and P/FCF 25.3x are above their 5y maxima [Certain] [RA]. The valuation points come from trend strength, not a discount: the close is only +0.8% above the 200-day average after a -11.4% three months [Certain] [HI], so any slowdown in margin gains risks a de-rating toward the 5y median 15.5x EV/EBITDA [Likely]. October's fall followed Safran and GE Aerospace results flagging aviation risks [Likely] (https://invezz.com/news/2026/10/27/rolls-royce-outlook-as-safran-and-ge-aerospace-earnings-flag-aviation-risks/). A narrowbody re-entry brings development cost and execution risk [Likely] (https://www.reuters.com/business/aerospace-defense/rolls-royce-nears-government-subsidy-deal-develop-new-engine-uk-ft-reports-2026-10-23/). Mechanical fair value is [data unavailable], so no independent anchor checks the price [Certain]. Buybacks at 20x EBITDA earn less than at median multiples [Guessing]. Revenue by country is unverified (macro overlay, context weight) [Certain].
## Bull case
Quality is high and still improving on a rolling basis: operating margin 20.7% TTM vs 16.3% a year earlier, FCF margin 19.3%, ROCE 24.8% at its 2-year high [Certain] [IS-T, CF-T, RA-T]. No **Direction change** line is printed; nothing is falling. The balance sheet is net cash (net debt/EBITDA -0.41x) [Certain] [BS]. The widebody installed base generates decades of per-flying-hour service revenue [Likely]. The 12 November update reaffirmed guidance, reported a growing engine backlog and launched a multi-year buyback [Likely] (https://www.reuters.com/business/aerospace-defense/rolls-royce-announces-15-billion-buyback-engine-demand-grows-2026-11-12/), and shares fell -0.70% YoY [Certain] [ST]. The trend is healthy without being stretched: 12-month +21.5%, above the 200-day, FCF yield 3.96%, and P/FCF is -7% vs peers [Certain] [ST, RA]. Macro is context only (overlay) [Certain].
## Decision
```json
{
  "ticker": "LON:RR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Python lists nothing falling: ROIC, operating margin and FCF margin all rose over the last year on the rolling table [RA-T, IS-T, CF-T].", "moat": "narrow", "key_risk": "medium", "key_risk_text": "A de-rating from the top of its own EV/EBITDA range if the margin gains slow or the aviation cycle softens, as peers flagged in October.", "veto": null},
  "thesis": "A net-cash, rapidly improving aero-engine franchise with rising rolling margins and returns, priced at the top of its own multiple range on trend strength rather than a discount.",
  "rationale": "Quality, balance sheet and direction are excellent, but EV/EBITDA sits near its 5y max, no mechanical fair value is computable and the expected 12-month value is close to the price. Good but not compelling at this price.",
  "price_at_decision": 1350.60,
  "price_date": "2026-11-13",
  "research_note": "research/LON-RR/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 16%, back to the level of a year earlier, showing the turnaround gains are reversing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 16}},
    {"text": "TTM FCF margin falls below 14%, showing cash conversion of the service model is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "Net debt/EBITDA turns positive above 1.0x (net cash now), e.g. from narrowbody development spend.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "TTM ROCE on the ratios page falls below 18%, or the company cuts full-year guidance in a release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1650, "basis": "Operating margin keeps rising as it did over the last year (+4.4pp [IS-T]) and EV/EBITDA holds near 20.3x [RA] on higher EBITDA, helped by the buyback."},
    "base": {"probability": 0.5, "target_price_12m": 1450, "basis": "Reaffirmed guidance and backlog growth (Reuters 2026-11-12) lift EBITDA while the multiple drifts slightly lower from 96% of its 5y range [RA]; no fair value is computable [data unavailable] so this is our own estimate."},
    "bear": {"probability": 0.25, "target_price_12m": 1050, "basis": "Aviation risks flagged by peers (Invezz 2026-10-27) slow margin gains and EV/EBITDA de-rates toward its 5y median 15.5x [RA] on flat TTM EBITDA."}
  },
  "entry_price": 1050,
  "entry_basis": "No mechanical fair value is computable; anchored instead on EV/EBITDA back near its 5y median 15.5x [RA], our bear scenario level, where the same quality would come with a real discount.",
  "replaces": null,
  "replacement_reason": null
}
```

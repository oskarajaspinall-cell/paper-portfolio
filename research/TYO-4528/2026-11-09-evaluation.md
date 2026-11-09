# Evaluation: Ono Pharmaceutical Co., Ltd. (TYO:4528) — 2026-11-09
## Bear case
Returns have halved from peak: ROIC 19.3% (FY2024) to 9.9% TTM, operating margin 31.9% to 20.0%, and the 3-year changes are still falling (-8.5pp ROIC, -14.1pp margin) [Certain]. The FY2025 step-down is unexplained in our research; the note did not read the Q2 results [Certain], so we cannot say whether it is a one-off charge or the start of royalty erosion [Guessing]. The edge is patent exclusivity on a partnered oncology franchise, which is time-limited, and loss of exclusivity on the lead franchise is the main unquantified risk [Guessing]. The price already discounts shrinking revenue (reverse DCF -15.0% year 1), but P/E 15.3x is at its 5y median, so earnings are not cheap [Certain]. The mechanical fair value is flagged unreliable (methods disagree 2.1x) and the P/E method's base, 2,385.99, sits near the price [Certain]. The foreign revenue split is unverified [Certain].
## Bull case
The last 12 months are rising: ROIC 6.4% to 9.9%, operating margin 11.5% to 20.0%, FCF margin 19.0% to 25.9%, its 2-year high [Certain]. That pattern fits a trough with the balance sheet intact rather than a broken model [Likely]: net cash (net debt/EBITDA -1.10x), Altman Z 5.29, Piotroski F 7, flat share count [Certain]. Cash flow is cheap: P/FCF 9.0x at 1% of its 5y range, FCF yield 11.12%, EV/EBITDA 7.4x against a peer median of 13.4x [Certain]. Pipeline activity (ONO-1110 Phase 2 data, sapablursen orphan designation, discovery partnerships) gives replenishment options [Likely]. Beta 0.18 and macro is context only per the overlay [Certain].
## Decision
```json
{
  "ticker": "TYO:4528",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and operating margin fell over 3 years, but the rolling-12-month table shows recovery (ROIC 6.4% to 9.9%, operating margin 11.5% to 20.0%, FCF margin at its 2-year high 25.9%) with net cash intact (-1.10x) [RA-T, IS-T, CF-T, ST]; the FY2025 cause itself is unverified in the note.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Loss of exclusivity / royalty erosion on the partnered lead oncology franchise, unverified in timing and size (note section 6), could make the recent recovery a pause rather than a trough.",
    "veto": null
  },
  "thesis": "A net-cash, cash-generative Japanese pharma priced for shrinking revenue whose margins are recovering, but whose earnings durability past its lead franchise is unverified.",
  "rationale": "Cheap on cash flow and net cash, with a real 12-month recovery, but ROIC is below 10%, earnings sit at a median multiple, the fair value is unreliable, and exclusivity risk on the lead franchise is unquantified. Not a high-conviction idea: AVOID; cash is acceptable.",
  "price_at_decision": 2352.5,
  "price_date": "2026-11-06",
  "research_note": "research/TYO-4528/2026-11-09.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 15%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "FCF margin (TTM) falls below 15%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "ROIC (TTM) falls below 7%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 7}},
    {"text": "Net cash is gone: net debt/EBITDA rises above 0.0x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 4197.11, "basis": "Recovery continues toward the 2-year highs (operating margin 24.6%, ROIC 11.9%) [RA-T, IS-T] and the market re-rates to the mechanical base fair value 4,197.11 [fact sheet Fair value], driven by the DCF on an 11.12% FCF yield [ST]."},
    "base": {"probability": 0.5, "target_price_12m": 2600, "basis": "Margins hold near TTM and EV/EBITDA drifts from 7.4x toward its 5y median 8.3x [RA], between the P/E method's base 2,385.99 and bull 2,682.49 [fact sheet Fair value]; below the blended base because the fair value is flagged unreliable."},
    "bear": {"probability": 0.25, "target_price_12m": 1429.21, "basis": "Lead-franchise royalty erosion (note section 6, Bear case) pushes earnings down and the P/E method's bear case of 1,429.21 [fact sheet Fair value] applies, near the 5y P/E low of 9.0x [RA]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Eastern Air Logistics Co., Ltd. (SHA:601156) — 2026-11-23
## Bear case
Returns have normalised from a pandemic freight windfall: ROIC fell from 113.8% (FY2021) to 16.5% TTM and operating margin from 25.1% to 15.8% [Certain]. The last year did not reverse that: operating margin slipped from 16.8% to 15.8% and ROIC sits 2.8pp below its 2-year high of 19.2% [Certain]. The ROCE and FCF upturns are weak evidence: TTM FCF conversion of 233.3% against 34.7% in FY2024 points to working-capital timing, so the 21.36% FCF yield likely overstates run-rate cash [Likely]. P/E of 11.0x is already above its 5-year max [Certain]; with the price 11.2% above its 200-day average, a freight-rate downturn would bring both a de-rating and an earnings cut [Likely]. No moat is evidenced in a cyclical, competitive market [Guessing]; the fair value is flagged unreliable [Certain], and no quarterly results or capital-return policy were read [Certain].
## Bull case
The balance sheet is net cash (net debt/EBITDA -0.69x) with Altman Z of 3.32 [Certain]. Returns have stabilised near 16% rather than kept falling: ROIC 16.5% against 16.0% a year earlier and ROCE 16.9% against 14.8% [Certain]. On cash and enterprise multiples the stock is cheap: EV/EBITDA 4.8x against a 5.8x 5-year median and 56% below peers, P/FCF 4.7x below its 5-year minimum [Certain]. The reverse DCF implies year-1 revenue growth of -22.9%, a harsh assumption for a business that is still growing cash flow [Likely]. The trend is working: the stock is up 19.7% over 12 months and beat SPY by 15.6pp, at low beta of 0.56 [Certain]. If even part of the FCF surge persists, the market is pricing a decline that has not arrived [Guessing].
## Decision
```json
{
  "ticker": "SHA:601156",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "The 5-year fall in ROIC and margins is the unwind of the FY2021-22 pandemic freight peak (ROIC 113.8% -> 16.6% FY2025 [RA]); over the last 12 months ROIC is flat (16.0% -> 16.5%) and ROCE rising (14.8% -> 16.9%) [RA-T], with net cash intact (-0.69x [BS,IS]); operating margin still slipped 1.1pp [IS-T].", "moat": "none", "key_risk": "medium", "key_risk_text": "A freight-rate downturn cuts margins further while the TTM FCF surge (233.3% of net income) proves to be working-capital timing, so the cheap P/FCF disappears and the P/E, already above its 5y max, de-rates.", "veto": null},
  "thesis": "A net-cash air-freight logistics operator whose returns have stabilised near 16% after the pandemic peak, trading at low cash and EV multiples, but without an evidenced moat and with FCF likely flattered by timing.",
  "rationale": "Quality is adequate and the balance sheet strong, but no moat, a cyclical industry, an unreliable fair value and an FCF yield likely inflated by working capital make it good but not compelling. Below the buy bar: AVOID; cash is acceptable.",
  "price_at_decision": 19.71,
  "price_date": "2026-11-20",
  "research_note": "research/SHA-601156/2026-11-23.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 12%, showing returns did not stabilise.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Operating margin (TTM) falls below 13%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 13}},
    {"text": "FCF margin (TTM) falls below 10%, confirming the cash surge was timing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "The balance sheet moves from net cash to net debt (net debt/EBITDA above 0x on the ratios page)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 26.0, "basis": "Returns hold near 16% and part of the FCF surge persists, so EV/EBITDA re-rates above its 5y median 5.8x toward its 6.4x max [RA], above the EV/EBITDA method's bull of 23.37 [fact sheet fair value]; the DCF's 53.32 is ignored as unreliable."},
    "base": {"probability": 0.5, "target_price_12m": 22.83, "basis": "EV/EBITDA returns toward its 5y median 5.8x [RA] on TTM EBITDA, the EV/EBITDA method's base of 22.83 [fact sheet fair value]; the DCF base of 51.07 is set aside because the fair value is flagged unreliable and FCF is likely flattered."},
    "bear": {"probability": 0.25, "target_price_12m": 13.81, "basis": "A freight downturn takes operating margin further below 15.8% [IS-T] and FCF conversion reverts toward the FY2024 34.7% [CF,IS], matching the EV/EBITDA method's bear of 13.81 [fact sheet fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the scorecard stays short of 4 even with full valuation points, because moat is none and ROIC and operating margin are still falling [RA-T,IS-T]; a lower price would not change the decision."
}
```

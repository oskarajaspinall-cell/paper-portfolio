# Evaluation: Pentair plc (PNR) — 2026-10-08
## Bear case
The multiple is at a trough because earnings credibility is impaired. The preliminary Q2 2026 release disclosed Pool destocking "more pronounced than previously estimated", with a deep guidance cut, and the CFO resigned the same day [Certain]. Bob Hau, who starts 2026-11-01, is the third CFO in about a year, and securities class actions are now proceeding [Certain]. ROE has fallen from 24.6% to 17.1% and net debt/EBITDA has risen from 1.24x to 1.62x. The debt-funded Taco deal closed on 2026-10-01, adding leverage just as Pool weakens [Certain]. TTM figures do not yet fully show the cut, so trailing P/E 13.1x likely overstates how cheap the stock is [Likely]. The macro overlay shows a hawkish, real-rate-led tightening: the 10y real yield is 2.91% and fed funds went up 25bp. That hits financed pool demand [Likely]. Q3 results on 2026-10-20 could cut guidance again [Guessing].
## Bull case
The business is still high quality. Gross margin rose from 35.0% to 41.4% and operating margin from 16.9% to 22.8% over five years. TTM ROIC is 14.0% and FCF conversion is 103.3% [Certain]. The stock trades below its 5-year minimum P/E, EV/EBITDA, P/FCF and P/B, at a 52% P/E discount to peers and an 8.08% FCF yield [Certain]. Shares outstanding fell 1.59% YoY and Altman Z is 4.99, so the balance sheet is not distressed [Certain]. Pool destocking is a channel-inventory event, and such events usually resolve within a few quarters [Likely]. If Flow and Water Solutions hold their margins, normalized earnings justify at least the 5-year minimum multiple [Likely]. Short interest is only 3.97% and fell 16.3% month-on-month, so the selling looks like capitulation rather than a building short thesis [Likely].
## Decision
```json
{
  "ticker": "PNR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A margin-expanding water-equipment franchise trades below every 5-year minimum multiple, but a Pool guidance cut, CFO churn, class actions, new acquisition debt and a hawkish rate backdrop mean trailing earnings cannot yet be trusted as the base.",
  "rationale": "The stock is cheap on trailing numbers, but those numbers precede a guidance cut. Management credibility is impaired, litigation is live, leverage is rising after Taco, and the macro tilt is moderately bearish on financed pool demand. Q3 results on 2026-10-20 come before any thesis can be tested. Conviction 3 is below the buy threshold, so AVOID and hold cash.",
  "price_at_decision": 52.19,
  "price_date": "2026-10-07",
  "research_note": "research/PNR/2026-10-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, showing Pool destocking has become a structural returns problem rather than channel timing.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM gross margin falls below 38%, showing pricing/mix pressure is spreading beyond Pool into Flow and Water Solutions.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 38}},
    {"text": "Debt/EBITDA rises above 3.0x, showing the debt-funded Taco acquisition plus weak Pool earnings are straining the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 61.35, "basis": "Destocking proves cyclical and P/E re-rates from 13.1x to its 5-year minimum of 15.4x [RA] on TTM earnings; probability trimmed from 0.30 for the overlay's moderate bear tilt (research/PNR/2026-10-08-macro.md)."},
    "base": {"probability": 0.40, "target_price_12m": 52.0, "basis": "Earnings hold near TTM and P/E stays near 13.1x [RA] while litigation and the CFO transition keep the discount; probability trimmed from 0.45 for the overlay's moderate bear tilt (research/PNR/2026-10-08-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 37.7, "basis": "Net margin reverts from 16.2% TTM to the FY2022 trough of 11.7% [IS] at an unchanged 13.1x P/E; probability raised from 0.25 because the overlay's moderate bear tilt (rates hitting financed Pool demand, Taco leverage) argues against it (research/PNR/2026-10-08-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

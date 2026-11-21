# Evaluation: Sasol Limited (JSE:SOL) — 2026-11-21
## Bear case
The fall is unexplained: the close is 17.5% below the 50-day MA with no earnings-type reaction and no company announcement in the headlines, so we cannot show it is an overreaction rather than news we have not seen (oil, refining margins, the rand or plant reliability) [Certain]. Earnings are commodity-driven and volatile: ROE swung from 24.1% to -25.4% to 8.8% and ROIC sits 4.6pp below its 2-year high of 20.1% [Certain]. The 12-month operating-margin recovery (15.0% to 17.1%) follows refining margins, not pricing power, and can reverse [Likely]. The valuation points come from trend strength after a +60.8% year, with the price now only at its 200-day MA: if spreads fade, a de-rating would break that trend [Likely]. P/FCF sits at 74% of its 5y range [Certain]. No mechanical fair value exists and South African currency and rate risk are unmeasured [Certain].

## Bull case
The business case is intact on the numbers: ROIC 15.4% (+5.4pp over 12 months), ROCE 16.5% at its 2-year high, operating margin 17.1% and net debt/EBITDA down to 1.11x from 1.55x, with management citing net debt at a 10-year low [Certain]. EV/EBITDA 3.3x sits at 12% of its 5y range, against a 7.9x peer median, and the FCF yield is 9.12% [Certain]. Piotroski 7 shows broad improvement [Certain]. The idled ISOSIV paraffin unit is back in beneficial operation [Certain]. With no company-specific news found, part of the fall may be sentiment after a +60.8% 12-month run, and the price is still at its 200-day MA [Guessing]. The bull case needs oil and chemical spreads to hold, which we cannot verify [Guessing].

## Decision
```json
{
  "ticker": "JSE:SOL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years: ROIC (+5.4pp), ROCE (+3.6pp) and operating margin (+2.1pp) rose over 12 months and FCF margin is flat [RA-T, IS-T, CF-T].",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Earnings track oil, refining margins, chemical spreads and the rand; the unexplained stock-specific fall may reflect a commodity or operational reversal that would undo the 12-month margin recovery and de-rate a price whose support is trend strength (ROE history 24.1% to -25.4% [RA]).",
    "veto": null
  },
  "thesis": "A deleveraged, cheap-on-EBITDA South African energy-chemicals group whose recovering returns depend on commodity spreads, with no measurable moat and an unexplained fall.",
  "rationale": "Cheap on EV/EBITDA with an improved balance sheet, but earnings are commodity-driven, there is no moat evidence, no fair value, and the cause of the fall is unknown, so it cannot be shown to be an overreaction. Same conclusion as the 2026-11-15 AVOID at conviction 3.",
  "price_at_decision": 20302,
  "price_date": "2026-11-20",
  "research_note": "research/JSE-SOL/2026-11-21.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, back to the FY2025 trough, showing the recovery has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 13%, well under the FY2025 low of 15.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 13}},
    {"text": "Net debt/EBITDA rises above 2.5x, reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "TTM FCF margin turns negative.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 30056, "basis": "Margins hold near 17.1% and EV/EBITDA re-rates off 12% of its 5y range, retesting the 6-month high of 30,056 [HI, RA]."},
    "base": {"probability": 0.45, "target_price_12m": 20291, "basis": "EV/EBITDA stays near its 5y median 3.2x [RA] on flat TTM EBITDA, leaving the price around its 200-day MA of 20,291.22 [ST, HI]."},
    "bear": {"probability": 0.30, "target_price_12m": 15382, "basis": "Commodity spreads reverse the 12-month margin recovery toward FY2025's 15.0% [IS-T] and the price revisits its 6-month low of 15,382 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: no mechanical fair value exists, the moat is unproven and earnings are commodity-driven with an unexplained fall; a lower price alone would not lift conviction to 4.",
  "replaces": null,
  "replacement_reason": null
}
```

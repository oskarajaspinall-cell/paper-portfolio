# Evaluation: Vertiv Holdings Co (VRT) — 2026-11-16
## Bear case
The price discounts years of AI build-out: the reverse DCF needs 29.4% year-1 revenue growth, and even the mechanical bull fair value (175.38) sits below the 202.07 close [Certain]. Returns are a cycle, not a franchise yet: operating margin was 4.0% in FY2022 and ROIC 2.4%, so today's 43.8% ROIC depends on hyperscaler capex staying high [Likely]. Beta 2.11 and a trend that is broken (25.6% below the 200-day average, 50-day 15.5% under the 200-day) show the market already doubting duration [Certain]. Rising real yields (+0.47pp in 3 months to 2.86%) press on a long-duration multiple, per the macro overlay [Likely]. P/E 35.4x and P/B 14.1x are still well above peers (27.1x, 7.6x) [Certain]. Midterm-policy worries hit the stock on 5 Nov; any capex pause would compress both earnings and multiple at once [Guessing].
## Bull case
The business is working and accelerating: TTM ROIC 43.8% vs 27.4% a year earlier, operating margin 21.1% (+3.1pp), FCF margin 24.0% (+10.1pp), all at or near 2-year highs [Certain]. The balance sheet moved from 5.80x leverage to net cash (-0.11x) [Certain]. Q3 operating profit rose 82.4% YoY [company-reported] and the outlook was raised [Likely]. The de-rating has gone far: P/E 35.4x is below its 5y minimum 39.8x and P/FCF 23.7x sits at its 5y low, with a 4.22% FCF yield [Certain]. EV/EBITDA 23.3x is in line with peers (23.8x) [Certain]. Product roadmap (800V DC, liquid cooling, Nvidia ATLAS validation) deepens the installed-base and service moat [Likely]. The mechanical DCF is blunt for a business whose returns tripled [Guessing].
## Decision
```json
{
  "ticker": "VRT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "ROIC, operating margin and FCF margin all rose over the last 1 and 3 years [RA-T, IS-T, CF-T].", "moat": "narrow", "key_risk": "medium", "key_risk_text": "An AI data-center capex slowdown would hit both earnings and the multiple of a beta-2.11 business whose margins were 4.0% in FY2022.", "veto": null},
  "thesis": "An AI-infrastructure power and cooling leader with surging returns and net cash, but the price still implies 29.4% revenue growth and sits far above every mechanical fair value while the trend is broken.",
  "rationale": "Quality and direction are excellent, but the price exceeds even the bull fair value and the stock trades well below its 200-day average, so there is neither a discount nor trend strength. Good but not compelling: AVOID, with an entry price at the margin-of-safety level.",
  "price_at_decision": 202.07,
  "price_date": "2026-11-13",
  "research_note": "research/VRT/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 17%, giving up the FY2024-to-TTM expansion from 17.3% to 21.1%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "TTM ROIC falls below 25%, under the 27.4% of a year earlier, showing AI-driven returns are fading.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "TTM FCF margin falls below 14%, back to the FY2024 level of 14.4%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "Net debt/EBITDA rises above 1.5x from -0.11x, reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 295, "basis": "P/FCF re-rates from its 5y low of 23.7x toward its 5y median 34.9x [RA] on TTM FCF as AI demand and the raised outlook hold; above the mechanical bull 175.38 because the DCF ignores the step-up in returns."},
    "base": {"probability": 0.4, "target_price_12m": 205, "basis": "EV/EBITDA stays near peers (23.8x) [RA] with FCF margin around 24.0% [CF-T]; above the mechanical base 93.70 because that DCF assumes growth fading from pre-AI history."},
    "bear": {"probability": 0.35, "target_price_12m": 120, "basis": "EV/EBITDA falls toward its 5y minimum 15.6x [RA] on a capex pause; probability raised from the bull case for the macro overlay's small toward-bear tilt from rising real yields (research/VRT/2026-11-16-macro.md)."}
  },
  "entry_price": 74.96,
  "entry_basis": "valuation file: base 93.70 x 0.8.",
  "replaces": null,
  "replacement_reason": null
}
```

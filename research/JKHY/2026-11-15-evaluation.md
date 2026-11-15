# Evaluation: Jack Henry & Associates (JKHY) — 2026-11-15
## Bear case
The price already discounts above-framework growth: the reverse DCF implies 13.6% year-1 revenue growth against the roughly 8% framework management cites [Likely]. The mechanical fair value (base 123.97, bull 135.98) sits below the 177.67 close [Certain], though the P/E method disagrees, so reliability is low. The stock is extended: +15.4% above its 200-day average, +25.6% over six months, RSI 67.4 [Certain]; if growth slows to the framework, a de-rating toward the 5y P/E low of 19.5x is the main risk [Likely]. Margin pressure is building: Q1 R&D rose 16.6% [company-reported] and cyber/AI/infrastructure spend is a stated headwind [Likely]. Reported growth is flattered by lumpy deconversion revenue (services and support 5.1% ex-deconversion) [company-reported]. The Direction change (ROIC down over five fiscal years, up over the last 12 months) reflects the FY2023-24 trough unwinding, not a new decline [Likely]. Short interest is rising [Certain].
## Bull case
A high-return, unlevered franchise that is working: TTM ROIC 23.8%, FCF margin 27.6%, FCF conversion 138.2%, net debt/EBITDA 0.13x [Certain]. Rolling ROIC rose from 21.8% to 23.8% and FCF margin from 24.6% to 27.6% over the last year, so the 5-year ROIC dip is a recovered trough, not erosion [Certain]. Q1 FY27 brought nine core wins and raised FY27 revenue and EPS guidance [Likely]; processing grew 10.7% [company-reported]. Core-system switching costs keep churn low and competitor disruption is feeding wins [Likely]. Despite the run-up, P/E (24.4x) sits 30% up its 5y range against a 31.7x median and P/FCF 15% up its range, at a 5.80% FCF yield [Certain]; a return toward the median P/E supports the P/E method's 230.66 [Guessing]. Low beta (0.54) and steady buybacks (shares -2.22% YoY) add defensiveness [Certain].
## Decision
```json
{
  "ticker": "JKHY",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Over the last 1 and 3 years ROIC (21.8% to 23.8%), operating margin (+3.3pp over 3 years) and FCF margin (24.6% to 27.6%) are all rising [RA-T, IS-T, CF-T]; the 5-year ROIC dip is the FY2023-24 trough that has since recovered.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "After a +25.6% six-month run the price implies 13.6% year-1 growth vs an ~8% framework; if growth stays at the framework or investment costs squeeze margins, the multiple de-rates toward its 5y low.",
    "veto": null
  },
  "thesis": "A high-return, unlevered core-banking franchise with rising rolling returns and cash margins and raised guidance, trading below its own 5-year median multiples, but whose price now implies growth above the company's framework.",
  "rationale": "Fundamentals are improving and the franchise is sound, but the price has run ahead: the reverse DCF needs above-framework growth and the mechanical fair value sits below the price. The skew is balanced, not compelling, so hold at the conviction-3 size rather than add.",
  "price_at_decision": 177.67,
  "price_date": "2026-11-13",
  "research_note": "research/JKHY/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 19%, the FY2024 trough, evidencing moat erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 19}},
    {"text": "TTM operating margin falls below 22%, under the FY2024 low of 22.1%, showing cloud/AI/security investment or renewal pricing is compressing profitability structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}},
    {"text": "TTM FCF margin falls below 20%, reversing the rising trend (TTM 27.6%).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Processing revenue growth in the 10-Q MD&A falls below 5% year on year for two consecutive quarters, or core client losses outnumber wins."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 230.66, "basis": "P/E re-rates toward its 5y median 31.7x [RA] as raised FY27 guidance and core wins deliver, matching the fact sheet's P/E-method base of 230.66."},
    "base": {"probability": 0.5, "target_price_12m": 185.0, "basis": "P/E holds near 24.4x [RA] while earnings grow at the ~8% framework (KBW transcript); above the low-reliability DCF base 123.97 because the DCF ignores the rising rolling ROIC and FCF margin [RA-T, CF-T]."},
    "bear": {"probability": 0.25, "target_price_12m": 141.64, "basis": "Growth slows to the framework and investment costs pressure margins, de-rating P/E toward its 5y low 19.5x [RA], the fact sheet's P/E-method bear of 141.64."}
  },
  "entry_price": 145.65,
  "entry_basis": "P/FCF back at its 5y low of 14.1x [RA] (vs 17.2x now); the DCF base 123.97 x 0.8 is not used because the fair-value methods differ by almost 2x (low reliability).",
  "replaces": null,
  "replacement_reason": null
}
```

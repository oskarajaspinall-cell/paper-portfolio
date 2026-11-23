# Evaluation: Jack Henry & Associates, Inc. (JKHY) — 2026-11-23
## Bear case
The cash-flow valuation says the price already pays for strong execution: base fair value 125.12 sits 27.0% below the 171.32 close and even the bull case (137.26) is below it [Certain]. The reverse DCF implies 12.4% year-1 revenue growth, above management's 8% framework [Likely]. The stock trades 11.3% above its 200-day average after a 22.5% six-month run, so the points it earns come from trend strength, not a discount; if growth slows, an extended price risks a de-rating toward the 5y P/E low of 19.5x [Likely]. Margins face cyber, AI and infrastructure cost headwinds, with R&D up 16.6% [company-reported] (https://www.sec.gov/Archives/edgar/data/779152/000077915226000098/jkhy-20260930.htm) [Likely]. Part of services growth is lumpy deconversion revenue that flatters the run-rate [Likely]. ROIC is still 1.3pp below FY2022 on fiscal-year endpoints, though the last 12 months are rising [Certain].
## Bull case
A sticky, switching-cost franchise in US community-bank cores: TTM ROIC 23.8%, operating margin 25.6%, FCF margin 27.6%, net debt/EBITDA 0.13x [Certain]. The Direction change line is a recovery, not a decline: rolling ROIC rose from 21.8% to 23.8% off the FY2024 trough of 19.1%, and FCF margin rose 3.0pp in a year [Certain]. Q1 FY27 brought record non-GAAP revenue, nine core wins and raised FY27 guidance, with processing up 10.7% [company-reported] (https://www.sec.gov/Archives/edgar/data/779152/000077915226000098/jkhy-20260930.htm) [Likely]. On its own history it is cheap: P/E 23.5x vs a 31.7x median and P/FCF 16.6x at the 12th percentile, with a 6.01% FCF yield [Certain]. Shares fell 2.22% YoY via buybacks, and FCF conversion is 138.2% [Certain]. Beta 0.54 and recurring revenue make it defensive [Likely]; macro is context only (overlay).
## Decision
```json
{
  "ticker": "JKHY",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROIC is lower than FY2022 on fiscal-year endpoints, but ROIC, ROCE, operating and FCF margin are all rising or flat over the last 1 and 3 years (RA-T, IS-T, CF-T); the five-year dip was the FY2024 trough of 19.1%, since recovered.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Growth slows toward the 8% framework while the price implies 12.4% year-1 growth and trades above its 200-day average: a de-rating toward the low end of the own-history P/E range, compounded by AI/cyber cost pressure on margins.",
    "veto": null
  },
  "thesis": "A high-return, unlevered core-banking franchise with recovering rolling returns and raised guidance trades below its own 5-year median multiples, but its price already implies growth above the company's framework.",
  "rationale": "Quality is high and improving and the stock is cheap on its own history, but the cash-flow fair value sits well below the price and the reverse DCF needs growth above the 8% framework. The scorecard keeps conviction at 3: hold at the current size, which is at the conviction-3 level; no add.",
  "price_at_decision": 171.32,
  "price_date": "2026-11-20",
  "research_note": "research/JKHY/2026-11-23.md",
  "triggers": [
    {"text": "TTM ROIC falls below 19%, the FY2024 trough, evidencing moat erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 19}},
    {"text": "TTM operating margin falls below 22%, under the FY2024 low of 22.1%, showing cloud/AI/security investment or renewal pricing is compressing profitability structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}},
    {"text": "TTM FCF margin falls below 20%, reversing the rising trend (TTM 27.6%).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Organic revenue growth (10-Q MD&A, ex-deconversion) turns negative, processing revenue growth falls below 5% for two consecutive quarters, or core client losses outnumber wins."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 205, "basis": "Guidance raises continue and P/E re-rates part way back toward its 5y median of 31.7x [RA], consistent with the P/E method's higher value; above the DCF bull of 137.26 because the DCF ignores the own-history multiple."},
    "base": {"probability": 0.5, "target_price_12m": 178, "basis": "Growth near the 8% framework (KBW transcript [OV]) with multiples steady at 23.5x P/E [RA]; above the DCF base of 125.12 because that model's cash-flow assumptions are harsher than the stock's own multiple history, as the P/E method of 230.66 shows."},
    "bear": {"probability": 0.25, "target_price_12m": 140, "basis": "Growth slows below the 12.4% the reverse DCF implies and the extended price de-rates toward the 5y P/E low of 19.5x [RA], between the DCF base of 125.12 and the current price."}
  },
  "entry_price": 106.35,
  "entry_basis": "valuation file: base 125.12 x 0.85."
}
```

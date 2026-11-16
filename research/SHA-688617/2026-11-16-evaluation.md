# Evaluation: APT Medical Inc. (SHA:688617) — 2026-11-16
## Bear case
The price already discounts exceptional growth: the reverse DCF needs 38.0% year-1 revenue growth, and even the mechanical bull fair value (261.96 CNY) sits below the 286.87 close [Certain]. Against peers it is far richer: P/E 39.6x vs a 28.1x peer median, EV/EBITDA 30.7x vs 17.2x [Certain]. The stock is extended, +22.8% above its 200-day average after +31.9% in three months [Certain]; if growth slows, a de-rating toward peer multiples would cut the price hard [Likely]. Revenue is China-only and procedure-linked, so national volume-based procurement could reprice catheters and erode the 72.8% gross margin [Likely]. ROIC is 7.6pp below three years ago, off the FY2023 peak of 64.4%, and cash conversion is lumpy (FY2024 FCF/NI 13.8%) [Certain]. The Q3 2026 filing was not read, so guidance is unverified [Certain].
## Bull case
This is a top-tier business that is working: TTM ROIC 57.4%, operating margin 36.4%, FCF margin 34.5%, all at their two-year highs and up on a year earlier [Certain]. The ROIC dip from FY2023 has reversed (+13.9pp over the last year), so the Direction change reads as a passing trough, not erosion [Likely]. Net cash, Altman Z 36.70, shares down 1.05% YoY [Certain]. Earnings growth outran the price: P/E, EV/EBITDA and P/FCF all sit below their 5-year minimum [Certain], and P/FCF 37.6x is below the 44.9x peer median [Certain]. Electrophysiology training and clinical adoption give a narrow moat [Guessing]. The 3.5% China premium likely depresses the DCF [Guessing].
## Decision
```json
{
  "ticker": "SHA:688617",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "Only 3-year ROIC is falling (-7.6pp from the FY2023 peak of 64.4%); over the last year ROIC rose +13.9pp to a 2-year high of 57.4% [RA-T] with operating and FCF margins also at 2-year highs [IS-T, CF-T], so the decline has already reversed.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "China volume-based procurement repricing EP catheters, which would compress the 72.8% gross margin and trigger a de-rating of an extended multiple (price +22.8% above its 200-day average, reverse DCF needs 38.0% growth).", "veto": null},
  "thesis": "A China electrophysiology device maker with exceptional and re-accelerating returns, but priced above even the mechanical bull fair value and at a wide premium to peers.",
  "rationale": "Quality and direction are excellent, but the price sits above the whole mechanical fair-value range and well above peer multiples; procurement-pricing risk on a China-only, extended stock makes it good but not compelling. Scorecard conviction 3: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 286.87,
  "price_date": "2026-11-13",
  "research_note": "research/SHA-688617/2026-11-16.md",
  "triggers": [
    {"text": "ROIC (ratios page, TTM) falls below 35%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 35}},
    {"text": "Operating margin (TTM) falls below 30%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "Gross margin (TTM) falls below 66%, a sign procurement pricing is eroding the moat", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 66}},
    {"text": "FCF conversion (FCF / net income, TTM) below 60% for two consecutive reporting periods"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 380, "basis": "Growth keeps outrunning the price and P/E re-rates toward its 5y median 53.6x [RA], above the mechanical bull 261.96 because the model's China premium and DCF miss the re-accelerating ROIC [RA-T]."},
    "base": {"probability": 0.45, "target_price_12m": 280, "basis": "P/E holds near the current 39.6x [RA] as margins stay at 2-year highs [IS-T]; above the mechanical base 158.85 because the stock has not traded near DCF value in 5 years (P/E 5y min 41.8x [RA])."},
    "bear": {"probability": 0.30, "target_price_12m": 200, "basis": "Procurement repricing or a growth slowdown de-rates P/E toward the 28.1x peer median [RA, P:SHE:300760]; held above the mechanical base 158.85 by net cash and 57.4% ROIC [RA]."}
  },
  "entry_price": 127.08,
  "entry_basis": "valuation file: base 158.85 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

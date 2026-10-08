# Evaluation: CoreWeave, Inc. (CRWV) — 2026-10-08
## Bear case
CoreWeave is a debt-funded GPU landlord whose returns do not cover its cost of capital: TTM ROCE -0.4%, net margin -25.4% and FCF margin -179.9% despite a 67.4% gross margin [Certain]. Net debt/EBITDA is 12.16x and the Altman Z of 0.29 sits in the distress zone [Certain]. Two customers make up 63% of H1 2026 revenue, so pricing power sits with the buyer [Certain]. Shares grew 75.59% YoY, and more equity issuance is likely while capex outruns operating cash flow [Likely]. At EV/Sales 12.2x and P/B 9.7x it trades at a premium to cash-rich hyperscaler peers that are building their own capacity [Certain]. The macro overlay (primary weight, moderate tilt toward bear) shows rising real yields (DFII10 2.91%) and HY spreads widening, which raises refinancing costs on a $35.1bn debt load [Likely]. No fair-value method can be computed [Certain].

## Bull case
The $103.7bn backlog gives multi-year revenue visibility, and operating cash flow was positive in H1 2026 [Certain]. If committed capacity finishes building and converts at today's gross margins, EBITDA growth could cut leverage from 12.16x quickly, as it did from 20.00x in FY2023 to 7.80x in FY2024 [Likely]. The stock is down 34.2% over 12 months, short interest is 16.73% and the price is near its 50-day average, so much of the bad news may already be priced [Likely]. New capacity such as the 240MW India project with AdaniConneX widens the customer base [Guessing]. A fall in real yields would re-rate long-duration AI infrastructure names [Guessing]. Even so, the bull case depends on financing and conversion that the fundamentals do not yet show [Likely].

## Decision
```json
{
  "ticker": "CRWV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A distress-zone, 12x-levered, FCF-negative GPU-rental business with 63% two-customer concentration trades at a premium to profitable hyperscaler peers, so neither the quality nor the valuation test of a core position is met.",
  "rationale": "The core test fails on both quality (negative ROCE, -179.9% FCF margin, Altman Z 0.29) and valuation (premium EV/Sales and P/B, no computable fair value). A primary macro headwind adds refinancing risk. The backlog is real, but conversion and deleveraging are still unproven. Conviction is 2, so no position; cash is acceptable.",
  "price_at_decision": 88.45,
  "price_date": "2026-10-07",
  "research_note": "research/CRWV/2026-10-08.md",
  "triggers": [
    {"text": "Leverage falls back to the FY2024 level: debt/EBITDA below 7.80x would show the backlog converting into EBITDA faster than debt grows.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 7.8}},
    {"text": "TTM operating margin recovers above the FY2024 level of 16.9%, showing depreciation and interest no longer erase gross profit.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 16.9}},
    {"text": "TTM FCF margin improves above the FY2025 level of -141.3%, showing capex intensity is easing as committed capacity comes online.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": -141.3}},
    {"text": "The top-two customer share of revenue (10-Q disclosure) falls well below the 63% seen in H1 2026 as a new large customer is added."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 117.49, "basis": "Backlog of $103.7bn converts at the 67.4% gross margin [IS] and leverage falls from 12.16x [RA], letting the stock retest its 117.49 August swing high [HI]; there is no mechanical fair value to reconcile with, because DCF and EV/Revenue are not computable (fact sheet Fair value)."},
    "base": {"probability": 0.42, "target_price_12m": 85.0, "basis": "Premium EV/Sales of 12.2x vs a 9.3x peer median [RA] erodes slightly while FCF margin stays deeply negative at -179.9% [CF,IS], leaving the price near its 88.33 50-day average [ST,HI]; probability shifted toward bear per the macro overlay's moderate bear tilt (research/CRWV/2026-10-08-macro.md)."},
    "bear": {"probability": 0.38, "target_price_12m": 60.55, "basis": "Rising real yields and HY spreads (research/CRWV/2026-10-08-macro.md, moderate bear tilt) make refinancing of the 12.16x-EBITDA debt load [RA] costlier and force more dilution after 75.59% share growth [ST], sending the stock back to its 60.55 52-week low [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

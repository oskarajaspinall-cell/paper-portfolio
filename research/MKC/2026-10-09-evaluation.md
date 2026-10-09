# Evaluation: McCormick & Company, Incorporated (MKC) — 2026-10-09

## Bear case
The 8.3x P/E is not real value: TTM net margin of 19.4% and ROE of 22.6% sit far above the FY21–25 ranges, so a one-off is inflating trailing EPS [Likely]. On EV/EBITDA, EV/Sales, P/FCF and P/B, MKC trades 34–53% above peers [Certain]. Returns are mediocre and sliding: ROIC fell from 9.8% to 8.9%, and gross margin from 39.7% to 38.9% [Certain]. Net debt/EBITDA is already 3.12x [Certain], ahead of a transformational, probably debt-funded Unilever Foods deal that the UK regulator is now investigating [Likely]. Real yields up 0.61pp in 3 months and a firmer dollar raise the cost of that financing and hurt FX translation (macro overlay, tilt toward bear, small) [Likely]. Short interest rose +20.3% to 6.0% of float [Certain]. The trend is weak: −30.0% over 12 months and 45.6pp behind SPY [Certain].

## Bull case
The price implies a −3.3% revenue decline, yet Q3 sales grew strongly and management reaffirmed its 2026 outlook [Likely]. The base fair value of $66.91 is +45.6% above the $45.94 close [Certain]. EV/EBITDA of 11.3x is below its 5-year minimum of 17.2x [Certain] for a category-leading spice franchise with a 0.64 beta [Certain]. FCF margin has risen to 12.0%, giving a 7.49% FCF yield [Certain], and leverage has fallen from 4.62x to 3.12x since FY2022 [Certain]. If Unilever Foods delivers the cited $600m synergy target, the earnings base could step up [Guessing]. A regulatory clearance would remove the main overhang [Guessing].

## Decision
```json
{
  "ticker": "MKC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A brand-leading spice franchise looks cheap only against its own rich history and a one-off-inflated trailing P/E, while returns and margins are eroding and leverage is set to rise into a regulator-scrutinised, transformational Unilever Foods deal.",
  "rationale": "The discount is to MKC's own past premium, not to peers: it still trades 34–53% above peers on EV/EBITDA, EV/Sales, P/FCF and P/B. ROIC and gross margin are drifting down, leverage is 3.12x before deal financing, and macro is a small headwind. Good but not compelling, so the answer is AVOID and no position.",
  "price_at_decision": 45.94,
  "price_date": "2026-10-08",
  "research_note": "research/MKC/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin climbs back above 40%, past the FY2021 level of 39.7%, showing pricing power is recovering rather than eroding.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 40}},
    {"text": "TTM ROIC rises above 10%, past the FY2021 five-year high of 9.8%, showing the returns erosion has reversed.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 10}},
    {"text": "Debt/EBITDA (statistics page) falls below 2.5x, showing any Unilever Foods financing has not stretched the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 2.5}},
    {"text": "The UK competition authority clears the Unilever Foods acquisition without material remedies, and the confirmed financing keeps net debt/EBITDA at or below 3.5x."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 62.0, "basis": "Q3 sales strength and the reaffirmed outlook [OV transcript] drive a partial re-rating toward the DCF base of $63.85 [fair value]. The target stays below the $108.23 bull fair value because the P/E leg rests on one-off-inflated TTM EPS (net margin 19.4% vs the 10.2–12.0% FY range [IS])."},
    "base": {"probability": 0.45, "target_price_12m": 50.0, "basis": "EV/EBITDA drifts modestly up from 11.3x but holds well below its 17.2x 5y minimum [RA] while the deal stays unresolved. The target sits below the $66.91 blended base because the P/E leg (73.01) uses inflated TTM earnings and MKC already trades 34% above the peer EV/EBITDA median [RA]. The macro overlay's small tilt toward bear (rising real yields, stronger dollar) also trims the range."},
    "bear": {"probability": 0.35, "target_price_12m": 36.0, "basis": "A debt-funded Unilever Foods deal pushes net debt/EBITDA above 3.5x from 3.12x [RA] while gross margin keeps eroding [IS], taking the price toward the $33.64 bear fair value. Probability was raised by the macro overlay's small tilt toward bear (real yields +0.61pp in 3m raise financing costs; research/MKC/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

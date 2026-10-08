# Evaluation: ResMed Inc. (RMD) — 2026-10-08
## Bear case
The cheapness is relative only to RMD's own richer past. At a 5.19% FCF yield and 21.7x P/E, RMD still trades at a premium to peers: +17% on P/E, +20% on EV/EBITDA [Certain] [ST, RA]. That is not a deep-value entry. FY2027 guidance was cut below expectations because ventilator sales were suspended and costs are under pressure (Reuters, 2026-08-07) [Likely]. Guided core growth is only mid-single-digit, so the stock lacks an obvious re-rating catalyst [Likely]. Short interest is 10.16% of float and rose 11.0% in a month [Certain] [ST], which suggests informed money sees the GLP-1 and device risks as unresolved [Guessing]. The stock has lagged SPY by 36.2pp over 12 months [Certain] [HI]. Q1 FY2027 results come on Oct 29, 2026 [Certain] [OV], and a second guidance disappointment would push the multiple toward its 5-year minimum of 18.5x P/E [Likely].
## Bull case
Quality is improving, not fading. ROIC is 26.2% (vs 22.0% in FY22), gross margin is 61.6% (+3.9pp) and operating margin is 34.0% (+6.0pp) [Certain] [RA, IS]. The balance sheet is net cash (-0.31x net debt/EBITDA) and FCF conversion is 108% [Certain] [BS, CF]. Every multiple sits in the bottom fifth of its 5-year range, with P/FCF at the 2nd percentile [Certain] [RA]. Masks and accessories give a recurring resupply stream on a large installed base [Likely]. Management says GLP-1 patients are adding to PAP therapy starts rather than replacing them [Likely] (Q4 2026 transcript). Shareholder returns are expanding: over $1.85bn guided for FY2027, including a $1.5bn buyback [Certain] (transcript). That supports per-share value without any re-rating [Likely]. A return toward the 27.5x median P/E would imply roughly 25%+ upside [Guessing].
## Decision
```json
{
  "ticker": "RMD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 26%-ROIC sleep-therapy franchise with expanding margins trades near the bottom of its own 5-year multiple range, but a 5.19% FCF yield, a premium to peers and a weak FY2027 growth outlook leave the upside good rather than compelling.",
  "rationale": "The business is excellent, but the de-rating looks deserved given mid-single-digit guided growth and the ventilator suspension. The FCF yield is modest against a peer premium, and rising short interest plus earnings on Oct 29 add event risk. That is conviction 3, below the buy threshold. Cash is preferable to a marginal Healthcare position next to ZTS.",
  "price_at_decision": 225.98,
  "price_date": "2026-10-07",
  "research_note": "research/RMD/2026-10-08.md",
  "triggers": [
    {"text": "Would turn more positive if TTM gross margin holds above 57% and ROIC stays above 20% through FY2027 while guided core growth is met; invalidation: TTM gross margin falls below 57%, reversing the FY22-FY26 expansion.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 57}},
    {"text": "TTM ROIC falls below 20%, giving up the five-year gain from 22.0%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below the FY2024 level of 29.5%, showing the supply-chain margin expansion has reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 29.5}},
    {"text": "Core revenue growth reported on the Q1 or Q2 FY2027 earnings call falls outside management's guided 5%-7% range."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 286, "basis": "Margin expansion continues and P/E re-rates from 21.7x to its 5y median of 27.5x [RA] on TTM earnings, as GLP-1 adds to the patient funnel (Q4 2026 transcript)."},
    "base": {"probability": 0.5, "target_price_12m": 232, "basis": "P/E holds near 21.7x [RA] while modest earnings growth and buybacks (shares -0.87% YoY [ST]) lift per-share value slightly."},
    "bear": {"probability": 0.25, "target_price_12m": 193, "basis": "A second guidance disappointment after the ventilator suspension (Reuters 2026-08-07 [OV]) pushes P/E to its 5y minimum of 18.5x [RA]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

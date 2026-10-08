# Evaluation: Newmont Corporation (NEM) — 2026-10-07
## Bear case
NEM's quality inflection is mostly gold-price beta, not a new cost structure [Likely]: operating margin went from 6.0% (FY23) to 55.2% TTM and ROIC from 2.5% to 27.9% (IS, RA) on spot-priced output with no differentiated pricing [Certain]. Today's price capitalises those peak margins: P/B 3.5x is above its 5y max of 3.2x and EV/Sales 4.6x sits at the 91st percentile, both rich versus peers (+13%/+29%) [Certain] (RA). The cheap-looking P/E (14.7x) and EV/EBITDA (6.9x) multiples rest on peak earnings, and P/E and P/FCF are still 13%/26% above peer medians [Certain]. The macro overlay flags real yields (DFII10 2.95%, +0.71pp 3m) and the dollar rising sharply against gold while the stock rallied +18.5% in 3m, a gap that a gold correction would close through high operating leverage [Likely] (research/NEM/2026-10-07-macro.md). A new CEO adds execution risk [Guessing].
## Bull case
The balance sheet is now net cash (net debt/EBITDA -0.20x TTM vs 2.10x FY23) and Piotroski F-score is 8 [Certain] (RA, ST), so a gold pullback does not threaten solvency. FCF margin of 37.8% and FCF/NI of 113.2% (CF, IS) fund large buybacks: shares are down 3.94% YoY [Certain] (ST), and management flagged a further buyback authorisation and dividend increase [Likely] (transcript). EV/EBITDA 6.9x sits at the 14th percentile of its 5y range and 7% below peers, and P/FCF 12.5x is below its 5y minimum [Certain] (RA), so the market already doubts that FCF will last. Tier-one, long-life assets and portfolio high-grading (the Northumberland sale) support durability [Likely]. Beta of 0.53 diversifies a portfolio tilted to equities [Certain] (ST).
## Decision
```json
{
  "ticker": "NEM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Newmont is a net-cash, tier-one gold producer, but its record returns are gold-price-driven and the price already capitalises peak margins (P/B above its 5y max, EV/Sales at the 91st percentile) just as real yields and the dollar turn against gold.",
  "rationale": "Quality metrics are cyclical, not structural; the valuation is mixed rather than attractive, with P/B and EV/Sales at or above 5y highs and premiums to peers on P/E and P/FCF. The macro overlay tilts moderately toward bear. Probability-weighted 12m value sits below the current price. Conviction 3 is below the buy threshold, so AVOID; cash is acceptable.",
  "price_at_decision": 116.39,
  "price_date": "2026-10-06",
  "research_note": "research/NEM/2026-10-07.md",
  "triggers": [
    {"text": "Q3 2026 or later results keep TTM operating margin above the current 55.2% despite the real-yield/dollar headwind, showing margins hold beyond the gold-price tailwind.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 55.2}},
    {"text": "TTM FCF margin rises above the current 37.8%, showing cash generation keeps compounding rather than peaking.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 37.8}},
    {"text": "Share count reduction accelerates beyond the current -3.94% YoY as the flagged buyback authorisation is executed from free cash flow.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": -3.94}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 135.29, "basis": "Gold holds as the real-yield/dollar rally stalls, so P/FCF re-rates from 12.5x to just above its 5y minimum of 14.2x [RA], which puts the price back at the 52-week high of 135.29 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 115.0, "basis": "Buyback accretion (shares -3.94% YoY [ST]) offsets a modest give-back from the 55.2% TTM operating margin [IS] with EV/EBITDA near 6.9x [RA]; flat, with the overlay's moderate bear tilt taking 0.05 off bull (research/NEM/2026-10-07-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 76.05, "basis": "Real yields and the dollar keep rising and gold corrects, so operating margin slides toward the FY2024 31.7% [IS] and P/B de-rates from above its 5y max of 3.2x [RA], back to the 52-week low of 76.05 [HI]; probability raised 0.05 per the overlay's moderate bear tilt (research/NEM/2026-10-07-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

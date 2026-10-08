# Evaluation: Ondas Inc. (ONDS) — 2026-10-08
## Bear case
Ondas is a structurally unprofitable roll-up. Operating margin has been negative in every fiscal year and is −121.0% TTM, and FCF margin is −98.7% [Certain] (IS, CF). The +96.2% TTM net margin comes alongside negative FCF conversion (−102.6%), which points to a one-off gain rather than a real inflection [Likely]. Growth is bought with stock: shares are up 297.32% YoY and 2026 acquisitions were paid mostly in equity [Certain] (ST; SEC 10-Q). Net debt/EBITDA is 7.44x, Altman Z is 1.79 and Piotroski F is 3 [Certain] (BS, ST). At 15.2x EV/Sales, the stock trades 132% above the peer median [Certain] (RA). Integrating five-plus acquisitions in two months adds execution risk [Likely]. Rising real yields and HY spreads make the next raise more costly [Likely] (macro overlay). Short interest is 44.45% and beta is 2.92 [Certain] (ST).
## Bull case
Order momentum is real. Ondas has announced over $270m of orders since June 30, and management raised full-year 2026 guidance on the Q2 call [Likely] (OV news; transcript /stocks/onds/transcripts/669130-q2-2026/). The defence pivot covers counter-UAS, ISR, precision strike and electronic safe-and-arm devices, with drone-import tariffs as a tailwind [Likely] (OV news). ROCE has improved from −58.6% in FY2024 to −7.4% TTM, and gross margin has recovered to 43.7% [Certain] (RA, IS). EV/Sales is at only the 12th percentile of its own 5-year range [Certain] (RA). With short interest at 44.45%, a margin inflection could force a sharp short squeeze [Guessing]. The stock is already down 37.1% over 12 months, so much of the dilution may be priced in [Likely] (ST).
## Decision
```json
{
  "ticker": "ONDS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "Ondas is building real defence order momentum, but it is a cash-burning, equity-funded roll-up at 15.2x EV/Sales with no fundamental valuation anchor, so it fails the good-business-at-an-attractive-price test.",
  "rationale": "This fails both core tests. Operating and FCF margins are deeply negative, dilution is 297% YoY, Altman Z is 1.79, and no fair-value method is computable to anchor the price. Order momentum is real but does not show in cash yet, and the macro overlay tilts toward bear. Conviction is 2, below the buy threshold, so AVOID with no position.",
  "price_at_decision": 7.19,
  "price_date": "2026-10-07",
  "research_note": "research/ONDS/2026-10-08.md",
  "triggers": [
    {"text": "TTM operating margin turns positive (from -121.0%), showing the order backlog converts into operating profit.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 0}},
    {"text": "TTM FCF margin turns positive (from -98.7%), showing the business is self-funding rather than reliant on share issuance.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 0}},
    {"text": "Shares-outstanding growth YoY falls below 10%, showing the equity-funded acquisition spree has stopped.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": 10}},
    {"text": "Piotroski F-Score rises materially from 3 alongside a positive operating margin for two consecutive quarters on the income statement."}
  ],
  "scenarios": {
    "bull": {"probability": 0.15, "target_price_12m": 14.16, "basis": "The >$270m in post-June orders and the raised FY2026 guide (OV news, Q2 transcript) start converting to margin, and the stock regains its 6-month high of 14.16 [HI]; the fact sheet has no fair value [data unavailable] because EBITDA and FCF are negative, so this target is a price-history anchor."},
    "base": {"probability": 0.40, "target_price_12m": 7.19, "basis": "P/B holds at its current 2.4x [RA] as revenue growth is offset by continued dilution (shares +297.32% YoY [ST]) and a -121.0% operating margin [IS]; the probability is shifted toward bear because of the macro overlay's moderate bear tilt (research/ONDS/2026-10-08-macro.md)."},
    "bear": {"probability": 0.45, "target_price_12m": 3.6, "basis": "P/B compresses from 2.4x to its 5y minimum of 1.2x [RA] as rising real yields and HY spreads (macro overlay, moderate bear tilt) worsen the terms of the next equity raise for a 7.44x net-debt/EBITDA, Altman Z 1.79 balance sheet [BS, ST]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

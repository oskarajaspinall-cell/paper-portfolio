# Evaluation: MMG Limited (HKG:1208) — 2026-11-08
## Bear case
MMG is a price-taker with no moat; returns are cyclical [Certain]: ROIC was 4.2% and 3.6% in FY2022-23 and is 20.3% TTM [RA]. The Direction change lines (operating margin 33.4% -> 42.6%, FCF margin 25.5% -> 31.9% over the last year, against falling 5-year trends) reflect metal prices and volume at a cyclical high, not a structural gain [Likely]. That makes the 3.4x EV/EBITDA and 22.62% FCF yield peak-earnings optics [Likely]. Fair value rests on EV/EBITDA alone because NAV is unavailable [Certain]. Peru (Las Bambas) and DRC political, royalty and blockade risk is unverified, not cleared (macro overlay) [Likely]. The macro overlay tilts small toward bear: VIX 28.18, HY spread widening, dollar up, with beta 1.56 [Certain]. The capital raise at a cyclical high diluted holders (shares up 3.43% YoY) [Certain]. The stock is down 25.9% in three months, and results on 2026-11-12 are a binary [Certain].

## Bull case
The balance sheet has been repaired: net debt/EBITDA is 0.16x against 3.44x in FY2022 [Certain]. ROIC, ROCE, operating and FCF margins are all at 2-year highs on rolling TTM [RA-T] [Certain], and H1 2026 was a record half per the call summary [Likely]. At 3.4x EV/EBITDA, below the 5y minimum of 4.1x and far under the 8.9x peer median, plus P/FCF of 4.4x, the market is already pricing a heavy normalisation [Likely]. September copper averaged above July (FRED, macro overlay), so the fall looks stock-specific rather than commodity-driven [Likely]. Base fair value of 8.13 sits above the price and bull 17.87 far above [Certain]. Piotroski F of 7 [Certain]. Lower cost guidance at Las Bambas, Khoemacau and Rosebery and growth at Kinsevere and Khoemacau support volumes [Likely].

## Decision
```json
{
  "ticker": "HKG:1208",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraged copper miner trading at a deep discount to peers, but on peak-cycle earnings with unverified Peru/DRC risk and no durable moat, so the discount is not yet compelling.",
  "rationale": "The new rolling data confirm a strong up-cycle, not a structural improvement; cheapness sits on peak EBITDA with a single valuation method. Country risk is unchecked, macro tilts small toward bear, and 2026-11-12 results are imminent. Good but not compelling: conviction stays 3, no upgrade to 4.",
  "price_at_decision": 6.83,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-1208/2026-11-08.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 25%: the up-cycle earnings power is gone", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}},
    {"text": "ROIC (TTM) falls below 10%: returns back to the FY2024-type range", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Debt/EBITDA rises above 2.0x: the deleveraging reverses", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "Shares change YoY exceeds 8%: further dilution erodes per-share value", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 11.96, "basis": "Copper holds and margins stay near 42.6% [IS-T], EV/EBITDA recovers toward its 5y median 6.3x [RA]; capped at the 52-week high [HI] rather than the 17.87 bull fair value, which capitalises peak EBITDA; probability trimmed for the small bear macro tilt (macro overlay)."},
    "base": {"probability": 0.45, "target_price_12m": 8.13, "basis": "Base EV/EBITDA fair value [IS,BS,CF,RA,ST,HI] as some normalisation of the 42.6% operating margin offsets a partial re-rating from 3.4x [RA]."},
    "bear": {"probability": 0.35, "target_price_12m": 5.18, "basis": "Bear fair value: copper softens in risk-off (VIX, HY spread and dollar all up, macro overlay small toward bear) and Peru/DRC disruption hits peak earnings; probability raised for the macro tilt and unverified country risk."}
  },
  "entry_price": 6.5,
  "entry_basis": "valuation file: base 8.13 x 0.8; at that level the discount would compensate for peak-earnings and unverified Peru/DRC risk, conditional on 2026-11-12 results not breaking a trigger.",
  "replaces": null,
  "replacement_reason": null
}
```

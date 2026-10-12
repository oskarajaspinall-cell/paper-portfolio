# Evaluation: Regency Centers Corporation (REG) — 2026-10-12
## Bear case
The discount is to REG's own history, not to peers: EV/EBITDA 17.2x vs a 17.0x peer median, P/E 24.3x vs 23.7x [Certain] (fact sheet RA, P:). The whole sector has de-rated, so the own-history P/FFO base fair value of 94.06 assumes rates go back down [Likely]. The official data point the other way: the 10y real yield rose 0.56pp in 3 months to 2.87% and the 10y Treasury is at 5.22% [Certain] (macro overlay, FRED). The overlay tilts moderately toward bear. Returns are only REIT-like, with ROIC flat at 5.4% [Certain] (RA). Net debt/EBITDA of 4.80x means higher refinancing costs eat into development spreads [Likely]. Momentum is negative: -9.3% over 3 months, -22.6pp vs SPY over 6 months, the 50-day average below the 200-day, and short interest up 8.5% [Certain] (HI, ST). The bear fair value of 71.75 sits at the current price, so the downside is not protected [Certain] (fact sheet).
## Bull case
Operations are at a record: about 97% leased, cash rent spreads above 10%, and FY guidance raised to mid-6% same-property NOI growth and more than 5% core FFO/share growth [Certain] (Q2 2026 transcript, https://stockanalysis.com/stocks/reg/transcripts/658187-q2-2026/). Grocery anchors in affluent trade areas and a development platform holding more than 20% share of US shopping-center development are durable advantages [Likely] (BofA transcript). The A-rated balance sheet is de-levering: net debt/EBITDA is 4.80x, falling, and the share count grew only 0.63% [Certain] (BS, IS, ST). EV/EBITDA and EV/Sales are below their 5-year minimums, and the base fair value of 94.06 is +30.6% above the price [Certain] (fact sheet). If real yields ease, the multiple re-rates while FFO keeps compounding [Likely].
## Decision
```json
{
  "ticker": "REG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, de-levering grocery-anchored REIT with record occupancy trades below its own 5-year multiples, but only in line with peers, so a re-rating depends on real yields that are still rising.",
  "rationale": "The fundamentals are strong, but the discount is sector-wide and driven by rates, not specific to REG. ROIC is REIT-like and the bear fair value sits at the price. The primary macro overlay tilts moderately toward bear while real yields keep rising. The expected return is good but not compelling, so conviction is 3: AVOID and hold cash.",
  "price_at_decision": 72.05,
  "price_date": "2026-10-09",
  "research_note": "research/REG/2026-10-12.md",
  "triggers": [
    {"text": "Net debt/EBITDA rises above 5.5x, the top of REG's own target range, eroding its balance-sheet cost-of-capital edge.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 5.5}},
    {"text": "TTM ROIC falls below 4.5%, under the 5-year low of 4.7%, showing development and leasing returns are deteriorating.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 4.5}},
    {"text": "Same-property NOI growth in the quarterly earnings release falls below 2% for two consecutive quarters, showing the leasing and escalator engine has stalled."},
    {"text": "Leased occupancy in the quarterly earnings release falls below 95%, reversing the record-occupancy trend."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 94.06, "basis": "Real yields ease (macro overlay macro_bull) and the multiple returns to its own-history P/FFO, reaching the fact sheet's base fair value of 94.06, close to the bull value of 95.39, with EV/EBITDA moving back toward its 5y median of 19.4x [RA]."},
    "base": {"probability": 0.4, "target_price_12m": 76.0, "basis": "The multiple stays at peer parity (EV/EBITDA 17.2x vs a 17.0x peer median [RA, P:]) while guided core FFO/share growth above 5% (Q2 2026 transcript) lifts the price modestly; this sits below the mechanical base of 94.06 because peers show the de-rating is sector-wide and rate-driven."},
    "bear": {"probability": 0.35, "target_price_12m": 64.0, "basis": "Real yields keep rising (DFII10 2.87%, +0.56pp/3m, macro overlay). The primary overlay's moderate tilt toward bear raises this probability, as the multiple compresses below the bear fair value of 71.75 and the 52-week low of 66.86 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The default anchor (base fair value 94.06 x 0.8) is already above the 72.05 price, and the bear fair value of 71.75 equals it. What holds conviction at 3 is a rising real-yield trend and a discount that only matches peers, so a lower price alone would not change the decision. A real-yield reversal (overlay refresh trigger DFII10 below 2.50%) would.",
  "replaces": null,
  "replacement_reason": null
}
```

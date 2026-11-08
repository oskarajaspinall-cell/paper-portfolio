# Evaluation: Zijin Gold International (HKG:2259) — 2026-11-07
## Bear case
This is a price-taker at what looks like peak margins: operating margin went from 20.3% in FY2023 to 56.6% TTM, and that is mostly the gold price, not a structural advantage [Likely]. The history covers FY2022-FY2025 only, with no gold downturn in it, so through-cycle returns are unproven [Certain]. Fair value can't be computed: NAV needs reserve data and the EV/EBITDA history is too short [Certain]. So there is no measurable margin of safety. Yet the stock trades at a premium of 24-38% to NEM, AEM, KGC and AU on every multiple (17.2x P/E vs 13.1x) [Certain]. It trades below its 200-day average, and over 52 weeks it has ranged from 84.20 to 268.00 [Certain]. Results are due Nov 13, right after a 14.6% jump [Certain]. The macro tilt is neutral: a firmer dollar and a VIX up 13.2 offset falling real yields [Likely].

## Bull case
The economics are excellent at current gold prices: ROIC is 44.2% TTM, the FCF margin was 33.6% in FY2025 and FCF/NI was 112.8% [Certain]. The balance sheet has moved from 0.58x net debt/EBITDA to net cash (-0.64x TTM), so growth has been self-funded [Certain]. The FCF yield is 6.60% [Certain]. Every quality metric has risen, and Piotroski F is 6 [Certain]. If real yields keep falling from 2.60%, gold could hold margins above 50% and support the multiple [Guessing]. The premium to peers may reflect a growth pipeline [Guessing]. But no reserve, production or cost data was available to verify that pipeline, so the bull case rests on the gold price rather than on company-specific evidence [Certain].

## Decision
```json
{
  "ticker": "HKG:2259",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A net-cash gold miner with 44.2% ROIC earns peak-like margins geared to the gold price, but it trades at a premium to established peers with no computable fair value and no reserve or cost data to show those margins will last.",
  "rationale": "The quality figures reflect the gold price more than a verified moat. The history has no downturn, fair value is unavailable, and the multiples are a premium to peers, so there is no margin of safety. Results on Nov 13 add event risk. Good but not compelling at conviction 2: AVOID, no position.",
  "price_at_decision": 136.50,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-2259/2026-11-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below 40%, showing the gold-price margin gains are reversing rather than structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}},
    {"text": "TTM ROIC falls below 20%, back toward FY2023 levels, undercutting the high-return case.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Debt/EBITDA on the statistics page rises above 1.0x, i.e. the net-cash position is lost through debt-funded expansion.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Positive: a primary company filing publishes reserve, production and all-in cost data showing a low-cost, long-life asset base, which would let a NAV be judged and could justify the premium to peers."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 175.50, "basis": "Margins hold above 50% as real yields fall from 2.60% (macro overlay, neutral small tilt, so the probability is unchanged), and the price retests its 6-month high of 175.50 [HI] while the premium to the 13.1x peer P/E [RA] persists."},
    "base": {"probability": 0.45, "target_price_12m": 136.50, "basis": "TTM operating margin of 56.6% [IS] flattens, and the stock stays near 17.2x P/E [RA] with no re-rating; fair value is unavailable, so there is no mechanical anchor to reconcile against."},
    "bear": {"probability": 0.30, "target_price_12m": 84.20, "basis": "The macro bear case (real yields above 2.9% and a firmer dollar, macro overlay) pushes margins back toward 40% and the multiple to the 13.1x peer median [RA], revisiting the 52-week low of 84.20 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "No fair value is computable (no NAV data, and the EV/EBITDA history is too short), and the obstacle is unverifiable through-cycle quality rather than price alone, so a lower price would not change the decision without reserve and cost data.",
  "replaces": null,
  "replacement_reason": null
}
```

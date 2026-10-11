# Evaluation: Kinross Gold Corporation (TSX:K) — 2026-10-11
## Bear case
Kinross's earnings are at a cyclical peak, not a new plateau: operating margin is 50.7% TTM against 5.1% in FY2021 [IS], and it has no pricing power over gold [Certain]. On normalized EBITDA the fact sheet's fair value is 18.04 CAD base and 14.50 CAD bear, 46.7%/57.2% below the 33.85 close [Certain]. So the P/E of 9.1x and EV/EBITDA of 4.9x are cheap only against peak earnings [Likely]. The macro overlay (primary weight) shows real yields up 0.56pp in 3 months and the dollar rising, with a moderate tilt toward bear [Likely]. Unit costs are rising too (AISC +13% YoY, note), so a lower gold price compresses margin from both sides [Likely]. Plaintiff-firm solicitations (Oct 1-8) add headline risk ahead of Q3 results on Oct 28 [Guessing]. Price trend is weak: -25.4% over 6 months and -16.9% vs the 200-day [Certain].
## Bull case
The balance sheet is net cash (net debt/EBITDA -0.35x [RA]), Altman Z is 6.54 and Piotroski F is 8 [Certain], so a down-cycle does not threaten solvency or force dilution [Likely]. FCF yield is 10.82% [ST], and shares fell 2.14% YoY through buybacks [Certain]. Multiples sit below their own 5y minimums and 27-34% below the peer median [Certain], so some of the gold headwind is likely priced in after the 6-month fall [Likely]. If real yields roll over, operating leverage is high and the bull fair value of 53.02 CAD is +56.6% away [Guessing].
## Decision
```json
{
  "ticker": "TSX:K",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A net-cash gold miner looks cheap on peak-cycle earnings, but on normalized EBITDA it trades well above base fair value while the primary macro driver (rising real yields and dollar) points against the gold price.",
  "rationale": "Low multiples reflect peak margins in a price-taking commodity business; normalized fair value (18.04 CAD base) is far below the close, real yields and the dollar are still rising, and AISC is inflating. The balance sheet limits downside but does not create an edge. Not a conviction-4 idea; cash is the better holding.",
  "price_at_decision": 33.85,
  "price_date": "2026-10-09",
  "research_note": "research/TSX-K/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin falls back below the FY2025 level of 44.1% [IS], showing earnings are normalizing; re-run the normalized valuation, since price and fair value may then converge.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 44.1}},
    {"text": "Share count shrinks more than 4% YoY (vs -2.14% now [ST]), showing capital returns are scaling into a durable shareholder-yield case.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": -4}},
    {"text": "An SEC filing discloses a specific securities claim or regulatory proceeding behind the Oct 2026 plaintiff-firm solicitations (thesis-negative), or confirms none exists."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 53.02, "basis": "Real yields and the dollar roll over and the gold price recovers, so peak EBITDA holds and the fact sheet's bull fair value of 53.02 CAD [IS,RA] is reached; probability trimmed because the macro overlay (research/TSX-K/2026-10-11-macro.md) tilts moderately toward bear."},
    "base": {"probability": 0.5, "target_price_12m": 33.85, "basis": "EV/EBITDA stays near 4.9x, around its 5y minimum of 5.0x [RA], while margin erosion from AISC inflation (note) is offset by buybacks (-2.14% shares [ST]); this sits above base fair value because the net-cash balance sheet (-0.35x net debt/EBITDA [RA]) and 10.82% FCF yield [ST] support the price near term."},
    "bear": {"probability": 0.3, "target_price_12m": 18.04, "basis": "Rising real yields and dollar push gold lower (macro overlay, moderate tilt toward bear, research/TSX-K/2026-10-11-macro.md), EBITDA reverts toward its 5y average and the stock re-prices to the fact sheet's base fair value of 18.04 CAD [IS,RA]; probability raised for the macro tilt."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: price alone is not the obstacle; the issue is cyclical peak earnings and a gold-price headwind, so a full re-research is needed when earnings normalize rather than at a fixed price.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Power Finance Corporation (NSE:PFC) — 2026-11-08
## Bear case
The cheapness cannot be tested. Operating margin, net margin, leverage and asset quality are all [data unavailable], so the stated value of a leveraged, state-directed power lender rests on a P/E figure alone [Certain]. TTM ROE of 18.7% sits below every fiscal year since FY2022 (20.5% in FY2026), so earnings power is softening even though the 5-year view reads "flat" [Certain]. The REC merger is approved but the swap-ratio dilution and integration terms are unresolved, and the government sets lending policy [Likely]. Piotroski F is 4 and FCF conversion was negative in FY2023-FY2026 [Certain]. Only P/E feeds the fair value. Its bear value of 169.27 is roughly half the price, the stock is 17.0% below its 200-day average, and momentum is negative against SPY [Certain]. The low P/E may just be a fair price for policy risk [Guessing].
## Bull case
At 4.1x earnings and 0.6x book, PFC trades below its own 5-year median P/E of 4.8x and at a deep discount to the peer median of 10.7x, while ROE has stayed around 20%-21.5% for five years [Certain]. Sovereign ownership, a specialised mandate and access to cheap funding (the USD note programme) form a structural moat, and absorbing REC removes the closest competitor [Likely]. Base fair value of 385.86 is above the 328.80 close, and the bull value of 474.52 implies a large re-rating if merger fears ease [Certain]. A 0.61 beta and a stable share count (0.01% YoY) limit the downside from dilution so far [Certain]. India's power-sector capex keeps loan growth visible [Guessing].
## Decision
```json
{
  "ticker": "NSE:PFC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A sovereign-backed power lender with steady ~20% ROE trades at 4.1x earnings and 0.6x book, but softening TTM ROE, unresolved REC-merger dilution and missing asset-quality data leave the discount unproven.",
  "rationale": "Cheap on P/E and P/B against its history and peers, but the valuation is P/E-only, asset quality and leverage are unavailable, TTM ROE is drifting below its fiscal-year range and merger terms are open. Expected value sits near the price with a deep bear case: good but not compelling, so no position.",
  "price_at_decision": 328.80,
  "price_date": "2026-11-06",
  "research_note": "research/NSE-PFC/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE falls below 15% (18.7% now), showing spread compression or credit costs are eroding earnings power.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 2.5% (2.9% now), showing funding costs are outrunning lending yields.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 2.5}},
    {"text": "Shares change YoY exceeds 5% from REC-merger issuance not matched by earnings growth.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}},
    {"text": "Piotroski F-score on the statistics page falls to 3 or below (4 now), signalling broad fundamental deterioration."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 474.52, "basis": "Merger closes on benign terms and P/E re-rates above its 5y median 4.8x toward the peer median 10.7x [RA]: the mechanical bull fair value of 474.52 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 350.0, "basis": "P/E recovers only partway toward its 5y median 4.8x [RA] because TTM ROE of 18.7% is below the FY2026 20.5% [RA]; set below the mechanical base 385.86 for softening ROE and unresolved REC swap dilution (research/NSE-PFC/2026-11-08.md)."},
    "bear": {"probability": 0.25, "target_price_12m": 169.27, "basis": "Credit costs or merger dilution push P/E toward its 5y low of 2.1x [RA]: the mechanical bear fair value of 169.27 [fact sheet Fair value]."}
  },
  "entry_price": 308.69,
  "entry_basis": "valuation file: base 385.86 x 0.8; at that level the margin of safety would offset the P/E-only valuation and unresolved merger terms.",
  "replaces": null,
  "replacement_reason": null
}
```

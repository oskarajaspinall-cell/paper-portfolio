# Evaluation: Copart, Inc. (CPRT) — 2026-10-08
## Bear case
Returns are eroding steadily, not cyclically: ROIC fell from 35.2% (FY2022) to 28.4% TTM, ROCE from 28.2% to 17.7% and operating margin from 39.3% to 35.4% while gross margin held flat, so fee or cost pressure is landing below the gross line [Certain] [RA, IS]. The 10-K concentration language makes insurer pricing pressure a plausible cause [Guessing]. The mechanical fair value base of 28.64 is only +7.6% above the 26.62 close, and the best-method DCF (15.99/20.36/22.23) sits below the price in every case [Certain]. The cash-funded ACV tender, repeatedly extended, moves Copart into whole-car auctions where it has no demonstrated moat and will consume the net-cash buffer [Likely]. Piotroski F of 4 and a -55.6pp 12-month lag versus SPY show no fundamental turn yet [Certain].
## Bull case
CPRT trades below its own 5-year minimum on every multiple: 17.2x P/E vs an 18.2x floor and 10.8x EV/EBITDA vs 12.3x [Certain] [RA]. The business still earns 28.4% ROIC, a 45.3% gross margin and a 27.2% FCF margin with rising 85.4% FCF conversion [Certain] [RA, CF]. Net debt/EBITDA of -2.36x and a -2.12% share count give balance-sheet and buyback support [Certain] [ST]. The insurance-salvage network (yards, VB3, long-dated insurer contracts) is costly to replicate [Likely]. If margins merely stabilise, EV/EBITDA reverting toward peers' 15.0x, let alone its 20.8x median, supports the 32.30 bull fair value [Likely].
## Decision
```json
{
  "ticker": "CPRT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, net-cash salvage-auction franchise trades below its 5-year multiple floor, but declining ROIC and operating margin plus a cash-funded move into whole-car auctions leave only modest, roughly symmetric upside to fair value.",
  "rationale": "Cheap versus its own history, but the fair-value base is only +7.6% above price, the DCF sits below price in all cases, and returns are still falling with the ACV deal unresolved. Good but not compelling: conviction 3, below the buy threshold. Revisit if margins and ROIC stabilise.",
  "price_at_decision": 26.62,
  "price_date": "2026-10-07",
  "research_note": "research/CPRT/2026-10-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 37%, back to the FY2024 level of 37.1%, showing the margin erosion was transitory rather than insurer fee pressure.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 37}},
    {"text": "TTM ROIC rises back above 31%, the FY2025 level of 31.6%, showing returns have stabilised after the ACV deal.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 31}},
    {"text": "A 10-K or 10-Q discloses the loss of a major insurance seller or fee concessions to large sellers, confirming structural pricing pressure (would harden the AVOID)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 32.30, "basis": "Margins stabilise and EV/EBITDA partially re-rates from 10.8x toward the 15.0x peer median [RA, P:KAR, P:RBA, P:KMX], matching the fact sheet's bull fair value of 32.30."},
    "base": {"probability": 0.45, "target_price_12m": 28.64, "basis": "Steady 27.2% FCF margin [CF, IS] with ROIC drifting near 28.4% [RA] supports the blended DCF/EV-EBITDA base fair value of 28.64, a modest +7.6% from the close."},
    "bear": {"probability": 0.30, "target_price_12m": 20.16, "basis": "Operating margin keeps falling from 35.4% [IS] and the cash ACV deal dilutes the 28.4% ROIC [RA], pulling value to the bear fair value of 20.16 where the DCF case (15.99-22.23) dominates."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

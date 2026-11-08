# Evaluation: CVC Capital Partners plc (AMS:CVC) — 2026-11-08
## Bear case
The cheapness is mostly a P/E illusion. On enterprise value, CVC trades in line with peers: EV/EBITDA 14.2x vs a 14.8x peer median and EV/Sales 8.5x vs 8.1x [Certain]. The 5y multiple ranges come from a short post-IPO history, so "below its 5y minimum" overstates value [Likely]. Earnings quality is uneven. The FY2025 net margin of 63.9% looks flattered, FCF/NI is 73.4% against 298.4% in FY2024, and Piotroski F is 3 [Certain]. The direction-change lines show operating margin 5.9pp below its 57.1% 2-year high and FCF margin 7.7pp below 43.0% [Certain]. That gap is driven by the timing of performance fees and realizations, and the macro overlay's risk-off move (VIX 28.18, HY spread +0.77 in 3 months) threatens exactly those [Likely]. The thesis holds only if exits continue. Guidance, the regional split and fee mix are unverified because the company site was blocked [Certain].

## Bull case
CVC is a high-return, asset-light manager: TTM ROIC 27.9%, operating margin 51.2% and FCF margin 35.3% [Certain]. All four rolling-12-month metrics are flat or rising: ROCE went from 18.9% to 20.6%, and operating and FCF margins are each up 2.5pp [Certain]. So the 5-year ROCE fall and the gap to the 2-year highs reflect FY2024's exceptional realizations, not erosion [Likely]. Leverage fell from 2.73x to 1.15x net debt/EBITDA [Certain]. At 18.7x P/E the stock sits 35% under the peer median, and P/FCF of 21.3x is 17% under peers [Certain]. The reverse DCF needs only 6.5% year-1 revenue growth. The H1 2026 call cited record realizations, strong fundraising and expansion in credit, secondaries and private wealth [Likely]. Insiders own 11.29%, which aligns management with shareholders [Certain].

## Decision
```json
{
  "ticker": "AMS:CVC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, deleveraging private-markets manager whose P/E discount to peers is real but whose EV-based multiples sit near peers, with exit-dependent earnings exposed to a fresh risk-off move and key operating data unverified.",
  "rationale": "Quality is strong and rolling returns are stable, but the value case rests on a P/E distorted by uneven earnings. EV/EBITDA and EV/Sales are near peers, the 5y ranges are short post-IPO history, the macro tilt hits performance fees, and guidance is unverified. The skew is good but not compelling, so AVOID with an entry price.",
  "price_at_decision": 14.46,
  "price_date": "2026-11-06",
  "research_note": "research/AMS-CVC/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 45% (51.2% now, 57.1% 2-year high), showing the fee base, not just performance-fee timing, is weakening.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 45}},
    {"text": "TTM ROIC falls below 20% (27.9% now), signalling the asset-light return profile is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA rises above 2.5x (1.15x TTM now), reversing the deleveraging from 2.73x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "TTM FCF margin falls below 28% (35.3% now), showing cash generation is deteriorating beyond realization timing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 28}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 22.0, "basis": "Realizations and fundraising continue as on the H1 2026 call (https://stockanalysis.com/quote/ams/CVC/transcripts/557778-h1-2026/) and P/E moves most of the way from 18.7x toward the 28.7x peer median [RA]; below the mechanical base of 25.01 because the 5y multiple history is short and post-IPO."},
    "base": {"probability": 0.45, "target_price_12m": 16.0, "basis": "Fees grow around the 6.5% the reverse DCF implies and P/FCF edges from 21.3x toward the 25.5x peer median [RA]; well below the mechanical base of 25.01 because that DCF extrapolates a lumpy, performance-fee-flattered margin (FY2025 net margin 63.9% [IS]); probability trimmed from an even split for the overlay's small toward-bear tilt (research/AMS-CVC/2026-11-08-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 9.5, "basis": "The macro bear (spreads above 4.5%, VIX above 25 for weeks; research/AMS-CVC/2026-11-08-macro.md) delays exits, performance fees and operating margin fall from 51.2% [IS-T], and P/E compresses toward its 12.8x 5y minimum [RA]; above the mechanical bear of 6.32 because recurring management fees cushion earnings; probability raised for the overlay's small bear tilt."}
  },
  "entry_price": 11.77,
  "entry_basis": "The default anchor (valuation file: base 25.01 x 0.8) sits above the price, so it can't serve. Use instead the 6-month low of 11.77 [HI] from the October risk-off: there the P/E discount to peers and the gap below base fair value would be wide enough to pay for the exit-cycle and earnings-quality uncertainty.",
  "replaces": null,
  "replacement_reason": null
}
```

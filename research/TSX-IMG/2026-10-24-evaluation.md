# Evaluation: IAMGOLD Corporation (TSX:IMG) — 2026-10-24
## Bear case
The quality turn is a gold-price and build-out story, not a moat: ROIC went from 0.0% in FY2023 to 30.5% TTM and gross margin from 12.6% to 50.3% as Côté Gold ramped into a high gold price [Certain]. A price-taker with one dominant asset and a 2.35 beta has no structural defence if gold falls [Likely]. The "cheap" 4.4x EV/EBITDA sits against a 5y history that was mostly a loss-making build phase, and it is in line with peers, so there is no relative discount [Certain]. The mechanical base fair value is 13.76 CAD against a 22.72 close, built on through-cycle EBITDA; Mine NAV is [data unavailable] [Certain]. The macro overlay tilts small toward bear: the 10y TIPS yield is up +0.21pp over ~3m and the dollar is firmer, both headwinds for gold, whose price is unverified [Likely]. Q3 results land Nov 5, 2026, a gap risk [Certain].

## Bull case
At current margins the cash engine is exceptional: a 17.30% FCF yield, P/FCF 5.8x versus a peer median of 19.0x, FCF conversion of 136.7% and net debt/EBITDA down from 5.08x to 0.02x [Certain]. Altman Z 5.46 and Piotroski F 8 confirm a clean balance sheet [Certain]. Côté Gold is a long-life Canadian asset, and management is prioritising optimisation and mine-life extension over M&A, limiting capital-allocation risk [Likely]. The stock is 16.1% below its 50-day average with RSI 32.3, so some gold-price risk is already in the price [Certain]. If real yields roll over or risk-off flows lift gold, margins expand further and the multiple can re-rate toward its 5y median of 10.0x [Guessing]. Dilution is mild at 1.16% a year [Certain].

## Decision
```json
{
  "ticker": "TSX:IMG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A newly deleveraged gold producer generating a 17.30% FCF yield from Côté Gold, but its returns are a peak-cycle function of an unverified gold price, it trades in line with peers and well above its through-cycle base fair value.",
  "rationale": "Cash generation and balance sheet are strong, but margins are cyclical and gold-driven, there is no discount to peers, price sits far above base fair value, macro tilts small toward bear and results arrive Nov 5. Good but not compelling: conviction 3, no position; re-research at a price that discounts cycle risk.",
  "price_at_decision": 22.72,
  "price_date": "2026-10-23",
  "research_note": "research/TSX-IMG/2026-10-24.md",
  "triggers": [
    {"text": "TTM gross margin falls below 35%, giving back most of the rise from 12.6% (FY2023) to 50.3%, showing the margin step-up was gold-price-driven rather than a structural cost advantage.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 35}},
    {"text": "TTM FCF margin falls below 20%, from 42.9%, showing Côté Gold cash generation is not durable.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA rises above 1.0x (0.01x now), signalling a return to debt-funded build-outs.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "TTM ROIC falls below 15%, from 30.5%, reversing the post-build-out returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 32.0, "basis": "Gold firms as real yields roll over (macro overlay bull) and EV/EBITDA re-rates from 4.4x toward its 5y median 10.0x [RA] only partially, taking the price back toward the 52-week high of 34.09 [HI]; below the mechanical bull 53.19 because peers also trade near 4.5x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 21.0, "basis": "EV/EBITDA stays near the peer median 4.5x [RA] on TTM EBITDA with margins roughly flat, a little below the close given the macro overlay's small bear tilt; above the mechanical base 13.76 because TTM cash generation (FCF yield 17.30% [ST]) is real while gold holds."},
    "bear": {"probability": 0.30, "target_price_12m": 12.0, "basis": "Rising real yields and a firmer dollar push gold lower (macro overlay, tilt toward bear, small, which raises this probability) and gross margin reverts toward the FY2024 33.7% [IS], taking value near the mechanical base 13.76 and above the bear 4.08 given the 0.02x net debt/EBITDA [BS,IS]."}
  },
  "entry_price": 11.01,
  "entry_basis": "valuation file: base 13.76 x 0.8; at that price the same cyclical evidence would carry a margin of safety on through-cycle EBITDA.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Greatland Resources Limited (ASX:GGP) — 2026-10-11
## Bear case
The cheapness is trailing. P/E 8.0x and EV/EBITDA 4.2x rest on FY2026, a record year with AISC of AUD 2,179/oz [Certain]. Management guides FY2027 to lower output (260-310koz vs 329koz) and AISC of AUD 2,933-3,330 [Certain], so forward EBITDA falls and the multiple is less cheap than it looks [Likely]. Heavy Havieron and Telfer growth capex has already cut the FCF margin from 44.3% to 34.7% [Certain]. GGP is an unhedged price-taker. The macro overlay (primary weight) flags US real yields up +0.56pp over 3 months and a firmer dollar, a moderate headwind for gold [Likely]. Shares rose 28.51% YoY [Certain]. The stock trades 17.7% below its 200-day average with the 50-day under the 200-day [Certain]. The mechanical fair value is EV/EBITDA on peak trailing EBITDA, and NAV data is unavailable [Certain], so the +63% upside is overstated [Likely].
## Bull case
Telfer is a large, under-used asset. Its mill runs at roughly 25% of capacity and the underground infrastructure is rated for 6Mt/yr against 1.3Mt processed today, so volume can grow at low marginal cost [Likely]. TTM ROIC is 85.8%, operating margin 52.2%, Altman Z 7.08 and Piotroski F 7 [Certain]. Liquidity of about AUD 1.8bn with zero debt funds the build-out without new equity [Certain]. Every multiple sits below its own 5-year minimum, and the stock trades at roughly half the peer median (EV/EBITDA 4.2x vs 8.4x, P/E 8.0x vs 19.6x) [Certain]. The FCF yield is 11.52% [Certain]. Even the mechanical bear fair value of AUD 11.71 is above the AUD 10.11 close [Certain]. If real yields roll over and Havieron delivers, both earnings and the multiple can re-rate toward peers [Guessing].
## Decision
```json
{
  "ticker": "ASX:GGP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-cost, net-cash gold-copper miner trades below its own 5-year multiple range and at half the peer EV/EBITDA, but the discount is on trailing earnings that the guided FY2027 output fall and AISC step-up will cut, while real yields are rising against gold.",
  "rationale": "The valuation discount is real but rests on peak trailing EBITDA. Guided FY2027 AISC of AUD 2,933-3,330 and lower output, heavy capex, 28.51% dilution and a moderate macro headwind for gold (primary overlay) leave the edge unclear. Earnings are due 2026-10-12. Good but not compelling, so conviction 3 means AVOID.",
  "price_at_decision": 10.11,
  "price_date": "2026-10-09",
  "research_note": "research/ASX-GGP/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROIC falls below 30%, showing the post-acquisition Telfer/Havieron returns were a one-off rather than a durable run-rate.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "TTM FCF margin falls below 15%, showing growth capex is structurally outrunning operating cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Debt/EBITDA rises above 1.0x, showing the AUD 500m facility is being drawn to fund capex beyond the cash buffer.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Reported AISC stays above AUD 3,000/oz beyond the guided FY2027 transition year (company quarterly reporting), or FY2027 production lands below the 260koz low end of guidance."}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 16.51, "basis": "EV/EBITDA re-rates to its 5y median of 7.7x [RA], toward the 8.4x peer median, as real yields roll over and FY2027 AISC lands at the low end of guidance; this equals the mechanical base fair value of 16.51 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 10.50, "basis": "The trailing 4.2x EV/EBITDA [RA] re-rates only modestly because guided FY2027 output of 260-310koz and AISC of AUD 2,933-3,330 (Q4 2026 transcript) cut EBITDA, so the target sits below the mechanical bear fair value of 11.71, which assumes trailing EBITDA holds."},
    "bear": {"probability": 0.35, "target_price_12m": 7.50, "basis": "With a moderate tilt toward bear per the macro overlay (research/ASX-GGP/2026-10-11-macro.md: DFII10 +0.56pp/3m, a firmer dollar), a softer gold price on top of the guided cost step-up compresses margins, the discount persists, and the price heads toward the 52-week low of 6.73 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. GGP already trades below its 5-year minimum on every multiple [RA]. What blocks conviction 4 is evidence still to come: FY2027 AISC and output delivery (results due 2026-10-12) and the direction of real yields and gold. A lower price would mainly reflect these risks playing out, not a better entry on the same evidence.",
  "replaces": null,
  "replacement_reason": null
}
```

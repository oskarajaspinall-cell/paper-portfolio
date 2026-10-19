# Evaluation: Vipshop Holdings Limited (VIPS) — 2026-10-19
## Bear case
The customer base is shrinking, not just growing slowly: Q2 2026 revenue fell 4.3% YoY and active customers fell to 42.3mn from 43.5mn [company-reported] (https://www.sec.gov/Archives/edgar/data/1529192/000110465926100484/tm2623972d1_ex99-1.htm) [Certain]. Headline cheapness is flattered: TTM net margin of 9.8% includes a one-off RMB5.79bn REIT listing gain [company-reported, same source], so the 4.2x P/E overstates run-rate value [Certain]. Quality is fading: ROIC fell from 55.4% (FY2023) to 22.8% TTM, FCF margin from 10.9% to 5.2%, FCF conversion from 150.9% to 75.5%, and Piotroski F is 4 [RA, CF, ST] [Certain]. On the less distorted cash measure, P/FCF of 8.7x sits mid-range and above peers [RA] [Certain]. PDD/Temu and Taobao markdowns contest the discount channel [Likely]. The price trend confirms it: below both moving averages, -45.9pp vs SPY over 12 months [HI] [Certain]. Cheap can stay cheap while the franchise erodes [Likely].
## Bull case
Net cash of 2.22x EBITDA and a 11.50% FCF yield fund heavy buybacks: shares fell 4.25% YoY and a new $1.0bn program was approved [ST; company-reported, SEC 6-K above] [Certain]. EV/EBITDA of 2.8x is below its 5y minimum of 3.3x and far below the 7.8x peer median [RA] [Certain]. The reverse DCF implies -18.6% year-1 revenue growth, much worse than the -4.3% just reported [company-reported], so even modest stabilisation would re-rate [Likely]. Gross margin is still near a five-year high at 23.4% [IS], suggesting the sourcing edge is intact [Likely]. Shan Shan outlets and SVIP are growing (Q2 2026 call headline [OV]) [Likely]. Base fair value is $20.31 against $12.86 [Certain], and low beta of 0.54 limits market-driven drawdowns [Certain].
## Decision
```json
{
  "ticker": "VIPS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, buyback-heavy off-price retailer trades below its own 5-year minimum EV/EBITDA, but a shrinking active-customer base, falling revenue and fading ROIC and cash conversion make it a value trap until the top line stabilises.",
  "rationale": "Cheap with strong cash returns, but quality is deteriorating: customers and revenue are falling, ROIC and FCF conversion are sliding, and TTM earnings are flattered by a one-off REIT gain. Good but not compelling; conviction 3 means no position. A lower price would not fix the obstacle, which is the customer trend.",
  "price_at_decision": 12.86,
  "price_date": "2026-10-16",
  "research_note": "research/VIPS/2026-10-19.md",
  "triggers": [
    {"text": "Active customers (SEC 6-K earnings release) return to year-on-year growth for two consecutive quarters, showing the customer erosion was cyclical rather than structural share loss."},
    {"text": "TTM gross margin falls below 22% (23.4% now), indicating the off-price sourcing edge is being competed away.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 22}},
    {"text": "TTM ROIC falls below 20% (22.8% now), confirming returns erosion continues beyond the FY2023 peak.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 19.07, "basis": "Revenue stabilises versus the -18.6% year-1 decline the reverse DCF implies [fact sheet Fair value] and EV/Sales returns to its 5y median 0.4x [RA], matching the EV/Revenue base value of 19.07; probability trimmed slightly for the overlay's small bear tilt from higher US yields (research/VIPS/2026-10-19-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 13.06, "basis": "Customers and revenue keep drifting down as in Q2 2026 [company-reported, SEC 6-K] while buybacks (shares -4.25% YoY [ST]) offset, leaving the stock near the mechanical bear fair value of 13.06 [fact sheet Fair value]; below the base fair value because that assumes a growth path the shrinking customer base does not support."},
    "bear": {"probability": 0.35, "target_price_12m": 10.5, "basis": "The one-off REIT gain drops out of TTM earnings [company-reported, SEC 6-K], FCF margin keeps falling from 5.2% [CF,IS] and P/B de-rates below its 5y minimum 1.1x [RA]; probability raised slightly for the overlay's small bear tilt, as higher US yields push the DCF bear value below price (research/VIPS/2026-10-19-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades far below base fair value less the margin of safety; the obstacle is the shrinking active-customer base and falling revenue, ROIC and FCF conversion, so a lower price would not change the decision until the customer trend stabilises.",
  "replaces": null,
  "replacement_reason": null
}
```

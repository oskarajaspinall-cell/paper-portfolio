# Evaluation: Albemarle Corporation (ALB) — 2026-10-12
## Bear case
ALB is a price-taker in a traded commodity with no pricing power, and Chinese converter oversupply caps margins even in upcycles [Likely]. Through-cycle returns are poor: ROIC fell 6.4pp over five years to 4.1% TTM, with FY2024 at -4.6% and >$726m of Energy Storage impairments [Certain]. The 8.9x P/FCF and 11.23% FCF yield flatter the business because TTM cash includes $525.2m of non-repeatable divestiture proceeds [Likely]. Shares rose 7.95% YoY, so owners funded the trough [Certain]. The mechanical bear fair value is negative (-18.19), so there is no valuation floor if lithium stays weak [Certain]. The macro overlay tilts moderately to bear: higher real yields, a stronger dollar and wider HY spreads weigh on USD commodity prices and on a back-loaded DCF [Likely]. Short interest is 9.45% and rising, and a new CEO only arrives on 2027-02-01 [Certain].
## Bull case
The price implies a -5.0% year-1 revenue decline. Base fair value is 184.89, +82.6% above the price [Certain]. EV/EBITDA of 8.3x is below its own 5y minimum of 9.7x [Certain]. H1 2026 deleveraging cut long-term debt from $3.119bn to $1.802bn, leaving $1.632bn of cash. Net debt/EBITDA is now 0.25x [Certain]. Margins are recovering off the trough: TTM gross margin is 24.0% against 1.6% in FY2024, and operating margin is 14.2% [Certain]. Low-cost Atacama brine and Greenbushes give a real cost edge for the next lithium upcycle [Likely]. Piotroski F of 7 confirms improving fundamentals [Certain]. Capex discipline (Kemerton halted) and a BHP mining CEO could lift through-cycle returns [Guessing].
## Decision
```json
{
  "ticker": "ALB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A low-cost lithium producer with a repaired balance sheet trades below its own 5y EV/EBITDA minimum, but returns depend on an uncertain commodity recovery that the business cannot control.",
  "rationale": "The upside depends on the lithium price, not on company execution. ROIC is 4.1% after five falling years and shares were diluted 7.95%. Trailing FCF is flattered by one-off divestiture cash, and the bear fair value is negative. Macro tilts toward the bear case. Cheapness alone is not conviction 4, so we stay in cash.",
  "price_at_decision": 101.27,
  "price_date": "2026-10-09",
  "research_note": "research/ALB/2026-10-12.md",
  "triggers": [
    {"text": "TTM gross margin rises above 30%, back to the FY2021 level, showing lithium pricing has recovered to a through-cycle level that supports a core thesis.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 30}},
    {"text": "TTM ROIC rises above 10%, showing the returns recovery is real and not only a balance-sheet repair.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 10}},
    {"text": "TTM operating margin rises above 20%, confirming the recovery carries through to operating profit and is not driven by one-offs.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 20}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 184.89, "basis": "Lithium reflation and a falling dollar/real yields (macro overlay bull path) lift margins further from the 24.0% TTM gross margin [IS], and the price reaches the blended base fair value of 184.89 (fact sheet Fair value)."},
    "base": {"probability": 0.45, "target_price_12m": 107.9, "basis": "Lithium stays range-bound and EV/EBITDA stays near 8.3x, below its 5y minimum of 9.7x [RA]. The price recovers only to the September swing low of 107.90 [HI], well below the DCF base of 132.00 because TTM FCF includes one-off divestiture cash (note section 2)."},
    "bear": {"probability": 0.35, "target_price_12m": 88.01, "basis": "The macro overlay's moderate bear tilt (research/ALB/2026-10-12-macro.md: higher real yields and a stronger dollar) moved probability from base to bear. Soft lithium sends the price back to the 52-week low of 88.01 [HI], below the EV/EBITDA bear fair value of 95.05, though above the negative DCF bear thanks to the 0.25x net debt/EBITDA [BS,IS]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is 2, so no entry price is set. Price is not the obstacle: the base fair value less 20% (184.89 x 0.8) is above the current price, and conviction is held back by commodity-driven returns and dilution. A lower price would not change the decision. Only the fundamental triggers above would.",
  "replaces": null,
  "replacement_reason": null
}
```

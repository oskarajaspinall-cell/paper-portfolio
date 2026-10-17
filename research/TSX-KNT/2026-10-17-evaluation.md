# Evaluation: K92 Mining Inc. (TSX:KNT) — 2026-10-17
## Bear case
The record margins come from metal prices, not a moat. Operating margin went from 27.0% in FY2023 to 67.2% TTM [Certain] [IS] while K92 stayed a price-taker on gold, copper and silver [Certain]. The mechanical EV/EBITDA fair value puts base at CAD14.57 and bear at CAD8.54, against a CAD27.35 close [Certain] [fact sheet]. The low P/E and EV/EBITDA percentiles only show that earnings ran ahead of the price; they are not a margin of safety [Likely]. Versus peers the stock is dear: EV/EBITDA 7.7x against a 4.1x peer median, P/B 4.9x against 1.9x [Certain] [RA]. The macro overlay finds real yields at 2.78% and the dollar both rising, a headwind for gold that is not yet priced [Likely] (macro overlay). All the cash flow comes from one mine in Papua New Guinea, a new CEO took over in August 2026, and FCF conversion is volatile at 49.9% TTM [Certain].
## Bull case
On the numbers, this is a top-tier operator. TTM ROIC is 55.7%, ROE 46.1%, the balance sheet is net cash (−0.53x net debt/EBITDA) and Piotroski F is 8 [Certain] [RA, ST]. Q3 brought record production and the 1 moz AuEq milestone, and Stage 3 is nearing completion on budget [Likely] (GlobeNewswire 2026-10-08 headline). Higher volumes could lift EBITDA even if metal prices are flat [Guessing]. P/E of 13.1x sits near its 5y low of 12.9x, and P/FCF of 26.2x is below its 5y minimum [Certain] [RA]. Growth so far has needed little dilution, with shares up only 1.21% YoY [Certain] [ST]. If real yields ease, the multiple could re-rate toward the 5y median EV/EBITDA of 13.3x [Guessing].
## Decision
```json
{
  "ticker": "TSX:KNT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "K92 is an exceptional high-grade, net-cash gold producer, but its record margins depend on metal prices that rising real yields and a firmer dollar now threaten, and the price sits far above the mechanical fair value.",
  "rationale": "Quality is outstanding, but earnings are metal-price driven, with a single asset, a new CEO and a moderately bearish macro tilt. The price is well above base fair value and at a large peer premium. That is good but not compelling, so I avoid and hold cash, re-checking at the entry price or if Stage 3 economics prove out.",
  "price_at_decision": 27.35,
  "price_date": "2026-10-16",
  "research_note": "research/TSX-KNT/2026-10-17.md",
  "triggers": [
    {"text": "Operating margin falls below 50% (from 67.2% TTM), signalling cost inflation or grade decline eroding the high-grade advantage", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 50}},
    {"text": "ROIC falls below 30% (from 55.7% TTM), showing the cost advantage no longer earns superior returns", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "Balance sheet turns net-debt-positive (net debt/EBITDA above zero from -0.53x TTM) as Stage 3/4 capex outruns operating cash flow"}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 40.0, "basis": "Stage 3 volumes lift TTM EBITDA [IS] and EV/EBITDA re-rates part-way toward its 5y median 13.3x [RA]; set below the mechanical bull CAD52.97 because single-asset PNG risk and a peer median of 4.1x cap the multiple."},
    "base": {"probability": 0.45, "target_price_12m": 25.0, "basis": "EV/EBITDA holds near today's 7.7x, close to its 5y low of 7.0x [RA], as volume growth roughly offsets a moderate metal-price headwind; probability shifted from bull to bear per the macro overlay's moderate tilt toward bear (research/TSX-KNT/2026-10-17-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 14.57, "basis": "Rising real yields and the dollar (macro overlay) pull metal prices and margins back toward the 5y average, and the price converges on the mechanical base fair value CAD14.57 (EV/EBITDA on normalised EBITDA, fact sheet)."}
  },
  "entry_price": 11.66,
  "entry_basis": "valuation file: base 14.57 x 0.8; at that price the market would be discounting normalised, not peak, metal-price earnings, which would justify conviction 4 on the same quality evidence.",
  "replaces": null,
  "replacement_reason": null
}
```

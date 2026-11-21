# Evaluation: T. Rowe Price Group (TROW) — 2026-11-21
## Bear case
TROW is losing client assets, not just riding a market dip: Q3 2026 net outflows of $28.3 billion, including target-date outflows of $6.5 billion [company-reported] (https://www.sec.gov/Archives/edgar/data/1113169/000111316926000005/trow-20260930.htm), October outflows continued, and management expects outflows to stay elevated [Certain]. The 12-month recovery in ROIC (19.3% -> 21.0%), operating margin (31.7% -> 34.2%) and FCF margin (16.2% -> 20.7%) came from markets lifting average AUM, not from organic growth [Likely]; with beta 1.45, a VIX at 28.44 and real yields up 0.53pp in 3 months (macro overlay), an equity drawdown would cut fees and margin together [Likely]. The 5-year fall from the FY2021 peak reflects active-to-passive share loss, which is structural [Likely]. Short interest of 13.01% (up 6.8%) shows a crowded bearish view; the price is below its 200-day average, so there is no trend support [Certain].
## Bull case
The price already discounts shrinkage: the reverse DCF implies -0.7% year-1 revenue growth, and P/E 10.2x and EV/EBITDA 6.1x sit below their 5-year minimums and 37% / 49% below peers [Certain]. Quality is high and improving on a rolling basis: TTM ROIC 21.0%, operating margin 34.2% at its 2-year high, FCF yield 7.42% [Certain]. The 5-year decline is measured from a market-driven FY2021 peak; current returns are back in the FY2024-25 range, so the last year is a recovery rather than a new leg down [Likely]. Net cash (net debt/EBITDA -0.96x) funds buybacks (shares -2.44% YoY) and the dividend [Certain]. ETF, SMA and fixed-income demand offsets part of the active-equity bleed [Likely]. Base fair value 120.41 sits well above the price, with the P/E method at 136.16 [Certain].
## Decision
```json
{
  "ticker": "TROW",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "The fact sheet shows ROIC, operating margin and FCF margin rising over the last 1 and 3 years (RA-T, IS-T, CF-T); the 5-year fall is measured from the market-driven FY2021 peak.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Persistent active-equity and target-date outflows compounding with an equity drawdown (beta 1.45, VIX rising) cut average AUM, fees and margin.",
    "veto": null
  },
  "thesis": "A net-cash, high-return asset manager trading below its own 5-year minimum P/E and EV/EBITDA prices in shrinkage, but persistent net outflows mean the cheapness depends on markets carrying AUM.",
  "rationale": "Scorecard total 8 gives conviction 3: high quality, net cash and below-history multiples, but the value blend sits just short of the next upside band, the price is below its 200-day average and persistent outflows keep key risk at medium. Only conviction 4+ is bought (owner rule), so AVOID.",
  "price_at_decision": 100.99,
  "price_date": "2026-11-20",
  "research_note": "research/TROW/2026-11-21.md",
  "triggers": [
    {"text": "TTM operating margin falls below 30%, showing outflows and fee pressure are overwhelming market-driven AUM gains.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 15%, under the FY2023 trough of 16.5%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 16%, back to the level of a year earlier.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 16}},
    {"text": "Quarterly net outflows worse than $40 billion, or quarter-end AUM below $1,700 billion, in the company's AUM releases."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 140, "basis": "Equities recover and outflows ease; P/E re-rates toward the P/E-method fair value of 136.16 and the 5y median 13.8x [RA] on TTM earnings, inside the mechanical bull of 164.73."},
    "base": {"probability": 0.45, "target_price_12m": 115, "basis": "Outflows continue but markets hold AUM; price moves toward the base fair value of 120.41, trimmed slightly for the macro overlay's small tilt toward bear (VIX and real-yield rise, research/TROW/2026-11-21-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 82, "basis": "An equity drawdown plus elevated outflows pushes AUM toward $1,700bn and margin below 34.2% (macro overlay bear); below the mechanical bear of 89.48 because the overlay tilts toward bear and lifts this probability."}
  },
  "entry_price": 100.0,
  "entry_basis": "Price is the obstacle: per the valuation file, the scorecard's value blend (base fair value 120.41 with the scenario expected value) reaches the next upside band just below the current close, taking the total to the buy line; base 120.41 x 0.85 sits above the price, so the scorecard re-score level is used instead."
}
```

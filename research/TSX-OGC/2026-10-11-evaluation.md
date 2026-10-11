# Evaluation: OceanaGold Corporation (TSX:OGC) — 2026-10-11

## Bear case
OGC is a price-taker: the jump in operating margin (21.8% FY2024 to 49.0% TTM) and ROIC (11.8% to 43.4%) comes mostly from the gold price, not from a lasting cost edge [Likely]. A P/E of 7.3x on peak earnings is a cyclical trap. The fair value, which normalises earnings, puts bear/base at 15.64/17.76 CAD, 55-60% below the 39.36 close, while bull adds only +18.9% [Certain]. The macro overlay marks real yields (DFII10 2.87%, +0.56pp/3m) and the dollar as rising together, the mix that hurts gold most, and tilts moderately toward bear [Likely]. Fixed mine costs mean a lower gold price cuts margin faster than revenue [Likely]. CEO Bond retires in April 2027 and NZ permits for Macraes Phase 4 are pending [Certain]; the proposed Ausgold deal adds integration or dilution risk [Likely]. The 50-day average sits 5.7% below the 200-day [Certain].

## Bull case
Even at peak, the cash is real. TTM FCF margin is 30.0%, FCF yield 11.97%, the balance sheet is net cash (-0.42x net debt/EBITDA) and the share count fell 4.21% YoY through buybacks [Certain]. EV/EBITDA of 3.9x is 53% below the peer median of 8.2x (AEM, KGC, EQX, NGD), and P/FCF of 8.4x is below its own 5y minimum [Certain]. Piotroski 7 and Altman Z 6.20 point to a sound balance sheet [Certain]. Management guides 520-590koz for 2026, with a path to 650koz from Waihi North, Katanning and exploration, so volume growth could offset part of any fall in gold [Likely]. If real yields stall, a re-rating toward peers could reach the bull fair value of 46.78 CAD [Guessing]. The peer discount may partly reflect jurisdiction (Philippines, NZ permitting), so some of it is justified [Likely].

## Decision
```json
{
  "ticker": "TSX:OGC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "OceanaGold's single-digit multiples sit on gold-price-driven peak margins, and with real yields and the dollar rising and through-cycle fair value 55-60% below the price, the cheapness is cyclical rather than a mispriced franchise.",
  "rationale": "Cash generation and the balance sheet are genuinely strong, but returns are a gold-price effect, not a moat. Base fair value of 17.76 CAD is far below 39.36, and the primary-weight macro overlay tilts moderately toward bear. Good but not compelling, so no position; cash is acceptable.",
  "price_at_decision": 39.36,
  "price_date": "2026-10-09",
  "research_note": "research/TSX-OGC/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15% from 43.4%, confirming the returns expansion was cyclical, not structural.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 30% from 49.0%, showing costs outrunning the gold price.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM FCF margin falls below 10% from 30.0%, ending the cash case for buybacks.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Debt/EBITDA rises above 1.0x, reversing the net-cash balance sheet (e.g. a debt-funded Ausgold deal or Waihi North build).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 46.78, "basis": "Real yields and the dollar reverse, gold holds and peak TTM EBITDA is sustained, reaching the fact sheet's bull EV/EBITDA fair value of 46.78 CAD [IS,RA]; probability trimmed for the macro overlay's moderate bear tilt (research/TSX-OGC/2026-10-11-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 39.36, "basis": "EV/EBITDA stays near 3.9x, close to its 5y median of 4.2x [RA]; buybacks (-4.21% shares [ST]) and guided 520-590koz output offset some margin give-back, leaving the price flat. This is above the mechanical base fair value because a full return to through-cycle earnings within 12 months is not assumed."},
    "bear": {"probability": 0.35, "target_price_12m": 17.76, "basis": "Rising real yields (DFII10 +0.56pp/3m) and the dollar push gold lower and margins normalise to through-cycle levels, matching the fact sheet's base EV/EBITDA fair value of 17.76 CAD [IS,RA]; probability raised for the macro overlay's moderate bear tilt (research/TSX-OGC/2026-10-11-macro.md)."}
  },
  "entry_price": 14.21,
  "entry_basis": "valuation file: base 17.76 x 0.8 (default margin of safety); at that level even through-cycle gold-price earnings would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

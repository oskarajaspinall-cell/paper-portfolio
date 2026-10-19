# Evaluation: Impala Platinum Holdings Limited (JSE:IMP) — 2026-10-19
## Bear case
Implats is a price-taker with no pricing power [Certain]: ROIC went from 37.2% (FY2022) to 1.6% (FY2024) and net margin from +27.1% to -20.0%, then back to 25.2%/23.0% TTM only on a higher PGM basket [Certain] (fact sheet RA, IS). A P/E of 5.5x on what may be near-peak earnings is the normal pattern for miners, not proof of cheapness [Likely]. The macro overlay tilts toward bear: the 10y real yield is 2.78%, up 0.43pp in 3 months, the broad dollar is up and fed funds were actually raised, all headwinds to USD PGM prices [Certain] (macro overlay, FRED). The stock is 20.8% below its 200-day average, with a 50-day below its 200-day [Certain] (HI, ST). Rustenburg fatalities and Eskom power risk remain [Likely] (note). No fair value can be computed [Certain], so the base case can't be anchored to a mechanical estimate.
## Bull case
The balance sheet is net cash across the whole cycle (net debt/EBITDA -0.51x TTM, never positive in 5 years) [Certain] (RA), with a Piotroski F of 7 and Altman Z of 5.25 [Certain] (ST). The FCF yield is 11.75%, and EV/EBITDA of 3.3x sits at the 3rd percentile of its 5y range and 35% below peers [Certain] (RA, ST). Management guided stable production and modest unit-cost inflation, and pays out most FCF under a rebased dividend framework [Likely] (note, H2 2026 transcript). A weaker rand partly offsets USD weakness [Guessing] (overlay). If real yields roll over, both the PGM price and the multiple could re-rate [Guessing].
## Decision
```json
{
  "ticker": "JSE:IMP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, low-multiple PGM producer whose value depends on whether today's PGM-price-driven margins last, a commodity call the evidence cannot make with high conviction.",
  "rationale": "The low multiples rest on cyclical TTM margins set by a PGM basket we cannot forecast. The macro overlay tilts slightly toward bear, and no fair value can be computed. The balance sheet and cash returns limit the downside, but this is good, not compelling. Conviction 3 means AVOID.",
  "price_at_decision": 18800.0,
  "price_date": "2026-10-16",
  "research_note": "research/JSE-IMP/2026-10-19.md",
  "triggers": [
    {"text": "Net margin falls back below 5%, showing the FY2026 recovery was a one-off price spike", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 5}},
    {"text": "FCF margin falls below 0%, as in FY2024, so cash no longer funds capex and dividends", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Operating margin holds above 25% through the FY2027 interim, which would show the margin is durable and could lift conviction", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 25}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 26300, "basis": "P/E re-rates from 5.5x to the 7.7x peer median [RA, P:JSE:AMS/SSW/NPH] on TTM earnings as real yields roll over (macro overlay macro_bull), close to the 6-month high of 27,998 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 19000, "basis": "EV/EBITDA stays near its 5y median of 3.4x [RA] on broadly stable production and modest cost inflation (note, H2 2026 transcript); no mechanical fair value is available to anchor it [Fair value section]."},
    "bear": {"probability": 0.30, "target_price_12m": 14000, "basis": "Bear weight raised by the small bear tilt in research/JSE-IMP/2026-10-19-macro.md (rising real yields and dollar): PGM prices fall and margins slide back toward FY2023's 20.2% operating margin [IS], so earnings drop and the stock trades below its 52-week low of 16,427 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades at the bottom of its own 5y multiple range [RA]. The open question is whether margins driven by the PGM price can last, and no fair value is computable to anchor a margin of safety. A lower price on the same evidence would not raise conviction to 4.",
  "replaces": null,
  "replacement_reason": null
}
```

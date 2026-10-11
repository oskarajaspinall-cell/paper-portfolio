# Evaluation: Intercontinental Exchange, Inc. (ICE) — 2026-10-11
## Bear case
The price already needs 14.6% year-1 revenue growth on the reverse DCF, and base fair value is $111.40, 28.7% below the $156.19 close [Certain]. Returns on capital are thin for a "moat" business: ROIC 8.6% TTM, below a cost of equity built on a 5.22% risk-free rate [Certain]. Leverage is still 2.90x net debt/EBITDA [Certain], and the announced MarketAxess deal could push it back up on undisclosed financing terms [Likely]. Rising real yields (10y TIPS 2.87%, +0.56pp/3m) raise the discount rate and weigh on Mortgage Technology origination volume [Likely]. The stock has lagged SPY by 17.7pp over 12 months [Certain], and the cheap multiples could stay cheap while rates stay high and the deal is unresolved [Guessing].

## Bull case
ICE is a capital-light infrastructure franchise: operating margin 52.4% TTM, FCF margin 48.1%, and FCF of 125.8% of net income [Certain]. It trades below its own 5-year EV/EBITDA minimum (16.0x vs 16.5x), at the bottom of its P/FCF range (17.3x vs 17.2x), and 32% below peers on P/FCF [Certain]. Deleveraging from 4.51x to 2.90x shows cash flows paying down acquisition debt [Certain]. New products (London gold futures, freight contracts, the OKX tokenization JV) add growth options in Exchanges [Likely]. If P/FCF goes back to its 21.5x 5-year median, the shares reach roughly the DCF bull value of $199.95 [Likely].

## Decision
```json
{
  "ticker": "ICE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-margin, cash-generative exchange and data franchise trades at the bottom of its own 5-year multiple range, but modest 8.6% ROIC, 2.90x leverage, an unquantified MarketAxess deal and a price already above base DCF fair value leave no margin of safety.",
  "rationale": "The business is high quality and cheap against its own history, but the price already sits 28.7% above base DCF value, ROIC is modest, MarketAxess financing is unknown and the macro tilt is moderately toward bear. Expected 12-month return is low single digits. That is good but not compelling, so conviction is 3 and the decision is AVOID.",
  "price_at_decision": 156.19,
  "price_date": "2026-10-09",
  "research_note": "research/ICE/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROIC rises above 10%, showing returns are clearing the cost of capital rather than drifting at the 7-8.6% five-year range.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 10}},
    {"text": "TTM operating margin falls below 47%, under the FY2024 five-year low of 47.7%, which would confirm the avoid on deteriorating franchise economics.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 47}},
    {"text": "TTM FCF margin falls below 41%, under the FY2021 five-year low of 41.2%, signalling cash-generation quality is eroding.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 41}},
    {"text": "ICE discloses MarketAxess financing terms (SEC filing or ice.com) that keep pro-forma net debt/EBITDA at or below the current 2.90x, removing the leverage overhang."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 194.0, "basis": "P/FCF re-rates from 17.3x to its 21.5x 5y median [RA] on steady 48.1% FCF margin [CF,IS], close to the $199.95 DCF bull value in the fact sheet."},
    "base": {"probability": 0.45, "target_price_12m": 160.0, "basis": "Multiples stay near the bottom of the 5y range (P/E 22.1x, EV/EBITDA 16.0x [RA]) while FCF and buybacks (-0.95% shares [ST]) add a few percent; this sits above the $111.40 DCF base because own-history and peer multiples (P/FCF 32% below peers) do not support the DCF's discount, but rising real yields cap any re-rating (macro overlay research/ICE/2026-10-11-macro.md, moderate bear tilt)."},
    "bear": {"probability": 0.30, "target_price_12m": 134.0, "basis": "P/E compresses from 22.1x to its 19.0x 5y minimum [RA] as yields rise and MarketAxess financing re-levers the balance sheet from 2.90x net debt/EBITDA [BS,IS]; the macro overlay's moderate bear tilt (research/ICE/2026-10-11-macro.md) raises this probability from 0.25 to 0.30, and the $111.40 DCF base marks further tail risk."}
  },
  "entry_price": 125.0,
  "entry_basis": "P/E back near its 5y minimum of 19.0x [RA] combined with the 6-month low of 121.79 [HI], at about $125, would give a margin of safety against the bear case. The default base fair value x 0.8 ($89.12) is not used, because own-history multiples show the DCF understates this franchise.",
  "replaces": null,
  "replacement_reason": null
}
```

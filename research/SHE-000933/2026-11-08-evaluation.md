# Evaluation: Henan Shenhuo Coal Industry and Electricity Power Co. Ltd (SHE:000933) — 2026-11-08
## Bear case
The Direction change lines (ROIC 13.0% -> 32.6%, operating margin 15.8% -> 29.8%, FCF margin 17.7% -> 25.8% over 12 months [RA-T, IS-T, CF-T]) are a commodity-spread upswing, not a better business: TTM sits above every fiscal year shown and the five-year FY trend is falling (ROIC -7.5pp, gross margin -12.4pp) [Certain]. Shenhuo is a price-taker in globally priced aluminum with a cost-only moat [Likely], so a reversal in the spread takes these margins back towards FY2024 levels (ROIC 12.6%, operating margin 15.6%) [Likely]. The price fell 20.4% over six months while TTM profit rose, and Q3 results drew no reaction: the market is already discounting a peak [Likely]. The through-cycle DCF base (70.19) capitalises that peak; the EV/EBITDA leg (26.18) sits almost at the price [Certain]. Insiders own 0.08% and shares rose 0.34% YoY: weak alignment, no buyback [Certain]. China policy risk is carried by the 3.5% premium [Certain].
## Bull case
Even on a cyclical reading the stock is cheap: EV/EBITDA 3.6x sits at 9% of its 5y range and below the 4.3x peer median, FCF yield is 21.96% and P/FCF 4.6x [Certain]. Profits are cash-backed: FCF conversion has stayed above 100% every year (154.8% TTM) [Certain]. The balance sheet has moved from 1.57x net debt/EBITDA (FY2024) to net cash (-0.20x), with Piotroski F 8 and Altman Z 3.79, so the downturn would be survivable and cash can accumulate [Certain]. Captive coal and power dampen cost volatility versus non-integrated smelters [Likely]. The mechanical bear fair value (28.92) is above the 25.26 close and the reverse DCF implies a -23.3% revenue fall in year 1 [Certain], so much of the normalisation may already be priced [Likely]. Macro is context only: the yuan barely moved (macro overlay) [Likely].
## Decision
```json
{
  "ticker": "SHE:000933",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, cash-generative integrated aluminum producer on low multiples, but the TTM surge in returns is peak-spread evidence and the upside rests on an unproven through-cycle normalisation.",
  "rationale": "Cheap and financially strong, but the 12-month jump in ROIC and margins is cyclical, the price is already discounting a fall, and the EV/EBITDA leg gives little upside. Good but not compelling; the new Recent direction inputs confirm a peak rather than a structural step-up, so conviction stays 3.",
  "price_at_decision": 25.26,
  "price_date": "2026-11-06",
  "research_note": "research/SHE-000933/2026-11-08.md",
  "triggers": [
    {"text": "ROIC falls below 10% (ratios/statistics page), showing the cycle has turned and the cost advantage does not hold returns", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 1.5x, eroding the balance-sheet cushion", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Gross margin falls below 20%, below the FY2024 trough area", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 20}},
    {"text": "FCF conversion (FCF/NI) below 100% for a full fiscal year (cash flow and income statement)"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 35.42, "basis": "Spread holds and the market accepts part of the normalised cash flow: price reaches the through-cycle DCF bear value 35.42 [IS,CF,RA], below the 70.19 DCF base because that base capitalises peak TTM margins (note section 3)."},
    "base": {"probability": 0.45, "target_price_12m": 26.18, "basis": "EV/EBITDA leg base 26.18 on the mechanical multiple [RA]; well below the blended base fair value 55.52 because the DCF leg rests on peak TTM ROIC 32.6% [RA-T] that the five-year falling trend does not support."},
    "bear": {"probability": 0.30, "target_price_12m": 15.90, "basis": "Aluminum spread reverses and margins revert towards FY2024 (operating margin 15.6% [IS]), matching the EV/EBITDA bear value 15.90 [RA]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: at EV/EBITDA 3.6x, 9% of its 5y range [RA], the stock is already cheap; the obstacle is whether peak-cycle TTM earnings are sustainable, which a lower price would not resolve. Evidence of margins holding through a weaker aluminum spread would.",
  "replaces": null,
  "replacement_reason": null
}
```

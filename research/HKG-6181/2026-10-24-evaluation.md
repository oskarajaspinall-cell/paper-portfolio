# Evaluation: Laopu Gold Co., Ltd. (HKG:6181) — 2026-10-24
## Bear case
The 6.3x P/E rests on earnings that are not turning into cash: FCF margin -8.0% TTM after -25.6% in FY2025, and FCF/NI -143.7% in FY2025 [Certain]. Growth in stock and stores absorbs all profit, and in gold jewellery stock carries gold-price risk [Likely]. Gross margin fell from 41.2% in FY2024 to 37.6% in FY2025, a sign that pricing power may be weaker than the brand story says [Guessing]. Piotroski F of 3 and 3.72% annual dilution point to weakening fundamentals and a cost to holders [Certain]. The stock is down 59.6% in 12 months and closed near its 52-week low of 274.00; nobody has explained the cause, and the H1 2026 results were not read [Certain]. The mechanical base fair value of 229.07 HKD is below the price, so the cheap multiple may simply be pricing in an earnings peak [Likely].

## Bull case
Returns are exceptional and still rising: TTM ROIC 39.9%, ROCE 68.5%, operating margin 26.4%, up from 12.7% in FY2021 [Certain]. The de-rating is extreme: P/E 6.3x against a 5y minimum of 20.1x, and EV/EBITDA 5.0x against 6.4x for peers [Certain]. Leverage is modest at 0.47x net debt/EBITDA and Altman Z is 9.85, so the balance sheet can carry the growth phase [Certain]. If expansion slows, the high-ROIC reinvestment should turn into strong free cash flow [Likely]. Gross margin recovered to 39.5% TTM [Certain]. Expansion in Hong Kong suggests management is still investing for growth [Likely].

## Decision
```json
{
  "ticker": "HKG:6181",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A very high-ROIC gold-jewellery brand trades far below its own multiple history, but its earnings are not converting to cash and the price sits above the mechanical base fair value.",
  "rationale": "Returns and the de-rating are striking, but negative FCF for three years, a Piotroski F of 3, dilution and an unexplained 59.6% collapse leave the cheap P/E unbacked by cash. The price is above base fair value, so there is no margin of safety. Good but not compelling: AVOID.",
  "price_at_decision": 284.60,
  "price_date": "2026-10-23",
  "research_note": "research/HKG-6181/2026-10-24.md",
  "triggers": [
    {"text": "TTM gross margin falls below 35%, under the FY2025 low of 37.6%, signalling loss of brand pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 35}},
    {"text": "TTM ROIC falls below 25%, giving up most of the rise from 14.0% in FY2021 to 39.9%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "TTM FCF margin falls below -15%, showing cash burn is deepening again rather than turning positive.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": -15}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.47x TTM now), showing the growth is being funded with debt.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 400.00, "basis": "FCF turns positive and P/E re-rates partway toward the 11.5x peer median [RA,P]; well below the 1,192.09 mechanical bull, which assumes a return toward the 20.1x-25.9x own-history range that negative FCF does not justify."},
    "base": {"probability": 0.45, "target_price_12m": 250.00, "basis": "Earnings ease from a peak and cash conversion stays weak, so the price settles close to the 229.07 P/E base fair value [IS,RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 200.30, "basis": "Gross margin falls further from 39.5% and FCF stays negative (FCF/NI -40.5% TTM [CF,IS]), in line with the P/E bear fair value of 200.30."}
  },
  "entry_price": 183.26,
  "entry_basis": "valuation file: base 229.07 x 0.8; a re-research there must also confirm cash conversion is improving.",
  "replaces": null,
  "replacement_reason": null
}
```

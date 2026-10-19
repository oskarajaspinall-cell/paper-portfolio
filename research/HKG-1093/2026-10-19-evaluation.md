# Evaluation: CSPC Pharmaceutical Group Limited (HKG:1093) — 2026-10-19

## Bear case
Every fiscal-year quality line has fallen for five years: ROIC from 34.9% to 12.8%, gross margin from 75.8% to 65.6%, operating margin from 22.4% to 15.2% [RA, IS] [Certain]. That is the signature of volume-based procurement eroding the legacy generics base [Likely]. The cheapness rests on TTM figures that look one-off: TTM net margin 23.7% and FCF margin 38.3% against FY2025's 14.9% and 14.9%, and FCF/NI of 161.7%, coincide with two 2026 AstraZeneca licensing deals [IS, CF] [Likely]. If upfronts roll off, the 11.8x P/E and 7.3x P/FCF are flattering, and the mechanical DCF base (HKD12.12) is built on non-recurring cash [Guessing]. The mechanical bear of HKD5.38 sits well below the price [Certain]. Relative strength is weak (-17.2pp vs SPY over 12 months) [HI] [Certain], and Q3 results on Nov 17, 2026 could reset earnings [Likely].

## Bull case
CSPC is net cash every year for five years (net debt/EBITDA -1.80x TTM) and is shrinking its share count (-1.02% YoY) [BS, ST] [Certain]. Even on depressed numbers it trades at a 60% P/E discount to peers (29.5x median) and 45% below on EV/EBITDA [RA] [Certain]; the reverse DCF implies a -11.7% year-1 revenue decline [Certain]. Two AstraZeneca deals in 2026 validate the innovative pipeline, making licensing a repeatable revenue stream rather than a one-off [Likely]. High insider ownership (26.50%) aligns management [ST] [Certain]. If even part of the TTM margin step-up proves recurring, FCF yield of 13.68% supports a re-rating toward base fair value of HKD12.12 [Guessing]. Low beta (0.71) and macro insensitivity (overlay: context) limit drawdown from rates [Likely].

## Decision
```json
{
  "ticker": "HKG:1093",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash Chinese drugmaker optically cheap on TTM figures that are likely inflated by AstraZeneca licensing upfronts, while its recurring generics business has seen five years of falling returns and margins.",
  "rationale": "Valuation looks compelling only on TTM numbers that probably include non-recurring licensing income; fiscal-year ROIC, gross and operating margins have fallen steadily for five years. Good but not compelling: until Q3 results show how much of the margin step-up is recurring, conviction is 3, which the owner rule makes an AVOID.",
  "price_at_decision": 8.88,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-1093/2026-10-19.md",
  "triggers": [
    {"text": "Results on or after Nov 17, 2026 show TTM operating margin holding near 27.9% with licensing upfronts a minority of profit, confirming recurring earnings power (would raise conviction)."},
    {"text": "TTM ROIC falls below 10%, extending the slide past FY2025's 12.8% and confirming the generics base is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM gross margin falls below 60%, extending the five-year slide past FY2025's 65.6%.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 60}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 12.12, "basis": "TTM FCF margin of 38.3% [CF,IS] proves largely recurring as licensing repeats, so the price reaches the mechanical base fair value of HKD12.12 (DCF blend) [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 9.14, "basis": "Licensing income partly normalises toward FY2025 net margin of 14.9% [IS]; the stock trades around the P/E-method bear value of HKD9.14 [fact sheet Fair value], near its 5y-low P/E of 12.0x [RA]."},
    "bear": {"probability": 0.3, "target_price_12m": 5.38, "basis": "Upfronts roll off and procurement pressure continues the five-year ROIC slide (-22.2pp) [RA], taking the price to the mechanical bear fair value of HKD5.38 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the default (base 12.12 x 0.8) is already above the price, and the open question is whether TTM earnings are recurring after the licensing upfronts; the Nov 17, 2026 results, not a lower price, resolve it.",
  "replaces": null,
  "replacement_reason": null
}
```

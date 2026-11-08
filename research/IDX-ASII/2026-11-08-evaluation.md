# Evaluation: PT Astra International Tbk (IDX:ASII) — 2026-11-08
## Bear case
Returns are falling now, not just cyclically low. The fact sheet's Direction change lines show TTM ROIC down from 10.1% to 8.0% and ROCE from 11.7% to 9.7% in a year, with operating margin at 11.1% against a 2-year high of 14.1% [RA-T, IS-T] [Certain]. The 5-year "flat/rising" reading rests on a weak FY2021 base, so the thesis-relevant trend is down [Certain]. Leverage rose while returns fell: net debt/EBITDA went from 0.16x in FY2022 to 1.23x [BS,IS], so new capital earns less [Likely]. The driver can't be pinned down because segment profits are [data unavailable], which also leaves SOTP blank [Certain]. The DCF base rests on a cyclical, declining-return business and is unreliable [Likely]. The business is wholly Indonesian, so EM risk-premium pressure (VIX 28.18, firmer dollar; macro overlay, context only) adds to it [Likely]. Altman Z 2.15 and Piotroski F 5 are middling [Certain].
## Bull case
The price already discounts a lot of decline. P/E is 6.7x against a 5y median of 8.0x and a peer median of 10.6x. P/B is 0.7x, below its 5y minimum, and the FCF yield is 13.21% [RA,ST] [Certain]. The reverse DCF implies -12.9% revenue growth in year 1, a harsher path than a diversified domestic franchise has shown [Likely]. Cash backs earnings: FCF conversion is 87.7% and the FCF margin of 8.1% is flat over the last 12 months [CF-T] [Certain]. Shares fell 1.17% YoY [ST] [Certain]. Leverage of 1.23x is moderate [Certain]. If the cycle turns, ROE and multiples could both recover from depressed levels [Guessing]. The price has bounced from the 3,920.00 low to above its 50-day average [HI] [Certain], but that does nothing for the business case.
## Decision
```json
{
  "ticker": "IDX:ASII",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A diversified Indonesian conglomerate trades below its own 5-year P/B floor at a 13.21% FCF yield, but ROIC, ROCE and operating margin are all falling over the last 12 months while leverage rises, leaving a value-trap risk the missing segment data cannot rule out.",
  "rationale": "Valuation is deeply cheap, but the owner rule buys quality on a stable or improving trend, and here every return metric fell over the last year as net debt rose. No segment data is available to show the decline is cyclical. Good but not compelling: AVOID until returns stop falling.",
  "price_at_decision": 5000.0,
  "price_date": "2026-11-06",
  "research_note": "research/IDX-ASII/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC recovers above 10.1% (its level a year earlier; 8.0% now), showing the return decline has reversed rather than continuing.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 10.1}},
    {"text": "TTM operating margin recovers above 12.7% (a year earlier; 11.1% now), showing margins track back toward the 2-year high of 14.1%.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 12.7}},
    {"text": "Net debt/EBITDA falls back below 1.0x (1.23x TTM now), showing leverage is no longer rising while returns fall.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 6400, "basis": "Returns stabilise and P/B re-rates from 0.7x toward its 5y median 0.9x [RA]. This sits far below the mechanical DCF bull of 24,959.99 because that DCF extrapolates a business whose ROIC is falling [RA-T]."},
    "base": {"probability": 0.45, "target_price_12m": 5300, "basis": "ROIC drifts near 8.0% [RA-T] and P/E edges from 6.7x toward but not to its 5y median 8.0x [RA] on lower earnings. This is well below the mechanical base of 12,232.38, which I treat as unreliable for a cyclical with falling returns and no SOTP data (note section 3)."},
    "bear": {"probability": 0.3, "target_price_12m": 3917.79, "basis": "ROIC and operating margin keep falling from 8.0% and 11.1% [RA-T, IS-T] as leverage rises from 1.23x [BS,IS]: the mechanical bear fair value of 3,917.79 [fact sheet Fair value], near the 52-week low of 3,920.00 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock is already below its own 5-year P/B minimum, and the base-fair-value-less-20% level sits above the price. What blocks a BUY is falling ROIC, ROCE and margins with rising leverage, plus no segment data, so a lower price would not change the decision. A stabilisation in returns would.",
  "replaces": null,
  "replacement_reason": null
}
```

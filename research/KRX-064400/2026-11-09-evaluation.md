# Evaluation: LG CNS Co., Ltd. (KRX:064400) — 2026-11-09
## Bear case
A labour-based integrator (gross margin 15.4%) whose moat is only [Guessing] [IS]. The price fell from a 52-week high of 153,300 to a 57,700 low, and nothing we hold explains why; the Oct 30, 2026 results are not in the fact sheet [HI, ST]. [Certain] We have no revenue-growth figures, segment mix, foreign share or own-history multiples, so the cheapness rests on peers alone [RA]. [Certain] The **Direction change** lines: ROIC fell from 25.2% to 22.8% and ROCE from 18.1% to 16.1% over a year, and FCF margin is 3.8pp below its 2-year high of 12.4% [RA-T, CF-T]. I judge the cause mostly denominator-driven, not structural (see Bull) [Likely], but with Q3 unseen I can't rule out the start of a real decline. FCF conversion is lumpy (30.0% in FY2023) and shares rose 6.01% [CF, ST]. The DCF bear is 25,975.74. [Certain]

## Bull case
The recent dip looks explained rather than structural. Operating margin is down only 0.4pp to 8.8% and FCF margin is flat at 8.6% over the same twelve months, while net cash grew (net debt/EBITDA from -0.76x in FY2024 to -1.46x TTM) and shares rose 6.01% [IS-T, CF-T, BS, ST]. [Certain] Idle cash from an equity raise inflating invested and employed capital fits a falling ROIC/ROCE with steady margins [Likely]: a lower return on the capital base, not an erosion of operating economics. On fiscal years, ROIC (20.4% to 22.2%) and operating margin (7.9% to 9.0%) have risen [RA, IS]. [Certain] Valuation is undemanding: P/E 14.9x against a 20.1x peer median, EV/Sales 1.0x against 1.7x, a 7.56% FCF yield, and a reverse DCF implying -0.5% revenue growth, with a base DCF of 91,859.42 above the 74,100 close [RA, ST]. [Certain] Altman Z of 4.96 means low balance-sheet risk. [Certain]

## Decision
```json
{
  "ticker": "KRX:064400",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash Korean IT-services group whose falling ROIC and ROCE look like a cash-inflated capital base rather than eroding margins, trading at a discount to peers and at a price implying slight revenue decline, but with too little verified evidence (unseen Q3 results, no growth or own-history data, an unexplained price collapse) for high conviction.",
  "rationale": "Re-judged without any trend rule: the decline looks explained (margins steady, net cash up), so direction is not the obstacle. Conviction stays 3 because of a low-margin business with an unproven moat, missing Q3 results, revenue growth and own-history multiples, an unexplained price collapse, and a wide bear-to-bull range. That gives a good but not compelling skew.",
  "price_at_decision": 74100.0,
  "price_date": "2026-11-06",
  "research_note": "research/KRX-064400/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 18%, showing the slide from 25.2% is a real erosion of returns and not a cash-inflated denominator.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "TTM operating margin falls below 7.5%, under the FY2021 level of 7.9%, showing pricing pressure on project and outsourcing work.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 7.5}},
    {"text": "FCF conversion (FCF/NI, cash-flow page, FY) falls below 60%, or net debt/EBITDA on the ratios page rises above 0x so the net cash is lost."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 105000, "basis": "Steady margins confirm the ROIC dip is denominator-driven and P/E re-rates part of the way from 14.9x toward the 20.1x peer median [RA, peers]; set below the mechanical bull of 143,371.74 because own-history multiples are [data unavailable]."},
    "base": {"probability": 0.45, "target_price_12m": 80000, "basis": "ROIC holds near 22.8% TTM [RA] and the peer discount persists, so returns roughly track earnings plus the 7.56% FCF yield [ST]; set below the mechanical base of 91,859.42 because the reverse DCF bar is low but the wide bear-to-bull DCF spread makes the base low-confidence (macro overlay is context only)."},
    "bear": {"probability": 0.3, "target_price_12m": 54100, "basis": "Unseen Q3 results or a continued ROCE slide from its 20.4% 2-year high [RA-T] send the price back to its 52-week low of 54,100 [HI]; set above the mechanical bear of 25,975.74 because net cash (net debt/EBITDA -1.46x [BS,IS]) and an Altman Z of 4.96 [ST] limit downside."}
  },
  "entry_price": 73487.54,
  "entry_basis": "valuation file: base 91,859.42 less the 20% margin of safety; a hit triggers re-research, which should also bring in the Oct 30, 2026 results that are currently missing.",
  "replaces": null,
  "replacement_reason": null
}
```

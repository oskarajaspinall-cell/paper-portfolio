# Evaluation: lululemon athletica inc. (LULU) — 2026-10-07
## Bear case
This is a fundamental downturn, not just a de-rating. ROIC has fallen from 44.0% (FY2022) to 23.7% TTM, and operating margin from the low-20s to 16.6% TTM [Certain] (RA, IS). The note's earnings release shows negative comps and a guidance cut, so TTM earnings understate the coming decline. That makes the 7.7x P/E optically cheap [Likely]. Gross margin of 54.9% TTM, below every year shown, points to eroding pricing power against Alo, Vuori, On and Nike [Likely]. FY2023's 4.0% FCF margin shows how fast cash conversion can collapse [Certain] (CF). Short interest is 13.55% and rising, the Piotroski F-score is only 4, and plaintiff-firm investigations add an overhang [Certain] (ST, OV). Momentum is broken: the stock is -34.6% vs its 200-day MA, with no earnings catalyst inside a quarter [Certain] (HI). Cheap multiples can stay cheap while estimates fall [Guessing].
## Bull case
The valuation already prices in a broken brand. P/E is 7.7x, EV/EBITDA 4.7x and P/FCF 7.7x, all below their 5y minimums and 54-66% below peer medians [Certain] (RA, P). The FCF yield is 13.07%, and shares fell 4.31% YoY through buybacks, so holders get paid while they wait [Certain] (ST). The balance sheet is near net cash (0.32x net debt/EBITDA) and Altman Z is 6.17, so solvency is not the issue [Certain] (BS, ST). Even after the downturn, ROIC of 23.7% and ROE of 30.9% are still high for apparel [Certain] (RA). If comps simply stabilize, a modest re-rating toward the peer EV/Sales median of 1.5x would give a large upside [Guessing]. Short interest of 13.55% could fuel a squeeze on any upside surprise [Guessing].
## Decision
```json
{
  "ticker": "LULU",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A still-profitable, near-net-cash premium apparel brand trades below every 5-year valuation minimum, but falling returns, margins and comps mean the low multiple may be reflecting an earnings reset rather than mispricing it.",
  "rationale": "The valuation is compelling, but every quality metric is falling, TTM earnings likely overstate the forward base, and there is no evidence yet that comps or gross margin have stabilized. Without that, the low multiple could be a value trap. Conviction 3 falls below the buy threshold of 4, so AVOID and hold cash. Revisit when margins inflect.",
  "price_at_decision": 93.61,
  "price_date": "2026-10-06",
  "research_note": "research/LULU/2026-10-07.md",
  "triggers": [
    {"text": "TTM gross margin recovers above 58%, back toward FY2024-25 levels, showing pricing power has been restored.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 58}},
    {"text": "TTM operating margin recovers above 20%, reversing the compression from the FY2025 level of 23.7%.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 20}},
    {"text": "TTM FCF margin recovers above 15%, showing cash generation has stabilized.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 15}},
    {"text": "TTM ROIC stabilizes above 35%, halting the five-year decline.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 35}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 135, "basis": "Comps stabilize and EV/Sales re-rates from 1.0x toward the 1.5x peer median [RA, P] on slightly lower sales, supported by the 13.07% FCF yield and 4.31% buyback shrink [ST]."},
    "base": {"probability": 0.45, "target_price_12m": 90, "basis": "P/E holds near 7.7x [RA] while earnings slip further as operating margin keeps compressing from 16.6% TTM [IS]; buybacks roughly offset the earnings decline."},
    "bear": {"probability": 0.30, "target_price_12m": 65, "basis": "Margin erosion extends (gross margin already 54.9% TTM, ROIC down to 23.7% [IS, RA]) and FCF margin falls toward the FY2023 4.0% low [CF], so earnings reset lower at a flat multiple amid rising 13.55% short interest [ST]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

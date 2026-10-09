# Evaluation: Brown-Forman Corporation (BF.B) — 2026-10-09
## Bear case
Returns on capital are falling, and the decline is structural rather than cyclical. ROIC dropped from 22.3% to 14.3% and ROE from 31.1% to 18.1% over five years, and operating margin is down 3.3pp [Certain]. Q1 FY2027 sales fell and missed estimates. Tequila is slowing, RTD is being taken back from the Pabst JV, and Canada still keeps US spirits off its shelves [Likely]. Younger consumers drinking less spirits is a secular headwind, not a dip [Guessing]. Leverage rose from 1.12x to 1.80x, and a new $500m note was priced at 5.375% just as the 10y yield rose to 5.28% [Certain]. EV/EBITDA, EV/Sales and P/B still sit 17%, 13% and 47% above the peer median, so the stock is cheap only against its own premium past [Certain]. Short interest is 10.2% and rising [Certain]. BF.B shares carry no votes [Certain].
## Bull case
Every multiple sits at or below the bottom of its 5-year range: P/E 17.1x against a 22.1x median, and P/FCF 13.2x, below its 5-year minimum [Certain]. The reverse DCF implies revenue falling 4.2% in year 1. That is a harsh path for a franchise whose gross margin has held at about 60.7% [Certain]. Cash generation has recovered sharply: FCF margin is 23.6% TTM, FCF conversion 128%, and the FCF yield 7.6%, while the share count fell 2.03% [Certain]. Management reaffirmed the full-year outlook, and gross margin improved in Q1 [Likely]. The mechanical fair-value base of $38.73 is 45.9% above the price [Certain]. Beta of 0.32 and an Altman Z of 4.27 point to limited downside to the balance sheet [Certain]. If tequila and RTD stabilise, the stock could re-rate toward its historical multiples [Guessing].
## Decision
```json
{
  "ticker": "BF.B",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A strong spirits franchise trades at the bottom of its own 5-year multiples, but falling returns, declining sales, rising leverage and a premium to peers on EV/EBITDA make it cheap for a reason rather than mispriced.",
  "rationale": "Valuation is undemanding and FCF has recovered, but ROIC, ROE and operating margin are all falling, sales are declining and there is no visible catalyst. Peers are cheaper on EV/EBITDA. Rising short interest and higher-for-longer rates add to the risk. That makes this good but not compelling: conviction 3, below the buy threshold.",
  "price_at_decision": 26.54,
  "price_date": "2026-10-08",
  "research_note": "research/BF.B/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin falls below 57%, showing Jack Daniel's pricing power is breaking down (now 60.7%).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 57}},
    {"text": "TTM ROIC falls below 10%, extending the decline from 22.3% (FY2022) to 14.3% and showing the moat no longer protects returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Debt/EBITDA rises above 3.0x (now 1.80x), so leverage threatens capital returns.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}},
    {"text": "TTM FCF margin falls back below 15% (now 23.6%), showing the cash recovery from the FY2023-25 trough was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 33.95, "basis": "Tequila and RTD stabilise and the price reaches the mechanical DCF base of 33.95 [fact sheet Fair value], about midway between today's P/E of 17.1x and its 22.1x 5-year median [RA]; the macro overlay's small tilt toward bear (research/BF.B/2026-10-09-macro.md) caps this at 0.20, below the 43.04 blended bull."},
    "base": {"probability": 0.5, "target_price_12m": 27.5, "basis": "Multiples hold near today's P/E of 17.1x and P/FCF of 13.2x [RA], and the 7.6% FCF yield and 2.03% buyback [ST] give modest support; the target sits well below the 38.73 mechanical base because that assumes history-based growth, while sales are falling and the price implies -4.2% growth [OV, fact sheet reverse DCF]."},
    "bear": {"probability": 0.3, "target_price_12m": 21.0, "basis": "Sales keep declining and ROIC keeps eroding (14.3% TTM [RA]), so P/E compresses below its 16.5x 5-year minimum on lower earnings and the price breaks the 22.61 52-week low [HI]; the target sits between the DCF bear of 10.90 and the EV/EBITDA bear of 26.02 [fact sheet Fair value], and probability is raised by the macro overlay's small bear tilt from 10y yields at 5.28% (research/BF.B/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

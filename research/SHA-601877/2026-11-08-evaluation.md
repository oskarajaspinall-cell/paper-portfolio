# Evaluation: Zhejiang Chint Electrics Co., Ltd. (SHA:601877) — 2026-11-08
## Bear case
Returns are low and falling: ROIC 6.6% TTM from 9.5% in FY2021, and on a rolling basis ROCE fell from 9.7% to 8.6% and operating margin from 14.5% to 12.9% over the last year [RA-T, IS-T]. [Certain] ROIC sits below a cost of equity built on a 4.84% risk-free rate plus the 3.5% CNY country premium, so growth destroys value. [Likely] The FCF surge (FCF/NI 534.4%) coincided with net debt/EBITDA rising from 2.50x to 4.25x and an Altman Z of 1.57 [ST], pointing to working-capital or financing inflows, not earnings power. [Likely] The Direction change line confirms it: FCF margin is 5.1pp below its 2-year high of 41.2%, so the cash spike behind the cheap FCF multiples is fading. [Likely] The DCF-led base fair value of 164.55 is an artefact of that FCF; the bear value is negative. [Certain] The Q3 2026 report was not read. [Certain]

## Bull case
On earnings and book the stock is cheap against its own history: P/E 11.6x and P/B 0.9x are below their 5y minimums, EV/EBITDA 9.6x sits at 15% of its range [RA]. [Certain] Peers trade at a P/E median of 25.7x and EV/EBITDA of 18.2x. [Certain] ROE has held at 11.1% TTM, gross margin rose over five years to 23.3% TTM, Piotroski F is 6 and shares fell 1.30% YoY [ST]. [Certain] If even part of the cash inflow is durable it would fund deleveraging, and a re-rating merely to the 5y median P/E of 13.2x or P/B of 1.1x gives moderate upside. [Guessing] Beta 0.75 and a stable yuan (overlay, context only) limit macro risk. [Likely] But no evidence of an improving business or a catalyst exists; cheapness alone is not a thesis. [Likely]

## Decision
```json
{
  "ticker": "SHA:601877",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A low-return electrical-equipment maker with falling ROIC and operating margin and rising leverage looks cheap on earnings and book, but its headline FCF yield rests on unreconciled cash inflows, so cheapness is not an edge.",
  "rationale": "Returns, margins and leverage are all moving the wrong way over the last year, and the FCF that drives the mechanical fair value is unexplained and already fading. Earnings and book multiples are cheap, but the business is not improving. Conviction 2: no position.",
  "price_at_decision": 24.73,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-601877/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC rises above 9.5%, back to the FY2021 level, showing returns are recovering rather than eroding.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 9.5}},
    {"text": "TTM operating margin rises above 14.5%, its 2-year high, reversing the last year's fall.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 14.5}},
    {"text": "Net debt/EBITDA falls below 2.5x (4.25x TTM now), showing the cash inflows are real and paying down debt.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 30.0, "basis": "P/B re-rates from 0.9x to its 5y median 1.1x [RA] as leverage stops rising; far below the mechanical bull of 202.91 because that DCF capitalises a 36.1% FCF margin the note judges non-recurring [CF-T]."},
    "base": {"probability": 0.45, "target_price_12m": 25.0, "basis": "P/E stays near 11.6x [RA] on flat earnings as ROIC 6.6% and operating margin 12.9% drift [RA-T, IS-T]; well below the mechanical base of 164.55 because that DCF-led value rests on unreconciled FCF (note section 2)."},
    "bear": {"probability": 0.3, "target_price_12m": 18.45, "basis": "Margins keep falling and leverage stays above 4x, valuing the stock at the mechanical EV/EBITDA bear of 18.45 [fact sheet Fair value] rather than the negative blended bear of -62.67."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

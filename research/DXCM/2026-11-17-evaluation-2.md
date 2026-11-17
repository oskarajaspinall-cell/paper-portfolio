# Evaluation: DexCom, Inc. (DXCM) — 2026-11-17
## Bear case
The price already assumes a lot: the reverse DCF implies 31.6% year-1 revenue growth, well above what the business is delivering, and the narrowed FY26 range points to low-teens growth [Likely]. On peers it is dear (P/E +27%, EV/EBITDA +32% vs the peer median) [Certain]; the cheapness is only against its own bubble-era history. The trend case is extended in that sense: a stock up 40.6% in 12 months with beta 1.44 de-rates hard if growth slows or Abbott presses on price, and rising real yields raise that multiple risk (macro overlay) [Likely]. FCF margin fell to 21.5% TTM from 23.5% a year earlier, 8.2pp below its 2-year high, while the MD&A flags G6 inventory charges and heavier advertising [Certain]. The mechanical base fair value of 60.90 sits below the price, though it is flagged unreliable [Certain]. Pricing-pressure language vanishing from the 10-Q proves nothing [Guessing].

## Bull case
This is a good business that is working: ROIC 45.9% TTM vs 24.1% in FY2024, operating margin 24.0% vs 14.9%, net cash and Piotroski 7 [Certain]. Q3 beat, US revenue grew 14% and the FY26 range was narrowed upward at the low end, with roughly 24% non-GAAP operating margin guided [Likely]. The FCF dip is timing, not earnings quality: conversion is still 110.8% of net income and operating margin rose through it [Likely]. Recurring sensor revenue, the installed base and payer access form a narrow moat against all but Abbott [Likely]. P/E 32.0x is at 1% of its 5y range and EV/EBITDA is below its 5y minimum, while shares fell 3.92% YoY on a completed buyback with a new programme announced [Certain]. The price sits above its 200-day average without being overextended, with a 3.61% FCF yield [Certain]. The FDA warning-letter risk factors were dropped [Likely].

## Decision
```json
{
  "ticker": "DXCM",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only FCF margin is falling over 1 year (23.5% -> 21.5% TTM) while operating margin rose to 24.0% and FCF conversion is 110.8% [CF-T,IS-T]; the 10-Q MD&A cites G6 discontinuation inventory charges and higher advertising (https://www.sec.gov/Archives/edgar/data/1093557/000109355726000195/dxcm-20260930.htm), a one-off rather than a broken model.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A de-rating from an extended price if growth slows: the reverse DCF implies 31.6% year-1 growth against low-teens guidance, with Abbott as a scaled price competitor and beta 1.44.",
    "veto": null
  },
  "new_evidence": {"type": "method_change", "text": "The 2026-11-15 AVOID 3 predates the 2026-11-17 scorecard rule (strength_at_value_points) that gives trend strength 3 points when the value blend is at or above the price; the evidence itself is unchanged."},
  "thesis": "A high-and-rising-return CGM franchise with net cash, at the bottom of its own multiple history and in a healthy uptrend, whose margin gains are still compounding.",
  "rationale": "Quality, rising returns, net cash and trend strength give the scorecard conviction 4, the minimum size. The main risk is a de-rating if growth undershoots what the price implies, and peers are cheaper, so this is a buy-bar name, not a 5. Python sets the volatility-scaled size; cash above the floor cannot fund it.",
  "price_at_decision": 81.61,
  "price_date": "2026-11-16",
  "research_note": "research/DXCM/2026-11-17.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 25%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "Gross margin (TTM) falls below 58%", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 58}},
    {"text": "Operating margin (TTM) falls below 18%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18}},
    {"text": "A new FDA warning letter, recall order or production shutdown disclosed in a 10-Q/8-K at sec.gov"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 110, "basis": "Margin gains continue and the P/E holds near today's level on higher earnings, in line with the P/E-method base of 109.30 [IS,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 85, "basis": "Earnings grow with guidance while the multiple drifts toward peers (P/E peer median 25.2x [RA]), leaving the price near today's level; above the unreliable blended base of 60.90."},
    "bear": {"probability": 0.25, "target_price_12m": 55, "basis": "Growth slows against the 31.6% the reverse DCF implies and the stock de-rates to its 52-week low area of 56.72 [HI], toward the blended base of 60.90."}
  },
  "replaces": "OTIS",
  "replacement_reason": "Cash above the 1.5% floor cannot fund the buy after today's pending orders. OTIS is held at conviction 3, its own thesis says the price sits above fair value while operating margin falls and leverage rises; DXCM clears the buy bar with rising returns and net cash."
}
```

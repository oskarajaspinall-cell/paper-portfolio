# Evaluation: Otis Worldwide Corporation (OTIS) — 2026-11-07
## Bear case
The price of 78.96 USD is above the mechanical base fair value of 70.99, and the best-method DCF gives only 60.40 [FV] [Certain]. The reverse DCF needs 6.7% year-1 revenue growth while margin expansion has stalled: TTM operating margin is 15.5% against 16.5% in FY2025, and the 10-Q shows Q3 gross margin down 120 basis points [company-reported] (https://www.sec.gov/Archives/edgar/data/1781335/000178133526000127/otis-20260930.htm) [Certain]. Q3 adjusted EPS was flat and FY26 guidance unchanged amid China weakness [OV transcript] [Certain]. Leverage keeps rising, with net debt / EBITDA at 3.12x TTM from 2.62x in FY2021, so buybacks are partly debt-funded [RA] [Likely]. A CEO transition is due in the first half of 2027 [Likely]. After the rally, the price is 12.3% above its 50-day average and RSI is 68.1, so near-term upside may already be priced in [ST] [Likely].

## Bull case
The thesis is still running, not spent. Quality keeps improving: ROIC is 58.0% TTM against 31.2% in FY2021, and FCF conversion is 107.5% TTM [RA, CF] [Certain]. Q3 organic sales rose 6%, with modernization up 20% and New Equipment back to growth [OV transcript] [Certain]. Even after the rerating, P/E of 19.6x, EV/EBITDA of 15.1x and P/FCF of 18.0x all sit below their 5-year minimums and below the peer medians of 28.9x, 18.4x and 23.8x [RA] [Certain]. The fair value is stale in one direction: the EV/EBITDA method alone gives 92.18, and the DCF is anchored on a five-year FCF margin that has not fallen below 10.0% [FV, CF] [Likely]. A 5.57% FCF yield and a 2.60% fall in the share count return cash to holders [ST] [Certain]. No core trigger has fired [Certain].

## Decision
```json
{
  "ticker": "OTIS",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A service-led elevator franchise with ROIC rising to 58.0% still trades below its own 5-year minimum on every multiple and below peers, pricing a transitory margin squeeze and CEO transition as permanent impairment.",
  "rationale": "Reaching base fair value has not completed the thesis. Multiples remain below their own 5-year floor and below peers, returns are rising and Q3 service and modernization growth was solid. Stalled margins, rising leverage and a stretched short-term chart rule out an ADD. No trigger has fired, so the existing size is kept.",
  "price_at_decision": 78.96,
  "price_date": "2026-11-06",
  "research_note": "research/OTIS/2026-11-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2021 5-year low of 15.2%, showing the service-margin squeeze is structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15.2}},
    {"text": "TTM FCF margin falls below the FY2025 5-year low of 10.0%, showing cash generation is deteriorating with margins.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10.0}},
    {"text": "Net debt/EBITDA on the ratios page rises above 3.5x (3.12x TTM now), showing capital returns are outrunning cash generation."},
    {"text": "Service operating margin in the earnings release falls below 20% for two consecutive quarters, or modernization backlog growth turns negative."}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 93.91, "basis": "Service and modernization growth restores margin expansion and EV/EBITDA moves back toward its 5y minimum of 16.4x [RA], which matches the EV/EBITDA bull value of 93.91 [FV]."},
    "base": {"probability": 0.5, "target_price_12m": 82.0, "basis": "Organic growth continues at the Q3 pace [OV transcript] with margins flat, so multiples stay below their 5y floor; set above the blended base of 70.99 because the EV/EBITDA method (92.18) better reflects a ROIC that has risen to 58.0% [RA] than a DCF tied to the FCF-margin history."},
    "bear": {"probability": 0.2, "target_price_12m": 56.96, "basis": "The Q3 gross-margin decline [company-reported] proves structural, China stays weak and leverage above 3.12x [RA] limits buybacks, so the shares fall to the mechanical bear fair value of 56.96 [FV]."}
  },
  "entry_price": 56.79,
  "entry_basis": "valuation file: base 70.99 x 0.8"
}
```

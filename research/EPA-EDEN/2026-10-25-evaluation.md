# Evaluation: Edenred SE (EDEN) — 2026-10-25
## Bear case
The derating has a reason: meal-voucher rule changes in Italy and Brazil hit the core franchise, and Q3 operating revenue edged down (https://www.nasdaq.com/articles/edenred-q3-operating-revenue-edges-down-confirms-outlook) [Certain]. Fee caps set by regulators can be extended to other countries and can't be fixed by management [Likely]. The 17.57% FCF yield and 210.2% FCF conversion [CF,IS] are flattered by float working capital, which reverses if issued volumes shrink, so the true recurring yield is lower [Likely]. Float income also depends on euro rates, which the macro overlay cannot assess [Likely]. Piotroski F is only 5 [ST], net debt/EBITDA rose back to 1.65x TTM from 1.13x in FY2025 [BS,IS], and the 12-month change of -0.6% shows the market has not rewarded the 6-month rebound [ST] [Certain]. The mechanical bear value of 20.78 EUR sits below the price [Certain].

## Bull case
Quality is rising, not breaking: ROIC 18.5% TTM vs 10.0% in FY2023, ROCE 27.2%, operating margin 29.6%, FCF margin 38.2% [RA,IS,CF] [Certain]. Yet P/E 12.6x sits at the 9th percentile of its 5y range (median 32.3x) and well below the peer median 22.3x; EV/EBITDA 7.1x vs a 19.6x median [RA] [Certain]. The reverse DCF implies -1.3% revenue growth in year 1, while Q3 intrinsic growth was 6.6%, Q3 core earnings beat, FY2026 EBITDA guidance was reaffirmed and 8%–12% growth is targeted for 2027–2028 (https://stockanalysis.com/quote/epa/EDEN/transcripts/654778-q3-2026-tu/) [Likely]. Mobility is offsetting the regulatory drag [Likely]. Shares fell 0.97% YoY and the dividend was raised 10% [ST, AGM transcript] [Certain]. Base fair value 37.90 EUR is well above the 25.91 close [Certain].

## Decision
```json
{
  "ticker": "EPA:EDEN",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A two-sided benefits and mobility payments network with ROIC rising to 18.5% and a 38.2% FCF margin trades at the bottom of its own 5-year multiples and below peers on P/E, where the price implies a revenue decline that reaffirmed guidance and 6.6% Q3 intrinsic growth do not show.",
  "rationale": "Rising returns, strong cash generation and a price implying shrinkage against guided growth give a favourable skew. Unresolved Italy/Brazil voucher regulation, float-flattered FCF and a mechanical bear value below the price cap conviction at 4, not 5: standard volatility-scaled core size. Financials is not held, so no cap is breached.",
  "price_at_decision": 25.91,
  "price_date": "2026-10-23",
  "research_note": "research/EPA-EDEN/2026-10-25.md",
  "triggers": [
    {"text": "TTM operating margin falls below 26%, under every year except the FY2023 trough (23.5%), showing regulation is compressing take rates structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 26}},
    {"text": "TTM ROIC falls below 14%, giving up most of the recovery from 10.0% in FY2023 to 18.5%, signalling the network moat is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 14}},
    {"text": "TTM FCF margin falls below 28%, under the five-year FY range of 31.0%-44.3%, showing float outflows or lost volumes are draining cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 28}},
    {"text": "Management withdraws or cuts the FY2026 EBITDA guidance or the 2027-2028 growth target in a results release, or a further country imposes a meal-voucher fee cap, or net debt/EBITDA on the ratios page rises above 2.5x."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 37.9, "basis": "Guidance holds and Mobility offsets the voucher drag, so the price converges on the mechanical base fair value of 37.90 EUR (FCFE/DCF, fact sheet Fair value), still far below the 5y median P/E of 32.3x [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 31.0, "basis": "Intrinsic growth stays positive per the Q3 transcript (https://stockanalysis.com/quote/epa/EDEN/transcripts/654778-q3-2026-tu/) and P/E re-rates partly from 12.6x toward the peer median 22.3x [RA], around the 52-week high of 30.85 [HI], below base fair value because the regulatory discount persists."},
    "bear": {"probability": 0.25, "target_price_12m": 20.78, "basis": "Regulation spreads beyond Italy and Brazil and float-driven FCF reverses, taking the price to the mechanical bear fair value of 20.78 EUR (fact sheet Fair value), above the 52-week low of 15.23 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Not applicable: BUY.",
  "replaces": null,
  "replacement_reason": null
}
```

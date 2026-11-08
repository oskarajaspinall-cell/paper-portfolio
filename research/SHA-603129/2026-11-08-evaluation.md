# Evaluation: Zhejiang Cfmoto Power (SHA:603129) — 2026-11-08
## Bear case
Margin of safety is thin: the price of 317.58 sits only 8.8% below the base fair value of 345.53, and the mechanical bear value is 68.58 [Certain]. Gross margin peaked at 32.3% in FY2023 and has fallen to 28.4% TTM [Certain]. Two Direction change lines matter. FCF margin fell from 18.1% to 15.6% over the last 12 months, 4.1pp below its 2-year high. That is the cash-conversion pillar of the thesis weakening, likely working capital or capex normalising rather than a break, but unverified [Likely]. The ROIC drop to 105.0% from 192.2% is a stale, patchy series (latest point 2024-03-31), so it is weak evidence either way [Likely]. The geographic revenue split is [data unavailable]. Export, tariff and CNY exposure is unknown, not zero (macro overlay) [Certain]. Powersports is cyclical, and P/B of 5.2x sits at the 69% point of its range [Certain].
## Bull case
Quality is genuinely improving on fiscal-year endpoints and on the rolling view. ROCE rose from 10.9% to 23.3% TTM, ROE is 28.3%, and operating margin of 10.8% is at its 2-year high, up 1.3pp in the last year [Certain]. The balance sheet is net cash (net debt/EBITDA -3.92x), FCF conversion is 176.5% and there is no dilution [Certain]. EV/EBITDA of 12.3x sits at the 7% point of its 5y range against a median of 18.2x, and below the peer median of 19.0x. The FCF yield is 8.26% [Certain]. The reverse DCF implies only 4.0% year-1 revenue growth, an undemanding bar for a share gainer [Likely]. Beta of 0.45 and relative strength against SPY show the market is rewarding delivery [Certain].
## Decision
```json
{
  "ticker": "SHA:603129",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash powersports maker with rising ROCE and operating margin trades below its own 5-year median EV/EBITDA, but the price already sits close to base fair value while FCF margin and gross margin are slipping and the geographic exposure is unknown.",
  "rationale": "Quality is real and improving, but the upside to base fair value is small, the expected value sits near the price, FCF margin is falling on the rolling view and the export mix is unverified. That is good but not compelling, so conviction is 3: AVOID, with an entry price at a 20% margin of safety.",
  "price_at_decision": 317.58,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-603129/2026-11-08.md",
  "triggers": [
    {"text": "TTM gross margin falls below 24%, under the FY2022 level of 25.1%, signalling loss of pricing power or mix deterioration.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 24}},
    {"text": "TTM FCF margin falls below 8%, showing the cash-conversion decline from 18.1% to 15.6% is structural rather than working-capital timing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "TTM operating margin falls below 8%, reversing the rise to 10.8% and returning to FY2023 levels.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}},
    {"text": "ROCE on the ratios page (TTM) falls below 18%, giving up most of the five-year rise from 10.9% to 23.3%."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 441.2, "basis": "Operating margin keeps rising from its 10.8% 2-year high [IS-T] and EV/EBITDA re-rates toward its 18.2x 5y median [RA], matching the EV/EBITDA bull value of 441.20 [fact sheet Fair value]; below the blended bull of 635.23 because the DCF bull extrapolates peak FCF conversion."},
    "base": {"probability": 0.5, "target_price_12m": 345.53, "basis": "ROCE holds near 23.3% [RA] with the reverse-DCF 4.0% growth delivered, giving the mechanical base fair value of 345.53 [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 207.13, "basis": "Gross margin keeps sliding from 32.3% [IS], FCF margin falls further from 15.6% [CF-T] and EV/EBITDA stays near its 5y low of 10.0x [RA], giving the EV/EBITDA method value of 207.13; above the blended bear of 68.58 because the through-cycle DCF bear of 28.63 assumes FY2021-type margins that a net-cash business at -3.92x net debt/EBITDA [BS] does not need to revisit."}
  },
  "entry_price": 276.42,
  "entry_basis": "valuation file: base 345.53 x 0.8 (20% margin of safety); at that level the same improving-quality evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Zoetis Inc. (ZTS) — 2026-11-08
## Bear case
Companion animal, about 67.3% of nine-month revenue `[company-reported]`, is losing share: dermatology fell about 13.5% in nine months `[company-reported]`, with generics on Convenia and Cerenia and weaker Librela (10-Q). [Certain] Management is planning cautiously for 2027 as pet owners cut vet visits (Reuters, 2026-11-05). [Likely] If pricing power is structurally impaired, the own-history P/E leg (191.45 base) overstates value and the DCF leg (93.14) is the better anchor. [Likely] The Direction change line: ROCE is 2.9pp below its 2-year high of 31.9%, and ROIC (-0.5pp) and FCF margin (-0.7pp) eased over the year; profitability has stopped compounding. [Certain] Net debt/EBITDA rose from 1.03x to 1.92x while earnings are flat, partly funding buybacks. [Certain] Macro is context only; no foreign country reaches 10% of revenue, so country risk is low. [Likely]
## Bull case
Economics remain intact: TTM operating margin 37.9% and gross margin 71.6% sit above both original trigger levels, and ROCE is up 2.5pp versus a year earlier, so the Direction change line is drift from a peak, not deterioration. [Certain] Q3 beat and FY adjusted EPS guidance was raised, clearing the guidance-cut trigger. [Likely] Livestock and diagnostics are growing. [Likely] Yet P/E 13.4x, EV/EBITDA 9.9x and P/FCF 14.4x are all below their 5y minimums and peer medians, at a 6.93% FCF yield; the reverse DCF implies only 0.8% year-1 growth. [Certain] Shares are down 5.45% YoY, so buybacks compound per-share value. [Certain] The price sits just above the mechanical bear value of 76.01 with base 125.91: the skew favours holding. [Likely]
## Decision
```json
{
  "ticker": "ZTS",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A high-return animal-health franchise whose margins remain intact despite companion-animal share loss trades below its own 5-year minimum multiples, pricing near-stagnation that growing livestock and diagnostics and raised EPS guidance do not show.",
  "rationale": "Original triggers untested: margins hold above both thresholds and EPS guidance was raised. Dermatology share loss and cautious 2027 planning keep conviction at 4, not 5. The price implies almost no growth, so the skew still favours owning it; the position is near its conviction size, so HOLD rather than ADD.",
  "price_at_decision": 79.40,
  "price_date": "2026-11-06",
  "research_note": "research/ZTS/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2023 5-year low of 35.9%, showing competition is eroding profitability, not just growth.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 35.9}},
    {"text": "TTM gross margin falls below the FY2022 5-year low of 69.7%, signalling structural loss of pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 69.7}},
    {"text": "TTM ROIC falls below 22%, a clear break below the five-year range, showing the moat's returns are eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 22}},
    {"text": "Companion-animal revenue declines for two further consecutive quarters with dermatology share loss cited in the 10-Q MD&A, or 2027 guidance implies a total revenue decline."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 125.91, "basis": "Livestock and diagnostics growth plus raised EPS guidance (Business Wire Q3 release) lift multiples partway off levels below their 5y minimums [RA]: the mechanical base fair value of 125.91 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 93.14, "basis": "Margins hold near the TTM 37.9% [IS] while companion-animal competition persists; valued on the DCF leg of 93.14 rather than the blended 125.91 because the P/E leg leans on own-history multiples that dermatology share loss (10-Q) may have lowered."},
    "bear": {"probability": 0.3, "target_price_12m": 76.01, "basis": "Dermatology share loss and cautious 2027 planning (Reuters 2026-11-05) push earnings lower and multiples stay below their 5y minimums [RA]: the mechanical bear fair value of 76.01 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is already 4 at the current price; the obstacle to conviction 5 is the unresolved companion-animal share loss and 2027 outlook, not price, so a lower price alone would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Toyo Suisan Kaisha (TYO:2875) — 2026-11-07
## Bear case
For a packaged-food company, the margins look like a peak. Operating margin roughly doubled from 8.2% (FY2022) to 16.6% TTM, and gross margin rose from 25.0% to 31.3% [Certain]. Input costs, pricing and the yen probably explain part of that, and those can reverse [Likely]. If they do, the P/E of 13.6x, below its 5y minimum, is cheap on peak earnings, not on normal earnings [Likely]. The mechanical bear value of 8,363.48 JPY sits below the price [Certain]. Cash conversion fell to 61.7% in FY2026, and FCF margin went from 10.6% to 8.1% between FY2024 and FY2026 before recovering [Certain]. The research is thin. Segment mix and overseas exposure are unknown, and the Q2 results of 2026-11-03 were not read [Certain]. So I cannot test whether the margin gains are structural [Certain]. Net cash of -2.23x EBITDA has been shrinking from -3.86x [Certain].

## Bull case
Returns have improved a great deal, and the gains look broad: ROIC went from 11.4% to 23.4% TTM, ROCE from 7.5% to 16.1% and ROE to 14.2% [Certain]. Piotroski F is 7 and Altman Z is 9.38 [Certain]. The stock is cheap on every measure. It trades below its 5y minimum P/E and P/FCF, at the floor of its EV/EBITDA range (6.7x), and at large discounts to the peer medians (22.0x P/E, 12.7x EV/EBITDA) [Certain]. The FCF yield is 6.46% and the share count fell 2.66% YoY [Certain]. The reverse DCF implies a -0.8% year-1 revenue decline, an undemanding bar [Certain]. Base fair value of 12,909.85 JPY is well above the price [Certain]. A beta of 0.25 adds a defensive diversifier [Certain]. A branded staple franchise should keep much of the margin gain [Guessing].

## Decision
```json
{
  "ticker": "TYO:2875",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash branded food maker with ROIC up from 11.4% to 23.4% trades below its own 5-year minimum P/E and P/FCF and far below peers, but the discount may correctly price margins at a cyclical peak.",
  "rationale": "Quality and valuation are attractive, but I can't tell whether the doubled operating margin is structural. Segment mix and the Q2 results are unread, the mechanical bear value is below the price and FCF conversion is lumpy. Good but not compelling: conviction 3, AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 10405.00,
  "price_date": "2026-11-06",
  "research_note": "research/TYO-2875/2026-11-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below 13.6%, the FY2024 level, showing the margin gain is reversing (the peak-margin bear case).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 13.6}},
    {"text": "TTM ROIC falls below 15%, giving back most of the rise from 11.4% in FY2022.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM gross margin falls below 28.7%, the FY2024 level, signalling input-cost or pricing pressure.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 28.7}},
    {"text": "FCF conversion (FCF/net income, cash flow page) stays below 70% on a TTM basis, showing reported earnings are not turning into cash."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 14434.53, "basis": "Margins hold near 16.6% TTM operating margin [IS] and the multiple re-rates toward its 5y median P/E of 17.1x [RA], consistent with the bull fair value of 14,434.53 JPY [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.45, "target_price_12m": 12909.85, "basis": "Returns stay near 23.4% ROIC [RA] and the price moves toward the mechanical base fair value of 12,909.85 JPY (DCF 67% + P/E 33%) [IS,BS,CF,RA,ST,HI], against a reverse DCF implying -0.8% growth."},
    "bear": {"probability": 0.30, "target_price_12m": 8363.48, "basis": "Operating margin reverts toward the FY2024 level of 13.6% [IS] as input-cost and yen tailwinds fade, matching the bear fair value of 8,363.48 JPY (DCF bear 7,220.15) [IS,BS,CF,RA,ST,HI]."}
  },
  "entry_price": 10327.88,
  "entry_basis": "valuation file: base 12,909.85 x 0.8; at that level the margin-of-safety covers the unresolved peak-margin risk.",
  "replaces": null,
  "replacement_reason": null
}
```

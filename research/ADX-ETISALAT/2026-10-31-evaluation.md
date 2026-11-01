# Evaluation: Emirates Telecommunications Group Company PJSC (ADX:ETISALAT) — 2026-10-31
## Bear case
The headline cheapness is partly an earnings mirage: TTM net margin of 25.3% against 19.7% in FY2025, with FCF conversion falling to 90.2%, points to a non-recurring gain inflating TTM profit, so the 9.2x P/E overstates the discount [Likely]. On the cleaner cash read, P/FCF of 10.2x sits inside its 5y range, not below it [Certain]. ROIC is still below FY2021 (16.2% vs 19.3%) [Certain], Altman Z is 1.61 and Piotroski F only 5 [Certain]. The research could not establish revenue growth, segment mix or what the Q3 2026 release said [Certain], so the reverse-DCF gap (price implies -4.4% growth) is untested against actual growth. The 5y multiple history may embed a one-time re-rating that need not recur, which would make the own-history fair value too generous [Guessing]. Institutional ownership of 5.2% suggests a thin free float [Likely], and international operations add currency risk the fact sheet cannot quantify [Guessing].
## Bull case
A defensive (beta 0.34) telecom with operating margin up from 24.0% to 29.6% and FCF margin of 22.9% trades below its 5y minimum on EV/EBITDA (6.1x vs 6.7x) and EV/Sales, at a 9.80% FCF yield [Certain]. Leverage fell from 1.46x to 0.67x net debt/EBITDA, leaving room for capital returns [Certain]. Against du, STC, Vodafone and Mobily it is at a 32% P/FCF and 19% EV/EBITDA discount [Certain]. Even the mechanical bear fair value of 22.96 AED is above the 20.94 AED close, and the base is 33.35 AED [Certain]. The price implies shrinking revenue for a business whose margins have been rising for five years [Likely]. ROCE has risen to 18.5% [Certain].
## Decision
```json
{
  "ticker": "ADX:ETISALAT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A margin-expanding, deleveraging telecom at a 9.80% FCF yield and below its 5-year minimum EV/EBITDA looks cheap, but TTM earnings appear inflated by a one-off and revenue growth is unverified, so the discount is not yet proven mispriced.",
  "rationale": "Cheap on EV/EBITDA and FCF yield with a mechanical bear value above the price, but P/FCF sits inside its own range, TTM profit looks one-off-inflated, ROIC is below FY2021, and the research could not verify growth or Q3 results. Good but not compelling: conviction 3, no position.",
  "price_at_decision": 20.94,
  "price_date": "2026-10-30",
  "research_note": "research/ADX-ETISALAT/2026-10-31.md",
  "triggers": [
    {"text": "TTM operating margin falls below 25%, giving up most of the expansion from 24.0% (FY2021) to 29.6%, signalling competitive or regulatory pressure in the home market.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}},
    {"text": "TTM FCF margin falls below 15%, under the FY2023 five-year low of 17.1%, showing capex or working capital is eroding cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Debt/EBITDA rises above 2.0x (0.67x net TTM now), showing M&A or payouts are being debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "TTM ROIC falls below 12%, under the FY2025 low of 13.5%, confirming returns on capital are structurally declining.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 31.45, "basis": "EV/EBITDA re-rates toward its 5y median 9.0x [RA], the mechanical EV/EBITDA base value of 31.45 AED, as margins hold and leverage keeps falling [BS,IS]; below the blended base of 33.35 AED because the DCF leans on own-history growth the note could not verify."},
    "base": {"probability": 0.5, "target_price_12m": 22.96, "basis": "Partial re-rating to the mechanical bear fair value of 22.96 AED [IS,BS,CF,RA,ST,HI] as cash flows hold but the one-off-inflated TTM net margin (25.3% vs 19.7% FY2025 [IS]) caps earnings-based upside; below the mechanical base because the 5y multiple history may not recur."},
    "bear": {"probability": 0.25, "target_price_12m": 17.6, "basis": "TTM profit normalises and growth disappoints, so the stock revisits its 52-week low of 17.60 AED [HI]; below the mechanical bear value because P/FCF of 10.2x is already inside its 5y range [RA] and gives less support than the earnings multiples suggest."}
  },
  "entry_price": 18.27,
  "entry_basis": "Mechanical base 33.35 x 0.8 is above the price, so not used; instead P/FCF back at its 5y low of 8.9x [RA] (vs 10.2x now), where the cash-flow valuation alone would justify conviction 4 despite the unverified growth and one-off earnings.",
  "replaces": null,
  "replacement_reason": null
}
```

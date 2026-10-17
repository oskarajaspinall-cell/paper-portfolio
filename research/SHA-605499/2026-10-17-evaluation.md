# Evaluation: Eastroc Beverage (Group) Co., Ltd. (SHA:605499) — 2026-10-17
## Bear case
The share price has fallen 49.1% in 12 months and sits 25.4% below its 200-day average, with negative relative strength over 3, 6 and 12 months [Certain]. The research does not explain the derating: no revenue growth, volume or channel data are shown, so a sharp growth slowdown, which the note itself says the price is discounting, cannot be ruled out [Likely]. The business is single-category while Want Want, Nongfu Spring and Red Bull China push into energy and hydration [Likely]. Cash quality is slipping: FCF conversion fell from 123.3% (FY2024) to 92.4% TTM and FCF margin trends down [Certain]. Shares outstanding rose 6.50% with no buyback, and TTM ROCE and ROE dropped sharply versus FY2025 as capital grew [Certain]. Results are due Oct 29, 2026, an imminent binary event [Certain]. "Cheap versus its own history" means little if the five-year multiples reflected a growth phase that has ended [Guessing].

## Bull case
Reported fundamentals are still improving: TTM gross margin 46.6% and operating margin 25.0% are five-year highs, and ROIC is 130.2% [Certain]. The balance sheet is net cash (net debt/EBITDA -2.78x) [Certain]. At 16.9x P/E and 10.3x EV/EBITDA the stock trades below its own five-year minimums and below the peer median of 32.9x and 14.1x [Certain]. The reverse DCF implies only 11.6% year-1 revenue growth fading to terminal, a modest bar for a brand with the densest refrigerated energy-drink network in China [Likely]. The FCF yield is 5.58%, and the mechanical base fair value of 140.04 CNY sits above the 114.25 close, with the bear value only 9.2% below [Certain]. Founder/insider ownership of 60.67% aligns incentives [Likely]. If Q3 results show growth holding, the multiple has room to recover toward peers [Guessing].

## Decision
```json
{
  "ticker": "SHA:605499",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 130%-ROIC Chinese energy-drink leader trades below its own 5-year minimum multiples, but the cause of the halving of its share price (a likely growth slowdown and rising competition) is not evidenced in the research, so the cheapness cannot yet be distinguished from a justified derating.",
  "rationale": "Quality and balance sheet are excellent and multiples are below their five-year lows, but the research shows no revenue-growth evidence to explain the derating, cash conversion is weakening, shares are diluting, and Q3 results land on Oct 29. Good but not compelling: conviction 3, AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 114.25,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-605499/2026-10-17.md",
  "triggers": [
    {"text": "TTM gross margin falls below 40%, signalling lost pricing power to competing energy and hydration lines.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
    {"text": "TTM net margin falls below 15%, showing single-category concentration risk crystallising.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 80%, indicating the distribution-network moat is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 80}},
    {"text": "Reported quarterly revenue (income statement) declines year on year in the Q3 2026 or later results, confirming the growth slowdown the price discounts."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 140.04, "basis": "Q3 results show growth intact and the multiple re-rates to the mechanical base fair value of 140.04 CNY (DCF 67% + P/E 33%) on record TTM operating margin of 25.0% [IS]."},
    "base": {"probability": 0.45, "target_price_12m": 116.16, "basis": "Earnings hold but the multiple stays depressed near the P/E-method bear value of 116.16 CNY, below the mechanical base because the 49.1% 12-month fall [ST] signals a growth slowdown the history-based growth assumption does not capture."},
    "bear": {"probability": 0.30, "target_price_12m": 97.48, "basis": "Competition and weaker cash conversion (FCF/NI down to 92.4% TTM [CF,IS]) cut growth below the 11.6% the reverse DCF implies, taking value to the DCF bear of 97.48 CNY."}
  },
  "entry_price": 112.03,
  "entry_basis": "valuation file: base 140.04 x 0.8; at that level the margin of safety would compensate for the unexplained growth risk on the same evidence.",
  "replaces": null,
  "replacement_reason": null
}
```

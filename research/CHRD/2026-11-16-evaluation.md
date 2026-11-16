# Evaluation: Chord Energy Corporation (CHRD) — 2026-11-16
## Bear case
Chord is a price-taker on WTI-linked Bakken crude with no real moat; returns are set by oil [Likely]. TTM earnings carry an elevated, geopolitically driven oil price: WTI peaked at 110.01 on 2026-10-19 and was 89.62 on 2026-11-11, against 69.60 in July (macro overlay, FRED) [Certain]. The low 3.2x EV/EBITDA is therefore cheap on near-peak earnings, not mid-cycle [Likely]. Operating margin fell to 18.9% from 20.3% a year earlier and sits 11.3pp below its 2-year high of 30.2% [Certain]; ROIC is 11.8pp below three years ago [Certain]. The stock is up 67.4% in 12 months and 12.3% above its 200-day average [Certain]: an extended price risks a de-rating if oil and growth slow [Likely]. The base fair value of 155.31 offers only +3.6%, the bear 114.28 is -23.8% [Certain]. New CEO since 2026-10-19 adds M&A-appetite uncertainty [Guessing].

## Bull case
The balance sheet is strong at 0.26x net debt/EBITDA [Certain]. FCF margin rose to 22.3% TTM from 17.6%, a 2-year high, and FCF yield is 17.68% [Certain], with over 75% of Q3 FCF returned to shareholders (Q3 release) [Likely]. Management raised 2026 production and EBITDA guidance [Likely]. Valuation is below peers on every multiple (EV/EBITDA 40% below the peer median) and at the bottom of its own 5y range [Certain]. The operating-margin dip is a cyclical normalisation from the FY2022 price peak with the balance sheet intact, not lost share [Likely]. The Marcellus sale for $550.0 million [company-reported] simplifies the portfolio [Likely]. If oil holds near 90, cash returns compound [Guessing].

## Decision
```json
{
  "ticker": "CHRD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "Operating margin and 3-year ROIC/FCF declines track oil-price normalisation from the FY2022 peak with net debt/EBITDA at 0.26x [RA]; FCF margin rose to 22.3% TTM [CF-T] and 2026 guidance was raised (Q3 release, https://www.prnewswire.com/news-releases/chord-energy-reports-third-quarter-2026-financial-and-operating-results-declares-base-dividend-and-updates-2026-outlook-302929809.html).", "moat": "none", "key_risk": "high", "key_risk_text": "The Middle East oil premium fades (WTI already off its 110.01 October peak, macro overlay) and EBITDA falls while the extended price de-rates.", "veto": null},
  "thesis": "A low-leverage, cash-returning Bakken producer that is cheap on trailing multiples, but those multiples rest on an elevated oil price and the mechanical upside is thin.",
  "rationale": "Strong balance sheet and FCF, but no moat, returns set by oil, earnings flattered by a geopolitical premium the macro overlay tilts against, and base fair value barely above the price. Valuation points come only from trend strength. Scorecard conviction 2, so AVOID.",
  "price_at_decision": 149.93,
  "price_date": "2026-11-13",
  "research_note": "research/CHRD/2026-11-16.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 12%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "FCF margin (TTM) falls below 12%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "ROIC (TTM) falls below 6%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 6}},
    {"text": "Net debt / EBITDA rises above 1.0x (e.g. debt-funded M&A under the new CEO)", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 159.44, "basis": "Oil holds near 90 and EV/EBITDA holds at its bull fair value of 159.44 [IS,RA], with raised 2026 guidance delivered (Q3 release)."},
    "base": {"probability": 0.45, "target_price_12m": 149.93, "basis": "Mechanical base 155.31 [RA] trimmed to the current price for the macro overlay's moderate bear tilt (research/CHRD/2026-11-16-macro.md): oil drifting from 89.62 erodes TTM EBITDA."},
    "bear": {"probability": 0.35, "target_price_12m": 114.28, "basis": "Geopolitical premium fades and WTI heads towards the July low of 69.60 (macro overlay), EBITDA falls and the bear fair value of 114.28 [RA] applies; probability raised for the overlay's moderate bear tilt."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

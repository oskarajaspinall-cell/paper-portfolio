# Evaluation: Palantir Technologies Inc. (PLTR) — 2026-11-16
## Bear case
The business is exceptional, but the price already assumes it stays that way for a decade. The reverse DCF implies 79.4% revenue growth in year 1, fading to terminal growth by year 10 [Certain]; any slowdown would de-rate a stock trading at 54.1x EV/Sales against a peer median of 10.8x and at a 1.00% FCF yield [Certain]. The trend is weakening: the price is 9.0% below its 50-day average, the 12-month change is -6.1%, and the 12-month return trails SPY by 16.5pp [Certain]. With beta at 1.61, a further rise in real yields (10y TIPS at 2.86%, up 0.47pp over three months, per the macro overlay) compresses long-duration multiples first [Likely]. Scrutiny of NHS and Australian data use could slow foreign government wins, though no single foreign country reaches 10% of revenue [Likely]. The mechanical base fair value of 38.40 sits far below the price, although it is flagged unreliable [Certain].

## Bull case
Fundamentals are accelerating on every rolling measure: TTM operating margin 45.6% vs 21.8% a year earlier, FCF margin 55.6% vs 46.0%, gross margin 84.7%, ROCE 28.6% at its 2-year high, so there is no Direction change line [Certain]. Earnings growth is outrunning the price: P/E 115.2x and EV/EBITDA 117.6x sit below their own 5-year minimums [Certain]. The Ontology embeds in customer operations, and the top three customers average fifteen years' tenure [company-reported] (https://www.sec.gov/Archives/edgar/data/1321655/000132165526000048/pltr-20260930.htm), which supports high switching costs [Likely]. The balance sheet is net cash (net debt/EBITDA -3.08x) with dilution of only 0.70% a year and Piotroski 7 [Certain]. The 50-day average is 20.0% above the 200-day and the price stays above the 200-day, so the long-term uptrend holds after a seven-session sell-off [Certain].

## Decision
```json
{
  "ticker": "PLTR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROIC, operating margin and FCF margin are all rising on the 1-year and 3-year rolling views (fact sheet Recent direction table, RA-T, IS-T, CF-T).",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Multiple de-rating: the price implies 79.4% year-1 revenue growth at a 1.00% FCF yield, so any growth slowdown or further real-yield rise (macro overlay) cuts the price sharply even if margins hold.",
    "veto": null
  },
  "thesis": "An accelerating, net-cash AI software platform with world-class margins whose price already discounts near-flawless growth for a decade.",
  "rationale": "Quality, direction and balance sheet are top-tier, but the price implies 79.4% year-1 growth at a 1.00% FCF yield, so there is neither a discount nor clean trend strength. Scorecard conviction 3: good but not compelling, so no position; cash is an acceptable outcome.",
  "price_at_decision": 167.99,
  "price_date": "2026-11-13",
  "research_note": "research/PLTR/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 35% (45.6% now), showing rising operating expenses are reversing the margin step-up.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 35}},
    {"text": "TTM FCF margin falls below 45% (55.6% now), showing cash generation is slowing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 45}},
    {"text": "TTM gross margin falls below 78% (84.7% now), signalling pricing pressure from competing AI platforms.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 78}},
    {"text": "Government revenue falls year on year in a quarterly 10-Q, or the top-three customer share of revenue rises above 25%."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 215, "basis": "Margins keep expanding (TTM operating margin 45.6% [IS-T]) and the multiple holds, so the price retests the 52-week high of 212.94 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 150, "basis": "Growth stays strong but the P/E keeps compressing from 115.2x [RA] as earnings catch up, with the macro overlay's small bear tilt from real yields (research/PLTR/2026-11-16-macro.md) keeping the multiple under pressure; well above the unreliable mechanical base of 38.40 because the DCF ignores the margin step-up."},
    "bear": {"probability": 0.30, "target_price_12m": 75, "basis": "Growth slows and EV/Sales de-rates from 54.1x toward its 5y median of 22.2x [RA], in line with the mechanical bull fair value of 77.36; probability raised a little for the macro overlay's small bear tilt (research/PLTR/2026-11-16-macro.md)."}
  },
  "entry_price": 90,
  "entry_basis": "The mechanical fair value is flagged unreliable (methods disagree 2.8x), so the anchor is P/FCF back at its 5y low of 53.6x [RA] on TTM FCF, where the same quality would come with a real discount.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Globus Medical, Inc. (GMED) — 2026-11-08
## Bear case
The top line has stalled. Q3 revenue was down slightly year on year and FY26 revenue guidance was cut, on Nevro weakness and delayed spine launches [Certain]. That leaves the reverse DCF's -0.3% implied year-1 growth looking like a fair read of current delivery, not an overly gloomy one [Likely]. The Direction change line (FCF margin falling over 5 fiscal years but rising from 20.9% to 24.4% over the last 12 months) is partly flattered: Q3 had a $24.6 million lower litigation provision [company-reported] and no repeat of last year's inventory step-up [Likely]. So the TTM peak margins may not last [Likely]. Gross margin has fallen from 75.0% to 69.3%, a structural mix shift [Certain]. Nevro is not earning its keep, Synaptive adds more integration risk [Likely], and short interest of 7.50% rose 21.0% on the month [Certain]. The mechanical bear value is 37.78 [Certain].

## Bull case
On every earnings multiple the stock is below its own 5-year minimum: P/E 17.5x vs 21.7x, EV/EBITDA 8.4x vs 13.0x, P/FCF 12.3x vs 19.8x. It is also well below the SYK/ZBH/MDT peer medians [Certain]. Returns are rising on a rolling basis: ROIC is up 2.2pp to 13.7% and operating margin up 5.0pp to 23.8% [Certain]. FCF conversion of 137.5% backs the 8.14% FCF yield [Certain]. Net cash (net debt/EBITDA -0.40x) and the $500 million buyback increase [company-reported] let it shrink the share count at a depressed multiple [Likely]. Enabling Technologies US unit deployment rose 52% [company-reported], which seeds future implant pull-through [Likely]. Base fair value is 131.26 [Certain]. If the spine launches land, revenue growth returns and the multiple re-rates [Guessing].

## Decision
```json
{
  "ticker": "GMED",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, cash-generative spine and robotics franchise trades below its own 5-year minimum multiples, but falling revenue and a cut FY26 guide mean the price roughly reflects current delivery rather than mispricing it.",
  "rationale": "Valuation, returns and buybacks are attractive, but revenue is shrinking, guidance was cut, Nevro is underperforming and TTM margins are helped by one-offs. The implied stagnation matches what the company is delivering, so the edge is a recovery bet, not a mispricing. Good but not compelling: conviction 3, no position.",
  "price_at_decision": 71.05,
  "price_date": "2026-11-06",
  "research_note": "research/GMED/2026-11-08.md",
  "triggers": [
    {"text": "TTM gross margin falls below 66%, showing the mix shift away from high-margin implants is deepening.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 66}},
    {"text": "TTM operating margin falls below 20%, showing the recent margin gain was one-off (litigation provision, absent step-up) rather than durable.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 11%, giving back the rolling-year recovery and signalling Nevro and Synaptive are diluting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 11}},
    {"text": "Positive case: quarterly revenue on the income statement page returns to year-on-year growth, with the delayed spine launches cited in the 10-Q MD&A, while FCF margin stays above 18%; this would justify re-research for conviction 4."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 105.0, "basis": "Delayed spine launches land and revenue growth resumes, so P/E re-rates from 17.5x back toward its 5y minimum of 21.7x [RA] on rising earnings; below the 131.26 base fair value because that DCF growth path rests on merger-inflated revenue CAGR while FY26 revenue guidance was just cut (fact sheet news, TheFly 2026-11-05)."},
    "base": {"probability": 0.45, "target_price_12m": 80.0, "basis": "Revenue stays flat, roughly matching the reverse DCF's -0.3% implied growth [fact sheet Fair value], while buybacks at an 8.14% FCF yield [ST] and a modest P/E re-rating from 17.5x [RA] add some value."},
    "bear": {"probability": 0.30, "target_price_12m": 55.0, "basis": "Nevro weakness deepens and the one-off margin help fades, so TTM operating margin drifts back from 23.8% toward FY2023-24 levels of 17.4%-17.5% [IS]; held above the mechanical bear of 37.78 [fact sheet Fair value] by net cash (net debt/EBITDA -0.40x [BS,IS]) and the buyback."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: base fair value 131.26 x 0.8 is above the price, and the stock is already below its own 5-year minimum multiples. Conviction 4 needs evidence that revenue is growing again and Nevro has stabilised, which a lower price alone would not supply.",
  "replaces": null,
  "replacement_reason": null
}
```

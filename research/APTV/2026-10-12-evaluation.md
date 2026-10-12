# Evaluation: Aptiv PLC (APTV) — 2026-10-12
## Bear case
The cheapness may be partly a data artefact. EV/EBITDA of 4.3x and P/B of 1.0x sit below their 5-year minimums, but the 2026 EDS separation changed the EBITDA and debt base partway through that history [Likely]. On cash, APTV is not cheap: P/FCF of 13.3x is 55% above the peer median and EV/Sales is 28% above [Certain]. The best-method DCF base is 40.57, below the 43.80 price, so the 76.02 blend rests on the weaker EV/EBITDA leg [Certain]. ROIC has fallen 7.7pp to 7.8%, TTM FCF margin is 3.3% against 7.5% in FY2025, and 2026 guidance was cut on China and Europe [Certain]. The trend is clearly down: -48.1% over 12 months, the 50-day average 25.9% below the 200-day, and -63.8pp against SPY [Certain]. Q3 results on Nov 3 could cut guidance again [Likely]. Rising real yields and credit spreads make this worse (macro overlay) [Likely].
## Bull case
The operating business is improving. Gross margin is up 3.5pp to 19.3%, operating margin up 3.1pp to 11.0% and ROCE up 3.3pp to 15.0% [Certain]. Net margin and ROE look weak mainly because of one-off separation items [Likely]. The reverse DCF implies 5.5% year-1 revenue growth, a low bar given 12% non-automotive growth and $10bn of awards in 2026 [Likely]. Shares outstanding are down 7.54% a year, with close to 100% of FCF going to buybacks [Likely]. Net debt/EBITDA is 1.52x, the Piotroski F-score is 7 and Altman Z is 3.22, so the balance sheet is not distressed [Certain]. Short interest fell 20.9% month on month [Certain]. If the post-separation earnings base holds, a re-rating to the peer EV/EBITDA of 5.2x would add a large return to the equity [Guessing].
## Decision
```json
{
  "ticker": "APTV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A margin-improving, buyback-heavy auto-electronics supplier looks optically cheap on EBITDA and book multiples, but post-separation earnings power is unproven, ROIC and FCF margin are falling, and the best-method DCF base sits below the price.",
  "rationale": "Margins and ROCE are rising, but the low EV/EBITDA rests on a history distorted by the separation. The DCF base (40.57) is below the price, FCF margin has more than halved and guidance was cut, with Q3 results due Nov 3. The macro tilt is toward bear. Good but not compelling, so conviction is 3 and the decision is AVOID.",
  "price_at_decision": 43.80,
  "price_date": "2026-10-09",
  "research_note": "research/APTV/2026-10-12.md",
  "triggers": [
    {"text": "TTM operating margin falls below 9% (the FY2023 level), reversing the margin-recovery trend that underpins the bull case.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 9}},
    {"text": "Net debt/EBITDA rises above 3.0x, showing buybacks are straining the balance sheet into continued China weakness.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}},
    {"text": "TTM FCF margin falls below 2.4% (the FY2022 five-year low), showing cash conversion is deteriorating rather than temporarily depressed.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 2.4}},
    {"text": "Non-automotive revenue growth reported in the earnings release turns negative, showing the robotics/drones/energy-storage diversification has stalled."}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 76.02, "basis": "Q3/Q4 results confirm the post-separation earnings base and the 11.0% operating margin [IS], so the stock re-rates to the blended base fair value of 76.02 (fact sheet fair value table)."},
    "base": {"probability": 0.45, "target_price_12m": 50.00, "basis": "EV/EBITDA moves partway from 4.3x toward the 5.2x peer median [RA, P:MGA/LEA/BWA/VC], held back by the 40.57 DCF base, which reflects the 3.3% TTM FCF margin [CF,IS]."},
    "bear": {"probability": 0.35, "target_price_12m": 35.00, "basis": "A further China/Europe guidance cut on Nov 3 (transcript 660507-q2-2026) pushes the price below the 38.17 blended bear fair value; the probability is raised 5pp and the target lowered because the macro overlay (research/APTV/2026-10-12-macro.md) tilts moderately toward bear on rising real yields and HY spreads."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: the best-method DCF base (40.57) is already close to the price, and the issue is unproven post-separation earnings power after a guidance cut, with ROIC down 7.7pp and FCF margin down from 7.5% to 3.3%. Q3 results on Nov 3 are the unresolved event; a lower price on this same evidence would not lift conviction to 4.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Shenzhou International Group Holdings Limited (HKG:2313) — 2026-11-08
## Bear case
The cheapness tracks a real fall in profits. The fact sheet prints a Direction change on all four rolling metrics. Operating margin went from 19.5% to 16.4%, ROIC from 21.2% to 18.3% and FCF margin from 12.0% to 8.7% in a year [Certain]. Nothing shows the slide has bottomed [Likely]. FCF conversion of 57.5% means P/FCF of 21.0x is dearer than the peer median of 13.7x [Certain]. The best-method DCF gives a base of only 27.73, below the 42.12 price. The blended base of 54.78 relies on EV/EBITDA going back to 5y multiples earned at higher margins [Certain]. The reverse DCF needs 19.5% year-one revenue growth, which is demanding while margins fall [Likely]. The customer and country mix is [data unavailable]. Brand concentration and tariff exposure are probable but unverified [Guessing]. RSI of 75.8 after the 2026-11-05 jump makes for a stretched entry [Certain].
## Bull case
A vertically integrated, net-cash manufacturer trades below its 5y minimum on every multiple: P/E 12.0x, EV/EBITDA 6.5x and P/B 1.5x [Certain]. On P/E and EV/EBITDA it is also below the peer median [Certain]. Returns are still well above the cost of capital, with ROIC at 18.3% TTM against 13.1%–13.4% in FY2021–FY2023 [Certain]. The balance sheet is strong: net debt/EBITDA of -2.06x and Altman Z of 4.69 [Certain]. Insiders own 44.04%, so their interests line up with shareholders' [Certain]. The 12-month fall of -36.3% may be pricing a cyclical squeeze on order pricing as permanent [Guessing]. If operating margin recovers toward the FY2024 level of 20.4%, earnings and the multiple could re-rate together [Likely]. A firmer CNY gives a mild translation tailwind (macro overlay) [Likely].
## Decision
```json
{
  "ticker": "HKG:2313",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-return knitwear manufacturer is statistically cheap against its own history, but every rolling return and margin metric is falling, the cash-flow DCF sits below the price and customer and tariff exposure cannot be verified, so the discount may be deserved.",
  "rationale": "The multiples are cheap only against a higher-margin past. On cash flow the stock is dear to peers, the DCF base is below the price and the margin slide has not visibly stopped. The expected value is only modestly above the price, which is good but not compelling. The obstacle is the quality trend, not the price.",
  "price_at_decision": 42.12,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-2313/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 19% (16.4% now, 19.5% a year earlier), showing the margin slide has reversed rather than become structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 19}},
    {"text": "TTM FCF margin recovers above 12% (8.7% now, 12.0% a year earlier), showing cash conversion is healing.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 12}},
    {"text": "TTM ROIC climbs back above 21% (18.3% now, 21.2% a year earlier), returning to the 2-year high zone.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 21}},
    {"text": "A primary company source discloses customer and country revenue mix showing limited single-customer concentration and US tariff exposure."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 62.0, "basis": "Operating margin recovers toward the FY2024 level of 20.4% [IS] and EV/EBITDA re-rates from 6.5x toward its 5y minimum of 9.8x [RA]; this is below the mechanical bull of 79.18 because that value assumes median multiples from a higher-margin era."},
    "base": {"probability": 0.45, "target_price_12m": 46.0, "basis": "Margins hold near the TTM 16.4% [IS-T] and EV/EBITDA drifts to the peer median of 7.0x [RA,P]; this is below the mechanical base of 54.78 because the best-method DCF gives only 27.73 and the blend leans on the EV/EBITDA leg of 108.88 [fact sheet Fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 34.0, "basis": "The rolling slide continues (FCF margin 8.7% vs 12.0% a year earlier [CF-T]) and P/E stays below its 5y minimum of 14.0x [RA]; this is slightly below the mechanical bear of 35.41 because the DCF bear leg is 23.88 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the default anchor (base 54.78 x 0.8) already sits above the price. A lower price would not change the decision while operating, FCF and ROIC margins are all falling and customer and tariff exposure is [data unavailable]. Re-research once the rolling margins stabilise (see the triggers).",
  "replaces": null,
  "replacement_reason": null
}
```

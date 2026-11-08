# Evaluation: Eiffage SA (EPA:FGR) — 2026-11-08
## Bear case
The shares are down 25.7% over six months and trail SPY by 25.9pp, and neither the note nor the fact sheet identifies why [Certain]. Buying before results on Nov 12, 2026 means buying an unexplained de-rating [Likely]. On earnings the stock is not cheap against its own history: P/E 9.7x sits on its 5y median of 9.8x [Certain]. The **Direction change** matters. FCF margin is 10.9% TTM, against 12.0% a year earlier and a 2-year high of 13.2% [Certain]. FCF conversion fell from 321.8% to 269.4% [Certain]. The FCF base looks inflated by concession and working-capital items, so the 27.70% FCF yield and the mechanical fair value of 748.57 are not usable [Likely]. Net debt/EBITDA rose back to 2.81x from 2.60x at FY2025 [Certain]. Altman Z is 1.04 [Certain]. Concessions saw lower light-vehicle traffic [Likely]. Shares grew 1.98% [Certain]. The foreign revenue mix is unverified [Certain].

## Bull case
EV/EBITDA of 5.2x is below its 5y minimum of 6.1x and below the 7.5x peer median [Certain]. P/E of 9.7x compares with 21.9x for peers and P/B of 1.2x with 2.7x [Certain]. The business is steady. Operating margin is 9.9% TTM, flat over five years and up 0.3pp in the last year [Certain]. ROCE rose to 11.2%, its 2-year high, and ROIC is up 0.5pp on a rolling basis [Certain]. Leverage has fallen from 3.80x in FY2021 [Certain]. Piotroski F is 7 [Certain]. Long-dated concessions and a record order book support earnings visibility [Likely]. The reverse DCF implies -29.2% year-1 revenue growth, which no operating figure shows, though it inherits the inflated FCF base [Likely]. Even on the EV/EBITDA method alone, the bear value of 130.36 sits above the price [Certain]. ECB policy is steady and macro is context only (research/EPA-FGR/2026-11-08-macro.md) [Likely].

## Decision
```json
{
  "ticker": "EPA:FGR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A steady-margin French contractor and concession owner with rising ROCE and falling leverage trades below its own EV/EBITDA range and far below peers, but on earnings it sits at its 5-year median after an unexplained six-month de-rating and with FCF falling from its high.",
  "rationale": "Cheap against peers and on EV/EBITDA, but P/E sits at its own median. The six-month fall has no identified cause. FCF is falling and unreliable, so the fair value carries no weight. Earnings-based scenarios give a modest expected return, which is good but not compelling. Results on Nov 12 may resolve the de-rating, so we avoid for now.",
  "price_at_decision": 106.00,
  "price_date": "2026-11-06",
  "research_note": "research/EPA-FGR/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 9.0% (9.9% now, flat for five years), showing contracting margins or concession traffic are deteriorating.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 9.0}},
    {"text": "TTM FCF margin falls below 8.0% (10.9% now, 13.2% 2-year high), turning the falling cash conversion into a structural problem.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8.0}},
    {"text": "TTM ROIC falls below 7.5% (8.6% now), reversing the five-year improvement from 7.6%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 7.5}},
    {"text": "Net debt/EBITDA rises above 3.2x (2.81x TTM, 2.60x at FY2025), showing the deleveraging has reversed.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 135.0, "basis": "Results show the de-rating was transitory and P/E re-rates toward its 5y max of 11.9x [RA] on a stable 9.9% operating margin [IS]; this sits inside the EV/EBITDA method's 130.36 to 155.80 range, and the DCF-led blend of 1,031.23 is ignored as an FCF artefact (269.4% FCF/NI [CF,IS])."},
    "base": {"probability": 0.5, "target_price_12m": 115.0, "basis": "P/E holds near its 5y median 9.8x [RA] on modestly higher TTM earnings with ROCE at 11.2% [RA]; this is below the EV/EBITDA bear of 130.36 and far below the mechanical base 748.57 because that value capitalises inflated FCF (FCF yield 27.70% [ST])."},
    "bear": {"probability": 0.25, "target_price_12m": 85.0, "basis": "The unexplained six-month fall of 25.7% [HI] reflects a real earnings issue (light-vehicle traffic, FCF margin down from its 13.2% 2-year high [CF-T]) and P/E falls to its 5y min of 7.8x [RA]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the cause of the six-month de-rating is unidentified and the FCF base behind the fair value is unreliable, so a lower price alone would not raise conviction; the Nov 12, 2026 results and a sourced revenue mix would.",
  "replaces": null,
  "replacement_reason": null
}
```

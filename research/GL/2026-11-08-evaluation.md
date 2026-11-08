# Evaluation: Globe Life Inc. (GL) — 2026-11-08
## Bear case
The Direction change is real and has an identifiable cause: TTM ROIC fell from 14.8% to 13.4% over the last year, below its 2-year high of 15.3% [Certain]. The Q3 10-Q ties it to American Income producing agents falling 6% on weak new-agent retention and to health-margin pressure from group claims [company-reported] [Certain]. Fewer agents now means lower life sales later, so the decline may not have finished [Likely]. Q3 EPS missed, and excess prior-period Medicare Supplement claims drew law-firm solicitations [Likely]. Net debt/EBITDA has risen to 2.09x as buybacks outrun deleveraging [Certain]. The 35.6% base upside depends on the P/B + ROE method (248.26). The P/E method gives 143.09, below the price, and the bear value is 128.97 [Certain]. P/FCF of 8.9x sits at the top of its 5y range, and FCF conversion has fallen from 155.9% to 112.6% [Certain]. US-only, so no country risk [Certain].

## Bull case
ROE of 19.3% and ROIC of 13.4% remain high for a life insurer, and both rose over five fiscal years [Certain]. The stock trades on 10.5x P/E and 9.1x EV/EBITDA, roughly a third below peers (15.4x, 13.8x), and on P/B 1.8x, under its 1.9x median [Certain]. An 11.25% FCF yield funds a new buyback authorization, with shares down 4.84% YoY [Certain]. Captive agency and affinity distribution plus high-persistency, low-ticket policies make earnings durable [Likely]. The Medicare Supplement charge stems from a CMS processing delay rather than mispricing, and the investigation notices are solicitations, not filed claims [Guessing]. Short interest of 0.04% shows no crowded bear thesis [Certain]. If agent retention stabilises, the blended base fair value of 213.21 is reachable [Guessing].

## Decision
```json
{
  "ticker": "GL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-ROE captive-agency life insurer trades at a deep peer discount with heavy buybacks, but falling ROIC driven by agent attrition and health-claim pressure leaves the earnings-based value below the price.",
  "rationale": "Valuation is cheap against peers, but the upside rests on the P/B + ROE method while ROIC is falling, agent counts are shrinking and the P/E method sits below the price. Good but not compelling: AVOID at conviction 3, re-examined at the earnings-based fair value or once agent retention stabilises.",
  "price_at_decision": 157.18,
  "price_date": "2026-11-06",
  "research_note": "research/GL/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC (ratios/statistics page) falls below 12%, extending the decline from 14.8% to 13.4% and showing that agent attrition is eroding returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA (site definition) rises above 2.5x from 1.93x, meaning buybacks are being funded with leverage.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "American Income average producing agent count (10-Q MD&A) declines more than 6% year on year for a second quarter running (the bear signal), or returns to growth (the bull signal that would raise conviction)."},
    {"text": "Health underwriting margin as a percent of premium (10-Q MD&A) falls below 22%."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 213.21, "basis": "Agent retention stabilises and ROE holds near 19.3% [RA], so the price re-rates to the blended base fair value of 213.21 led by P/B + ROE [fact sheet Fair value], helped by buybacks shrinking shares 4.84% YoY [ST]."},
    "base": {"probability": 0.5, "target_price_12m": 170.0, "basis": "Earnings grow modestly at roughly the current 10.5x P/E, above its 9.6x 5y median [RA], with buybacks adding per-share growth; set well below the blended base of 213.21 because the P/E method gives 143.09 and ROIC is falling (14.8% to 13.4%) [RA-T]."},
    "bear": {"probability": 0.25, "target_price_12m": 128.97, "basis": "A second quarter of American Income agent decline (10-Q, note section 2) and further health-claim pressure push ROIC lower, and the price falls to the mechanical bear fair value of 128.97 [fact sheet Fair value], near the 52-week low of 129.21 [HI]."}
  },
  "entry_price": 143.09,
  "entry_basis": "Valuation file: the P/E-method base fair value of 143.09 [IS] [RA]. The default anchor (base 213.21 x 0.8) sits above the price, and the blend leans on a ROE that is falling. At 143.09 even the earnings-based value covers the price, so the agent-attrition risk would be paid for.",
  "replaces": null,
  "replacement_reason": null
}
```

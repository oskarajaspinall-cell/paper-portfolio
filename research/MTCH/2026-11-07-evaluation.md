# Evaluation: Match Group, Inc. (MTCH) — 2026-11-07
## Bear case
The top line is shrinking. Q3 revenue was below the prior year, and Q4 is guided down 1% to flat (https://www.tipranks.com/news/the-fly/match-group-sees-q4-revenue-down-1-to-flat-at-865m-875m-thefly-news) [Certain]. The reverse DCF already prices -2.3% year-1 growth, which is close to that guide [OV]. So the low multiples (P/FCF 7.8x, EV/EBITDA 10.1x [RA]) mostly reflect a declining franchise, not a mispricing [Likely]. Management flags a 1-point EBITDA margin headwind from in-app fees in 2027 (transcript [OV]) [Certain]. Apple pulled Azar for weeks in 2026 (SEC 10-Q), which shows real platform dependence [Certain]. Leverage is still 2.51x net debt/EBITDA with 2027-28 maturities, and Altman Z is 1.13 [ST] [Certain]. The mechanical bear fair value of 17.98 is far below the 39.03 close, so the downside is wide [Certain]. Beta is 1.46 [ST].
## Bull case
The economics are excellent: ROIC 24.7%, gross margin 75.9%, operating margin 31.1% and FCF margin 32.7% TTM, with all but ROIC above their FY levels [RA,IS] [Certain]. The FCF yield is 12.84% [ST]. It funds a share count down 6.86% YoY and deleveraging from 3.50x to 2.51x [ST,RA] [Certain]. Every multiple sits at the bottom of its 5y range [RA] [Certain]. Tinder daily users returned to year-on-year growth in September after more than three years, and Hinge delivered double-digit revenue growth (https://www.prnewswire.com/news-releases/match-group-announces-third-quarter-results-302926778.html) [Certain]. If Tinder's user recovery turns into revenue in 2027, the price, which implies continued shrinkage, re-rates toward the base fair value of 48.83 [Likely]. Piotroski F is 7 [ST].
## Decision
```json
{
  "ticker": "MTCH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, 32.7%-FCF-margin dating franchise buying back stock at the bottom of its 5-year multiples, but the price already discounts the revenue decline management guides to, and the Tinder user recovery has not yet reached revenue.",
  "rationale": "The business is cheap and highly cash-generative, but the reverse DCF roughly matches guided Q4 revenue, so the edge depends on an unproven Tinder revenue turnaround. A 2027 fee headwind, platform risk, leverage and a far-lower bear value make it good but not compelling. Conviction 3: AVOID.",
  "price_at_decision": 39.03,
  "price_date": "2026-11-06",
  "research_note": "research/MTCH/2026-11-07.md",
  "triggers": [
    {"text": "Tinder revenue returns to year-on-year growth in a company quarterly release, confirming the user recovery is monetising (would raise conviction); a renewed Tinder user decline for two quarters would break it."},
    {"text": "Hinge revenue growth in the company quarterly release falls below 10% year on year, removing the offset to Tinder."},
    {"text": "TTM operating margin falls below 24%, the FY2024 level, showing in-app fee and reinvestment costs are eroding profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 24}},
    {"text": "Net debt / EBITDA rises above 3.0x, reversing the deleveraging from 3.50x to 2.51x ahead of 2027-28 maturities.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 54.56, "basis": "Tinder's DAU return to growth (PRNewswire Q3 release) reaches revenue and the price moves to the mechanical bull fair value of 54.56 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 42.95, "basis": "Revenue roughly flat, in line with the Q4 guide of down 1% to flat (TheFly headline [OV]), plus the 2027 in-app fee margin headwind (transcript [OV]); EV/Revenue base 42.95 is used rather than the 48.83 blended base because the DCF base assumes growth the guide does not yet show."},
    "bear": {"probability": 0.25, "target_price_12m": 31.19, "basis": "Tinder relapses and the fee headwind bites, so EV/Sales falls back toward its 5y low of 3.1x [RA], i.e. the EV/Revenue bear value of 31.19; the DCF bear of 17.98 assumes a sustained decline that buybacks and a 32.7% FCF margin [CF,IS] make less likely within 12 months."}
  },
  "entry_price": null,
  "entry_basis": "The price already sits at the default anchor (base 48.83 x 0.8), so price is not the obstacle: the missing evidence is Tinder revenue growth, and a lower price on the same evidence would not change the decision; re-research on the trigger above.",
  "replaces": null,
  "replacement_reason": null
}
```

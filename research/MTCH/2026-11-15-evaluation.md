# Evaluation: Match Group, Inc. (MTCH) — 2026-11-15
## Bear case
Growth is not back. Q3 revenue fell year over year while EPS rose, and Q4 is guided down 1% to flat (https://www.tipranks.com/news/the-fly/match-group-sees-q4-revenue-down-1-to-flat-at-865m-875m-thefly-news) [Certain]. Management flags a 1-point Adjusted EBITDA margin headwind from in-app fees in 2027 (transcript [OV]) [Certain], and Apple's removal of Azar shows real platform dependence (SEC 10-Q) [Certain]. The five-year operating margin and ROIC labels are falling; the last 12 months reversed that (operating margin 26.4% to 31.1% [IS-T]), but cost discipline on flat revenue, not growth, drives it, so the fee headwind could undo part of it [Likely]. The price is above its 200-day average (+12.5%) after a +26.2% year [ST,HI]: if the Tinder recovery stalls, that trend premium de-rates [Likely]. Net debt/EBITDA is 2.51x with maturities from December 2027, Altman Z 1.13, beta 1.46 [ST] [Certain]. The DCF bear value is 17.24 [Certain].
## Bull case
The economics are excellent and improving over the last year: ROIC 24.7%, ROCE 30.3%, operating margin 31.1% and FCF margin 32.7% TTM, all at or near their 2-year highs [RA-T,IS-T,CF-T] [Certain]. The FCF yield of 12.03% funds a share count down 6.86% YoY and deleveraging from 3.50x to 2.51x [ST,RA] [Certain]. P/E, EV/EBITDA and P/FCF sit in the bottom 1-5% of their five-year ranges [RA] [Certain], and the reverse DCF prices 0.0% year-1 revenue growth [Certain]. Tinder daily users returned to year-on-year growth after more than three years, and Hinge delivered double-digit revenue, user and payer growth (https://www.prnewswire.com/news-releases/match-group-announces-third-quarter-results-302926778.html) [Certain]. Relative strength versus SPY is +15.8pp over 12 months [HI] [Certain]. If user growth reaches Tinder revenue in 2027, the price moves toward the base fair value of 46.75 [Likely].
## Decision
```json
{
  "ticker": "MTCH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Over the last 1 and 3 years ROIC, operating margin and FCF margin are all flat or rising [RA-T,IS-T,CF-T]; only the 5-year fiscal endpoints show ROIC and operating margin lower.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Tinder's user recovery fails to reach revenue while the 2027 in-app fee headwind lands, de-rating a price now above its 200-day average.", "veto": null},
  "thesis": "A high-return, 32.7%-FCF-margin dating franchise buying back stock at the bottom of its five-year multiples, with Tinder users recovering but revenue still guided flat to down.",
  "rationale": "Quality, cash returns and trend are strong, but revenue is still shrinking and the base fair value is only modestly above the price; the scorecard keeps it below the buy bar.",
  "price_at_decision": 41.63,
  "price_date": "2026-11-13",
  "research_note": "research/MTCH/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 26%, showing in-app fees and reinvestment eroding profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 26}},
    {"text": "TTM FCF margin falls below 25%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "Net debt / EBITDA rises above 3.5x, reversing the deleveraging ahead of the 2027 maturities.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}},
    {"text": "Tinder daily-active-user growth in the company results release turns negative again for two consecutive quarters (breaks it); Tinder revenue returning to year-on-year growth would raise conviction."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 52.38, "basis": "Tinder's DAU return to growth (PRNewswire Q3 release) reaches revenue in 2027 and the price moves to the mechanical bull fair value of 52.38 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 42.95, "basis": "Revenue roughly flat, in line with the Q4 guide of down 1% to flat (TheFly headline [OV]) and the 2027 fee headwind (transcript [OV]); the EV/Revenue base of 42.95 is used rather than the 46.75 blend because the DCF base assumes growth the guide does not yet show."},
    "bear": {"probability": 0.25, "target_price_12m": 31.19, "basis": "Tinder relapses and the fee headwind bites, EV/Sales returns toward its 5y low of 3.1x [RA], the EV/Revenue bear value of 31.19; the DCF bear of 17.24 assumes a sustained decline that buybacks and a 32.7% FCF margin [CF,IS] make unlikely within 12 months."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the missing evidence is Tinder revenue growth, so a lower price on the same evidence would not justify conviction 4; re-research on the Tinder trigger.",
  "replaces": null,
  "replacement_reason": null
}
```

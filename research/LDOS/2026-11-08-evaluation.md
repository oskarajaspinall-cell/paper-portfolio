# Evaluation: Leidos Holdings (LDOS) — 2026-11-08

## Bear case
Returns are rolling over: TTM ROIC fell from 16.6% to 15.2% and ROCE from 19.3% to 17.1%, both more than 2pp below their 2-year highs [RA-T] [Certain]. The driver is the debt-funded Entrust deal: net debt/EBITDA rose from 1.77x to 2.46x [BS,IS] [Certain], and acquired capital has not yet earned its keep [Likely]. Operating margin is flat at 11.8% rather than expanding [IS-T] [Certain], and the 10-Q cites completed higher-margin contracts [company-reported] [Likely]. FY26 revenue guidance was cut, the Q3 call flagged uncertainty weighing on 2027 bottom-line growth, and funding runs only to December 11, 2026, so a shutdown could delay billings [Likely]. About 83% of revenue is US government [company-reported], so federal-budget risk is concentrated; no foreign-country exposure is material (macro overlay, weight context) [Likely]. The 50-day sits below the 200-day [ST] [Certain].

## Bull case
The price already discounts a severe reset: the reverse DCF implies -11.6% year-1 revenue growth [OV], against 4% Q3 growth and EPS guidance raised for the third consecutive quarter [Likely]. P/E 11.9x, EV/EBITDA 9.2x and P/FCF 8.3x are all below their own 5y minimums and at a discount to peers [RA] [Certain]. Cash is strengthening, not weakening: FCF margin rose from 8.0% to 11.0% TTM [CF-T] and FCF yield is 12.10% [ST] [Certain], funding deleveraging, a dividend raised to $0.45 and a share count down 3.42% YoY [ST] [Certain]. The ROIC/ROCE dip is a denominator effect from acquired capital, not a margin break; returns remain well above FY2021-23 levels [RA] [Likely]. Even the mechanical bear fair value of 145.50 sits above the 132.68 close [Certain], and beta of 0.55 limits market drag [ST] [Certain].

## Decision
```json
{
  "ticker": "LDOS",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A government-IT incumbent with ROIC still well above its FY2021-23 levels and an 11.0% FCF margin trades below its own 5-year minimum on every earnings multiple and below peers, where the price implies a -11.6% revenue decline that raised EPS guidance does not show.",
  "rationale": "Valuation still discounts a contraction that Q3 results and raised EPS guidance contradict, and cash generation is improving. The ROIC/ROCE slide is acquisition-driven, yet it, the revenue-guidance cut and 2027 uncertainty keep conviction at 4, not 5. The position is already at its ~7% target, so no ADD; HOLD.",
  "price_at_decision": 132.68,
  "price_date": "2026-11-06",
  "research_note": "research/LDOS/2026-11-08.md",
  "entry_price": null,
  "entry_basis": "Already conviction 4 and held at its full target size; price is not the obstacle to more, the position-size rule is (a fall below size is handled by the top-up rule), and the conviction-5 cap comes from falling returns and 2027 guidance uncertainty, which a lower price would not resolve.",
  "triggers": [
    {"text": "TTM operating margin falls below 10.5%, reversing most of the five-year expansion from 8.5% to 11.8% and showing contract completions are not being replaced at similar margins.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10.5}},
    {"text": "TTM ROIC falls below 13%, showing the decline from 16.6% is no longer a temporary acquisition denominator effect but deteriorating returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 13}},
    {"text": "TTM FCF margin falls below 8%, back to the level of a year earlier, showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "Net debt/EBITDA on the ratios page rises above 3.0x (2.46x TTM now) without a visible deleveraging path from the Entrust debt."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 190.0, "basis": "Guidance momentum continues and EV/EBITDA re-rates from 9.2x to around its 5y minimum of 11.2x [RA], landing just above the EV/EBITDA leg of 178.85 but well below the DCF-led bull of 290.19, which the note treats as optimistic (note section 3)."},
    "base": {"probability": 0.5, "target_price_12m": 160.0, "basis": "Flat 11.8% operating margin [IS-T] and 11.0% FCF margin [CF-T] hold while EV/EBITDA recovers partway toward its 5y minimum [RA]; set near the EV/EBITDA bear leg of 166.47 rather than the 270.01 blended base, because the DCF leg extrapolates growth the cut revenue guidance does not support."},
    "bear": {"probability": 0.25, "target_price_12m": 110.0, "basis": "A shutdown after December 11, 2026 plus the 2027 bottom-line uncertainty flagged on the Q3 call (note section 6) keep EV/EBITDA near 9.2x [RA] on lower EBITDA; set below the mechanical bear of 145.50 because that value assumes a multiple floor the market has already broken."}
  }
}
```

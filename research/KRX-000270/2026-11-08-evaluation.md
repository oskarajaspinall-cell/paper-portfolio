# Evaluation: Kia Corporation (KRX:000270) — 2026-11-08
## Bear case
Profitability is rolling over fast. The Direction change lines show TTM ROIC down from 22.0% to 14.1%, ROCE from 17.2% to 10.9% and operating margin from 10.2% to 6.8% within twelve months, each well below its 2-year high [Certain] [RA-T, IS-T]. The driver is incentives and FX squeezing profit despite record volumes (Q2 call) [Likely]: pricing power is thin, so record US sales do not protect margin [Likely]. This directly threatens any re-rating thesis. P/E of 5.5x is above its own 5y median of 4.5x, so on earnings the stock is not cheap against its own history; the peer gap reflects a structural Korean discount [Likely]. The through-cycle DCF base of 433,711.84 assumes mid-cycle margins the last year contradicts; EV/EBITDA gives 99,724.72, roughly the price [Certain]. Q3 figures are absent, US tariff risk is unverified (macro overlay), and the price is -30.7% vs the 200-day [Certain].

## Bull case
The balance sheet is a fortress: net debt/EBITDA -1.91x, Altman Z 3.02, Piotroski 6 [Certain] [ST]. FCF yield is 17.24% and FCF conversion recovered to 95.2% TTM [Certain] [ST, CF]. EV/EBITDA of 1.5x sits at 14% of its 5y range and P/B of 0.6x is below its five-year minimum, versus peer medians of 9.7x and 0.8x [Certain] [RA]. Even the mechanical bear fair value of 175,113.26 is above the 100,300.00 close [Certain]. Demand is real: Kia America reported a sixth consecutive record month in October [Likely]. A 6.8% operating margin is still respectable for a mass-market maker [Guessing], the share count is shrinking (-1.02% YoY) [Certain], and a mild dollar tailwind helps exports (macro overlay) [Likely]. If incentives normalise, earnings could recover from a depressed base [Guessing].

## Decision
```json
{
  "ticker": "KRX:000270",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash automaker at a very low EV/EBITDA and P/B, but with returns and margins falling sharply on incentives and FX, so the cheapness reflects a cyclical earnings downturn not yet shown to have bottomed.",
  "rationale": "Cheap on cash and book, but ROIC, ROCE and operating margin are all falling hard over the last year, P/E is above its own 5y median, the EV/EBITDA fair value sits near the price, Q3 figures are unverified and tariff risk is unsized. Good but not compelling: conviction 3, no position.",
  "price_at_decision": 100300.00,
  "price_date": "2026-11-06",
  "research_note": "research/KRX-000270/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 5% (6.8% now, 10.2% a year earlier), showing incentive pressure is structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 5}},
    {"text": "TTM ROIC falls below 10% (14.1% now), below the FY2021 level of 14.4% and confirming the downcycle is deepening.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 3% (5.6% now), eroding the cash-yield support.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 3}},
    {"text": "Net debt/EBITDA turns positive (above 0x, -1.91x now), removing the net-cash cushion.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 120697.76, "basis": "Incentives ease and operating margin recovers toward its 2-year high of 12.0% [IS-T]: the mechanical EV/EBITDA bull value of 120,697.76 [fact sheet Fair value]; below the DCF-led blend bull of 430,736.36 because that DCF assumes mid-cycle margins the last twelve months contradict."},
    "base": {"probability": 0.45, "target_price_12m": 99724.72, "basis": "Margins stabilise near the TTM 6.8% [IS] and EV/EBITDA stays near its 5y median of 1.6x [RA]: the mechanical EV/EBITDA base of 99,724.72, not the through-cycle DCF base, which extrapolates FY2023-24 returns now falling [RA-T]."},
    "bear": {"probability": 0.30, "target_price_12m": 90403.38, "basis": "Operating margin keeps sliding as in the last year (10.2% to 6.8%) [IS-T] with unverified US tariff risk (research/KRX-000270/2026-11-08-macro.md): the mechanical EV/EBITDA bear value of 90,403.38 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below every mechanical bear value except EV/EBITDA; the obstacle is the sharp fall in ROIC, ROCE and operating margin over the last year. A lower price would not change the decision; evidence of margin stabilisation in reported results would.",
  "replaces": null,
  "replacement_reason": null
}
```

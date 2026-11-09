# Evaluation: Kia Corporation (KRX:000270) — 2026-11-09
## Bear case
The Direction change lines are real: TTM ROIC fell from 22.0% to 14.1%, ROCE from 17.2% to 10.9% and operating margin from 10.2% to 6.8%, each far below its 2-year high [Certain] [RA-T, IS-T]. The cause looks cyclical rather than structural: the Q2 call blamed incentives and FX while sales hit records and share rose, so the business model is not broken [Likely]. But incentive dependence shows thin pricing power, and no evidence shows the margin has bottomed: Q3 figures are absent from the fact sheet [Certain]. On its own history the stock is not cheap on earnings: P/E 5.5x is above its 5y median of 4.5x and P/FCF 5.8x above its 4.4x median [Certain] [RA]; the peer gap reflects a lasting Korean discount [Likely]. The EV/EBITDA fair value of 99,724.72 sits at the price [Certain]. US tariff risk is unverified and unsized (macro overlay) [Likely].

## Bull case
Read correctly, this is a cyclical margin reset in a fortress balance sheet: net debt/EBITDA -1.91x, Altman Z 3.02, Piotroski 6 [Certain] [ST]. Operating margin of 6.8% is back near the FY2021 level of 7.3%, not a collapse, while volumes are at records (Kia America's sixth consecutive record month) [Likely]. Cash keeps coming: FCF yield 17.24%, FCF conversion back to 95.2% TTM, shares down 1.02% YoY [Certain] [ST, CF]. P/B of 0.6x is below its five-year minimum and EV/EBITDA 1.5x sits at 14% of its 5y range, against peer medians of 0.8x and 9.7x [Certain] [RA]. The price already fell to a 6-month low of 87,900 after Q3 [Certain] [HI]. If incentives normalise toward the FY2025 margin of 8.0%, earnings recover from a depressed base and the through-cycle DCF base of 433,711.84 shows the mid-cycle value [Guessing]. A firmer dollar helps exports (macro overlay) [Likely].

## Decision
```json
{
  "ticker": "KRX:000270",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash automaker in a cyclical, incentive- and FX-driven margin reset (not a structural decline) trading below its 5-year P/B minimum, but on earnings and FCF multiples at or above its own 5-year medians, so the 12-month skew is positive yet modest.",
  "rationale": "The fall in returns reads as cyclical with the balance sheet intact, so direction is not the obstacle. Price is: P/E and P/FCF sit above their own 5y medians, the EV/EBITDA value equals the price, no trough is evidenced and tariffs are unsized. Expected value only modestly above the price: good, not compelling. Conviction 3, no position.",
  "price_at_decision": 100300.00,
  "price_date": "2026-11-06",
  "research_note": "research/KRX-000270/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 5% (6.8% now, 10.2% a year earlier), showing incentive pressure is structural rather than cyclical.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 5}},
    {"text": "TTM ROIC falls below 10% (14.1% now), below the FY2021 level of 14.4% and confirming the downcycle is deepening.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 3% (5.6% now), eroding the cash-yield support.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 3}},
    {"text": "Net debt/EBITDA turns positive (above 0x, -1.91x now), removing the net-cash cushion that makes the reset survivable.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 133700, "basis": "Incentives ease and operating margin recovers toward the FY2025 8.0% [IS] while P/B returns to its 5y median 0.8x from 0.6x [RA]; well below the DCF-led blend bull of 430,736.36 because that DCF assumes mid-cycle margins not yet evidenced."},
    "base": {"probability": 0.45, "target_price_12m": 105000, "basis": "Margins stabilise near the TTM 6.8% [IS-T] and EV/EBITDA holds near its 5y median 1.6x [RA] (mechanical EV/EBITDA base 99,724.72), plus a year of cash retained at the 17.24% FCF yield [ST]; below the blend base of 322,382.80, whose through-cycle DCF is not supported by own-history P/E of 4.5x [RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 82064, "basis": "The operating-margin slide of the last year (10.2% to 6.8%) [IS-T] continues with unverified US tariff risk (research/KRX-000270/2026-11-08-macro.md) and P/E reverts from 5.5x to its 5y median 4.5x [RA] on TTM earnings."}
  },
  "entry_price": 82064,
  "entry_basis": "P/E back at its 5y median of 4.5x [RA] on TTM earnings (the base fair value less 20% is above the price, so not usable): at that level P/B would sit far below its 5y minimum of 0.6x and the net-cash, cyclical-reset case would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

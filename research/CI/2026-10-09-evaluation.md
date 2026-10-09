# Evaluation: The Cigna Group (CI) — 2026-10-09
## Bear case
Margins are eroding structurally, not cyclically: gross margin fell from 13.2% to 9.1% and operating margin from 4.7% to 3.9% over five years [Certain] (IS). On a 2.3% net margin, small medical-cost or PBM-reform shocks wipe out a large share of earnings [Likely]. The shift from rebates to the fee-based "Signature" model is a live, unproven economic reset of Evernorth, the growth engine [Likely] (investor-day transcript, OV). The $3bn modernization programme spends cash that would otherwise fund buybacks [Likely] (OV news). The tape agrees: CI lags SPY by 24.2pp over 12 months, and short interest rose 25.2% in a month [Certain] (HI, ST). Multiples below their 5-year minimums may reflect the whole sector being de-rated for regulatory reasons, not mispricing [Guessing]. The DCF fair value ($793 base) is inflated by thin-margin, high-FCF-conversion arithmetic and should not be trusted [Likely].

## Bull case
The price assumes distress. The reverse DCF implies -16.0% year-one revenue [Certain] (fact sheet), yet management reaffirmed FY26 guidance at the 2026-09-30 investor day [Likely] (OV news). P/E 11.5x, EV/EBITDA 7.7x and P/FCF 8.1x all sit below their own 5-year minimums and 42-51% below peers [Certain] (RA, peers). Quality is rising: ROIC went from 8.8% to 13.4%, ROE to 16.8%, FCF conversion is 142.0%, and net debt/EBITDA fell from 2.84x to 1.93x [Certain] (RA). The 12.29% FCF yield funds a 3.55% annual share-count reduction [Certain] (ST), so holders compound even with no re-rating. A beta of 0.30 diversifies a book weighted to technology [Certain] (ST). The conservative P/E method alone gives fair value of $298-$410 [Certain] (fact sheet), above the $281.03 close.

## Decision
```json
{
  "ticker": "CI",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A deleveraging managed-care and PBM franchise with ROIC rising to 13.4% and a 12.29% FCF yield trades below its own 5-year minimum P/E, EV/EBITDA and P/FCF, where the price implies a -16% revenue decline that reaffirmed guidance does not support.",
  "rationale": "Every cash-flow multiple is below its 5-year floor, and returns, leverage and buybacks are all improving, so the downside is cushioned by cash yield. PBM-reform risk and a 2.3% net margin cap conviction at 4, not 5. A 7% position takes Healthcare to about 14% alongside ZTS, well within the 30% cap, and cash covers it.",
  "target_weight_pct": 7,
  "price_at_decision": 281.03,
  "price_date": "2026-10-08",
  "research_note": "research/CI/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 9%, giving up the five-year improvement from 8.8% to 13.4%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "TTM operating margin falls below 3.5%, under the FY2025 five-year low of 3.7%, showing PBM reform or medical-cost pressure is compressing profitability structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 3.5}},
    {"text": "TTM net margin falls below 1.5%, near the FY2024 trough of 1.4%, confirming margin compression is structural.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 1.5}},
    {"text": "TTM FCF margin falls below 2.5%, under the five-year low of 3.1%, signalling earnings quality and buyback capacity are deteriorating.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 365.44, "basis": "P/E re-rates toward its 5-year median of 15.1x [RA] as Signature-model economics prove out, matching the fact sheet's P/E-method base fair value of 365.44; the DCF values (base 1,006.86) are set aside as inflated by thin-margin arithmetic."},
    "base": {"probability": 0.5, "target_price_12m": 298.47, "basis": "P/E recovers only to about its 5-year minimum of 12.3x [RA] on reaffirmed guidance [OV news], in line with the fact sheet's P/E-method bear fair value of 298.47, which is well below the DCF-led blend because CI's 2.3% net margin makes the DCF unreliable."},
    "bear": {"probability": 0.2, "target_price_12m": 239.51, "basis": "PBM reform or medical-cost pressure extends the five-year gross-margin decline (13.2% to 9.1%) [IS], and the stock retests its 52-week low of 239.51 [HI], below every mechanical fair value."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

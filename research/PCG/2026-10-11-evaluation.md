# Evaluation: PG&E Corporation (PCG) — 2026-10-11
## Bear case
PCG is cheap for a reason. The equity carries wildfire liability with no legislative backstop: the reform bill was shelved and the CEO said that "crushed" the stock [Certain]. The business burns cash (FCF margin -16.5% TTM, FCF/NI -139.5%) and funds it with 6.19x net debt/EBITDA and 3.06% annual share issuance [Certain]. Management's strategic review and $2bn 2027 capex cut show the balance sheet is not investment grade [Likely]. ROCE of 4.4% and ROE of 9.3% are low for a regulated utility [Certain]. The 5,000-mile undergrounding plan adds more capex and financing need [Likely]. Fair value sits at $10.13 base and $10.66 bull, both below the $13.13 close, because the $0.05 quarterly dividend supports little intrinsic value [Certain]. The macro overlay says rising rates and HY spreads (10y +68bp in 3m) push against a levered, cash-burning issuer [Likely].

## Bull case
Every multiple is below its 5-year minimum: P/E 9.5x vs a 13.6x floor, EV/EBITDA 8.9x vs 9.7x, P/B 0.9x vs 1.1x. P/E is also 51% under the peer median of 19.4x [Certain]. Fundamentals are improving, not breaking: net margin rose to 11.8% TTM, net debt/EBITDA fell from 8.03x in FY2023 to 6.19x and Piotroski is 6 [Certain]. A regulated monopoly has no competitive threat [Certain]. If California revives wildfire reform, the liability discount could close quickly toward the 5y-minimum P/E [Guessing]. The capex cut should narrow cash burn and support credit repair [Likely]. Short interest is only 1.88% [Certain]. Still, the re-rating hinges on a legislative event that nobody can time or size, so this is an option, not a thesis.

## Decision
```json
{
  "ticker": "PCG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "PCG looks cheap on peer and own-history multiples, but negative free cash flow, 6.19x leverage, ongoing dilution and an unresolved wildfire-liability regime mean the discount is a fair price for binary regulatory risk, not a mispricing.",
  "rationale": "Re-rating depends on California wildfire reform, a political event we cannot time. Cash burn (FCF margin -16.5%), leverage and dilution weigh on per-share value meanwhile. Mechanical fair value ($10.13 base) sits below price and macro tilts bearish. Expected 12-month value is roughly flat with a fat left tail. Conviction 2, so no position.",
  "price_at_decision": 13.13,
  "price_date": "2026-10-09",
  "research_note": "research/PCG/2026-10-11.md",
  "triggers": [
    {"text": "California enacts wildfire-liability reform that caps utility exposure or durably replenishes the wildfire fund (PG&E IR / filing), removing the binary overhang behind the discount.", "check": null},
    {"text": "TTM FCF margin improves above -5% (vs -16.5% now), showing the capex cut is turning cash burn toward self-funding.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": -5}},
    {"text": "Share count growth falls below 1% YoY (vs 3.06% now), showing equity dilution to fund the balance sheet has largely ended.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": 1}},
    {"text": "TTM ROE rises above 10.5% (vs 9.3% now), showing allowed returns are converting into peer-like equity returns.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 10.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 18.8, "basis": "Wildfire reform is revived (CEO call for reform, CNBC 2026-09-02 headline) and P/E re-rates to its 5y minimum of 13.6x [RA] on TTM EPS implied by 13.13 / 9.5x, so the bull case sits above mechanical fair value because that model cannot capture removal of the liability discount."},
    "base": {"probability": 0.45, "target_price_12m": 13.13, "basis": "No reform and continued cash burn (FCF margin -16.5% [CF,IS]) and 3.06% dilution [ST] keep P/E near today's 9.5x [RA], offsetting earnings growth; this is above the $10.13 base fair value because peer-relative P/E (19.4x median) supports the market price."},
    "bear": {"probability": 0.35, "target_price_12m": 10.13, "basis": "Fund-depletion risk and rising financing costs push the price to the fact sheet's DDM/P-E base fair value of $10.13; the macro overlay (research/PCG/2026-10-11-macro.md, tilt moderate toward bear: 10y +68bp, HY spread +45bp over 3m) shifts 0.05 probability from base to bear."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

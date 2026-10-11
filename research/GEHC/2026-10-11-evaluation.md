# Evaluation: GE HealthCare Technologies Inc. (GEHC) — 2026-10-11
## Bear case
The price of $65.74 is already 10.1% above the base fair value of $59.13, and the reverse DCF implies 8.3% year-1 revenue growth. That is a demanding ask for a business whose operating margin (14.0%, -1.0pp), net margin (9.3%, -2.7pp) and ROCE (10.3%, -3.3pp) are all falling [Certain]. Net debt/EBITDA has climbed to 2.36x TTM before the $945m cash-funded Sofie deal, and the Altman Z of 1.92 sits in the grey zone [Certain]. In imaging, Siemens, Philips, United Imaging and Mindray contest the moat, and lower-cost Chinese entrants are pressing on price [Likely]. Macro adds to the pressure: the 10y real yield is up 0.56pp in 3 months and HY spreads are up 0.45pp, which raise the discount rate and refinancing cost on newly added debt [Likely]. The stock lags SPY by 28.2pp over 12 months, and Q3 results come on Oct 28 [Certain].
## Bull case
On 15.1x P/E the stock sits at the 11th percentile of its own 5y range and 25% below peers. EV/EBITDA of 10.6x is 17% below the peer median [Certain]. P/B of 2.7x is below its own 5y minimum [Certain]. FCF conversion has improved to 79.5% and the dividend was raised 14% [Certain]. Sofie gives PDx, the fastest-growing segment, a US "final mile" in PET radiopharma supply [Likely]. A large installed base keeps service and consumable revenue recurring [Likely]. If margins return to the FY2024 operating level of 15.5%, the bull fair value of $74.31 is reachable [Guessing]. Low beta (0.85) and modest short interest (3.76%, falling) point to no crowding [Certain].
## Decision
```json
{
  "ticker": "GEHC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A franchise imaging and radiopharma business that looks cheap against peers and its own P/E history, but at $65.74 it trades above its $59.13 base fair value while margins and returns drift down and leverage rises into a cash-funded acquisition.",
  "rationale": "The multiples are low for a reason: operating and net margins and ROCE are falling, and leverage is rising before Sofie closes. The price already implies 8.3% growth, and the probability-weighted value sits below the close. A moderate macro bear tilt adds to this. Good but not compelling, so the answer is AVOID; re-look nearer the margin-of-safety entry or on proof of margin recovery.",
  "price_at_decision": 65.74,
  "price_date": "2026-10-09",
  "research_note": "research/GEHC/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 15.5%, back to the FY2024 level, showing the margin drift has reversed (would raise conviction).", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 15.5}},
    {"text": "Net debt/EBITDA rises above 3.0x after the Sofie acquisition, confirming the leverage concern (would lower conviction further).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}},
    {"text": "TTM gross margin falls below 38%, signalling price pressure from lower-cost imaging competitors.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 38}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 74.31, "basis": "Operating margin recovers toward the FY2024 level of 15.5% [IS] and PDx/Sofie growth supports the fact sheet's bull fair value of $74.31 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 59.13, "basis": "Margins hold near the TTM 14.0% operating level [IS] and the price converges on the blended DCF/P-E base fair value of $59.13 [IS,BS,CF,RA,ST,HI]; at that level P/E sits near its 5y low of 13.9x [RA]."},
    "bear": {"probability": 0.3, "target_price_12m": 44.68, "basis": "Margins keep falling and net debt/EBITDA rises from 2.36x [BS,IS] after the cash-funded Sofie deal, giving the bear fair value of $44.68 [IS,BS,CF,RA,ST,HI]; probability raised 5pp for the macro overlay's moderate bear tilt (rising real yields and HY spreads, research/GEHC/2026-10-11-macro.md)."}
  },
  "entry_price": 47.3,
  "entry_basis": "valuation file: base 59.13 x 0.8 = 47.30; at that level the falling-margin risk is priced with a margin of safety.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Arthur J. Gallagher & Co. (AJG) — 2026-10-12
## Bear case
The roll-up is earning less on each dollar it deploys: ROIC fell from 10.5% (FY2021) to 6.6% TTM and ROE from 12.9% to 6.7% [RA] [Certain]. Acquisitions are funded with debt and stock: net debt/EBITDA is 2.97x TTM, up from net cash in FY2024, and shares rose 6.58% YoY [RA, ST] [Certain]. Even after a -24.2% year, the stock trades at a +103% P/E and +54% P/FCF premium to MMC/AON/WTW/BRO [RA, peers] [Certain]. The cheap P/B mostly reflects goodwill, not tangible value [Likely]. Base fair value of 236.20 is only +1.5% above the 232.70 close, so there is no margin of safety [Certain]. Management's own investor update says property pricing is easing [OV transcript] [Likely]. The macro overlay finds that a +56bp/3m rise in real yields hits a premium-multiple, debt-funded compounder harder than its peers [macro] [Likely].

## Bull case
This is a durable franchise. Operating margin rose to 19.9% TTM and gross margin to 43.2% [IS] [Certain]. FCF conversion of 145.7% shows cash earnings run well above reported net income, which is held down by amortisation of acquired intangibles [CF, IS] [Likely]. On P/E (38.6x) and P/FCF (26.1x) the stock sits at or below the bottom of its own 5-year range, and EV/EBITDA (16.9x) is below its 5-year minimum of 20.1x [RA] [Certain]. Management guides Q3 organic growth to about 6%, and tuck-in deals continue (Ornella, Winter & Co, Albany) [OV news] [Likely]. If ROIC stabilises as the large acquisition is absorbed, a P/E re-rating toward the 44.5x median would support the 292–315 bull range [Guessing]. Beta is 0.55 and short interest is low at 3.25% [ST] [Certain].

## Decision
```json
{
  "ticker": "AJG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality broker franchise whose returns on capital are falling as its debt- and stock-funded roll-up expands, trading near base fair value at a large peer premium, so the risk/reward is not compelling.",
  "rationale": "The business has a real moat and improving margins, but ROIC and ROE are declining, leverage and dilution are rising, and the stock still carries a large peer premium. With price near base fair value, there is no margin of safety. The macro tilt is toward the bear case. Good but not compelling, so AVOID until the price offers a cushion.",
  "price_at_decision": 232.70,
  "price_date": "2026-10-09",
  "research_note": "research/AJG/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC recovers above the FY2024 level of 9.3%, showing recent acquisitions earn adequate returns.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 9.3}},
    {"text": "TTM FCF margin recovers above the FY2024 level of 22.3%, showing cash generation is keeping up with M&A.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 22.3}},
    {"text": "Net debt/EBITDA (ratios page, site definition) falls below the FY2022 level of 2.65x, evidencing deleveraging after the 2025 acquisition wave."},
    {"text": "Organic brokerage growth disclosed in the Q3 2026 or later earnings release reaccelerates to double digits, justifying the peer premium."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 292.08, "basis": "P/E re-rates toward its 5y median of 44.5x [RA] as ROIC stabilises after the acquisition, matching the fact sheet's P/E bull value of 292.08 (below the 315.46 blended bull, because the EV/EBITDA bull leg assumes a re-rating far above today's 16.9x)."},
    "base": {"probability": 0.45, "target_price_12m": 236.2, "basis": "Margins hold (operating margin 19.9% TTM [IS]), but falling ROIC (6.6% TTM [RA]) caps the multiple, so the price tracks the fact sheet's base fair value of 236.20."},
    "bear": {"probability": 0.35, "target_price_12m": 192.54, "basis": "ROIC/ROE keep falling and leverage stays near 2.97x [RA]; the multiple compresses to the fact sheet's bear fair value of 192.54, near the 6-month low of 190.75 [HI]. Bear probability was raised moderately per the macro overlay's tilt toward bear (research/AJG/2026-10-12-macro.md: +56bp/3m real yields hit a premium, debt-funded roll-up)."}
  },
  "entry_price": 188.96,
  "entry_basis": "valuation file: base 236.20 x 0.8; at that price the same evidence (moat and margins against falling ROIC) would carry a margin of safety that justifies conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

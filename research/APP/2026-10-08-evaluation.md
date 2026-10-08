# Evaluation: AppLovin Corporation (APP) — 2026-10-08
## Bear case
The class actions target the moat itself. They allege AppLovin misled investors on the strength of its AI models and its AI video creative tool [Certain], so the AXON flywheel behind the 77.4% operating margin is now disputed [Likely]. The court denied AppLovin's restraining order against Unity's Ad Quality SDK, which lets a rival tool into the ecosystem [Certain]. San Diego County has added a consumer-protection suit [Certain]. The 30 June 10-Q predates all of this, so the size of any liability is unknown [Guessing]. Beta is 2.56 [Certain], and the macro overlay tilts moderately toward bear because the 10y real yield rose +0.61pp over 3m [Certain]. The FCF yield is only 4.81% [Certain], so there is little cushion if margins normalise. Momentum is -56.8% over 12m [Certain], and Q3 results on Nov 4 come before the litigation is resolved [Likely].

## Bull case
On every metric the business has got better. TTM ROIC is 132.7%, the FCF margin is 66.3% and net debt/EBITDA is 0.09x [Certain]. The P/E of 21.6x is below the 5y minimum of 37.8x [Certain], and P/FCF is 20.8x versus a peer median of 41.0x [Certain]. All of the de-rating has come from the share price, not from earnings [Certain]. Shares outstanding fell 1.81% YoY [Certain] and FCF conversion is 102.7% [Certain], so buybacks continue. The suits are allegations, not findings [Guessing]. Piotroski F of 7 and Altman Z of 24.42 show no financial stress [Certain]. If Q3 margins hold, the litigation discount could unwind quickly in a beta-2.56 stock [Guessing].

## Decision
```json
{
  "ticker": "APP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "An exceptional-return ad platform trades below its own 5-year minimum P/E, but securities suits attack the credibility of the AI engine that produces those returns, so the discount may be justified rather than an opportunity.",
  "rationale": "The quality and the de-rating are real, but the open risk is to the moat itself: the AI-claims litigation and the Unity ruling. Add beta 2.56, a 4.81% FCF yield and a bear macro tilt, and this is good but not compelling. Conviction 3 is below the buy threshold, so AVOID and keep the cash.",
  "price_at_decision": 281.29,
  "price_date": "2026-10-07",
  "research_note": "research/APP/2026-10-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2024 level of 59.3%, showing AXON's advantage is eroding (confirms AVOID).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 59.3}},
    {"text": "TTM FCF margin falls below the FY2023 level of 57.6%, showing monetisation efficiency is deteriorating (confirms AVOID).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 57.6}},
    {"text": "Share count turns to net dilution year over year, ending capital return.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "The Q3 2026 10-Q (results Nov 4, 2026) discloses no material loss contingency from the AI-claims class actions while operating margin holds above FY2025's 75.8%; this would lift conviction and warrant re-initiation."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 492.26, "basis": "The litigation overhang clears and P/E re-rates to its 5y minimum of 37.8x [RA] on unchanged TTM earnings implied by the 21.6x current P/E [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 281.29, "basis": "Margins hold (TTM operating margin 77.4% [IS]), but the lead-plaintiff process and the Unity ruling keep EV/EBITDA near its current bottom-quarter 17.5x [RA], so the price stays flat."},
    "bear": {"probability": 0.30, "target_price_12m": 212.13, "basis": "The FCF margin falls from 66.3% to the 50% thesis-break level [CF,IS] at an unchanged 20.8x P/FCF [RA]; probability raised from 0.25 for the moderate bear tilt from rising real yields in research/APP/2026-10-08-macro.md."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

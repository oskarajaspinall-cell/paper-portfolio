# Evaluation: T-Mobile US, Inc. (TMUS) — 2026-10-09
## Bear case
The market's -24.8% 12-month move and -40.4pp underperformance vs SPY [Certain] look like a repricing of industry structure, not a mispricing. A SpaceX spectrum deal hit all three US carriers on 2026-10-08 [Certain], and Mint's "any plan for $10/month" offer the same day suggests promotional intensity is rising [Likely]. The bull case depends on margins holding, yet that is exactly what a satellite entrant plus a price war would test [Guessing]. Leverage amplifies any EBITDA miss: net debt/EBITDA is still 3.42x, Altman Z 1.80 [Certain], and the macro overlay shows 10y real yields up 0.61pp in three months with the curve pricing more tightening, a moderate bear tilt for a levered bond proxy [Likely]. The DCF base of 275.91 extrapolates merger-era growth; the reverse DCF says the market expects revenue to fall 6.1% [Certain]. Q3 results on Oct 28 will be the first read on all of this [Certain].
## Bull case
Every fundamental is moving the right way. ROIC has risen five years straight to 8.9%, operating margin to 22.1% and FCF margin to 20.0% [Certain], while leverage fell from 4.08x to 3.42x [Certain]. The stock trades below its own 5-year minimum on P/E (18.0x), EV/EBITDA (8.8x) and P/FCF (10.0x) at a 10.01% FCF yield [Certain]. Shares fell 3.93% YoY on buybacks and the dividend was raised 15% [Certain]. Even the EV/EBITDA method's bear value of 186.15 sits above the 171.31 close [Certain]. Satellite-to-device service is a coverage complement with physics limits on capacity, and the carriers' own JV hedges it [Likely]. If yields stabilise, a re-rating toward the 5y median 10.5x EV/EBITDA is the obvious path [Likely].
## Decision
```json
{
  "ticker": "TMUS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraging, rising-ROIC wireless leader at a 10% FCF yield and below its 5-year minimum multiples, but with a fresh, unquantified competitive threat (SpaceX spectrum, $10 Mint promotion) hitting a 3.42x-levered balance sheet as real yields rise.",
  "rationale": "Valuation is compelling, yet the October 8 SpaceX spectrum shock and visible promotional pricing are unresolved, and margins are where the risk sits. Leverage and a moderate bear macro tilt magnify that. Q3 results on October 28 give the evidence within weeks. Good but not compelling, so conviction 3 and no position.",
  "price_at_decision": 171.31,
  "price_date": "2026-10-08",
  "research_note": "research/TMUS/2026-10-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2023 level of 19.5%, showing new-entrant and promotional pressure is eroding pricing power.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 19.5}},
    {"text": "TTM FCF margin falls below the FY2024 level of 16.5%, showing the cash-generation step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 16.5}},
    {"text": "TTM ROIC falls below the FY2024 level of 8.1%, reversing the five-year rise in returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8.1}},
    {"text": "Q3 2026 results (Oct 28) show operating margin holding at or above the 22.1% TTM level despite the Mint promotion and SpaceX spectrum entry; that would lift conviction and prompt re-research."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 220.0, "basis": "Margins hold and EV/EBITDA re-rates toward its 5y median 10.5x [RA], matching the EV/EBITDA method's base value of 220.17 [fact sheet fair value]; probability trimmed from 0.30 for the moderate bear macro tilt (research/TMUS/2026-10-09-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 186.0, "basis": "EV/EBITDA recovers only to its 5y minimum 9.4x [RA] on flat TTM EBITDA, the EV/EBITDA method's bear value of 186.15; below the DCF base of 275.91 because that DCF extrapolates merger-era revenue growth that the reverse DCF (-6.1%) and the SpaceX spectrum news [OV] contradict."},
    "bear": {"probability": 0.30, "target_price_12m": 150.0, "basis": "Satellite entry and promotional pricing (SpaceX spectrum deal and Mint $10 offer [OV]) push operating margin back toward the FY2023 level of 19.5% [IS] while EV/EBITDA stays at 8.8x [RA], with 3.42x net leverage [BS,IS] magnifying the equity hit; probability raised from 0.25 for the moderate bear macro tilt (research/TMUS/2026-10-09-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: at a 10.01% FCF yield and below 5-year minimum multiples [RA,ST] valuation already supports a position; the missing evidence is whether margins survive the SpaceX spectrum entry and promotional pricing, which Q3 2026 results on Oct 28 will show. A lower price before then would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

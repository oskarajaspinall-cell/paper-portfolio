# Evaluation: LVMH Moët Hennessy - Louis Vuitton (EPA:MC) — 2026-11-16
## Bear case
The price fell to our entry level with no earnings reaction in the last 10 sessions: this is the same sector slump, not new information [Certain]. Returns are still eroding: ROIC fell from 19.6% (FY2021) to 12.4% TTM, 4.2pp below its 2-year high, and operating margin is 3.7pp below its 2-year high of 25.5% [Certain]. The cheap multiples (P/E 18.4x, below the 5y minimum of 24.1x) sit on earnings that may still be falling, so the discount can be a value trap [Likely]. Gucci cutting prices raises the risk that the sector's pricing power, the core of the moat, is being tested; if LV must follow, gross margin (66.4%) compresses [Guessing]. China exposure is unsized and drives the demand slump [Likely]. The price is 12.5% below its 200-day average and down 36.6% in a year: no trend support [Certain]. The DCF alone (419.26) is barely above the price [Certain].

## Bull case
This is a cyclical trough with the balance sheet intact: net debt/EBITDA 1.24x, Altman Z 3.36 [Certain]. The last 12 months are flat, not collapsing: operating margin +0.2pp and FCF margin +0.7pp to an 18.0% TTM high, with FCF conversion at 132.1% [Certain]. Every multiple sits below its own 5y minimum and roughly half the peer median; FCF yield is 7.17% [Certain]. The reverse DCF implies only 2.1% year-1 revenue growth [Certain]. Louis Vuitton declining to cut prices suggests brand discipline [Guessing], and a small net buyback (-0.61% shares) adds per-share value [Certain]. A recovery in demand would lift both margin and multiple from trough levels [Likely].

## Decision
```json
{
  "ticker": "EPA:MC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years: the last 12 months are flat (ROIC -0.8pp, operating margin +0.2pp, FCF margin at its 18.0% TTM high [RA-T, IS-T, CF-T]). The level sits below the 2-year highs after the sector-wide demand slump tied to Chinese customers (https://nypost.com/2026/10/23/business/luxury-loses-its-sheen-as-lvmh-kering-and-hermes-stocks-all-plunge-amid-declining-sales/), with net debt/EBITDA at 1.24x [RA]: a cyclical trough with the balance sheet intact, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "The luxury demand slump persists and sector price cuts (https://www.wsj.com/business/retail/gucci-is-cutting-prices-louis-vuitton-is-reluctant-to-follow-the-trend-50e4b218) force LV to follow, pushing margins and ROIC lower so the low multiples prove a value trap.",
    "veto": null
  },
  "thesis": "The world's largest luxury group trades below every own-history multiple at a 7.17% FCF yield in a cyclical demand trough, but returns are still well below their 2-year highs and the mechanical upside is modest.",
  "rationale": "Scorecard conviction 3: a strong franchise at a real discount, but ROIC of 12.4% only earns one quality point, the base fair-value upside is modest and the price fell to our entry level on the same sector slump, not new evidence. Good but not compelling, so AVOID; the entry price watches for a deeper discount.",
  "price_at_decision": 403.45,
  "price_date": "2026-11-13",
  "research_note": "research/EPA-MC/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 19% (21.8% now), showing the slump is structural rather than cyclical.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 19}},
    {"text": "TTM ROIC falls below 10% (12.4% now), losing the quality that makes the discount worth owning.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM gross margin falls below 63% (66.4% now), showing price cuts are eroding brand pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 63}},
    {"text": "Net debt/EBITDA rises above 2.0x (1.24x now), removing the balance-sheet cushion through the trough.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 555.11, "basis": "Demand recovers and earnings re-rate toward the P/E method's base of 555.11 [fact sheet fair value], still below the 5y minimum P/E of 24.1x [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 464.54, "basis": "Flat margins (operating +0.2pp, FCF at an 18.0% TTM high [IS-T, CF-T]) support the mechanical base fair value of 464.54 [fact sheet fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 327.87, "basis": "Sector price cuts (WSJ headline in the fact sheet) push margins lower, matching the mechanical bear fair value of 327.87 [fact sheet fair value]."}
  },
  "entry_price": 394.86,
  "entry_basis": "valuation file: base 464.54 x 0.85",
  "replaces": null,
  "replacement_reason": null
}
```

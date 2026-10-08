# Evaluation: Domino's Pizza, Inc. (DPZ) — 2026-10-07
## Bear case
The 27.4% 12-month fall and the slide below every 5-year multiple floor (P/E 17.4x vs 23.9x minimum) [Certain] probably reflect a structural reset in unit growth, not a temporary dip [Likely]. Franchisee stress is now visible: one operator's failure closed about 13 stores [Likely], and a 50%-off pizza promotion in October hints at weak traffic [Guessing]. The balance sheet leaves little room: net debt/EBITDA is 4.84x [Certain] while US real yields are up 71bp in 3 months and HY spreads have widened 44bp (macro overlay) [Certain], which raises refinancing costs and slows buyback-funded EPS growth [Likely]. Short interest is 10.79% of float and up 12.5% in a month [Certain]. A new CEO took over on Oct 1 and Q3 results land on Oct 13 [Certain]; a reset of guidance is possible [Guessing]. The fact sheet shows no revenue-growth data, so the thesis cannot rule out stalling sales [Certain].
## Bull case
The business is still improving. Operating margin is 19.3% TTM, up from 17.9% in FY2021, and ROIC is 62.2% [Certain]. FCF conversion is 109.5% and the FCF margin is 13.0% [Certain]. On a 6.52% FCF yield and 15.3x P/FCF, 34% below peers [Certain], the market prices in a decline that the reported numbers do not show [Likely]. Leverage has fallen from 6.50x in FY2022 to 4.84x [Certain]. Altman Z of 3.15 and Piotroski F of 7 indicate no distress [Certain]. Shares outstanding fell 2.45% YoY, adding per-share growth even with no re-rating [Certain]. The new CEO is a 15-year insider, which limits strategic disruption [Likely]. A return to the 21.6x peer-median P/E alone would lift the shares about 24% [Likely].
## Decision
```json
{
  "ticker": "DPZ",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-ROIC, asset-light pizza franchisor trades below its own 5-year minimum multiples at a 6.52% FCF yield, but 4.84x leverage, emerging franchisee stress, a fresh CEO and a bear-tilted real-rate backdrop make the re-rating uncertain.",
  "rationale": "The valuation is cheap and margins are intact. But leverage near 4.84x is exposed to rising real yields and wider spreads, franchisee closures and heavy discounting hint at weak traffic, and the data does not show revenue growth. Q3 results arrive in six days. Good but not compelling at conviction 3, so AVOID; holding cash is acceptable.",
  "price_at_decision": 302.87,
  "price_date": "2026-10-06",
  "research_note": "research/DPZ/2026-10-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below 17%, reversing the five-year expansion from 17.9% (FY2021) and signalling franchise economics are eroding.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "TTM FCF margin falls below 10%, toward the FY2022 low of 8.6%, showing cash generation can no longer fund buybacks.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 50%, below every fiscal year since FY2021, indicating the delivery-density moat is weakening.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 50}},
    {"text": "Net debt/EBITDA (ratios page) rises back above 6.0x, the FY2021-FY2022 level, reversing the deleveraging."}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 376, "basis": "P/E re-rates from 17.4x to the 21.6x peer median [RA, P:PZZA/YUM/QSR/WING] on unchanged TTM earnings, while ROIC holds at 62.2% [RA]; probability cut from 0.25 by the macro overlay's moderate bear tilt (research/DPZ/2026-10-07-macro.md) because higher real yields work against the re-rating."},
    "base": {"probability": 0.50, "target_price_12m": 310, "basis": "P/E holds at 17.4x [RA] while the 2.45% YoY reduction in shares [ST] lifts per-share earnings, and margins stay near 19.3% operating [IS]."},
    "bear": {"probability": 0.30, "target_price_12m": 259, "basis": "Franchisee stress and discounting push operating margin back to the FY2022 16.5% from 19.3% [IS] at a constant 17.4x P/E [RA]; probability raised from 0.25 by the macro overlay's moderate bear tilt (research/DPZ/2026-10-07-macro.md), since refinancing 4.84x net debt/EBITDA [RA] costs more."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

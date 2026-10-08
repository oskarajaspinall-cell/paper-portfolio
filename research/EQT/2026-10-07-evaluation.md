# Evaluation: EQT Corporation (EQT) — 2026-10-07
## Bear case
The cheap multiples are measured on what look like peak cash margins. TTM FCF margin of 40.4% and operating margin of 46.2% sit at five-year highs, yet FY2024 delivered 11.4% and 6.8% [Certain] [IS,CF]. An 11.45% FCF yield on cyclically high margins is a classic commodity value trap [Likely]. Q2 2026 missed on weaker gas prices [Certain] (Reuters, 2026-07-21). Shares outstanding grew 5.93% YoY, diluting per-share cash flow [Certain] [ST]. P/B of 1.3x is above its five-year maximum, and P/E and EV/Sales are above peer medians [Certain] [RA]. The stock lags SPY by 31.7pp over 6 months, and short interest rose 16.6% month on month [Certain] [HI,ST]. The note has no proprietary edge on the gas price, which drives most of the return [Likely].

## Bull case
EQT is the largest US gas producer and owns its midstream after Equitrans. That cuts the takeaway and basis risk that peers carry [Likely] (eqt.com). Net debt/EBITDA fell to 0.79x from 7.89x in FY2021 [Certain] [RA]. EV/EBITDA of 5.5x and P/FCF of 8.7x sit in the bottom decile of the five-year range and below peer medians of 6.1x and 13.1x [Certain] [RA]. Piotroski F-Score is 7 and ROIC is rising [Certain] [ST,RA]. Management raised FY2026 volume guidance and cut capex [Certain] (Q2 2026 call). LNG-export and data-centre demand could lift Appalachian realisations [Guessing]. Beta of 0.65 cushions market drawdowns [Certain] [ST].

## Decision
```json
{
  "ticker": "EQT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-leverage, midstream-integrated gas producer trades at the bottom of its 5-year EV/EBITDA and P/FCF ranges, but those multiples rest on cyclically high gas-driven margins and per-share dilution.",
  "rationale": "Cash multiples look cheap, but FCF and operating margins sit at cyclical highs, and FY2024 showed how far they can fall. Shares grew 5.93% and the Q2 profit miss shows gas-price dependence we cannot forecast. That is good but not compelling: conviction 3, below the buy threshold, so cash is preferred.",
  "price_at_decision": 52.47,
  "price_date": "2026-10-06",
  "research_note": "research/EQT/2026-10-07.md",
  "triggers": [
    {"text": "TTM FCF margin falls below 20%, showing the integration and cost advantage is not holding through the gas cycle.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA rises back above 3x, eroding the balance-sheet advantage over peers.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3}},
    {"text": "TTM ROIC falls back to the FY2024 level of 1.2% or lower, breaking the structural-improvement thesis.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 1.2}},
    {"text": "YoY share count growth exceeds the current 5.93%, signalling continued dilutive equity-funded M&A.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5.93}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 73.5, "basis": "EV/EBITDA re-rates from 5.5x to its 5y median of 7.4x [RA] on TTM EBITDA with net debt at 0.79x EBITDA [RA], helped by midstream-integrated volume growth (Q2 2026 call)."},
    "base": {"probability": 0.5, "target_price_12m": 55.5, "basis": "P/E moves from 12.1x to its 5y median of 12.8x [RA] on flat TTM earnings, as raised volume guidance offsets dilution of 5.93% [ST]."},
    "bear": {"probability": 0.3, "target_price_12m": 45.0, "basis": "FCF margin reverts from 40.4% TTM to the FY2025 level of 34.7% [CF,IS] at an unchanged 8.7x P/FCF [RA], in line with the gas-price-driven Q2 miss (Reuters 2026-07-21)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

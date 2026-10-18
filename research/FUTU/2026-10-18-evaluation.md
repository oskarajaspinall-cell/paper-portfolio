# Evaluation: Futu Holdings Limited (FUTU) — 2026-10-18
## Bear case
The discount is a regulatory discount, and it is unresolved. Management itself flagged "moderate asset outflows" from Mainland China regulatory changes on the Q2 2026 call [Certain], and US plaintiff firms allege Futu understated a Chinese penalty while continuing the operations under rectification [Guessing]. If mainland clients must be offboarded, the earnings base behind the 10.5x P/E shrinks, so the multiple is not cheap on the right numbers [Likely]. Cash flow is no anchor: FCF margin swung from -70.5% to 257.5% in a year on client balances [Certain], so the 35.10% FCF yield and the FCFE fair value of 235.71 overstate owner cash [Likely]; the P/E method's base of 75.36 sits below the price [Certain]. Net margin has already slipped from 53.8% (FY2025) to 46.2% TTM, Piotroski F is 2 [Certain]. The portfolio already holds two China/HK names plus a pending third [Certain].

## Bull case
This is a high-return compounder priced as a value trap. ROE rose from 19.2% to 30.5% TTM and operating margin to 66.7% [Certain], while funded accounts grew 33.6% and client assets 43.6% YoY [company-reported] (https://www.sec.gov/Archives/edgar/data/1754581/000110465926098911/tm2623384d1_ex99-1.htm). The P/E of 10.5x is below its own 5y minimum of 13.9x and far under the 23.6x peer median [Certain]; the reverse DCF implies -0.6% revenue growth [Certain]. Overseas growth (Moomoo in the US, Canada, Singapore) is diluting mainland exposure [Likely], insiders own 36.82% [Certain], and the Q2 release discloses no penalty [Certain]. Higher-for-longer rates support interest income (macro overlay, small bull tilt) [Likely].

## Decision
```json
{
  "ticker": "FUTU",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A 30.5%-ROE, 66.7%-operating-margin online broker trades below its own 5-year minimum P/E, but an unresolved Mainland China regulatory rectification and alleged penalty make the earnings base behind that multiple uncertain.",
  "rationale": "Quality and valuation are compelling on paper, but the discount reflects an unresolved, binary mainland regulatory risk the evidence cannot size, FCF is distorted by client balances, net margin is slipping, and the portfolio already carries heavy China/HK exposure. Good but not compelling: AVOID until the regulatory outcome is disclosed.",
  "price_at_decision": 105.48,
  "price_date": "2026-10-16",
  "research_note": "research/FUTU/2026-10-18.md",
  "triggers": [
    {"text": "TTM net margin rises back above 50%, showing mainland rectification has not dented profitability (supports a re-look).", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 50}},
    {"text": "TTM ROE falls below 15%, reversing the five-year improvement and confirming the AVOID.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "A company 6-K/20-F confirms the size and scope of any PRC penalty and the completion of mainland rectification, resolving the overhang either way."},
    {"text": "Company-reported funded-account growth in the next 6-K stays above 20% YoY despite mainland outflows, showing overseas growth fully offsets the regulatory hit."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 157.79, "basis": "Regulatory overhang clears and P/E re-rates to its 5y median 15.7x [RA] on TTM earnings, matching the P/E-method bull of 157.79; below the FCFE bull because FCF is inflated by client-balance swings [CF]."},
    "base": {"probability": 0.45, "target_price_12m": 120.0, "basis": "Growth in funded accounts [company-reported] offsets moderate mainland outflows (Q2 2026 transcript) and P/E recovers part-way toward its 5y minimum 13.9x [RA], with the macro overlay's small bull tilt (higher-for-longer rates, calm VIX) nudging this up; well below FCFE base 235.71 because that model capitalises distorted client-related FCF [CF]."},
    "bear": {"probability": 0.30, "target_price_12m": 70.0, "basis": "A confirmed PRC penalty or forced mainland offboarding cuts the earnings base, taking the price toward the P/E-method bear of 66.83 [IS,RA], consistent with net margin already slipping from 53.8% to 46.2% TTM [IS]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its own 5-year minimum P/E. The blocker is an unresolved Mainland China regulatory rectification and alleged penalty; a lower price would not change the decision until a company filing resolves it.",
  "replaces": null,
  "replacement_reason": null
}
```

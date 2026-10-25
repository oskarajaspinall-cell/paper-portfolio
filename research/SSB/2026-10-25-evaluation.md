# Evaluation: SouthState Bank Corporation (SSB) — 2026-10-25
## Bear case
The cheapness is shallow. ROE has sat at 9.3-10.7% for five years [RA], roughly the bank's cost of equity, so a P/B of 1.1x [RA] is about fair, not a bargain [Likely]. The best-fit method, P/B + sustainable ROE, puts base value at 105.19, essentially the 105.51 close [Certain]. The blended upside to 132.73 rests on an FCFE DCF that bank cash-flow noise distorts (FCF conversion 28.9% in FY2025 [CF,IS]) [Likely]. Shares grew 3.19% YoY on acquisition dilution and the Piotroski F is 4 [ST] [Certain]. Q3 adjusted EPS came in below expectations per the headline flow [OV] [Likely]. Macro: high-yield spreads widened 0.72pp in a month and 2y yields price hikes, raising deposit-cost and CRE-mark risk (macro overlay) [Likely]. A fully adverse scenario would lift the allowance by about $176 million [company-reported] [Certain].

## Bull case
P/E 11.2x is below its 5y minimum of 11.6x and P/B is under the peer median of 1.3x [RA] [Certain]. The reverse DCF implies -4.8% year-1 revenue growth, while Q3 loans and deposits each grew 9% annualised with NIM held at 3.78% and guided to stay in range through 2027 [OV] [Likely]. Efficiency ratio improved to 50.0% as merger costs rolled off [company-reported] [Likely]. Sun Belt deposit franchise is durable, beta 0.78 is low and short interest fell 6.4% on the month [ST] [Likely]. A steeper curve could re-rate P/B toward peers (macro overlay) [Guessing].

## Decision
```json
{
  "ticker": "SSB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A steady 10%-ROE Sun Belt regional bank growing loans with a stable margin, but at 1.1x book its returns roughly match its cost of equity, so the shares are only modestly cheap.",
  "rationale": "Solid, not compelling. The best-fit bank method (P/B + ROE) puts base value at the price; the blended upside depends on a bank FCFE DCF we distrust. Flat ROE, acquisition dilution, a weak F-score and widening spreads leave no margin of safety. Conviction 3: AVOID, revisit near book-value lows.",
  "price_at_decision": 105.51,
  "price_date": "2026-10-23",
  "research_note": "research/SSB/2026-10-25.md",
  "triggers": [
    {"text": "TTM ROE falls below 8%, under the five-year low of 9.3%, showing the franchise cannot earn its cost of equity.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 8}},
    {"text": "TTM net margin falls below 27%, under the 30-31% band held for five years, signalling credit costs or deposit pricing are eroding earnings.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 27}},
    {"text": "Shares change YoY exceeds 6% without a matching rise in earnings, showing growth is being bought with dilution.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 6}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 125, "basis": "P/B re-rates from 1.1x toward the peer median 1.3x [RA] as loan growth and the guided NIM range hold [OV] and the curve steepens (macro overlay bull); below the blended bull 159.20 because that leans on the FCFE DCF."},
    "base": {"probability": 0.5, "target_price_12m": 108, "basis": "P/B + sustainable ROE base 105.19 [IS,BS,RA] plus a year of book growth at a flat ~10% ROE [RA]; below the blended base 132.73 because bank FCFE is distorted (FCF conversion 28.9% in FY2025 [CF,IS]); macro tilt neutral/small (macro overlay), no change to odds."},
    "bear": {"probability": 0.25, "target_price_12m": 92, "basis": "Spreads keep widening (macro overlay bear) and credit costs rise toward the adverse-scenario allowance build [company-reported], taking P/B to its 5y low 1.0x [RA]; below the mechanical bear 109.29, which the FCFE leg inflates."}
  },
  "entry_price": 95.09,
  "entry_basis": "P/B + ROE bear value 95.09 [IS,BS,RA], about P/B back at its 5y low 1.0x [RA]; the default base 132.73 x 0.8 sits above the price because the FCFE leg inflates the blend, so the bank-appropriate method is used.",
  "replaces": null,
  "replacement_reason": null
}
```

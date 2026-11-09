# Evaluation: Old National Bancorp (ONB) — 2026-11-09
## Bear case
Returns are ordinary. ROE was flat over five years (9.3% to 9.0%) and only the TTM 11.5% looks better, helped by Bremer scale and merger costs falling from $12.1 million to $0.7 million [company-reported] [Likely]. Shares outstanding rose 10.97% YoY from deal issuance, so per-share gains must outrun dilution [Certain]. The FCF margin direction change (five-year fall, last-year rise from 34.5% to 36.8%) reflects deal timing, not a better franchise, and bank FCF is a noisy measure [Likely]. P/B of 1.2x sits above its 5y maximum of 1.1x, so book value is not cheap against history [Certain]. The best valuation method (P/B + ROE) gives a base of 20.70, below the 24.93 close; the higher blend is flagged unreliable [Certain]. Macro overlay: NIM narrowed, the 2y yield points to further hikes and VIX rose 13.2 in a month, a risk to a multiple already at its range top [Likely].

## Bull case
Q3 was a record quarter with stable credit, strong deposit growth and FY2026 guidance still for EPS growth above 15% (transcript headline, fact sheet) [Likely]. P/E of 10.2x sits at the 31% position of its 5y range, below the 12.7x median and 3% below peers [Certain]. FCF yield is 10.39% and FCF conversion 102.3% [Certain]. Q3 provisions of $33.6 million [company-reported] show no credit stress, and CET1 of 11.11% (headline, unverified) suggests capital is adequate [Guessing]. Expenses excluding merger costs fell to $354.7 million from $376.5 million [company-reported], so Bremer synergies are arriving and the rolling FCF margin is at its 2-year high [Likely]. If ROE holds near 11.5%, the P/E could drift toward its median [Guessing].

## Decision
```json
{
  "ticker": "ONB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python lists nothing falling over 1 or 3 years: the rolling FCF margin rose from 34.5% to 36.8% and ROE TTM is 11.5%; the five-year fall in net and FCF margins came with the Bremer deal, whose merger costs fell from $12.1 million to $0.7 million [company-reported] (https://www.sec.gov/Archives/edgar/data/707179/000070717926000067/onb-20260930.htm).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Net interest margin squeeze and multiple compression from a hike path and a higher risk premium, with P/B already above its 5y maximum (macro overlay).",
    "veto": null
  },
  "thesis": "A scaled Midwest regional bank earning a recovering 11.5% ROE after the Bremer deal trades at a below-median P/E, but its P/B is above its own 5-year range and the best valuation method sits below the price, so the upside rests on EPS growth outrunning dilution.",
  "rationale": "Average-quality bank, fairly priced: the P/E is modest but P/B is at a 5-year high and the best method (P/B + ROE) values it below the close; the blended fair value is unreliable and macro tilts slightly bearish. Good but not compelling: AVOID, with an entry where book value is cheap again.",
  "price_at_decision": 24.93,
  "price_date": "2026-11-06",
  "research_note": "research/ONB/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROE falls below 9%, back under the five-year level and showing the post-Bremer improvement has reversed.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9}},
    {"text": "TTM net margin falls below 30%, showing deposit costs or provisions are compressing profitability.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 30}},
    {"text": "Quarterly provision for credit losses in the 10-Q exceeds $60 million (Q3 was $33.6 million [company-reported])."},
    {"text": "Shares outstanding growth YoY stays above 5% beyond FY2027 without matching EPS growth.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 31.60, "basis": "EPS growth above 15% (Q3 transcript headline [OV]) and ROE near 11.5% TTM [RA] let the P/E move toward its 5y median 12.7x [RA], consistent with the mechanical base fair value 31.60 (fact sheet)."},
    "base": {"probability": 0.45, "target_price_12m": 26.50, "basis": "P/E stays near 10.2x [RA] while EPS grows modestly net of the 10.97% share dilution [ST], below the unreliable blend because the best method (P/B + ROE base 20.70) sits under the price."},
    "bear": {"probability": 0.30, "target_price_12m": 19.93, "basis": "The macro overlay's small bear tilt (hikes, NIM squeeze, higher risk premium) pushes P/B back toward its 5y range from 1.2x [RA], to the P/B + ROE bear value 19.93 (fact sheet); bear probability raised for that tilt."}
  },
  "entry_price": 20.70,
  "entry_basis": "The mechanical blend is flagged unreliable and its base x 0.8 is above the price, so the entry anchors on the best method: P/B + ROE base 20.70 (fact sheet), where P/B returns to its 5y range [RA].",
  "replaces": null,
  "replacement_reason": null
}
```

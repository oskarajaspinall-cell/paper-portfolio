# Evaluation: Meta Platforms, Inc. (META) — 2026-11-16
## Bear case
Cash conversion has broken down: TTM FCF margin is 11.9% against 23.7% a year earlier, and FCF/net income is 38.1% [Certain]. P/FCF of 57.3x sits above its 5y max of 36.1x and the FCF yield is only 1.75% [Certain], so the price already assumes AI capex earns a return that is not yet visible [Likely]. All four direction flags fall the same way: operating margin 37.8% from 43.2%, ROCE 21.9% from 30.7% [Certain]. Part is a one-off $9.89 billion attorneys-general charge [company-reported] (https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm), but depreciation from the build-out recurs [Likely]. Legal risk is widening: the Italian fine, youth and privacy bellwether trials [Certain]. Reality Labs is expected to lose $18 billion to $19 billion in 2026 [company-reported] (same URL). The trend is weak: only 1.8% above its 200-day average, 12-month change +3.4%, and any slowdown in ad growth would de-rate a capex-heavy story [Likely].
## Bull case
The ad franchise is intact: gross margin 81.0% and ROIC 29.6%, rising over the last 12 months [Certain]. The margin compression is spending, not lost demand: infrastructure costs, AI token costs and legal charges [Certain], so it is a heavy-investment dip, not a structural break [Likely]. On earnings the stock is fairly priced: P/E 21.5x, below its 5y median of 23.7x and in line with peers at 21.1x; EV/EBITDA 14.4x is under its 5y median of 16.3x [Certain]. The balance sheet stays strong: net debt/EBITDA 0.28x, Altman Z 6.44 [Certain]. Relative strength vs SPY is +10.9pp over 3 months [Certain]. If capex growth slows and FCF recovers toward its FY2025 margin of 22.9%, P/FCF would normalise without a lower price [Guessing]. The mechanical DCF is negative on depressed FCF, so the base fair value of 230.28 understates the business [Likely].
## Decision
```json
{
  "ticker": "META",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating margin, ROCE and FCF margin fall on infrastructure costs, AI token costs and a one-off $9.89 billion attorneys-general charge [company-reported] (https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm), not on lost ad demand; gross margin 81.0% and ROIC rising over 12 months [RA-T].",
    "moat": "wide",
    "key_risk": "medium",
    "key_risk_text": "AI and data-centre capex fails to earn a return, keeping FCF margin depressed (11.9% TTM) while depreciation and legal charges compress operating margin further.",
    "veto": null
  },
  "thesis": "A wide-moat ad franchise fairly priced on earnings but expensive on cash flow, where the case depends on AI capex converting into FCF recovery that is not yet visible.",
  "rationale": "Quality is high and the decline looks investment-driven, but the price offers no discount on cash flow (P/FCF above its 5y max) and only a weak trend, so the scorecard does not reach the buy bar. Good but not compelling: AVOID, waiting for FCF recovery or a much lower multiple.",
  "price_at_decision": 641.69,
  "price_date": "2026-11-13",
  "research_note": "research/META/2026-11-16.md",
  "triggers": [
    {"text": "TTM FCF margin falls below 5% (11.9% now), showing capex is consuming cash without a return.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}},
    {"text": "TTM ROIC falls below 20% (29.6% now), showing the AI build-out is diluting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 30% (37.8% now), showing depreciation and legal costs are structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.28x now), showing the build-out is being debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 800, "basis": "FCF recovers toward the FY2025 margin of 22.9% [CF,IS] and P/E re-rates toward its 5y max of 27.5x [RA]; between the EV/Revenue base 698.50 and bull 769.85 and above them on the re-rating."},
    "base": {"probability": 0.5, "target_price_12m": 670, "basis": "P/E holds near 21.5x, below its 5y median of 23.7x [RA], on modest earnings growth as the one-off legal charge drops out; close to the EV/Revenue base of 698.50, while the negative DCF reflects capex-depressed FCF and is set aside as unreliable."},
    "bear": {"probability": 0.25, "target_price_12m": 480, "basis": "Capex returns disappoint and legal costs mount (Bear case), de-rating P/E toward its 5y min of 13.6x [RA], near the 52-week low of 520.26 [HI] and above the mechanical bear values."}
  },
  "entry_price": 406,
  "entry_basis": "P/E back at its 5y low of 13.6x [RA] on TTM earnings; the mechanical base 230.28 x 0.8 is not used because the DCF is negative on capex-depressed FCF and unreliable.",
  "replaces": null,
  "replacement_reason": null
}
```

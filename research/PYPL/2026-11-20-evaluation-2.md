# Evaluation: PayPal Holdings, Inc. (PYPL) — 2026-11-20
## Bear case
Branded checkout, the high-margin core, is losing mix to lower-margin Braintree: gross margin has fallen 5.5pp over five years to 40.5%, and the 10-Q attributes falling branded revenue to mix, merchant incentives and lower FX fees [company-reported] (https://www.sec.gov/Archives/edgar/data/1633917/000163391726000088/pypl-20260930.htm) [Certain]. That reads as contested share, not a cycle [Likely]. On a rolling basis operating margin fell 1.0pp and ROIC 0.8pp in the last year [Certain]. FCF margin rose over the last 12 months but sits 4.0pp below its 2-year high, so the Direction change line shows recovery, not new highs [Certain]. The CFO and Chief Risk Officer leaving on the same day, with an interim risk head and a new cyber-risk factor in the 10-Q, raises execution and controls risk mid-turnaround [Likely]. Multiples below their 5-year minimums can stay there for an ex-growth payments firm; peers are not comparable [Likely].
## Bull case
The price implies roughly zero revenue growth (reverse DCF), yet ROIC is 21.8% and ROCE is rising [Certain]. P/E 10.5x sits at its 5-year minimum, and EV/EBITDA, P/FCF and P/B are below theirs; the FCF yield is 13.45% [Certain]. Shares outstanding are down 8.79% YoY, so buybacks at this yield compound per-share value quickly if FCF holds [Certain]. Net debt/EBITDA of 0.61x leaves room [Certain]. Braintree and Venmo revenue are growing [company-reported] (https://www.sec.gov/Archives/edgar/data/1633917/000163391726000088/pypl-20260930.htm), and a cost programme targeting at least $1.5 billion of run-rate savings [company-reported] can offset mix pressure [Likely]. The stock is above its 200-day average with a positive 6-month trend [Certain]. The base fair value of 67.80 is above the price [Certain]. Leadership changes follow a three-year strategy plan and add a risk-heavy board member [Likely].
## Decision
```json
{
  "ticker": "PYPL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no ROIC, operating-margin or FCF-margin decline over 1 or 3 years beyond its threshold; the 1-year slips in operating margin (-1.0pp) and ROIC (-0.8pp) are flat-rated [IS-T, RA-T], and FCF margin is rising over 12 months [CF-T]. The 5-year gross-margin fall reflects branded-checkout mix loss per the 10-Q (https://www.sec.gov/Archives/edgar/data/1633917/000163391726000088/pypl-20260930.htm).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Branded checkout keeps losing share to wallets and Braintree mix, so profit stops growing and the low multiple persists; CFO and CRO turnover adds execution risk.",
    "veto": {"code": "governance", "reason": "On 2026-11-20 the CFO/COO and the Chief Risk Officer were both replaced, the risk function is under an interim head, and the new CFO starts only in February, mid-restructuring and with a new cyberattack risk factor in the 10-Q (https://www.prnewswire.com/news-releases/paypal-announces-executive-leadership-appointments-to-advance-three-year-strategy-302946916.html). The score cannot see a finance-and-controls leadership vacuum at a payments firm; it should not be bought until the new team is in place."}
  },
  "thesis": "A high-ROIC, lightly levered payments network at or below its 5-year minimum multiples with a 13.45% FCF yield, cheap enough to buy, but mid-way through a finance and risk leadership turnover that clouds execution.",
  "rationale": "The measurable scorecard reaches the buy line, but the same-day CFO and Chief Risk Officer exits leave finance and controls in transition during a restructuring; the veto holds conviction at 3, matching the prior AVOID. Price is not the obstacle; leadership stability is.",
  "price_at_decision": 56.37,
  "price_date": "2026-11-19",
  "research_note": "research/PYPL/2026-11-20.md",
  "triggers": [
    {"text": "TTM operating margin falls below 15% (17.7% now), showing branded-checkout erosion is compressing profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 15% (21.8% now).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 14% (18.4% now), undermining buyback capacity.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "Net debt/EBITDA on the ratios page (debt minus cash and short-term investments) rises above 1.5x from 0.61x, showing buybacks are being debt-funded."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 85.0, "basis": "Cost savings and Braintree/Venmo growth stabilise margins and P/E re-rates toward its 5y median 20.6x [RA], close to the mechanical bull fair value 88.66 [IS,CF]."},
    "base": {"probability": 0.5, "target_price_12m": 64.0, "basis": "Flat-to-low growth with buybacks; price moves part-way to the base fair value 67.80 [IS,CF] while the multiple stays near its 5y minimum given branded-checkout mix loss (10-Q)."},
    "bear": {"probability": 0.25, "target_price_12m": 42.0, "basis": "Branded erosion and leadership turnover cut operating margin further; price heads toward the bear fair value 38.17 [IS,CF], near the 52-week low 38.46 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the scorecard already reaches the buy line at this price. The block is the finance and risk leadership transition; a re-check once the new CFO is in place and the risk head is permanent would change the decision, a lower price would not.",
  "replaces": null,
  "replacement_reason": null
}
```

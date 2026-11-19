# Evaluation: UnitedHealth Group (UNH) — 2026-11-19
## Bear case
The fall is stock-specific and regulatory, not a results miss: a proposed CMS rule would extrapolate Medicare Advantage audit findings back to 2018 payments, a retroactive recovery nobody can size yet [Likely]. Returns were already eroding before it: ROIC fell from 16.8% (FY2023) to 12.4% TTM and sits 2.5pp below its 2-year high of 14.9%, because Medicare Advantage and Medicaid rates lag medical cost trend [company-reported] [Certain]. If CMS caps payment economics permanently, that decline becomes structural, not a repricing cycle [Guessing]. Leverage rose (net debt/EBITDA 2.57x TTM vs 1.78x FY2023) [Certain], part of profit is divestiture gains [Likely], and the P/E fair value rests on TTM earnings a clawback would cut [Guessing]. Even after the fall UNH trades at a premium to peers (P/E +34%, EV/EBITDA +17%) [Certain], and it is below its 200-day average, so there is no trend support [Certain].
## Bull case
UNH trades below its own 5-year minimum on P/E (19.2x vs 21.8x), EV/EBITDA (12.5x vs 14.8x) and P/FCF (13.7x vs 18.6x) at a 7.28% FCF yield [Certain]. Cash conversion is strong at 143.7% of net income [Certain]. ROIC was flat-to-up over the last year (+0.6pp), so the reset looks like it is stabilising as pricing actions shed 1.8 million unprofitable members [company-reported] [Likely]. Scale and the integrated insurer-Optum model remain a narrow moat [Likely]. Divestiture proceeds fund debt repayment, shares fall modestly and the dividend continues [Certain]. The mechanical base fair value of 433.95 sits well above the price [Certain]. The CMS rule is only proposed; a softened final rule would leave the reset as a temporary, priced-in trough [Guessing].
## Decision
```json
{
  "ticker": "UNH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC fell over 3 years because Medicare Advantage and Medicaid rates lag medical cost trend; the 10-Q shows benefit and pricing actions shedding 1.8 million members to restore margin, and ROIC was flat (+0.6pp) over the last 12 months [RA-T], a repricing cycle with the balance sheet intact (sec.gov 10-Q).",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "The proposed CMS rule extrapolating Medicare Advantage audits back to 2018 payments is finalised, forcing an unquantified retroactive recovery and a permanently lower payment economics (Barron's headline in the fact sheet).",
    "veto": {"code": "binary_event", "reason": "An unsized retroactive CMS audit recovery is pending a final rule; until its scope is known the earnings base under the cheap multiples is unverifiable."}
  },
  "thesis": "A scale managed-care franchise at the bottom of its own 5-year multiples while its repricing stabilises returns, but with an unsized retroactive CMS audit clawback now pending.",
  "rationale": "Cheap against its own history with a high FCF yield, but the fall is a regulatory event, not an overreaction to results: a retroactive Medicare Advantage audit recovery can't be sized from the evidence, still trades at a peer premium and sits below its 200-day average. The binary_event veto holds conviction at 3; no position.",
  "price_at_decision": 349.91,
  "price_date": "2026-11-18",
  "research_note": "research/UNH/2026-11-19.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, under the FY2025 low of 10.2%, showing the repricing is failing.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA (site definition) rises above 2.5x from 1.68x, reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "CMS finalises the audit rule with extrapolation back to 2018 payments and UNH discloses a material recovery in a filing; or the rule is dropped or limited to future years (removing the veto)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 478.70, "basis": "The CMS rule is softened and the repricing restores returns, lifting P/E to the mechanical bull fair value of 478.70 [IS,RA], still inside the 5y P/E range."},
    "base": {"probability": 0.45, "target_price_12m": 397, "basis": "A partial clawback and flat ROIC keep P/E near its 5y minimum of 21.8x [RA] on TTM earnings, below the base fair value of 433.95 because that P/E rests on earnings the audit rule may reduce (note section 3)."},
    "bear": {"probability": 0.30, "target_price_12m": 261, "basis": "The rule is finalised retroactively and P/E de-rates to the peer median of 14.3x [P:CI,P:ELV,P:HUM,P:CVS], below the bear fair value of 380.66 because the history-based model cannot see a regulatory reset."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the unresolved CMS retroactive audit rule is; a lower price would not change the decision until the final rule's scope is known.",
  "replaces": null,
  "replacement_reason": null
}
```

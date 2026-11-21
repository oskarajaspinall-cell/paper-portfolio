# Evaluation: Prologis, Inc. (PLD) — 2026-11-21
## Bear case
Returns on capital are thin: ROIC 4.0% TTM and flat for five years [Certain], so this is a scale landlord, not a compounder, and the value case rests on a re-rating. Leverage is rising, net debt/EBITDA 5.43x vs 5.05x in FY2021 [Certain], while the debt-plus-share SEGRO deal adds integration, funding and GBP risk [Likely]. FCF yield is -0.62% on development spend [Certain]. The fall to 122.50 tracks the macro: the 10y real yield is up 0.53pp in three months and HY spreads have widened (macro overlay) [Certain]; if real yields push above ~3.1%, the multiple compresses further toward the bear value of 114.14 [Likely]. The fair value rests on one method (P/FFO proxy; NAV unavailable) [Certain]. The price is 11.0% below its 200-day average, so there is no trend-strength support either [Certain]. ROE has fallen 2.4pp over five years [Certain].

## Bull case
The fall is rate-driven, not a business break: Q3 core FFO beat and 2026 guidance was raised, occupancy 95.6%, and same-store NOI guidance increased (Q3 transcript summary, fact sheet) [Likely]. In-place rents sit below market with a ~16% mark-to-market [company-reported] (https://www.sec.gov/Archives/edgar/data/1045609/000119312526436160/pld-20260930.htm), embedding organic growth [Likely]. P/E 27.0x is at the 5th percentile of its 5y range and EV/EBITDA is below its 5y minimum [Certain]; the base fair value of 147.94 sits well above the price [Certain]. Scale, infill locations and power access are a narrow moat, with a 5.8 GW data center pipeline as an option [Likely]. A director bought shares on 18 Nov [Certain]. If real yields retrace below ~2.6%, the multiple can recover with no earnings change (macro overlay) [Guessing].

## Decision
```json
{
  "ticker": "PLD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "ROIC is flat over 1, 3 and 5 years (4.0% TTM vs 3.9% a year earlier [RA-T]); margins are [data unavailable] for this REIT.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Real yields and credit spreads keep rising, compressing the P/FFO multiple and raising SEGRO funding cost on a 5.43x net debt/EBITDA balance sheet.", "veto": null},
  "thesis": "A best-in-class logistics landlord de-rated by rising real yields, but with ROIC near 4% it lacks the quality the core mandate requires, so the discount alone is not enough.",
  "rationale": "The entry-price fall is rate-driven, not a broken business, and the multiple is near 5y lows; but returns on capital are low, leverage is rising, the trend is down and fair value rests on one method. The scorecard sits below the buy bar, so AVOID; a lower price does not fix the quality obstacle.",
  "price_at_decision": 122.50,
  "price_date": "2026-11-20",
  "research_note": "research/PLD/2026-11-21.md",
  "triggers": [
    {"text": "ROIC (TTM, ratios page) falls below 3.5%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 3.5}},
    {"text": "Net debt/EBITDA rises above 6.0x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 6.0}},
    {"text": "Shares change YoY exceeds 5% (SEGRO funding dilution)", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}},
    {"text": "Occupancy falls below 93% in a quarterly release, or same-store NOI guidance is cut"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 163.55, "basis": "Real yield retraces and the P/FFO multiple returns to the bull fair value of 163.55 on raised core FFO guidance (fact sheet fair value; macro overlay macro_bull)."},
    "base": {"probability": 0.45, "target_price_12m": 135.00, "basis": "Partial re-rating toward the base fair value of 147.94 as rent mark-to-market lifts FFO, held below it by the neutral macro tilt with rates staying high (macro overlay, small neutral tilt)."},
    "bear": {"probability": 0.30, "target_price_12m": 114.14, "basis": "Real yield above ~3.1% and wider spreads compress the multiple to the bear fair value of 114.14 while SEGRO funding raises leverage (fact sheet; macro overlay macro_bear)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: ROIC near 4% gives a quality level of 0, which blocks conviction 4 at any price, so a lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Edenred SE (EPA:EDEN) — 2026-11-09
## Bear case
Meal-voucher fee rules in Italy and Brazil are regulatory price caps, and they already show: TTM operating margin fell from 34.3% to 29.6% in a year and ROCE from 28.6% to 27.2%, 4.6pp below its 2-year high [Certain]. These **Direction change** lines come from a lower regulated take-rate, not a cycle, so that margin level is unlikely to come back [Likely]. Latin America is 30% of revenue [company-reported] (https://www.edenred.com/fr/investisseurs-actionnaires/chiffres-et-indicateurs-cles), and the overlay flags a weaker real against the euro and Selic cuts that lower float income (research/EPA-EDEN/2026-11-09-macro.md) [Likely]. The 38.2% FCF margin compares with 23.6% a year earlier, so FCF swings with client-fund float and the FCFE fair value may overstate value [Likely]. Leverage rose from 1.13x to 1.65x, Altman Z is 0.27, and the mechanical bear value of 21.15 is below the price [Certain]. More countries could cap fees [Guessing].

## Bull case
The price implies a -2.9% year-1 revenue decline. Yet Q3 intrinsic growth was 6.6%, FY2026 EBITDA guidance was reaffirmed and 8%–12% growth is targeted for 2027–2028 (https://stockanalysis.com/quote/epa/EDEN/transcripts/654778-q3-2026-tu/) [Likely]. ROIC is 18.5% TTM, flat over the year and above every fiscal year in the table, so returns are holding up even as margin falls [Certain]. P/E of 11.9x sits at 8% of its 5y range (median 32.3x), EV/EBITDA of 6.8x at 3%, and the FCF yield is 18.51% [Certain]. The margin fall looks like a one-step regulatory reset that guidance already absorbs, not lost share; Mobility keeps growing [Likely]. The employer–merchant network is a two-sided moat [Likely]. Buybacks cut shares by 0.97% and the dividend rose 10% [Likely]. The base fair value is 38.59 [Certain].

## Decision
```json
{
  "ticker": "EPA:EDEN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "structural",
    "decline_evidence": "Operating margin fell 34.3% -> 29.6% and ROCE 28.6% -> 27.2% over the last 12 months [IS-T, RA-T]; the Q3 2026 call ties this to meal-regulation impacts in Italy and Brazil (https://stockanalysis.com/quote/epa/EDEN/transcripts/654778-q3-2026-tu/). A regulatory fee cap is a lasting cut to the price, so the margin level is structurally lower, even though guidance was reaffirmed and ROIC is flat.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Further meal-voucher regulation (Brazil implementing rules, another country capping fees) compresses take-rates beyond what the reaffirmed FY2026 guidance and the 2027-2028 targets absorb; Brazil events are unverified by official sources (research/EPA-EDEN/2026-11-09-macro.md).",
    "veto": null
  },
  "new_evidence": {"type": "method_change", "text": "The earlier BUY 4 verdicts (2026-10-25, re-checked 2026-11-08) predate the 2026-11-09 scorecard; under it, a structural regulatory margin decline, a narrow moat and medium key risk give conviction 3 on the same fact-sheet evidence."},
  "thesis": "A high-return benefits and mobility payments network (ROIC 18.5%) trades near the bottom of its own 5-year multiple ranges, but regulatory fee caps in Italy and Brazil have structurally lowered its margin, and its FCF is flattered by float.",
  "rationale": "Valuation is compelling and returns are holding up, but the margin decline comes from regulatory price caps (structural), with more regulation and Brazil macro as live risks and a bear value below the price. Python's scorecard gives conviction 3: good but not compelling, so AVOID (owner rule: high conviction only).",
  "price_at_decision": 24.60,
  "price_date": "2026-11-06",
  "research_note": "research/EPA-EDEN/2026-11-09.md",
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: valuation already scores its maximum (P/E at 8% and EV/EBITDA at 3% of their 5y ranges [RA]), and the base fair value x 0.8 sits above the current price. What holds conviction at 3 is the structural regulatory margin decline and the risk of more regulation, so a lower price would not change the decision. Evidence that margins have stabilised (a stable rolling operating margin, or official confirmation of the Brazil rules' scope) would.",
  "triggers": [
    {"text": "TTM operating margin falls below 26% (29.6% now), turning the one-step regulatory reset into continuing take-rate compression.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 26}},
    {"text": "TTM ROIC falls below 14% (18.5% now), showing the network's returns are eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 14}},
    {"text": "Debt/EBITDA rises above 2.5x (1.65x TTM net now), showing leverage building beyond seasonal float swings.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "Positive change: the rolling operating margin stops falling against a year earlier and FY2026 EBITDA guidance is delivered, showing the regulatory reset is complete (would argue for re-research toward a BUY)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 45.0, "basis": "The 2027-2028 growth target of 8%-12% (Q3 2026 transcript) starts to show and P/E re-rates partway from 11.9x toward its 5y median 32.3x [RA]; below the mechanical bull of 55.24 because the 38.2% FCF margin is float-flattered against 23.6% a year earlier [CF-T]."},
    "base": {"probability": 0.45, "target_price_12m": 32.0, "basis": "Operating margin settles near the TTM 29.6% [IS-T] with ROIC 18.5% [RA] and EV/EBITDA recovers modestly from 6.8x (3% of its 5y range) [RA]; below the mechanical base of 38.59 because that FCFE value extrapolates float-assisted FCF, and probability trimmed from an even split for the macro overlay's small toward-bear tilt on Brazil (research/EPA-EDEN/2026-11-09-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 21.15, "basis": "Italy and Brazil rules deepen the margin fall from its 34.3% 2-year high [IS-T] while a weaker real and Selic cuts cut translation and float income: the mechanical bear fair value of 21.15 [fact sheet Fair value]; probability raised for the overlay's small toward-bear tilt (research/EPA-EDEN/2026-11-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

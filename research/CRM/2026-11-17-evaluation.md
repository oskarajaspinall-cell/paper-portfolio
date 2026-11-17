# Evaluation: Salesforce, Inc. (CRM) — 2026-11-17

## Bear case
Seat-based application software is the category most exposed to AI-native agents, and today's fall came on Anthropic IPO talk, not on CRM's own numbers [Likely]. The cheapness may be a lasting de-rating: P/E, EV/EBITDA and P/FCF all sit below their five-year minimums, and the note judges part of that structural [Likely]. Returns are only moderate (ROIC 11.0%) and the **Direction change** is real: ROIC fell from 12.2% to 11.0% over the last 12 months as Informatica enlarged the capital base [Certain]; serial M&A (Cresta, Rune) plus the accelerated buyback took net debt/EBITDA from -0.18x to 2.40x [Certain]. The breach headlines and the new cybersecurity language in the 10-Q are a reputational risk [Likely]. The Microsoft Copilotforce tie-up may signal dependence on a competitor's distribution [Guessing]. Results land Dec 2, 2026, so the near-term path is event-driven [Certain]. The 12-month change is -20.2% and the stock trails SPY [Certain].

## Bull case
Nothing in the business explains today's drop: the breach was at a third-party vendor, outages hit the whole sector, and no results or guidance changed [Likely]. Operating margin (21.5%) is flat and FCF margin rose to 34.5% over the last year, so the ROIC dip is a denominator effect from a deal, not margin erosion [Likely]. That is a temporary decline with cash generation intact. At a 9.50% FCF yield and P/FCF of 10.5x, below its own five-year minimum and well below peers, the price implies 8.4% year-1 revenue growth fading to terminal, a modest bar for a ~95% recurring-revenue base [company-reported] [Likely]. Shares outstanding fell 7.44% YoY, compounding per-share value [Certain]. Switching costs in data, workflows and integrations give a narrow moat [Likely]. Mechanical base fair value is 248.79 against a 214.83 close [Certain]; the price still sits above its 200-day average [Certain].

## Decision
```json
{
  "ticker": "CRM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only TTM ROIC is falling (12.2% to 11.0%, RA-T) while operating margin held (+0.3pp, IS-T) and FCF margin rose (+2.9pp, CF-T): a larger capital base after the Informatica deal, not margin erosion (research/CRM/2026-11-17.md section 2).",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "AI-native agents erode seat-based CRM pricing, turning the de-rating below five-year minimum multiples into a permanent one while debt-funded M&A lifts leverage.",
    "veto": null
  },
  "thesis": "A highly cash-generative CRM franchise trades below its own five-year minimum multiples on AI-disruption fears, but moderate returns, rising leverage and an unresolved disruption risk keep it short of high conviction.",
  "rationale": "Today's fall is headline-driven (third-party breach, sector outages, AI IPO talk) and does not break the business case, but the scorecard does not reach the buy bar: ROIC is only moderate and slipping, leverage has risen, and AI disruption is a high-probability risk. Good but not compelling: AVOID, with an entry price.",
  "price_at_decision": 214.83,
  "price_date": "2026-11-16",
  "research_note": "research/CRM/2026-11-17.md",
  "triggers": [
    {"text": "TTM operating margin falls below 19% (21.5% now), showing AI pricing pressure or integration costs are eroding profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 19}},
    {"text": "TTM FCF margin falls below 30% (34.5% now), showing the cash engine behind the thesis is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 9% (11.0% now), meaning acquisitions are failing to earn their cost.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "Net debt/EBITDA on the ratios page rises above 3.0x (2.40x TTM now) from further debt-funded M&A or buybacks."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 297.34, "basis": "Disruption fears fade and the multiple recovers toward its own history, matching the mechanical bull fair value 297.34 on TTM FCF margin of 34.5% [CF,IS]."},
    "base": {"probability": 0.5, "target_price_12m": 248.79, "basis": "Margins hold and the market re-rates modestly to the mechanical base fair value 248.79, as the 8.4% growth the reverse DCF implies is met by a ~95% recurring base [company-reported]."},
    "bear": {"probability": 0.25, "target_price_12m": 146.32, "basis": "AI disruption is priced as permanent and the stock retests its 52-week low 146.32 [HI]; above the mechanical bear 90.51 because that DCF bear assumes a revenue fall the 34.5% FCF margin [CF,IS] does not show."}
  },
  "entry_price": 211.47,
  "entry_basis": "valuation file: base 248.79 x 0.85.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: LATAM Airlines Group (SNSE:LTM) — 2026-11-09
## Bear case
Returns are rolling over from a cycle peak. Over the last 12 months ROIC fell from 30.1% to 25.4%, ROCE from 22.1% to 18.9% and operating margin from 15.5% to 13.7%, each well below its 2-year high [Certain]. The driver is a fuel-cost spike and a weaker Brazilian real, and management trimmed its earnings outlook (Reuters, 2026-11-03) [Likely]. Fuel and FX are cyclical but outside management's control; if they persist, the decline continues and the 8.7x P/E is on earnings that are still falling [Likely]. The macro overlay notes the real at 5.4252 per USD and weakening, with Brazilian politics unverified [Certain]. Altman Z of 1.71 says the mended balance sheet is not a fortress [Certain]. The mechanical fair value is unreliable (methods disagree 10.4x), so there is no robust valuation anchor [Certain]. P/E sits at the 69% point of its own range, not cheap [Certain].
## Bull case
Cash generation is real and steady: FCF margin of 13.0% is flat on a rolling year, FCF conversion is 132.4% of net income, and the FCF yield is 15.62% [Certain]. EV/EBITDA of 4.9x is below its 5y minimum of 5.0x and well under the 8.0x peer median; P/FCF of 6.4x compares with a 25.2x peer median [Certain]. Leverage fell from 2.86x in FY2023 to 1.75x, and the share count is down 3.83% YoY, so cash is returned [Certain]. The reverse DCF implies -18.4% year-1 revenue growth, a far harsher path than a fuel squeeze with unit revenue gains offsetting most of it (Q3 call headline, fact sheet) [Likely]. The decline in returns is cost-driven, not lost share; dominant hubs in a consolidated region support pricing [Likely]. The guidance trim is already public and in the price [Guessing].
## Decision
```json
{
  "ticker": "SNSE:LTM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and operating margin fell over the last 12 months on a fuel-cost spike and a weaker real, partly offset by higher unit revenue; FCF margin is flat and net debt/EBITDA is 1.75x, so the balance sheet is intact (https://www.reuters.com/business/latam-airlines-trims-earnings-outlook-fuel-costs-bite-2026-11-03/; Q3 call headline in the fact sheet; RA-T).",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Airline earnings mean-revert from peak returns: a persistent fuel spike and BRL weakness (outlook already trimmed) could keep compressing margins, and the low multiples are on peak-cycle earnings.",
    "veto": null
  },
  "thesis": "Latin America's dominant airline group generates a 15.62% FCF yield at an EV/EBITDA below its own 5-year minimum, but its returns are rolling over from a cycle peak on fuel and currency costs.",
  "rationale": "Cheap on cash flow and EV/EBITDA with a repaired balance sheet, but returns and margins are falling from a cyclical peak, the outlook was just trimmed on fuel, P/E is mid-range and the fair value is unreliable, leaving little scenario upside. Scorecard conviction 2: AVOID, cash is acceptable.",
  "price_at_decision": 23.36,
  "price_date": "2026-11-06",
  "research_note": "research/SNSE-LTM/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, showing returns are reverting to pre-recovery airline levels rather than dipping on fuel.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 10%, showing the fuel and currency squeeze is not being passed through to fares.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 6%, breaking the cash-generation case.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "Net debt/EBITDA rises above 3.0x (1.75x TTM now), reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 28.87, "basis": "Fuel eases and margins return toward their 2-year highs, lifting EV/EBITDA from 4.9x toward its 6.2x 5y median [RA], in line with the mechanical EV/EBITDA bull value of 28.87 [fact sheet fair value]; the DCF bull is ignored as unreliable."},
    "base": {"probability": 0.45, "target_price_12m": 25.78, "basis": "Margins stabilise near TTM levels and P/E moves from 8.7x to its 9.6x 5y median [RA] on TTM EPS, well below the through-cycle DCF base because the fact sheet flags that method as unreliable (methods disagree 10.4x)."},
    "bear": {"probability": 0.3, "target_price_12m": 20.33, "basis": "The fuel and BRL squeeze persists after the trimmed outlook (Reuters, 2026-11-03), pushing the price back to its 52-week low of 20.33 [HI], above the EV/EBITDA bear value of 7.27 since FCF margin is holding at 13.0% [CF-T]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: the obstacle is falling returns at a cyclical peak with a high fuel/BRL risk, not the price alone, so a lower price would not by itself justify conviction 4; re-research if margins stabilise.",
  "replaces": null,
  "replacement_reason": null
}
```

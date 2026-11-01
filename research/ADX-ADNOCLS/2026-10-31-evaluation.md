# Evaluation: ADNOC Logistics & Services plc (ADX:ADNOCLS) — 2026-10-31
## Bear case
The dip has no identified cause: no filing, results or headline after 2026-08-24, so it cannot be judged an overreaction [Certain]. TTM operating margin of 26.0% sits far above FY2025's 18.1%, so earnings look partly cyclical and multiples on TTM flatter the stock [Likely]. FCF conversion is only 39.4% TTM as fleet capex absorbs cash; P/FCF of 22.6x is a premium to the peer median of 12.9x, as are P/E and EV/EBITDA [Certain]. The EV/EBITDA method's base value is 3.73 AED and the mechanical bear is negative, so the base fair value of 8.18 rests on the DCF [Certain]. Hormuz tensions are a direct operating risk [Likely]. ADNOC controls the equity and the float is thin, limiting minority influence [Likely]. Q3 results on Nov 11, 2026 are the next real evidence [Certain].
## Bull case
Quality is improving: ROIC rose from 3.6% (FY2021) to 19.4% TTM, net debt/EBITDA is 0.13x and Piotroski F is 8 [Certain]. Contracted work for parent ADNOC gives visibility, consistent with a beta of 0.42 [Likely]. Guidance was reportedly raised for the third time in August (Reuters headline, unverified) [Guessing]. The stock trades below its own 5y minimum P/E (12.4x) and EV/EBITDA (9.1x), and the base fair value of 8.18 sits above the 6.85 close [Certain]. Fleet additions (11 vessels bought, LNG newbuilds) can grow contracted earnings [Likely]. The price fall, with an RSI of 36.6 and no news, looks like thin-float drift rather than a broken thesis [Likely].
## Decision
```json
{
  "ticker": "ADX:ADNOCLS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-leverage, ADNOC-contracted shipping franchise with rising ROIC trades below its own 5-year multiples, but on likely above-cycle margins, weak cash conversion and a peer premium, with an unexplained fall and Q3 results imminent.",
  "rationale": "The fall has no identified cause, so it is neither a proven overreaction nor the removal of the original obstacles: likely peak margins, capex-heavy cash conversion, a peer premium on P/E and P/FCF, and a fair value resting on the DCF alone. Good but not compelling; wait for the Nov 11 results.",
  "price_at_decision": 6.85,
  "price_date": "2026-10-30",
  "research_note": "research/ADX-ADNOCLS/2026-10-31.md",
  "triggers": [
    {"text": "TTM operating margin falls below 15%, under FY2025's 18.1%, showing contract economics, not just the cycle, are weakening.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 10%, giving back most of the rise from 3.6% to 19.4%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin turns negative, showing fleet expansion is consuming more cash than operations generate.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Net debt/EBITDA rises above 2.0x (0.13x TTM), showing acquisitions are being debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 10.28, "basis": "Q3 confirms margins hold near the 26.0% TTM level [IS] and EV/EBITDA recovers toward its 5y range (min 9.1x) [RA], matching the EV/EBITDA bull value of 10.28 in the fair value section."},
    "base": {"probability": 0.5, "target_price_12m": 7.58, "basis": "Margins ease from 26.0% TTM toward FY2025's 18.1% [IS] while fleet additions add volume, so the stock returns only to its 2026-10-09 swing high [HI], below the 8.18 base fair value because that value rests on the DCF while the EV/EBITDA base is 3.73."},
    "bear": {"probability": 0.25, "target_price_12m": 5.63, "basis": "Margins revert to FY2025 levels [IS] and Hormuz disruption (Iran tanker blacklist headline [OV]) hits operations, sending the stock back to its 6-month low [HI]; the mechanical bear of -12.04 is a negative-FCF DCF artefact and not a credible price for a 0.13x-levered business [BS]."}
  },
  "entry_price": 6.54,
  "entry_basis": "valuation file: base 8.18 x 0.8 (20% margin of safety); at that price the peak-margin and cash-conversion risks would be paid for.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: The People's Insurance Company (Group) of China (HKG:1339) — 2026-11-09
## Bear case
Earnings have rolled over and nobody here knows why. TTM ROIC fell from 13.2% to 7.4% in a year and ROE from 15.9% (FY2025) to 9.4% TTM [Certain]. The Direction change line shows the 3-year ROIC change is flat, so FY2024-25 looks like a peak, not a new run rate [Likely]. The Q3 2026 release was not read, so the cause of the fall (investment returns on a Chinese bond/equity book, catastrophe losses or underwriting) is unverified [Certain]. The cheapness is mostly the P/B+ROE leg, and that leg needs ROE near FY2025 levels that TTM no longer shows; the P/E leg's base of 6.23 HKD is only modestly above the price [Certain]. Returns have been volatile (ROIC 5.6% in FY2021), state control limits minority leverage over capital allocation, and the stock fell 26.8% in 12 months [Likely].
## Bull case
The price assumes little. P/E of 6.9x sits below its 5y minimum of 7.2x and below the peer median of 7.9x; P/B of 0.6x is in the lowest quarter of its 5y range and about half the peer median of 1.3x [Certain]. Even the mechanical bear fair value of 6.17 HKD is above the 5.37 close [Certain]. A state-backed national P&C franchise with scale, distribution and licensing barriers is a plausible narrow moat [Likely]. No dilution (shares -0.11% YoY), low beta of 0.61, and the macro overlay finds no macro variable moving the odds [Certain]. If the TTM ROE dip is investment-mark volatility rather than underwriting damage, ROE can revert toward the 5y range and the P/B+ROE base of 8.42 HKD becomes reachable [Guessing].
## Decision
```json
{
  "ticker": "HKG:1339",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "structural",
    "decline_evidence": "TTM ROIC fell from 13.2% to 7.4% and ROE to 9.4% TTM (RA-T, RA); the 3-year ROIC change is flat, so FY2024-25 reads as a peak. The Q3 2026 results (https://stockanalysis.com/quote/hkg/1339/filings/3910639/) were not read, so no evidence shows the fall is a one-off; it cannot be credited as temporary.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "ROE stays near the 9.4% TTM level instead of reverting toward FY2024-25, which removes the P/B+ROE leg of the fair value.",
    "veto": null
  },
  "thesis": "A state-backed Chinese P&C insurer at a P/E below its 5-year minimum and P/B about half its peers, but with ROE and ROIC down sharply over the last year for an unverified reason.",
  "rationale": "Cheap on own-history and peer multiples, but the upside rests on ROE reverting while TTM ROE and ROIC have fallen hard for an unread reason, and quality and leverage score weakly. Not compelling: AVOID, re-research once the cause of the earnings fall is known.",
  "price_at_decision": 5.37,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-1339/2026-11-09.md",
  "triggers": [
    {"text": "TTM ROE (ratios page) stays below 9% for two consecutive quarterly TTM readings, showing the earnings reset is persistent.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9}},
    {"text": "TTM ROIC falls below 6%, toward the FY2021 low of 5.6%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 6}},
    {"text": "Net debt/EBITDA (site definition) rises above 3.5x, outside its 5y range.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}},
    {"text": "Share count change YoY exceeds +3% (dilution of minority holders).", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 7.69, "basis": "ROE reverts toward the FY2025 15.9% [RA] and the price reaches the mechanical base fair value of 7.69 HKD (P/B+ROE 67%, P/E 33%) [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 6.23, "basis": "ROE stays near the 9.4% TTM level [RA] and the stock re-rates only to the P/E method's base of 6.23 HKD on TTM earnings, below the blended base because the P/B+ROE leg assumes ROE that TTM does not show [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 4.63, "basis": "ROIC slides further from 7.4% TTM [RA-T] and the price retests its 52-week low of 4.63 HKD [HI], below the mechanical bear of 6.17 because that bear still assumes ROE the TTM figures do not support."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its own 5y P/E minimum and below the mechanical bear fair value; the unresolved cause of the TTM ROE/ROIC fall is. A lower price would not change the decision; re-research once the Q3 2026 results explain it.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Humanwell Healthcare (Group) Co.,Ltd. (SHA:600079) — 2026-11-09
## Bear case
[Likely] China's volume-based procurement is a standing price cap on generics, and the margin gains (operating margin 15.6% TTM, gross margin 49.5%) are what is most exposed to it. [Certain] The mechanical base fair value of 16.95 CNY sits below the 19.51 close, and the reverse DCF needs 17.1% year-1 revenue growth. [Certain] The direction-change line: FCF margin 8.6% TTM is 2.1pp below its 2-year high of 10.7% (2026-03-31); [Likely] that is a quarterly working-capital swing rather than a break, since it is still up 2.5pp on a year earlier, but FCF conversion was negative as recently as FY2022, so cash quality has a short record. [Certain] The Q3 2026 report (2026-10-29) was not read, and the US revenue share is unverified. [Guessing] Acquisitions drove past leverage swings and could again. [Certain] ROE fell over five years and net margin dipped to 5.2% in FY2024.

## Bull case
[Certain] Returns are rising over 1, 3 and 5 years: ROIC 12.3% TTM vs 8.8% a year earlier, operating margin up 3.0pp in the last year, FCF margin up 6.1pp over three years. [Certain] The balance sheet has deleveraged from 2.28x to 0.47x net debt/EBITDA, with no dilution (shares -0.79% YoY) and Piotroski F of 7. [Certain] It is cheap on its own history and peers: P/E 12.3x below its 5y minimum of 15.5x and 55% below the peer median; EV/EBITDA 7.7x below its 5y minimum of 8.1x; FCF yield 6.62%. [Likely] Licences for controlled anaesthetic drugs give a regulatory moat that procurement cuts reach less easily than plain generics. [Likely] The fair value is flagged unreliable (methods disagree 2.8x), and the P/E method alone puts the base at 29.83.

## Decision
```json
{
  "ticker": "SHA:600079",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "ROIC, operating margin and FCF margin all rose over the last 1 and 3 years [RA-T, IS-T, CF-T]; FCF margin sits 2.1pp below its 2-year high but is up 2.5pp year on year.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "China volume-based procurement price cuts compress the improved margins of its anaesthetic and generic drugs.", "veto": null},
  "thesis": "An improving, deleveraged Chinese specialty drug maker trading below its own 5-year multiple range, with procurement pricing the main risk to margins.",
  "rationale": "Quality is improving and multiples are at five-year lows, but the mechanical fair value is below the price and unreliable, the Q3 report and foreign mix are unverified, and the scorecard does not reach the buy bar. Good but not compelling: AVOID.",
  "price_at_decision": 19.51,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-600079/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 12% (procurement cuts biting).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "TTM ROIC falls below 9%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "Net debt/EBITDA rises above 2.0x (debt-funded acquisition).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 24.29, "basis": "Margins hold and P/E re-rates toward its 5y minimum of 15.5x [RA], consistent with the mechanical bull fair value of 24.29 [fact sheet]."},
    "base": {"probability": 0.5, "target_price_12m": 19.51, "basis": "Earnings grow modestly while P/E stays near 12.3x [RA], below its own range as China risk keeps a discount; above the unreliable mechanical base of 16.95 because the P/E method gives 29.83 [fact sheet]."},
    "bear": {"probability": 0.25, "target_price_12m": 16.03, "basis": "Procurement cuts reverse part of the operating-margin gain [note section 2] and the price returns to its 52-week low of 16.03 [HI]."}
  },
  "entry_price": 13.56,
  "entry_basis": "valuation file: base 16.95 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: CTS Eventim AG & Co. KGaA (ETR:EVD) — 2026-10-19
## Bear case
The cheapness is partly an accounting artefact: EV/EBITDA of 8.7x sits far below its 5y minimum of 13.1x mainly because net cash, likely swollen by presale ticket money owed to promoters, shrinks EV [Likely]. On cash it is not cheap: P/FCF of 21.6x is above the peer median of 13.6x and the FCF yield is only 4.62% [Certain]. FCF margin fell from 16.5% (FY22) to 4.2% (FY25) and FCF/NI to 46.4% before a partial TTM recovery to 89.0% [Certain]; the note can't prove this is timing [Guessing]. The CFO left with immediate effect and no stated reason two months after results, an unresolved governance flag at the exact point cash conversion is in question [Certain]. The reverse DCF needs 15.3% year-1 revenue growth, which isn't a low bar [Certain]. Net margin has drifted from 11.6% to 9.3% [Certain]. Beta 1.25 ties it to discretionary spending [Certain].
## Bull case
A two-sided ticketing network with ROCE rising to 31.2% TTM and ROE 29.8% is a genuine moat business [Certain]. Operating margin rose from 13.3% (FY22) to 14.9% TTM and gross margin to 25.9% [Certain]. P/E of 19.2x is below its 5y minimum of 21.9x and P/B of 4.9x below its 5.9x minimum [Certain]. The base fair value of 78.54 EUR sits above the price [Certain]. Recent quarters showed double-digit revenue growth in both segments, per the Q1 and Q2 2026 call headlines [Likely]. Insiders own 49.34% and a director and the KPS Stiftung both bought after the CFO exit, which argues against a hidden accounting problem [Likely]. Net cash every year gives M&A optionality [Certain]. If TTM FCF conversion near 89.0% holds into a full year, the cash multiple falls back toward its 5y median of 18.0x [Guessing].
## Decision
```json
{
  "ticker": "ETR:EVD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-ROCE, net-cash European ticketing network looks cheap on earnings multiples, but weak cash conversion, a cash multiple above peers and an unexplained CFO exit leave the value case unproven.",
  "rationale": "Quality is real, but the headline discount rests on EV inflated by presale float, while P/FCF sits above peers and FCF conversion only partly recovered. The abrupt, unexplained CFO exit adds governance risk at the worst moment. Good but not compelling: conviction 3, no position until cash conversion and the CFO question are resolved.",
  "price_at_decision": 61.75,
  "price_date": "2026-10-16",
  "research_note": "research/ETR-EVD/2026-10-19.md",
  "triggers": [
    {"text": "TTM FCF margin rises above 13%, back to the FY2024 level of 13.0%, showing the FY2025 cash shortfall was working-capital timing (would raise conviction).", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 13}},
    {"text": "TTM operating margin falls below 13%, under the FY2022 level of 13.3%, showing ticketing/live economics are eroding (thesis worse).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 13}},
    {"text": "TTM net margin falls below 8%, extending the drift from 11.6% (FY2023), indicating competition or cost pressure on promotion economics.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 8}},
    {"text": "The company discloses the reason for the CFO's immediate exit in a filing or ad-hoc release; a non-accounting reason with clean Q3 2026 results would remove the governance obstacle."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 85.20, "basis": "FCF conversion normalises and EV/EBITDA re-rates toward its 5y minimum 13.1x [RA], matching the EV/EBITDA bear value of 85.20 [fair value table]; the mechanical bull of 807.64 is rejected as driven by the FY2021 outlier FCF margin of 120.3% [CF,IS]."},
    "base": {"probability": 0.45, "target_price_12m": 68.00, "basis": "Steady operating margin near 14.9% TTM [IS] with partial FCF recovery lifts the price toward, but short of, the DCF base of 71.15 [fair value table], as the reverse-DCF bar of 15.3% growth caps re-rating."},
    "bear": {"probability": 0.30, "target_price_12m": 48.80, "basis": "CFO exit reveals cash-conversion or reporting problems and FCF stays near the FY2025 4.2% margin [CF,IS], taking the price to the blended bear fair value of 48.80, near the 52-week low of 48.26 [HI]."}
  },
  "valuation_overrides": [
    {"method": "dcf", "scenario": "bull", "field": "margin", "value": 0.208, "reason": "Bull FCF margin set to FY2023's 20.8% [CF,IS], the best year excluding the FY2021 outlier of 120.3%, which produces an implausible DCF bull of 1,162.81."}
  ],
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: base fair value less the margin of safety is above the current price, yet the unexplained CFO exit and unproven FCF conversion keep conviction at 3; a lower price would not change that, a resolved CFO question and a clean full year of cash conversion would.",
  "replaces": null,
  "replacement_reason": null
}
```

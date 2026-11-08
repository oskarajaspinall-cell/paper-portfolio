# Evaluation: Julius Bär Gruppe AG (SWX:BAER) — 2026-11-08
## Bear case
The cheap P/E of 12.2x [RA] sits on above-normal earnings: TTM net margin of 27.0% against a 5y low of 14.0% [IS], and ROE has swung from 7.3% to 16.2% [RA] [Certain]. Fee income follows markets, and the macro overlay shows VIX up 13.2 in a month to 28.18, with fees lagging markets (research/SWX-BAER/2026-11-08-macro.md) [Likely]. P/B of 1.9x is above its 5y max [RA], so on book the stock is not cheap [Certain]. FINMA found serious AML and risk-management breaches [Certain]; de-risking weighs on net new money until 2028 per management [Likely]. The bear fair value of 45.07 sits far below the price while base gives only +9.1% [Certain]. The Direction change line (FCF margin rising over 12 months, falling over 5 years) is noise: bank FCF swings with client balances and does not support or threaten the thesis [Likely]. Piotroski F is 4 [Certain].
## Bull case
H1 2026 brought record net profit and AUM with improved cost efficiency (transcript, /quote/swx/BAER/transcripts/550407-h1-2026/) [Likely]. FINMA enforcement is concluded and a buyback of up to 600 million CHF followed [Likely]. P/E is 19% below the peer median of 15.2x and near the bottom of its own 5y range [RA] [Certain]. The reverse DCF implies -2.6% year-1 revenue growth, a decline that record AUM does not show [Certain]. Beta of 0.83 [ST] and a stock already down 8.4% over 3 months price part of the risk-off shock [Likely]. A bull fair value of 85.31 is reachable if markets calm and net new money normalises [Guessing].
## Decision
```json
{
  "ticker": "SWX:BAER",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A Swiss private bank at record profit trades at a low P/E, but on above-normal margins, a book multiple at its 5-year high and with post-FINMA de-risking still slowing flows, leaving a balanced rather than compelling skew.",
  "rationale": "Base fair value offers single-digit upside against a deep bear case; earnings sit near a cyclical peak just as the macro overlay tilts toward risk-off, and the FINMA remediation still weighs on flows. Good but not compelling: AVOID at conviction 3, revisit at a margin of safety to base fair value.",
  "price_at_decision": 67.90,
  "price_date": "2026-11-06",
  "research_note": "research/SWX-BAER/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE falls below 10%, showing the earnings recovery from the FY2023 trough has reversed.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "TTM net margin falls below 18%, showing fee and interest income are reverting to the trough rather than holding near 27.0%.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 18}},
    {"text": "Shares change YoY exceeds 3%, signalling dilution rather than buyback-led capital return.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}},
    {"text": "Any new FINMA or other regulatory sanction that restricts client onboarding or business, per company releases."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 85.31, "basis": "Markets calm, net new money normalises and P/E holds at the current level on record earnings: the mechanical bull fair value of 85.31 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 72.0, "basis": "Earnings hold near TTM with ROE 16.2% [RA] and P/E near its 5y median 11.8x [RA]; set below the mechanical base of 74.05 because TTM net margin of 27.0% is above normal [IS], and probability trimmed from an even split for the overlay's small bear tilt (research/SWX-BAER/2026-11-08-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 45.07, "basis": "Risk-off deepens (VIX above 35 per the overlay), AUM and activity fall and net margin reverts toward the FY2023 14.0% [IS]: the mechanical bear fair value of 45.07; probability raised for the macro overlay's small toward-bear tilt (research/SWX-BAER/2026-11-08-macro.md)."}
  },
  "entry_price": 59.24,
  "entry_basis": "valuation file: base 74.05 x 0.8, a 20% margin of safety that would compensate for above-normal margins and the FINMA remediation.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Sterling Infrastructure, Inc. (STRL) — 2026-11-07
## Bear case
The 14.2x P/E [RA] is cheap only on peak-cycle earnings: operating margin rose from 7.8% to 18.6% in five years [IS] in a contract business with limited structural moat [Likely]. The price fell 71.5% in six months despite a beat-and-raise [HI], so the market is discounting something the sources read do not explain, possibly political backlash against AI data centres [Guessing]. Mechanical base fair value is 147.91, well below the 252.82 close, and the reverse DCF already requires 18.3% year-1 revenue growth [Certain]. FCF conversion fell to 85.0% TTM from 298.7% in FY2023 [CF,IS] and Q3 gross margin eased to 24.1% from 24.7% [company-reported] [Certain]. Backlog now includes uncommitted MSA estimates and contracts are terminable on short notice [company-reported] [Certain]. Beta 1.98 and ATR at 13.8% of the close [ST,HI] mean gap risk is extreme [Certain].

## Bull case
Fundamentals are still accelerating: TTM ROIC 44.2% vs 11.7% in FY2021 [RA], Piotroski F 8, Altman Z 7.33 and roughly zero net debt [ST] [Certain]. Q3 beat and FY2026 guidance was raised [Likely]. Backlog of $4.14bn and combined backlog of $6.14bn, with 1.9x book-to-burn over nine months [company-reported], gives multi-quarter visibility [Certain]. P/E is 50% below the 28.4x peer median and EV/EBITDA 8.5x is 35% below peers [RA] [Certain]. If the data-centre fear proves overdone, a return toward the 5y median EV/EBITDA of 10.3x [RA] or the mechanical bull value of 446.75 is plausible [Guessing].

## Decision
```json
{
  "ticker": "STRL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return site-development contractor with accelerating backlog trades at a deep discount to peers, but on peak-cycle margins with an unexplained price collapse and a mechanical base value far below the price.",
  "rationale": "Quality and backlog are strong and multiples are low, but earnings look cyclical-peak, the cause of the six-month collapse is unknown, base fair value sits well below the price and volatility is extreme. Good but not compelling: conviction 3, so AVOID; re-research on a further de-rating toward the margin-of-safety entry.",
  "price_at_decision": 252.82,
  "price_date": "2026-11-06",
  "research_note": "research/STRL/2026-11-07.md",
  "triggers": [
    {"text": "TTM gross margin falls below 20%, back to the FY2024 level, showing the mix shift to mission-critical site work has reversed.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 25%, signalling the step-up in returns was cyclical rather than structural.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "Backlog book-to-burn in the 10-Q falls below 1.0x for two consecutive quarters, showing data-centre-type demand is fading."},
    {"text": "FCF conversion (cash flow page) falls below 50% for a full fiscal year, showing growth is consuming cash."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 446.75, "basis": "Raised guidance and 1.9x book-to-burn [company-reported] hold and the multiple re-rates toward the 5y median EV/EBITDA of 10.3x [RA], matching the mechanical bull fair value of 446.75 [fact sheet]."},
    "base": {"probability": 0.45, "target_price_12m": 230, "basis": "Backlog of $4.14bn [company-reported] supports near-term earnings but margins plateau and the de-rating persists; set above the mechanical base of 147.91 because the DCF fades growth faster than the backlog implies, yet below the price given the reverse-DCF hurdle of 18.3% growth [fact sheet]."},
    "bear": {"probability": 0.3, "target_price_12m": 100.21, "basis": "Data-centre demand slows, margins mean-revert from 18.6% toward the 5y history [IS] and the stock reaches the mechanical bear fair value of 100.21 [fact sheet]."}
  },
  "entry_price": 118.33,
  "entry_basis": "valuation file: base 147.91 x 0.8, a level that would pay for peak-margin risk with a margin of safety.",
  "replaces": null,
  "replacement_reason": null
}
```

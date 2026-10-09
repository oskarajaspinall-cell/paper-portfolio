# Evaluation: Everest Group, Ltd. (EG) — 2026-10-09
## Bear case
P/B of 0.9x sits at the 2nd percentile of its 5y range [Certain] because the market doubts the book itself: Q2 brought roughly $200m of North America casualty reserve strengthening for older accident years [Likely], and social-inflation reserve charges tend to recur across several quarters [Likely]. ROE (-3.0pp) and ROIC (-1.6pp) have both fallen over five years [Certain], with a FY2022 trough of 6.4% ROE showing how fast earnings can collapse [Certain]. Piotroski F-score is a middling 4 [Certain], gross premium is shrinking [Likely], and two divestitures in the Insurance segment reshape the mix [Certain]. Short interest rose 32.3% month-on-month ahead of the Oct 28 Q3 print [Certain]. A cheap P/E of 7.9x [Certain] on earnings that may be restated through reserves is not a margin of safety [Guessing]. Hurricane-season catastrophe losses land in Q3 as well [Guessing].

## Bull case
EG trades on 7.9x P/E, 11th percentile of its 5y range and 15% below peers, and at 0.9x book, 30% below the 1.3x peer median [Certain], despite a 12.6% TTM ROE [Certain]. The mechanical base fair value is 468.98, +25.7% [Certain]. Management is cutting volume to protect margins and returning capital aggressively: shares down 4.73% YoY plus a $2.00 dividend [Certain]. Elevated Treasury yields lift reinvestment income on the float [Likely] (macro overlay). Beta of 0.26 diversifies the portfolio, which holds no Financials [Certain]. If Q3 shows reserves have stabilised, a re-rating toward book-plus is plausible [Guessing].

## Decision
```json
{
  "ticker": "EG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A reinsurer earning a 12.6% ROE trades at 0.9x book and 7.9x earnings, but recurring casualty reserve charges and a five-year decline in returns leave the book value and earnings base unproven.",
  "rationale": "Cheap on every own-history and peer measure, but the discount reflects an unresolved reserve-adequacy question, not mispriced quality. ROE and ROIC are trending down, F-score is 4, and Q3 results on Oct 28 can reset the book. Good but not compelling: conviction 3, no position.",
  "price_at_decision": 373.10,
  "price_date": "2026-10-08",
  "research_note": "research/EG/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE falls below the FY2024 level of 10.1%, showing reserve charges are eroding earnings power rather than being a one-off.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10.1}},
    {"text": "TTM ROIC falls below the FY2024 level of 8.2%, confirming the five-year decline in returns is continuing.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8.2}},
    {"text": "Shares outstanding stop shrinking (YoY change above 0%), signalling capital is being retained to shore up reserves rather than returned.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "The Q3 2026 earnings release (Oct 28) or a later quarter reports further prior-year North America casualty reserve strengthening."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 538.64, "basis": "Q3/Q4 show no further reserve charges, so the TTM ROE of 12.6% [RA] holds and the P/E method's bull value of 538.64 [fair value] is reached; below the blended bull of 625.81 because a P/B re-rating needs several clean quarters, and the macro overlay's neutral/small tilt (research/EG/2026-10-09-macro.md) leaves this unchanged."},
    "base": {"probability": 0.45, "target_price_12m": 425.24, "basis": "P/E reverts toward its 5y median of 9.1x [RA] on modestly lower earnings, matching the P/E method base of 425.24 [fair value]; below the blended base 468.98 because P/B at 0.9x [RA] stays capped while reserve adequacy is unproven, and the neutral macro tilt (research/EG/2026-10-09-macro.md) does not move it."},
    "bear": {"probability": 0.30, "target_price_12m": 289.53, "basis": "Another casualty reserve charge (Q2 transcript, https://stockanalysis.com/stocks/eg/transcripts/657888-q2-2026/) pushes ROE back toward the FY2022 6.4% trough [RA], matching the P/E method bear of 289.53 [fair value]; above the blended bear of 250.43 because the buyback-shrunk share count (-4.73% YoY [ST]) and book value support a floor, with the macro tilt neutral (research/EG/2026-10-09-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below the valuation file's base 468.98 x 0.8. The barrier is unresolved reserve adequacy in North America casualty; a lower price would not change the decision. Re-research after the Oct 28 Q3 results shows whether reserves have stabilised.",
  "replaces": null,
  "replacement_reason": null
}
```

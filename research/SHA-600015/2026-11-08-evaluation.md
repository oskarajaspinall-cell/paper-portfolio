# Evaluation: Hua Xia Bank Co., Limited (SHA:600015) — 2026-11-08
## Bear case
This is a value trap, not a mispricing. ROE has slipped from 8.2% in FY2021 to 7.3% in FY2025 and 6.3% TTM [RA], below any cost of equity carrying the 3.5% China premium, so the bank destroys value on each yuan retained [Certain]. Shares outstanding rose 9.73% YoY [ST], diluting holders at 0.3x book [Certain]. Piotroski F of 4 is middling [Certain]. The Direction change line (FCF margin down 76.3pp to 115.6% TTM [CF-T]) is deposit and loan flow noise for a bank, not earnings power, but it does mean the 12.99% FCF yield and the FCFE fair value of 15.40 rest on meaningless cash flows [Likely]. The DDM cross-check of 4.37 sits below the price [Certain]. P/B has been 0.3x at its 5y min, median and max, so a re-rating has no precedent [Certain]. The Q3 2026 filing was not read, and the LPR/NIM path is unverified (macro overlay) [Certain].
## Bull case
The price assumes shrinkage: the reverse DCF implies -19.0% revenue growth in year 1 [Certain]. P/E of 4.7x and P/B of 0.3x sit well below peer medians of 7.1x and 0.4x [RA] [Certain]. Net margin has held between 38.0% and 40.7% for five years [IS], so there is no sign of a credit-cost blow-up yet [Likely]. Mechanical base fair value is 13.00 against a 6.56 close [Certain]. Beta of -0.02 means the stock moves little with global equities [Certain]. The macro overlay sees mild yuan strength and no verified policy shock [Certain]. If ROE stabilises and dilution stops, the peer discount could narrow [Guessing]. But nothing in the evidence shows ROE stabilising or a catalyst, and without that, cheapness alone is not a thesis [Likely].
## Decision
```json
{
  "ticker": "SHA:600015",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A sub-scale Chinese regional bank with falling ROE below its cost of equity and ongoing dilution trades at 0.3x book, a discount that its fundamentals justify rather than contradict.",
  "rationale": "Cheap on every multiple, but ROE is falling (6.3% TTM), shares rose 9.73% YoY and P/B has never left 0.3x in five years. The mechanical fair value rests on bank cash flows that are noise and a re-rating with no precedent. Without evidence of ROE stabilising, this is a value trap: conviction 2, no position.",
  "price_at_decision": 6.56,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-600015/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE rises above 8.5%, back above its FY2021-FY2024 level of about 8.2%, showing returns have stabilised and recovered.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 8.5}},
    {"text": "Share count growth falls below 1% year on year (9.73% now), showing the dilution has stopped.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": 1}},
    {"text": "TTM net margin falls below 35% (38.0% now), showing spread compression or credit costs are worsening, which would confirm the avoid.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 35}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 8.7, "basis": "ROE stabilises and P/B re-rates from 0.3x toward the peer median 0.4x [RA]; still far below the mechanical bull of 13.40 because P/B has sat at 0.3x across its whole 5y range [RA], so the P/B + ROE fair value assumes a re-rating never seen."},
    "base": {"probability": 0.5, "target_price_12m": 6.7, "basis": "P/E holds near 4.7x, above its 5y median 4.2x [RA], on flat earnings as ROE drifts around the 6.3% TTM [RA] and dilution offsets retained earnings; below the mechanical base 13.00 because the FCFE leg uses deposit-driven bank cash flows (FCF margin 115.6% TTM vs 192.0% a year earlier [CF-T]) that are noise."},
    "bear": {"probability": 0.3, "target_price_12m": 5.3, "basis": "ROE keeps falling from 6.3% TTM [RA] as China property and margin pressure (unverified LPR path, macro overlay research/SHA-600015/2026-11-08-macro.md) hit earnings and P/E returns toward its 5y low 3.7x [RA], toward the DDM cross-check of 4.37 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: ROE is deteriorating below the cost of equity and dilution continues, and P/B has been 0.3x for five years, so a lower price would not change the decision; it needs ROE stabilisation and an end to dilution.",
  "replaces": null,
  "replacement_reason": null
}
```

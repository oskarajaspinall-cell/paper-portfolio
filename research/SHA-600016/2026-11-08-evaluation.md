# Evaluation: China Minsheng Banking Corp. (SHA:600016) — 2026-11-08
## Bear case
Profitability is eroding every year: ROE fell from 6.2% (FY2021) to 4.5% (FY2025) and 3.7% TTM, and net margin from 38.0% to 31.7% TTM [RA, IS] [Certain]. A bank earning well below its cost of equity justifies a discount to book, so the 0.2x P/B is a value trap, not a margin of safety [Likely]. Shares outstanding rose 8.46% YoY: issuing equity at 0.2x book dilutes holders heavily [ST] [Certain]. Piotroski F-score is 2 [ST] [Certain]. P/E of 6.7x sits above its own 5y max of 6.2x because earnings are falling faster than the price [RA] [Certain]. The flagged FCF-margin direction change (0.9% to -88.4% TTM) [CF-T] reflects loan and deposit flows, not a cash problem, so it does not drive the thesis [Likely]. The dividend-discount value of 1.97 is far below the price [fact sheet Fair value] [Certain]. The Q3 2026 filing was not reviewed [Guessing].
## Bull case
The price already discounts shrinkage: the reverse DCF implies -11.9% year-1 revenue growth [fact sheet Fair value] [Certain]. P/B of 0.2x is below its own 5y minimum and half the peer median of 0.4x [RA] [Certain]. The mechanical base fair value of 4.77 sits well above the 3.40 close, and even the bear value of 3.42 roughly matches the price [fact sheet Fair value] [Certain]. If the ROE slide stabilises, a modest re-rating toward peers' book multiples is plausible [Guessing]. The yuan's recent gain is a small translation tailwind (research/SHA-600016/2026-11-08-macro.md) [Certain]. Beta of 0.16 limits market-driven drawdowns [ST] [Likely]. But no evidence in the fact sheet or note shows the turn in returns has begun, so the bull case rests on a hope of mean reversion rather than a visible catalyst [Likely].
## Decision
```json
{
  "ticker": "SHA:600016",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A low-return Chinese joint-stock bank with ROE falling to 3.7% TTM, dilutive equity issuance and a Piotroski score of 2 is cheap on book for a reason, with no evidence yet that profitability is stabilising.",
  "rationale": "The 0.2x P/B and mechanical base fair value look attractive, but the base rests on a sustainable ROE the falling trend does not support, dilution at deep discount to book destroys per-share value, and quality is deteriorating. Good-looking cheapness is not high conviction; AVOID.",
  "price_at_decision": 3.40,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-600016/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE recovers above 6% (3.7% now, 6.2% in FY2021), showing profitability has turned and the book discount can narrow.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 6}},
    {"text": "Share count growth turns negative YoY (8.46% now), ending dilution at a deep discount to book.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": 0}},
    {"text": "TTM net margin recovers above 36% (31.7% now), back toward the FY2021-FY2023 level of about 38%.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 36}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 4.34, "basis": "ROE stabilises and P/B re-rates toward peers' 0.4x [RA], reaching the P/B + ROE base value of 4.34 [fact sheet Fair value]; below the blended base 4.77 because the FCFE leg extrapolates bank cash flows that are not meaningful."},
    "base": {"probability": 0.5, "target_price_12m": 3.42, "basis": "ROE keeps drifting lower from 3.7% TTM [RA] and P/B stays at its 0.2x floor, so the price tracks the mechanical bear fair value of 3.42 [fact sheet Fair value]; the falling trend argues against the mechanical base."},
    "bear": {"probability": 0.3, "target_price_12m": 2.66, "basis": "Further dilution (8.46% share growth YoY [ST]) and margin erosion (net margin 31.7% TTM [IS]) push value to the P/B + ROE bear of 2.66 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: falling ROE, dilution and a Piotroski score of 2 mean a lower price would not change the decision until profitability stabilises.",
  "replaces": null,
  "replacement_reason": null
}
```

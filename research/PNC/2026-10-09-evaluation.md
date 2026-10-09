# Evaluation: The PNC Financial Services Group, Inc. (PNC) — 2026-10-09
## Bear case
The price of $219.68 sits above every own-history fair value: base $204.48, bull $210.19 and bear $167.68 [ST] [Certain]. P/B of 1.5x is at the 96th percentile of its 5y range and 14% above the 1.3x peer median [RA] [Certain]. You pay a premium multiple for a scaled incumbent without a structural moat [Likely]. Quality signals are only middling, with a Piotroski F-Score of 4 [ST] [Certain]. The macro overlay tilts toward bear (small): DGS10 at 5.28% (+0.72pp 3m) raises the discount rate, and HY spreads widening +0.41pp in 1m is an early provisioning risk (research/PNC/2026-10-09-macro.md) [Likely]. Q3 results on Oct 15 are a binary event before any entry could settle [Certain]. The stock has fallen 8.3% below its 50-day average with relative strength −15.0pp vs SPY over 6m [HI] [Certain]. Weak momentum has not yet produced value [Likely].

## Bull case
Profitability is improving steadily. ROE has risen from 10.4% (FY2021) to 12.6% TTM, and net margin from 28.4% to 31.4% [RA,IS] [Certain]. P/E of 12.1x is at only the 21st percentile of its 5y range [RA] [Certain]. The reverse DCF implies −1.6% year-1 growth, a modest bar [ST] [Certain]. The prime-rate hike to 7.00% lifts loan yields now (fact-sheet headline) [Likely]. Redeeming the Series S preferreds signals ample capital [Likely]. The FCFE DCF base of $260.73 sits well above the price [ST] [Certain]. The coast-to-coast branch build-out is on track, which could extend the low-cost deposit franchise [Likely]. Still, the best-fit method for banks (P/B + ROE, $176.36 base) does not support the price, so upside rests on ROE continuing to rise beyond its own history [Guessing].

## Decision
```json
{
  "ticker": "PNC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "PNC is a well-run regional bank with rising ROE, but at 1.5x book (96th percentile of its 5y range, 14% above peers) the price already exceeds even its own-history bull fair value.",
  "rationale": "Quality is improving, but there is no valuation edge. The price is above the bear, base and bull fair values, and P/B is at the top of its 5y range and above peers. The macro tilt (rising real yields, wider HY spreads) leans bear. Q3 results are imminent. This is good but not compelling, so AVOID; cash is acceptable.",
  "price_at_decision": 219.68,
  "price_date": "2026-10-08",
  "research_note": "research/PNC/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE falls below 10%, reversing the FY2021-TTM improvement from 10.4% to 12.6%.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "TTM net margin falls below 27%, giving back the expansion since FY2023 (26.9%) and signalling provisioning or NIM pressure.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 27}},
    {"text": "Q3 2026 or later results show ROE rising above its 5y range and sustained, which would make the bull fair value catch up with the price (would raise conviction)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 240.0, "basis": "ROE keeps rising from 12.6% TTM [RA] and P/E holds near its 5y median of 12.4x [RA], partly closing toward the FCFE DCF base of 260.73 [ST]; this sits above the fact-sheet bull fair value of 210.19 because it assumes ROE beyond its own history."},
    "base": {"probability": 0.5, "target_price_12m": 205.0, "basis": "P/B mean-reverts from 1.5x (96th percentile) toward its 5y median of 1.4x [RA], consistent with the fact-sheet base fair value of 204.48 [ST]."},
    "bear": {"probability": 0.3, "target_price_12m": 167.68, "basis": "Fact-sheet bear fair value of 167.68 [ST]; probability raised by the macro overlay's small bear tilt (DGS10 +0.72pp 3m and HY spreads +0.41pp 1m lift the discount rate and provisioning risk, research/PNC/2026-10-09-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2 is below the entry-watch threshold of 3; no entry price is set.",
  "replaces": null,
  "replacement_reason": null
}
```

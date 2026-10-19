# Evaluation: Bank of Hangzhou Co., Ltd. (SHA:600926) — 2026-10-19
## Bear case
The cheapness is not evident on the metrics that matter for a bank. P/B of 0.7x sits mid-range of its own 5-year history (0.5x–0.8x) and level with the peer median, and P/E of 6.3x is near its 5y median of 6.1x [Certain] (RA). The headline +49.5% base fair value leans on an FCFE DCF built on bank "free cash flow" that the note itself says reflects deposit and loan-book movements, not distributable cash [Likely]. The P/B + ROE method, the one suited to banks, gives a base of 20.07 [Certain]. ROE has slipped from 13.7% to 12.1% TTM and the Piotroski score is a middling 4 [Certain] (RA, ST). There is no NPL or provision-coverage data and no allowlisted primary source, so credit quality, the main risk in a Chinese regional bank, cannot be verified [Certain]. Results land Oct 28, 2026 [Certain] (OV).

## Bull case
Profitability has improved over five years: ROE rose from 10.8% (FY2021) and net margin climbed every year to 57.8% TTM [Certain] (RA, IS). At 6.3x earnings the stock trades below the 7.0x peer median [Certain] (RA). The reverse DCF implies a -10.6% year-1 revenue decline, which looks too pessimistic for a bank still earning a 12.1% ROE [Likely]. Even the bank-appropriate P/B + ROE method's base value of 20.07 sits above the 16.83 close [Certain]. Dilution is minimal at 0.83% YoY [Certain] (ST). A deposit franchise in wealthy Zhejiang is a plausible moat [Guessing]. With a 5y beta of 0.08, returns are largely uncorrelated with the rest of the portfolio [Certain] (ST). Good but not compelling: without asset-quality evidence the rerating case lacks support, so conviction stays at 3 and the decision is AVOID.

## Decision
```json
{
  "ticker": "SHA:600926",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A Zhejiang city commercial bank with an improving but recently fading ROE trades mid-range of its own P/B and P/E history, and its credit quality, the key risk, cannot be verified from the available data.",
  "rationale": "The bank-appropriate P/B + ROE value gives only moderate upside. The headline fair value is inflated by an FCFE model that is not meaningful for a deposit-taker. ROE is off its peak, the F-score is 4 and there is no asset-quality data. Good but not compelling, so conviction is 3: AVOID. Cash is acceptable.",
  "price_at_decision": 16.83,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-600926/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROE (statistics page) falls below 10%, reversing the five-year improvement from 10.8% and signalling credit-cost or margin pressure.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "TTM net (profit) margin falls below 50%, giving up most of the five-year rise to 57.8% and pointing to rising provisions.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 50}},
    {"text": "Shares outstanding grow more than 5% YoY (0.83% now), showing capital is being raised to cover credit losses.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 22.01, "basis": "Q3 results on Oct 28, 2026 [OV] confirm stable credit and ROE recovers toward its 13.7% FY2023/24 peak [RA], lifting value to the P/B + ROE bull of 22.01 [fact sheet fair value]; the FCFE-driven blended bull of 29.86 is set aside because bank cash flow reflects deposit flows (note section 5)."},
    "base": {"probability": 0.5, "target_price_12m": 18.0, "basis": "P/B holds near its 0.7x 5y median [RA] while book compounds on a 12.1% TTM ROE [RA], so the target sits below the P/B + ROE base of 20.07 because ROE is easing and the blended base of 25.16 relies on the non-meaningful FCFE DCF (note section 3)."},
    "bear": {"probability": 0.25, "target_price_12m": 13.0, "basis": "Unverified asset quality (note section 2) shows up as higher credit costs, ROE keeps slipping from 13.7% toward 10.8% [RA] and P/B moves toward its 5y low of 0.5x [RA], below the P/B + ROE bear of 16.37."}
  },
  "entry_price": 12.0,
  "entry_basis": "P/B back at its 5y low of 0.5x [RA]. The default base 25.16 x 0.8 is above the current price, and that base is inflated by a bank FCFE DCF, so the anchor is the bank's own P/B floor, where the price would compensate for the unverified credit risk.",
  "replaces": null,
  "replacement_reason": null
}
```

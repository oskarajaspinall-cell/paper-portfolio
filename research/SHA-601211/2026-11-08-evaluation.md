# Evaluation: Guotai Haitong Securities Co., Ltd. (SHA:601211) — 2026-11-08
## Bear case
This is a low-return, market-beta business. ROIC is 2.2% TTM and ROE 8.8%, below FY2021's 10.3% [Certain] [RA]. The 54.7% operating margin is a 2-year high driven by onshore turnover, so it is cyclical, not a moat [Likely] [IS-T]. The Direction change line matters: FCF margin is 68.7pp below its 2-year high of 275.7%. That reflects client-balance and working-capital swings, not earnings power [Likely] [CF-T]. It also means the FCFE/DCF fair value (base 22.96) is built on cash flow that is not meaningful for a broker, so the apparent +39.5% upside is unreliable [Likely]. Shares rose 32.86% YoY from the merger, so per-share growth lags [Certain] [ST]. Other negatives: a Piotroski score of 4, leverage that is [data unavailable], an ICAC detention at the Hong Kong unit with unknown impact, and a -15.6% 12-month trend [Likely].
## Bull case
The stock trades at 9.6x P/E, below its 5y minimum of 10.0x and 3% below peers. P/B is 0.7x, at the floor of its 0.7x–1.0x range [Certain] [RA]. The price implies only 0.2% year-1 revenue growth, while TTM margins are rising: operating margin is up 4.3pp and ROIC up 0.5pp year on year [Certain] [IS-T, RA-T]. The P/E method alone gives a base of 21.25, above the close [Certain]. As China's largest state-backed broker after the merger, it gains scale in a licence-limited industry that policy is consolidating [Likely] (https://www.scmp.com/business/china-business/article/3292700/china-spur-mergers-us16-trillion-stockbroking-sector-after-guotai-haitong-deal). A sustained onshore turnover recovery could re-rate it toward its 12.4x median P/E [Guessing].
## Decision
```json
{
  "ticker": "SHA:601211",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "China's largest state-backed broker is cheap on P/E and P/B against its own history, but its sub-cost-of-capital returns, cyclical peak margins and merger dilution mean the discount is largely earned.",
  "rationale": "Cheapness rests on peak-cycle earnings and an FCFE fair value built on meaningless broker cash flow. ROIC of 2.2% and ROE of 8.8% do not clear the cost of equity. The scenario expected value sits near the price. Good-but-not-compelling at best: AVOID, conviction 2.",
  "price_at_decision": 16.46,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-601211/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE rises above 11.1% (the FY2025 level) and holds, showing the merged firm earns returns nearer its cost of equity through the cycle.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 11.1}},
    {"text": "TTM ROIC rises above 3.0% (the FY2021 level), showing merger synergies lift returns structurally rather than cyclically.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 3.0}},
    {"text": "TTM operating margin falls below 40%, showing the current margin is a cyclical peak and confirming the AVOID.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 21.25, "basis": "Onshore activity keeps TTM operating margin near its 54.7% 2-year high [IS-T] and the market pays the P/E method's base value of 21.25 [fact sheet Fair value], toward the 12.4x 5y median P/E [RA]; below the FCFE bull of 39.73 because broker FCF is client-balance driven [CF-T]."},
    "base": {"probability": 0.45, "target_price_12m": 17.16, "basis": "Earnings hold and the P/E stays near the bottom of its 5y range, so the stock meets the P/E method's bear value of 17.16 [fact sheet Fair value]; below the FCFE base of 22.96 because the FCF margin of 207.0% is a working-capital artefact [CF-T]."},
    "bear": {"probability": 0.30, "target_price_12m": 12.16, "basis": "Turnover fades and margins mean-revert toward the FY2023 32.6% operating margin [IS], with ROE back toward its 5.9% FY2023 trough [RA]: the mechanical bear fair value of 12.16 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: price is not the main obstacle. The stock is already below its 5y minimum P/E; the issue is sub-cost-of-capital returns and cyclical earnings, so a lower price alone would not justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

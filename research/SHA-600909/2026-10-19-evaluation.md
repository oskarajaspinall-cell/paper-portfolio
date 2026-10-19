# Evaluation: Huaan Securities Co., Ltd. (SHA:600909) — 2026-10-19
## Bear case
Huaan is a mid-sized Chinese broker with no visible moat: ROIC sat at 2.2% for FY2022-24 and is only 4.4% TTM [Certain], likely below its cost of capital [Likely]. The low P/E of 11.2x against its 5y range of 15.0x-19.2x is a cyclical-peak illusion: TTM ROE of 12.5% versus 6.2%-6.8% in FY2023-24 reflects a turnover boom [Likely]. Against peers it is expensive: P/E 11.2x vs 9.6x, P/FCF 4.8x vs 2.8x, P/B 1.3x vs 0.7x [Certain], so peer-premium compression is the more likely re-rating [Likely]. The FCF yield of 20.69% is a trading-book artefact; FCF/NI was -415.9% in FY2023 [Certain]. Mechanical fair value gives only +8.8% base against -32.6% bear [Certain]. The macro overlay tilts small toward bear: dollar strength and a hawkish Fed may limit PBOC easing that drives turnover [Guessing].
## Bull case
Earnings power is improving: operating margin rose to 60.7% TTM from 41.3% in FY2023 and ROE to 12.5% [Certain]. Shares fell 2.01% YoY, so there is no dilution [Certain]. If Chinese stimulus sustains turnover and IPO issuance, operating leverage could lift earnings further and push the multiple back toward its 5y range [Guessing]. The bull fair value of 10.94 CNY [Certain] and the 52-week high of 12.95 [Certain] show how much upside a hot market can bring. Beta is low at 0.79 [Certain]. Earnings on Oct 29, 2026 could confirm that the recovery is holding [Likely]. Still, every leg of this case depends on the market cycle rather than on the franchise.
## Decision
```json
{
  "ticker": "SHA:600909",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A moat-less, cyclical mid-sized Chinese broker at peak-cycle ROE that trades at a premium to larger peers, with thin base-case upside and a deep bear case.",
  "rationale": "Persistently low ROIC, earnings tied to market turnover, and P/E, P/FCF and P/B all above the peer medians. Base fair value is barely above the price while the bear case is far below, and the macro tilt leans bear. Low P/E against its own history reflects a cyclical earnings peak, not cheapness. Not compelling; cash is preferable.",
  "price_at_decision": 7.19,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-600909/2026-10-19.md",
  "triggers": [
    {"text": "ROIC rises structurally above 6%, showing returns on capital clear the cost of capital rather than tracking turnover", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 6}},
    {"text": "ROE sustained above 15% through a weaker turnover period, evidencing a structural rather than cyclical improvement", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 15}},
    {"text": "FY2026 results show FCF conversion positive for a third consecutive fiscal year alongside stable net margin, implying earnings backed by cash"}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 10.94, "basis": "Stimulus sustains turnover and ROE holds near 12.5% TTM [RA], matching the bull FCFE fair value of 10.94 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 7.83, "basis": "Earnings normalise modestly and the stock trades at the base FCFE/DCF fair value of 7.83 [fact sheet Fair value], with peer premium on P/B persisting [RA]."},
    "bear": {"probability": 0.35, "target_price_12m": 4.85, "basis": "Turnover fades so ROE reverts toward the FY2023-24 range [RA] and the peer P/B premium compresses, reaching the bear fair value of 4.85; probability raised by the macro overlay's small tilt toward bear (research/SHA-600909/2026-10-19-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: the obstacle is weak, cyclical quality (low ROIC, no moat), not price; a lower price alone would not justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

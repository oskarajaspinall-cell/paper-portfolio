# Evaluation: Mizrahi Tefahot Bank (TLV:MZTF) — 2026-11-09
## Bear case
The price already discounts peak returns. P/E of 10.5x sits above the top of its own 5-year range (6.5x to 10.3x, median 7.5x) and P/B of 1.5x is at 90% of its range, roughly in line with Israeli peers [Certain] [RA]. ROE has eased from 19.8% (FY2022) to 16.0% TTM as rates fall and the state takes a share via a special tax and client relief [Certain] [RA]; that is partly cyclical normalisation, but the political reach on bank profits is recurring [Likely]. The Direction change line (FCF margin from 134.1% to 95.1% over 12 months) reflects deposit and loan flows, not earnings quality, so it does not threaten the thesis [Likely]. Piotroski F is 4 [Certain] [ST]. The mechanical fair value is unusable (base 135.15 against 22,450 ILA, a unit mismatch), so there is no independent valuation anchor [Certain]. Israel geopolitical risk is unhedged [Likely].
## Bull case
A high-return domestic oligopoly lender: ROE of 16.0% TTM and 16% in Q2 2026 despite the special tax, relief measures and lower rates [Likely] (/quote/tlv/MZTF/transcripts/787722-q2-2026/). Net margin rose from 30.1% to 38.7% TTM [Certain] [IS]. Management reports strong credit growth and pays out 50% of quarterly profit as dividends, with dilution minimal at 0.26% YoY [Certain] [ST]. Management's ex-tax Q1 ROE of 16.3% suggests the levy masks underlying returns that could re-emerge if it lapses [Guessing]. Beta of 0.14 makes it a diversifier [Certain]. But at in-line peer multiples and the top of its own range, the upside is a modest re-rating plus dividends, not a mispricing [Likely].
## Decision
```json
{
  "ticker": "TLV:MZTF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "ROE eased from 16.9% (FY2025) to 16.0% TTM because of a special tax, client relief and lower rates; management puts Q1 ROE ex-tax and relief at 16.3% (/quote/tlv/MZTF/transcripts/787731-q1-2026/). The FCF margin swing reflects bank balance-sheet flows. Capital and dividends are intact.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Falling Bank of Israel rates plus political levies compress ROE toward the low teens, while P/E already sits above its 5y range.", "veto": null},
  "thesis": "A high-ROE Israeli mortgage lender in a concentrated market, but priced at the top of its own multiple history with returns past their peak.",
  "rationale": "Quality is good (ROE 16.0%, narrow moat), but P/E is above its 5-year maximum and P/B near the top of its range and in line with peers, so there is no margin of safety. The mechanical fair value is unreliable. Good but not compelling, so AVOID; a re-rating back to median book multiples would change it.",
  "price_at_decision": 22450.00,
  "price_date": "2026-11-06",
  "research_note": "research/TLV-MZTF/2026-11-09.md",
  "triggers": [
    {"text": "ROE (TTM) falls below 13%", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 13}},
    {"text": "Net (profit) margin falls below 33%", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 33}},
    {"text": "Shares outstanding grow more than 3% YoY (capital-raising dilution)", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 24000, "basis": "ROE holds near 16% with credit growth and P/B moves to its 5y max of 1.6x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 22450, "basis": "ROE stays around 16.0% TTM and P/B stays at 1.5x, in line with the peer median [RA]; return comes from the 50% payout."},
    "bear": {"probability": 0.30, "target_price_12m": 19450, "basis": "Lower rates and the special tax push ROE down and P/B reverts to its 5y median of 1.3x [RA]; the mechanical fair value is ignored as unreliable (unit mismatch)."}
  },
  "entry_price": 19450,
  "entry_basis": "Mechanical fair value is unreliable, so entry is anchored instead on P/B back at its 5y median of 1.3x [RA] at the current book value, where the same quality would come with a margin of safety.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Wan Hai Lines Ltd. (TPE:2615) — 2026-11-15
## Bear case
Container shipping is a commodity business with no durable moat; returns track the freight cycle [Likely]. ROIC went from 124.6% (FY2021) to -5.8% (FY2023), and FCF margin hit -48.3% that year [Certain]. The fact sheet's Direction change lines show ROIC, operating margin and FCF margin falling over 5 fiscal years but rising over the last 12 months, still below their 2-year highs (ROIC 21.4%) [Certain]; the recovery is cyclical, not structural improvement [Likely]. The low P/E of 5.9x sits at 76% of its 5y range because profits are near cyclical highs [Likely]. Base fair value 106.14 TWD is below the 107.50 close and the bear value 48.84 shows how far a freight normalisation could take it [Certain]. The price sits 19.5% above its 200-day average after +31.7% in 12 months: an extended price risks a sharp de-rating if rates soften [Likely]. Country revenue mix and Taiwan Strait / Red Sea exposure are unverified [Guessing].
## Bull case
The balance sheet is net cash (net debt/EBITDA -1.34x) with a Piotroski F of 7, so a downturn is survivable [Certain]. The last 12 months are improving: ROIC 15.4% to 17.5%, operating margin 26.5% to 28.9%, FCF margin 7.9% to 18.3% [Certain]. FCF yield is 10.31% and EV/EBITDA 3.4x sits at 7% of its 5y range and 18% below peers, P/B 1.0x near its 5y low [Certain]. The trend is strong: +44.7% over 6 months and +43.1pp relative strength vs SPY [Certain]. Beta of 0.58 keeps portfolio volatility contribution modest [Likely]. If freight rates hold, the stock could revisit its 52-week high of 134.50 [Guessing].
## Decision
```json
{
  "ticker": "TPE:2615",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROIC, operating margin and FCF margin are rising over the last 12 months and 3 years (RA-T, IS-T, CF-T); the 5-year fall reflects the FY2021-22 freight peak.",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Freight-rate normalisation pulls earnings back toward the bear case (fair value bear 48.84 TWD); an extended price (19.5% above the 200-day average) would de-rate with it.",
    "veto": null
  },
  "thesis": "A net-cash container carrier riding a cyclical upswing, priced at its mechanical base fair value with no moat to protect returns when freight rates normalise.",
  "rationale": "Quality is cyclical, not durable; base fair value sits just below the price and the bear value is far lower. Trend and net cash do not offset a high, likely freight-cycle risk with no moat. Good-but-not-compelling is an AVOID.",
  "price_at_decision": 107.50,
  "price_date": "2026-11-13",
  "research_note": "research/TPE-2615/2026-11-15.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 10%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Operating margin (TTM) falls below 20%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "FCF margin (TTM) falls below 8%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 134.50, "basis": "Freight rates hold and the rising 12-month margins (operating margin 28.9% [IS-T]) carry the price back to its 52-week high of 134.50 [HI], above the mechanical bull 111.97 because the EV/EBITDA model caps on history."},
    "base": {"probability": 0.45, "target_price_12m": 106.14, "basis": "EV/EBITDA stays near its 5y median 3.5x [RA], matching the mechanical base fair value of 106.14 TWD [valuation]."},
    "bear": {"probability": 0.30, "target_price_12m": 48.84, "basis": "Freight normalisation cuts EBITDA as in FY2023 (operating margin -8.1% [IS]), in line with the mechanical bear fair value of 48.84 TWD."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the missing moat and the high freight-cycle risk cap the score below conviction 4 at any price (a lower price would also lose the trend-strength points), and a lower price would likely come with falling earnings. A lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

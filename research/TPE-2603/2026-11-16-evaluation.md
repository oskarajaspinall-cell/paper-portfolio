# Evaluation: Evergreen Marine Corporation (Taiwan) Ltd. (TPE:2603) — 2026-11-16
## Bear case
Container shipping is a commodity service with no moat; returns follow freight rates [Likely]. ROIC fell from 105.1% (FY2022) to 12.2% TTM and is down 3.8pp in the last 12 months, 13.9pp below its 2-year high; operating and FCF margins are falling too [Certain]. The cause is cyclical normalisation of freight rates, not lost share, but nothing in the inputs says the descent has ended [Likely]. The price is extended: P/E 7.0x sits 79% up its 5y range against a 3.5x median, P/FCF 5.4x is above its 5y max, and the close of 257.50 is above even the mechanical bull fair value of 233.29 [Certain]. The 18.42% FCF yield is a near-peak FCF figure; FY2023 showed FCF margin can turn negative at -9.5% [Certain]. A price +19.0% above its 200-day average risks a sharp de-rating if rates slow [Likely].
## Bull case
The balance sheet is net cash (net debt/EBITDA -0.08x) and FCF conversion is 129.2% of net income TTM, so the company can ride a downturn without distress [Certain]. P/B 0.9x is only 21% up its 5y range and below the peer median of 1.0x [Certain]. Momentum is strong: +38.5% in 12 months and +28.1pp ahead of SPY, with the 50-day average +14.6% over the 200-day [Certain]. Operating margin of 20.7% TTM is still well above the FY2023 trough of 12.0%, and if freight stays firm the stock trades on 7.0x earnings, below the peer median of 7.5x [Likely]. Dilution is negligible at 0.18% YoY [Certain].
## Decision
```json
{
  "ticker": "TPE:2603",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC, operating and FCF margin are falling as freight rates normalise from the 2025 peak (operating margin 34.8% at 2025-03-31 to 20.7% TTM [IS-T]); this is the freight cycle with the balance sheet intact (net debt/EBITDA -0.08x [RA]), not lost share or a broken model, though the cycle may have further to fall.",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Freight rates keep mean-reverting, pulling earnings and FCF back toward trough levels (FY2023 ROIC 5.5%, FCF margin -9.5% [RA,CF]) and de-rating a price that already sits above the mechanical bull fair value.",
    "veto": null
  },
  "thesis": "A net-cash container line priced on near-peak cyclical cash flows with no moat; the trend is strong but the price already exceeds the mechanical bull fair value.",
  "rationale": "Cyclical commodity business with no moat, returns falling over the last year, and a price above even the bull fair value; the strong trend and net cash do not offset the high risk of freight-rate mean reversion. The scorecard is low; AVOID.",
  "price_at_decision": 257.50,
  "price_date": "2026-11-13",
  "research_note": "research/TPE-2603/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 15% (freight downturn deepening)", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 8%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "TTM FCF margin falls below 10%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 274.50, "basis": "Freight stays firm and the stock retests its 52-week high of 274.50 [HI] on TTM margins holding near 20.7% [IS-T]."},
    "base": {"probability": 0.45, "target_price_12m": 233.29, "basis": "Modest freight normalisation de-rates EV/EBITDA from 4.1x toward the mechanical bull fair value of 233.29 [fact sheet Fair value]; set above the mechanical base because P/B 0.9x sits low in its 5y range [RA] and net cash supports the floor."},
    "bear": {"probability": 0.30, "target_price_12m": 157.49, "basis": "Freight rates mean-revert and EV/EBITDA returns to its 5y median 2.8x [RA], i.e. the mechanical base fair value 157.49 [fact sheet Fair value]; not the mechanical bear of 23.41, which net cash and P/B near its 5y low make implausible."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the only obstacle: there is no moat and returns are falling with the freight cycle, so a lower price alone would not lift this to conviction 4; re-research on a fresh cycle low.",
  "replaces": null,
  "replacement_reason": null
}
```

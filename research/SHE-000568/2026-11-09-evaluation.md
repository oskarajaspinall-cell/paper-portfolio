# Evaluation: Luzhou Laojiao Co.,Ltd (SHE:000568) — 2026-11-09
## Bear case
Profitability is collapsing on a rolling basis, not drifting: ROIC fell from 58.3% to 19.3% and operating margin from 54.8% to 39.8% in twelve months, and FCF margin went to 0.0% TTM [Certain]. Every Direction change line points the same way, and the cause is not established in the research: it is consistent with baijiu demand or price weakness, which for a premium brand would hit the pricing power the moat rests on [Likely]. TTM gross margin slipping to 83.4% from 86.6% hints at price or mix pressure, not only cost [Likely]. On depressed earnings the stock is not cheap: P/E 20.6x sits near its 5y median of 19.9x, EV/EBITDA 13.2x is above peers' 12.0x, and the mechanical base fair value is only +3.5% above the price while the bear value is -28.5% [Certain]. Cash conversion has vanished for unverified reasons [Certain]. Piotroski F is only 5 [Certain].
## Bull case
This is a historically superb franchise: 80%+ gross margins and ROIC above 40% every fiscal year FY2021-FY2025 [Certain]. The balance sheet is net cash (net debt/EBITDA -2.25x) with Altman Z 9.75, so a downturn cannot become distress [Certain]. P/B 2.5x is below its 5y minimum of 3.4x and the share price is -39.1% over 12 months, so much bad news is priced [Certain]. If the decline is a cyclical destocking that ends, EV/EBITDA recovering toward the 5y median on normalised EBITDA supports the bull value of 129.63 [Guessing]. The +10.0% reaction on 3.9x volume after the Q3 2026 filing suggests the results were better than feared [Likely], though their content was not read [Certain]. Beta 0.25 keeps it a low-correlation holding [Certain].
## Decision
```json
{
  "ticker": "SHE:000568",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "structural",
    "decline_evidence": "ROIC 58.3% -> 19.3%, operating margin 54.8% -> 39.8% and FCF margin 49.4% -> 0.0% over the last 12 months [RA-T, IS-T, CF-T], with TTM gross margin down to 83.4% [IS]; the note could not establish a guided reset, one-off or investment cause, so a temporary label is unsupported and the decline is treated as a loss of pricing power until evidence shows otherwise.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Baijiu price and demand weakness persists, so the premium-brand margin and cash conversion do not recover and the current multiples are on peak-ish rather than trough earnings.",
    "veto": null
  },
  "thesis": "A net-cash premium baijiu franchise whose returns, margins and cash conversion are falling fast for an unexplained reason, trading near its own median earnings multiples with little mechanical upside.",
  "rationale": "Quality is deteriorating sharply on a rolling basis with no cited temporary cause, cash conversion is at zero and valuation is mid-range on depressed earnings with the bear value further from the price than the base. Net cash removes distress risk but not the thesis risk. AVOID; no position.",
  "price_at_decision": 81.17,
  "price_date": "2026-11-06",
  "research_note": "research/SHE-000568/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 50%, showing the margin reset was temporary and pricing power is intact.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 50}},
    {"text": "TTM FCF margin recovers above 20%, showing cash conversion has normalised.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 20}},
    {"text": "TTM ROIC recovers above 30%, showing returns are rebuilding toward the franchise's history.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 30}},
    {"text": "TTM gross margin falls below 80%, confirming structural price/mix erosion (would harden the AVOID).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 80}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 129.63, "basis": "Demand stabilises and EV/EBITDA recovers to the mechanical bull value of 129.63 [fact sheet fair value, RA]."},
    "base": {"probability": 0.45, "target_price_12m": 84.0, "basis": "Margins stay near the 39.8% TTM level and EV/EBITDA holds near its 5y median 13.9x, the mechanical base value of 84.00 [fact sheet fair value, RA, IS-T]."},
    "bear": {"probability": 0.35, "target_price_12m": 58.07, "basis": "The unexplained fall in ROIC and FCF margin continues [RA-T, CF-T], de-rating to the mechanical bear value of 58.07 [fact sheet fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: returns, margins and cash conversion are deteriorating with no established temporary cause, so a lower price on the same evidence would not justify conviction 4; re-examine when a margin or FCF recovery trigger fires.",
  "replaces": null,
  "replacement_reason": null
}
```

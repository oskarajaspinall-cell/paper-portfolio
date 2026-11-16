# Evaluation: Arch Capital Group Ltd. (ACGL) — 2026-11-16
## Bear case
The reinsurance cycle is turning: management cites reinsurance net premiums written down about 9% in Q3 and continued property-catastrophe pricing pressure [company-reported] (https://www.sec.gov/Archives/edgar/data/947484/000094748426000152/acgl-20260930.htm) [Certain]. ROIC of 15.9% is 4.8pp below its 2-year high of 20.7% and down over three years [RA-T] [Certain]; a soft market usually pushes it lower still [Likely]. Q3 was flattered by light catastrophe activity, so a normal or heavy cat year could hit earnings hard [Likely]. The mechanical base of 150.47 leans on P/B + ROE capitalising a near-peak ROE; the P/E method gives only 99.30, below the 109.61 close [Certain]. P/B of 1.6x is 18% above peers [RA] [Certain]. The price is 12.3% above its 200-day average after a 19.4% year; if earnings growth slows, that run can de-rate [Likely]. A co-founder stepping down as Chair adds modest uncertainty [Guessing].
## Bull case
ACGL earns ROE of 18.7% TTM, far above FY2022's 11.2% [RA] [Certain], from three diversified segments, so a soft reinsurance line is offset by mortgage and casualty insurance [company-reported] (same 10-Q) [Likely]. It trades at 8.9x P/E, 15% below the peer median of 10.6x, and EV/EBITDA sits at the 7th percentile of its 5y range [RA] [Certain]. Shrinking reinsurance premiums while buying back stock (shares -6.92% YoY [ST]) is disciplined capital allocation, not lost franchise [Likely]. The balance sheet is light (net debt/EBITDA 0.60x site definition [RA]) [Certain]. The trend is healthy: beating SPY by 14.8pp over 3 months, above both moving averages, RSI 65.9 [HI, ST] [Certain]. Higher yields lift reinvestment income on the short-duration book (macro overlay, context only) [Likely].
## Decision
```json
{
  "ticker": "ACGL",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC is flat on a year earlier but down over three years and 4.8pp below its 2024 high [RA-T]; the cause is the softening reinsurance and property-cat pricing cycle with Q3 reinsurance NPW down about 9% [company-reported] (https://www.sec.gov/Archives/edgar/data/947484/000094748426000152/acgl-20260930.htm), a cyclical trough with the balance sheet intact (net debt/EBITDA 0.60x [RA]) and buybacks continuing, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A softening reinsurance cycle plus a normal-to-heavy catastrophe year compresses ROE from 18.7% while the price, 12.3% above its 200-day average, de-rates.",
    "veto": null
  },
  "thesis": "A diversified, lightly levered specialty insurer earning high-teens ROE at a below-peer P/E with a healthy uptrend, bought despite a softening reinsurance cycle from near-peak returns.",
  "rationale": "The scorecard gives 4: high ROE, a light balance sheet, a below-peer P/E and trend strength, with the ROIC dip explained by a cyclical soft market. The P/E method below the price and catastrophe exposure argue for only the standard core size, which Python volatility-scales; no cap is breached, so nothing is replaced.",
  "price_at_decision": 109.61,
  "price_date": "2026-11-13",
  "research_note": "research/ACGL/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROE falls below 14%, giving up most of the rise from 11.2% (FY2022) to 18.7% and showing the soft cycle is breaking underwriting returns.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 14}},
    {"text": "TTM ROIC falls below 12%, back toward FY2021 levels (12.3%).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA (site definition) rises above 1.5x from 0.60x, showing capital returns or losses are straining the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Reinsurance net premiums written decline by more than 15% year on year for two consecutive quarters in the 10-Q."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 150.47, "basis": "ROE holds near 18.7% [RA] through the soft market and the stock reaches the mechanical base fair value of 150.47 (fact sheet Fair value)."},
    "base": {"probability": 0.5, "target_price_12m": 118.0, "basis": "P/E stays near 8.9x [RA] while buybacks (shares -6.92% YoY [ST]) lift per-share earnings against softer reinsurance pricing [company-reported]; below the mechanical base because P/B + ROE capitalises a near-peak ROE (note section 3)."},
    "bear": {"probability": 0.25, "target_price_12m": 85.47, "basis": "A heavy catastrophe year and continued reinsurance pricing pressure [company-reported] cut earnings and the stock falls to the mechanical bear fair value of 85.47 (fact sheet Fair value)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

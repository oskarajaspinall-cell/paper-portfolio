# Evaluation: The Charles Schwab Corporation (SCHW) — 2026-10-08
## Bear case
The price already sits at fair value: the FCFE DCF base is 93.55 vs a 95.58 close (-2.1%), with only +8.5% to the bull case and -41.5% to the bear [Certain]. The 17.4x P/E is "cheap" only against peak-rate earnings; ROE of 20.3% TTM rides on net interest revenue from swept cash, not on capital efficiency (ROIC flat at 8.6%) [Certain]. The macro overlay flags a one-month hawkish repricing (10y 5.27%, +0.49pp; fed funds up 0.25pp) that revives the 2022-23 cash-sorting and AFS/HTM-markdown playbook, when net margin fell to 26.8% [Likely]. AI competition from Vanguard and bearish options flow [Likely], rising short interest (+14.6%) [Certain] and -19.1pp relative strength over 6 months [Certain] show sentiment is still deteriorating. Q3 results on Oct 15 will reveal the cash mix; buying a week before is a coin-flip [Guessing].

## Bull case
Fundamentals are at five-year highs: ROE 20.3%, operating margin 50.2%, net margin 38.8% TTM, all rising [Certain]. P/E of 17.4x sits 43% below its own 5-year minimum and 16% below the peer median of 20.6x [Certain]. Shares fell 3.36% YoY on buybacks and the FCF yield is 6.50% [Certain]. A record net-new-asset quarter [Likely] and the Anthropic/Claude advisor tie-up [Likely] support organic growth from scale. Beta of 0.78 and low short interest (1.19%) limit risk [Certain]. The 3-month underperformance (-10.2pp vs SPY) may already discount much of the rate risk [Guessing].

## Decision
```json
{
  "ticker": "SCHW",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A scale brokerage earning record ROE and margins trades below its own 5-year P/E floor, but the price already matches the FCFE base fair value and a hawkish rate shock threatens the cash-sorting and securities-mark risks behind its earnings.",
  "rationale": "Quality is real and P/E is cheap versus history, but the mechanical fair value base (93.55) is below the price, upside to the bull case is only +8.5%, and the macro overlay tilts moderately toward bear just before Q3 results reveal client cash trends. Good but not compelling: conviction 3, no position.",
  "price_at_decision": 95.58,
  "price_date": "2026-10-07",
  "research_note": "research/SCHW/2026-10-08.md",
  "triggers": [
    {"text": "Thesis weakens further if TTM ROE falls below the FY2023 level of 13.1%, erasing the rise to 20.3% TTM and showing rate-driven earnings were transitory.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 13.1}},
    {"text": "Thesis weakens further if TTM operating margin falls below 40%, the FY2023-24 trough level, signalling a repeat of the 2022-23 net-interest squeeze.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}},
    {"text": "Thesis weakens further if TTM net margin falls below the FY2024 level of 30.3%, reversing the rise to 38.8% TTM.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 30.3}},
    {"text": "Q3 2026 earnings release (Oct 15) or later 10-Q shows client sweep cash and net interest revenue resuming growth with net new assets still at records, which would lift conviction."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 113.0, "basis": "P/E re-rates from 17.4x to the 20.6x peer median [RA, P:IBKR/RJF/LPLA/MS] on TTM earnings as record ROE (20.3%) and margins hold; above the DCF bull of 103.68 because that DCF ignores the peer-multiple gap, while the P/E method bull is 148.16."},
    "base": {"probability": 0.43, "target_price_12m": 93.55, "basis": "Fact-sheet FCFE DCF base fair value of 93.55 [IS,BS,CF,RA,ST], consistent with the reverse DCF already implying 4.6% growth, i.e. the price discounts steady fundamentals."},
    "bear": {"probability": 0.32, "target_price_12m": 69.64, "basis": "P/E method bear of 69.64 [RA]: renewed cash-sorting compresses net interest revenue as in FY2023 (net margin 26.8% [IS]); probability raised moderately per the macro overlay's toward-bear tilt (research/SCHW/2026-10-08-macro.md), target above the 55.92 DCF bear since FY2023 margins still kept ROE above 13%."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

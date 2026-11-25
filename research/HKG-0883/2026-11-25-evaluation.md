# Evaluation: CNOOC Limited (HKG:0883) — 2026-11-25
## Bear case
The fall has no verified cause: no earnings reaction in the last 10 sessions, the oil-price explanation is a guess and the Q3 release could not be read [Certain]. TTM ROIC of 24.1% may embed elevated oil prices; FY2021 ROIC was 15.1% [Likely]. The Direction change lines (ROCE 2.3pp below its 2-year high, FCF margin down over five fiscal years) are cyclical, not structural [Likely]. At 20.86 HKD the price is only 2.0% under base fair value 21.28, with bear 15.67; the multiples sit mid-range in their own 5-year history (P/E 6.0x vs a 4.8x median), so the discount to peers is persistent, not a mispricing [Likely]. The price is 16.4% below its 200-day average with negative 3- and 6-month momentum: no trend support [Certain]. State ownership and a governance probe of a former chairman add China-specific risk [Likely].
## Bull case
A net-cash (net debt/EBITDA -0.98x), low-cost producer with a 76.7% gross margin, 43.7% operating margin and a 13.71% FCF yield trades at 2.2x EV/EBITDA, well below peers [Certain]. The last year improved: ROIC rose from 21.0% to 24.1% and FCF margin from 23.1% to 27.5%; nine-month production hit a record and net income rose [Likely]. The Bohai discovery and the Lingshui 17-2 restart support volumes, and Beijing is pushing domestic output [Likely]. Shares fell 0.41% YoY and Piotroski F is 7 [Certain]. RSI of 23.4 suggests the sell-off is stretched [Guessing].
## Decision
```json
{
  "ticker": "HKG:0883",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no metric falling over 1 or 3 years; the fact sheet's Direction change lines (ROCE below its 2-year high, FCF margin down over 5 fiscal years) track the oil cycle: rolling ROIC rose from 21.0% to 24.1% and FCF margin from 23.1% to 27.5% over the last year, net cash keeps building (net debt/EBITDA -0.98x) [RA-T, CF-T, RA]; no lost share or broken model.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Oil prices fall from levels that may be inflating TTM returns, pulling earnings back toward the FY2021 ROIC of 15.1% [RA]; the dip itself has no verified cause.",
    "veto": null
  },
  "thesis": "A net-cash, low-cost offshore producer trades cheaply against peers but only around its own history and base fair value, with earnings tied to an oil price that has no verified floor.",
  "rationale": "The dip removed no obstacle: the price is still near base fair value, mid-range in its own multiples and below its 200-day average, and the fall's cause is unverified. Quality and balance sheet are strong, but the scorecard does not reach the buy bar. AVOID; watch the entry price.",
  "price_at_decision": 20.86,
  "price_date": "2026-11-24",
  "research_note": "research/HKG-0883/2026-11-25.md",
  "triggers": [
    {"text": "TTM operating margin falls below 35%, showing the low-cost advantage eroding beyond a normal oil-price swing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 35}},
    {"text": "TTM ROIC falls below 15%, back to the FY2021 trough.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA rises above 0.3x, meaning the net cash position is gone.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 0.3}},
    {"text": "Shares change YoY rises above +2%, signalling dilution.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 26.00, "basis": "EV/EBITDA re-rates to the bull fair value 26.00 [fact sheet Fair value] as record production and the Lingshui 17-2 restart lift volumes (Reuters 2026-10-30 URL in note)."},
    "base": {"probability": 0.5, "target_price_12m": 21.28, "basis": "EV/EBITDA holds near its 5y median 2.1x [RA] on TTM EBITDA, the base fair value 21.28 [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 15.67, "basis": "Oil-driven earnings fall back toward FY2021 returns (ROIC 15.1% [RA]) and the multiple compresses to the bear fair value 15.67 [fact sheet Fair value]."}
  },
  "entry_price": 18.09,
  "entry_basis": "valuation file: base 21.28 x 0.85."
}
```

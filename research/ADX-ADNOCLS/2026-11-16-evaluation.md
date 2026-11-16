# Evaluation: ADNOC Logistics & Services plc (ADX:ADNOCLS) — 2026-11-16
## Bear case
Earnings are at a freight-rate peak, not a new base: TTM ROIC 25.6% against a prior fiscal-year peak of 15.0%, and operating margin 27.6% against a 22.9% FY peak [Certain]. The Q3 call itself says volatility and geopolitics cloud 2027 [Likely]. Multiples below their 5y minimum (P/E 6.3x vs 12.4x) are the market's normal discount for peak shipping profits, and the reverse DCF already prices -4.2% revenue growth [Likely]; if rates normalise, earnings fall faster than revenue and the stock de-rates despite looking cheap [Likely]. The trend-strength case (price 9.6% above its 200-day average, +24.1% over 12 months) is exactly what reverses if growth slows [Likely]. Fleet purchases at peak rates risk poor returns [Guessing]. The Hormuz standoff can disrupt operations as well as lift rates [Likely]. ADNOC control leaves minorities little say; fair value is flagged unreliable (methods disagree 4.6x) [Certain].
## Bull case
The business is working on every rolling metric: ROIC, ROCE, operating and FCF margin all sit at their 2-year highs, with FCF margin up from 3.0% to 12.6% in a year [Certain]. Q3 delivered record revenue and net profit, with FY 2026 profit guidance raised (transcript) [Likely]. The balance sheet is near net-cash (net debt/EBITDA 0.05x, Piotroski 7) [Certain], so a downturn would be absorbed, not fatal. Parent-linked export volumes and fleet growth give a floor that a pure spot tanker owner lacks [Likely]. Even at a 7.56% FCF yield on 47.8% conversion, the stock trades at 4.9x EV/EBITDA vs peers at 10.3x [Certain], and shares outstanding fell 6.97% YoY [Certain]. Price is above a rising 200-day average without being overextended [Certain].
## Decision
```json
{
  "ticker": "ADX:ADNOCLS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Python finds no falling metric: ROIC, operating and FCF margin are all at their 2-year highs on the rolling view [RA-T, IS-T, CF-T].", "moat": "narrow", "key_risk": "high", "key_risk_text": "Freight rates normalise from the current peak (Q3 call: volatility and geopolitics cloud 2027), taking TTM ROIC back toward the FY2025 12.8% and de-rating a price supported by trend strength.", "veto": null},
  "thesis": "A near-net-cash, parent-anchored tanker and logistics operator earning peak freight returns trades far below its own and peers' multiples, but those multiples discount a likely rate normalisation.",
  "rationale": "Scorecard sets the conviction. Returns, balance sheet and trend are strong, but the earnings are cyclical-peak and the fair value is unreliable, so the low multiples are not a clear margin of safety. Q3 results confirm strength yet add no evidence that peak returns persist into 2027.",
  "price_at_decision": 6.74,
  "price_date": "2026-11-13",
  "research_note": "research/ADX-ADNOCLS/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, back under the FY2025 level of 12.8%, showing the rate windfall has fully reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM operating margin falls below 18%, under the FY2025 level of 18.1%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18}},
    {"text": "Net debt/EBITDA rises above 1.5x as fleet purchases are debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "TTM FCF margin falls below 3% while fleet capex continues.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 10.0, "basis": "Rates stay elevated and P/E re-rates part way toward its 5y minimum of 12.4x on TTM earnings [RA], below the DCF bull 22.27 since peak cash flows are not extrapolated."},
    "base": {"probability": 0.45, "target_price_12m": 7.0, "basis": "Partial rate normalisation offset by fleet growth keeps the price near the 50-day average 7.13 [HI], between the EV/EBITDA base 3.96 and the unreliable DCF base 18.33."},
    "bear": {"probability": 0.3, "target_price_12m": 4.8, "basis": "ROIC reverts toward FY2025 12.8% [RA] as rates normalise and the price returns to its 52-week low of 4.80 [HI], above the EV/EBITDA bear 3.56."}
  },
  "entry_price": 4.8,
  "entry_basis": "Fair value is flagged unreliable (base 13.54 x 0.8 is above the price), so anchor on the 52-week low of 4.80 [HI]: there the EV/EBITDA multiple would discount a full rate normalisation.",
  "new_evidence": {"type": "new_results", "text": "Q3 2026 results (2026-11-12) give a newer reporting period: TTM to 2026-09-30, https://stockanalysis.com/quote/adx/ADNOCLS/filings/3984276/"},
  "replaces": null,
  "replacement_reason": null
}
```

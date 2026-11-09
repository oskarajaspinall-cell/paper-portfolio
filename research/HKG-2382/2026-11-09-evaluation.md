# Evaluation: Sunny Optical Technology (Group) Company Limited (HKG:2382) — 2026-11-09
## Bear case
Sunny sells largely commoditised handset optics: gross margin of 19.5% TTM against 23.3% in FY2021 shows thin pricing power [Certain], and returns collapsed to a 5.5% ROIC in FY2023 when the handset cycle turned [Certain], so today's 21.9% is a cyclical reading, not a floor [Likely]. The Direction change on ROIC (27.0% to 21.9% in 12 months, 5.1pp below its 2-year high) shows the recovery in returns has already rolled over even as margins rose [Certain]; if it reflects pricing pressure rather than a capital-base effect, the margin gains will follow it down [Guessing]. The discount to the 5y multiple range is flattered by the 2021 peak [Likely], P/FCF sits above peers [Certain], and the DCF alone (56.87 HKD) is below the price, with the fair value flagged unreliable [Certain]. Segment and geographic mix are unverified, and China policy risk was not checked in the overlay [Certain].
## Bull case
The business is in a cyclical recovery with the balance sheet intact: net cash (net debt/EBITDA -2.25x), Piotroski 7, Altman Z 3.87 [Certain]. Over the last 12 months operating margin rose from 7.1% to 8.5%, FCF margin from 3.1% to 9.0% and ROCE from 8.9% to 12.4%, all at 2-year highs, so the 5-year "falling" reads are the FY2021 peak-to-FY2023 trough, not a broken model [Certain]. H1 2026 revenue and profit grew despite industry headwinds, with vehicle, pan-IoT and XR diversifying away from handsets [Likely]. Every multiple sits below its 5-year minimum (P/E 12.3x vs median 37.3x, EV/EBITDA 7.1x vs 18.7x) and below peers on P/E and EV/EBITDA [Certain]; the price implies 8.7% year-1 growth, roughly what H1 delivered [Likely]. Shares are not being diluted [Certain].
## Decision
```json
{
 "ticker": "HKG:2382",
 "decision": "AVOID",
 "position_type": "CORE",
 "conviction": 3,
 "scorecard": {
  "decline_cause": "temporary",
  "decline_evidence": "The 5-year declines run from the FY2021 peak to the FY2023 cyclical trough (ROIC 5.5%) with net cash intact (net debt/EBITDA -2.25x [RA]); over the last 12 months operating margin, FCF margin and ROCE are rising to 2-year highs [IS-T, CF-T, RA-T]. Only TTM ROIC fell, while ROCE rose, consistent with a capital-base effect rather than lost share.",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "Handset optics pricing and volume: a downturn in the handset cycle or price competition compresses the thin 19.5% gross margin [IS] and returns, as in FY2023.",
  "veto": null
 },
 "thesis": "A net-cash optics leader in a cyclical recovery, with operating and FCF margins at 2-year highs, trades below its own 5-year minimum on every multiple and below peers on P/E and EV/EBITDA, pricing growth no faster than H1 2026 delivered.",
 "rationale": "The scorecard sets conviction 4: high returns, net cash, a temporary explained decline and own-history cheapness outweigh a narrow moat, the ROIC roll-over and an unreliable fair value. Python sizes it (volatility-scaled). It breaches the China/HK and Technology caps, so it replaces JKHY, the weakest technology holding. [Second opinion: conviction 3; a  BUY needs both evaluations at 4+.]",
 "price_at_decision": 64.05,
 "price_date": "2026-11-06",
 "research_note": "research/HKG-2382/2026-11-09.md",
 "triggers": [
  {
   "text": "TTM operating margin falls below 6%, back to the FY2024 level of 5.9%, showing the margin recovery has reversed.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 6
   }
  },
  {
   "text": "TTM ROIC falls below 15%, extending the drop from 27.0% into a renewed cyclical downturn.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 15
   }
  },
  {
   "text": "TTM FCF margin falls below 4%, near the FY2024 level of 3.6%, showing the cash recovery was transitory.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 4
   }
  },
  {
   "text": "Net debt/EBITDA on the ratios page rises above 0x, i.e. the net cash balance is lost."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 100.0,
   "basis": "Margin and FCF recovery continues with vehicle/XR diversification [IS-T, CF-T, note section 2] and multiples move toward the low end of their 5y range [RA], between the base and bull fair value of 85.50-113.33 [valuation file]."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 75.0,
   "basis": "Growth near the 8.7% the reverse DCF implies with stable margins; a partial re-rating below the 85.50 blended base because the DCF (56.87) and EV/EBITDA (142.75) disagree and the fair value is flagged unreliable [fact sheet Fair value]."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 45.0,
   "basis": "A handset downturn repeats the FY2023 margin collapse (operating margin 1.8% [IS]); the price falls below the DCF base of 56.87 but stays above the 31.38 bear fair value given net cash [BS, RA]."
  }
 },
 "replaces": "JKHY",
 "replacement_reason": "Adding this name breaches the 30% Technology cap and the 25% China/HK cap. JKHY is the weakest technology holding: conviction 3, already being trimmed, and its own thesis says the price now implies growth above what has been delivered. Sunny is conviction 4 and trades below its 5-year minimum on every multiple.",
 "second_opinion": {
  "file": "research/HKG-2382/2026-11-09-evaluation-2.md",
  "conviction": 3
 },
 "entry_price": null,
 "entry_basis": "Second opinion at conviction 3: no entry price set."
}
```

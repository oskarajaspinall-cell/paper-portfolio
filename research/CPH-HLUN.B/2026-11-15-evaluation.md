# Evaluation: H. Lundbeck A/S (CPH:HLUN.B) — 2026-11-15
## Bear case
The re-rating has largely happened: P/E 14.3x and EV/EBITDA 7.6x both sit above their 5y max, the price is +37.7% above its 200-day average and RSI is 73.6 [Certain]. An extended price risks a de-rating back toward the 5y median P/E of 13.1x if Vyepti growth slows [Likely]. The moat is patent-based, not structural: value depends on Vyepti exclusivity and an unproven Parkinson's/MSA pipeline whose rNPV is [data unavailable] [Likely]. Direction change: ROIC is 3.7pp and FCF margin 3.8pp below their September 2024 highs; ROIC and operating margin are flat over the last year, so the FY trend overstates momentum [Certain]. The cause looks temporary (FY2024 leverage-funded investment, since repaid to 0.61x) rather than structural [Likely]. US drug-pricing policy could hit the likely US-heavy mix, unverified [Guessing]. Mechanical fair value is unreliable (methods disagree 2.6x) [Certain].
## Bull case
A good business that is working: Q3 beat and raised full-year guidance, led by Vyepti, with nine-month revenue up across all regions [Certain] (https://www.prnewswire.com/news-releases/lundbeck-raises-financial-guidance-for-2026-302934778.html). Operating margin rose from 13.8% (FY2021) to 24.4% TTM, gross margin 81.2%, FCF margin 20.3% and up 8.5pp in the last year [Certain]. Balance sheet is sound at 0.61x net debt/EBITDA, down from 2.00x [Certain]. Despite the re-rating it is cheap against peers (P/E 60% below the peer median) and yields 9.10% FCF; the reverse DCF implies -0.5% year-1 revenue growth, undemanding against raised guidance [Likely]. The trend is healthy (50-day 12.4% above the 200-day, 12-month change +33.9%) without being severely overextended [Certain]. Low beta of 0.19 adds diversification [Certain].
## Decision
```json
{
  "ticker": "CPH:HLUN.B",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "No metric falls over 1 or 3 years (ROIC +0.4pp 1y, operating margin +0.4pp 1y, FCF margin +8.5pp 1y [RA-T, IS-T, CF-T]); the gap to the September 2024 highs follows FY2024 leverage-funded investment, since repaid to 0.61x [BS,IS].", "moat": "narrow", "key_risk": "medium", "key_risk_text": "De-rating from above-5y-max multiples if Vyepti growth slows, or US pricing pressure on branded neuroscience drugs.", "veto": null},
  "thesis": "A specialty neuroscience pharma with rising margins, strong cash conversion and raised guidance, trading cheaply against peers but above its own 5y multiple range.",
  "rationale": "Scorecard gives conviction 3: balance sheet and trend are strong, but ROIC is only mid-teens, the moat is patent-based and multiples already sit above their 5y range with no reliable fair-value discount. Good but not compelling, so AVOID; the entry price at a margin of safety to base fair value would revisit it.",
  "price_at_decision": 59.35,
  "price_date": "2026-11-13",
  "research_note": "research/CPH-HLUN.B/2026-11-15.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 20%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA rises above 2.0x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "FCF margin (TTM) falls below 12%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "Vyepti growth stalls or full-year guidance is cut at a later report (company release)"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 88.89, "basis": "Vyepti keeps growing on raised guidance and the DCF-led bull fair value 88.89 is reached [IS,CF,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 64.65, "basis": "Growth continues at the guided pace and the stock holds near the blended base fair value 64.65, with multiples staying above their 5y range [RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 38.25, "basis": "Vyepti slows and P/E de-rates toward its 5y median 13.1x, in line with the bear fair value 38.25 [RA]."}
  },
  "entry_price": 51.72,
  "entry_basis": "valuation file: base 64.65 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

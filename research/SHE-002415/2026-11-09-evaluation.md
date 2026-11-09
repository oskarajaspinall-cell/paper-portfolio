# Evaluation: Hangzhou Hikvision Digital Technology Co., Ltd. (SHE:002415) — 2026-11-09
## Bear case
The 12-month rebound may be a peak, not a new level: ROIC 31.3% and operating margin 21.2% TTM sit at the 2-year high, while the five fiscal years fell from ROIC 52.3% [Certain]. If margins revert toward FY2025's 16.9%, the low P/E of 17.9x is flattering peak earnings [Likely]. FCF margin fell to 16.0% from 21.4% a year earlier; FY2025's 153.0% cash conversion looks like a working-capital release that has unwound [Likely]. Market access keeps shrinking: reported US FCC import restrictions and India's certification refusal (headlines in the fact sheet) cap overseas growth, and the overseas revenue share is unverified [Likely]. The DCF base of 20.74 CNY sits well below the 35.25 close, and the price implies 19.0% year-1 revenue growth, demanding for a hardware maker facing bans [Certain]. The multiples have been cheap for five years; the discount may simply be the permanent sanctions price [Guessing].
## Bull case
Hikvision is a net-cash compounder (net debt/EBITDA -1.37x, Piotroski 7, Altman Z 6.19) that has kept ROIC above 20% through every year of sanctions [Certain]. The last year shows a broad recovery: gross margin 48.6% is the highest in the table and operating margin rose 5.6pp, which suggests mix and cost discipline rather than a one-off [Likely]. P/E 17.9x and EV/EBITDA 12.8x are below their 5y minimums and about half the peer medians [Certain]. FCF yield 5.01% with 90.4% conversion and a falling share count [Certain]. If P/E simply returns to its 5y median of 23.7x on TTM earnings, the stock re-rates materially [Likely]. Beta 0.31 makes it a low-correlation diversifier [Certain].
## Decision
```json
{
  "ticker": "SHE:002415",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only FCF margin is falling over the last year (21.4% -> 16.0% TTM [CF-T,IS-T]); FY2025 conversion of 153.0% was unusually high and TTM conversion of 90.4% is normal, while ROIC and operating margin rose and the balance sheet stays net cash (-1.37x [BS,IS]): a working-capital normalisation, not a broken model.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Further market-access loss (US FCC import restrictions, India certification refusal, per fact-sheet headlines) erodes overseas sales and pushes margins back toward the FY2024 14.7% level; overseas share unverified.",
    "veto": null
  },
  "thesis": "A net-cash, high-ROIC surveillance hardware leader trading below its own 5-year multiple range, held back by sanctions and doubts over whether the 12-month margin rebound lasts.",
  "rationale": "Cheap on own-history multiples with a strong balance sheet, but the fair value is unreliable (DCF base well below the price), the margin rebound is unproven at a 2-year high, and market-access risk is unquantified. Good but not compelling: AVOID, per the scorecard.",
  "price_at_decision": 35.25,
  "price_date": "2026-11-06",
  "research_note": "research/SHE-002415/2026-11-09.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 15%: the rebound has reversed", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "ROIC (TTM) falls below 20%: returns break their sanction-era floor", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Gross margin (TTM) falls below 42%: price competition is winning", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 42}},
    {"text": "FCF margin (TTM) falls below 9%: cash conversion breaks down", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 9}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 46.7, "basis": "Margins hold near the 21.2% TTM level [IS-T] and P/E returns to its 5y median 23.7x [RA] on TTM earnings, close to the EV/EBITDA method's base of 51.45 [valuation file]."},
    "base": {"probability": 0.45, "target_price_12m": 35.5, "basis": "Earnings hold and the P/E stays near 17.9x, below its 5y minimum of 19.3x [RA], as the sanctions discount persists; above the unreliable blended base of 30.98 because the DCF leg understates a business with ROIC 31.3% [RA-T]."},
    "bear": {"probability": 0.3, "target_price_12m": 24.0, "basis": "Further market-access loss (FCC/India headlines [OV]) pushes operating margin back toward FY2025's 16.9% [IS] at a depressed multiple, between the blended bear 19.90 and the DCF base 20.74-to-blended base 30.98 range [valuation file]."}
  },
  "entry_price": 24.78,
  "entry_basis": "valuation file: base 30.98 x 0.8 (default margin of safety; the fair value is flagged unreliable, so a hit triggers a full re-check)",
  "replaces": null,
  "replacement_reason": null
}
```

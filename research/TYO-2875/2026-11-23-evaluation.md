# Evaluation: Toyo Suisan Kaisha, Ltd. (TYO:2875) — 2026-11-23
## Bear case
The return step-up may be cyclical, not structural: ROIC went from 11.4% in FY2022 to 24.4% TTM and gross margin from 25.0% to 31.3% [Certain], and the note itself says part may be input-cost relief [Guessing]. If commodity or freight costs turn, margins can revert toward FY2023 levels and today's P/E of 13.7x is a multiple on peak earnings [Likely]. Last-year ROIC is only flat (+0.6pp) and below its 2-year high of 25.6% [Certain]. FCF conversion fell to 61.7% in FY2026 before recovering to 86.1% TTM, so cash quality needs confirming [Certain]. The overseas (North America) profit pool and its revenue share are unquantified, leaving yen and US tariff/competition risk unsized [Likely]. There is no trend support: the price is 2.6% below its 200-day average with a 12-month change of -2.0% [Certain], and Q2 results content is unread [Certain].
## Bull case
A net-cash staples franchise (net debt/EBITDA -2.22x, Altman Z 9.38, Piotroski 7) with ROIC 24.4% and operating margin 16.6% at its 2-year high [Certain]. The last 12 months show ROCE, operating margin and FCF margin all rising, FCF margin to 11.5% from 6.1% a year earlier [Certain], so there is no direction-change warning. Yet P/E 13.7x and P/FCF 15.5x sit below their own 5-year minimums, EV/EBITDA at the bottom of its range, and every multiple below the peer median [Certain]. The reverse DCF implies roughly zero revenue growth [Likely]. Buybacks shrank the share count 2.66% YoY and the FCF yield is 6.43% [Certain]. Mechanical base fair value 12,711.88 JPY sits above the 10,450.00 close [Certain]. Beta 0.25 makes it a low-correlation defensive [Certain].
## Decision
```json
{
  "ticker": "TYO:2875",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python-listed trends: ROIC, operating margin and FCF margin are flat or rising over the last 1 and 3 years [RA-T, IS-T, CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Margins and ROIC partly reflect input-cost relief and could revert toward FY2023 levels if commodity costs rise, turning a low P/E into a peak-earnings multiple.",
    "veto": null
  },
  "thesis": "A net-cash, high-ROIC Japanese noodle and food maker with rising rolling margins trades below its own 5-year minimum P/E and P/FCF and well below peers, pricing no growth.",
  "rationale": "Fundamentals have improved since purchase: rolling operating and FCF margins rose and multiples sit at or below their own 5-year lows. The margin-reversion risk is real but the net-cash balance sheet cushions it. Held at its current size; cash above the floor is too small for a meaningful ADD.",
  "price_at_decision": 10450.00,
  "price_date": "2026-11-20",
  "research_note": "research/TYO-2875/2026-11-23.md",
  "entry_price": null,
  "entry_basis": "The scorecard already gives conviction 4 at today's price, so price is not the obstacle; the position is held at its size and a lower price would not change the decision.",
  "triggers": [
    {"text": "TTM ROIC falls below 18%, giving up most of the rise from 11.4% in FY2022 to 24.4%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "TTM operating margin falls below 13%, back under the FY2024 level of 13.6%, showing the margin gains were input-cost relief.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 13}},
    {"text": "TTM gross margin falls below 28%, under the FY2024 level of 28.7%, signalling lost pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 28}},
    {"text": "TTM FCF margin falls below 6%, back to the level of a year earlier, showing the cash recovery was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 14188.39, "basis": "Margins hold and the multiple returns toward its 5y median P/E of 17.1x [RA], consistent with the mechanical bull fair value 14,188.39 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 12711.88, "basis": "Earnings stay near TTM levels and the P/E moves off its below-5y-minimum level toward history, in line with the mechanical base fair value 12,711.88 [IS,BS,CF,RA,ST,HI]."},
    "bear": {"probability": 0.25, "target_price_12m": 8275.59, "basis": "Input-cost relief reverses and margins revert toward FY2023 levels (operating margin 9.2% [IS]), matching the mechanical bear fair value 8,275.59 [IS,BS,CF,RA,ST,HI]."}
  }
}
```

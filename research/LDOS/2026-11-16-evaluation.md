# Evaluation: Leidos Holdings, Inc. (LDOS) — 2026-11-16
## Bear case
The market prices a shrinking business: the reverse DCF implies -11.0% year-1 revenue growth [Certain]. That may be right. FY26 revenue guidance was cut after the SES sale, and the call flags VBA uncertainty weighing on 2027 earnings growth [Likely]. ROIC fell from 16.6% to 15.2% and ROCE from 19.3% to 17.1% over the last 12 months, both below their January 2026 highs [Certain]. The Direction change is mostly the larger capital base after the Entrust deal, but completed higher-margin contracts also weighed [Likely]. Net debt/EBITDA rose to 2.46x from 1.77x, and debt-funded Entrust adds integration risk [Certain]. About 83% of revenue is U.S. government [company-reported], and funding runs only to 11 December 2026 under a continuing resolution, so a shutdown could hit cash and bookings [Certain]. The stock is 5.5% below its 200-day average and down 32.0% in 12 months: no trend support [Certain].
## Bull case
The returns gains are real: ROIC went from 9.9% (FY2021) to 15.2% TTM and operating margin from 8.5% to 11.8%, with the latter flat over the last year [Certain]. FCF margin rose 3.0pp in a year to 11.0%, so cash generation is improving, not falling [Certain]. Q3 beat on EPS and full-year EPS guidance was raised for the third consecutive quarter [Certain]. Yet the stock trades below its own 5-year minimum on P/E (11.7x), EV/EBITDA (9.1x) and P/FCF (8.2x), and below peers on each, at a 12.27% FCF yield [Certain]. Buybacks cut the share count 3.42% YoY [Certain]. The EV/EBITDA method alone gives 166.47 to 178.85, well above the price, even before the DCF [Certain]. Clearances and recompete incumbency make revenue sticky [Likely]. Beta is 0.55 [Certain]. The fall in returns looks like an acquisition denominator effect, not lost share [Likely].
## Decision
```json
{
  "ticker": "LDOS",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and ROCE fell over the last 12 months while operating margin is flat and FCF margin rose 3.0pp [IS-T, CF-T]; the fall tracks the larger post-Entrust capital base and debt, and Q3 operating income rose on program wins (10-Q https://www.sec.gov/Archives/edgar/data/1336920/000133692026000293/ldos-20261002.htm).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "U.S. federal funding (continuing resolution to 11 December 2026) and VBA uncertainty cut 2027 earnings growth, turning the implied revenue decline into reality.",
    "veto": null
  },
  "thesis": "A government-IT incumbent with ROIC well above its FY2021-23 levels and an 11.0% FCF margin trades below its own 5-year minimum on every earnings multiple and below peers, where the price implies a -11.0% revenue decline that raised EPS guidance does not show.",
  "rationale": "Evidence matches the 2026-11-08 HOLD 4: fundamentals intact, ROIC dip explained by the Entrust capital base, cash generation rising, multiples below their own 5-year minimum. Held at its existing target size; no ADD as the position is at size and funding/VBA risk is live.",
  "price_at_decision": 130.53,
  "price_date": "2026-11-13",
  "research_note": "research/LDOS/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 10.5%, reversing most of the five-year expansion from 8.5% to 11.8% and showing contract completions are not being replaced at similar margins.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10.5}},
    {"text": "TTM ROIC falls below 13%, showing the decline from 16.6% is no longer an acquisition denominator effect but deteriorating returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 13}},
    {"text": "TTM FCF margin falls below 8%, back to the level of a year earlier, showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "Net debt/EBITDA on the ratios page rises above 3.0x (2.46x TTM now) without a visible deleveraging path from the Entrust debt."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 178.85, "basis": "Funding resolves and EPS guidance keeps rising, so EV/EBITDA re-rates toward its 5y median 11.9x [RA], matching the EV/EBITDA base fair value 178.85 (fact sheet Fair value); the DCF bull is not used as it assumes growth the guidance cut does not support."},
    "base": {"probability": 0.5, "target_price_12m": 166.47, "basis": "EV/EBITDA returns toward its 5y minimum 11.2x [RA] on TTM EBITDA [IS] as the SES divestiture and Entrust settle, the EV/EBITDA bear value 166.47; below the 259.21 blended base because the DCF leg extrapolates growth the cut revenue guidance does not show."},
    "bear": {"probability": 0.25, "target_price_12m": 112.07, "basis": "A shutdown after the 11 December 2026 continuing resolution [company-reported, 10-Q] plus VBA pressure on 2027 earnings keeps multiples at today's 9.1x EV/EBITDA [RA] and the price revisits its October swing low 112.07 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is already 4 (a HOLD at the buy bar, position at size); no lower entry price is needed to justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

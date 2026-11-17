# Evaluation: Gedeon Richter PLC (BUD:RICHTER) — 2026-11-17
## Bear case
The price has already run: up 40.9% over 12 months, 11.0% above its 200-day average and at its 52-week high of 13,860.00 [Certain]. P/E (64%), EV/Sales (83%) and P/B (96%) sit high in their own 5-year ranges, so a growth slowdown could de-rate the stock even as cash multiples look cheap [Likely]. Gross margin of 67.8% is unusually high for a generics-exposed group and may be a mix peak [Guessing]. The direction change is real: TTM FCF margin fell from 29.3% to 26.8% while operating margin rose, so cash is lagging profit [Certain]; the cause is not disclosed in our inputs [Certain]. Regional mix is [data unavailable] and the company's own site was blocked, so CIS/EU country exposure and HUF translation risk (Q1 2026 cited currency headwinds) cannot be checked [Likely]. The Q3 2026 release was not read [Certain].
## Bull case
Returns and margins are rising on every horizon: TTM ROIC 22.5% (17.4% a year earlier), operating margin 34.5% (28.7% a year earlier), both at 2-year highs [Certain]. The FCF-margin dip leaves it at 26.8%, still far above FY2021's 14.9%, with FCF conversion at 103.6% of net income, which points to timing rather than a broken model [Likely]. The balance sheet is net cash (-0.61x net debt/EBITDA), Altman Z 6.64 [Certain]. On cash multiples it is cheap: a 10.11% FCF yield, P/FCF 9.9x in the 12th percentile of its range and EV/EBITDA 5.8x below its 5-year median 6.4x and 28% under peers [Certain]. The reverse DCF prices -5.1% year-1 revenue growth against a 2026 outlook of high single-digit growth from the Q4 2025 call [Likely]. Beta 0.31 adds a low-correlation exposure [Certain].
## Decision
```json
{
  "ticker": "BUD:RICHTER",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "new_evidence": {"type": "method_change", "text": "The scorecard rule changed after the 2026-11-15 AVOID 3 (strength_at_value_points, 2026-11-17): two trend-strength points now count as three when the value blend is at or above the price, and the earlier evaluation re-scores across the buy line."},
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "Only TTM FCF margin is falling (29.3% to 26.8%) while TTM operating margin rose from 28.7% to 34.5% and FCF conversion is 103.6% of net income [IS-T, CF-T, CF, IS]: cash lagging rising profit with net cash intact reads as working-capital or investment timing, not lost share or a price cap.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "A de-rating if growth slows after a 40.9% 12-month run with P/E high in its own range, compounded by a possible gross-margin mix peak and unverified regional/HUF exposure.", "veto": null},
  "thesis": "A net-cash pharma with rising ROIC and operating margin trades at a 10.11% FCF yield and below its own median EV/EBITDA, pricing a revenue decline its outlook does not show.",
  "rationale": "Scorecard gives conviction 4: high and rising returns, net cash, a cheap cash yield and a healthy uptrend; the FCF-margin dip looks like timing. Python sets the volatility-scaled core size; cash after the pending order cannot fund it above the 1.5% floor, so a conviction-3 holding funds it.",
  "price_at_decision": 13700.00,
  "price_date": "2026-11-16",
  "research_note": "research/BUD-RICHTER/2026-11-17.md",
  "triggers": [
    {"text": "TTM operating margin falls below 28%, giving up the step-up from 28.7% a year earlier to 34.5%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "TTM ROIC falls below 16%, back under the FY2021 level of 16.0%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 16}},
    {"text": "TTM FCF margin falls below 18%, showing the current slide is structural rather than timing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 18}},
    {"text": "Net debt/EBITDA rises above 1.0x, signalling a debt-funded deal that ends the net cash position.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 18245.16, "basis": "Rising margins are sustained and the stock reaches the mechanical blended base fair value of 18,245.16 [fact sheet Fair value], consistent with the reverse DCF's -5.1% implied growth being too pessimistic."},
    "base": {"probability": 0.5, "target_price_12m": 14574.46, "basis": "EV/EBITDA moves back toward its 5y median 6.4x [RA] on TTM EBITDA, the EV/EBITDA base of 14,574.46; below the DCF base because P/E and P/B already sit high in their own ranges."},
    "bear": {"probability": 0.25, "target_price_12m": 11141.92, "basis": "Growth slows and the gross margin proves a mix peak, de-rating to the EV/EBITDA bear of 11,141.92 [fact sheet Fair value]; the DCF bear of 5,351.49 is not used because it ignores the net cash and 10.11% FCF yield [ST]."}
  },
  "replaces": "OTIS",
  "replacement_reason": "OTIS is held at conviction 3 with, by its own thesis, a balanced rather than compelling skew: price above its mechanical fair value, falling operating margin and rising leverage. Richter clears the buy bar with rising margins, net cash and a value blend above the price."
}
```

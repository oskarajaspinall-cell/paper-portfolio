# Evaluation: TAL Education Group (TAL) — 2026-10-25
## Bear case
The quality is one good year, not a record: ROIC was negative or near zero in four of five fiscal years before 30.5% in FY2026 [RA] [Certain]. TTM net margin of 28.4% far exceeds the 12.5% operating margin, so P/E 6.3x flatters on non-operating gains that are unlikely to recur [Likely]. FCF conversion is falling (70.4% TTM) [CF,IS] [Certain]. The business was rebuilt after the 2021 tutoring clampdown and stays policy-dependent, with no evident moat in a fragmented market [Likely]. The stock fell sharply on 2026-10-21 for an unexplained reason, is 14.5% below its 50-day average with RSI 25.6, and Q2 FY2027 results land on Oct 29, 2026 [ST,HI] [Certain]; buying four days before an unexplained-drop print is a coin toss [Guessing]. Beta 0.09 understates China regulatory and US-listing risk [Likely].
## Bull case
On cleaner reads TAL is cheap: EV/EBITDA 6.6x and P/FCF 8.8x sit below their own 5y minimums of 9.0x and 12.6x, at an 11.32% FCF yield [RA,ST] [Certain]. The balance sheet is net cash (net debt/EBITDA -5.13x) [BS,IS] [Certain], and shares fell 8.26% YoY on buybacks [ST] [Likely]. Margins have risen for five years: gross 56.0%, operating 12.5%, FCF 20.0% TTM [IS,CF] [Certain]. The reverse DCF prices a 21.2% revenue fall in year 1, against Q1 FY2027 commentary of strong revenue and profit growth [OV] [Likely]. Insiders own 34.69%, aligning management with capital returns [ST] [Likely]. If the turnaround margins hold, the mechanical base fair value of 23.92 is well above the price [FV] [Guessing].
## Decision
```json
{
  "ticker": "TAL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 20%-FCF-margin China learning-services turnaround trades below its own 5-year minimum EV/EBITDA and P/FCF, but one profitable year after four weak ones, non-operating-inflated earnings and policy risk do not yet make the cheapness a durable-quality bargain.",
  "rationale": "Cheap on FCF with net cash and buybacks, but the operating record is one year deep, net income is flattered by non-operating gains, China education policy is an unpriced-in-beta risk, and results arrive in four days after an unexplained drop. Good but not compelling: conviction 3, no position.",
  "price_at_decision": 10.17,
  "price_date": "2026-10-23",
  "research_note": "research/TAL/2026-10-25.md",
  "triggers": [
    {"text": "TTM operating margin falls below 6%, giving back about half of the turnaround from -0.1% (FY2025) to 12.5% TTM.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 6}},
    {"text": "TTM gross margin falls below 50%, near the FY2022 low of 49.8%, signalling pricing pressure in learning services or devices.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 50}},
    {"text": "TTM FCF margin falls below 10%, under the FY2024-FY2025 levels of 13.0%/12.7%, showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "A new PRC education regulation restricts TAL's learning-services or devices business, as disclosed in a 20-F/6-K or company release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 18.28, "basis": "Turnaround margins hold through Q2 FY2027 and EV/EBITDA re-rates to the mechanical base EV/EBITDA value of 18.28 [FV], still below the DCF base 26.74 because the 5y record does not support extrapolating peak margins for ten years."},
    "base": {"probability": 0.45, "target_price_12m": 14.56, "basis": "P/FCF recovers to its 5y minimum of 12.6x [RA] on TTM FCF (8.8x now) as buybacks continue; below the blended base fair value 23.92 because the DCF extrapolates a one-year turnaround from a weak 5y ROIC record [RA]."},
    "bear": {"probability": 0.3, "target_price_12m": 6.93, "basis": "Non-operating gains fade and policy or results disappoint, leaving the mechanical bear EV/EBITDA value of 6.93 [FV]; the negative DCF bear (-16.88) ignores the net cash (net debt/EBITDA -5.13x [BS,IS]) and is not used."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the default (base 23.92 x 0.8) is already above the price. The obstacle is evidence that operating profitability is durable beyond one year and the Oct 29, 2026 results after an unexplained drop; a lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

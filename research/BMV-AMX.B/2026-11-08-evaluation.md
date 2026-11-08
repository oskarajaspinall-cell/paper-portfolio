# Evaluation: América Móvil (BMV:AMX.B) — 2026-11-08
## Bear case
The base fair value of 40.00 MXN rests almost entirely on the DCF (49.06), which assumes the TTM FCF margin of 18.4%, a five-year high, persists; it was 9.4% in FY2022 [Certain]. The own-history EV/EBITDA method gives 21.89, below the 23.95 close, and the current 5.8x sits next to its 5y median of 5.9x: the "discount" is permanent, not a mispricing [Likely]. P/E of 15.8x is above peers and P/B of 3.1x is at the top of its range [Certain]. Net margin of 9.4% shows heavy below-the-line financing/FX costs; Altman Z is 1.77 [Certain]. A controlling family holds 21.09%, the country revenue mix is unconfirmed and Brazil/Mexico politics are unverified (macro overlay) [Likely]. Operating margin sits below its 2-year high of 20.8% and management flagged Mexico price competition [Likely]. After a 16.2% three-month run with RSI 75.0, entry is stretched [Certain].
## Bull case
The price implies revenue shrinking 9.8% in year 1, while Q3 revenue grew 7.6% (transcript headline) [Likely]. FCF yield is 12.54% and EV/EBITDA is 17% below peers [Certain]. Every rolling-12-month metric improved: ROIC +2.4pp to 11.7%, ROCE +1.2pp, FCF margin +1.4pp [Certain]. Net debt/EBITDA fell from 2.38x to 1.90x, so cash flow increasingly accrues to equity [Certain]. Beta 0.13 makes it a low-correlation defensive compounder, with capex held flat per the May 2026 outlook [Likely]. If FCF margin holds, the DCF value is reachable over time [Guessing].
## Decision
```json
{
  "ticker": "BMV:AMX.B",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cash-generative, deleveraging LatAm telecom whose upside depends on a peak FCF margin persisting while its own-history EV/EBITDA value sits below the price.",
  "rationale": "Improving returns and a high FCF yield are real, but the market has always priced AMX near 5.9x EV/EBITDA, the second method values it below the price, FCF margin is at a five-year high, and the stock just ran hard. Good but not compelling: conviction 3, no position.",
  "price_at_decision": 23.95,
  "price_date": "2026-11-06",
  "research_note": "research/BMV-AMX.B/2026-11-08.md",
  "triggers": [
    {"text": "TTM FCF margin falls below 14% (cash-flow-statement trailing page)", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "TTM ROIC falls below 9% (ratios trailing page)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "Net debt/EBITDA rises above 2.4x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.4}},
    {"text": "TTM operating margin falls below 17.5%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 29.0, "basis": "EV/EBITDA moves toward the 7.0x peer median [RA] on TTM EBITDA as ROIC and FCF margin keep rising [RA-T,CF-T] and leverage falls, short of the DCF 49.06 because the stock has never traded near it."},
    "base": {"probability": 0.5, "target_price_12m": 25.0, "basis": "EV/EBITDA stays near its 5.9x 5y median [RA] while modest EBITDA growth and deleveraging from 1.90x [RA] add equity value; sits between the EV/EBITDA value 21.89 and well below the DCF-led base 40.00 because the DCF assumes a peak FCF margin persists."},
    "bear": {"probability": 0.25, "target_price_12m": 18.72, "basis": "Mexico price competition (Q3 transcript [OV]) pushes operating margin back toward 17.6% [IS] and EV/EBITDA to its 5.6x 5y low [RA], matching the mechanical bear fair value 18.72."}
  },
  "entry_price": 20.55,
  "entry_basis": "Back at the 50-day average 20.55 [ST,HI], the pre-results level, the price would sit below the own-history EV/EBITDA value 21.89 as well as the DCF, so both methods would show upside; the default base 40.00 x 0.8 is above the price and unusable.",
  "replaces": null,
  "replacement_reason": null
}
```

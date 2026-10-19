# Evaluation: Amadeus IT Group, S.A. (BME:AMS) — 2026-10-19
## Bear case
The market is pricing structural disintermediation, not a Middle East blip: AI agents and airline direct channels could route bookings around the GDS, and the 12-month fall of -19.9% with relative strength of -34.7pp vs SPY says investors believe it [Guessing]. Air Distribution already lagged Air IT and Hospitality in H1 2026, and management widened the FY2026 guidance range on the Q2 call [Likely]. Pending IPS and IDEMIA acquisitions add integration risk outside the historicals and could lift leverage from 1.06x net debt/EBITDA [Likely]. On peers it is not cheap: P/E 18.0x vs a 13.7x peer median and P/FCF 10.7x vs 7.8x [Certain]. If the multiple simply stays below its 5y floor while bookings stagnate, there is no re-rating and the shares could retest the 52-week low of 46.21 [Guessing].

## Bull case
A two-sided travel-distribution and airline-IT oligopoly with ROIC of 19.0%, operating margin 27.5% and FCF margin 32.5% TTM, all on rising 5y trends [Certain]. Every earnings multiple sits below its own 5y minimum (EV/EBITDA 10.1x vs 12.1x min, P/FCF 10.7x vs 12.8x) at a 9.38% FCF yield [Certain], and the reverse DCF implies -4.6% year-1 revenue decline against reported H1 constant-currency growth of 5% [Likely]. Shares fell -3.96% YoY on buybacks funded from free cash flow [Certain]. Balance sheet is sound: Altman Z 3.81, Piotroski F 7, beta 0.66 [Certain]. Even the mechanical bear fair value of 62.04 is above the price [Certain]; macro is context only (low beta, company-specific discount) [Likely].

## Decision
```json
{
  "ticker": "BME:AMS",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A 19%-ROIC, 32.5%-FCF-margin travel-IT oligopolist trades below its own 5-year minimum on every earnings multiple at a 9.38% FCF yield, where the price implies a revenue decline that its reported growth and guidance do not show.",
  "rationale": "Rising quality, a 9.38% FCF yield funding buybacks, and a price below even the mechanical bear value give a favourable skew. AI/direct-booking disintermediation risk, the peer P/E premium and pending acquisitions cap conviction at 4, not 5: standard volatility-scaled core size. Holdings stay well below 15.",
  "price_at_decision": 54.40,
  "price_date": "2026-10-16",
  "research_note": "research/BME-AMS/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, giving up most of the post-pandemic rise to 19.0% and signalling moat erosion rather than a cyclical dip.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM operating margin falls below 20%, under every year since FY2022 (21.1%), showing disintermediation is forcing price cuts.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 25%, under the 31.2%-33.8% band held since FY2022, showing cash generation can no longer fund buybacks and acquisitions.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}},
    {"text": "Air Distribution segment revenue in the earnings release declines year on year for two consecutive quarters, signalling structural bookings loss rather than one-off Middle East disruption."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 81.87, "basis": "Middle East disruption fades and EV/EBITDA re-rates toward its 5y median of 15.4x [RA], matching the EV/EBITDA method base value of 81.87; set below the DCF base of 100.14 because that assumes growth the AI-disintermediation debate makes uncertain."},
    "base": {"probability": 0.5, "target_price_12m": 63.34, "basis": "Constant-currency growth continues per the Q2 2026 call (https://stockanalysis.com/quote/bme/AMS/transcripts/550383-q2-2026/) and EV/EBITDA recovers only toward its 5y minimum of 12.1x [RA], close to the EV/EBITDA bear value of 63.34 and the blended bear fair value of 62.04."},
    "bear": {"probability": 0.25, "target_price_12m": 46.21, "basis": "Air Distribution keeps lagging and IPS/IDEMIA integration disappoints, so the multiple stays below its 5y floor and the shares retest the 52-week low of 46.21 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

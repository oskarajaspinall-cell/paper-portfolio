# Evaluation: Aon plc (AON) — 2026-10-08
## Bear case
Aon is buying USI for ~$17.0bn funded entirely with new debt on top of net debt/EBITDA already at 2.50x TTM [Certain]. Management itself guides EPS accretion only from 2028, so the deal dilutes earnings through 2027 [Certain], and buybacks, which cut shares 1.08% YoY, are suspended [Certain]. Cash quality is already slipping: FCF conversion fell from 162.9% to 83.0% TTM [Certain], and Altman Z is 1.67 [Certain]. The macro overlay flags 10y yields at 5.27% and widening HY spreads into the Q4 note pricing, raising the locked-in coupon [Likely]. The headline P/E discount (14.9x vs peers 20.3x) overstates cheapness: EV/EBITDA of 12.2x is in line with peers (12.4x), so the market is pricing the leverage, not mispricing the franchise [Likely]. Momentum is -24.8% over 3 months with Q3 results on Oct 30 before the deal closes [Certain].

## Bull case
The franchise is better than ever: operating margin 28.5% TTM (+10.0pp over 5y), ROIC 16.1% and gross margin 48.2% are all rising [Certain]. Every multiple sits below its own 5-year minimum, P/E 14.9x vs a 20.5x floor [Certain], and FCF yield is 5.66% [Certain]. Brokerage is asset-light with recurring, sticky client relationships among a narrow peer set [Likely]. The NFP integration gives Aon a template, and $395m of identified run-rate synergies support deleveraging [Likely]. Beta of 0.69 and an RSI of 28.4 suggest much of the integration fear is already priced [Guessing]. If financing is placed on reasonable terms and synergies land, a partial re-rating toward its own historic floor offers substantial upside over 12 months [Guessing].

## Decision
```json
{
  "ticker": "AON",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, margin-expanding insurance broker trades below its own 5-year multiple floor, but the all-debt USI deal, EPS dilution through 2027 and suspended buybacks explain most of the discount, since EV/EBITDA sits in line with peers.",
  "rationale": "Quality is real, but the cheapness is mostly leverage being priced: EV/EBITDA matches peers, the deal is dilutive through 2027, FCF conversion is falling and the macro overlay tilts moderately bear on financing costs. Good but not compelling; conviction 3 is below the buy threshold, so cash is preferred until financing terms and integration are visible.",
  "price_at_decision": 270.47,
  "price_date": "2026-10-07",
  "research_note": "research/AON/2026-10-08.md",
  "triggers": [
    {"text": "Net debt/EBITDA rises above 4.0x, showing post-USI deleveraging is off track (would confirm the bear case).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.0}},
    {"text": "TTM operating margin falls below 24%, showing pricing or integration-cost pressure on the franchise.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 24}},
    {"text": "TTM ROIC falls below 12%, showing returns are not sustained on the larger post-USI capital base.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "FCF conversion (FCF/NI, cash flow and income statement pages) recovers above 100% after the USI close, showing cash generation can fund deleveraging (would raise conviction)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 372, "basis": "Financing prices well and synergies track, so P/E re-rates from 14.9x to its 5y minimum 20.5x [RA]; probability cut from 0.25 by the overlay's moderate bear tilt (research/AON/2026-10-08-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 275, "basis": "EV/EBITDA holds near the 12.4x peer median vs 12.2x now [RA,P:MMC,P:WTW,P:AJG,P:BRO] as dilution through 2027 (note, sec.gov 8-K) offsets the 18.5% FCF margin [CF,IS]."},
    "bear": {"probability": 0.35, "target_price_12m": 230, "basis": "FCF margin slips to its 5y low 16.8% [CF,IS] with P/FCF de-rating below 17.7x [RA] as higher coupons on the ~$17.0bn USI debt slow deleveraging; probability raised from 0.25 per the macro overlay's moderate bear tilt (research/AON/2026-10-08-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

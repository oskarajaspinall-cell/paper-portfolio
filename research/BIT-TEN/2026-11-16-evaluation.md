# Evaluation: Tenaris S.A. (BIT:TEN) — 2026-11-16
## Bear case
The price already discounts a recovery that the fundamentals have not delivered yet. P/E of 16.1x and EV/EBITDA of 10.0x sit above their 5y maxima of 11.2x and 9.7x, and P/B of 1.9x is above its 1.5x max [Certain]. Meanwhile ROIC of 12.2% is 6.1pp below its 2-year high and operating margin of 18.2% is 3.3pp below its 21.5% high [Certain]. This is a cyclical tube maker coming off the FY2023 peak (ROIC 26.5%), not a compounder [Certain]. After a +55.4% 12-month run, a slower 2027 (tariff costs flagged for 2027 pricing, a partial Middle East recovery) would bring a de-rating back towards the 5y median multiples [Likely]. The base fair value of 25.64 EUR is below the 27.66 close, and the bear range is very wide [Certain]. The regional revenue mix is unknown, so the Iraq exposure cannot be sized [Certain].

## Bull case
A net-cash balance sheet (net debt/EBITDA -0.90x, Altman Z 6.52, Piotroski F 7) means the cycle is an earnings risk, not a solvency risk [Certain]. FCF conversion of 96.5% funds a buyback (shares -5.42% YoY) and a doubled interim dividend [Likely]. Q3 beat consensus and management guides to a higher Q4, with offshore supporting 2027 [Likely]. The last-year trend is flat to rising, not falling: FCF margin rose 1.7pp to 15.7% and ROCE was flat [Certain]; the 3-year decline is the normalisation from the FY2023 peak with the balance sheet intact, i.e. cyclical [Likely]. P/E is 36% below the peer median, the FCF yield is 6.01% and the stock trades above its 50-day and 200-day averages [Certain]. Scale and premium connections plausibly support above-commodity margins [Guessing].

## Decision
```json
{
  "ticker": "BIT:TEN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {"decline_cause": "temporary", "decline_evidence": "ROIC, operating and FCF margin are down over 3 years from the FY2023 cyclical peak (ROIC 26.5%) but flat to rising over the last year (FCF margin +1.7pp), with net cash intact (net debt/EBITDA -0.90x) [RA-T, CF-T, RA]; Q3 beat and a higher Q4 is guided (https://www.fool.com/earnings/call-transcripts/2026/11/05/tenaris-ts-q3-2026-earnings-call-transcript/).", "moat": "narrow", "key_risk": "medium", "key_risk_text": "A softer 2027 drilling cycle or unrecovered tariff costs compress margins while the multiples sit above their 5y maxima, causing a de-rating after the +55.4% run.", "veto": null},
  "thesis": "A net-cash, high-cash-conversion seamless-tube leader in a cyclical recovery, but priced above its own history on every earnings multiple.",
  "rationale": "Quality and balance sheet are solid and the cycle decline looks temporary, but P/E and EV/EBITDA sit above their 5y maxima and the base fair value is below the price, so there is no discount and no trend-strength credit. Good but not compelling: AVOID at scorecard conviction 2.",
  "price_at_decision": 27.66,
  "price_date": "2026-11-13",
  "research_note": "research/BIT-TEN/2026-11-16.md",
  "triggers": [
    {"text": "ROIC TTM falls below 10% (structural margin loss, not the cycle)", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Operating margin TTM falls below 15% (tariff costs not recovered in pricing)", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "FCF margin TTM falls below 10%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Net debt (debt less cash and short-term investments) turns positive on the balance sheet: the net cash position is gone"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 32.0, "basis": "Q4 volume and margin guidance is delivered and 2027 offshore demand holds, so the DCF base of 30.20 [IS,CF] is exceeded as margins move back towards the 21.5% 2-year high [IS-T]."},
    "base": {"probability": 0.5, "target_price_12m": 26.5, "basis": "Margins stay near the 18.2% TTM [IS-T] and the multiple drifts from above its 5y max towards the blended base fair value of 25.64 [valuation], offset by buybacks (shares -5.42% YoY [ST])."},
    "bear": {"probability": 0.25, "target_price_12m": 17.5, "basis": "A softer drilling cycle plus tariff costs (https://www.fool.com/earnings/call-transcripts/2026/11/05/tenaris-ts-q3-2026-earnings-call-transcript/) de-rate EV/EBITDA from 10.0x towards its 5.8x median [RA], near the EV/EBITDA fair value of 16.53; net cash limits the downside versus the mechanical bear of 3.44, which the DCF's negative bear case distorts."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

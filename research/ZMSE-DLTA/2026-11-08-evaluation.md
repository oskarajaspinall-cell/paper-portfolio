# Evaluation: Delta Corporation Limited (ZMSE:DLTA) — 2026-11-08
## Bear case
The price cannot be underwritten: P/E, EV/EBITDA, P/FCF, P/B, market cap and peer multiples are all [data unavailable] [ST], so there is no own-history or peer check [Certain]. The only anchor is a DCF on USD financials against a ZWG share price; its bear-to-bull range (12.47 to 113.52 ZWG) is too wide for a margin of safety [Certain]. The +123.5% 52-week rise likely reflects ZWG depreciation and inflation as much as value [Likely]. Returns are past their peak: TTM ROIC 42.8% is 2.7pp below a year earlier and 27.4pp below its 2-year high of 70.2%; ROCE is 18.5pp below that high [RA-T] [Certain]. The driver looks like gross margin sliding from 51.4% to 47.4% [IS] [Likely]; the USD restatement basis is unverified [Guessing]. Sole-country Zimbabwe risk (currency, capital controls, liquidity) is unverified by any official source [Likely]. Results due Nov 10, 2026 reset the TTM data.

## Bull case
On the numbers this is a superior franchise: TTM ROIC 42.8%, ROCE 51.7%, ROE 44.8% and operating margin 22.0% [RA,IS] [Certain]. The balance sheet is net cash (net debt/EBITDA -0.14x) and Piotroski F is 7 [ST] [Certain]. Cash quality is improving over the last year, not just on fiscal endpoints: FCF margin rose 3.9pp to 12.2% TTM and FCF conversion reached 77.5% [CF-T,IS-T] [Certain]; the ROIC decline is from an exceptional 70.2% peak to a level that remains very high [Likely]. Shares fell 1.39% year on year [ST] [Certain]. Scale in brewing and bottling in an import-constrained market is a plausible moat [Likely]. The reverse DCF implies -3.8% first-year revenue growth, and the mechanical base value of 58.21 ZWG is well above the 34.95 close [Certain], though that DCF's reliability is doubtful [Guessing].

## Decision
```json
{
  "ticker": "ZMSE:DLTA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "Delta's high-return, net-cash beverage franchise cannot be underwritten because valuation data are unavailable and its USD financials against a ZWG price in a sole-country Zimbabwe exposure make the DCF unreliable.",
  "rationale": "Quality is genuinely high, but there is no multiple, market cap or peer check, the only fair value mixes USD financials with a ZWG price, returns are below their 2-year highs and country risk is unverified. Evidence too thin and uncheckable for conviction 4; cash is acceptable.",
  "price_at_decision": 34.95,
  "price_date": "2026-11-05",
  "research_note": "research/ZMSE-DLTA/2026-11-08.md",
  "triggers": [
    {"text": "ROIC (ratios page, TTM) falls below 30%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "Operating margin (TTM) falls below 18%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18}},
    {"text": "FCF margin (TTM) falls below 8%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "Net debt/EBITDA turns positive above 1.0x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 58.21, "basis": "The mechanical DCF base value of 58.21 ZWG [IS,BS,CF,RA,ST] is realised as FCF margin keeps rising (12.2% TTM [CF-T]); capped at the DCF base rather than its 113.52 bull because the USD/ZWG mismatch makes the upper range unreliable."},
    "base": {"probability": 0.45, "target_price_12m": 34.95, "basis": "Below the DCF base because the USD-reported DCF cannot be validated against a ZWG price and no multiples exist [ST]; the price holds near the 34.95 close as ROIC stays high but off its 70.2% peak [RA-T]."},
    "bear": {"probability": 0.30, "target_price_12m": 12.47, "basis": "DCF bear value of 12.47 ZWG [IS,BS,CF,RA,ST] as gross margin keeps sliding from 51.4% to 47.4% [IS] and the currency-driven +123.5% 52-week rise [ST] reverses under sole-country Zimbabwe risk (note section 6)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: valuation multiples, market cap and peers are unavailable and the USD-vs-ZWG basis of the DCF is unverified, so a lower ZWG price would not by itself justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

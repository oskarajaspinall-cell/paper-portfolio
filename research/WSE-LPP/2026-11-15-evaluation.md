# Evaluation: LPP SA (WSE:LPP) — 2026-11-15
## Bear case
The price has run ahead of the fundamentals [Certain]: +71.7% over 12 months, 30.9% above the 200-day average, RSI 68.8, and P/B 10.2x above its 5y max. Base fair value 30,420.97 PLN is only +6.0% above the close, so returns now depend on growth holding; if Sinsay or store openings slow, an extended stock de-rates [Likely]. June guidance was already cut on fewer openings and operational headwinds [Likely]. ROIC is 5.0pp below its 2-year high of 22.6% and ROCE slipped from 28.6% to 27.2% over the last year [Certain]; the FCF rebound from 2.7% to 13.4% may be partly working-capital timing, given FY2023's -3.6% [Likely]. Results land Dec 3, 2026, a near-term gap risk [Certain]. Foreign revenue mix and PLN exposure are unverified (macro overlay) [Certain].
## Bull case
A high-return, vertically integrated retailer that is working [Likely]: TTM ROIC 17.6%, ROE 38.3%, gross margin 57.4% (a 5-year high), operating margin up 1.2pp to 12.8% over 12 months [Certain]. Q2 brought record profitability and a Sinsay recovery (transcript) [Likely]. The ROIC/ROCE dip from the 2024 peak looks like an investment phase (store expansion, logistics) rather than lost share, with leverage falling to 1.54x from 2.70x [Likely]. Despite the run, EV/EBITDA 11.0x is below its 5y minimum and 23% under peers, P/FCF 16.1x is below its 5y median, and the FCF yield is 6.21% [Certain]. Beta 0.36 and Piotroski 7 add resilience [Certain].
## Decision
```json
{
  "ticker": "WSE:LPP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Scorecard finds nothing falling over 1y or 3y; ROIC and ROCE sit below their 2024 highs, which the Q2 transcript ties to store-expansion investment alongside record profitability (https://stockanalysis.com/quote/wse/LPP/transcripts/543283-q2-26-27/), not lost share.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Growth slows (fewer openings, as in the June guidance cut) and the extended price, 30.9% above its 200-day average, de-rates.", "veto": null},
  "thesis": "A high-return, vertically integrated apparel retailer in a strong uptrend, priced close to its base fair value.",
  "rationale": "Scorecard conviction 3: quality and trend are strong, but base fair value sits barely above the price, the stock is extended into the Dec 3 results, and the moat is narrow. Good but not compelling, so AVOID (owner rule: high conviction only); entry price at base fair value less the margin of safety.",
  "price_at_decision": 28700.00,
  "price_date": "2026-11-13",
  "research_note": "research/WSE-LPP/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 10.5%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10.5}},
    {"text": "TTM ROIC falls below 13%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 13}},
    {"text": "Net debt/EBITDA rises above 2.7x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.7}},
    {"text": "TTM FCF margin falls below 6% with no working-capital explanation in filings", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 40280, "basis": "Margins keep rising and P/E re-rates to its 5y max 38.6x [RA] on TTM EPS [IS]."},
    "base": {"probability": 0.5, "target_price_12m": 30420.97, "basis": "Mechanical base fair value 30,420.97 PLN (DCF + EV/EBITDA blend) [fact sheet Fair value], consistent with the reverse-DCF 6.5% growth."},
    "bear": {"probability": 0.25, "target_price_12m": 22790.51, "basis": "Growth slows after the June guidance cut (Q1 transcript) and EV/EBITDA de-rates to the method's bear value 22,790.51 PLN [fact sheet Fair value]."}
  },
  "entry_price": 24336.78,
  "entry_basis": "valuation file: base 30,420.97 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

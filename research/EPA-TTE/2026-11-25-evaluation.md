# Evaluation: TotalEnergies SE (EPA:TTE) — 2026-11-25
## Bear case
Earnings sit near a cyclical high: TTM ROIC 14.3% and operating margin 17.0% are 2-year highs, against FY2025's 8.0% and 10.8% [Certain]. The Direction change lines (12-month rise against a 5-year fall) look like the oil and gas cycle turning up, not a better business, so they can reverse as fast [Likely]. The reverse DCF prices a year-1 revenue fall of 17.2%, and the DCF base is flagged unreliable because it extrapolates near-peak cash flow [Certain]. P/B 1.5x and EV/Sales sit above their 5y max [Certain]. The trend case is thin: the close is below the 50-day average with 6-month momentum flat, so an extended 12-month run (+39.9%) risks a de-rating if prices normalise [Likely]. The dip's cause is unverified; Q3 results were not reviewed [Certain]. ROCE is falling over 3 years [Certain]. No moat: a commodity price-taker [Likely].

## Bull case
On today's earnings the stock is cheap: P/E 8.8x vs peer median 14.1x, EV/EBITDA 4.3x vs 5.8x, FCF yield 12.27% [Certain]. The balance sheet is strong (net debt/EBITDA 0.52x, Piotroski F 8) and shares fell 2.31% YoY on buybacks [Certain]. The 12-month recovery in ROIC, operating and FCF margin is a cyclical upturn with the balance sheet intact, i.e. temporary rather than structural [Likely]. LNG growth (a 15-year China supply agreement) and the Continental Resources US gas deal add volume [Likely]. No company-specific negative headline explains the dip, and a low-beta, high-yield major can re-rate toward peers [Guessing].

## Decision
```json
{
  "ticker": "EPA:TTE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Python finds none of ROIC, operating margin or FCF margin falling over 1 or 3 years; all rose over the last 12 months (ROIC 8.3% -> 14.3%, operating margin 11.6% -> 17.0%) [RA-T, IS-T], a commodity-cycle upswing with net debt/EBITDA 0.52x [ST].", "moat": "none", "key_risk": "medium", "key_risk_text": "Oil and gas prices normalise from a cyclical high, cutting earnings back toward FY2025 levels (ROIC 8.0%) and de-rating the stock; the reverse DCF already prices a year-1 revenue fall of 17.2%.", "veto": null},
  "thesis": "A cheap, low-leverage integrated major whose returns are cyclical, with earnings near a cycle high and no moat to protect them.",
  "rationale": "Cheap on peers and FCF yield with a strong balance sheet, but returns are commodity-driven near a 2-year high, the fair value is unreliable and the dip is small and unexplained. Same evidence as the 15 Nov AVOID; nothing reported since changes it. Conviction 3: AVOID.",
  "price_at_decision": 77.68,
  "price_date": "2026-11-24",
  "research_note": "research/EPA-TTE/2026-11-25.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 8%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "FCF margin (TTM) falls below 6%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "Net debt/EBITDA rises above 1.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Operating margin (TTM) falls below 11%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 94.0, "basis": "Earnings hold and P/E re-rates to its 5y max of 10.7x [RA], still below the peer median of 14.1x, supported by the 12.27% FCF yield and buybacks [ST]."},
    "base": {"probability": 0.45, "target_price_12m": 76.0, "basis": "Earnings ease from the TTM high while P/E stays near its 5y range (median 7.9x) [RA]; well below the DCF base of 168.14, which is flagged unreliable for extrapolating near-peak cash flow [fact sheet Fair value]."},
    "bear": {"probability": 0.3, "target_price_12m": 62.0, "basis": "Commodity normalisation takes returns back toward FY2025 (ROIC 8.0%, operating margin 10.8%) [RA, IS] at a P/E near its 5y low of 7.5x [RA]; below the mechanical DCF bear of 71.29 because that bear still starts from peak cash flow."}
  },
  "entry_price": 66.0,
  "entry_basis": "P/E back near its 5y low of 7.5x [RA] on TTM earnings, a price that would offset the cyclical-peak risk; the default (valuation file base 168.14 x 0.85) is above the price and the fair value is flagged unreliable, so it cannot anchor.",
  "new_evidence": null,
  "replaces": null,
  "replacement_reason": null
}
```

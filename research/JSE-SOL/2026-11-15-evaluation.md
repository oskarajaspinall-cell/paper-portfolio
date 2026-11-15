# Evaluation: Sasol Limited (JSE:SOL) — 2026-11-15
## Bear case
Sasol is a commodity converter with no evident moat: returns follow oil, refining margins, the rand and plant reliability [Likely]. The price is +104.4% in 12 months and 21.3% above its 200-day average, partly on an oil/Hormuz spike [Likely]; if that fades, an extended price risks a sharp de-rating [Likely]. Earnings multiples are not cheap: P/E 13.0x sits 66% up its 5y range and P/FCF 13.1x at 97% [Certain]. FCF margin slipped to 4.3% and ROIC is 4.6pp below its 2-year high of 20.1% [Certain]; the five-year operating-margin decline is only partly reversed by the last year's rise (15.0% to 17.1%), a cyclical recovery rather than a new trend [Likely]. Net margin was -16.1% in FY2024 and Altman Z 2.06 is grey-zone [Certain]. South African country, rand and fuel-pricing risk are unverified [Certain]. No mechanical fair value exists [Certain].

## Bull case
FY2026 showed better reliability and cost discipline, with net debt at a 10-year low [Likely]; net debt/EBITDA fell from 1.55x to 1.11x [Certain]. TTM ROIC 15.4% and ROCE 16.5% are up year on year, and operating margin recovered to 17.1% [Certain]. EV/EBITDA 3.7x is 53% below the peer median and P/B 0.9x is below peers' 1.4x [Certain]. The FCF yield is 7.62% and Piotroski F is 7 [Certain]. The trend is strong: the 50-day average is 22.5% above the 200-day and relative strength vs SPY is +94.0pp over 12 months [Certain]. The restarted Italian paraffin unit adds chemicals volume [Likely]. Higher oil supports Secunda fuel margins [Likely].

## Decision
```json
{
  "ticker": "JSE:SOL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python lists nothing falling over 1 or 3 years: ROIC and operating margin rose over the last 12 months [RA-T, IS-T] and FCF margin is flat [CF-T]; the ROIC gap to its 2-year high reflects the cyclical FY2024 peak.",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Oil/refining margins and the rand reverse after a +104.4% 12-month run, de-rating an extended price on a commodity-driven earnings base with no moat.",
    "veto": null
  },
  "thesis": "A cyclical South African fuels-and-chemicals converter with improving reliability and lower leverage, but no moat and an oil-spike-driven price run.",
  "rationale": "Balance sheet and returns improved and EV/EBITDA is low, but earnings multiples are high in their own range, there is no mechanical fair value, no moat, and the rally rides an oil spike. Good trend, not compelling enough for high conviction: AVOID.",
  "price_at_decision": 24300.0,
  "price_date": "2026-11-13",
  "research_note": "research/JSE-SOL/2026-11-15.md",
  "triggers": [
    {"text": "ROIC TTM falls below 10% [RA-T]", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Operating margin TTM falls below 14% [IS-T]", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 14}},
    {"text": "Net debt / EBITDA rises above 2.0x [RA]", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "FCF margin TTM falls below 2% [CF-T]", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 30056, "basis": "Oil and refining margins hold and reliability gains persist, so the price retests its 52-week high of 30,056 ZAc [HI] while EV/EBITDA stays below the 8.0x peer median [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 24536, "basis": "Earnings hold near FY2026 levels with ROIC 15.4% [RA-T], so the price trades around its 50-day average of 24,535.94 ZAc [HI]; no mechanical fair value exists to reconcile against [valuation file]."},
    "bear": {"probability": 0.30, "target_price_12m": 17842, "basis": "The oil/Hormuz spike fades (https://www.ibtimes.com.au/sasol-shares-rise-oil-prices-hormuz-strikes-1876452) and P/E 13.0x near the top of its range [RA] de-rates, taking the price back to the August swing low of 17,842 ZAc [HI]."}
  },
  "entry_price": 20032,
  "entry_basis": "No mechanical fair value (no ZAR FX rate), so anchored to the 200-day average of 20,032.19 ZAc [ST,HI], where the 12-month trend gain is largely given back and earnings multiples would sit nearer their 5y medians.",
  "replaces": null,
  "replacement_reason": null
}
```

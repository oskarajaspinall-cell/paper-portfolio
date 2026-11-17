# Evaluation: Autoliv, Inc. (ALV) — 2026-11-17
## Bear case
Autoliv is a cyclical supplier whose earnings follow global light-vehicle production, and Q3 sales were nearly flat as vehicle output weakened [Certain] (OV transcript). FY26 guidance is flat organic sales and the adjusted margin was steered to the low end of its range [company-reported] (https://www.sec.gov/Archives/edgar/data/1034670/000119312526429588/alv-20260930.htm). Rolling returns have peaked: ROIC is 4.8pp below its 2-year high of 23.3% and ROCE fell from 26.0% to 24.8% over 12 months [Certain] (RA-T), driven by tariff, raw-material and logistics costs only mostly passed through [company-reported] (same URL). If pass-through weakens, this becomes structural [Guessing]. It already trades at a premium to peers on every multiple and P/B sits at 90% of its 5y range [Certain] (RA). China OEM exposure is growing but unquantified [data unavailable]. The price is below its 200-day average with a -2.1% 12-month change, so there is no trend support [Certain] (HI, ST).

## Bull case
Safety is a concentrated oligopoly where certification, liability record and scale keep entrants out [Likely]. Five-year returns rose (ROIC 12.7% to 18.5% TTM, operating margin 8.3% to 10.2%) and the 12-month dip is cost pressure, not lost share: FCF margin rose from 5.4% to 6.6% and FCF conversion is 117% [Certain] (IS, CF-T). Leverage is modest at 1.21x net debt/EBITDA [Certain] (BS). The stock is cheap on its own history: EV/EBITDA 6.7x at the bottom of its 5y range, P/FCF 11.8x below its 5y minimum, an 8.48% FCF yield [Certain] (RA, ST). The reverse DCF implies only 1.5% year-1 revenue growth [Certain]. Shares fell 4.12% YoY and the dividend was raised 15% [Certain] (ST; https://www.prnewswire.com/news-releases/autoliv-declares-increased-quarterly-dividend-302933998.html). Base fair value 138.05 sits above the price [Certain].

## Decision
```json
{
  "ticker": "ALV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no metric falling over 1 or 3 years; the softer ROCE and ROIC below its 2-year high reflect tariff, raw-material and logistics costs mostly passed through [company-reported] (https://www.sec.gov/Archives/edgar/data/1034670/000119312526429588/alv-20260930.htm), while FCF margin rose from 5.4% to 6.6% and leverage is flat at 1.21x.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A light-vehicle production downturn or weaker tariff/cost pass-through pushes margins back toward the FY2022 level, with the premium to peers de-rating.",
    "veto": null
  },
  "thesis": "The leading auto-safety supplier with rising five-year returns, an 8.48% FCF yield and EV/EBITDA at the bottom of its own range is cheap on history, but its rolling returns have peaked and its earnings stay tied to a flat vehicle-production cycle.",
  "rationale": "Quality, balance sheet and own-history cheapness are real, but rolling returns are off their highs, growth guidance is flat, the stock trades at a premium to peers and has no trend support. The scorecard sets the conviction; below the buy bar this is an AVOID with an entry price.",
  "price_at_decision": 117.37,
  "price_date": "2026-11-16",
  "research_note": "research/ALV/2026-11-17.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, giving up most of the five-year improvement from 12.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 9%, showing cost pass-through has failed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 9}},
    {"text": "TTM FCF margin falls below 4.5%, back to FY2024 levels, showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 4.5}},
    {"text": "Net debt/EBITDA rises above 2.0x, e.g. from acquisitions or buybacks outrunning cash flow.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 152.0, "basis": "Cost pass-through restores ROIC toward its 23.3% 2-year high and EV/EBITDA returns to its 5y median 7.8x [RA], near the mechanical bull fair value 153.88."},
    "base": {"probability": 0.5, "target_price_12m": 135.0, "basis": "Flat organic sales with margin around guidance [company-reported] and EV/EBITDA partly re-rating from the 5y minimum 6.7x [RA], a little under the base fair value 138.05."},
    "bear": {"probability": 0.25, "target_price_12m": 100.0, "basis": "A production downturn cuts EBITDA while EV/EBITDA stays at its 6.7x 5y low [RA]; above the DCF bear 46.40, which is an unreliable extreme next to the EV/EBITDA bear 114.55."}
  },
  "entry_price": 117.34,
  "entry_basis": "valuation file: base 138.05 x 0.85.",
  "replaces": null,
  "replacement_reason": null
}
```

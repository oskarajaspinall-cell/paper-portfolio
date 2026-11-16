# Evaluation: Trex Company, Inc. (TREX) — 2026-11-16
## Bear case
Returns are still falling, not turning: TTM ROIC 14.3% vs 17.0% a year earlier and 24.0% two years ago; operating margin 19.2% vs 24.2% [RA-T, IS-T] [Certain]. The Direction change lines confirm the 5-year decline continued through the last 12 months [Certain]. Part is Arkansas ramp cost (depreciation, freight, labour) [company-reported] [Likely], but the push into cladding and fencing suggests the core decking franchise is maturing [Guessing]. The valuation points come from trend strength: the price is 20.8% above its 200-day average after +59.6% in 12 months, and the reverse DCF already implies 27.5% year-1 growth [Certain]; if growth slows the multiple can de-rate toward its 5y P/E low of 19.8x [Likely]. Real yields rose +0.47pp in three months, hitting deferrable remodel demand and the multiple (macro overlay) [Likely]. A sole national distributor concentrates channel risk [Certain].
## Bull case
Q3 sales rose 26% to $360M with back-to-back record quarters, and FY sales guidance was raised to $1.296B-$1.306B [OV transcript] [Certain]. The margin squeeze is explained by a guided plant ramp, not lost share: underlying growth outpaced the market [Likely]. FCF margin jumped to 15.7% from 2.0% as capex eased, FCF conversion is 112.9%, and P/FCF of 26.2x sits below its 5y minimum [Certain]. The balance sheet is sound (net debt/EBITDA 0.67x, Altman Z 7.89) and shares are down 3.13% YoY on buybacks [Certain]. P/E of 30.8x is in the bottom fifth of its own 5y range and below the peer median 34.2x [Certain]. Once Arkansas is absorbed, gross margin can recover toward its FY2024 43.6% [Guessing], and the brand plus recycled-material cost position protects returns [Likely].
## Decision
```json
{
  "ticker": "TREX",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Gross margin fell to 36.0% from 40.5% on depreciation, freight and labour as the Arkansas plant started [company-reported] (https://www.sec.gov/Archives/edgar/data/1069878/000119312526447251/trex-20260930.htm), while Q3 sales rose 26% with guidance raised; FCF margin rose to 15.7% [CF-T]. A ramp cost, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "After a +59.6% re-rating the price assumes a margin recovery; if rising real yields slow remodel demand and Arkansas stays under-absorbed, margins keep falling and the multiple de-rates toward its 5y low.",
    "veto": null
  },
  "thesis": "A leading composite-decking brand with explained ramp-driven margin pressure, strong sales momentum and rising FCF, but a price that already discounts the recovery.",
  "rationale": "Scorecard gives 3: sound balance sheet and strong trend, but ROIC and operating margin are still falling and the value blend shows no discount after the re-rating. Good but not compelling, so AVOID (owner rule: only high conviction is bought); cash is an acceptable outcome.",
  "price_at_decision": 52.76,
  "price_date": "2026-11-13",
  "research_note": "research/TREX/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 17%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "TTM ROIC falls below 12%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA rises above 1.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "TTM FCF margin falls below 8%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 65.0, "basis": "Arkansas absorbed and margins recover while raised FY guidance holds; the EV/EBITDA method's base of 59.37 and bull of 84.21 [fact sheet fair value] bracket this, above the unreliable DCF."},
    "base": {"probability": 0.45, "target_price_12m": 52.0, "basis": "Growth continues but margin stays near 19.2% [IS-T]; P/E holds near its 5y median 31.0x [RA]; sits between the DCF base 18.36 and EV/EBITDA base 59.37, which disagree 3.2x so the blended 32.03 is weighed lightly."},
    "bear": {"probability": 0.30, "target_price_12m": 35.61, "basis": "Real yields keep rising and remodel demand slows, de-rating the multiple toward its 5y low (macro overlay tilt toward bear, small, adds weight here); matches the EV/EBITDA bear of 35.61 [fact sheet fair value]."}
  },
  "entry_price": 25.62,
  "entry_basis": "valuation file: base 32.03 x 0.8; the fair value is flagged unreliable, so a hit means a full re-research, with the margin trend re-checked first.",
  "replaces": null,
  "replacement_reason": null
}
```

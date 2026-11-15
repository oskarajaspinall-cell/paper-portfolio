# Evaluation: Asahi Intecc Co., Ltd. (TYO:7747) — 2026-11-15
## Bear case
The price already discounts a lot: the reverse DCF implies 20.9% year-1 revenue growth, and the mechanical base fair value of 2,711.32 JPY sits 28.9% below the 3,811.00 close [Certain]. Against peers the stock is dear on every multiple (EV/EBITDA +62%, P/FCF +72%) and P/B of 5.8x is above its 5y maximum [Certain]. Valuation support comes from trend strength (up 61.6% in 12 months, 10.8% above the 200-day average), not a discount; if growth slows from a 31.0% operating margin that is hard to extend, an extended price risks a de-rating toward the base fair value [Likely]. The Direction change flag is real: FCF margin fell to 21.8% from 27.0% [Certain], most likely working-capital timing after FY2025's 254.7% conversion [Likely], but unproven. Q1 FY2027 results (2026-11-13) are not yet reflected [Certain]. Geographic mix and FX exposure are unknown [Certain].
## Bull case
A high-quality, accelerating compounder: TTM ROIC 27.5% vs 19.0% a year earlier, operating margin 31.0% vs 25.1%, gross margin 70.4% [Certain]. A 70% gross margin in consumable guidewires suggests a surgeon-preference and technical moat [Likely]. The balance sheet is net cash (net debt/EBITDA -1.07x), Piotroski 8, Altman Z 13.14, and the share count is shrinking 2.02% [Certain]. P/E of 31.6x is at the bottom (1% position) of its own 5y range and EV/EBITDA at 25%, so on own history it is not stretched [Certain]. FCF conversion of 98.9% is sound; the FCF margin dip looks like normalisation from an inflated FY2025, not a structural break [Likely]. Beta 0.42 makes it a low-volatility way to own a working business [Certain].
## Decision
```json
{
  "ticker": "TYO:7747",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only FCF margin falls (27.0% -> 21.8% TTM) while ROIC and operating margin rise; FY2025 FCF conversion of 254.7% vs 98.9% in FY2026 points to working-capital timing, not lost economics [CF,IS; note section 2].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A de-rating of an extended price: the reverse DCF already implies 20.9% year-1 growth, so any slowdown from a 31.0% operating margin could pull the price toward the 2,711.32 base fair value [fact sheet Fair value].",
    "veto": null
  },
  "thesis": "A net-cash, high-return guidewire franchise with rising margins, but the price already discounts strong growth and sits well above the mechanical base fair value.",
  "rationale": "Quality, balance sheet and trend are strong, but the price needs sustained high growth and carries de-rating risk; geographic mix and the Q1 FY2027 results are unverified. Scorecard sets conviction; good but not compelling, so AVOID with an entry price.",
  "price_at_decision": 3811.00,
  "price_date": "2026-11-13",
  "research_note": "research/TYO-7747/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 26% (margin expansion reverses)", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 26}},
    {"text": "TTM ROIC falls below 20%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 15% (cash conversion breaks)", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 4793.69, "basis": "Margin gains continue and the multiple holds; matches the mechanical bull fair value 4,793.69 [fact sheet Fair value, IS-T]."},
    "base": {"probability": 0.45, "target_price_12m": 3811.00, "basis": "Earnings keep growing but P/E stays near its 5y low of 31.4x [RA], so the price roughly holds; above the 2,711.32 base fair value because the DCF uses own-history growth below the improved margins [IS-T]."},
    "bear": {"probability": 0.30, "target_price_12m": 2711.32, "basis": "Growth slows short of the 20.9% the reverse DCF implies and the stock de-rates to the mechanical base fair value 2,711.32 [fact sheet Fair value]."}
  },
  "entry_price": 2169.06,
  "entry_basis": "valuation file: base 2,711.32 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

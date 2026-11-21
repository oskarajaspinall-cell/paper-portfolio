# Evaluation: EOG Resources, Inc. (EOG) — 2026-11-21
## Bear case
EOG's returns follow oil and gas prices, not a moat: ROIC fell from 32.6% in FY2022 to 16.0% in FY2025 and is down over three years even after the TTM rebound to 22.7% [Certain]. The rolling recovery (ROIC 17.6% -> 22.7%, FCF margin 17.2% -> 25.3%) reflects firmer commodity prices and record volumes, which can reverse; it should not be extrapolated [Likely]. The mechanical fair value of 154.15 is barely above the 148.60 close, one method only with a narrow range, so there is no real margin of safety [Certain]. Valuation support comes from trend strength (price above its 200-day, up 38.8% in 12 months), and an extended energy price risks a de-rating if crude softens [Likely]. The dip has no identified stock-specific cause; it may be a sector rotation that continues [Guessing]. Commodity prices are outside the macro snapshot, so the overlay offers no help [Certain].

## Bull case
The fall is not tied to company news: Q3 delivered record production, an 8% dividend increase and unchanged guidance, and the 10-Q shows no change to Risk Factors [Certain]. The balance sheet is near net-cash (net debt/EBITDA 0.16x, Altman Z 3.86, Piotroski 7) [Certain]. The last year is improving, with FCF margin at its 2-year high and operating margin 35.5% [Certain]. It is cheap on cash: P/FCF 10.4x and EV/EBITDA 5.0x sit below their 5-year minimums, FCF yield is 9.58% and P/E is 20% under peers [Certain]. Buybacks shrink the count 3.50% a year and the authorization was raised to $20 billion [company-reported] [Certain]. Low-cost, high-return inventory is a real, if shared, edge [Likely].

## Decision
```json
{
  "ticker": "EOG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and operating margin are down over three years because 2022-23 commodity prices were exceptional; over the last 12 months both are rising (ROIC 17.6% -> 22.7%, operating margin 31.6% -> 35.5% [RA-T, IS-T]) with net debt/EBITDA 0.16x [RA], a cyclical swing with the balance sheet intact, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "A fall in oil and gas prices takes returns back toward the FY2025 level (ROIC 16.0% [RA]) and de-rates a stock whose valuation points rest on trend strength after a 38.8% 12-month rise [ST].",
    "veto": null
  },
  "thesis": "A near-net-cash, low-cost shale producer with improving rolling returns trades below its own 5-year EV/EBITDA and P/FCF minimums, but its returns follow commodity prices and the mechanical fair value offers little margin of safety.",
  "rationale": "The dip has no stock-specific cause and the business is sound, but the evidence is the same as the 2026-11-15 AVOID: cyclical, commodity-driven returns, a narrow moat and fair value barely above the price. Conviction 3 does not clear the buy bar; cash is acceptable.",
  "price_at_decision": 148.60,
  "price_date": "2026-11-20",
  "research_note": "research/EOG/2026-11-21.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, under the FY2025 level of 16.0%, showing returns are breaking below the cyclical range.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 15%, under the FY2025 five-year low of 15.2%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Shares outstanding change YoY turns positive (now -3.50%), i.e. buybacks stop shrinking the count.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "Net debt/EBITDA on the ratios page rises above 1.0x (0.16x TTM) without a matching acquisition."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 165.93, "basis": "Firm commodity prices and continued buybacks return the stock to its 52-week high of 165.93 [HI], consistent with the mechanical bull fair value range being exceeded only modestly [IS,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 154.15, "basis": "EV/EBITDA reverts to its 5y median 5.3x [RA] on TTM EBITDA, the mechanical base fair value of 154.15."},
    "bear": {"probability": 0.25, "target_price_12m": 127.30, "basis": "Softer oil prices push returns back toward FY2025 levels (ROIC 16.0% [RA]) and the stock to its 6-month low of 127.30 [HI]."}
  },
  "entry_price": 131.03,
  "entry_basis": "valuation file: base 154.15 x 0.85",
  "replaces": null,
  "replacement_reason": null
}
```

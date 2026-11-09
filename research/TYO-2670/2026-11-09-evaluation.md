# Evaluation: ABC-Mart,Inc. (TYO:2670) — 2026-11-09
## Bear case
The re-rating is done. The stock is up 22.8% over 12 months with RSI 69.1, and the close of 3,201.00 JPY sits on the mechanical base fair value of 3,229.65 JPY, so there is no margin of safety [Certain]. EV/Sales and P/B are above their 5y maxima, and EV/EBITDA of 8.2x is 23% above peers [Certain]. On the Direction change, TTM ROIC fell to 23.0% from 24.3% and sits 12.8pp below its 2-year high of 35.8%. FCF margin of 8.8% is 6.7pp below its 2024 high, and FCF conversion fell to 60.8% in FY2026 [Certain]. The cause (capex, inventory or working capital) is unverified [Guessing]. Returns look to have plateaued rather than compounded [Likely]. The moat is scale and brand-partner access, and brand owners selling direct could erode it [Guessing]. Piotroski F is 4 [Certain]. The price already implies 6.1% year-1 revenue growth [Likely].

## Bull case
This is a high-quality, net-cash retailer. ROIC is 23.0% TTM against 13.8% in FY2022, operating margin is 16.8% TTM (its 2-year high) against 11.3%, net debt/EBITDA is -3.00x and Altman Z is 9.85 [Certain]. The ROIC dip over the last year is mild while margins stay at their high, which points to a heavier asset or working-capital base rather than a broken model [Likely]. P/E of 16.9x is at 30% of its 5y range and below the peer median of 17.2x, and P/FCF of 23.7x is well below the peer median [Certain]. If FCF conversion recovers towards FY2025's 101.6%, cash returns could support a move to the bull fair value of 4,635.89 JPY [Guessing]. A beta of -0.13 diversifies the portfolio [Certain]. Insiders own 12.66% [Certain].

## Decision
```json
{
  "ticker": "TYO:2670",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "TTM ROIC fell to 23.0% from 24.3% [RA-T], but operating margin is at its 2-year high of 16.8% [IS-T] and FCF margin rose year on year to 8.8% from 7.8% [CF-T]; the balance sheet is net cash at -3.00x [BS]. This looks like a heavier invested-capital base, not lost share or a price cap.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Brand owners shifting to direct-to-consumer sales could compress ABC-Mart's gross margin (50.4% TTM [IS]) and returns; plausible but not visible in the data yet.",
    "veto": null
  },
  "thesis": "A high-return, net-cash Japanese footwear retailer whose quality is real, but at the base fair value after a 22.8% rise the price leaves no margin of safety.",
  "rationale": "The quality is good and the balance sheet strong, but the price sits on the base fair value, EV/Sales and P/B are above their 5y maxima, and FCF conversion has weakened. Good but not compelling, so AVOID. It becomes a buy near the entry price below.",
  "price_at_decision": 3201.00,
  "price_date": "2026-11-06",
  "research_note": "research/TYO-2670/2026-11-09.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 18%, showing returns are eroding rather than plateauing", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "Operating margin (TTM) falls below 14.5%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 14.5}},
    {"text": "Gross margin (TTM) falls below 48%, a sign of lost brand-partner terms", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 48}},
    {"text": "FCF conversion (FCF/NI, fiscal year) stays below 60% for a second year"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 4635.89, "basis": "FCF conversion recovers towards FY2025's 101.6% [CF] and margins hold at 16.8% [IS], reaching the mechanical bull fair value [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 3229.65, "basis": "Returns plateau with ROIC around 23.0% [RA] and the price stays near the mechanical base fair value, which the DCF (3,239.01) and EV/EBITDA (3,210.93) methods both support [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 2820.23, "basis": "EV/EBITDA falls back from 8.2x towards its 5y median of 8.0x as the FCF weakness persists, giving the EV/EBITDA bear value [RA]; this is above the blended bear of 1,808.24 because the DCF bear's growth haircut looks too severe for a net-cash retailer at its margin high [IS,BS]."}
  },
  "entry_price": 2583.72,
  "entry_basis": "valuation file: base 3229.65 x 0.8, the 20% margin of safety [ST]; price is the obstacle, quality is intact.",
  "replaces": null,
  "replacement_reason": null
}
```

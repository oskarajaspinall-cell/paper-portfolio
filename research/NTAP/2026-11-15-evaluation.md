# Evaluation: NetApp, Inc. (NTAP) — 2026-11-15
## Bear case
The price already discounts a lot. P/E 25.6x, EV/EBITDA 16.5x and P/FCF 21.6x all sit above their own 5y maxima, and the reverse DCF needs 25.5% year-1 revenue growth [Certain]. Mechanical base fair value is 87.50 against 181.37 [Certain]. The trend points come from an extended price, so if AI-storage growth slows the stock can de-rate toward its historical range [Likely]. The **Direction change** is real: TTM FCF margin fell from 25.2% to 22.3%, 4.7pp below its 2-year high. The 10-Q blames memory and component cost inflation and adds risk language on fixed-price purchase commitments [company-reported] [Likely]. That looks like a cyclical input-cost squeeze on a price-taker, not lost share [Likely]. Macro tilts bear (small): 10y real yields rose +0.47pp over 3m and beta is 1.51 (macro overlay) [Certain]. Q2 results land on 2026-12-01 [Certain]. Buybacks at record multiples earn less [Likely].
## Bull case
This is a business that is working. ROCE rose to 30.1% and operating margin to 26.0% on a rolling basis, both at their 2-year highs. Gross margin is 70.6% and the balance sheet is net cash (-0.50x) [Certain]. The FCF dip comes from input costs that price rises are offsetting, per the filing [company-reported]. FCF conversion is still 116.4% of net income [Certain], so the dip looks temporary [Likely]. The ONTAP installed base and support contracts give recurring revenue, and hyperscaler integration plus AI deals (PEAK:AIO, Nebul adopting Novus, Oracle) extend the franchise [Likely]. The stock is +62.6% over 12 months and +17.7% above its 200-day, with a 4.63% FCF yield. It has pulled back 11.0% below its 50-day, so the run is not extreme [Certain]. Against peers it is cheaper on P/FCF by -16% [Certain]. Shares are down 3.14% YoY [Certain].
## Decision
```json
{
  "ticker": "NTAP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "TTM FCF margin fell from 25.2% to 22.3% while operating margin and ROCE rose to 2-year highs; the Q1 FY2027 10-Q attributes gross-margin pressure to memory/component cost inflation offset by price rises (https://www.sec.gov/Archives/edgar/data/1002047/000119312526380207/ntap-20260731.htm), and FCF conversion remains 116.4% [CF,IS].",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "De-rating: every multiple sits above its own 5y maximum and the reverse DCF needs 25.5% year-1 revenue growth; slower AI-storage demand or persistent memory-cost inflation (with rising real yields, macro overlay) would compress the multiple toward its historical range.",
    "veto": null
  },
  "thesis": "A high-return, net-cash storage franchise with rising rolling margins is in a genuine AI-driven uptrend, but the price sits above every own-history multiple and implies growth the business has not shown.",
  "rationale": "Quality, balance sheet and trend are strong, but the scorecard does not reach the buy bar: the price discounts 25.5% growth, all multiples exceed their 5y maxima and the probability-weighted scenarios sit below the price. Good but not compelling is an AVOID (owner rule: high conviction only).",
  "price_at_decision": 181.37,
  "price_date": "2026-11-13",
  "research_note": "research/NTAP/2026-11-15.md",
  "triggers": [
    {"text": "TTM gross margin falls below 66%, meaning price rises fail to cover memory costs.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 66}},
    {"text": "TTM operating margin falls below 22%, reversing the rolling expansion from 21.8% to 26.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}},
    {"text": "TTM FCF margin falls below 18%, showing the input-cost squeeze is structural rather than temporary.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 18}},
    {"text": "Trailing ROCE on the ratios page falls below 22%, or net debt/EBITDA turns positive from net cash."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 240.0, "basis": "AI-storage demand and price rises hold margins at 2-year highs [IS-T], and the stock regains its 52-week high of 240.87 [HI] as Q2 results confirm the rerating; well above mechanical bull fair value 105.13 because the model ignores the AI rerating."},
    "base": {"probability": 0.4, "target_price_12m": 165.0, "basis": "P/E drifts toward its 5y max 21.2x [RA] (macro overlay: rising real yields, small bear tilt) partly offset by earnings growth from rising operating margin [IS-T]; still above base fair value 87.50, which assumes historical growth."},
    "bear": {"probability": 0.35, "target_price_12m": 106.0, "basis": "AI growth slows and memory costs persist, so multiples revert toward their 5y range, near the EV/Revenue base fair value 106.15 [IS,RA]; probability raised for the macro overlay's small bear tilt."}
  },
  "entry_price": 70.0,
  "entry_basis": "valuation file: base 87.50 x 0.8.",
  "replaces": null,
  "replacement_reason": null
}
```

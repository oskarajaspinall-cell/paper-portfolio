# Evaluation: Abercrombie & Fitch Co. (ANF) — 2026-11-17
## Bear case
The entry hit is a fall with no identified cause: the stock is down from 172.00 (2026-11-05) to 145.77 with no company news, one week before Q3 results on 2026-11-24 [Certain]. A price fall alone is no reason to buy. TTM margins are flattered by about $100 million of IEEPA tariff refunds in Q2 cost of sales, with about $14 million more due in Q3 [company-reported] (https://www.sec.gov/Archives/edgar/data/1018840/000101884026000047/anf-20260801.htm), so underlying returns are lower than the 14.1% operating margin shows [Likely]. The Direction change is real: ROIC fell from 29.7% to 26.7% over 12 months and sits 12.2pp below its 2-year high; ROCE fell from 31.5% to 30.1% [Certain]. Apparel brand heat is cyclical (FY2023 ROIC 1.3%) [Certain]. After a 107.7% 12-month rise and 35.0% above the 200-day average, any growth slowdown at the print risks a sharp de-rating [Likely]. Short interest 12.09% and rising [Certain].
## Bull case
Even with refunds stripped out the business earns high returns: ROIC 26.7%, ROE 40.6%, FCF margin rising 3.8pp to 10.6% over 12 months, net debt/EBITDA 0.71x, Altman Z 4.98 [Certain]. The ROIC dip is from a FY2025 peak after tariff costs, which the refunds partly reverse, not lost share: Q2 was a record with raised full-year guidance (https://www.wsj.com/business/retail/abercrombie-lifts-outlook-as-profit-sales-rise-dc5bf32f) [Likely]. The price is cheap on cash: FCF yield 9.16%, P/FCF 10.9x below its 5y minimum, EV/EBITDA 21% below peers [Certain]. The reverse DCF implies only 0.4% year-1 revenue growth [Certain]. Buybacks cut shares 9.81% YoY, compounding per-share value [Certain]. The uptrend is intact: 50-day average 37.2% above the 200-day, RSI 42.2 cooled off [Certain].
## Decision
```json
{
  "ticker": "ANF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and ROCE are down from the FY2025 peak after tariff costs compressed FY2026 operating margin (15.2% to 12.9% [IS]); TTM operating margin is flat (+0.1pp) and FCF margin rising (+3.8pp) [IS-T, CF-T], Q2 was a record with raised guidance (https://www.wsj.com/business/retail/abercrombie-lifts-outlook-as-profit-sales-rise-dc5bf32f) and IEEPA tariffs are being refunded (https://www.sec.gov/Archives/edgar/data/1018840/000101884026000047/anf-20260801.htm): a cost shock, not lost share.",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Brand heat in fashion apparel is cyclical (FY2023 ROIC 1.3% [RA]); after a 107.7% 12-month rise on refund-flattered margins, a slowdown at the 2026-11-24 Q3 print would de-rate the stock and expose lower underlying margins.",
    "veto": null
  },
  "thesis": "A high-return, lowly levered apparel retailer with a 9.16% FCF yield and heavy buybacks, whose refund-flattered margins and cyclical brand heat make the recent unexplained fall an unclear opportunity a week before results.",
  "rationale": "The fall has no identified cause and does not change the business case, but it does not remove the obstacle either: no moat, refund-flattered margins and a binary print a week away. The evidence is unchanged since the 2026-11-15 AVOID; the scorecard stays below the buy line. Cash is acceptable.",
  "price_at_decision": 145.77,
  "price_date": "2026-11-16",
  "research_note": "research/ANF/2026-11-17.md",
  "triggers": [
    {"text": "TTM operating margin falls below 11%, showing underlying margin ex tariff refunds is materially lower.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11}},
    {"text": "TTM ROIC falls below 20%, showing brand heat is fading rather than a tariff-cost dip.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 6%, reversing the cash recovery.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "Quarterly net sales growth in the earnings release turns negative for two consecutive quarters."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 205, "basis": "Q3 confirms raised guidance and underlying margins hold, so the price moves toward the DCF base of 193.21 and beyond on buybacks (shares -9.81% YoY [ST]), short of the 244.40 bull fair value."},
    "base": {"probability": 0.45, "target_price_12m": 150, "basis": "P/E holds near 12.4x [RA] as refund one-offs (about $14 million more in Q3 [company-reported], 10-Q) fade and buybacks offset them; below the 169.82 mechanical base because the TTM margin the DCF uses is refund-aided."},
    "bear": {"probability": 0.30, "target_price_12m": 95, "basis": "Brand heat cools at the print and EV/EBITDA falls toward its 5y minimum of 5.0x [RA], near the EV/EBITDA bear fair value of 85.62; the negative DCF bear is ignored as unreliable."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: valuation already scores on trend strength [ST], so no lower price lifts the scorecard to conviction 4; the obstacles are no moat, refund-flattered margins (https://www.sec.gov/Archives/edgar/data/1018840/000101884026000047/anf-20260801.htm) and cyclical brand heat.",
  "replaces": null,
  "replacement_reason": null
}
```

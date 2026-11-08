# Evaluation: Deckers Outdoor Corporation (DECK) — 2026-11-07
## Bear case
Premium footwear is fashion-dependent, and rivals' aggressive discounting is now hitting HOKA and UGG sell-through. That led to a cut in full-year sales guidance on 2026-10-22 [Certain] (https://www.reuters.com/business/deckers-results-show-aggressive-discounts-rivals-are-hitting-premium-brands-2026-10-22/). TTM ROIC has fallen to 71.9% from 104.4% in FY2026 [RA] [Certain]. The filing cites softer domestic DTC traffic, a disruptive European logistics transition and higher chargeback reserves [Certain]. IEEPA tariff refunds flatter cost of sales, so the 58.9% TTM gross margin overstates underlying pricing power [Likely]. Short interest of 8.19%, up 14.3% in a month [ST], shows growing scepticism [Certain]. If HOKA's share loss is structural, the multiple is a value trap: the mechanical bear value of 38.06 implies a margin fade the price has not yet priced in [Guessing]. The stock trades below its 200-day average, with 6-month relative strength of -16.8pp [HI] [Certain].
## Bull case
Even after the cut, the business earns elite returns: ROIC of 71.9%, a 23.6% operating margin, net cash and 99.3% FCF conversion [RA, IS] [Certain]. Q2 earnings beat the company's own expectations, and management raised its margin view while keeping full-price discipline (transcript, fact sheet news) [Likely]. At 86.71 the stock trades below its own 5y minimum P/E (11.4x vs 13.9x), EV/EBITDA (7.9x vs 9.3x) and P/FCF (11.0x vs 12.9x), with a 9.09% FCF yield [RA, ST] [Certain]. It also trades well below the peer median [Certain]. The reverse DCF implies -1.2% revenue growth, while the company still guides to growth [Likely]. Buybacks have cut the share count by 6.97% YoY at sub-historical multiples, which compounds per-share value [Certain]. Base fair value of 112.86 sits well above the price [Certain].
## Decision
```json
{
  "ticker": "DECK",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A net-cash, 70%+-ROIC footwear brand owner trades below its own 5-year minimum P/E, EV/EBITDA and P/FCF at a 9.09% FCF yield with 6.97% annual share shrinkage, pricing a revenue decline that beat-and-guide-growth results do not show.",
  "rationale": "Margins, cash conversion and net cash are intact and valuation is below every 5y low, so the thesis holds at conviction 4 and the position stays at its conviction size. The guidance cut, rival discounting and falling ROIC leave growth unresolved, so there is no case for conviction 5 or an ADD. Macro is context only.",
  "price_at_decision": 86.71,
  "price_date": "2026-11-06",
  "research_note": "research/DECK/2026-11-07.md",
  "triggers": [
    {"text": "TTM gross margin falls below 55%, under the FY2024 level of 55.6%, showing rival discounting is eroding full-price discipline.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}},
    {"text": "TTM operating margin falls below 20%, reversing most of the five-year expansion from 18.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 60%, under the FY2022 five-year low of 60.8%, showing brand-moat economics are deteriorating.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 60}},
    {"text": "FY2027 annual revenue (income statement page) declines year on year, showing HOKA and UGG together are shrinking rather than slowing."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 140, "basis": "Growth stabilises after the Q2 guidance cut and P/E re-rates toward its 5y median 17.6x [RA] on intact TTM margins [IS], below the bull fair value 182.96 because the guidance cut caps near-term growth."},
    "base": {"probability": 0.5, "target_price_12m": 105, "basis": "Margins hold at TTM 23.6% operating [IS] and P/E recovers to around its 5y minimum 13.9x [RA] as buybacks continue, a little below the base fair value 112.86 because slower HOKA/UGG growth (WSJ headline URL in fact sheet) delays a full re-rating."},
    "bear": {"probability": 0.25, "target_price_12m": 67, "basis": "Rival discounting (Reuters URL in fact sheet) erodes the 58.9% gross margin [IS] and earnings reset to the P/E-method bear value 67.01 in the fair value table; the DCF bear 23.59 is set aside as a margin collapse the net-cash balance sheet and current results do not show."}
  },
  "entry_price": null,
  "entry_basis": "Already held at its conviction-4 size; an ADD needs conviction 5, which requires evidence that HOKA/UGG growth is re-accelerating (the Q3 release) or that the ROIC decline is stabilising, not a lower price.",
  "replaces": null,
  "replacement_reason": null
}
```

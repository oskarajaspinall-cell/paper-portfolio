# Evaluation: NetEase, Inc. (HKG:9999) — 2026-11-07
## Bear case
The mechanical base fair value of 220.11 HKD sits only modestly above the 200.40 close, so much of the re-rating since our entry is done [Certain]. The bear value of 145.25 is well below the price, and the downside is larger than the base-case upside [Certain]. Earnings are hit-driven: TTM net margin of 27.9% is already below FY2025's 30.0% and ROE slipped to 20.4%, so the next cycle of titles must land [Certain]. PRC game regulation and VIE/listing risk can reset the multiple overnight and is not something fundamentals warn of in advance [Likely]. Insiders hold 45.32%, so minority holders have little say on capital allocation [Certain]. Results on Nov 19 are a near-term event risk [Certain].
## Bull case
Quality is still improving: operating margin rose from 18.7% (FY2021) to 35.2% TTM, gross margin to 67.2%, FCF margin to 43.5% with FCF conversion of 156.0% [Certain]. EV/EBITDA of 9.1x is below its own 5y minimum of 9.3x and about half the peer median of 17.6x; P/FCF of 11.0x sits near its 5y low of 10.7x at a 9.13% FCF yield [Certain]. The reverse DCF implies -1.8% revenue growth, which a business still expanding margins and returns does not show [Likely]. Net cash (net debt/EBITDA -3.76x), Altman Z 8.53 and monthly buybacks limit balance-sheet risk [Certain]. Every existing thesis trigger is comfortably clear [Certain].
## Decision
```json
{
  "ticker": "HKG:9999",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A net-cash games franchise with operating margin up to 35.2% and a 43.5% FCF margin trades below its own 5-year minimum EV/EBITDA and near its P/FCF low, where the price implies a revenue decline its improving fundamentals do not show.",
  "rationale": "Thesis intact and every trigger clear; multiples remain at the bottom of their own range. But the base fair value gap has narrowed and the bear value sits well below the price, so the skew no longer justifies adding ahead of Nov 19 results. Keep the existing size; no trim warranted while quality keeps rising.",
  "price_at_decision": 200.40,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-9999/2026-11-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2024 level of 28.1%, reversing the five-year expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28.1}},
    {"text": "TTM FCF margin falls below the FY2024 level of 36.5%, signalling cash generation is no longer keeping pace.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 36.5}},
    {"text": "TTM gross margin falls below the FY2024 level of 62.5%, indicating game-portfolio mix or monetization is deteriorating.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 62.5}},
    {"text": "A new PRC regulation materially restricts game monetization, or a VIE-related regulatory action forces deconsolidation, as disclosed in a company filing or release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 247.35, "basis": "Margin expansion continues and multiples recover toward their 5y medians (EV/EBITDA 10.4x [RA]), matching the mechanical bull fair value of 247.35 [IS,CF,RA]."},
    "base": {"probability": 0.5, "target_price_12m": 220.11, "basis": "Margins hold near TTM levels (operating 35.2% [IS]) and the market drops the implied -1.8% revenue decline, reaching the mechanical base fair value of 220.11 [IS,CF,RA]."},
    "bear": {"probability": 0.25, "target_price_12m": 145.25, "basis": "A weak title cycle or PRC regulatory action compresses margins and multiples, as in the mechanical bear fair value of 145.25 with the 3.5% China premium [IS,CF,RA]."}
  },
  "entry_price": 176.09,
  "entry_basis": "valuation file: base 220.11 x 0.8; at that level the same evidence would justify adding.",
  "replaces": null,
  "replacement_reason": null
}
```

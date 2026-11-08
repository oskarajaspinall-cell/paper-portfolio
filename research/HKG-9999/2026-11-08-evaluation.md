# Evaluation: NetEase, Inc. (HKG:9999) — 2026-11-08
## Bear case
The upside is thin: base fair value of 220.11 HKD is only +9.8% above the 200.40 close, and the mechanical bear of 145.25 sits -27.5% below, so the skew is only moderately favourable [Certain]. P/E of 17.2x is a +21% premium to the peer median [Certain]. China risk is real and unpriced by fundamentals: game-licensing rules or a VIE action could hit monetisation abruptly; the macro overlay rates macro as context only, with CNY and the HKD peg stable, so the country risk is regulatory rather than currency [Likely]. No Direction change line fired, but FCF margin (43.5%) sits below its 45.0% 2-year high and trailing ROIC (340.3%) is a small-capital-base artefact, not evidence of improvement [Certain]. Results on Nov 19, 2026 are binary event risk for a hit-driven pipeline; the stock is -7.8% over 12 months with the 50-day below the 200-day [Certain].
## Bull case
Fundamentals are still improving on the rolling view, not just fiscal-year endpoints: operating margin +3.8pp to 35.2%, ROCE +1.5pp to 23.3%, FCF margin +2.3pp, all at or near 2-year highs [Certain]. Gross margin rose to 67.2% and FCF conversion is 156.0% of net income, with net cash (net debt/EBITDA -3.76x) [Certain]. On cash measures it is cheap: EV/EBITDA 9.1x is below its 5y minimum of 9.3x and 56% under peers, P/FCF 11.0x is near its 10.7x low, FCF yield 9.13% [Certain]. The reverse DCF implies -1.8% year-1 revenue growth, which a diversified live-service portfolio with rising margins does not show [Likely]. Monthly buybacks continue and dilution is slight at 0.39% [Certain]. The 3.5% China premium is already inside the fair value, so the discount is not double-counted [Likely].
## Decision
```json
{
  "ticker": "HKG:9999",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A net-cash games franchise with operating margin rising to 35.2% and a 43.5% FCF margin trades below its own 5-year minimum EV/EBITDA and near its P/FCF low, where the price implies a revenue decline its improving fundamentals do not show.",
  "rationale": "The thesis is intact and the last-12-month trend confirms it: margins and ROCE at 2-year highs, net cash, cheap cash multiples. Modest base fair-value upside, China regulatory risk and Nov 19 results keep this a hold at conviction 4, not an add; the current size stands.",
  "price_at_decision": 200.40,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-9999/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below the FY2024 level of 28.1%, reversing the five-year expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28.1}},
    {"text": "TTM FCF margin falls below the FY2024 level of 36.5%, signalling cash generation is no longer keeping pace.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 36.5}},
    {"text": "TTM gross margin falls below the FY2024 level of 62.5%, indicating game-portfolio mix or monetization is deteriorating.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 62.5}},
    {"text": "A new PRC regulation materially restricts game monetization, or a VIE-related regulatory action forces deconsolidation, as disclosed in a company filing or release."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 247.35, "basis": "Operating margin keeps rising from 35.2% [IS-T] and EV/EBITDA recovers from 9.1x toward its 5y median 10.4x [RA]: the mechanical bull fair value 247.35 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 220.11, "basis": "Margins hold near TTM levels with FCF conversion of 156.0% [CF,IS] and the price-implied -1.8% growth proves too pessimistic: the mechanical base fair value 220.11 [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 145.25, "basis": "A weak new-title cycle or PRC licensing tightening (note section 6) pulls FCF margin back toward the FY2024 36.5% [CF,IS]: the mechanical bear fair value 145.25 with the 3.5% China premium [fact sheet Fair value]."}
  },
  "entry_price": 176.09,
  "entry_basis": "valuation file: base 220.11 x 0.8; at that level the same evidence would justify adding at conviction 4 with a full margin of safety.",
  "replaces": null,
  "replacement_reason": null
}
```

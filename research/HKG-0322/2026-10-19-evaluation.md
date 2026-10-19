# Evaluation: Tingyi (Cayman Islands) Holding Corp. (HKG:0322) — 2026-10-19
## Bear case
Tingyi is a low-margin staples business: net margin is only 5.9% TTM and has barely moved in five years (+0.6pp) [Certain], so a small reversal in the gross-margin gains (35.4% TTM vs 28.6% in FY2022) would erase much of the earnings [Likely]. Nongfu Spring and others are disrupting bottled water and tea pricing [Likely], and the fact sheet shows no revenue-growth evidence to counter the reverse DCF's implied -3.7% year-1 decline [Certain]. TTM ROIC of 35.6% sits far above the FY2025 22.3%, which may be a cyclical peak rather than a new base [Guessing]. The mechanical bear fair value of 6.40 is far below the price, and the base case offers only +23.1% [Certain]. Dividend policy is [data unavailable] in the research, so capital returns cannot be credited [Certain]. Low institutional ownership (13.4%) limits any re-rating catalyst [Guessing].
## Bull case
Five years of rising quality: ROIC 16.7% to 22.3%, ROE 18.6% to 28.7%, operating margin 5.5% to 7.8% (8.4% TTM) [Certain]. FCF conversion has stepped up to 124.2% of net income and the balance sheet is net cash (-0.23x) [Certain]. Yet the stock trades below its own 5-year minimum P/E (13.0x vs 13.3x), EV/EBITDA (5.9x vs 6.8x) and P/FCF (10.4x vs 11.3x), at a 9.59% FCF yield and deep discounts to peers on P/E and EV/EBITDA [Certain]. The price implies shrinking revenue that the margin trend does not show [Likely]. Beta of 0.13 makes it a diversifier, and the macro overlay finds no transmission from US rates or the dollar [Likely]. If margins merely hold, a return toward the 5y median P/E of 15.6x gives a solid return [Likely].
## Decision
```json
{
  "ticker": "HKG:0322",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash Chinese noodle and beverage leader with five years of rising ROIC and margins trades below its own 5-year minimum P/E and EV/EBITDA at a 9.59% FCF yield, but thin net margins, unproven revenue growth and intense beverage competition make the skew good rather than compelling.",
  "rationale": "Quality and cash conversion are improving and the multiple is cheap, but base upside is modest, the mechanical bear sits far below the price, net margin is thin and barely improved, revenue growth is unevidenced and TTM ROIC may be peaking. Good but not compelling: conviction 3, AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 12.37,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-0322/2026-10-19.md",
  "triggers": [
    {"text": "TTM gross margin falls below 30%, giving back the FY2022-TTM recovery from 28.6% to 35.4% and signalling pricing/input-cost gains have reversed under competition.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 15%, under the FY2021 level of 16.7%, giving up the five-year improvement.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA rises above 1.0x (-0.23x TTM), ending the net-cash position.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Annual revenue (income statement) declines in two consecutive fiscal years, confirming the reverse-DCF shrinkage case."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 16.43, "basis": "Margin expansion continues and the price converges on the blended bull fair value of 16.43 (DCF 15.27, P/E 18.74) [IS,RA,ST], consistent with the rising ROIC and gross margin trend [RA,IS]."},
    "base": {"probability": 0.45, "target_price_12m": 14.84, "basis": "Margins hold and P/E returns to its 5y median of 15.6x [RA] on TTM earnings (13.0x now [RA]), slightly below the mechanical base 15.23 because revenue growth is unevidenced and the reverse DCF implies -3.7% [ST]."},
    "bear": {"probability": 0.30, "target_price_12m": 9.42, "basis": "Beverage price competition from Nongfu Spring (note section 2) reverses gross-margin gains and the price revisits its 52-week low of 9.42 [HI]; held above the mechanical bear 6.40 because the net-cash balance sheet (-0.23x [RA]) and FCF conversion cushion downside."}
  },
  "entry_price": 12.18,
  "entry_basis": "valuation file: base 15.23 x 0.8; at that level the same rising-quality, net-cash evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

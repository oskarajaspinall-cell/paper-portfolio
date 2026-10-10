# Evaluation: STERIS plc (STE) — 2026-10-10
## Bear case
The price already assumes far more growth than STERIS delivers. Reverse DCF implies 15.7% year-one revenue growth versus roughly 7% reported last quarter [Certain] (factsheet Fair value; Q1 FY2027 transcript [OV]). Both mechanical methods sit below the price: base DCF 139.13 and blended base 176.90, 17.5% under the 214.40 close [Certain]. Looking "below its 5y minimum" mostly reflects a 58.7x median P/E inflated by depressed FY2022–23 earnings, so it says little about cheapness [Likely]. Versus peers, EV/EBITDA is +2%, P/FCF +8% and P/B +16% [Certain]: no discount. TTM ROIC of 9.7% [RA] barely covers a cost of equity near 10% (5.22% risk-free plus beta × 5% ERP) [Likely]. The $600m chemistries plant and restructuring add capex and execution risk while FCF margin has already slipped from 16.4% to 15.3% TTM [Certain]. Relative strength is -27.2pp vs SPY over 12m [Certain].
## Bull case
Quality is improving steadily. ROIC rose from 7.1% to 9.7%, ROCE from 6.5% to 12.2% and operating margin from 16.1% to 19.0% [Certain] [RA, IS]. Net debt/EBITDA fell from 2.64x to 0.95x and the Piotroski F-score is 7 [Certain]. Recurring consumables and service revenue tied to an installed base of sterilizers creates switching costs [Likely] (steris.com/about). Q1 FY2027 beat on EPS with 7% revenue growth and margin expansion, and management targets double-digit bottom-line growth [Likely] (transcripts [OV]). P/E of 26.2x is 17% below the peer median of 31.6x [Certain]. With earnings compounding at double digits, a flat multiple still yields a mid-teens return, and a re-rating towards peers adds upside [Guessing].
## Decision
```json
{
  "ticker": "STE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A steadily improving, deleveraging sterilization-consumables franchise whose ~10% ROIC and ~7% growth do not yet justify a price implying 15.7% growth and sitting 17.5% above base fair value.",
  "rationale": "Quality trend is genuine, but ROIC barely clears the cost of capital, the stock is not cheap versus peers on EV/EBITDA, P/FCF or P/B, and the reverse DCF demands roughly twice the delivered growth. Good but not compelling: conviction 3, no position; cash is acceptable.",
  "price_at_decision": 214.40,
  "price_date": "2026-10-09",
  "research_note": "research/STE/2026-10-10.md",
  "triggers": [
    {"text": "TTM ROIC falls below 8%, back under the FY2024 level of 7.7%-8.4%, reversing the five-year improvement.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "TTM operating margin falls below 17%, under the FY2024 level of 17.6%, undoing the margin expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "TTM FCF margin falls below 11.9%, the FY2024 level, showing the $600m chemistries build and restructuring are eroding cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 11.9}},
    {"text": "Organic revenue growth in quarterly earnings releases falls below mid-single digits for two consecutive quarters, contradicting management's mid-to-high single-digit target."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 258.0, "basis": "P/E re-rates from 26.2x to the 31.6x peer median [RA, P:BDX/DHR/SYK/BAX] as double-digit EPS growth targets are met (Morgan Stanley transcript 2026-09-15 [OV]); sits below the 388.11 bull fair value because that relies on the inflated 5y P/E history."},
    "base": {"probability": 0.45, "target_price_12m": 215.0, "basis": "P/E holds near 26.2x [RA] with operating margin around 19.0% [IS]; above the 176.90 base fair value because the mechanical DCF uses history-based growth below the ~7% organic growth reported in Q1 FY2027 [OV]."},
    "bear": {"probability": 0.30, "target_price_12m": 176.9, "basis": "The price converges to the 176.90 blended base fair value as the market stops paying for the 15.7% reverse-DCF growth [factsheet Fair value] and restructuring dilutes the 15.3% TTM FCF margin [CF, IS]."}
  },
  "entry_price": 141.52,
  "entry_basis": "valuation file: base 176.90 x 0.8 (20% margin of safety); at that level the same quality evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

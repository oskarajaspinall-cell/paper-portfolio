# Evaluation: Fast Retailing Co., Ltd. (TYO:9983) — 2026-11-23
## Bear case
The business is excellent but the price already assumes perfection [Certain]. P/E of 46.6x, P/B 8.9x and P/FCF 35.6x all sit above their own 5-year maxima, and P/E is +110% versus peers [Certain]. The mechanical base fair value of 46,024.04 JPY is -44.0% from the close, and even the bull case is -20.9% [Certain]. The reverse DCF needs 24.3% year-1 revenue growth, well above anything plausible for a mature apparel retailer [Likely]. The price is +12.1% above its 200-day average after +52.6% in 12 months: an extended price risks a sharp de-rating back toward the 5y median P/E of 34.7x if growth merely slows [Likely]. Greater China is material and Beijing-Tokyo tension is unverified but live (macro overlay) [Guessing]. FCF conversion is falling over five years (-8.2pp) and dipped to 102.8% in FY2025 [Certain].

## Bull case
Quality is top-tier and still improving on the rolling 12 months [Certain]: ROIC 38.1% vs 32.4% a year earlier, operating margin 18.4% vs 16.4%, FCF margin 17.9% vs 13.1% (RA-T, IS-T, CF-T). Net cash (net debt/EBITDA -1.55x), Altman Z 10.06, Piotroski 7 and no dilution [Certain]. A fifth consecutive record annual profit with strength in all regions, and guidance for further growth (fact-sheet headlines) [Likely]. Scale in sourcing and a single global basics range give a durable cost and brand edge [Likely]. Founder-aligned ownership (insiders 37.52%) [Likely]. The trend is strong: +17.3pp versus SPY over 3 months with beta 0.47 [Certain].

## Decision
```json
{
  "ticker": "TYO:9983",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "ROIC, operating margin and FCF margin all rise over 1 and 3 years on the rolling-12-month table [RA-T, IS-T, CF-T].", "moat": "narrow", "key_risk": "high", "key_risk_text": "De-rating: P/E 46.6x above its 5y max of 41.0x and the reverse DCF implies 24.3% year-1 growth; any slowdown likely compresses the multiple sharply.", "veto": null},
  "thesis": "A best-in-class, net-cash apparel compounder whose improving returns are already more than priced in at multiples above their own 5-year range.",
  "rationale": "Quality, direction and balance sheet are excellent, but the value blend sits far below the price and every multiple is above its own 5y max, so trend strength earns no valuation points. Good but not compelling at this price; cash is acceptable.",
  "price_at_decision": 82220.00,
  "price_date": "2026-11-20",
  "research_note": "research/TYO-9983/2026-11-23.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 16%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 16}},
    {"text": "ROIC (TTM) falls below 30%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "Gross margin falls below 52%", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 52}},
    {"text": "FCF margin (TTM) falls below 12%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 88690, "basis": "Margins keep rising (operating margin 18.4% vs 16.4% a year earlier [IS-T]) and the market holds P/E above its 5y max, retesting the 52-week high of 88,690.00 [HI]; above the mechanical bull of 65,021.72 because the market already pays well above its history."},
    "base": {"probability": 0.45, "target_price_12m": 76000, "basis": "Earnings keep growing but P/E of 46.6x drifts back toward its 5y max of 41.0x [RA], roughly offsetting growth; well above the base fair value of 46,024.04 because the mechanical range ignores the improved ROIC of 38.1% [RA-T]."},
    "bear": {"probability": 0.30, "target_price_12m": 53650, "basis": "Growth slows against the 24.3% the reverse DCF implies and P/E de-rates toward its 5y median of 34.7x [RA], back to the 52-week low of 53,650.00 [HI]; still above the bear fair value of 35,091.27 given net cash and record profits."}
  },
  "entry_price": 39120.43,
  "entry_basis": "valuation file: base 46,024.04 x 0.85"
}
```

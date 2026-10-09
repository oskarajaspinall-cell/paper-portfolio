# Evaluation: Western Digital Corporation (WDC) — 2026-10-09
## Bear case
WDC is earning peak-cycle returns in a business with a history of collapse: ROIC is 52.9% TTM, but it was -2.2% in FY2023 and 0.7% in FY2024 [Certain]. The margin surge reflects an AI/cloud HDD shortage, not a structural moat [Likely], and Toshiba's reported push for TDK's heads business threatens the supply discipline behind pricing [Likely]. Cloud is 89% of revenue and three customers are each ≥10%, so a hyperscaler capex pause hits fast [Certain]. The cheap-looking 16.2x P/E is flattered by a 72.9% net margin against a 35.8% operating margin [Likely]. On cash flow the stock is expensive: 41.9x P/FCF (+74% vs peers), a 2.38% FCF yield, and FCF conversion down to 37.3% [Certain]. The base fair value of 134.18 is 65.9% below the 393.31 close, and the bull of 421.84 is only 7.3% above it [Certain]. Beta is 2.17 [Certain].
## Bull case
The HDD market is a three-player oligopoly [Certain], and demand for AI data storage is still running ahead of supply [Likely]. Management guided 42-49% YoY Q1 FY27 revenue growth, close to the 48.1% the reverse DCF implies, so near-term numbers may justify the price [Likely]. The balance sheet is net cash (-0.08x net debt/EBITDA), the Altman Z is 13.24, and FY2026 buybacks were $2.592bn, which cushions any downturn [Certain]. The stock is well off its 52-week high of 799.87 and 14.6% below its 50-day average, and short interest fell 13.1% [Certain]. Results on Oct 22 could reset the story [Guessing]. Even so, this is a bet on how long the cycle lasts, not on value in hand.
## Decision
```json
{
  "ticker": "WDC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A net-cash HDD oligopolist earning peak-cycle returns on an AI storage shortage, priced near its own-history bull fair value and expensive on cash flow, so the risk of mean reversion outweighs the near-term growth.",
  "rationale": "Core needs a good business at an attractive price. Returns are cyclical (FY2023-24 ROIC near zero). The bull fair value of 421.84 offers only 7.3% upside, against a base 65.9% below. P/FCF is 41.9x with a 2.38% FCF yield, FCF conversion is falling, and new Toshiba capacity threatens pricing. Conviction 2 means no position.",
  "price_at_decision": 393.31,
  "price_date": "2026-10-08",
  "research_note": "research/WDC/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin falls below the FY2025 level of 38.8%, signalling the HDD supply shortage is easing.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 38.8}},
    {"text": "TTM operating margin falls below the FY2025 level of 22.4%, confirming pricing power is fading.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22.4}},
    {"text": "TTM ROIC falls below the FY2022 level of 11.5%, back into its pre-shortage range.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 11.5}},
    {"text": "A 10-K/10-Q or earnings release reports that one of the three ≥10%-of-revenue customers was lost or materially cut orders."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 495.49, "basis": "Guided 42-49% Q1 FY27 revenue growth (SEC 8-K ex. 99.1, research note) holds while the oligopoly keeps pricing, taking the stock back to its 2026-09-09 swing high of 495.49 [HI], above the bull fair value of 421.84 because the shortage lasts longer than the 5y-average normalisation assumes."},
    "base": {"probability": 0.45, "target_price_12m": 291.0, "basis": "P/E reverts from 16.2x to its 5y median of 12.0x [RA] on roughly flat TTM earnings, as near-term growth offsets the non-operating boost (72.9% net vs 35.8% operating margin [IS]); this lands between base (134.18) and bull (421.84) fair value because the near-term growth is visible in guidance; the macro overlay's neutral/small tilt (research/WDC/2026-10-09-macro.md) leaves this unchanged."},
    "bear": {"probability": 0.30, "target_price_12m": 134.18, "basis": "Toshiba/TDK capacity additions (invezz.com 2026-10-06 per note) and a hyperscaler capex pause take margins back toward their 5y average, so the price converges on the fact sheet's base fair value of 134.18 [IS,BS,CF,RA,ST,HI]; the mechanical bear of -17.38 is not meaningful for a net-cash company."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

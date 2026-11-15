# Evaluation: APA Corporation (APA) — 2026-11-15
## Bear case
APA is a commodity price-taker with no moat beyond its cost position [Likely]. Returns are cyclical: ROIC fell from 43.8% (FY2023) to 14.0% (FY2025) before recovering to 23.0% TTM [RA]. The Direction change lines (ROIC, ROCE, operating and FCF margin rising over 12 months against a falling 5-year trend) reflect commodity prices and cost cuts, not a better business [Likely]; the cost-savings lever is one-off [company-reported] (https://www.sec.gov/Archives/edgar/data/1841666/000184166626000071/apa-20260930.htm). Low multiples sit on near-cycle-high earnings [Likely]. The stock is up 102.8% in 12 months and 25.0% above its 200-day average [ST,HI]: an extended price risks a sharp de-rating if oil eases [Likely]. Egypt cost-recovery volumes fall as prices rise [Certain], and Egypt's currency and politics are unverified (macro overlay). Price sits at base fair value 48.80 with bear 38.46 below [Certain]; reserve NAV is [data unavailable]. The 10-Q dropped its decommissioning risk factor unexplained [Guessing].
## Bull case
The balance sheet is the strongest in five years: net debt/EBITDA fell from 1.67x (FY2021) to 0.53x TTM [BS,IS] [Certain]. A 12.81% FCF yield [ST] funds dividends, buybacks (shares -2.69% YoY [ST]) and debt repayment; nine-month debt repaid was $1.2 billion [company-reported] (https://www.sec.gov/Archives/edgar/data/1841666/000184166626000071/apa-20260930.htm) [Certain]. Q3 lifted the FY2026 FCF outlook (https://stockanalysis.com/stocks/apa/transcripts/726549-q3-2026/) [Likely]. Piotroski F 8 and beta 0.28 [ST] [Certain]. EV/EBITDA 3.1x sits 27% up its 5y range and 43% below peers [RA] [Certain]. The trend is working: 50-day 19.2% above the 200-day, relative strength vs SPY +92.4pp over 12 months [ST,HI] [Certain]. Suriname (GranMorgu), Alaska and Uruguay exploration is optionality the multiple ignores [Guessing].
## Decision
```json
{
  "ticker": "APA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 5y and 3y declines in ROIC and operating margin are a commodity peak-to-trough (FY2022-23 highs) with the balance sheet intact (net debt/EBITDA 0.53x TTM [BS,IS]); all four metrics have risen over the last 12 months [RA-T,IS-T,CF-T], tracking prices and cost cuts (sec.gov 10-Q).",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "Oil and gas prices ease, taking TTM EBITDA back toward FY2024-25 levels and de-rating a stock that has doubled and trades well above its 200-day average.",
    "veto": null
  },
  "thesis": "A deleveraged, cash-generative E&P in a strong uptrend, but its returns track the commodity cycle with no moat and the price already sits at base fair value on near-cycle-high earnings.",
  "rationale": "Strong balance sheet, high FCF yield and a working trend, but returns are cyclical, there is no moat and the price has reached base fair value with the bear value well below. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 48.44,
  "price_date": "2026-11-13",
  "research_note": "research/APA/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, under the FY2024-25 levels of 14.4%/14.0%, showing returns have reset to the cycle trough or worse.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 15% (22.6% now), meaning cash no longer comfortably funds buybacks and debt reduction.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 30% (43.3% now), under the FY2025 level of 30.8%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "Net debt/EBITDA on the ratios page rises above 1.5x (0.53x TTM now), reversing the deleveraging."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 52.86, "basis": "EV/EBITDA re-rates to the bull fair value of 52.86 [IS,BS,RA] as TTM EBITDA holds and buybacks continue (shares -2.69% YoY [ST])."},
    "base": {"probability": 0.45, "target_price_12m": 48.8, "basis": "Mechanical base fair value of 48.80 on EV/EBITDA near its 5y median 3.2x [RA]; macro overlay weight is context, so no adjustment."},
    "bear": {"probability": 0.35, "target_price_12m": 38.46, "basis": "Returns revert toward FY2024-25 ROIC of 14.4%/14.0% [RA] as commodity prices ease, giving the bear fair value of 38.46 on EV/EBITDA [IS,BS,RA]."}
  },
  "entry_price": 39.04,
  "entry_basis": "valuation file: base 48.80 x 0.8 (20% margin of safety), which would offset the commodity-cycle risk to near-peak earnings.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Alphabet Inc. (GOOGL) — 2026-11-16
## Bear case
The AI capex build is consuming the cash engine: FCF margin fell from 19.1% to 4.2% in 12 months and FCF conversion is 8.4% TTM, so the stock trades at 184.1x FCF and a 0.54% FCF yield [Certain]. The Direction change lines are real: ROIC 31.5% to 23.8% and ROCE 28.4% to 18.1% as net PP&E jumped [company-reported]; whether that capital earns its cost is unproven [Guessing]. The 15.1x P/E flatters, since a 50.0% net margin against a 33.3% operating margin points to non-operating gains [Likely]. Capex is now externally funded (senior notes, ATM equity, new guarantees and repurchase obligations in the 10-Q) [Certain]. Mechanical fair value base 256.59 sits below the price [Certain]. AI search and Amazon shopping search contest the core franchise [Guessing]. The price is 12.6% below its 200-day average with 6-month momentum of -25.5%: no trend support [Certain].

## Bull case
Operations are not weakening: operating margin is at its 2-year high of 33.3% and gross margin 60.9%, both rising over five years [Certain]. The returns decline is a heavy-investment denominator effect, not lost share [Likely]. A $567.7bn revenue backlog, just over 55% recognised within 24 months [company-reported], gives visibility that Cloud/TPU capacity will be monetised [Likely]. The balance sheet is net cash (net debt/EBITDA -0.62x) and dilution is only 0.33% YoY [Certain]. Search distribution, data, YouTube and TPU scale form a wide moat [Likely]. If capex peaks, FCF snaps back towards the FY2025 18.2% margin and the stock re-rates [Guessing].

## Decision
```json
{
  "ticker": "GOOGL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC, ROCE and FCF margin fall while operating margin rises to its 2-year high of 33.3% [IS-T]; the 10-Q shows net PP&E rising from $246.6bn to $372.8bn [company-reported] (https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm): heavy investment, not lost share, though its return is unproven.",
    "moat": "wide",
    "key_risk": "high",
    "key_risk_text": "The AI capex build fails to earn its cost of capital, leaving FCF depressed and returns structurally lower, while AI search erodes the core ad franchise.",
    "veto": null
  },
  "thesis": "A wide-moat franchise with rising operating margins whose free cash flow has been absorbed by an externally funded AI capex build, trading above its mechanical fair value with no trend support until the capex earns a visible return.",
  "rationale": "Operations are strong and the decline is investment-driven, but FCF yield is 0.54%, the price sits above base fair value 256.59 and below its 200-day average, so neither a discount nor trend strength supports a buy. Good but not compelling: AVOID; cash is acceptable.",
  "price_at_decision": 295.77,
  "price_date": "2026-11-13",
  "research_note": "research/GOOGL/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 30%, showing the AI transition is eroding the core franchise's profitability rather than just its cash flow.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM ROIC falls below 18%, showing the capex build keeps diluting returns without matching earnings.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "TTM FCF margin turns negative, meaning the capex build outruns operating cash flow entirely.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Net debt/EBITDA (debt minus cash and short-term investments, ratios page) turns positive above 0.5x from -0.62x TTM, i.e. capex is funded by leverage."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 338.23, "basis": "Backlog of $567.7bn [company-reported] (https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm) converts and FCF margin recovers towards the FY2025 18.2% [CF], so the price regains its 200-day average of 338.23 [ST], above the mechanical bull 278.04 because the EV/Revenue method ignores a capex peak."},
    "base": {"probability": 0.5, "target_price_12m": 256.59, "basis": "EV/Revenue fair value base 256.59 [fact sheet Fair value] as FCF stays depressed by capex and P/FCF at 184.1x [RA] limits multiple support."},
    "bear": {"probability": 0.25, "target_price_12m": 152.61, "basis": "EV/Revenue fair value bear 152.61 [fact sheet Fair value] if ROIC keeps falling from 23.8% [RA-T] and AI search erodes ad revenue."}
  },
  "entry_price": 205.27,
  "entry_basis": "valuation file: base 256.59 x 0.8; at that discount the investment-driven FCF dip would be priced in, though a visible FCF recovery would matter as much as price.",
  "replaces": null,
  "replacement_reason": null
}
```

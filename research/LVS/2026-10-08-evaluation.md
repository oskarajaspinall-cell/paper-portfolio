# Evaluation: Las Vegas Sands Corp. (LVS) — 2026-10-08
## Bear case
The stock is down 31.5% in 12 months with RSI 19 and short interest up 11.8% month-on-month, and the research does not explain the fall [Certain]. Since FX and rates barely moved, the drawdown points to Macao-specific demand or share loss that has not yet reached the TTM figures [Likely]. Macao EBITDA was hit by low VIP hold, and renovations take ~400-500 keys offline per quarter into 2027 [Likely]. The discount is narrow: on P/FCF (8.6x vs 5.0x) and EV/Sales (2.6x vs 2.0x) LVS is dearer than WYNN/MGM/MLCO [Certain]. The 5y P/E range is set by recovery years, so "below its 5y minimum" overstates the cheapness [Likely]. Buybacks run alongside 2.57x net debt/EBITDA, and P/B is 39.9x, so there is little equity cushion if EBITDA slips [Certain]. Earnings on Oct 21 could reset the base [Guessing].

## Bull case
LVS holds one of six Macao concessions (to 2032) and one of two Singapore licences (no third before 2031), so statutory scarcity protects returns [Certain]. TTM ROIC is 19.8%, operating margin 23.3% and FCF margin 19.7%, all far above pandemic levels [Certain]. At 13.9x P/E and 7.6x EV/EBITDA, about 23% below peer medians, with an 11.65% FCF yield, the market prices a lasting Macao impairment [Likely]. Share count is down 6.01% YoY and $787m was repurchased in Q2 2026, so per-share value compounds without a re-rating [Certain]. Marina Bay Sands posted $689M Q2 EBITDA, which anchors cash flow [Certain]. The macro overlay finds CNY firmer and the HKD peg intact, so the selloff is not macro-driven [Likely].

## Decision
```json
{
  "ticker": "LVS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A licence-protected Macao/Singapore resort operator with 19.8% ROIC and an 11.65% FCF yield trades below peers on earnings multiples, but an unexplained Macao-driven 31.5% drawdown, a pricier P/FCF than peers and 2.57x leverage make the discount a fair price rather than a mispricing.",
  "rationale": "Quality and licences are real, but the cheapness is mixed: dearer than peers on P/FCF and EV/Sales. The drawdown's cause is unidentified, and Q3 results land on Oct 21. The probability-weighted 12m value is roughly the current price. Good, not compelling, so conviction is 3 and we avoid it under the owner rule.",
  "price_at_decision": 35.81,
  "price_date": "2026-10-07",
  "research_note": "research/LVS/2026-10-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, reversing the post-2022 recovery (would confirm structural Macao impairment).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Debt/EBITDA rises above 4x, signalling EBITDA deterioration or buybacks outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4}},
    {"text": "TTM operating margin falls below 21.7%, the FY2024 level, showing renovation disruption or share loss is eroding profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 21.7}},
    {"text": "Positive re-assessment: Macao quarterly EBITDA in the Q3/Q4 2026 earnings releases trends clearly toward management's ~$700m/quarter target, showing Macao weakness reflects hold and renovations rather than share loss."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 46.37, "basis": "Macao volumes recover and P/E re-rates from 13.9x to the 18.0x peer median [RA,P:WYNN,P:MGM,P:MLCO] on flat TTM earnings."},
    "base": {"probability": 0.5, "target_price_12m": 38.10, "basis": "P/E holds at 13.9x [RA] while the 6.01% YoY share reduction [ST] lifts per-share earnings; macro overlay (research/LVS/2026-10-08-macro.md) tilt is neutral/small, so probabilities are unchanged."},
    "bear": {"probability": 0.25, "target_price_12m": 20.82, "basis": "Macao share loss suspected in the Bear case drives LVS to the 5.0x peer-median P/FCF from 8.6x [RA,P:WYNN,P:MGM,P:MLCO]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

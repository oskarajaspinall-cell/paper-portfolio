# Evaluation: Paycom Software, Inc. (PAYC) — 2026-11-17
## Bear case
The price has already done the work: the shares are 49.7% above the 200-day average after an 83.0% six-month gain, and the base fair value of 260.07 sits only +2.1% above the 254.75 close [Certain]. An extended price risks a de-rating if growth slows: the reverse DCF already asks for 10.2% year-1 revenue growth [Certain]. Margins are at their two-year highs, and the 10-Q ties part of the gain to lower headcount, a one-time lever that cannot repeat indefinitely [Likely]. Buybacks are now debt-funded ($750.0 million [company-reported] on the revolver), moving net debt/EBITDA from -0.44x to 0.75x while buying near fair value [Certain]. FCF conversion has fallen 11.4pp over five years and Piotroski F is 5 [Certain]. Interest income on corporate funds fell, and a rate-cut cycle would trim float income [Likely]. Rising real yields are a multiple headwind (macro: context only) [Likely].

## Bull case
This is a good business that is working. ROIC 39.3%, operating margin 33.9% and FCF margin 30.1% are all rising on the rolling 12 months (+9.4pp, +6.0pp, +10.4pp), not just on fiscal-year endpoints [Certain]. Payroll is embedded in clients' workflows on a single database, a switching-cost moat [Likely]. Despite the rally, P/E 23.9x and EV/EBITDA 14.1x sit at 4% and 1% of their five-year ranges and 13% and 30% below peers; P/FCF 16.9x is below its five-year minimum, a 5.91% FCF yield [Certain]. Q3 brought higher FY26 guidance [Likely]. Shares are down 12.61% year on year, compounding per-share value, and leverage stays modest [Certain]. Relative strength vs SPY is +39.1pp over 12 months with RSI at 49.6, so the trend is strong without being overbought [Certain].

## Decision
```json
{
  "ticker": "PAYC",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no falling ROIC, operating margin or FCF margin: rolling 12 months ROIC +9.4pp, operating margin +6.0pp, FCF margin +10.4pp [RA-T, IS-T, CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Peak margins plus an extended price (49.7% above the 200-day average, reverse DCF implying 10.2% growth): if growth slows or cost-cut gains fade, the stock de-rates, amplified by debt-funded buybacks.",
    "veto": null
  },
  "new_evidence": {"type": "method_change", "text": "The earlier AVOID 3 predates a scorecard rule change (trend-strength valuation points); re-scored under today's rules it lands on the other side of the buy line. The business evidence itself is unchanged."},
  "thesis": "A high-return, switching-cost payroll franchise with rising rolling margins and ROIC trades at the bottom of its own 5-year earnings multiples and below peers while in a strong uptrend, with buybacks compounding per-share value.",
  "rationale": "Scorecard sets conviction 4: top-tier and rising returns, modest leverage, and valuation points from trend strength with own-history multiples near their lows. Python sets the volatility-scaled size. Cash after the pending RELY order cannot fund it above the 1.5% floor, so conviction-3 JKHY is replaced.",
  "price_at_decision": 254.75,
  "price_date": "2026-11-16",
  "research_note": "research/PAYC/2026-11-17.md",
  "triggers": [
    {"text": "TTM operating margin falls below 27% (33.9% now), back under the FY2021-25 band, showing the cost-cut margin gain was transitory.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 27}},
    {"text": "TTM ROIC falls below 30% (39.3% now), under the FY2025 level of 30.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "TTM gross margin falls below 84% (88.4% now), showing pricing or mix pressure.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 84}},
    {"text": "TTM FCF margin falls below 20% (30.1% now), back to the FY2025 level, or net debt/EBITDA on the ratios page rises above 2.0x as buybacks lean further on debt.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 354.14, "basis": "Rising margins hold and growth beats the 10.2% the reverse DCF implies, matching the DCF bull value of 354.14 [IS, CF, RA]."},
    "base": {"probability": 0.5, "target_price_12m": 260.07, "basis": "Margins hold near the TTM 33.9% and the price converges on the blended base fair value of 260.07 [IS, BS, CF, RA, ST, HI]."},
    "bear": {"probability": 0.25, "target_price_12m": 170.86, "basis": "Growth slows and the extended price de-rates to the EV/Revenue bear value of 170.86; not the blended bear of 100.23, whose DCF leg assumes a collapse the rising rolling margins do not show [RA, RA-T]."}
  },
  "replaces": "JKHY",
  "replacement_reason": "JKHY is held at conviction 3 with a price that already implies growth above its own framework; PAYC clears the buy bar at conviction 4 with higher, rising returns and multiples near their 5-year lows, and cash after the pending RELY order cannot fund a full position above the 1.5% floor.",
  "entry_price": null,
  "entry_basis": null
}
```

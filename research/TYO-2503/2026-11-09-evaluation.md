# Evaluation: Kirin Holdings Company, Limited (TYO:2503) — 2026-11-09
## Bear case
The re-rating already happened: the stock is up 41.1% in 12 months and sits near its 52-week high of 3,178.00 [Certain]. The "cheap" multiples rest on a TTM that is the best in five years: operating margin 11.8% against 7.5% a year earlier and FCF margin 7.8% against 0.7% [Certain]. The Direction change line cuts both ways: five fiscal years of falling FCF margin (7.3% to 4.9%) and FCF conversion that swung from 33.4% to 222.4% show cash is lumpy, and the TTM jump may include working-capital timing or Four Roses disposal effects [Guessing]. Even at its best, ROIC of 9.5% is barely above a plausible cost of capital in a mature, shrinking-volume category [Likely]. P/B of 1.5x is above its 5y max [Certain]. Results land on Nov 11, 2026, two sessions away, and overseas exposure is unverified [Certain].
## Bull case
Every earnings multiple sits at or below its own 5y floor: P/E 12.8x against a 12.9x minimum and EV/EBITDA 7.9x against 9.0x, with a 7.92% FCF yield and discounts to peers of -23% on P/E and -36% on EV/EBITDA [Certain]. The improvement is broad, not one line: ROIC, ROCE, operating and FCF margin are all at their 2-year highs on a rolling basis, Piotroski F is 8, and net debt/EBITDA fell to 1.68x from 2.37x [Certain]. The FCF recovery is therefore more likely the 5-year decline reversing (heavy investment years ending, portfolio pruning) than a one-off [Likely]. The reverse DCF prices -1.5% revenue growth in year 1, and the mechanical base fair value of 4,053.05 is well above the price [Certain]. Entrenched Japanese brands and distribution keep margins stable [Likely].
## Decision
```json
{
  "ticker": "TYO:2503",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years: ROIC, ROCE, operating and FCF margin are all at 2-year highs on the rolling view [RA-T,IS-T,CF-T]; the 5-year FCF margin fall (7.3% to 4.9%) [CF,IS] has reversed in the last 12 months (0.7% to 7.8%) with net debt/EBITDA down to 1.68x.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "TTM margins prove a peak (disposal or working-capital effects) and revert toward FY2025 levels, removing the earnings discount; results on Nov 11, 2026 test this directly.",
    "veto": null
  },
  "thesis": "A Japanese brewer whose margins and cash flow have recovered to five-year highs trades below its own 5-year multiple floors, but returns remain modest and the recovery is unproven beyond one strong year.",
  "rationale": "Valuation is attractive and the FCF decline has reversed, but ROIC of 9.5% is modest in a mature category, the TTM may be a peak, and results are two sessions away. The scorecard gives conviction 3: good but not compelling, so AVOID; cash is acceptable.",
  "price_at_decision": 2967.00,
  "price_date": "2026-11-06",
  "research_note": "research/TYO-2503/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 9.0%, back to FY2025 levels, showing the margin recovery was not durable.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 9.0}},
    {"text": "TTM ROIC falls below 7.0%, reversing the recovery from the FY2024 low of 5.5%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 7.0}},
    {"text": "TTM FCF margin falls below 4.0%, showing the TTM cash spike was timing rather than a reversal of the 5-year decline.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 4.0}},
    {"text": "Net debt/EBITDA rises above 2.5x (1.68x TTM now), reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 4053.05, "basis": "TTM margins hold and the multiples recover toward their 5y medians (P/E 14.8x, EV/EBITDA 9.4x [RA]), reaching the mechanical base fair value; below the mechanical bull of 4,466.52 because ROIC stays modest [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 3430, "basis": "Earnings hold near TTM and P/E drifts back to its 5y median 14.8x [RA]; below the base fair value of 4,053.05 because one strong year of FCF does not yet justify the DCF's full cash assumption (EV/EBITDA cross-check 3,842.21 [IS,BS])."},
    "bear": {"probability": 0.25, "target_price_12m": 2467, "basis": "Operating margin reverts toward FY2025 9.7% [IS] on disposal or working-capital effects and the stock returns to its 6-month low of 2,467.00 [HI]; well above the mechanical bear of 1,370.60, which a collapsed DCF input drives (note section 3)."}
  },
  "entry_price": null,
  "entry_basis": "The obstacle is not price: the base fair value less 20% (4,053.05 x 0.8) is above the current price, and what holds conviction below 4 is modest ROIC and an unproven one-year margin recovery; a lower price would not change that. Re-check after a further reported period confirms the TTM margins.",
  "replaces": null,
  "replacement_reason": null
}
```

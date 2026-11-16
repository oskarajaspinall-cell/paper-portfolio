# Evaluation: TotalEnergies SE (EPA:TTE) — 2026-11-15
## Bear case
TTE is a commodity price-taker whose returns follow oil, gas and LNG prices, not a moat [Likely]. The **Direction change** lines show ROIC, ROCE, operating and FCF margin falling over five fiscal years (ROIC 16.1% FY2022 to 8.0% FY2025) but rising in the last 12 months (ROIC 8.0% to 13.9%, operating margin 11.6% to 17.0%) [Certain]. That rebound is cyclical price, not a better business, and every TTM figure sits at its 2-year high, so earnings are near a cyclical peak [Likely]. On own history it is not cheap: P/E 9.2x vs a 5y median of 7.9x, P/B 1.6x above its 5y max of 1.4x [Certain]. The price is 9.4% above its 200-day average after a +48.6% year [Certain]; if commodity prices normalise, earnings and the multiple can de-rate together. The DCF base of 159.84 EUR extrapolates peak TTM cash flow and is unreliable [Likely]. Latest Q3 results were not reviewed [Certain].
## Bull case
Even at the cycle high the balance sheet is strong: net debt/EBITDA 0.52x, Piotroski F 8 [Certain]. FCF yield 11.57% with FCF conversion 106.3% of net income funds buybacks (shares -2.31% YoY) and the dividend [Certain]. Against peers it is cheap: P/E 9.2x vs 14.8x, EV/EBITDA 4.5x vs 6.0x [Certain]. The reverse DCF already prices a 15.2% year-1 revenue fall, so a normalisation is partly in the price [Certain]. New long-term LNG contracts with ADNOC Gas and Jiangsu Guoxin support the LNG franchise [Likely]. Relative strength vs SPY is +38.2pp over 12 months with the 50-day 6.1% above the 200-day: a business that is working in an uptrend that is not overextended [Certain]. The 5-year decline is cyclical with the balance sheet intact, not structural [Likely].
## Decision
```json
{
  "ticker": "EPA:TTE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years; the 5-year falls in ROIC and margins tracked the post-2022 commodity retreat and reversed in the last 12 months (ROIC 8.0% to 13.9% [RA-T]) with leverage low (net debt/EBITDA 0.52x [ST]), a cycle rather than lost share.",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "Oil, gas and LNG prices normalise from the levels lifting TTM returns to their 2-year highs, cutting earnings while the stock's extended price (9.4% above its 200-day average after +48.6% in 12 months) de-rates.",
    "veto": null
  },
  "thesis": "A low-leverage integrated major with an 11.57% FCF yield and buybacks trades cheaply against peers, but its returns are at a cyclical high and not cheap on its own history.",
  "rationale": "Strong balance sheet, cash returns and an uptrend, but earnings sit near a commodity-cycle high with no moat to protect them, and the stock is mid-range or above on its own multiples. The mechanical DCF upside rests on peak cash flow. Good but not compelling: AVOID.",
  "price_at_decision": 82.17,
  "price_date": "2026-11-13",
  "research_note": "research/EPA-TTE/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 8%, back to the FY2025 trough, showing the recovery has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "TTM FCF margin falls below 6%, under the FY2025 low of 6.4%, so cash no longer covers buybacks and dividend.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.52x TTM), showing capital returns are outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "TTM operating margin falls below 11%, near the FY2025 level of 10.8%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 95.6, "basis": "TTM earnings hold and P/E re-rates to its 5y max of 10.7x [RA], still below the peer median of 14.8x; below the DCF bull because that extrapolates peak TTM cash flow."},
    "base": {"probability": 0.45, "target_price_12m": 84.0, "basis": "P/E holds near 9.2x [RA] as buybacks (shares -2.31% YoY [ST]) offset some earnings normalisation; well below the DCF base of 159.84 [IS,CF], which capitalises near-peak TTM cash flow while the reverse DCF prices a revenue fall."},
    "bear": {"probability": 0.30, "target_price_12m": 67.63, "basis": "Commodity normalisation takes returns back toward FY2025 levels (ROIC 8.0% [RA]), matching the DCF bear fair value of 67.63 and near the 6-month low of 65.75 [HI]."}
  },
  "entry_price": 70.56,
  "entry_basis": "P/E back at its 5y median of 7.9x [RA] on TTM earnings; the default (valuation file: base 159.84 x 0.8) is above the price because the DCF base rests on peak cash flow.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: EMS-CHEMIE HOLDING AG (SWX:EMSN) — 2026-11-16
## Bear case
The price already discounts perfection. P/E 41.7x sits at 90% of its 5y range and the reverse DCF needs 23.2% year-1 revenue growth [Certain], demanding for a business whose operating margin troughed at 22.5% in FY2023 [Likely]. EV/EBITDA is +137% above peers [Certain]. The valuation points would come from trend strength (+16.0% above the 200-day, +51.6% over 12 months) [Certain]; an extended price risks a sharp de-rating to the 5y median P/E of 31.0x if growth slows [Likely]. ROCE is down 4.2pp over five years and ROE 6.7pp, though ROCE rose over the last 12 months (24.6% -> 26.2%), still 2.6pp below its 2-year high; the cause is cash piling up (net debt/EBITDA -1.19x), not weaker operations [Likely]. Insiders hold 40.51%: thin float, controlled governance [Certain]. Revenue mix and moat mechanism are unverified [Certain].
## Bull case
Among the best economics in chemicals: ROIC 35.1% TTM, operating margin 29.9% and FCF margin 28.4%, all rising over the last 12 months [Certain]. FCF conversion 116.4% and a net-cash balance sheet (Altman Z 21.30) leave no financial risk [Certain]. Margins and returns held through the FY2023 trough, suggesting niche pricing power [Likely]. The trend is working: relative strength vs SPY is positive at 3, 6 and 12 months, and P/FCF 35.9x is only at 36% of its own 5y range [Certain]. Controlling owners are aligned and the share count is flat [Likely]. The mechanical fair value is flagged unreliable (methods disagree 2.0x), so the headline discount overstates the gap [Certain].
## Decision
```json
{
  "ticker": "SWX:EMSN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds nothing falling over 1 or 3 years; ROIC, ROCE, operating and FCF margin all rose over the last 12 months [RA-T]. The 5-year ROCE/ROE drift reflects accumulating net cash (net debt/EBITDA -1.19x TTM) diluting capital, not weaker operations [RA].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "De-rating: P/E 41.7x near its 5y max and a price implying 23.2% year-1 growth; any slowdown could compress the multiple toward its 31.0x median.",
    "veto": null
  },
  "thesis": "An exceptional net-cash specialty-polymer franchise with rising returns and margins, but priced near the top of its own multiple range for growth well above its history.",
  "rationale": "Quality, balance sheet and trend all score well, but the price sits near the top of its own multiple range and needs 23.2% year-1 growth, a real de-rating risk with an unverified moat mechanism. Scorecard conviction 3: good but not compelling, so AVOID and wait for a lower entry.",
  "price_at_decision": 846.50,
  "price_date": "2026-11-13",
  "research_note": "research/SWX-EMSN/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 28%, well under the 35.1% now, showing the returns franchise is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 28}},
    {"text": "TTM operating margin falls below 24%, reversing the recovery from the FY2023 trough of 22.5%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 24}},
    {"text": "TTM FCF margin falls below 20%, under the FY2024 level of 21.7%, showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA (ratios page) turns positive from -1.19x TTM, i.e. the net cash position is gone."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 900.00, "basis": "Rising margins and FCF sustain the P/E near its 5y max of 43.4x [RA] and the price retests its 52-week high of 900.00 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 818.38, "basis": "EV/EBITDA stays near the top of its range on TTM EBITDA, the EV/EBITDA method's bull value of 818.38 [fact sheet fair value]; the DCF is ignored as unreliable (methods disagree 2.0x)."},
    "bear": {"probability": 0.30, "target_price_12m": 567.40, "basis": "Growth falls short of the 23.2% the reverse DCF implies and EV/EBITDA de-rates toward its 5y median of 23.9x [RA], the EV/EBITDA method's bear value of 567.40 [fact sheet fair value]."}
  },
  "entry_price": 358.0,
  "entry_basis": "valuation file: base 447.49 x 0.8; valuation, not quality, is the obstacle.",
  "replaces": null,
  "replacement_reason": null
}
```

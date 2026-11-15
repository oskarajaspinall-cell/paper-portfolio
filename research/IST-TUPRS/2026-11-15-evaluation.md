# Evaluation: Türkiye Petrol Rafinerileri A.S. (IST:TUPRS) — 2026-11-15
## Bear case
TTM returns sit near a cycle high: ROIC 38.9% TTM versus 13.8% and 12.0% in FY2024-25, and the 3-year change is still falling [Certain] [RA, RA-T]. The Q3 call itself flags geopolitical and Q4 seasonal risks after record utilisation and strong cracks [Likely] (transcript, [OV]). The price has run +84.0% in 12 months and sits 21.6% above its 200-day average, so the trend points rest on peak-margin earnings; if cracks normalise, earnings and the multiple can de-rate together [Likely]. The reverse DCF already implies -12.5% year-1 revenue growth, but the mechanical fair value is flagged unreliable (methods disagree 3.6x), so the "cheap" signal is weak [Certain]. Turkish country risk (TRY depreciation, policy, inflation-distorted ratios) is unquantified here and the revenue mix is [data unavailable] [Likely]. Moat is local scale, not pricing power [Guessing].
## Bull case
Net cash (-1.15x net debt/EBITDA TTM), FCF conversion above 100% in four of five fiscal years and 132.6% TTM, Altman Z 3.28 [Certain] [BS, CF, ST]. The last 12 months are genuinely improving: operating margin 6.1% to 13.2%, FCF margin 5.8% to 13.2% [Certain] [IS-T, CF-T]. Management raised full-year refining-margin guidance at Q3 on record utilisation [Likely] (transcript, [OV]). At P/E 5.6x, EV/EBITDA 2.8x and a 23.48% FCF yield it trades well below the peer medians (8.7x, 5.2x) [Certain] [RA, P:*]. The stock is in a healthy uptrend (50-day 28.2% above the 200-day, RSI 51.1) with low beta 0.30, and the mid-cycle reverse-DCF assumption leaves room if margins hold [Likely].
## Decision
```json
{
  "ticker": "IST:TUPRS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 3-year ROIC decline is the refining-margin cycle unwinding from the FY2022 peak (99.5%) with the balance sheet net cash throughout (-1.15x TTM) [RA, BS]; the last 12 months are rising (ROIC 16.3% to 38.9%) on record utilisation and strong cracks (Q3 2026 transcript, [OV]).",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Refining cracks normalise from a cycle high: TTM ROIC 38.9% vs 12.0% in FY2025 [RA]; after a +84.0% 12-month run a margin reversal would cut earnings and de-rate the extended price together.",
    "veto": null
  },
  "thesis": "Net-cash Turkish refiner at a low multiple on cyclically elevated margins; cheap only if cracks hold.",
  "rationale": "Strong balance sheet and cash conversion, but earnings sit near a cycle high, fair value is flagged unreliable and TRY country risk is unquantified. The scorecard does not reach the buy bar; good but not compelling, so AVOID.",
  "price_at_decision": 359.00,
  "price_date": "2026-11-13",
  "research_note": "research/IST-TUPRS/2026-11-15.md",
  "triggers": [
    {"text": "ROIC TTM falls below 15% (margin cycle reverses back to FY2024-25 levels).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "Operating margin TTM falls below 8%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8}},
    {"text": "FCF margin TTM falls below 5%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 520.00, "basis": "Raised refining-margin guidance holds (Q3 2026 transcript, [OV]) and the 23.48% FCF yield [ST] re-rates toward the peer P/E median 8.7x [RA, P:*]; below the unreliable blended base 637.18 because the DCF leg extrapolates peak cash flow."},
    "base": {"probability": 0.40, "target_price_12m": 360.00, "basis": "Cracks ease seasonally (Q4 risk flagged on the Q3 call) while EV/EBITDA stays near its 5y median 3.1x [RA]; price roughly flat, between the EV/EBITDA base 235.43 and the DCF base 838.06."},
    "bear": {"probability": 0.35, "target_price_12m": 235.43, "basis": "Margins revert toward FY2025 (operating margin 6.5% [IS]) and the stock falls to the EV/EBITDA method's base fair value 235.43 [valuation file], unwinding part of the +84.0% run [ST]."}
  },
  "entry_price": 287.00,
  "entry_basis": "Close to the 200-day average 295.25 [ST,HI] and well below the 359.00 close; the valuation-file base 637.18 x 0.8 is above the price and the fair value is flagged unreliable, so it cannot anchor. Lower price would reduce the de-rating risk of buying peak margins.",
  "replaces": null,
  "replacement_reason": null
}
```

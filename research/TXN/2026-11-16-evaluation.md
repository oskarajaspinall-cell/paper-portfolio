# Evaluation: Texas Instruments Incorporated (TXN) — 2026-11-16
## Bear case
The price already discounts the recovery. P/E 39.4x and EV/EBITDA 26.4x sit above their 5y maxima, and EV/Sales is 122% above peers [Certain]. The reverse DCF implies 46.9% year-one revenue growth [Certain]. Trend strength is what supports the price; an extended stock, 14.7% above its 200-day average after a +86.2% year, risks a sharp de-rating toward its 5y median multiples if the cyclical upturn slows [Likely]. The direction change (ROIC 21.1% -> 30.1%, operating margin 34.9% -> 41.1% over the last year) is mostly operating leverage on a cyclical upturn plus falling capex, not a structural reset; the next downturn can reverse it [Likely]. The macro overlay tilts small toward bear: the 10y real yield is up 0.47pp in 3 months, and the multiple is the exposed variable [Likely]. China is 23% of revenue, with export policy and Silicon Labs approval unverified [Guessing].

## Bull case
A best-in-class analog franchise is working again. Q3 revenue rose 28% YoY across industrial, automotive and data center, and Q4 guidance beat [Certain]. The 300mm capex cycle is rolling off: TTM FCF margin went from 12.0% to 35.2% and FCF conversion to 102.9% [Certain], so the five-year decline in ROIC, ROCE and margins was a temporary investment-plus-trough effect, now reversing [Likely]. Owned capacity and a long-tail catalogue with sticky design-ins give a durable cost and share advantage [Likely]. Balance sheet is strong: net debt/EBITDA 0.51x, Altman Z 11.02, Piotroski 8 [Certain]. P/E is 10% below the peer median [Certain]. The mechanical fair value is flagged unreliable (methods disagree 4.4x) and its through-cycle DCF anchors on depressed capex-cycle FCF [Likely].

## Decision
```json
{
  "ticker": "TXN",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "3-year falls in ROIC and operating margin came from the 300mm capex cycle and the cyclical trough; over the last 12 months ROIC rose 21.1% -> 30.1%, operating margin 34.9% -> 41.1% and FCF margin 12.0% -> 35.2% [RA-T, IS-T, CF-T], with Q3 revenue up 28% YoY and lower 2026 capex guided [company-reported] (https://www.sec.gov/Archives/edgar/data/97476/000009747626000169/txn-20260930.htm).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "De-rating of an extended price: multiples above their 5y maxima, so a slower cyclical upturn or a further real-yield rise (macro overlay) compresses the multiple even with earnings intact.",
    "veto": null
  },
  "thesis": "A high-quality analog franchise in a cyclical and FCF recovery, but priced above its own 5y multiple range for that recovery.",
  "rationale": "Quality, balance sheet and the 12-month direction are strong and the decline was temporary, but valuation sits above its 5y range and the macro overlay leans bear on the multiple. Good but not compelling at this price; the scorecard does not reach the buy bar, so AVOID.",
  "price_at_decision": 303.60,
  "price_date": "2026-11-13",
  "research_note": "research/TXN/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 34% (back to the FY2024 trough level), showing the recovery has failed", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 34}},
    {"text": "TTM ROIC falls below 21%, below the FY2024/FY2025 trough", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 21}},
    {"text": "TTM FCF margin falls below 20%, implying capex is rising again or cash conversion broke", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Net debt / EBITDA (ratios page) rises above 2.0x, e.g. from Silicon Labs deal funding, or the deal is blocked by a regulator"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 360, "basis": "Industrial and data-center upturn keeps beating (Q4 guidance beat, Reuters URL in fact sheet) and P/E holds near today's 39.4x on higher earnings [RA], retaking the 334.03 52-week high [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 290, "basis": "Earnings keep growing but the multiple drifts back toward its 5y max P/E of 35.8x [RA]; well above the unreliable mechanical base of 102.25 because the through-cycle DCF anchors on capex-depressed FCF (methods disagree 4.4x)."},
    "bear": {"probability": 0.30, "target_price_12m": 210, "basis": "Macro overlay tilt toward bear (small, research/TXN/2026-11-16-macro.md) raised this probability: a further real-yield rise or slower cycle de-rates EV/EBITDA to the level the EV/EBITDA method's base of 210.49 implies."}
  },
  "entry_price": 210.49,
  "entry_basis": "The EV/EBITDA method's base fair value of 210.49 (valuation file), used instead of base 102.25 x 0.8 because the blended fair value is flagged unreliable (methods disagree 4.4x); at that level the valuation points would reflect a real discount.",
  "replaces": null,
  "replacement_reason": null
}
```

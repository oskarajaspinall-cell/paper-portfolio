# Evaluation: Man Group Plc (LON:EMG) — 2026-11-15
## Bear case
The recovery is cyclical fee income, not a step-change: ROIC fell from 46.0% (FY2022) to 13.1% (FY2025) before rebounding to 21.3% TTM, and the 12-month rise in ROIC, operating margin and FCF margin is driven by performance fees and AUM gains that reverse when fund returns fade [Likely]. The price already discounts the peak: P/E 14.9x vs a 5y median of 10.4x, P/B 2.9x above its 5y maximum, and the mechanical base fair value 265.54 GBX sits below the 314.80 close [Certain]. After a +51.6% year, the price is extended; if AUM growth or performance fees slow, a de-rating toward the P/E-method base of 221.04 is the likely path [Likely]. FCF conversion of 158.2% flatters the 11.11% FCF yield and is unlikely to persist [Likely]. The Kuwait pension fund broadly won its London lawsuit on 5 Nov 2026; damages and Man's share are unquantified [Certain] and could be material [Guessing].

## Bull case
Man is a net-cash (net debt/EBITDA -0.02x), Piotroski F 8 asset manager with a shrinking share count (-1.67% YoY) [Certain]. Record AUM was reported on 16 Oct 2026 and Meiji Yasuda expanded its private-credit commitment with a possible 5% stake, diversifying away from pure hedge-fund performance fees [Likely]. The rolling-12-month trend is clearly up: ROIC 13.4% to 21.3%, operating margin 19.6% to 27.3%, FCF margin 23.4% to 30.4% [Certain]. On cash, it is not expensive: P/FCF 9.0x sits below its 5y median of 9.2x and well below peers at 15.9x, and the reverse DCF implies only 1.4% year-1 revenue growth, a low bar with AUM at a record [Likely]. The stock trades above its 200-day average, not overextended, with relative strength of +41.2pp over 12 months: a business that is working [Certain]. Beta 0.55 adds diversification [Certain].

## Decision
```json
{
  "ticker": "LON:EMG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no falling metric over the last 1 year: ROIC, operating margin and FCF margin all rose over the 12 months to 2026-06-30 [RA-T, IS-T, CF-T]; the 5-year fall reflects the FY2022 performance-fee peak, not a broken model.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Performance fees and AUM gains reverse while the price is extended after a +51.6% year at P/E 14.9x vs a 10.4x 5y median, de-rating it toward the P/E-method base; plus an unquantified Kuwait lawsuit liability.",
    "veto": null
  },
  "thesis": "A net-cash, record-AUM asset manager whose returns have rebounded on performance fees trades at an above-median earnings multiple, so the upside depends on peak fee income persisting.",
  "rationale": "Quality, balance sheet and trend are good, but earnings are cyclical performance fees near a rebound high, the price sits above the mechanical base fair value and P/B above its 5y range, and an unquantified lawsuit loss is pending. Good but not compelling: AVOID.",
  "price_at_decision": 314.80,
  "price_date": "2026-11-13",
  "research_note": "research/LON-EMG/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 20%, back to the FY2025 level, showing the fee rebound has reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 13%, under the FY2025 level of 13.1%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 13}},
    {"text": "Net debt/EBITDA rises above 1.5x, i.e. the net cash position is lost.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "A company release quantifies the Kuwait pension fund judgment as material to Man Group's net cash, or the judgment is overturned on appeal (removing the overhang)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 348.80, "basis": "Record AUM and the Meiji Yasuda private-credit commitment keep fee income rising, and the price retakes its 52-week high of 348.80 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 287.78, "basis": "Fee income normalises and the price drifts to the DCF-method base fair value of 287.78 [fact sheet fair value], between the blended base 265.54 and the current close."},
    "bear": {"probability": 0.30, "target_price_12m": 221.04, "basis": "Performance fees fade and the P/E de-rates toward its 5y median 10.4x [RA], matching the P/E-method base of 221.04 [fact sheet fair value], with the Kuwait judgment adding to the hit."}
  },
  "entry_price": 212.43,
  "entry_basis": "valuation file: base 265.54 x 0.8; at that price the earnings multiple would sit near its 5y median, paying for cyclical fees with a margin of safety.",
  "replaces": null,
  "replacement_reason": null
}
```

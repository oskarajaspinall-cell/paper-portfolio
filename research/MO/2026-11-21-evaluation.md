# Evaluation: Altria Group (MO) — 2026-11-21

## Bear case
Cigarette volume decline is structural: discount share rose 2.0 points and adjusted domestic cigarette volume fell an estimated 4% in Q3 2026 [company-reported] (https://www.sec.gov/Archives/edgar/data/764180/000076418026000114/mo-20260930.htm) [Certain]. Earnings rest on pricing outrunning volume, which cannot last indefinitely [Likely]. On a rolling basis ROIC slipped from 38.8% to 37.4% and FCF margin from 45.6% to 44.0%, with ROIC 8.0pp and operating margin 16.6pp below 2-year highs [RA-T, IS-T] [Certain]; the slip is small but in the wrong direction [Likely]. EV/EBITDA, P/FCF and EV/Sales sit above their 5y maxima [RA] [Certain]: despite the uptrend (price +7.0% above its 200-day, 12-month change +27.7%) [ST, HI], an extended multiple risks a de-rating back to the 5y medians if earnings growth slows [Likely]. Base fair value 79.70 offers little margin of safety; the bear value is 55.66 [Certain]. The dip has no fundamental cause, so it opens nothing new [Likely].

## Bull case
Very high, stable returns: ROIC 37.4%, operating margin 61.2%, FCF margin 44.0%, net debt/EBITDA 1.66x [RA, IS] [Certain]. The 2-year highs were a one-off peak; TTM figures sit within the FY2021-25 range [Likely]. Q3 2026 raised full-year guidance and expanded the buyback (https://www.businesswire.com/news/home/20261028923631/en/Altria-Reports-2026-Third-Quarter-and-Nine-Months-Results-Announces-Expanded-Share-Repurchase-Program-Raises-2026-Full-Year-Earnings-Guidance/) [Certain]. FCF yield 7.28% and P/E 15.5x at 28% of its 5y range, near peers [ST, RA] [Certain]. The price implies -2.0% year-1 revenue growth, roughly what pricing-over-volume has outrun [Likely]. Beta 0.46; the radar's stock-specific signal rests on a negative fitted beta in a market sell-off, a regression artefact [Likely]. FDA moves to speed pouch/vape approvals may help on! and NJOY [Guessing].

## Decision
```json
{
  "ticker": "MO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC (38.8% to 37.4%) and FCF margin (45.6% to 44.0%) slipped on a rolling basis, but TTM figures sit within the FY2021-25 range and the 2024 2-year highs were a one-off peak [RA-T, RA]; Q3 2026 raised guidance and expanded the buyback (Business Wire release URL in the note).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Cigarette volume decline accelerates (discount share up 2.0 points, volume down an estimated 4% in Q3 [company-reported]) faster than pricing can offset, de-rating a multiple already above its 5y EV/EBITDA and P/FCF maxima.",
    "veto": null
  },
  "new_evidence": {"type": "method_change", "text": "The 2026-11-15 AVOID at conviction 3 predates the trend-strength guards (no strength points above the own 5-year range or the value blend, 2026-11-16/18); under them the same evidence scores 2. The decision (AVOID) is unchanged."},
  "thesis": "A very high-return, cash-generative US tobacco franchise, but priced near its base fair value with multiples above their 5y range on a structurally shrinking category.",
  "rationale": "The dip has no fundamental cause: Q3 raised guidance and the fall is a beta artefact. Quality is excellent, but the price sits near base fair value with EV/EBITDA and P/FCF above their 5y maxima, so the scorecard gives no valuation points. Good but not compelling; no position.",
  "price_at_decision": 74.87,
  "price_date": "2026-11-20",
  "research_note": "research/MO/2026-11-21.md",
  "triggers": [
    {"text": "TTM ROIC falls below 33%, showing pricing no longer offsets volume loss.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 33}},
    {"text": "TTM FCF margin falls below 40%, under the FY2021-22 levels.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 40}},
    {"text": "Net debt/EBITDA rises above 2.5x (1.66x now), signalling debt-funded deals or buybacks.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "Adjusted domestic cigarette volume decline exceeds 7% in two consecutive quarters (10-Q MD&A)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 88.33, "basis": "Guidance is met and buybacks continue, so the stock reaches the DCF bull value 88.33 [fact sheet fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 79.7, "basis": "Pricing keeps offsetting a structural volume decline and the price converges on base fair value 79.70 [fact sheet fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 55.66, "basis": "Volume decline accelerates and EV/EBITDA de-rates from 11.3x toward its 5y median 9.1x [RA], consistent with bear fair value 55.66."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

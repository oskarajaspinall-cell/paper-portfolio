# Evaluation: NICE Ltd. (TLV:NICE) — 2026-11-09
## Bear case
The Direction change lines are real: on a rolling basis ROIC fell from 16.7% to 10.2%, operating margin from 21.9% to 17.2% and FCF margin from 26.5% to 17.6% [RA-T, IS-T, CF-T] [Certain]. Gross margin also slipped to 64.0% TTM [IS] [Certain]. A falling gross margin is the part a restructuring cannot explain. Together with slower cloud growth, slower AI ramps and soft non-core streams (Q3 2026 transcript) [Likely], it fits a structural story: generative-AI agents shrink contact-centre seats, NICE's pricing base [Guessing]. On that reading the low multiple is fair, not cheap, and the mechanical fair value, built on fiscal-year margins the last year reverses, overstates value [Likely]. The Q3 profit decline and the workforce cut could mean weak demand, not efficiency [Likely]. Israel cost-base, shekel and security risk cannot be sized (macro overlay) [Guessing].
## Bull case
Most of the decline has an explanation other than a broken model. Net debt/EBITDA moved from -1.40x (FY2024) to -0.38x (FY2025) while the share count fell 5.35% [BS, ST] [Certain]: cash went to buybacks and heavy investment, which raises invested capital and depresses ROIC while returns on it are still building [Likely]. Restructuring costs weigh on TTM operating margin and are one-off [Likely]. Revenue is still growing, Q3 beat the top of guidance and FY26 EPS guidance rose (Q3 2026 transcript) [Likely], so management is not guiding a demand collapse. Yet the reverse DCF implies -14.2% revenue growth in year 1 [fact sheet] [Certain]. EV/EBITDA 7.3x, EV/Sales 1.8x and P/B 1.6x sit below their own 5-year minimums, the FCF yield is 9.16% even on depressed FCF, and the balance sheet stays net cash [RA, ST] [Certain]. Gartner CCaaS Leader placement says the franchise still competes [Likely].
## Decision
```json
{
  "ticker": "TLV:NICE",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A net-cash, still-growing contact-centre and AI customer-service software franchise trades below its own 5-year minimum EV/EBITDA and EV/Sales at a 9.16% FCF yield, where the price implies a steep revenue decline that beat-and-raise results do not show, while the rolling margin dip is largely investment, buyback-funded capital deployment and restructuring.",
  "rationale": "The rolling decline is mostly explained (cash deployed, restructuring, investment) with the balance sheet intact and guidance raised; the price already discounts shrinkage. Falling gross margin and AI seat risk are real, so conviction 4, not 5, at the standard vol-scaled size. Technology stays within the cap once the pending JKHY exit fills.",
  "price_at_decision": 31520.00,
  "price_date": "2026-11-06",
  "research_note": "research/TLV-NICE/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 15% (17.2% now), showing the margin fall is not restructuring and investment but lost pricing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 14% (17.6% now), showing cash generation is deteriorating structurally rather than resetting.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "TTM gross margin falls below 62% (64.0% now), confirming AI-driven price/mix pressure on the seat-based model.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 62}},
    {"text": "TTM ROIC falls below 8% (10.2% now), showing the deployed capital is not earning its keep.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 55000, "basis": "Restructuring and cloud growth lift operating margin back toward its 22.2% 2-year high [IS-T] and EV/EBITDA re-rates partway from 7.3x toward the 19.1x peer median [RA]; well below the mechanical bull of 144,666.23 because that DCF extrapolates fiscal-year margin gains the rolling year reversed."},
    "base": {"probability": 0.50, "target_price_12m": 40000, "basis": "Margins stabilise near TTM 17.2% [IS-T], revenue keeps growing per raised FY26 guidance (Q3 2026 transcript) and P/FCF recovers modestly from 10.9x toward its 23.9x 5y median [RA] helped by buybacks (shares -5.35% [ST]); below the mechanical base of 82,023.60 because the DCF does not capture the lower FCF margin [CF-T]."},
    "bear": {"probability": 0.25, "target_price_12m": 25000, "basis": "AI agents erode seat pricing, gross margin keeps sliding from 64.0% [IS] and P/FCF holds near its 9.9x 5y minimum on lower FCF [RA], near the 24,260.00 52-week low [HI]; below the mechanical bear of 59,072.04 for the same declining-margin reason."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

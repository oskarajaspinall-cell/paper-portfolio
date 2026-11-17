# Evaluation: Mid-America Apartment Communities, Inc. (MAA) — 2026-11-17
## Bear case
The fall is earned, not an overreaction. Q3 brought a narrowed, lower 2026 core FFO range and a delayed new-lease recovery, with same-store revenue declining [company-reported] [Certain]. Returns are low and falling: ROIC 5.1% TTM vs 5.5% a year earlier and a 2-year high of 6.1%; ROE 6.9% and falling [RA, RA-T] [Certain]. Leverage is rising while returns fall: net debt/EBITDA 4.74x TTM from 3.64x in FY2023 [BS,IS] [Certain]. $1.2 billion of variable-rate debt [company-reported] meets a market pricing hikes (2y 4.88% vs fed funds 3.88%) and real yields up ~0.5pp in 3 months, pressuring both the multiple and FFO (macro overlay) [Likely]. The stock is 8.1% below its 200-day average and trails SPY by 21.3pp over 12 months: not a business that is working [Certain]. FCF yield is only 1.85% [ST] [Certain].
## Bull case
On enterprise multiples MAA is cheap: EV/EBITDA 15.9x sits below its 5y minimum of 16.0x and 14% under peers; EV/Sales 8.8x is also below its 5y minimum; P/B near the bottom of its range [RA] [Certain]. The mechanical P/FFO fair value of 137.79 base (126.02 bear) sits above the price [Likely]. Management cites strong renewals, better turnover, improving October leasing and declining new supply, setting up a 2027 recovery as Sunbelt deliveries recede [company-reported] [Likely]. The Series I preferred redemption trims funding cost [company-reported] [Likely]. Beta 0.70 and an investment-grade balance sheet limit downside [Likely]. If real yields fall back, the multiple and financing cost both ease (macro overlay) [Guessing].
## Decision
```json
{
  "ticker": "MAA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC and ROE are falling on a Sunbelt supply wave depressing new-lease rents; management reports declining new deliveries, strong renewals and improving October leasing (10-Q https://www.sec.gov/Archives/edgar/data/912595/000119312526437813/maa-20260930.htm; Q3 call https://stockanalysis.com/stocks/maa/transcripts/719961-q3-2026/), with the balance sheet investment-grade. Leverage rising adds risk but does not show lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "The new-lease recovery slips again and higher short rates on $1.2 billion of variable-rate debt force another core FFO guidance cut while leverage keeps rising.",
    "veto": null
  },
  "thesis": "A Sunbelt apartment REIT trading below its own 5-year EV/EBITDA minimum on a supply-driven rent trough, but with low and falling returns, rising leverage and a downtrend, it is cheap rather than a good business that is working.",
  "rationale": "The entry-price hit came from a guidance-driven fall that reflects real deterioration (lower FFO range, falling ROIC, rising leverage), not an overreaction. ROIC near 5% gives no quality-level points, so the scorecard cannot reach 4 at any price. Cheap enterprise multiples alone do not clear the bar; AVOID.",
  "price_at_decision": 117.82,
  "price_date": "2026-11-16",
  "research_note": "research/MAA/2026-11-17.md",
  "triggers": [
    {"text": "Net debt/EBITDA (statistics page) rises above 5.5x, showing leverage outrunning a recovery.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 5.5}},
    {"text": "TTM ROIC falls below 4.5%, showing the rent trough is deepening rather than bottoming.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 4.5}},
    {"text": "Same-store revenue growth (10-Q MD&A) is negative for two further consecutive quarters, or core FFO guidance is cut again."},
    {"text": "Conversely: same-store revenue turns positive with new-lease rent growth in the 10-Q, evidencing the supply-driven recovery."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 137.79, "basis": "New supply recedes and October leasing gains hold (Q3 call, /stocks/maa/transcripts/719961-q3-2026/), re-rating to the base P/FFO fair value 137.79 [fact sheet fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 126.02, "basis": "A slow 2027 recovery with flat FFO lifts EV/EBITDA back toward its 16.0x 5y floor [RA], near the bear P/FFO fair value 126.02; held below base fair value because returns and leverage are worsening [RA-T, BS]."},
    "bear": {"probability": 0.35, "target_price_12m": 105.0, "basis": "Another FFO cut on delayed leasing and variable-rate interest cost, with real yields still rising; the macro overlay's small tilt toward bear (research/MAA/2026-11-17-macro.md) moves probability from base to bear, and the price breaks the 113.95 52-week low [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: ROIC of 5.1% TTM scores no quality-level points, so the scorecard cannot reach conviction 4 at any price; a lower price would not change the decision until returns recover.",
  "replaces": null,
  "replacement_reason": null
}
```

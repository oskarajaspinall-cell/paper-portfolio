# Evaluation: Avery Dennison Corporation (AVY) — 2026-10-09
## Bear case
Returns are fading: ROIC fell from 18.4% (FY2021) to 15.1% TTM and ROE fell 13.2pp, while net debt/EBITDA rose to 2.28x and hit 2.61x at FY2025 [Certain]. The cheapest-looking multiple, P/FCF 11.9x, rests on a TTM FCF margin of 11.5% against 8.0% in FY2025 and 150.8% FCF conversion. That is probably working-capital timing, not a new run-rate [Guessing]. On P/E, EV/EBITDA and EV/Sales, AVY still trades 28-36% above packaging peers, so the "cheap" story is only cheap against its own history [Certain]. The moat comes from scale and know-how, not pricing power, and UPM, 3M and Nitto Denko are credible rivals [Certain]. The shares trail SPY by 18.9pp over 6 months, and management already guides to destocking [Likely]. Q3 results on Oct 29 are an event risk [Certain].
## Bull case
Every multiple sits below its 5-year minimum: EV/EBITDA is 10.8x vs a 12.2x floor and P/E 18.3x vs 19.4x [Certain]. The reverse DCF implies -3.3% revenue growth, while Q2 delivered 8% organic growth and FY2026 guidance is 3%-4% organic with 7% EPS growth [Likely]. High-value categories are about 45% of sales, carry above-average margins and are lifting gross margin, which is up 1.2pp to 29.0% [Likely]. Buybacks cut the share count 3.08% YoY [Certain]. With beta 0.80 and Altman Z 3.54, the downside should be moderate [Certain]. The mechanical base fair value of 213.64 is 27.5% above the price [Certain].
## Decision
```json
{
  "ticker": "AVY",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A good, mix-improving labels and RFID franchise trades below its own 5-year multiple floors, but ROIC is falling, leverage is rising and the FCF that makes it look cheap is probably inflated by timing, so the discount is not compelling.",
  "rationale": "The discount to its own history is real, but it rests on TTM FCF that is likely flattered, and AVY still trades above packaging peers. ROIC is trending down and leverage up, so this is good but not compelling. Conviction 3 sits below the buy threshold. We revisit after Q3 results confirm FCF and margin.",
  "price_at_decision": 167.62,
  "price_date": "2026-10-08",
  "research_note": "research/AVY/2026-10-09.md",
  "triggers": [
    {"text": "Upgrade case: TTM ROIC rises back above the FY2022 level of 16.3%, showing mix-shift returns are lifting overall returns; downside invalidation is ROIC below the FY2023 low of 13.5%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 13.5}},
    {"text": "TTM gross margin falls below the FY2022 5-year low of 26.6%, reversing the high-value-category mix gain.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 26.6}},
    {"text": "TTM operating margin falls below the FY2023 5-year low of 11.6%, showing destocking or input inflation is structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 11.6}},
    {"text": "Net debt/EBITDA (ratios page) rises above the FY2025 high of 2.61x, signalling M&A or buybacks are outrunning cash generation."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 230.07, "basis": "Q3/Q4 confirm the TTM FCF margin of 11.5% [CF,IS] and high-value mix gains, so the price reaches the mechanical bull fair value of 230.07 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.5, "target_price_12m": 191.6, "basis": "EV/EBITDA partly re-rates toward its 12.2x 5y floor [RA], which is the EV/EBITDA bear value of 191.60 [IS,BS,CF,RA,ST]. This sits below the 213.64 blended base because that base is DCF-heavy and runs on a TTM FCF margin that is probably inflated (11.5% vs FY2025 8.0% [CF,IS])."},
    "bear": {"probability": 0.25, "target_price_12m": 124.73, "basis": "FCF falls back to FY2025 conversion and destocking flagged on the Q2 call (/stocks/avy/transcripts/656205-q2-2026/) extends the ROIC decline [RA], so the price falls to the mechanical bear fair value of 124.73 [IS,BS,CF,RA,ST,HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

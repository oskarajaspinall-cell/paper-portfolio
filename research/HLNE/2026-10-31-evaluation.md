# Evaluation: Hamilton Lane Incorporated (HLNE) — 2026-10-31
## Bear case
The cheapness is multiple compression, not mispriced value: the DCF leg (82.50) sits below the 83.91 close and base fair value offers only +9.8% [Certain]. Quality is slipping at the margin: operating margin fell from 46.1% (FY2022) to 43.6% TTM, gross margin from 64.9% to 60.7%, and ROIC from 28.5% (FY2025) to 19.8% TTM [Certain]. Shares outstanding rose 34.50% YoY despite buybacks; the note cannot reconcile this, so dilution is unresolved [Guessing]. The wealth channel pits it against far larger alternatives managers, a fee-rate risk [Likely]. Founder-era succession (a new co-CEO, Mario Giannini retiring) is a key-person risk [Likely]. Short interest of 10.22% of float and results due Nov 3, 2026 add gap risk before the thesis can be tested [Certain].
## Bull case
P/E of 12.8x is below its 5y minimum of 17.5x and far below the 34.5x peer median; EV/EBITDA of 12.1x is also below its 5y floor [Certain]. Earnings are cash-backed: FCF conversion 133.0%, FCF margin 42.7%, FCF yield 7.93%, net debt/EBITDA 0.07x [Certain]. The fee base is long-dated and contractual, with evergreen funds driving fee growth per the latest 10-Q and $50.0 million of buybacks in the June quarter [company-reported] [Likely]. The P/E leg of fair value (base 111.32) shows meaningful re-rating room if the fall of 27.3% over 12 months proves overdone [Likely]. Macro is calm (high-yield spread 3.26%, VIX 17.2) and context only [Likely].
## Decision
```json
{
  "ticker": "HLNE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cash-generative, net-cash private-markets manager trades below its own 5-year multiple range, but slipping margins and ROIC, unresolved share-count growth and succession leave the mechanical base value only slightly above the price.",
  "rationale": "Good but not compelling: base fair value offers little margin of safety and the DCF leg is below the price, while margins and ROIC are drifting down, the share count jump is unexplained and leadership is changing with results due Nov 3. Conviction 3 is below the buy threshold, so no position; cash is acceptable.",
  "price_at_decision": 83.91,
  "price_date": "2026-10-30",
  "research_note": "research/HLNE/2026-10-31.md",
  "triggers": [
    {"text": "TTM operating margin falls below 38%, well under the 42.8%-46.1% FY range, showing wealth-channel competition is compressing fee economics.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 38}},
    {"text": "TTM ROIC falls below 14%, under the FY2022 five-year low of 15.8%, signalling the franchise's returns are eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 14}},
    {"text": "TTM FCF margin falls below 30%, signalling earnings are no longer turning into cash outside the FY2024 dip.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.07x TTM now), showing capital returns or growth are being debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 111.32, "basis": "Evergreen fee growth holds and the P/E moves back toward its 5y minimum of 17.5x [RA], matching the P/E leg base value 111.32 in the fact-sheet fair value."},
    "base": {"probability": 0.45, "target_price_12m": 92.11, "basis": "Fees grow roughly in line with the 9.8% reverse-DCF implied growth while margins drift, consistent with the blended base fair value 92.11 [IS,RA,ST]."},
    "bear": {"probability": 0.30, "target_price_12m": 54.97, "basis": "Operating margin keeps sliding from 43.6% [IS], the share-count jump of 34.50% [ST] proves real dilution and succession disrupts fundraising, consistent with the mechanical bear fair value 54.97."}
  },
  "entry_price": 73.69,
  "entry_basis": "valuation file: base 92.11 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

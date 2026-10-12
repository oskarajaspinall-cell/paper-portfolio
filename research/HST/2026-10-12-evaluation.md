# Evaluation: Host Hotels & Resorts, Inc. (HST) — 2026-10-12
## Bear case
There is no margin of safety. The close of $22.65 sits at the base fair value of $22.67, the bull value is only $23.27 (+2.7%) and the bear value is $20.55 (-9.3%), so the skew tilts down [Certain]. Host owns hotels but does not control the brands or operators. ROIC of 6.9% is a cycle-level return with no structural edge over PK, SHO or DRH [Likely]. RevPAR is near a cyclical high after World Cup and luxury-resort demand, so 2026 comparisons may be the peak [Guessing]. The macro overlay says the 10y real yield rose +56bp and the HY spread +45bp over 3 months. Both work against a leveraged, cap-rate-priced REIT [Likely]. P/B of 2.4x is above its own 5y maximum and 93% above peers [Certain]. Over 3 months the stock trails SPY by -5.8pp [Certain].
## Bull case
The fundamentals are improving. ROIC rose from -1.1% to 6.9% and ROE from -0.2% to 15.6% TTM. Site net debt/EBITDA fell from 8.69x to 2.18x [Certain]. In Q2 2026, comparable RevPAR grew +7.0% and adjusted EBITDAre +5.8%, and FY2026 guidance was raised [Likely]. P/E of 15.2x is below its own 5y minimum of 15.9x and 31% below the peer median of 22.1x. EV/EBITDA of 11.5x is 6% below peers [Certain]. A 6.46% FCF yield and a -1.38% YoY share count show cash coming back to holders [Certain]. Host is the largest U.S. lodging REIT with an investment-grade balance sheet, so it can buy assets if rates bring distressed sellers [Likely].
## Decision
```json
{
  "ticker": "HST",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Host is the best-capitalised U.S. lodging REIT and its fundamentals are improving, but the price already equals its base fair value of $22.67 while rising real yields push against a cap-rate-priced, cyclical asset base.",
  "rationale": "The business is improving and cheap on P/E, but EV/EBITDA is only in line with its own history and peers. The price is at base fair value, the bull value is +2.7% and the bear value is -9.3%, and the macro tilt is toward bear. That is good but not compelling, so conviction is 3: AVOID. Watch for a 20% margin of safety.",
  "price_at_decision": 22.65,
  "price_date": "2026-10-09",
  "research_note": "research/HST/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC falls below 5%, reversing the post-pandemic improvement to 6.9% and showing returns have rolled over with the lodging cycle.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 5}},
    {"text": "Net debt/EBITDA rises back above 4.0x, undoing the deleveraging from 8.69x (FY2021) to 2.18x TTM.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.0}},
    {"text": "Comparable hotel RevPAR growth in the quarterly earnings release turns negative for two consecutive quarters, or FY2026 guidance is cut below the raised range."},
    {"text": "TTM ROE falls below 10%, back under the FY2022-FY2024 range, showing the TTM 15.6% was a peak.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 25.71, "basis": "Raised RevPAR guidance holds and P/E re-rates from 15.2x toward its 5y minimum-to-median of 15.9x-17.9x [RA], back to the 52-week high of 25.71 [HI]; this is above the mechanical bull value of 23.27 because that P/FFO proxy does not credit the guidance raise; the probability was cut from 0.25 for the overlay's moderate tilt toward bear (research/HST/2026-10-12-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 22.67, "basis": "RevPAR growth moderates and the multiple holds, so the price tracks the P/FFO-proxy base fair value of 22.67 [IS,BS,CF,RA,ST] at the current 5.22% risk-free rate."},
    "bear": {"probability": 0.35, "target_price_12m": 19.64, "basis": "Real yields and HY spreads keep rising (overlay tilt toward bear, moderate, research/HST/2026-10-12-macro.md) and RevPAR peaks, pushing value below the mechanical bear of 20.55 to the April 2026 low of 19.64 [HI]; the probability was raised from 0.25 for the macro tilt."}
  },
  "entry_price": 18.14,
  "entry_basis": "valuation file: base 22.67 x 0.8 = 18.14 [IS,BS,CF,RA,ST] (a 20% margin of safety), which would make the skew clearly favourable even with the macro tilt toward bear.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Lockheed Martin Corporation (LMT) — 2026-10-10
## Bear case
The quality trend is pointing the wrong way. ROIC fell from 38.4% (FY2021) to 23.9% (FY2025), gross margin from 13.6% to 10.2% and operating margin from 11.7% to 9.3% [Certain] [RA, IS]. That looks like structural fixed-price program pressure [Likely]. Net debt/EBITDA rose from 0.90x to 1.73x TTM, so more of the dividend and buybacks is funded with debt [Certain] [BS, IS]. Valuation is not cheap on its own history: P/E 18.8x and EV/EBITDA 13.9x sit mid-range (48%/51%) [Certain] [RA]. The DCF base fair value depends on a 5.22% risk-free rate. The macro overlay flags that a further rise in real yields would shrink that gap [Likely] (research/LMT/2026-10-10-macro.md). The price is below both its 50-day and 200-day averages, has lagged SPY by 32.8pp over 6 months and reports on Oct 22, 2026 [Certain] [HI, ST]. That leaves near-term event risk with no visible margin catalyst [Guessing].
## Bull case
The moat is real: sole-source, decades-long platforms (F-35, PAC-3) with a beta of 0.10 [Certain] [ST]. Recent order flow includes a seven-year PAC-3 MSE seeker scale-up and the PAC-3 Edge interceptor (Reuters, 2026-10-05/09) [Likely]. Cash quality is improving: TTM FCF margin is 11.3% and FCF conversion 138.8%, up from FY2024's 7.4%/99.1% [Certain] [CF, IS]. The FCF yield is 7.42%, P/FCF sits at the 8th percentile of its 5-year range, and LMT trades at a 15% P/E and 22% P/FCF discount to peers [Certain] [ST, RA]. The reverse DCF implies -1.3% year-1 revenue growth, which looks pessimistic during a munitions replenishment cycle [Likely]. Shares outstanding fell 1.97% YoY and the dividend was raised to $3.60 [Certain] [ST, OV]. The blended base fair value of 612.84 is 20.3% above the close [Certain].
## Decision
```json
{
  "ticker": "LMT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A sole-source defense franchise with strong, improving cash conversion and a 7.42% FCF yield, but five years of falling ROIC and margins and mid-range own-history earnings multiples leave the valuation case good rather than compelling.",
  "rationale": "Cash conversion and the peer discount are attractive, but ROIC, gross and operating margins have fallen for five years. Leverage has risen, P/E and EV/EBITDA sit mid-range of their own history, and the DCF gap is rate-sensitive per the macro overlay. Q3 results land Oct 22. Conviction 3 is below the buy threshold, so cash is preferred.",
  "price_at_decision": 509.59,
  "price_date": "2026-10-09",
  "research_note": "research/LMT/2026-10-10.md",
  "triggers": [
    {"text": "TTM operating margin recovers above the FY2023 level of 13.4%, showing program-cost pressure has reversed (would raise conviction).", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 13.4}},
    {"text": "TTM gross margin recovers above the FY2022/FY2023 level of 12.7%, confirming fixed-price program charges are behind it (would raise conviction).", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 12.7}},
    {"text": "TTM ROIC rises back above the FY2022 level of 31.0%, showing the moat again turns into rising capital returns (would raise conviction).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 31.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 641.19, "basis": "Replenishment orders (PAC-3 seeker contract, Reuters 2026-10-05) lift margins back toward FY2023 levels and the stock reaches the fact sheet's bull fair value of 641.19 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.45, "target_price_12m": 560.0, "basis": "FCF conversion of 138.8% [CF,IS] supports a partial re-rating toward the EV/EBITDA base of 581.63, held below the 612.84 blended base by falling margins [IS] and a small bear tilt from real yields per research/LMT/2026-10-10-macro.md."},
    "bear": {"probability": 0.30, "target_price_12m": 420.0, "basis": "Margins keep compressing [IS] and P/E de-rates from 18.8x to its 5y low of 15.5x [RA], with probability raised slightly for higher-for-longer real yields per research/LMT/2026-10-10-macro.md."}
  },
  "entry_price": 490.27,
  "entry_basis": "valuation file: base 612.84 x 0.8; at that level the FCF yield and P/FCF near its 5y low would compensate for the declining margin trend.",
  "replaces": null,
  "replacement_reason": null
}
```

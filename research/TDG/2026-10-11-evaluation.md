# Evaluation: TransDigm Group Incorporated (TDG) — 2026-10-11
## Bear case
The fact sheet's own fair value puts base value at 803.20, 27.5% below the 1,107.99 close, and the price still needs 13.4% year-1 revenue growth to work [Certain]. TDG funds its growth with debt: net debt/EBITDA rose from 4.77x (FY24) to 6.03x TTM after the Prince & Izant deal, Altman Z is 1.93, and FCF conversion slipped to 90.5% [Certain]. The macro overlay (research/TDG/2026-10-11-macro.md) shows real yields up 0.56pp and HY spreads up 0.45pp over three months, with the 2y yield above fed funds pointing to higher-for-longer. For a 6x-levered serial acquirer, that raises interest cost and the discount rate together [Likely]. The FCF yield is 3.15%, thin cover for this risk [Certain]. "Cheap versus peers" may only mean the whole aerospace group was re-rated at a cyclical peak [Guessing].
## Bull case
This is one of the best business models in industrials. Around 90% of sales are proprietary, about 55% come from the aftermarket, and FAA certification locks in each part, which gives 46.7% operating margins [Certain]. ROIC rose from 9.4% to 15.4% and ROCE from 9.7% to 19.3% over five years, so returns improved even with heavy M&A [Certain]. Q2 and Q3 FY2026 both beat, and management raised guidance each time [Likely]. The stock trades at the bottom of its own 5-year EV/EBITDA range (18.0x), below its 5-year minimum P/E and P/FCF, and 38% below peers on EV/EBITDA [Certain]. A mechanical DCF built on its own history probably understates a business whose returns have stepped up [Likely]. Short interest is low at 2.18% [Certain].
## Decision
```json
{
  "ticker": "TDG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "TDG has a top-tier proprietary aerospace aftermarket moat with rising ROIC and trades at the bottom of its own multiple range, but 6.03x leverage, a 3.15% FCF yield and a price 27.5% above base fair value leave too little margin of safety while real yields and credit spreads rise.",
  "rationale": "Quality is excellent and improving, and the stock is cheap against its own history and peers. Even so, base fair value is 803.20, leverage is rising after the Prince & Izant deal, and the macro overlay tilts moderately toward the bear case. The probability-weighted 12-month value is roughly the current price. That is good but not compelling, so conviction is 3 and the decision is AVOID; cash is acceptable.",
  "price_at_decision": 1107.99,
  "price_date": "2026-10-09",
  "research_note": "research/TDG/2026-10-11.md",
  "triggers": [
    {"text": "Net debt/EBITDA rises above 7x without a deleveraging path, showing M&A is outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 7}},
    {"text": "TTM operating margin falls below 44%, the FY2023 level, signalling erosion of proprietary-part pricing power.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 44}},
    {"text": "TTM ROIC falls below 12.6%, the FY2023 level, showing acquisitions are diluting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12.6}},
    {"text": "TTM FCF margin falls below 15%, under the 5-year low of 15.3%, showing cash conversion is deteriorating.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1390, "basis": "EV/EBITDA re-rates from 18.0x to its 5y median of 21.1x [RA] on TTM EBITDA, with the gain leveraged into equity by 6.03x net debt/EBITDA [BS,IS], helped by guidance raised twice in FY2026 (factsheet news, Q2/Q3 transcripts); this sits below the bull fair value of 1,547.89."},
    "base": {"probability": 0.45, "target_price_12m": 1150, "basis": "EV/EBITDA stays near its 5y low of 18.0x [RA] while EBITDA grows with organic aftermarket demand and the Prince & Izant deal; this is above the 803.20 base fair value because the own-history DCF does not capture ROIC rising from 9.4% to 15.4% [RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 800, "basis": "Probability raised for the macro overlay's moderate tilt toward bear (research/TDG/2026-10-11-macro.md): real yields rising further and HY spreads widening push the discount rate and refinancing cost up for a 6.03x-levered acquirer [BS,IS], and the price converges on the DCF base fair value of 803.20 (factsheet Fair value)."}
  },
  "entry_price": 642.56,
  "entry_basis": "valuation file: base 803.20 x 0.8 (factsheet Fair value [IS,BS,CF,RA,ST,HI]). At that price the 6.03x leverage and the macro tilt would be well compensated by the moat and the rising-ROIC evidence.",
  "replaces": null,
  "replacement_reason": null
}
```

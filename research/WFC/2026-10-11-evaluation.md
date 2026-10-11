# Evaluation: Wells Fargo & Company (WFC) — 2026-10-11
## Bear case
The price already discounts the good news. At 83.55, WFC trades at 1.5x P/B, 91% of its own 5y range (0.9x-1.6x), and above all three fair-value scenarios, including the 77.76 bull case [Certain]. Returns do not justify a re-rating. TTM ROE of 12.6% is a cyclical recovery on a flat five-year trend, and it still trails large-bank peers [Likely]. The Piotroski F-score is 3 [Certain]. A HUD fair-lending probe opened on 2026-10-07. Its scope and cost are unknown, and it revives the regulatory overhang this franchise has carried before [Guessing]. The macro overlay tilts toward bear (moderate): the 10y is at 5.22% and HY spreads widened +0.45pp over 3m, which lifts the cost of equity and the provisioning risk [Likely]. Short interest rose 12.3% month on month [Certain]. Relative strength is -17.4pp vs SPY over 6m, and Q3 results land on Oct 13 [Certain].

## Bull case
WFC runs a scale national deposit franchise that is hard to replicate [Likely]. Net margin rose from 18.8% in FY2022 to 27.2% TTM, and ROE of 12.6% is the best in five years [Certain]. Buybacks are shrinking the share count by 5.98% a year [Certain], which compounds per-share value even if the multiple holds. On earnings the stock is not expensive: P/E of 12.1x sits slightly below its 12.5x 5y median and 3% below the 12.6x peer median [Certain]. The reverse DCF implies only -1.3% revenue growth [Certain]. A positively sloped curve supports net interest margin (macro overlay) [Likely]. If the HUD probe proves narrow, the stock could re-test its 91.99 6-month high [Guessing].

## Decision
```json
{
  "ticker": "WFC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A scale deposit franchise with recovering but flat-trend ROE trades near the top of its own 5y P/B range and above every fair-value scenario, while a new HUD probe and rising rates add downside risk.",
  "rationale": "There is no margin of safety. P/B is 91% of the way up its 5y range and the price sits above even the 77.76 bull fair value. ROE is only back to its FY2021 level, the HUD probe is unquantified and the macro overlay tilts toward bear. The expected value of the scenarios is below the price. This is a decent bank but not compelling, so it is an AVOID; cash is acceptable.",
  "price_at_decision": 83.55,
  "price_date": "2026-10-09",
  "research_note": "research/WFC/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROE (statistics page) falls below the FY2023 level of 10.3%, showing the return recovery has reversed.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10.3}},
    {"text": "TTM net margin (statistics page) falls below the FY2022 five-year low of 18.8%, erasing the efficiency gains.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 18.8}},
    {"text": "Share count stops shrinking (YoY shares change turns positive), ending the buyback support to per-share value.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "An SEC filing discloses that the HUD fair-lending probe resulted in a material penalty, consent order or mortgage-business restriction."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 92.0, "basis": "ROE holds at the 12.6% five-year best [RA] and the 5.98% annual share shrinkage [ST] continues, so P/B holds near its 1.6x 5y max [RA] and the stock re-tests its 91.99 6-month high [HI]; this sits above the 77.76 bull fair value because it assumes the peak multiple persists."},
    "base": {"probability": 0.45, "target_price_12m": 76.0, "basis": "P/E stays near its 12.5x 5y median [RA] on flat-trend ROE [RA], but the HUD probe overhang (https://www.reuters.com/business/finance/wells-fargo-faces-regulator-probe-over-efforts-boost-black-homeownership-wsj-2026-10-07/) and a 5.22% risk-free rate pull the price toward the fact sheet's 71.61-77.76 base-bull fair-value band."},
    "bear": {"probability": 0.35, "target_price_12m": 55.0, "basis": "P/B de-rates toward its 1.0x 5y median [RA] as the HUD probe and widening HY spreads raise provisioning and cost-of-equity risk, so the price sits between the 40.93 bear and 71.61 base fair values; the bear probability was raised (moderate) per the macro overlay's tilt toward bear (research/WFC/2026-10-11-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

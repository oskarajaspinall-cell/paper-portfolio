# Evaluation: Valero Energy Corporation (VLO) — 2026-10-10
## Bear case
VLO is pricing peak-cycle, war-driven crack spreads as if they last. TTM ROIC of 25.2% compares with 8.9% in FY2024, so returns follow the refining cycle and show no structural step-up [Certain]. On almost every measure the stock is above its own 5y range: EV/EBITDA is 9.6x against a 5y max of 9.3x, P/FCF 12.3x against 9.9x and P/B 5.0x against 1.9x [Certain]. The price of 433.75 is 30.8% above base fair value (300.30) and only 8.8% below the bull case (471.87) [Certain]. Barron's flags demand destruction and a possible diesel export ban, and a Middle East de-escalation would take away the supply premium [Likely]. The White House is also pressing refiners on pump prices ahead of the midterms [Likely]. Rising yields (10y at 5.22%) push fair value lower still [Certain]. Buying after a 167% 12-month run, with no moat, means paying for the peak of the cycle [Likely].

## Bull case
The balance sheet is strong. Net debt/EBITDA is 0.26x, down from 2.40x in FY2021, with Altman Z at 4.90 and Piotroski F at 7 [Certain]. The 7.6% TTM FCF margin funds buybacks, and the share count is down 4.60% YoY [Certain]. The WSJ suggests Q3 results (due Oct 22) could beat the near-record June quarter, which would cut the trailing multiples [Likely]. On EV/EBITDA VLO trades 13% below its peers [Certain]. If disrupted global supply keeps crack spreads high for another year, cash returns keep compounding and the price can move toward the bull fair value [Guessing]. Even so, the upside to the bull case is small next to the downside to the base case.

## Decision
```json
{
  "ticker": "VLO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A well-capitalised but moatless refiner whose price already capitalises peak, war-disrupted crack spreads, trading above its own 5-year multiple ranges and 30.8% over base fair value.",
  "rationale": "The balance sheet and buybacks are strong, but earnings sit at a geopolitical cyclical peak. Every multiple except P/E is above its own 5y max, and the price sits near the bull fair value. The reward is asymmetric to the downside, and the macro overlay tilts slightly further toward the bear case. This is not high conviction, so no position: cash is the better holding.",
  "price_at_decision": 433.75,
  "price_date": "2026-10-09",
  "research_note": "research/VLO/2026-10-10.md",
  "triggers": [
    {"text": "TTM operating margin holds above 9% (vs 7.9% TTM and a 5y FY peak of 9.2%) after supply disruption eases, evidencing a structurally higher margin base rather than a cyclical spike.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 9}},
    {"text": "TTM FCF margin rises above 9% (vs 7.6% TTM and a 5y FY high of 6.4%), showing cash generation can support the current valuation through the cycle.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 9}},
    {"text": "TTM gross margin falls below 10% (FY2024 trough 10.8%), confirming full crack-spread reversion and resetting the earnings base to which any entry case must be anchored.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 471.87, "basis": "War-disrupted supply keeps crack spreads elevated (WSJ headline [OV]) and Q3 earnings re-rate trailing multiples, reaching the fact sheet's bull fair value 471.87 [IS,BS,CF,RA,ST,HI]."},
    "base": {"probability": 0.40, "target_price_12m": 390.0, "basis": "Margins ease partway from TTM 7.9% operating margin [IS] and EV/EBITDA eases back from 9.6x toward its 5y max of 9.3x [RA], above the base fair value 300.30 because buybacks (-4.60% shares [ST]) and near-zero net debt support the price."},
    "bear": {"probability": 0.35, "target_price_12m": 300.30, "basis": "Crack spreads normalise on demand destruction or export-ban risk (Barron's, https://www.barrons.com/articles/diesel-prices-valero-marathon-refining-stocks-4487b345) and the price falls to base fair value 300.30 [IS,BS,CF,RA,ST,HI]. The probability is raised slightly for the macro overlay's small tilt toward bear (rising 10y yield, research/VLO/2026-10-10-macro.md). The bear target stays above the mechanical bear 153.36 because net debt/EBITDA of 0.26x [RA] limits downside within 12 months."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

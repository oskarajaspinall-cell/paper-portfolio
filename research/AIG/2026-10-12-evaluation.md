# Evaluation: American International Group, Inc. (AIG) — 2026-10-12
## Bear case
Returns have structurally reset: ROE fell from 16.0% (FY2021) to 7.2% TTM and ROIC from 9.8% to 7.7% [Certain] [RA], so the sub-peer P/B of 1.0x vs 2.1x is earned, not a mispricing [Likely]. On earnings the stock is not cheap: P/E 14.2x sits at the 93rd percentile of its 5y range and 29% above the 11.0x peer median [Certain] [RA]. The mechanical fair value (P/B+ROE, P/E) puts base at $41.33 and even bull at $61.48, below the $77.04 close [Certain]. Four senior departures/appointments in six weeks, including Executive Chairman Zaffino, add underwriting-execution risk into Q3 results on Nov 3 [Likely] (WSJ, Business Wire [OV]). The macro overlay tilts small toward bear: widening HY spreads and a firmer dollar tend to compress financial multiples faster than higher yields lift investment income [Guessing] (research/AIG/2026-10-12-macro.md). Relative strength is -24.0pp vs SPY over 12 months [Certain] [HI].

## Bull case
Capital return is aggressive: shares fell 11.07% YoY [Certain] [ST], and leverage is low and falling (net debt/EBITDA 1.12x) [Certain] [RA], funding more buybacks [Likely]. ROE and ROIC are rising off the FY2022-24 trough (ROIC 5.1% to 7.7% TTM) [Certain] [RA]; Q2 2026 showed 10% adjusted EPS growth and 13% first-half premium growth per the call transcript [Likely] [OV]. EV/EBITDA of 5.9x is 34% below peers and in the bottom quartile of its own range [Certain] [RA]. A 5.22% 10y yield lifts reinvestment yields on a large fixed-income book [Likely] (macro overlay). If ROE reaches double digits, P/B could re-rate toward peers [Guessing]. Still, nothing here shows a cheap price: the P/E is near its 5y high, so the upside needs a recovery that has not yet shown up.

## Decision
```json
{
  "ticker": "AIG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A sub-peer-return diversified insurer whose ROE has halved since FY2021 trades near the top of its own 5-year P/E range and far above its mechanical fair value, during unusual senior-management turnover.",
  "rationale": "Quality is mid-recovery but still low (ROE 7.2%) and the P/B discount to peers reflects it. P/E near its 5y high, price 46% above base fair value and a probability-weighted target below the price give no margin of safety. Buybacks and low leverage are real but don't make this compelling. Cash is preferred.",
  "price_at_decision": 77.04,
  "price_date": "2026-10-09",
  "research_note": "research/AIG/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROE rises above 10%, closing much of the return gap to peers that justifies the P/B discount.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 10}},
    {"text": "TTM ROIC rises back above the FY2021 level of 9.8%, reversing the 5-year decline.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 9.8}},
    {"text": "Q3 2026 results (Nov 3, 2026) and the following quarter show General Insurance underwriting results holding up through the leadership transition, with continued premium growth."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 84.74, "basis": "ROE recovery and an 11.07% YoY share shrink [ST] re-rate P/B to its 5y max 1.1x [RA] from 1.0x; above the $61.48 mechanical bull because that model holds ROE at 7.2% TTM [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 72.0, "basis": "P/B holds near 1.0x [RA] as ROE stays around 7.2% [RA] and buybacks offset some P/E drift down from the 93rd-percentile 14.2x [RA]; above the $41.33 base fair value because the market has held P/B at 0.7-1.1x for five years, not at the model's ROE-implied level; probability shifted toward bear per the small bear macro tilt (research/AIG/2026-10-12-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 48.29, "basis": "P/E reverts to its 5y median 8.9x [RA] from 14.2x on flat TTM EPS as leadership turnover [OV] and widening HY spreads (macro overlay, small bear tilt) compress the multiple; consistent with the P/E-method fair value range $24.85-$48.34."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

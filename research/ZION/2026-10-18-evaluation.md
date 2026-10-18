# Evaluation: Zions Bancorporation, National Association (ZION) — 2026-10-18
## Bear case
The headline cheapness is largely an accounting artefact. TTM ROE of 16.4% and the 8.1x P/E rest on Q2 2026's $252m of pre-tax noncustomer gains (Visa Class B-1 sale, SBIC marks), worth ~$1.31/share after tax [company-reported] (https://www.sec.gov/Archives/edgar/data/109380/000010938026000111/zions-20260630.htm) [Certain]. Strip them and ROE sits back in the FY2021-25 range of 12.8-14.7%, on a five-year falling trend, and P/B of 1.2x is mid-range on its own history [Certain]. The efficiency ratio is flat at 62.2% [company-reported]: no cost edge [Likely]. The mechanical fair value leans on an FCFE DCF built from bank cash flows that reflect deposit/loan balance swings, not owner earnings [Likely]. Rates are moving against it: fed funds 3.88% after a hike, 10y at 5.10%, which threatens funding costs and AOCI-hit book value (macro overlay) [Likely]. Piotroski F is 4, and Q3 results land on 2026-10-19 [Certain].

## Bull case
Even on normalised returns, a Western regional bank with a low-cost deposit franchise at 1.2x book, below the 1.4x peer median, is not expensive [Certain]. NIM rose to 3.27% from 3.17% on lower funding costs and average loans grew 2% q/q [company-reported] (https://www.sec.gov/Archives/edgar/data/109380/000010938026000111/zions-20260630.htm) [Certain]. The reverse DCF implies -11.8% year-one revenue growth, a bar current loan growth clears [Likely]. Fee diversification (the acquired agency multifamily platform, wealth, capital markets) and steady buybacks support EPS [Likely]. Credit is described as stable and HY spreads at 3.23% remain tight (macro overlay) [Likely]. The bear fair value of $74.96 sits above the $63.37 close [Certain], though that figure overstates value for the reasons in the bear case [Likely].

## Decision
```json
{
  "ticker": "ZION",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A fairly valued Western regional bank whose apparent discount to its own history and peers is mostly one-off Visa/SBIC gains inflating TTM earnings, with core ROE average and drifting lower.",
  "rationale": "Ex one-off gains, returns sit inside a falling five-year range and P/B is mid-range on history; the fair-value premium rests on bank FCFE and inflated TTM ROE. Rising rates add NIM and book-value risk, and Q3 results tomorrow will show core earnings. Good but not compelling: AVOID, cash is acceptable.",
  "price_at_decision": 63.37,
  "price_date": "2026-10-16",
  "research_note": "research/ZION/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROE rises above 15% after the Visa/SBIC gains roll out of the trailing window, showing core profitability has genuinely stepped up above the FY2021-25 range.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 15}},
    {"text": "TTM net margin holds above 30% once the one-off gains roll off, evidencing a structurally better earnings mix (fees, funding costs).", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 30}},
    {"text": "Reported NIM (10-Q / earnings release) stays above 3.27% for two consecutive quarters despite higher rates, while the efficiency ratio falls below 60%, showing a real funding-cost and cost edge."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 81.71, "basis": "Core ROE holds near the TTM level and NIM keeps expanding, so value reaches the fact sheet's P/B + ROE base of 81.71 [IS,BS,RA] as P/B moves toward the 1.4x peer median [RA]; overlay's neutral, small tilt leaves the probability unchanged (research/ZION/2026-10-18-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 68.0, "basis": "Gains roll off, ROE reverts to the FY2021-25 12.8-14.7% band [RA] and P/B stays near its 1.3x 5y median [RA] on modest book growth, below the mechanical base of 92.81 because the FCFE leg uses bank cash flows driven by balance-sheet swings (note section 5)."},
    "bear": {"probability": 0.25, "target_price_12m": 52.0, "basis": "Higher-for-longer rates reverse the NIM gain below 3.17% and widen AOCI losses (macro overlay bear), so P/B falls to its 1.1x 5y low [RA] on a smaller book, below the mechanical bear of 74.96 for the same FCFE and inflated-ROE reasons."}
  },
  "valuation_overrides": [
    {"method": "pb_roe", "scenario": "base", "field": "roe", "value": 0.135, "reason": "TTM ROE of 16.4% includes Q2 2026 Visa Class B-1 and SBIC one-off gains (note section 2, sec.gov 10-Q); FY2025 ROE of 13.5% [RA] is the sustainable run-rate."},
    {"method": "pb_roe", "scenario": "bear", "field": "roe", "value": 0.128, "reason": "FY2023 ROE of 12.8% [RA], the five-year low, is the relevant downside if the NIM tailwind reverses under higher rates (macro overlay)."}
  ],
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below base fair value less the margin of safety, but that value rests on one-off-inflated ROE and bank FCFE. A lower price would not change the decision; Q3 2026 results proving core ROE above the historical range would.",
  "replaces": null,
  "replacement_reason": null
}
```

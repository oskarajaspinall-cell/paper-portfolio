# Evaluation: UMB Financial Corporation (UMBF) — 2026-11-07
## Bear case
The headline base fair value of 193.36 leans on an FCFE DCF (286.42) that is generous for a bank; the credible P/B + ROE anchor is 146.83, and its bear of 130.37 sits below the 133.77 close [Certain]. On book the stock is not cheap: P/B 1.3x is 11% above peers [Certain]. Growth is acquisition-led and dilutive: shares rose 14.35% YoY after HTLF, and El Dorado adds another part-stock deal with thrift-style credit and integration risk, still needing approvals [Certain]. Q3 earnings were flattered by non-recurring securities gains, so the 10.1x P/E overstates cheapness [Likely]. Piotroski F of 4 and lumpy FCF conversion (46.5% in FY2024) weaken earnings quality [Certain]. The macro overlay tilts toward bear: VIX at 28.18 and HY spreads up 0.77pp over 3m could push P/B toward its 1.1x 5y low (research/UMBF/2026-11-07-macro.md) [Likely].

## Bull case
ROE has held 12-15% through the cycle and is 13.5% TTM, rising over five years [Certain]. Q3 net interest income rose 13.7% year on year and fees were 30.1% of revenue [company-reported], a richer mix than a typical regional bank [Likely]. P/E of 10.1x sits near the bottom of its 9.3x-14.5x 5y range and 20% below the peer median; P/FCF 8.9x is 19% below peers, with an 11.24% FCF yield [Certain]. The reverse DCF implies -7.3% year-1 revenue growth, a shrinkage that 11.1% annualised loan growth in Q3 does not show [Likely]. El Dorado adds $2.1 billion of low-cost deposits, modestly accretive per management [Likely]. Beta of 0.85 limits drawdown risk [Certain]. If integration goes cleanly, P/B can re-rate toward its 1.5x 5y median [Guessing].

## Decision
```json
{
  "ticker": "UMBF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A steady 13.5%-ROE, fee-rich regional bank trades cheaply on earnings but only fairly on book, with acquisition-driven dilution and a fresh deal clouding per-share value.",
  "rationale": "The credible P/B + ROE value is only modestly above the price and its bear is below it; the higher blended value rests on a bank FCFE DCF. Dilution, a new part-stock acquisition, non-recurring Q3 gains and a bear-leaning macro tilt make this good but not compelling. Cash is preferable.",
  "price_at_decision": 133.77,
  "price_date": "2026-11-06",
  "research_note": "research/UMBF/2026-11-07.md",
  "triggers": [
    {"text": "TTM ROE (statistics page) falls below 10%, under the FY2021 five-year low of 11.5%, showing the returns franchise is eroding.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "TTM net margin falls below 25%, near the FY2023 five-year low of 24.6%, signalling credit costs or deposit pricing are compressing profitability.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 25}},
    {"text": "Shares change YoY stays above 20%, signalling growth is being funded by dilution rather than earned per share.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 20}},
    {"text": "FCF conversion (cash flow / income statement pages) stays below 80% TTM for two consecutive quarters, showing earnings are not turning into cash."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 159.2, "basis": "ROE holds at 13.5% [RA] and El Dorado integrates cleanly, lifting value to the P/B + ROE bull of 159.20 [IS,BS,RA]; below the blended bull because the FCFE DCF is generous for a bank (note section 3)."},
    "base": {"probability": 0.45, "target_price_12m": 146.83, "basis": "Earnings steady with 13.7% NII growth [company-reported] offset by dilution; value converges on the P/B + ROE base of 146.83 [IS,BS,RA], below the blended 193.36 because the FCFE DCF overstates a bank (note section 3)."},
    "bear": {"probability": 0.3, "target_price_12m": 114.0, "basis": "Per the macro overlay's small toward-bear tilt (research/UMBF/2026-11-07-macro.md), wider HY spreads compress P/B toward its 1.1x 5y low [RA] while deal dilution and non-recurring Q3 gains cut earnings power; probability raised for the tilt."}
  },
  "entry_price": 117.46,
  "entry_basis": "valuation file: P/B + ROE base 146.83 x 0.8 [IS,BS,RA]; the blended base 193.36 x 0.8 is above the price and leans on a bank FCFE DCF (note section 3).",
  "replaces": null,
  "replacement_reason": null
}
```

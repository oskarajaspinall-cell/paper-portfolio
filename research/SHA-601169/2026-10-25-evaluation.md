# Evaluation: Bank of Beijing Co., Ltd. (SHA:601169) — 2026-10-25
## Bear case
Profitability is eroding with no sign of a floor: ROE fell from 8.6% (FY2021) to 5.5% (FY2025) and 5.3% TTM, and net margin from 52.0% to 47.8% TTM [RA, IS] [Certain]. A P/B of 0.3x is roughly what that ROE justifies against a cost of equity built on a 4.96% risk-free rate plus a 3.5% country premium, so the discount is earned [Likely]. On earnings the stock is not cheap: P/E 6.8x sits at the 92nd percentile of its 5y range and in line with the 6.7x peer median [RA] [Certain]. The mechanical base fair value of 8.19 leans on an FCFE DCF that is unreliable for a bank, whose cash flows carry deposit and loan movements; the dividend-discount value is only 2.68 [Likely]. Asset quality, NIM and capital adequacy are absent from the data, so property-credit losses or a recapitalisation cannot be ruled out [Guessing]. Piotroski F is 4 [ST] [Certain].

## Bull case
P/B of 0.3x is at the bottom of its 5y range and well below the 0.5x peer median [RA] [Certain]. The reverse DCF implies -13.5% year-1 revenue growth, so the price already assumes decline [Certain]. The P/B + ROE method alone gives a base of 7.52 CNY, so even modest ROE stabilisation would re-rate the shares [Likely]. Net margin has held near the high-40s TTM, showing earnings are falling slowly rather than collapsing [Certain]. Results due Oct 31, 2026 could show ROE bottoming [Guessing]. The macro overlay is context-only and flags no adverse shock (CNY 6.6861 per USD) [Likely].

## Decision
```json
{
  "ticker": "SHA:601169",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A deep discount to book that is largely justified by a steadily falling ROE, with no visible asset-quality or capital data to show the decline has bottomed.",
  "rationale": "Cheap on P/B but not on P/E, ROE still falling, and the mechanical base fair value rests on an FCFE method unsuited to banks. Without NIM, asset quality or capital data, this looks like a value trap rather than a compelling core idea; conviction 2 is an AVOID.",
  "price_at_decision": 5.41,
  "price_date": "2026-10-23",
  "research_note": "research/SHA-601169/2026-10-25.md",
  "triggers": [
    {"text": "ROE recovers above its FY2021 level of 8.6%, showing profitability has turned (statistics page).", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 8.6}},
    {"text": "Net margin recovers above its FY2021 level of 52.0%, showing margin compression has reversed (statistics page).", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 52.0}},
    {"text": "Company-reported results show stable or rising net interest margin and non-performing loan ratio stable or falling for two consecutive reports."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 7.52, "basis": "ROE stabilises and the stock re-rates to the P/B + ROE base value of 7.52 [RA,ST]; below the blended base 8.19 because the FCFE leg is distorted by banking cash flows."},
    "base": {"probability": 0.5, "target_price_12m": 5.41, "basis": "ROE drifts near 5.3% TTM [RA] and P/B stays around 0.3x, the bottom of its 5y range [RA], leaving the price near the 5.41 close, which is the mechanical bear fair value."},
    "bear": {"probability": 0.3, "target_price_12m": 4.03, "basis": "ROE keeps falling as in FY2021 to FY2025 [RA] and the stock trades to the P/B + ROE bear value of 4.03 [RA,ST], consistent with the 2.68 dividend-discount value showing little support."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades at the mechanical bear fair value and its lowest 5y P/B; the issue is a falling ROE and missing asset-quality and capital evidence, so a lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

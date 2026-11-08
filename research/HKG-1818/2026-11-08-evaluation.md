# Evaluation: Zhaojin Mining Industry Company Limited (HKG:1818) — 2026-11-08
## Bear case
Earnings are the gold price times ounces less cost, and the last quarter shows the cycle turning: every rolling-12-month return metric sits below its 2026-06-30 high (ROIC 10.4% vs 13.6%, operating margin 28.5% vs 33.9%, FCF margin 18.8% vs 29.6%) [RA-T, IS-T, CF-T] [Certain]. That direction change is the thesis risk: it most likely reflects a softer gold price, and operating leverage cuts both ways [Likely]. The mechanical base fair value of 17.75 HKD is barely above the 17.41 close, with a bear of 14.56 [Certain], so the price already assumes TTM margins hold. "Cheap vs 5y history" is an artefact of depressed past earnings [Likely]; it is dearer than A-share peers on P/E and EV/EBITDA [Certain]. Trend is broken (down 38.6% over 12 months, 50-day 24.4% below the 200-day) [Certain]. Gold price, reserves and cost position are [data unavailable], so key drivers are unverified [Certain].

## Bull case
The business has been transformed: ROIC rose from 1.7% to 10.4%, operating margin from 12.0% to 28.5%, and net debt/EBITDA fell from 7.31x to 0.82x [RA, IS] [Certain]. Each recent-direction metric is still above a year earlier [RA-T] [Certain]. FCF conversion is about 104% with a 6.84% FCF yield, and the share count fell 5.09% YoY [CF, ST] [Certain]. It is cheaper than peers on P/FCF and P/B [Certain]. The macro overlay notes falling real yields and a VIX spike that support gold, offset by a firmer dollar (tilt neutral, small) [Likely]. If gold re-firms, margins recover toward the peak and the bull fair value is far above the price [Guessing].

## Decision
```json
{
  "ticker": "HKG:1818",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraged, much-improved gold miner, but at 17.41 HKD the price already discounts TTM margins that are rolling over from their mid-2026 peak, leaving no margin of safety.",
  "rationale": "Quality gains are real, yet base fair value sits barely above the price, all return metrics are falling from their 2-year highs and the gold price, reserves and costs are unverified. Good but not compelling at this price; cash is acceptable.",
  "price_at_decision": 17.41,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-1818/2026-11-08.md",
  "triggers": [
    {"text": "ROIC (TTM, statistics page) falls below 8%, showing the return improvement was purely cyclical", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "Operating margin (TTM) falls below 22%, back toward the FY2024 level", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}},
    {"text": "FCF margin (TTM) falls below 10%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Debt/EBITDA rises above 2.0x, reversing the deleveraging", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 24.0, "basis": "Gold re-firms and operating margin recovers toward its 33.9% 2-year high [IS-T], lifting EBITDA under the EV/EBITDA method; below the mechanical bull of 51.06 because that implies the 5y median multiple on peak earnings, which history set on depressed profits [RA]; macro overlay tilt neutral/small leaves this probability unchanged."},
    "base": {"probability": 0.45, "target_price_12m": 17.75, "basis": "TTM earnings roughly sustained and the multiple holds, matching the mechanical base fair value of 17.75 HKD (EV/EBITDA, fact sheet)."},
    "bear": {"probability": 0.3, "target_price_12m": 14.56, "basis": "The decline from the 2026-06-30 peaks continues and margins revert toward 22% as in the macro overlay's bear (research/HKG-1818/2026-11-08-macro.md), matching the mechanical bear of 14.56 HKD."}
  },
  "entry_price": 14.2,
  "entry_basis": "valuation file: base 17.75 x 0.8 (20% margin of safety); at that price the same evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

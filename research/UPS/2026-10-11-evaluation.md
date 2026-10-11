# Evaluation: United Parcel Service, Inc. (UPS) — 2026-10-11
## Bear case
Every return metric has fallen for five years: ROIC 39.0% to 16.6%, operating margin 13.2% to 9.2%, FCF margin 11.1% to 6.1% TTM [Certain]. Leverage is rising into the recovery, with net debt/EBITDA at 1.99x versus 0.94x in FY2021 [Certain]. A ~$5.4bn dividend, ~$3.0bn capex and transformation cash costs all compete for that thinner cash flow, and no buybacks are planned [Certain]. The low multiples (EV/EBITDA 8.6x, below its 5y minimum) look like the market pricing lower structural profitability, not a mispricing [Likely]. At 94.57 the stock already sits above the 90.22 base fair value. The reverse DCF prices in 4.6% year-1 growth, which needs the unproven $3bn savings plan to land [Likely]. Rising real yields and HY spreads cut the DCF and raise funding costs at the same time (macro overlay, moderate bear tilt) [Likely]. The F-35 export-control report adds a compliance risk nobody can size yet [Guessing].
## Bull case
The Amazon glide-down finished in June 2026. Transformation delivered ~$1.2bn of benefits in H1 toward a $3bn 2026 target, and FY2026 adjusted operating-profit guidance was raised (2Q26 release) [Likely]. Cash conversion is strong (FCF/NI 119.4% TTM), giving a 6.78% FCF yield [Certain]. EV/EBITDA (8.6x), EV/Sales (1.2x) and P/FCF (14.7x) are all below their 5y minimums, and the discount to the peer median is 42-54% [Certain]. If operating margin recovers toward the FY2023 level of 10.5%, the EV/EBITDA method's base value of 127.97 shows the re-rating room [Guessing]. The UPS/FedEx duopoly in US small parcels is intact, and wins such as the exclusive TikTok Shop returns deal add optionality [Likely]. Q3 results on Oct 27 could show the savings in the numbers [Guessing].
## Decision
```json
{
  "ticker": "UPS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A US parcel duopolist trading below its own 5-year minimum EV/EBITDA and P/FCF, but on falling returns and rising leverage, with the price already above the DCF-led base fair value, so the cheapness is earned until the transformation shows up in margins.",
  "rationale": "The stock is cheap on multiples but not on cash flow: 94.57 is above the 90.22 base fair value. ROIC, margins and FCF margin are still falling, leverage is rising, the macro tilt leans bear and the export-control issue is open. The recovery is a management claim, not yet a result. That is good but not compelling, so AVOID, with an entry at base fair value less a margin of safety.",
  "price_at_decision": 94.57,
  "price_date": "2026-10-09",
  "research_note": "research/UPS/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin rises above 10.5%, the FY2023 level, proving the Amazon glide-down and the transformation savings are rebuilding profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 10.5}},
    {"text": "TTM FCF margin rises above 6.8%, the FY2024 level, showing cash generation funds the dividend and the restructuring costs.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 6.8}},
    {"text": "Net debt/EBITDA on the ratios page falls back below 1.68x (FY2024), showing leverage has stabilised after the restructuring."},
    {"text": "UPS or a US regulator discloses a material penalty or export-privilege restriction over the reported F-35 parts shipment to China (would further lower conviction)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 127.02, "basis": "Transformation savings (~$1.2bn H1 toward $3bn, 2Q26 release) lift margins and EV/EBITDA re-rates from 8.6x toward its 5y median of 11.0x [RA], matching the fact sheet's bull fair value."},
    "base": {"probability": 0.5, "target_price_12m": 90.22, "basis": "Margins stabilise near 9.2% TTM [IS] and the price converges on the DCF-led base fair value; the reverse DCF's 4.6% implied growth is roughly met, so there is no re-rating."},
    "bear": {"probability": 0.3, "target_price_12m": 63.46, "basis": "ROIC and FCF margin keep falling while net debt/EBITDA climbs past 1.99x [RA], and rising real yields and HY spreads cut the DCF (macro overlay research/UPS/2026-10-11-macro.md, moderate bear tilt, which moved 0.05 of probability from bull to bear), taking the price to the fact sheet's bear fair value."}
  },
  "entry_price": 72.18,
  "entry_basis": "valuation file: base 90.22 x 0.8 (20% margin of safety on the DCF-led base fair value).",
  "replaces": null,
  "replacement_reason": null
}
```

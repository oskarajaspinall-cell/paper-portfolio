# Evaluation: ADNOC Logistics & Services plc (ADX:ADNOCLS) — 2026-10-20
## Bear case
The price already reflects the re-rating: base fair value is only 8.04 AED against a 7.37 AED close, and the reverse DCF needs 12.0% year-1 revenue growth [Certain]. TTM returns (ROIC 19.4%, operating margin 26.0%) sit well above every fiscal year, including FY2025's 18.1% operating margin, so they may be a cyclical freight peak, not a run-rate [Likely]. Cash conversion is still weak: FCF margin 9.8% and P/FCF 24.3x, double the peer median of 11.8x, while the $1.3bn 11-vessel purchase and $900m LNG order keep capex heavy [Likely]. It trades at a premium to peers on P/E and EV/EBITDA [Certain]. Hormuz tensions (Iran blacklisting tankers) are a direct operating risk for a Gulf-based fleet [Likely]. A free float dominated by ADNOC (institutions 4.5%) leaves minority holders with little influence over how capital is allocated [Likely].

## Bull case
Five years of rising quality: ROIC from 3.6% to 19.4%, ROE to 22.5%, net debt/EBITDA down to 0.13x, Piotroski 8 [Certain]. Long-term ADNOC contracts make revenue more visible than at spot-exposed peers, consistent with a 0.40 beta [Likely]. Every earnings multiple sits below its own 5-year minimum (P/E 9.6x vs 12.4x min; EV/EBITDA 7.0x vs 9.1x) [Certain]. Profit guidance was reportedly raised a third time in August (headline only) [Guessing]. Fleet additions could compound contracted EBITDA, supporting the bull value of 11.69 AED [Guessing].

## Decision
```json
{
  "ticker": "ADX:ADNOCLS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A captive, low-leverage ADNOC shipping arm whose returns have re-rated sharply, but the price already sits near base fair value and implies double-digit growth from TTM margins that may be peak-cycle.",
  "rationale": "Quality and balance sheet are strong, but base fair value offers little upside, the price implies 12.0% growth, TTM margins look elevated versus FY2025, FCF conversion is weak during heavy fleet capex, and Hormuz risk is direct. Good but not compelling: conviction 3, so AVOID; re-examine near the entry price.",
  "price_at_decision": 7.37,
  "price_date": "2026-10-19",
  "research_note": "research/ADX-ADNOCLS/2026-10-20.md",
  "triggers": [
    {"text": "TTM operating margin falls below 15%, under every fiscal year since FY2022, showing weaker contract economics with ADNOC.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 10%, giving back most of the five-year rise toward open-market tanker economics.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin turns negative again, showing fleet capex outpacing cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Net debt/EBITDA on the ratios page rises above 2.0x (0.13x TTM now), showing fleet-expansion debt outpacing EBITDA."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 11.69, "basis": "Fleet additions lift contracted EBITDA and the multiples return toward their 5y median (EV/EBITDA 10.1x [RA]), matching the mechanical bull fair value of 11.69 AED [fact sheet]."},
    "base": {"probability": 0.5, "target_price_12m": 8.04, "basis": "TTM returns hold and the mechanical base fair value of 8.04 AED (DCF 67% + EV/EBITDA 33%) is reached [fact sheet]."},
    "bear": {"probability": 0.3, "target_price_12m": 5.8, "basis": "Operating margin reverts toward the FY2025 18.1% [IS] and P/B falls to its 5y min 1.6x [RA]; the mechanical bear of -11.78 AED is a DCF artifact and is not used."}
  },
  "entry_price": 6.43,
  "entry_basis": "valuation file: base 8.04 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

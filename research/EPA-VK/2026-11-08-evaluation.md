# Evaluation: Vallourec S.A. (EPA:VK) — 2026-11-08
## Bear case
These are cyclical returns. ROIC was 2.5% and ROE -20.8% in FY2021-22, and the mechanical bear fair value is negative (-2.47 EUR) [Certain]. The Direction change line matters: ROCE of 16.1% sits 4.4pp below its 20.5% 2-year high (2024-06-30). The driver is the fade from 2023-24 peak tube pricing, not a new deterioration, because the last 12 months are rising [Likely]. Still, it shows the peak has passed. Base fair value of 19.97 EUR is only +5.6% above the close, so there is little margin of safety [Certain]. EV/Sales and P/B sit above their 5y maxima [Certain]. Middle East disruption already cut Q2 volumes, and the revenue split by country is [data unavailable], so geopolitical exposure cannot be sized [Likely]. ArcelorMittal's exit removed an anchor holder, and shares rose 1.75% YoY [Certain]. Results are due Nov 20, 2026 [Certain].

## Bull case
The balance sheet has swung from 2.13x net debt/EBITDA to net cash (-0.18x) [Certain], and the investment-grade rating was renewed [Likely]. TTM ROIC (17.7%), operating margin (16.2%) and FCF margin (12.0%) are all up year on year, with FCF conversion of 124.3% and a Piotroski F of 8 [Certain]. Proprietary VAM premium connections and qualification barriers argue for a higher through-cycle floor than FY2021 [Likely]. At a 10.12% FCF yield and EV/EBITDA of 5.4x, it trades well below its peers TS, NOV, SLB and WFRD [Certain]. The reverse DCF implies -2.3% year-1 revenue growth, so a downturn is already priced [Certain]. Offshore contract wins, US strength and geothermal (a target of 10%-15% of EBITDA from New Energies by 2030) add optionality [Likely].

## Decision
```json
{
  "ticker": "EPA:VK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash premium-tubulars franchise with recovered returns and a 10.12% FCF yield trades cheaply against peers, but at roughly its own base fair value on cyclical, post-peak returns, so the skew is balanced rather than compelling.",
  "rationale": "Quality, cash and balance sheet are strong, and the market prices a mild downturn. But the price already sits near base fair value, the history shows deep cyclical troughs, and the Middle East exposure cannot be sized. Expected value roughly equals the price. That makes it good, not compelling: conviction 3, AVOID, wait for a lower entry.",
  "price_at_decision": 18.91,
  "price_date": "2026-11-06",
  "research_note": "research/EPA-VK/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 12% (16.2% now), showing premium-connection pricing is rolling over into a cyclical downturn.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "TTM ROIC falls below 12% (17.7% now), signalling returns are reverting toward the FY2021 trough rather than holding a higher floor.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM FCF margin falls below 6% (12.0% now), showing cash conversion was cycle-flattered.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "Net debt/EBITDA rises above 1.0x (-0.18x now), reversing the deleveraging.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 26.0, "basis": "Offshore wins and US strength (Q2 2026 transcript) keep the TTM margins rising [IS-T], and the price moves toward the mechanical bull of 30.64 [fact sheet Fair value], held below it because EV/Sales and P/B already sit above their 5y maxima [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 20.0, "basis": "Margins and ROIC hold near TTM levels [RA-T] and the stock converges on the mechanical base fair value of 19.97 [fact sheet Fair value], with EV/EBITDA near its 5y median 5.2x [RA]."},
    "bear": {"probability": 0.3, "target_price_12m": 12.0, "basis": "Middle East disruption (Q2 2026 transcript) and a drilling downturn push returns back toward the cycle; anchored on the EV/EBITDA bear of 11.55 [fact sheet Fair value] rather than the negative DCF bear, because net cash (-0.18x [RA]) and an investment-grade rating cushion the trough."}
  },
  "entry_price": 15.98,
  "entry_basis": "valuation file: base 19.97 x 0.8; at that level the same evidence (net cash, rising TTM returns, a downturn priced in) gives a margin of safety large enough for conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

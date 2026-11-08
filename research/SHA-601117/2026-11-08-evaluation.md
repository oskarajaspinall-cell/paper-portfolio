# Evaluation: China National Chemical Engineering Co., Ltd (SHA:601117) — 2026-11-08
## Bear case
This is a thin-margin, state-linked EPC contractor with no evident moat [Likely]. ROIC has collapsed from 35.3% (FY2021) to 12.4% TTM and sits 5.5pp below its 2-year high of 18.0% [Certain] [RA, RA-T]; the Direction change reflects a shrinking customer-prepayment float, visible as net debt/EBITDA moving from -6.46x to -2.19x [Likely] [BS, IS]. That threatens the thesis: the "net cash" is largely working capital owed to others, so cheapness on EV is partly illusory [Likely]. FCF margin is 3.5pp below its 2-year high of 6.8% and was negative in FY2025 and FY2022 [Certain] [CF-T, CF]; the second Direction change is that same lumpy prepayment timing, so the 13.83% FCF yield is unreliable [Likely]. Altman Z of 1.39 [Certain] [ST]. The mechanical base value rests on a working-capital-driven DCF with a bear of 0.84 [Certain]. Overseas exposure is unknown and China policy risk unverified (macro overlay) [Certain].
## Bull case
The price discounts severe decline: P/E 6.8x is below its 5y minimum of 7.1x, P/B 0.6x at its 5y floor, and the reverse DCF implies -24.6% year-1 revenue [Certain] [RA, fact sheet Fair value]. Margins are quietly improving: gross margin from 9.3% to 11.1% and operating margin 4.3% TTM against 3.8% a year earlier, a 2-year high [Certain] [IS, IS-T]. ROIC and ROCE are flat over the last year, so the decline may be stabilising [Likely] [RA-T]. Shares fell 1.76% YoY, a modest buyback [Certain] [ST]. EV/EBITDA of 3.2x against a peer median of 11.9x leaves room for a re-rating if cash conversion steadies [Guessing]. Still, there is no catalyst, no moat and erratic cash, so the case is "cheap", not "compelling" [Likely].
## Decision
```json
{
  "ticker": "SHA:601117",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A statistically cheap, state-linked chemical EPC contractor whose falling ROIC, shrinking prepayment float and erratic cash conversion make the low multiples a value trap risk rather than a mispriced quality business.",
  "rationale": "Cheap on every multiple, but ROIC is well below its 2-year high, the net-cash float is shrinking, FCF is lumpy and Altman Z is weak. The mechanical base value leans on a working-capital-sensitive DCF; the EV/EBITDA leg shows far less upside. No moat and no catalyst: good-but-not-compelling at best, so AVOID.",
  "price_at_decision": 7.30,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-601117/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10% (12.4% now), showing returns are still eroding rather than stabilising.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 3.5% (4.3% now), reversing the contract-margin improvement.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 3.5}},
    {"text": "TTM FCF margin turns negative (3.2% now), confirming cash conversion is unreliable.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Net debt/EBITDA on the ratios page (debt less cash) rises above -1.0x (-2.19x TTM now), i.e. the net-cash cushion largely disappears."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 10.00, "basis": "Margins keep rising from the 4.3% TTM operating margin [IS-T] and the EV/EBITDA fair-value leg's bull of 9.94 is reached, near the 52-week high of 10.48 [HI]; below the blended bull of 15.89 because that DCF capitalises lumpy prepayment-driven FCF."},
    "base": {"probability": 0.50, "target_price_12m": 8.20, "basis": "P/E recovers partway from 6.8x toward its 5y median 8.9x [RA] on flat earnings, short of the EV/EBITDA leg's base of 8.68; well below the mechanical base of 14.14 because the DCF leg is driven by working-capital swings (FCF margin -0.6% in FY2025 vs 3.2% TTM [CF])."},
    "bear": {"probability": 0.25, "target_price_12m": 6.00, "basis": "The float keeps unwinding (net debt/EBITDA -6.46x to -2.19x [BS,IS]) and FCF turns negative again as in FY2025 [CF], taking the price below the 52-week low of 6.72 [HI]; above the mechanical bear of 0.84, a DCF artefact of negative FCF years, given P/B of 0.6x [RA]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: falling ROIC, a shrinking prepayment float and erratic cash conversion keep conviction low at any price; a lower price would not change the decision until the fundamentals stabilise.",
  "replaces": null,
  "replacement_reason": null
}
```

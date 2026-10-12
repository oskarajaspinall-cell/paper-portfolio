# Evaluation: Amcor plc (AMCR) — 2026-10-12

## Bear case
The Berry Global merger has so far diluted rather than compounded: ROIC fell from 10.3% to 6.9%, ROCE from 12.2% to 7.1%, and shares rose 45.57% YoY [Certain]. Leverage is high for a low-growth, low-margin converter: net debt/EBITDA 3.97x, and an Altman Z of 1.37 sits in the distress zone [Certain]. The stock is not cheap against peers: P/E 17.5x vs 14.8x and P/FCF 15.7x vs 13.5x [Certain]. The EV/EBITDA leg of the fair value gives only 27.07, well below the price [Certain]. The 10-K gives no quantified deleveraging target or timeline [Certain]. Real yields up 0.56pp and HY spreads up 0.45pp in three months hit a levered, bond-proxy equity (macro overlay, secondary weight, moderate tilt toward bear) [Likely]. Relative strength is −14.6pp vs SPY over six months, with no sign of a turn [Certain].

## Bull case
The price implies only 0.2% year-1 revenue growth, while management guides to double-digit EPS growth with synergies "ahead of schedule" (Jefferies transcript) [Likely]. Q4 adjusted EPS grew 23% [Likely]. EV/EBITDA of 9.4x, EV/Sales and P/FCF all sit below their own 5-year minimums [Certain]. FCF conversion of 111% and a 6.38% FCF yield fund the dividend and debt paydown [Certain]. Leverage has already fallen from 6.98x to 3.97x [Certain]. Contractual pass-through pricing kept gross margin flat at about 20% [Likely]. The DCF base of 58.05 is 39% upside [Certain]. If synergies show up in ROIC and leverage returns toward its FY2022 level of 3.05x, the multiple could re-rate toward its 11.5x median [Guessing].

## Decision
```json
{
  "ticker": "AMCR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A post-merger packaging leader trading below its own 5-year EV/EBITDA minimum, where synergy delivery could re-rate the shares, but falling returns, 3.97x leverage and a distress-zone Altman Z mean the upside is not yet earned.",
  "rationale": "Cheap against its own history, but not against peers on P/E or P/FCF. ROIC is still falling, leverage is high and the macro tilts toward bear. The re-rating depends on synergies and deleveraging that the reported figures do not yet show. Good but not compelling: no position. Revisit when returns and leverage improve.",
  "price_at_decision": 41.72,
  "price_date": "2026-10-09",
  "research_note": "research/AMCR/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC rises above 8% (from 6.9%), showing the Berry synergies are lifting returns rather than just offsetting dilution.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 8}},
    {"text": "TTM FCF margin rises above 6% (from 5.2%), showing integration is improving cash conversion.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 6}},
    {"text": "Net debt/EBITDA (ratios page) falls below 3.5x (from 3.97x TTM), showing deleveraging is under way and easing the balance-sheet distress flag."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 58.05, "basis": "Synergies ahead of schedule (Jefferies transcript) lift EBITDA and EV/EBITDA moves from 9.4x back toward its 5y range of 10.0x-11.5x [RA], reaching the mechanical base fair value of 58.05 (fact sheet)."},
    "base": {"probability": 0.45, "target_price_12m": 46.0, "basis": "EV/EBITDA stays near 9.4x [RA] while guided double-digit EPS growth (Q4 2026 transcript) adds modest equity value on a 3.97x-levered balance sheet; set below the DCF-led base of 58.05 because the EV/EBITDA method gives 27.07 (fact sheet)."},
    "bear": {"probability": 0.35, "target_price_12m": 35.88, "basis": "Macro overlay (secondary weight, moderate tilt toward bear: real yields +0.56pp, HY spreads +0.45pp) raised bear probability; ROIC keeps falling from 6.9% [RA] and the multiple compresses to the mechanical bear fair value of 35.88 (fact sheet)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: base fair value 58.05 x 0.8 = 46.44 is already above the price. What stops a BUY is falling ROIC, 3.97x leverage and an Altman Z of 1.37. Conviction 4 needs evidence of deleveraging and recovering returns (e.g. at the Nov 4, 2026 results), not a lower price.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Kimco Realty Corporation (KIM) — 2026-10-12
## Bear case
The price already sits on base fair value: 22.16 vs a P/FFO-proxy base of 22.61 (+2.1%), with the bear at 21.18 [Certain]. That leaves no margin of safety. The scarce grocery-anchored real estate is not turning into shareholder returns. ROIC is only 4.0% TTM, and ROE fell from 10.7% to 5.8% over five years [Certain]. Both are likely below the cost of capital when the 10y Treasury is at 5.22% [Likely]. Net debt/EBITDA of 6.12x leaves the equity exposed to refinancing at higher rates. The macro overlay tilts moderately toward bear, because real yields rose 0.56pp in 3m and the curve still leans toward tightening [Likely]. Versus peers, KIM is not cheap: +14% on P/E and +2% on EV/EBITDA [Certain]. Short interest is up 22.3% in a month [Certain]. Relative strength is -14.7pp vs SPY over 3m, and nothing fundamental shows a turn [Certain].

## Bull case
Retail supply is tight. Management reports record small-shop occupancy, raised 2026 guidance and a 12% dividend increase in Q2 [Likely]. Leverage has fallen from 8.81x to 6.12x and ROIC has edged up from 3.1% to 4.0%, so the balance sheet is improving [Certain]. EV/EBITDA of 17.3x and EV/Sales of 10.5x sit in the bottom 4% of their own 5y ranges [Certain]. P/B is 1.4x, 49% below peers [Certain]. If real yields ease, cap rates compress and the stock could re-rate toward the bull fair value of 31.17 (+40.7%) [Likely]. Q3 results on Oct 29 could confirm the leasing momentum [Guessing]. This is a good asset at a fair price. It is not a mispriced one.

## Decision
```json
{
  "ticker": "KIM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A quality grocery-anchored REIT with improving leverage, priced at its base fair value, offers no margin of safety while low ROIC and a rising-real-yield backdrop cap the upside case.",
  "rationale": "Price 22.16 sits at base fair value 22.61 and bear 21.18 is only 4% below. ROIC of 4.0% and 6.12x leverage give a thin buffer with real yields rising (macro overlay: moderate tilt toward bear). Good business, not compelling at this price. Conviction 3 is below the buy threshold, so AVOID and set an entry price.",
  "price_at_decision": 22.16,
  "price_date": "2026-10-09",
  "research_note": "research/KIM/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC falls below 3%, reversing the FY2021-TTM recovery from 3.1% to 4.0% [RA].", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 3}},
    {"text": "TTM ROE falls below 4%, extending the five-year decline from 10.7% to 5.8% [RA].", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 4}},
    {"text": "Net debt/EBITDA (site definition, ratios page) rises back above 7x, undoing the deleveraging from 8.81x to 6.12x [RA]."}
  ],
  "scenarios": {
    "bull": {"probability": 0.15, "target_price_12m": 31.17, "basis": "Real yields ease and the record occupancy shown in the Q2 2026 call turns into FFO growth, so the stock re-rates to the P/FFO-proxy bull fair value of 31.17 [IS,BS,CF,RA,ST]; the probability is cut for the macro overlay's moderate tilt toward bear (research/KIM/2026-10-12-macro.md)."},
    "base": {"probability": 0.55, "target_price_12m": 22.61, "basis": "Steady leasing with ROIC around 4.0% [RA] keeps the stock near its P/FFO-proxy base fair value of 22.61 [IS,BS,CF,RA,ST]."},
    "bear": {"probability": 0.30, "target_price_12m": 21.18, "basis": "Real yields keep rising (DFII10 +0.56pp in 3m), which raises refinancing cost on 6.12x net debt/EBITDA [RA] and compresses the multiple to the bear fair value of 21.18; the probability is raised per the macro overlay's moderate bear tilt (research/KIM/2026-10-12-macro.md)."}
  },
  "entry_price": 18.09,
  "entry_basis": "valuation file: base 22.61 x 0.8 = 18.09; at that level the same evidence would give a 20% margin of safety against the low-ROIC and rate risks.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: A. O. Smith Corporation (AOS) — 2026-10-07
## Bear case
Returns are eroding, not just de-rating: ROIC has fallen from 40.6% (FY2022) to 23.0% TTM and ROCE from 31.9% (FY2025) to 24.9% TTM [Certain]. China is in structural decline after subsidies ended, and the only remedy on offer is an open-ended strategic review [Likely]. Management narrowed FY2026 EPS guidance downward and excludes tariff effects [Certain]. That leaves an unquantified risk into the Oct 29, 2026 print [Likely]. Net debt/EBITDA moved from net cash to 0.63x after the debt-funded Leonard Valve deal while buybacks continue [Certain]. Price action is weak: -22.4% over 12 months, -38.8pp versus SPY, and 9.80% of float is short [Certain]. The low multiple may be a value trap. It could reflect a lower earnings base, not mispricing. Cheapness against peers is modest: EV/EBITDA is 10.4x vs a 11.7x peer median [Certain].
## Bull case
The North America replacement-driven water-heater duopoly still produces rising gross (38.6%) and operating (18.2%) margins [Certain]. Every multiple sits below its own 5-year minimum: P/FCF is 12.0x vs a 17.1x floor, and the FCF yield is 8.37% [Certain]. FCF conversion is 127.8% TTM and the share count fell 3.71% YoY, so holders compound even without a re-rating [Certain]. Leverage of 0.63x is still low and Altman Z is 6.56 [Certain]. If China is resolved through a partnership or exit, the market may value the higher-quality North American business on its own merits [Guessing]. With 9.80% short interest, a clean Q3 could squeeze the shorts [Guessing].
## Decision
```json
{
  "ticker": "AOS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cash-generative North America water-heater duopolist trades below its own 5-year minimum multiples at an 8.37% FCF yield, but falling ROIC, a China drag, rising leverage and a guidance cut make the discount look partly earned rather than clearly mispriced.",
  "rationale": "Cheap on its own history but only modestly below peers (EV/EBITDA 10.4x vs 11.7x). ROIC is falling, leverage is rising, China is unresolved and Q3 lands Oct 29 with tariffs excluded from guidance. Good but not compelling: conviction 3 is below the owner's buy threshold of 4, so AVOID. Cash is acceptable.",
  "price_at_decision": 56.90,
  "price_date": "2026-10-06",
  "research_note": "research/AOS/2026-10-07.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, showing the decline from 30.0% (FY2025) to 23.0% TTM is continuing rather than stabilising (would deepen AVOID; stabilisation above 23% would argue for re-review).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM gross margin falls below 35%, under the FY2022 5-year low of 35.4%, indicating North America pricing power is breaking.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 35}},
    {"text": "TTM operating margin falls below the FY2022 5-year low of 16.6%, showing China and tariffs are eroding group profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 16.6}},
    {"text": "North America segment sales (10-Q) decline for two consecutive quarters, breaking the replacement-demand core of the thesis; conversely, a completed China partnership/exit with NA growth intact would prompt re-evaluation for BUY."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 68.00, "basis": "China strategic review resolves and EV/EBITDA re-rates from 10.4x toward its 5y median 12.3x [RA] on flat TTM EBITDA [IS], with 0.63x net leverage [BS,IS] adding little drag."},
    "base": {"probability": 0.45, "target_price_12m": 60.00, "basis": "Multiples stay near the current 15.4x P/E [RA] while the 8.37% FCF yield [ST] and -3.71% YoY share count [ST] lift per-share value modestly as North America offsets China."},
    "bear": {"probability": 0.30, "target_price_12m": 47.00, "basis": "Q3 (Oct 29, 2026 [OV]) brings further guidance cuts and tariff costs; ROIC keeps falling from 23.0% TTM [RA] and earnings drop roughly a fifth at an unchanged 15.4x P/E [RA], breaking the 54.16 52-week low [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

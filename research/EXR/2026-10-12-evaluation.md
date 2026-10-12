# Evaluation: Extra Space Storage Inc. (EXR) — 2026-10-12
## Bear case
Returns on capital have structurally reset, not cycled: ROIC fell from 8.9% (FY21) to 5.4% TTM and ROE from 26.1% to 7.0% [Certain] [RA]. Leverage is drifting up (net debt/EBITDA 5.55x to 5.94x, site definition) while growth depends on external funding: 2.02% share dilution, a $1.5bn bridge-loan book and new bond issuance [Certain] [ST, note]. Real yields and HY spreads are still rising, which hits both the discount rate and marginal funding cost versus the 4.90% June note [Certain] (macro overlay, FRED DFII10/BAMLH0A0HYM2). Same-store revenue growth is only 2.4% with new supply a cited risk [Likely] (Q2 transcript). A 3.58% FCF yield sits below the 5.22% 10y Treasury [Certain] [ST, fact sheet]. The base fair value implies only +12.5%, while the stock lags SPY by 21.1pp over 12 months with no sign of a turn [Certain] [HI]. A CEO handover on 2027-01-01 adds execution noise [Certain] (PRNewswire).

## Bull case
EXR is the largest US self-storage operator with a fee-earning third-party platform that feeds acquisitions and a pricing-technology edge in a fragmented market [Certain] (10-K, sec.gov). EV/EBITDA of 18.8x sits at the 2nd percentile of its 5y range (18.5x-33.0x) and in line with peers, so the ROIC decline looks priced [Certain] [RA]. Operations are steady: Q2 FFO/share +4.9%, occupancy 94.2%, and 2026 guidance raised [Likely] (Q2 transcript). Fair value base 151.54 is +12.5% and bull 202.61 is +50.5% [Certain] (fact sheet). If real yields roll over, REIT multiples re-rate toward the 20.2x 5y median EV/EBITDA [Guessing] (macro overlay). Short interest is low at 2.33% [Certain] [ST].

## Decision
```json
{
  "ticker": "EXR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "The largest US self-storage operator trades at the bottom of its own 5-year EV/EBITDA range, but falling ROIC, rising leverage and a rate-sensitive, externally funded growth model leave only modest, macro-exposed upside to base fair value.",
  "rationale": "Cheap against its own history, but the business is deteriorating (ROIC 8.9% to 5.4%, leverage up) and the overlay tilts moderately to bear as yields and spreads keep rising. A +12.5% base upside does not compensate for that. Good but not compelling, so no position; buy only with a full margin of safety.",
  "price_at_decision": 134.65,
  "price_date": "2026-10-09",
  "research_note": "research/EXR/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC falls below 4.5%, extending the decline from 8.9% (FY2021) to 5.4% TTM and showing returns are still eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 4.5}},
    {"text": "Net debt/EBITDA rises above 6.5x (5.94x TTM, site definition), showing external growth is being funded by more leverage.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 6.5}},
    {"text": "Same-store occupancy in the quarterly earnings release falls below 92% (94.2% in Q2 2026), or same-store revenue growth turns negative."},
    {"text": "Reported same-store revenue growth and FFO/share growth both reaccelerate in the Q3/Q4 2026 releases while TTM ROIC stops falling, which would show returns have troughed (positive trigger for re-evaluation)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 152.0, "basis": "Real yields roll over and EV/EBITDA re-rates from 18.8x toward its 5y median 20.2x [RA], about the base fair value 151.54 (fact sheet); below the mechanical bull 202.61 because falling ROIC [RA] argues against a return to past peak multiples; probability trimmed for the overlay's moderate bear tilt (research/EXR/2026-10-12-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 138.0, "basis": "Steady operations (occupancy 94.2%, raised 2026 guidance, Q2 transcript) offset by ROIC stuck near 5.4% [RA] keep EV/EBITDA near today's 18.8x [RA], below base fair value 151.54 because the overlay's moderate bear tilt on rising real yields lowers the range (research/EXR/2026-10-12-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 118.0, "basis": "Real yields and HY spreads keep widening while leverage rises past 6x net debt/EBITDA [RA], pushing value below the mechanical bear 127.96 and the 52-week low 125.71 [HI], as the macro overlay's bear chain describes (research/EXR/2026-10-12-macro.md); probability raised for its moderate bear tilt."}
  },
  "entry_price": 121.23,
  "entry_basis": "valuation file: base 151.54 x 0.8 (fact sheet fair value); at that level the margin of safety would compensate for the ROIC decline and rate exposure.",
  "replaces": null,
  "replacement_reason": null
}
```

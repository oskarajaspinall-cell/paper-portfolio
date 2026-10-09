# Evaluation: Textron Inc. (TXT) — 2026-10-09
## Bear case
Cash conversion is getting worse. FCF margin fell from 9.9% (FY21) to 5.0% TTM, and FCF/net income from 163.9% to 81.0% [Certain] (CF,IS). On P/FCF, the multiple that matters most here, TXT is 16.7x versus a 13.8x peer median, a 21% premium [Certain] (RA). So the discount on P/E and EV/EBITDA is a quality discount, not a mispricing [Likely]. Buybacks (shares -4.30% YoY [ST]) are being funded from a shrinking FCF base, and net debt/EBITDA has risen from 1.28x to 1.65x [Certain] (BS,IS). Base fair value of 76.68 is only 4.7% above the 73.22 close, so the margin of safety is thin [Certain]. The macro overlay flags real yields up 61bp in 3m, which pressures business-jet financing for Textron Aviation, the largest segment [Likely] (research/TXT/2026-10-09-macro.md). Price momentum is poor: the stock is 18.0% below its 200-day average and lagging SPY by 30.0pp over 12m [Certain] (HI). Q3 results are due Oct 29 [Certain].

## Bull case
TXT trades below its own 5y minimum on P/E (14.0x vs 16.7x), EV/EBITDA (9.2x vs 10.8x) and P/B (1.6x vs 1.9x), and at a 28-44% discount to its defense peers [Certain] (RA). Returns are steady: ROIC 9.6%, ROE 12.1%, and ROCE up 1.2pp over five years [Certain] (RA). Bell and Textron Systems give long-cycle, high-switching-cost defense revenue, which the macro overlay rates as rate-insensitive [Likely]. The price implies only 4.5% revenue growth in year 1 [Certain] (fair value section). The EV/EBITDA method alone puts fair value at 86.66-90.66 [Certain]. A 4.30% annual share-count reduction compounds per-share value [Certain] (ST). If FCF conversion normalises, the bull DCF of 156.63 shows how much upside a cash recovery would unlock [Guessing].

## Decision
```json
{
  "ticker": "TXT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "TXT looks cheap on earnings multiples against its history and its defense peers, but five years of falling FCF conversion and a P/FCF premium to peers mean the discount reflects weaker cash quality, and base fair value sits only 4.7% above the price.",
  "rationale": "This is a mediocre-quality business (ROIC 9.6%, FCF margin falling to 5.0%), not a mispriced compounder. The earnings-multiple discount disappears on P/FCF, where TXT trades at a premium to peers. Base fair value gives only 4.7% upside, and the macro tilt points toward the bear case. Good but not compelling, so no position.",
  "price_at_decision": 73.22,
  "price_date": "2026-10-08",
  "research_note": "research/TXT/2026-10-09.md",
  "triggers": [
    {"text": "TTM FCF margin recovers above 7%, showing the five-year cash-conversion decline has reversed.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 7}},
    {"text": "TTM ROIC rises above the FY2023 peak of 11.9%, showing returns are improving rather than flat.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 11.9}},
    {"text": "Net debt/EBITDA rises above 2.0x, showing buybacks are being funded with leverage rather than FCF (would further weaken the case).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "The Q3 2026 10-Q (Oct 29) shows Aviation or Bell backlog falling materially year on year."}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 90.57, "basis": "FCF conversion stabilises and EV/EBITDA re-rates from 9.2x toward its 5y minimum of 10.8x [RA], matching the EV/EBITDA-method base of 90.57. This is set below the 134.64 blended bull because that figure assumes the DCF's full cash-recovery growth, which the falling FCF trend [CF,IS] does not support. Probability is cut for the moderate bear macro tilt (research/TXT/2026-10-09-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 76.68, "basis": "Margins and FCF stay near TTM levels (operating 8.4%, FCF 5.0% [IS,CF]), and the price converges on the blended DCF/EV-EBITDA base fair value of 76.68 [fact-sheet fair value]."},
    "bear": {"probability": 0.35, "target_price_12m": 65.21, "basis": "FCF conversion keeps falling (81.0% TTM [CF,IS]), and real yields rising past 3.25% squeeze Aviation financing and the discount rate. The price moves to the 65.21 blended bear fair value. Probability is raised for the moderate bear macro tilt (research/TXT/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

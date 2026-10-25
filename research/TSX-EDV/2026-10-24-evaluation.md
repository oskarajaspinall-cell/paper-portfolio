# Evaluation: Endeavour Mining plc (TSX:EDV) — 2026-10-24
## Bear case
Endeavour takes whatever gold sells for, and its returns are at a cyclical peak. ROIC went from -20.7% in FY2024 to 35.3% TTM and operating margin from 14.9% to 43.2% [RA,IS] because the gold price rose, not because the business got better [Likely]. The cheap multiples (EV/EBITDA 4.3x, P/FCF 8.5x) are built on those peak earnings. On P/E (14.9x, above peers) and P/B (3.3x, near its 5y max) the stock is expensive [Certain]. The mechanical base fair value of 44.77 CAD and bear value of 37.54 sit far below the 71.89 close; only the bull case of 88.06 supports the price [Certain]. The macro overlay points toward the bear case: the 10y TIPS yield is up to 2.64% and the dollar index is firmer, both headwinds for gold [Likely]. Add West African sovereign and permit risk, the Ity fatality and Q3 results due Nov 12, 2026 [Certain].
## Bull case
The balance sheet is strong: net debt/EBITDA is -0.06x, Altman Z is 5.05 and Piotroski F is 8 [Certain]. A 30.2% FCF margin, an 11.74% FCF yield and FCF conversion of 171.0% [ST,CF] fund management's "nearly $2 billion" of shareholder returns since 2021 with almost no dilution: shares are up only 0.18% YoY [Likely]. EV/EBITDA is below its own 5y minimum of 4.4x and well under the 6.4x peer median [RA] [Certain]. Assafou and Sabodala-Massawa add growth [Likely]. A NAV valuation is not available, so the EV/EBITDA fair value may understate the value of the reserves [Guessing]. If gold holds, the stock compounds cash [Likely].
## Decision
```json
{
  "ticker": "TSX:EDV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash West African gold producer with peak-cycle 43.2% operating margins looks cheap on EV/EBITDA, but the price only works if gold stays strong, and the mechanical base value sits well below the price.",
  "rationale": "Balance sheet and cash returns are strong, but margins are gold-driven and at a peak. P/E and P/B are rich against peers and its own history, base and bear fair values sit far below the price, and macro tilts toward bear. The risk/reward is skewed to the downside: good, not compelling, so AVOID.",
  "price_at_decision": 71.89,
  "price_date": "2026-10-23",
  "research_note": "research/TSX-EDV/2026-10-24.md",
  "triggers": [
    {"text": "TTM operating margin falls below 30%, showing the gold-price margin expansion from 14.9% to 43.2% is reversing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM FCF margin falls below 15%, showing cash generation can no longer fund shareholder returns.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA rises above 1.0x (-0.06x TTM now), showing project capex or returns are being debt-funded.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Shares outstanding up more than 5% year on year (0.18% now), signalling dilutive funding.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 88.06, "basis": "Real yields ease and the dollar weakens so gold and the 43.2% TTM operating margin [IS] hold, reaching the mechanical bull fair value of 88.06 CAD; probability trimmed for the macro overlay's small tilt toward bear (research/TSX-EDV/2026-10-24-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 66.0, "basis": "Gold roughly holds and EV/EBITDA stays near 4.3x [RA] as margins ease slightly from the peak; set above the mechanical base of 44.77 CAD because the 11.74% FCF yield [ST] and net cash support value and NAV is unavailable, but below the price given the macro headwinds (research/TSX-EDV/2026-10-24-macro.md)."},
    "bear": {"probability": 0.35, "target_price_12m": 37.54, "basis": "Rising real yields and a firmer dollar push gold lower, operating margin compresses toward 30% and EBITDA falls back toward its 5y average, matching the mechanical bear fair value of 37.54 CAD; weighted up for the macro overlay's small tilt toward bear (research/TSX-EDV/2026-10-24-macro.md)."}
  },
  "entry_price": 35.82,
  "entry_basis": "valuation file: base 44.77 x 0.8 (20% margin of safety, fact sheet Fair value [IS,BS,CF,RA,ST,HI]); at that price even the mechanical bear case is covered and the same evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

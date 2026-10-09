# Evaluation: W. R. Berkley Corporation (WRB) — 2026-10-08

## Bear case
WRB is a quality franchise priced as one, not a mispricing [Certain]. P/E of 14.3x sits mid-range in its own 5y band (13.3x–15.7x) and P/B of 2.8x is at the 69th percentile, while it trades at a 34% P/E and 38% P/B premium to CB/TRV/MKL/RLI [Certain] (fact sheet, Valuation). The mechanical fair value base of 73.89 is only +6.0% above the 69.73 close; the bear value of 60.62 is −13.1%, so the payoff is roughly symmetric [Certain] (fact sheet, Fair value). Q2 commentary flags competitive pressure in reinsurance, and EPS growth leaned on record investment income [Likely] (fact sheet News, Q2 transcript), which is rate-dependent, not underwriting-earned. FCF conversion is drifting down (207%→180%) [Certain]. The stock has lagged SPY by 24.8pp over 12 months with short interest rising 4.0% [Certain] — the market sees a softening specialty cycle [Guessing].

## Bull case
Returns are improving while leverage falls: ROIC 11.7%→15.7%, ROE 15.9%→20.2%, site net debt/EBITDA 1.23x→0.19x [Certain] (fact sheet, Quality). A 12.8% FCF yield and P/FCF of 7.8x (23% below peers) fund buybacks (shares −1.11% YoY) and dividends without leverage [Certain]. The decentralized niche-unit model, still adding units such as Berkley Meridian, supports pricing discipline [Likely] (berkley.com; fact sheet News). The macro overlay tilts small toward bull: a real-rate-led rise in yields (10y 5.27%) lifts reinvestment yield on the float [Likely] (research/WRB/2026-10-08-macro.md). Beta of 0.27 makes it a portfolio diversifier [Certain]. Still, the upside to the bull fair value of 77.06 is only +10.5% [Certain] — a sound business without an attractive entry.

## Decision
```json
{
  "ticker": "WRB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-ROE, deleveraging specialty P&C insurer that is fairly priced against its own history and at a premium to peers, leaving limited upside versus a bear case that is larger than its bull case.",
  "rationale": "Quality is real, but valuation is not attractive: P/E and EV/EBITDA sit at their 5y medians, P/B is in the upper part of its range and above peers, and fair value upside is +6% base against −13% bear. Good but not compelling, so conviction is 3 and the owner rule means AVOID; cash is acceptable.",
  "price_at_decision": 69.73,
  "price_date": "2026-10-07",
  "research_note": "research/WRB/2026-10-08.md",
  "triggers": [
    {"text": "TTM ROE falls below 15%, under the FY2021-25 range (15.9%-22.1%), showing underwriting returns are fading.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 12%, back toward the FY2021 trough of 11.7%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA (site definition, Ratios page) rises back above 1.0x, reversing the FY2021-25 deleveraging."},
    {"text": "FCF conversion (FCF/net income) falls below 150%, extending its downtrend from 207% beyond the FY2021-25 range."}
  ],
  "scenarios": {
    "bull": {"probability": 0.28, "target_price_12m": 77.06, "basis": "ROE holds near the TTM 20.2% [RA] and the P/B + ROE fair value reaches its bull case of 77.06 [fact sheet Fair value]; probability raised from 0.25 by the overlay's small tilt toward bull as rising real yields lift float income (research/WRB/2026-10-08-macro.md)."},
    "base": {"probability": 0.50, "target_price_12m": 73.89, "basis": "Multiples stay near their 5y medians (P/E 14.6x, EV/EBITDA 10.7x [RA]) and the blended base fair value of 73.89 is reached [fact sheet Fair value]."},
    "bear": {"probability": 0.22, "target_price_12m": 60.62, "basis": "Reinsurance competition noted on the Q2 2026 call (fact sheet News transcript) softens returns and P/B derates toward its 5y low of 2.3x [RA], consistent with the bear fair value of 60.62; probability trimmed from 0.25 by the overlay's small bull tilt (research/WRB/2026-10-08-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

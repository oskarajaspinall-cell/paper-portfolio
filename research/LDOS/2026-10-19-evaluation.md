# Evaluation: Leidos Holdings, Inc. (LDOS) — 2026-10-19
## Bear case
Leidos depends on one buyer: US government customers were 83-85% of H1 2026 revenue [company-reported] (https://www.sec.gov/Archives/edgar/data/1336920/000133692026000246/ldos-20260703.htm), and the 10-Q flags FY2027 continuing-resolution and shutdown risk [Certain]. The stock fell from 160.79 to 98.86 in under three months, and neither the note nor the fact sheet explains why. It also trades well below peers (EV/EBITDA 9.0x vs a 12.8x peer median), so the discount may be company-specific, not just a sector de-rating [Guessing]. Net debt/EBITDA went back up to 2.45x after $1.4bn of notes for Entrust/Analogic, just as the 10y yield (5.10%) and HY spreads rose (macro overlay) [Certain]. The TTM FCF margin of 12.3% is well above FY2025's 9.5%, so the 13.80% FCF yield may overstate what the business earns normally [Likely]. Q3 results on Nov 3, 2026 are a binary near-term event [Certain].

## Bull case
Quality has improved a lot: ROIC rose from 9.9% to 14.2%, operating margin from 8.5% to 11.8% and gross margin from 14.7% to 17.8% [Certain]. Yet P/E 11.7x, EV/EBITDA 9.0x and P/FCF 7.2x all sit below their own 5-year minimums [Certain]. The reverse DCF implies -13.7% year-1 revenue, which contract incumbency with cleared staff and multi-year programmes makes unlikely [Likely]. Even the mechanical bear fair value (138.10) is above the 124.85 close [Certain]. A 13.80% FCF yield funds buybacks (shares -3.02% YoY) while debt comes down [Certain]. New awards keep coming (a Defense Health Agency contract, the MOD LCST extension) and the stock is up 15.3% over 3 months, which suggests the June panic is fading [Likely]. Beta of 0.59 and Altman Z of 3.44 limit the downside [Certain].

## Decision
```json
{
  "ticker": "LDOS",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A government-IT incumbent with ROIC up from 9.9% to 14.2% and a 13.80% FCF yield funding buybacks trades below its own 5-year minimum on every earnings multiple and below peers, where the price implies a -13.7% revenue decline that its contract base does not show.",
  "rationale": "Rising quality, a strong FCF yield and a price below even the mechanical bear value give a favourable skew. The unexplained mid-year crash, single-customer budget risk, re-levering for M&A, a bearish rate backdrop and results on Nov 3 hold conviction at 4, not 5: standard volatility-scaled core size.",
  "price_at_decision": 124.85,
  "price_date": "2026-10-16",
  "research_note": "research/LDOS/2026-10-19.md",
  "triggers": [
    {"text": "TTM operating margin falls below 10%, reversing the five-year expansion from 8.5% to 11.8%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 10%, erasing the improvement from 9.9% in FY2021 to 14.2%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM FCF margin falls below 6%, under the FY2022 five-year low of 6.0%, showing the cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "Net debt/EBITDA on the ratios page rises above 3.0x (2.45x TTM now) without a visible deleveraging path from the Entrust/Analogic debt."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 175.44, "basis": "EV/EBITDA returns to around its 5y median of 11.9x [RA] on TTM EBITDA, matching the EV/EBITDA bull fair value of 175.44 [IS,RA]; the blended DCF values of 300.72 and above are discounted because TTM FCF margin of 12.3% sits well above the FY2025 level of 9.5% [CF,IS]."},
    "base": {"probability": 0.45, "target_price_12m": 150, "basis": "EV/EBITDA recovers only partway toward its 5y minimum of 11.2x [RA] as margins hold near 11.8% [IS], below the EV/EBITDA base of 174.89 because the macro overlay's moderate bear tilt (10y yield 5.10%, HY spreads wider; research/LDOS/2026-10-19-macro.md) caps the re-rating."},
    "bear": {"probability": 0.30, "target_price_12m": 105, "basis": "A FY2027 continuing resolution or shutdown (10-Q, https://www.sec.gov/Archives/edgar/data/1336920/000133692026000246/ldos-20260703.htm) plus higher interest on the new notes push the stock back toward the July swing low of 103.90 [HI]; probability raised from a neutral weight for the macro overlay's moderate bear tilt (research/LDOS/2026-10-19-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

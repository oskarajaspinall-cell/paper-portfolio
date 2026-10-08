# Evaluation: Expand Energy Corporation (EXE) — 2026-10-08

## Bear case
EXE is a price-taker in natural gas with no moat beyond relative cost position; returns swung from ROIC 36.6% (FY2022) to -2.8% (FY2024) [Certain], and the 5y ROIC trend is falling (-6.3pp) [Certain]. The TTM recovery (operating margin 29.9%, FCF margin 19.6%) is a gas-price outcome, not a structural one [Likely]. Per-share value is leaking: shares outstanding are up 13.24% YoY despite buybacks [Certain], and the company layered a new senior notes offering on top of the Twin Eagle acquisition [Certain]. Net debt/EBITDA went from 0.28x to 4.42x in a single down-cycle year (FY2024) [Certain], so today's 0.46x offers limited comfort. The macro overlay tilts small toward bear as real yields and HY spreads rise [Likely]. The stock trades below both its 50- and 200-day averages with short interest up 13.8% [Certain]; the cheap multiple may simply be a cyclical-peak earnings trap [Guessing].

## Bull case
On every multiple EXE is cheap: EV/EBITDA 3.5x, at the 4th percentile of its 5y range and 40% below the 5.8x peer median; P/FCF 8.2x vs 12.5x peers; FCF yield 12.14% [Certain]. Leverage is low at 0.46x net debt/EBITDA and Piotroski F-score is 8 [Certain]. FCF conversion has recovered to 89.1% TTM [Certain]. Scale from the merger plus Twin Eagle's marketing and storage integration could lower breakevens and smooth earnings versus pure producers [Likely]. The shares have underperformed SPY by 34.5pp over 12 months, so much of the rate/credit and sentiment damage looks priced [Likely]. A return merely to the 5y median EV/EBITDA of 4.4x would be a meaningful re-rate, and buybacks plus the dividend pay investors to wait [Likely].

## Decision
```json
{
  "ticker": "EXE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-cost, low-leverage gas producer trades at the bottom of its own 5-year EV/EBITDA range and well below peers, but its returns are set by the gas price, not a moat, and per-share value is being diluted.",
  "rationale": "Cheap, but cheap for a reason: a commodity price-taker with a falling 5y ROIC trend, 13.24% share-count growth, fresh debt issuance and a small bear macro tilt. The discount is real but not compelling enough for a 7% core position; cash is the better outcome. Revisit if per-share discipline and through-cycle returns are proven.",
  "price_at_decision": 88.12,
  "price_date": "2026-10-07",
  "research_note": "research/EXE/2026-10-08.md",
  "triggers": [
    {
      "text": "Shares outstanding shrink year-on-year (shares change YoY turns negative), showing buybacks now outpace merger/acquisition issuance.",
      "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": 0}
    },
    {
      "text": "TTM ROIC rises above 15%, above the FY2021 level of 15.4%, reversing the falling 5y returns trend.",
      "check": {"source": "statistics", "field": "roic", "op": ">", "value": 15}
    },
    {
      "text": "TTM FCF margin rises above 20%, showing the Twin Eagle marketing integration is lifting cash generation beyond the TTM 19.6%.",
      "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 20}
    }
  ],
  "scenarios": {
    "bull": {
      "probability": 0.25,
      "target_price_12m": 114,
      "basis": "EV/EBITDA re-rates from 3.5x to its 5y median 4.4x [RA] on TTM EBITDA with net debt/EBITDA held at 0.46x [RA], as the peer discount of -40% [P:EQT,P:AR,P:RRC,P:CTRA,P:CNX] narrows."
    },
    "base": {
      "probability": 0.45,
      "target_price_12m": 88,
      "basis": "EV/EBITDA stays at 3.5x [RA]; the 12.14% FCF yield [ST] funds debt paydown and buybacks but is offset by 13.24% share-count growth [ST], leaving the price flat; probability shifted from 0.50 by the overlay's small toward-bear macro tilt (research/EXE/2026-10-08-macro.md)."
    },
    "bear": {
      "probability": 0.30,
      "target_price_12m": 71,
      "basis": "Gas-driven earnings fade and EV/EBITDA falls to its 5y minimum 2.9x [RA] on TTM EBITDA, as in FY2024 when ROIC hit -2.8% [RA]; probability raised from 0.25 by the overlay's small toward-bear tilt on rising real yields and HY spreads (research/EXE/2026-10-08-macro.md)."
    }
  },
  "replaces": null,
  "replacement_reason": null
}
```

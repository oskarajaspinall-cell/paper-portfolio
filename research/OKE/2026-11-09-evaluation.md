# Evaluation: ONEOK, Inc. (OKE) — 2026-11-09
## Bear case
Cash is not following earnings. FCF conversion has fallen from 123.3% (FY2021) to 62.2% TTM, and FCF margin dropped from 9.3% to 5.9% in the last 12 months, 7.8pp below its 2-year high [Certain]. Operating margin fell from 18.0% to 14.2% over the same year, contradicting the 5-year "rising" read [Certain]; if this is cost creep rather than commodity mix and timing, the EBITDA cheapness is illusory [Guessing]. P/FCF of 21.2x sits above its 5y maximum, so on cash the stock is not cheap [Certain]. Q3 net income was lifted by a one-time noncash tax benefit, flattering P/E [company-reported]. The $4.6 billion Brazos deal was partly funded by Apollo Class B units, a costly claim ranking ahead of common [Likely]; shares rose 2.75% YoY and Altman Z is 1.65 [Certain]. The mechanical fair value is flagged unreliable, with the bear at 77.94 below the price [Certain].

## Bull case
About 90% of 2026 earnings are fee-based under minimum-volume and take-or-pay contracts [company-reported], and the integrated gathering-to-export network is hard to replicate [Likely]. Returns are not deteriorating: rolling ROIC rose from 8.0% to 8.8%, its 2-year high, and net debt/EBITDA fell from 5.29x (FY2024) to 3.68x, with S&P and Fitch lifting ratings to BBB+ [company-reported]. Q3 beat and FY2026 guidance was raised again, including Brazos [Certain]. The margin dip is consistent with acquisition and growth-capex timing and commodity-linked revenue mix, not pricing erosion [Likely]. The stock trades below its 5y minimum P/E and at its 5y minimum EV/EBITDA of 10.7x, and below peers by 37% on P/E and 19% on EV/EBITDA [Certain]. The reverse DCF implies only 3.3% year-one growth, a modest hurdle against raised guidance [Likely]. Macro is context only (research/OKE/2026-11-09-macro.md).

## Decision
```json
{
  "ticker": "OKE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating and FCF margin fell over the last year while rolling ROIC rose to its 2-year high of 8.8% [RA-T] and leverage fell to 3.68x [BS,IS]; Q3 beat and FY2026 guidance was raised again including Brazos (https://www.globenewswire.com/news-release/2026/10/27/3389643/0/en/oneok-announces-higher-third-quarter-2026-earnings-and-increases-2026-financial-guidance.html), consistent with acquisition/growth-capex timing and commodity-linked revenue mix rather than lost share or a price cap.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "FCF conversion keeps falling (62.2% TTM) after Brazos, so EBITDA cheapness never turns into cash while the Apollo Class B claim ranks ahead of common.",
    "veto": null
  },
  "thesis": "A fee-based US midstream network that is cheap on EBITDA against its own history and peers, but with ROIC below 10%, leverage near 3.7x and falling cash conversion, is an adequate business at a fair cash price rather than a high-conviction opportunity.",
  "rationale": "Python's scorecard sets conviction 2: ROIC of 8.8% and 3.68x leverage score nothing on quality or balance sheet, and with the fair value unreliable the value upside is small. EBITDA cheapness is offset by P/FCF above its 5y high and 62.2% FCF conversion. No position; cash is an acceptable outcome.",
  "price_at_decision": 85.19,
  "price_date": "2026-11-06",
  "research_note": "research/OKE/2026-11-09.md",
  "new_evidence": {"type": "new_information", "text": "No new company evidence since the 2026-11-08 AVOID 3: the change is that Python's conviction scorecard (owner-approved 2026-11-09, scripts/scorecard.py) now sets CORE conviction, and it scores this same evidence at 2. The decision, AVOID, is unchanged."},
  "triggers": [
    {"text": "TTM ROIC rises above 10% (8.8% now), lifting returns into the quality band that would make the EBITDA cheapness worth owning.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 10}},
    {"text": "Net debt/EBITDA falls below 3.0x (3.68x now) with Brazos in the numbers, showing the deleveraging is durable.", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 3.0}},
    {"text": "TTM FCF margin recovers above 9.3%, its level a year earlier (5.9% now), showing the margin dip was timing and investment.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 9.3}},
    {"text": "TTM FCF conversion (FCF/NI, cash-flow and income-statement pages) returns above 94.5%, its FY2024 level, meaning growth spending is turning into cash."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 110.0, "basis": "Raised guidance plus Brazos lift EBITDA and EV/EBITDA re-rates toward its 5y median 12.6x [RA]; well below the mechanical bull of 381.97 because the fair value is flagged unreliable (methods disagree 2.5x)."},
    "base": {"probability": 0.5, "target_price_12m": 95.0, "basis": "EBITDA grows with the raised guide and EV/EBITDA recovers partway from its 5y minimum 10.7x [RA]; below the blended base of 101.12 because the DCF leg extrapolates and FCF conversion is only 62.2% [CF,IS]."},
    "bear": {"probability": 0.25, "target_price_12m": 72.0, "basis": "FCF conversion keeps falling and the multiple stays at its 5y floor while the Apollo claim and 2.75% share growth dilute common [ST]; below the mechanical bear of 77.94, toward the EV/EBITDA bear of 37.41 only partly, since contracts are about 90% fee-based [company-reported]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2 is below the entry-price threshold; the obstacle is quality (ROIC below 10%, leverage, cash conversion), which a lower price would not fix.",
  "replaces": null,
  "replacement_reason": null
}
```

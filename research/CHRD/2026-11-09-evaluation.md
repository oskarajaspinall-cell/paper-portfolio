# Evaluation: Chord Energy Corporation (CHRD) — 2026-11-09
## Bear case
Chord is a Bakken price-taker with revenue almost all WTI-linked crude [Certain]. The 10-Q ties the current oil price to the Strait of Hormuz closure and OPEC+ [Certain]; WTI rose from $81.96 to $99.64 in three months (macro overlay), so TTM earnings likely sit on a geopolitical premium that can reverse quickly [Likely]. The Direction change line matters: operating margin fell over the last 12 months (20.3% to 18.9%) and is 11.3pp below its 2-year high even as oil rose, which points to cost or realised-price pressure, not only the cycle [Likely]. The cheap 2.9x EV/EBITDA is cheap on near-peak EBITDA; the mechanical base fair value of 155.31 rests on EV/EBITDA alone, with NAV [data unavailable] [Certain]. Altman Z 1.76, Piotroski F 5, a new CEO from 19 Oct 2026 and share count up 0.33% (buybacks not shrinking it) add uncertainty [Certain].

## Bull case
The balance sheet is strong: net debt/EBITDA 0.26x [Certain]. FCF margin rose over the last 12 months (17.6% to 22.3%), now at its 2-year high, and the FCF yield is 19.42% [Certain]; more than 75% of Q3 free cash flow goes to shareholders (transcript) [Likely]. The 3-year falls in ROIC and margins reflect oil normalising from the 2022 peak with the balance sheet intact, i.e. cyclical rather than structural [Likely]; ROIC recovered from 4.8% to 10.3% in a year [Certain]. On every multiple it trades below peers (EV/EBITDA 41% below, P/FCF 53% below) and near the bottom of its own 5y range [Certain]. Headlines report a Q3 EPS beat and raised FY26 EBITDA guidance [Likely]. The Marcellus sale ($550.0 million [company-reported]) sharpens the oil focus [Certain].

## Decision
```json
{
  "ticker": "CHRD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "The 3-year falls in ROIC and margins track oil normalising from the FY2022 peak (ROIC 46.0% in FY2022) with net debt/EBITDA at 0.26x [RA,BS]; over the last 12 months ROIC (4.8% to 10.3%) and FCF margin (17.6% to 22.3%) recovered [RA-T,CF-T]. The 1-year operating-margin slip (20.3% to 18.9%) is the cyclical cost/realised-price mix, not lost share (note §2).",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "WTI is elevated by the Hormuz closure and OPEC+ (10-Q, https://www.sec.gov/Archives/edgar/data/1486159/000148615926000047/chrd-20260930.htm); a de-escalation toward the ~$80 of August (macro overlay) would roll TTM earnings and FCF off sharply.",
    "veto": null
  },
  "thesis": "A low-leverage, high-FCF Bakken oil producer trading at a trough multiple, but on earnings inflated by a geopolitical oil premium that can reverse.",
  "rationale": "Cheap on every multiple with a strong balance sheet and heavy cash returns, but there is no moat, the value-blend upside is thin and earnings depend on an oil price the 10-Q links to the Hormuz closure. The scorecard gives conviction 2, below the buy bar (owner rule: high conviction only), so AVOID.",
  "price_at_decision": 136.49,
  "price_date": "2026-11-06",
  "research_note": "research/CHRD/2026-11-09.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 6%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 6}},
    {"text": "FCF margin (TTM) falls below 15%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA rises above 1.5x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "Shares outstanding rise more than 3% year on year (dilutive M&A or issuance)", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 159.44, "basis": "WTI holds above ~$90 (macro overlay), FCF margin stays near the TTM 22.3% [CF-T] and EV/EBITDA re-rates to the mechanical bull fair value of 159.44 [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 145, "basis": "Oil eases partly; EV/EBITDA moves toward its 5y median 3.5x [RA] on lower EBITDA, landing below the mechanical base 155.31 because the macro overlay's moderate bear tilt (geopolitical oil premium) trims the earnings base."},
    "bear": {"probability": 0.35, "target_price_12m": 105, "basis": "A Hormuz de-escalation sends WTI toward ~$80 (macro overlay, whose moderate bear tilt raises this probability), TTM earnings roll off and the price falls below the mechanical bear 114.28 as EV/EBITDA near its 5y low 2.6x [RA] applies to lower EBITDA."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

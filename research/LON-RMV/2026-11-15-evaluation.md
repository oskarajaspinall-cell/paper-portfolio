# Evaluation: Rightmove plc (LON:RMV) — 2026-11-15
## Bear case
The stock has run hard: +41.8% in six months, 26.3% above its 200-day average, RSI 68.7 [Certain]. Part of that is takeover speculation after Reuters reported activist Sachem Head pressing for a sale, which is sources-based and unconfirmed [Likely]. If no bidder appears, that premium can unwind quickly toward the 200-day average [Likely]. Meanwhile the business is slowing: management guided 2027 revenue growth similar to 2026, with new-homes weakness a drag and UK housing conditions "challenging" [Likely]. Operating margin has slipped from 73.4% (FY2021) to 66.7% TTM and sits 2.3pp below its 2-year high; FCF margin is 2.3pp below its 2-year high [Certain]. A five-year margin drift in a near-monopoly can signal rising cost to defend share or reinvest in AI [Guessing]. Piotroski F is only 4 [Certain]. With no computable fair value, the upside anchor is weaker than usual [Certain].
## Bull case
Rightmove is the UK's dominant property portal: 100% gross margin, 66.7% operating margin, 54.3% FCF margin, FCF conversion 109.1%, net cash [Certain]. The network effect (agents must list where buyers are) has kept ROIC near 500% for five years [Likely]. The last 12 months are stable rather than deteriorating: ROIC +30.3pp, FCF margin +0.4pp, operating margin only -1.5pp, consistent with a cyclical new-homes trough and product investment rather than lost share [Likely]. Even after the rally, P/E 20.4x sits at 12% of its 5y range, EV/EBITDA 14.1x at 4%, P/FCF 17.7x at 5%, below the peer medians of 25.4x P/E and 20.2x EV/EBITDA, with a 5.66% FCF yield [Certain]. Buybacks shrink the share count 2.63% a year [Certain]. An activist pushing a sale adds optionality, not dependence [Likely].
## Decision
```json
{
  "ticker": "LON:RMV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating margin is 1.5pp lower over 12 months while FCF margin (+0.4pp) and ROIC (+30.3pp) rose; the 2026-11-06 trading update ties the slowdown to a cyclical new-homes slump (https://www.reuters.com/world/uk/uks-rightmove-sees-2027-revenue-growth-similar-2026-due-homebuilding-slump-2026-11-06/), with net cash intact [BS].",
    "moat": "wide",
    "key_risk": "medium",
    "key_risk_text": "The price is extended (26.3% above its 200-day average) partly on unconfirmed activist sale speculation; if no bid emerges while 2027 growth stays subdued, the stock de-rates.",
    "veto": null
  },
  "thesis": "The UK's dominant, net-cash property portal with stable rolling returns trades at the bottom of its own 5-year multiple range, but the recent rally rests partly on unconfirmed bid speculation while growth is guided flat.",
  "rationale": "Exceptional, cash-rich franchise at the cheap end of its own history, but the scorecard does not reach the buy bar: no computable fair value, a trend lifted by takeover speculation and a slowing 2027 guide. Good but not compelling; cash is acceptable.",
  "price_at_decision": 582.20,
  "price_date": "2026-11-13",
  "research_note": "research/LON-RMV/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 62% (66.7% now), showing competition or cost of defence is eroding the franchise.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 62}},
    {"text": "TTM FCF margin falls below 49% (54.3% now), showing cash generation is deteriorating.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 49}},
    {"text": "TTM ROIC falls below 350% (497.4% now), a break well below the five-year range.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 350}},
    {"text": "Company-reported revenue growth guidance is cut again, or agent/developer advertiser numbers fall in two consecutive reports (RNS)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 680, "basis": "A bid emerges from the Sachem Head sale push (Reuters 2026-11-13) or P/E re-rates toward its 5y median 23.1x [RA] on stable TTM earnings [IS]."},
    "base": {"probability": 0.5, "target_price_12m": 600, "basis": "P/E holds near the current 20.4x [RA] while buybacks (shares -2.63% YoY [ST]) and growth guided similar to 2026 (Reuters 2026-11-06) lift EPS modestly."},
    "bear": {"probability": 0.25, "target_price_12m": 470, "basis": "Bid speculation fades and P/E falls back to its 5y low 18.2x [RA] with weak new-homes demand, the price returning toward its 200-day average 460.93 [ST,HI]."}
  },
  "entry_price": 519,
  "entry_basis": "Fair value is [data unavailable] (no GBP FX rate), so anchored on P/E back at its 5y low of 18.2x [RA] on TTM earnings: the same evidence at the floor of its own history would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

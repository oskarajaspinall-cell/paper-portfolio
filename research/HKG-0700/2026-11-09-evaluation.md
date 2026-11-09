# Evaluation: Tencent Holdings Limited (HKG:0700) — 2026-11-09
## Bear case
The cheapness is on earnings, not cash: FCF margin fell to 21.3% TTM from 26.6% a year earlier, 13.3pp below its 2-year high [Certain] (CF-T), and P/FCF of 19.5x sits 60% up its 5y range [Certain] (RA). That decline contradicts the 5-year rising FCF trend; if AI capex is the cause [Guessing], the payback depends on compute Tencent may not be able to get: Oracle reportedly cancelled a chip-leasing deal under US pressure [Likely] (Reuters URL in note). The mechanical DCF base, which carries a 3.5% China risk premium, is 228.95 HKD and the blended base 337.13 HKD, both below the 419.80 close; the reverse DCF implies 21.6% year-1 revenue growth [Certain] (fact sheet). Mainland policy and VIE risk sit outside any model [Likely]. The price trend is weak: -33.7% over 12 months, below the 200-day average [Certain] (ST, HI).
## Bull case
Quality is rising on a rolling basis: ROIC 18.3% TTM vs 15.3% a year earlier, operating margin 33.3% vs 31.6%, both at 2-year highs [Certain] (RA-T, IS-T). Since operating profit is expanding, the FCF dip reads as heavy investment, not a broken model [Likely]. The messaging/social network effect feeds games, ads and payments, and widening gross margin (56.7% vs 43.9% in FY2021) signals pricing power [Likely] (IS). P/E of 14.3x and EV/EBITDA of 10.9x are below their 5y minimums and well under peer medians of 19.1x and 15.5x [Certain] (RA). Net debt/EBITDA is 0.04x and shares fell 1.10% YoY [Certain] (ST). The EV/Revenue base of 553.51 HKD sits above the price [Certain]; the fair value is flagged unreliable, so the cheapness on own-history multiples carries more weight [Likely]. Results on 2026-11-18 could show AI spend converting [Guessing].
## Decision
```json
{
  "ticker": "HKG:0700",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell to 21.3% TTM from 26.6% while operating margin rose to 33.3% from 31.6% and ROIC to 18.3% from 15.3% [CF-T, IS-T, RA-T]; earnings are expanding, so the cash drop points to heavy investment (likely AI capex, not shown on the fact sheet), with net debt/EBITDA 0.04x intact.",
    "moat": "wide",
    "key_risk": "medium",
    "key_risk_text": "US-China tech restrictions (the reported Oracle chip-leasing cancellation) and China policy limit AI compute and the return on the capex that is depressing FCF; a wider China discount would keep the multiple at its lows.",
    "veto": null
  },
  "thesis": "A wide-moat Chinese platform with rising ROIC and operating margin trades below its own 5-year minimum P/E and EV/EBITDA, but falling FCF and a mechanical fair value below the price leave the valuation case unproven.",
  "rationale": "Quality, balance sheet and earnings multiples are attractive, but FCF margin is falling as capex rises, P/FCF is mid-range, and the blended base fair value is below the price. The scorecard gives conviction 3, below the buy bar, so AVOID; owner rule: only high conviction is bought.",
  "price_at_decision": 419.80,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-0700/2026-11-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 28%, reversing much of the expansion to 33.3%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 28}},
    {"text": "TTM ROIC falls below 14%, giving up the rise from 13.0% (FY2021) to 18.3%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 14}},
    {"text": "TTM FCF margin falls below 15%, showing AI spend is not converting to cash.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.04x now), showing capex or returns outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 540.00, "basis": "AI spend converts and the China discount narrows, so P/E returns toward its 5y median of 18.4x [RA] on TTM earnings, near the EV/Revenue base of 553.51 HKD and above the blended bull of 529.63 HKD (fact sheet)."},
    "base": {"probability": 0.50, "target_price_12m": 435.00, "basis": "Earnings keep growing with operating margin at 33.3% [IS-T] but FCF stays depressed by capex [CF-T], so P/E only recovers to around its 5y minimum of 14.8x [RA]; above the unreliable blended base of 337.13 HKD because the DCF is penalised by the TTM FCF dip and the 3.5% China premium."},
    "bear": {"probability": 0.25, "target_price_12m": 337.13, "basis": "US chip restrictions (Reuters URL in note) and a wider China discount keep FCF margin falling from 21.3% [CF-T], and the price converges on the blended base fair value of 337.13 HKD (fact sheet)."}
  },
  "entry_price": 269.70,
  "entry_basis": "valuation file: base 337.13 x 0.8; at that level the valuation pillar would clear the mandate with the same quality evidence.",
  "replaces": null,
  "replacement_reason": null
}
```

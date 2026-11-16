# Evaluation: Haidilao International Holding Ltd. (HKG:6862) — 2026-11-16
## Bear case
The last 12 months are going the wrong way: TTM ROIC fell 61.3% -> 48.8%, operating margin 13.4% -> 12.3% and FCF margin 11.9% -> 8.0% [RA-T, IS-T, CF-T] [Certain]. FCF conversion slid from 190.0% (FY2023) to 88.6% TTM as opening capex rises [Likely]. The five-year "rising" trends start from a COVID trough, so they overstate durability [Likely]. Restaurants are easy to copy and tied to mainland consumer spending; returns this high probably mean-revert [Guessing]. The stock is 22.1% below its 200-day average, down 25.3% over 12 months and 35.7pp behind SPY: it is cheap but not working [Certain]. The mechanical bear fair value of 4.49 shows how wide the range is [Certain]. Insiders own 64.19%, so minority-governance risk applies [Certain]; the H1 2026 net loss came from FX [Likely], and results are due 2026-11-25 (est.) [Likely]. PBoC policy and politics are unverified (macro overlay) [Certain].

## Bull case
This is an exceptionally profitable, net-cash restaurant operator: TTM ROIC 48.8%, ROCE 44.6% (flat over the year), net debt/EBITDA -0.27x, Altman Z 7.50, share count flat [RA, ST] [Certain]. In H1 2026 Q2 revenue grew 10% and operating profit rose 118.9% on stronger traffic and lower expense ratios; the net loss was FX, not operations [OV transcript] [Likely]. Delivery and new brands are growing and double-digit second-half openings are planned, so part of the FCF dip is investment, not erosion [Likely]. P/E 12.1x, EV/EBITDA 6.5x and EV/Sales 1.1x sit below their 5y minimums and roughly a third below peers (YUMC, HKG:9922, MCD) [RA] [Certain]. FCF yield is 7.13% and the reverse DCF only asks for 5.5% year-1 revenue growth [ST] [Certain]. Base fair value 11.52 sits above the price [Certain].

## Decision
```json
{
  "ticker": "HKG:6862",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "H1 2026 transcript (OV, /quote/hkg/6862/transcripts/613065-h1-2026/): Q2 operating profit rose 118.9% on traffic and lower expense ratios; the net loss was FX; ROCE flat over the year [RA-T]; FCF dip coincides with planned double-digit openings and net cash intact [ST].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Mainland consumer weakness or copycat competition keeps eroding margins and returns (TTM operating and FCF margin already falling), with a controlled-company governance overlay.",
    "veto": null
  },
  "thesis": "A net-cash, very high-return hotpot leader trading below its own 5-year multiple range, but with falling 12-month margins and a downtrend, it is cheap rather than working.",
  "rationale": "Quality and balance sheet are strong and multiples sit below their 5y minimums, but base fair value upside is modest, the 12-month margin and FCF slide is unresolved ahead of results on 2026-11-25, and the price trend is weak. The scorecard gives conviction 3: good but not compelling, so AVOID with an entry price.",
  "price_at_decision": 9.92,
  "price_date": "2026-11-13",
  "research_note": "research/HKG-6862/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 10% (statistics page).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 35% (statistics page).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 35}},
    {"text": "TTM FCF margin falls below 6% (statistics page).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 6}},
    {"text": "Net cash turns into net debt: net debt/EBITDA (debt less cash and short-term investments) rises above 1.0x as expansion is debt-funded."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 15.21, "basis": "Margins stabilise after the openings cycle and EV/EBITDA re-rates toward its own history, matching the EV/EBITDA method's base value of 15.21 (fact sheet Fair value, RA)."},
    "base": {"probability": 0.5, "target_price_12m": 11.52, "basis": "Operating margin holds near 12.3% TTM [IS-T] and the stock reaches the mechanical blended base fair value of 11.52 (fact sheet Fair value)."},
    "bear": {"probability": 0.25, "target_price_12m": 8.93, "basis": "FCF margin keeps sliding from 8.0% [CF-T] and weak mainland demand holds the stock at its 52-week low of 8.93 [HI]; above the mechanical bear 4.49 because the net-cash balance sheet [ST] and FCF yield 7.13% limit a de-rating from below-5y-minimum multiples."}
  },
  "entry_price": 9.22,
  "entry_basis": "valuation file: base 11.52 x 0.8; at that price the discount would earn the extra valuation points for conviction 4 on the same evidence.",
  "replaces": null,
  "replacement_reason": null
}
```

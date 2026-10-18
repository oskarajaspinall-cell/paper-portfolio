# Evaluation: TIM S.A. (BVMF:TIMS3) — 2026-10-18
## Bear case
The 20.23% FCF yield [ST] is probably overstated: FCF runs at 211.4% of net income [CF,IS], which for a tower- and lease-heavy telecom likely reflects lease payments sitting in financing rather than true owner cash [Guessing]. The DCF that drives the base fair value of 41.25 BRL rests on that FCF; the lease-neutral EV/EBITDA method gives only 16.66 / 21.43 / 23.29 BRL [Certain]. The stock is down 28.7% in six months and trails SPY by 37.5pp [HI] while the note cannot name a company-specific cause [Certain]; management itself cites slowing mobile growth on pricing and churn and a "below-the-line" promotional shift [Likely] (transcript). A three-player market that starts competing on price is exactly where margin expansion reverses [Guessing]. Minority holders sit under a controlling parent, institutional ownership is only 16.4% [ST], and Altman Z is 2.18 [ST] [Certain]. Earnings on Nov 9, 2026 are an unresolved catalyst [Certain].

## Bull case
Quality is improving on every line: ROIC 17.6% (+7.0pp over 5y), operating margin 25.8% (+7.0pp), Piotroski 7 [RA,IS,ST] [Certain]. P/E 10.5x and EV/EBITDA 4.4x sit below their own 5-year minimums and well below peers' 15.4x and 5.8x [RA] [Certain]. The reverse DCF implies -15.5% year-1 revenue growth against reported growth in Q2 2026 [Likely] (transcript), and even the mechanical bear fair value of 24.30 BRL is above the 18.93 close [Certain]. Leverage is modest at 1.05x net debt/EBITDA, shares fell 0.89% YoY [RA,ST] [Certain], and broadband and B2B are now the fastest-growing segments, diversifying away from mobile [Likely]. Near-zero beta of 0.09 [ST] would diversify a US/China-heavy book [Certain].

## Decision
```json
{
  "ticker": "BVMF:TIMS3",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A rising-ROIC Brazilian mobile operator trades below its own 5-year minimum P/E and EV/EBITDA, but the headline FCF yield is likely lease-flattered and the unexplained derating coincides with management-flagged pricing pressure and churn in mobile.",
  "rationale": "Cheap and improving, but the upside depends on a DCF built on FCF at more than double net income; the lease-neutral EV/EBITDA method shows modest upside. Mobile churn, a promotional shift, a controlling parent and earnings in three weeks leave this good but not compelling. Cash is the better outcome.",
  "price_at_decision": 18.93,
  "price_date": "2026-10-16",
  "research_note": "research/BVMF-TIMS3/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROIC falls back below 13% (FY2024 level 13.9%), showing the margin-expansion story has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 13}},
    {"text": "TTM FCF margin falls below 20% (FY2022 level 20.6%), showing cash conversion has broken down.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 20% (FY2023 level 20.1%), showing promotional competition is eroding profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "Mobile postpaid net adds in the earnings release turn negative for two consecutive quarters, evidencing a price war rather than a cyclical promotional phase; conversely, stable postpaid adds with rising service revenue in the Nov 9, 2026 results would lift conviction."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 24.30, "basis": "Results show mobile churn stabilising and margin expansion continuing, re-rating the stock to the blended bear fair value of 24.30 BRL with P/E back toward its 5y median 11.8x [RA]; the DCF base of 51.16 is not used because its FCF input is likely lease-flattered."},
    "base": {"probability": 0.50, "target_price_12m": 21.43, "basis": "EV/EBITDA recovers toward its 5y median 5.6x [RA] on TTM EBITDA, the EV/EBITDA method's base value of 21.43 BRL, as broadband/B2B growth offsets slower mobile (transcript)."},
    "bear": {"probability": 0.25, "target_price_12m": 16.66, "basis": "The below-the-line promotional shift (transcript) becomes a price war, operating margin stalls from 25.8% [IS] and EV/EBITDA stays below its 5y minimum 4.6x [RA], the EV/EBITDA method's bear value of 16.66 BRL."}
  },
  "entry_price": 16.66,
  "entry_basis": "The default base 41.25 x 0.8 sits above the price because the DCF is lease-flattered; use the lease-neutral EV/EBITDA method's bear value of 16.66 BRL (valuation file; fact sheet fair value [RA,ST]), where the bear scenario is fully priced and the same evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

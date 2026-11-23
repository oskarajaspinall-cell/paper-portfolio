# Evaluation: Yifeng Pharmacy Chain Co., Ltd. (SHA:603939) — 2026-11-23
## Bear case
The cheapness is partly a peer effect: EV/EBITDA of 6.2x is only in line with the peer median, and peers trade far lower on P/FCF (3.6x) and P/B (1.6x) [Certain]. The whole China pharmacy group is being de-rated, which points to sector-wide pressure (drug-price reform, online competition, store saturation) rather than a mispricing of one name [Likely]. Gross margin has slipped from 40.1% to 38.5% [Certain], consistent with that pressure. FCF margin sits 3.9pp below its 2-year high of 17.9%, and FCF conversion near 197% of net income leans on working capital and lease accounting that may not repeat [Guessing]. The Q3 2026 report was not reviewed [Certain], so a guidance or store-closure signal could be missed. The price is 13.5% above its 200-day average after a 25.6% six-month run [Certain]; if growth slows, the trend-strength support goes with it.

## Bull case
Returns are rising, not peaking: ROIC is 24.9% on a rolling basis, up from 21.2% a year earlier and 14.0% in FY2021, with operating margin at its 2-year high of 10.4% [Certain]. The balance sheet is net cash (-1.89x net debt/EBITDA) and shares are shrinking 1.25% a year [Certain]. P/E of 17.8x sits at 7% of its 5-year range and EV/EBITDA below its 5-year minimum, with an 11.28% FCF yield [Certain]. The reverse DCF implies revenue shrinking 7.4% in year 1, which a chain still growing profit does not show [Likely]. The FCF-margin dip from its 2024 peak has already partly reversed (+2.9pp over the last year) and remains above FY2021, so it reads as working-capital timing, not a broken model [Likely]. Low beta (0.17) and positive relative strength suggest a market reassessing the name upward [Likely].

## Decision
```json
{
  "ticker": "SHA:603939",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Python flags the 3-year FCF-margin fall (17.9% 2-year high to 14.0%); over the last 12 months it rose +2.9pp from 11.1% [CF-T,IS-T] while ROIC (+3.7pp) and operating margin (+0.6pp) rose [RA-T,IS-T], so it is working-capital timing off an unusual 2024 peak, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Sector-wide drug-price reform and online competition compress pharmacy gross margin (already 40.1% to 38.5% [IS]), and peers' much lower cash multiples suggest the market prices this for the whole group; a slowdown would also de-rate a price now 13.5% above its 200-day average.",
    "veto": null
  },
  "thesis": "A net-cash Chinese pharmacy chain with ROIC rising to 24.9% and an 11.28% FCF yield trades near the bottom of its own multiple ranges, pricing a revenue decline its rising returns do not show.",
  "rationale": "The scorecard gives conviction 4: rising returns, net cash and a deep own-history discount outweigh sector margin pressure and peers' lower cash multiples. Python sizes it. Cash sits at the floor and China/HK exposure near its 25% cap, so it must replace a China/HK holding.",
  "price_at_decision": 26.26,
  "price_date": "2026-11-20",
  "research_note": "research/SHA-603939/2026-11-23.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, giving up most of the rise from 14.0% in FY2021 to 24.9%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM operating margin falls below 8.5%, under the FY2023 five-year low of 8.9%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 8.5}},
    {"text": "TTM gross margin falls below 36%, showing drug-price or reimbursement pressure is structural.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 36}},
    {"text": "TTM FCF margin falls below 8%, under the FY2021 level of 8.6%, showing the cash conversion was not durable.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 52.0, "basis": "P/E re-rates toward its 5y median 28.7x [RA] on rising ROIC; below the mechanical bull 61.16 because peers stay cheaper on cash multiples [RA,P]."},
    "base": {"probability": 0.5, "target_price_12m": 36.0, "basis": "EV/EBITDA recovers toward its 5y min 8.9x [RA] as profit keeps growing; below the mechanical base 43.46 because EV/EBITDA is only in line with peers at 6.1x [RA,P]."},
    "bear": {"probability": 0.25, "target_price_12m": 22.0, "basis": "Drug-price reform hits gross margin (already down to 38.5% [IS]) and P/E slips to its 5y min 15.7x [RA], a little under the mechanical bear 24.92."}
  },
  "replaces": "HKG:3998",
  "replacement_reason": "A BUY would breach the 1.5% cash floor and the China/HK 25% cap; HKG:3998 is the only China/HK holding held 30+ days whose sale frees room for a full size (HKG:9999 just fell sharply and awaits re-research). Yifeng sells non-discretionary pharmacy goods with rolling returns still rising and very low beta, against a weather- and fashion-cyclical apparel brand."
}
```

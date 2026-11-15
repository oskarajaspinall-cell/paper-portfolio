# Evaluation: Deckers Outdoor Corporation (DECK) — 2026-11-15
## Bear case
The Q2 guidance cut is the first crack in brand heat: management blamed rival discounting, softer domestic DTC traffic and higher promotional intensity, and HOKA and UGG are both slowing [Certain] (note §6, 10-Q). The moat is brand and full-price discipline, not structure, so a fashion or running-cycle turn can take the returns away fast [Likely]. ROIC has fallen from 78.5% to 71.9% over the last 12 months and sits 46.9pp below its 2-year high [Certain] (RA-T). That is partly a seasonal inventory build, but if discounting persists the inventory becomes markdowns [Guessing]. Near-term margins are flattered by one-off IEEPA tariff refunds, and management says mitigation won't fully offset new tariffs [Certain] (10-Q). The European 3PL failure adds execution risk [Certain]. Trend is negative: -12.0% vs the 200-day average and lagging SPY [Certain] (HI). Bear fair value is 37.63 [Certain].

## Bull case
This is a net-cash business (net debt/EBITDA -0.48x) with TTM ROIC 71.9%, a 58.9% gross margin, a 23.6% operating margin and about 99% FCF conversion [Certain] (RA, IS). Margins are holding: operating margin is flat year on year and ROCE is at its 2-year high of 45.7% [Certain] (RA-T, IS-T). Guidance moderated sales growth but margin expectations rose, with full-price discipline intact [Likely] (Q2 transcript, OV). Yet the stock trades at 11.5x P/E, 7.9x EV/EBITDA and 11.0x P/FCF, all below their 5y minimums and well under peers, at a 9.08% FCF yield [Certain] (RA, ST). The reverse DCF implies -0.3% year-1 revenue growth, a decline the slowed-but-positive outlook does not show [Likely]. Buybacks cut the share count 6.97% YoY at these depressed multiples [Certain] (ST). Base fair value is 110.02 [Certain].

## Decision
```json
{
  "ticker": "DECK",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "TTM ROIC is falling (78.5% to 71.9%, RA-T) and FCF margin is down -1.1pp over 3 years but flat over the last year (18.7% to 18.9%, CF-T); operating margin is flat at 23.6% and ROCE is at its 2-year high [IS-T, RA-T]. The note ties the ROIC dip partly to a seasonal inventory build in the 10-Q (https://www.sec.gov/Archives/edgar/data/910521/000162828026068116/deck-20260930.htm), with net cash intact.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Rival discounting and slower HOKA/UGG growth (Q2 guidance cut, 10-Q MD&A) turn into lasting markdowns and gross-margin erosion once the one-off tariff refunds stop flattering cost of sales.",
    "veto": null
  },
  "thesis": "A net-cash, very high-return footwear brand owner with flat margins and ROCE at its 2-year high trades below its own 5-year minimum P/E, EV/EBITDA and P/FCF at a 9.08% FCF yield, pricing a revenue decline its slowed-but-positive outlook does not show.",
  "rationale": "Evidence is unchanged from the last review: quality and balance sheet intact, multiples below 5-year floors, the ROIC dip explained by inventory timing while margins hold. The guidance cut and discounting keep the score in the hold band, not at the buy threshold, so no ADD; the position stays at its current size.",
  "price_at_decision": 86.82,
  "price_date": "2026-11-13",
  "research_note": "research/DECK/2026-11-15.md",
  "triggers": [
    {"text": "TTM gross margin falls below 55%, under the FY2024 level of 55.6%, showing rival discounting or markdowns are eroding full-price discipline.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}},
    {"text": "TTM operating margin falls below 20%, reversing most of the five-year expansion from 18.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 14%, showing the inventory build is turning into cash and margin stress rather than a seasonal swing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "TTM ROIC falls below 55%, showing the decline from 78.5% is no longer inventory timing but eroding returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 55}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 140.0, "basis": "Discounting fades and the P/E re-rates toward its 5y median 17.6x [RA]; set below the mechanical bull 178.57 because sales guidance was just cut (note §6)."},
    "base": {"probability": 0.5, "target_price_12m": 100.0, "basis": "Margins hold near 23.6% [IS-T] and the multiple recovers to around its 5y minimum 13.9x P/E [RA]; between the P/E base 84.84 and DCF base 122.61, shaded below the blended base 110.02 for slower HOKA/UGG growth."},
    "bear": {"probability": 0.25, "target_price_12m": 67.01, "basis": "Rival discounting becomes markdowns once tariff refunds stop flattering cost of sales (10-Q, note §6); the P/E-method bear fair value 67.01 [Fair value], not the DCF bear 22.94 which assumes a collapse net cash and margins do not show."}
  },
  "entry_price": 77.2,
  "entry_basis": "The 52-week low of 77.20 [HI]: the default (base 110.02 x 0.8) sits above today's price, so the swing low is used; a retest there on unchanged fundamentals would widen the discount further.",
  "replaces": null,
  "replacement_reason": null
}
```

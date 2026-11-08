# Evaluation: Vodacom Group Limited (JSE:VOD) — 2026-11-08
## Bear case
The price already capitalises the improvement [Likely]. P/E of 15.7x sits at the 97th percentile of its own 5y range (median 14.1x) and P/B 2.9x at the 82nd; P/FCF of 9.6x is above its 5y median 8.6x and well above peers at 5.9x [Certain] [RA]. There is no mechanical fair value (no ZAR rate), so no model cross-check exists [Certain]. Net margin fell 4.4pp over five years to 12.3% as interest, tax and minorities absorb profit, and net debt/EBITDA crept up to 1.16x with the Safaricom stake funded by ZAR and KES facilities [Likely] [IS,RA]. Kenyan, Egyptian and Tanzanian currency exposure is material but unquantified; weaker KES or EGP against the rand would cut translated profit and raise KES debt cost (research/JSE-VOD/2026-11-08-macro.md) [Guessing]. The stock is at its 52-week high with results due Nov 10 [Certain].

## Bull case
Returns are rising on a rolling basis, not just at fiscal-year endpoints: TTM ROIC 16.9% (+2.1pp), ROCE 20.2% (+1.2pp) and operating margin 23.8% (+2.0pp, its 2-year high) [Certain] [RA-T,IS-T]. Cash backs earnings: FCF margin 19.5%, FCF/net income 158.7%, FCF yield 10.43% [Certain] [CF,ST]. EV/EBITDA of 6.1x sits at the 24th percentile of its 5y range, so on cash-flow-based enterprise value it is not stretched [Certain] [RA]. Safaricom consolidation at 55% and Egypt, Tanzania and fintech growth add a growth leg, and the dividend was raised [Likely] (transcript /quote/jse/VOD/transcripts/666160-h2-2026-q-a/). Beta 0.30 and Piotroski F of 7 point to a defensive, financially sound compounder [Likely] [ST].

## Decision
```json
{
  "ticker": "JSE:VOD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cash-generative African telecom with rising returns and a 10.43% FCF yield, but its earnings and book multiples sit near the top of their own 5-year ranges, leaving a fair rather than compelling skew before unquantified frontier-currency risk.",
  "rationale": "Quality is good and improving, but P/E near its 5y high, P/FCF above its median and far above peers, no fair-value cross-check, unsized KES/EGP exposure and results two days away leave expected value only modestly above the price. Good but not compelling: AVOID, with an entry where P/FCF returns to its 5y median.",
  "price_at_decision": 16267.0,
  "price_date": "2026-11-06",
  "research_note": "research/JSE-VOD/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 21%, under the FY2025 level of 21.7%, reversing the rolling-year expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 21}},
    {"text": "TTM ROIC falls below 14%, under the five-year range, showing Safaricom consolidation dilutes returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 14}},
    {"text": "Net debt/EBITDA rises above 1.8x (1.16x now), showing the Safaricom funding is stretching the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.8}},
    {"text": "FCF conversion (FCF/net income) falls below 110% on the cash-flow and income statements, showing cash no longer backs earnings."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 19500, "basis": "EV/EBITDA re-rates from 6.1x to its 5y median 6.4x [RA] on higher EBITDA from Safaricom consolidation and operating margin holding its 23.8% 2-year high [IS-T]; no mechanical fair value exists (no ZAR rate), so this is built from own-history multiples."},
    "base": {"probability": 0.5, "target_price_12m": 17000, "basis": "Multiples hold near EV/EBITDA 6.1x [RA] while rising ROIC (16.9%, +2.1pp [RA-T]) and the 10.43% FCF yield [ST] carry modest earnings growth; no mechanical fair value to reconcile with (no ZAR rate)."},
    "bear": {"probability": 0.25, "target_price_12m": 13000, "basis": "P/E reverts from the 97th percentile toward its 5y median 14.1x and P/FCF toward its 5y low 7.1x [RA] as unquantified KES/EGP weakness cuts translated profit (research/JSE-VOD/2026-11-08-macro.md country_risk)."}
  },
  "entry_price": 14570,
  "entry_basis": "No fair value is computable (no ZAR rate), so anchored on P/FCF back at its 5y median 8.6x [RA] from 9.6x on TTM FCF: the same improving quality at a median cash multiple would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

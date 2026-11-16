# Evaluation: Deckers Outdoor Corporation (DECK) — 2026-11-16
## Bear case
This is a fashion-exposed, two-brand business whose heat is fading [Likely]. Management cut full-year sales guidance on 2026-10-22 as rivals' aggressive discounting hit premium brands, and the 10-Q reports softer domestic DTC traffic and conversion [Certain]. The **Direction change** is real: TTM ROIC fell from 78.5% to 71.9%, 46.9pp below its 2-year high [Certain]. Margins are flattered by one-off IEEPA tariff refunds (about $46,000k in the half-year, `[company-reported]`) and incremental tariffs won't be fully mitigated [Certain]. Net cash narrowed from -1.14x to -0.48x net debt/EBITDA as buybacks ran ahead [Certain]. The trend is broken: 11.8% below the 200-day average and trailing SPY by 9.9pp over 12 months [Certain]. If HOKA joins the promotional cycle, the multiple can stay below its 5-year minimum and the bear fair value of 37.65 is not absurd [Guessing].

## Bull case
The economics are intact [Certain]: TTM gross margin 58.9% (rising), operating margin 23.6% (flat year on year), FCF margin 18.9% (flat), ROCE 45.7% at its 2-year high, FCF conversion 99.3%, and still net cash. The ROIC decline comes from a larger capital base, not weaker margins [Likely], so it reads as temporary. Growth slowed but stayed positive: Q2 revenue grew 3.5% with margin expectations raised and full-price discipline held [Likely]. Yet the price implies -0.4% revenue growth; P/E 11.0x, EV/EBITDA 7.9x and P/FCF 11.0x all sit below their own 5-year minimums and well below peers, with a 9.08% FCF yield [Certain]. Shares fell 6.97% YoY, so per-share value compounds even at low growth [Certain]. Base fair value of 110.15 sits well above the 86.82 close [Certain].

## Decision
```json
{
  "ticker": "DECK",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC fell 78.5% -> 71.9% TTM [RA-T] while operating margin (+0.0pp) and FCF margin (+0.2pp) are flat over the last year and ROCE is at its 2-year high [IS-T, CF-T, RA-T], so it reflects a larger invested-capital base, not eroding margins (note section 2); the 3-year FCF margin dip (-1.1pp) is from a 20.4% peak to a still-high 18.9%, with FCF conversion 99.3% [CF,IS].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Rival discounting spreads to HOKA and UGG, forcing markdowns that break full-price discipline and push gross margin down (Reuters 2026-10-22 headline and 10-Q DTC softness, https://www.sec.gov/Archives/edgar/data/910521/000162828026068116/deck-20260930.htm).",
    "veto": null
  },
  "thesis": "A net-cash, very high-return footwear brand owner with flat margins and ROCE at its 2-year high trades below its own 5-year minimum P/E, EV/EBITDA and P/FCF at a 9.08% FCF yield, pricing a revenue decline its slowed-but-positive outlook does not show.",
  "rationale": "Same evidence as the 2026-11-15 HOLD: a deep discount to its own history and peers with intact margins, against a guidance cut and a broken price trend. The score sits in the hold band, not at the add threshold; the position is near its conviction size, so no add and no trim.",
  "price_at_decision": 86.82,
  "price_date": "2026-11-13",
  "research_note": "research/DECK/2026-11-16.md",
  "triggers": [
    {"text": "TTM gross margin falls below 55%, under the FY2024 level of 55.6%, showing rival discounting or markdowns are eroding full-price discipline.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}},
    {"text": "TTM operating margin falls below 20%, reversing most of the five-year expansion from 18.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 14%, showing inventory or promotions are turning into cash and margin stress.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "TTM ROIC falls below 55%, showing the decline from 78.5% is no longer a capital-base effect but eroding returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 55}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 150, "basis": "Growth re-accelerates and the multiple returns toward its 5y median P/E of 17.6x [RA], short of the bull fair value of 178.77 because the guidance cut caps near-term growth (WSJ 2026-10-22 headline)."},
    "base": {"probability": 0.5, "target_price_12m": 105, "basis": "Slow positive growth with flat margins re-rates toward the base fair value of 110.15 [valuation file], slightly lower for the one-off tariff refunds flattering margins (note section 5)."},
    "bear": {"probability": 0.25, "target_price_12m": 67, "basis": "Discounting spreads and the stock is valued on the P/E bear case of 67.01 [fair value table], above the blended bear of 37.65 because net cash and a 9.08% FCF yield [ST] support the floor."}
  },
  "entry_price": 77.2,
  "entry_basis": "The 6-month and 52-week low of 77.20 [HI]; the default base-less-20% level sits above today's price, so it can't serve. At that low the discount to its own 5-year minimum multiples deepens enough to justify an ADD on the same evidence.",
  "replaces": null,
  "replacement_reason": null
}
```

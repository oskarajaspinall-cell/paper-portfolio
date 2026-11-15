# Evaluation: Evolution AB (STO:EVO) — 2026-11-15
## Bear case
Growth has stalled: Q1 2026 revenue fell 1.5% and Q3 grew only 3.7%, with European regulation and Asian cybercrime weighing, and a post-quarter Brazil ban clouding Q4 [Likely]. Brazil's revenue share is [data unavailable] and the ban is unverified by any official or company source, so the hit could be larger than the price assumes [Guessing]. Operating margin has fallen from 62.1% at its 2-year high to 57.0% TTM and ROIC sits 2.5pp below its 2-year high [Certain]; if this is lost markets rather than investment, the decline is structural. The price is 23.7% above its 200-day average after a +33.9% year, so a further growth slowdown risks a de-rating from here [Likely]. Candle Lake crossed the mandatory-bid threshold and bid 695 crowns, well below the price; with insiders at 36.32%, a controlling holder could squeeze minorities or thin the free float [Likely].
## Bull case
This is an exceptional business on a low multiple: ROIC 32.1%, FCF margin 59.3%, FCF conversion 116.5% and net cash [Certain]. P/E 14.3x, EV/EBITDA 10.5x and P/FCF 11.3x all sit in the bottom tenth of their 5-year ranges, with an 8.87% FCF yield [Certain]. The reverse DCF says the price implies -1.4% revenue growth in year 1, yet Q3 revenue grew and regional growth was broad [Likely]. Adjusted EBITDA margin held near 65.8% through 2026 and FY margin guidance is unchanged, so the operating-margin slide looks like studio investment and depreciation rather than pricing loss [Likely]. Buybacks cut the share count 4.06% YoY and are accretive at these multiples [Certain]. Trend is healthy: above the 200-day average, beating SPY by 23.5pp over 12 months [Certain]. Base fair value is 1,320.92 SEK [Certain].
## Decision
```json
{
  "ticker": "STO:EVO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating margin fell from 59.1% to 57.0% TTM while the call summaries show adjusted EBITDA margin steady at 65.4% (Q1), 65.9% (Q2) and 65.8% (Q3) with FY margin guidance unchanged (https://stockanalysis.com/quote/sto/EVO/transcripts/552836-q3-2026/), pointing to studio investment and depreciation on flat revenue rather than lost pricing; FCF margin is flat over the last year [CF-T].",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Regulatory loss of markets (the unverified post-quarter Brazil ban, European regulation) keeps revenue flat or falling, turning the margin slide structural and de-rating a price already well above its 200-day average.",
    "veto": null
  },
  "thesis": "A net-cash live-casino supplier with ROIC above 30% and a near-60% FCF margin trades near its 5-year multiple floor, but stalled growth, an unquantified Brazil ban and a controlling bidder leave the skew short of compelling.",
  "rationale": "Quality and cash yield are outstanding and the multiple is low, but revenue has stalled under regulation, the Brazil ban's size is unknown, and Candle Lake's position adds governance risk. The scorecard sets the conviction; below the buy bar this is an AVOID, re-checked on Q4 results.",
  "price_at_decision": 871.00,
  "price_date": "2026-11-13",
  "research_note": "research/STO-EVO/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 52% (57.0% now), showing regulation is compressing profitability beyond investment.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 52}},
    {"text": "TTM ROIC falls below 25% (32.1% now), showing returns are eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}},
    {"text": "TTM FCF margin falls below 50% (59.3% now), showing cash generation is breaking.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 50}},
    {"text": "Quarterly revenue declines year on year for two consecutive reported quarters, or the company discloses the Brazil ban removes a material share of revenue."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1320.92, "basis": "Revenue stabilises after Brazil and the multiples re-rate toward the mechanical base fair value of 1,320.92 SEK [IS,BS,CF,RA,ST,HI]; below the mechanical bull because growth has stalled (Q1 decline, Q3 +3.7%, per the Q3 call summary)."},
    "base": {"probability": 0.45, "target_price_12m": 1009.55, "basis": "Flat revenue near the reverse-DCF's -1.4% implied growth holds the stock at the DCF bear value of 1,009.55 SEK [IS,BS,CF,RA,ST], below the mechanical base because the Brazil ban and European regulation cap growth."},
    "bear": {"probability": 0.30, "target_price_12m": 647.18, "basis": "A material Brazil loss and further margin slide take EV/EBITDA to its bear value of 647.18 SEK [IS,BS,CF,RA,ST], near the 5-year EV/EBITDA low of 8.7x [RA]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: the unquantified Brazil ban and Candle Lake's control position must resolve first; a lower price alone would not change the decision.",
  "new_evidence": null,
  "replaces": null,
  "replacement_reason": null
}
```

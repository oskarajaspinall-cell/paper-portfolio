# Evaluation: The Kraft Heinz Company (KHC) — 2026-10-12
## Bear case
Operating margin is falling, from 21.4% (FY2024) to 18.0% TTM [Certain] [IS], and management is now putting $700 million back into marketing and innovation to win back shoppers (CNBC headline, 2026-09-15 [OV]). That makes margin recovery a hope, not yet evidence [Likely]. The CEO's own "green shoots, but we need to do better" (2026-08-05 [OV]) says share trends are still weak [Likely]. Leverage near 3.0x net debt/EBITDA [RA] and an Altman Z of 0.85 [ST] leave little room if volumes keep slipping [Certain]. ROE has turned negative (-8.8% TTM) [RA] after a large charge, and a P/B of 0.7x [RA] suggests the market doubts the book value of the brands [Likely]. Short interest is 11.52% and rising (+14.8%) [ST] [Certain]. The cheap multiples can stay cheap for a structurally shrinking brand portfolio [Guessing].
## Bull case
On cash, KHC is deeply cheap. Its FCF yield is 14.45% [ST], P/FCF is 6.9x against a 5y minimum of 7.8x and a peer median of 9.8x, and EV/EBITDA is 7.8x, below its 5y minimum of 8.2x and the peer median of 8.4x [RA] [Certain]. FCF margin has risen to 15.3% TTM [CF,IS] and ROIC to 8.1% [RA] [Certain]. That points to an accounting-driven earnings collapse, not a cash collapse [Likely]. The reverse DCF prices a -15.5% revenue decline [Fair value], which looks harsher than the fundamentals show [Likely]. Catalysts are close: Q3 results on Oct 28 and an Investor Day on Nov 12 [OV] [Certain]. With short interest at 11.52% [ST], any evidence that the reinvestment is working could force a sharp re-rating [Guessing].
## Decision
```json
{
  "ticker": "KHC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "KHC's 14.45% FCF yield and below-5y-minimum multiples are real, but with operating margin falling, a $700m reinvestment of unproven payback and ~3.0x leverage, this is a turnaround bet whose evidence is not yet in.",
  "rationale": "Cheap on cash, but quality is moving the wrong way: operating margin is down 3.4pp from FY2024, ROE is negative, Altman Z is 0.85 and short interest is rising. The expected return rests on the turnaround working, which Q3 results and the Investor Day will test within weeks. Good but not compelling at conviction 3, so AVOID and keep the cash.",
  "price_at_decision": 22.27,
  "price_date": "2026-10-09",
  "research_note": "research/KHC/2026-10-12.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 20%, back toward the FY2024 level of 21.4%, showing the brand reinvestment is restoring profitability (would raise conviction).", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 20}},
    {"text": "Net debt/EBITDA falls below 2.8x, showing real deleveraging that lowers balance-sheet risk (would raise conviction).", "check": {"source": "statistics", "field": "debtEbitda", "op": "<", "value": 2.8}},
    {"text": "TTM FCF margin falls below 12%, back to the FY2024 level of 12.2%, showing the reinvestment is eroding the cash case (confirms AVOID).", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "The Q3 2026 release (Oct 28) or the Nov 12 Investor Day shows positive organic sales growth and market-share gains in two consecutive quarters, evidencing a working turnaround."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 33.30, "basis": "Reinvestment restores share and margin, and EV/EBITDA returns to its 5y median of 10.2x [RA] on TTM EBITDA with net debt held at ~2.97x [RA]; well below the DCF bull of 83.07 [Fair value], which capitalises a 15.3% FCF margin at a cost of equity depressed by a 0.11 beta [ST]."},
    "base": {"probability": 0.45, "target_price_12m": 25.20, "basis": "FCF holds near the 15.3% TTM margin [CF,IS] and P/FCF re-rates only to its 5y minimum of 7.8x [RA]; deliberately far below the mechanical base of 60.80 [Fair value], because falling operating margin [IS] and the $700m reinvestment (CNBC 2026-09-15 [OV]) argue against capitalising the current FCF."},
    "bear": {"probability": 0.30, "target_price_12m": 18.70, "basis": "Operating margin keeps sliding from 18.0% TTM [IS] and EBITDA falls ~10% while EV/EBITDA stays at 7.8x [RA]; the fixed ~2.97x net debt [RA] levers the fall into equity, close to the DCF bear of 15.93 [Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: KHC already trades below its 5y minimum P/FCF and EV/EBITDA [RA]. What blocks a BUY is falling operating margin and an unproven turnaround, so a lower price would not change the decision. Evidence from the Q3 release or the Investor Day would.",
  "replaces": null,
  "replacement_reason": null
}
```

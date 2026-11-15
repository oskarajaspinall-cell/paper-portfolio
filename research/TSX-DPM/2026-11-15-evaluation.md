# Evaluation: DPM Metals Inc. (TSX:DPM) — 2026-11-15
## Bear case
Record margins are a gold-price outcome, not a moat: operating margin 58.5% TTM vs 37.6% in FY2021, and a miner is a price taker [Likely]. The macro overlay tilts small toward bear: the 10y real yield rose to 2.86% and the dollar strengthened over ~3m, a gold headwind (research/TSX-DPM/2026-11-15-macro.md) [Likely]. The multiple is already above its own history: P/E 11.1x vs a 6.9x 5y median, EV/EBITDA 7.4x vs 2.8x, P/B at 93% of its range, all above peers [Certain]. The trend is broken: price is 7.3% below the 200-day average with -20.6% 3-month momentum [Certain]. FCF margin fell from 59.4% to 46.6% over the last year [Certain], and shares rose 26.71% YoY, diluting per-share returns [Certain]. The Bosnia Constitutional Court decision on Vareš is unread, an unsized jurisdiction risk [Guessing].
## Bull case
Returns are high and rising on a rolling basis: ROIC 32.4% TTM vs 22.4% a year earlier, ROCE 24.3% at its 2-year high [Certain]. The FCF-margin dip coincides with growth spending on Vareš, which the Q3 call says reached commercial production early, with 2026 guidance on track [Likely]. The balance sheet is net cash (net debt/EBITDA -0.94x), Altman Z 11.83, Piotroski 7 [Certain]. FCF yield is 8.35% and P/FCF 12.0x is 23% below peers [Certain]; a dividend was declared [Certain]. The 12-month change is +50.1% and the 50-day average remains 8.5% above the 200-day, so the pullback may be a pause [Likely]. If gold holds, Vareš adds production that a peer-discount cash multiple does not price [Guessing].
## Decision
```json
{
  "ticker": "TSX:DPM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell from 59.4% to 46.6% TTM while ROIC, ROCE and operating margin rose; the fall coincides with Vareš growth spending, and Q3 FCF was strong with Vareš in commercial production early (https://stockanalysis.com/quote/tsx/DPM/transcripts/721368-q3-2026/).",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Gold price falls as real yields and the dollar rise (macro overlay), compressing record margins and de-rating a multiple already above its 5y median.",
    "veto": null
  },
  "thesis": "A net-cash, high-return gold miner whose record margins rest on the gold price, trading above its own multiple history and below its 200-day average, with an unread Bosnian court ruling on its growth asset.",
  "rationale": "Quality and balance sheet are strong, but returns are gold-driven with no moat, multiples sit above their own history and peers, the trend is broken and the Vareš court ruling is unverified. Good but not compelling: AVOID.",
  "price_at_decision": 48.74,
  "price_date": "2026-11-13",
  "research_note": "research/TSX-DPM/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 20% (32.4% now), showing returns were a gold-price peak.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 40% (58.5% now), reversing the gold-driven expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}},
    {"text": "Debt/EBITDA rises above 1.0x, ending the net-cash position.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Management cuts 2026 production guidance, or a Bosnian court or regulatory ruling delays or halts Vareš (company releases)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 72.54, "basis": "Gold holds, Vareš ramps and the price retests its 52-week high of 72.54 [HI] on ROIC 32.4% and an 8.35% FCF yield [RA,ST]."},
    "base": {"probability": 0.45, "target_price_12m": 50.0, "basis": "P/E stays near 11.1x on steady TTM earnings [RA]; well above the mechanical 11.59 fair value, which applies a 2.8x 5y-median EV/EBITDA from pre-Vareš, lower-gold years and is marked unreliable (note section 3)."},
    "bear": {"probability": 0.30, "target_price_12m": 30.6, "basis": "Real yields and the dollar push gold lower and P/E reverts toward its 6.9x median [RA], near the 52-week low of 30.60 [HI]; probability raised for the overlay's small bear tilt (research/TSX-DPM/2026-11-15-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle: the returns are gold-price driven with no moat, the Vareš Constitutional Court outcome is unverified, and the mechanical base fair value (11.59) is unreliable, so a lower price alone would not justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

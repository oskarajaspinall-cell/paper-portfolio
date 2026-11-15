# Evaluation: Manhattan Associates (MANH) — 2026-11-15
## Bear case
The price already discounts heroic growth: the reverse DCF implies 38.7% year-1 revenue growth against about 11% reported [Certain] [FS fair value; note]. P/E 72.1x is +185% vs peers and the stock sits +50.6% above its 200-day average after +104.8% in six months, so it is severely extended [Certain] [ST, HI]. An extended price risks a sharp de-rating if cloud growth or bookings merely slow; P/E back at its 5y low of 47.5x would erase a large part of the price with earnings unchanged [Likely] [RA]. The macro overlay tilts toward bear (small): real yields rose 0.47pp over 3m [Likely] [macro]. The direction change is real: operating margin fell from 25.9% to 24.9% over the last year [Certain] [IS-T], which the call ties to continued investment [Likely]. FCF yield is only 2.54% [Certain]. Plaintiff-firm releases are noise but litigation status is unverified [Guessing].

## Bull case
A genuinely excellent business: ROCE 106.2%, FCF margin 32.8%, FCF conversion 178.3% and net cash [Certain] [RA, CF]. Mission-critical warehouse and order systems carry high switching costs [Likely]. Q3 delivered record bookings, cloud growth of about 28% [company-reported] and a raised outlook [Likely] [note; OV transcript]. The operating-margin dip of 1.1pp is a temporary investment choice, not lost share: FCF margin rose over the same year to 32.8% from 31.2% [Certain] [CF-T, IS-T]. On its own history the stock is mid-range, not stretched: P/E at 59% and P/FCF at 38% of the 5y range [Certain] [RA]. ROIC swings (543.1% vs a 698.0% high) reflect near-zero invested capital, not deterioration [Likely]. The share count fell 2.97% YoY [Certain] [ST]. Relative strength vs SPY is +36.3pp over 12 months [Certain] [HI].

## Decision
```json
{
  "ticker": "MANH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating margin fell 25.9% -> 24.9% TTM [IS-T] while FCF margin rose 31.2% -> 32.8% [CF-T]; the Q3 call cites continued investment alongside a raised FY margin outlook (OV transcript, /stocks/manh/transcripts/717275-q3-2026/). ROIC moves reflect negligible invested capital, not lost share.",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "De-rating: price +50.6% above its 200-day and P/E 72.1x vs peers 25.3x; any slowdown in cloud growth or bookings compresses the multiple with earnings intact, amplified by rising real yields (macro overlay).",
    "veto": null
  },
  "thesis": "A best-in-class, net-cash supply chain software compounder whose fundamentals are working, but whose price is extended well above trend and already discounts far more growth than it delivers.",
  "rationale": "Quality and momentum are excellent, but the price is severely overextended above its 200-day average, the reverse DCF demands implausible growth and the macro tilt adds multiple risk. No discount and no healthy-trend points: good but not compelling, so AVOID; a cooler trend or a lower price would revisit it.",
  "price_at_decision": 257.15,
  "price_date": "2026-11-13",
  "research_note": "research/MANH/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 22%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}},
    {"text": "TTM FCF margin falls below 28%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 28}},
    {"text": "Cloud subscription revenue growth falls below 18% year on year (10-Q / earnings release)"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 283.86, "basis": "Cloud growth and record bookings sustain the multiple; consistent with the EV/Revenue bull value of 283.86 [fact sheet fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 240.00, "basis": "Earnings grow on the raised outlook but P/E drifts from 72.1x below its 5y median of 75.1x as the extended trend cools; sits between the EV/Revenue base 275.98 and the unreliable DCF base [RA, fact sheet fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 169.40, "basis": "P/E de-rates to its 5y low of 47.5x [RA] on flat earnings; probability raised a notch from bull per the macro overlay's small tilt toward bear on rising real yields (research/MANH/2026-11-15-macro.md)."}
  },
  "entry_price": 205.00,
  "entry_basis": "Price is the obstacle, but base fair value 145.14 is flagged unreliable (methods disagree 3.5x), so the anchor is a reset to the September swing lows near 200.93 [HI] with P/FCF falling toward its 5y low of 27.9x [RA]: the trend is no longer overextended and the FCF yield is real.",
  "replaces": null,
  "replacement_reason": null
}
```

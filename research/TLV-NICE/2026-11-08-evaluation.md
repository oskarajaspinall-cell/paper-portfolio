# Evaluation: NICE Ltd. (TLV:NICE) — 2026-11-08
## Bear case
The 5-year improvement has turned over. On a rolling basis ROIC fell from 16.7% to 10.2%, operating margin from 21.9% to 17.2% and FCF margin from 26.5% to 17.6%, with gross margin down to 64.0% TTM [RA-T, IS-T, CF-T] [Certain]. The fact sheet's Direction change lines show this is not noise. Every return and margin metric is falling at once, and cloud growth is slowing, with management citing slower AI ramps and soft non-core streams (Q3 2026 transcript) [Likely]. That fits generative-AI agents shrinking contact-centre seats, NICE's pricing base [Guessing]. The Q3 profit decline and the cut of 5% of the workforce could mean weak demand rather than efficiency [Likely]. The mechanical fair value runs DCF on the fiscal-year trend that the last 12 months contradict, so it overstates value [Likely]. Israel/shekel cost and political risk is unquantified (macro overlay) [Guessing].
## Bull case
The price implies -14.2% revenue growth in year 1 while Q3 revenue grew 8% year on year and beat guidance, and FY26 EPS guidance rose (Q3 2026 transcript) [Likely]. EV/EBITDA of 7.3x, EV/Sales of 1.8x and P/B of 1.6x all sit below their own 5-year minimums, and P/E of 16.5x is at the 6th percentile of its range [RA] [Certain]. Even after the fall, the FCF yield is 9.16% and FCF/NI is 146.8% [ST, CF] [Certain]. Net cash and a 5.35% fall in the share count mean buybacks near the P/FCF low add value [ST] [Likely]. The Gartner CCaaS Leader placement suggests the franchise is still competitive [Likely]. The restructuring could rebuild operating margin toward its 22.2% 2-year high [IS-T] [Guessing].
## Decision
```json
{
  "ticker": "TLV:NICE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash contact-centre software franchise trades below its own 5-year minimum EV/EBITDA and EV/Sales, but returns, margins and cash conversion are all falling on a rolling basis while AI threatens its seat-based model, so cheapness alone does not make the skew compelling.",
  "rationale": "The valuation is extreme and Q3 beat guidance, but ROIC, operating, gross and FCF margins are all falling together and cloud growth is slowing. Until margins stabilise, the low multiple may be pricing real AI disruption rather than an error. Good but not compelling: AVOID, conviction 3.",
  "price_at_decision": 31520.00,
  "price_date": "2026-11-06",
  "research_note": "research/TLV-NICE/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 20% (17.2% now, 22.2% 2-year high), showing the restructuring is rebuilding profitability rather than masking demand loss.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 20}},
    {"text": "TTM FCF margin recovers above 22% (17.6% now, 26.5% a year earlier), showing cash generation has stabilised.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 22}},
    {"text": "TTM gross margin falls below 62% (64.0% now), confirming AI-driven price/mix pressure and closing the case.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 62}},
    {"text": "TTM ROIC falls below 8% (10.2% now), showing the return decline is structural.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 48000, "basis": "Restructuring lifts operating margin back toward the 22.2% 2-year high [IS-T] and P/E re-rates partway toward the 22.2x peer median [RA]; well below the mechanical bull of 144,666.23 because that DCF extrapolates fiscal-year margin gains that the rolling 12 months reverse."},
    "base": {"probability": 0.45, "target_price_12m": 34000, "basis": "Margins stabilise near TTM 17.2% [IS-T], P/FCF stays near its current 10.9x low-range level [RA] and buybacks (shares -5.35% [ST]) add modestly; below the mechanical base of 82,023.60 because the DCF does not capture the falling FCF margin [CF-T]."},
    "bear": {"probability": 0.30, "target_price_12m": 25000, "basis": "AI agents erode seat-based pricing, gross margin keeps sliding from 64.0% [IS] and FCF falls further while P/FCF holds near its 9.9x 5y minimum [RA]; below the mechanical bear of 59,072.04 for the same declining-trend reason, near the 24,260.00 52-week low [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its own 5-year minimum multiples and the default anchor (base 82,023.60 x 0.8) sits above the price; the obstacle is falling returns, margins and cash conversion, so a lower price would not change the decision until the margin triggers show stabilisation.",
  "replaces": null,
  "replacement_reason": null
}
```

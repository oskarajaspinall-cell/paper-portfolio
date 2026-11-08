# Evaluation: Atour Lifestyle Holdings Limited (ATAT) — 2026-11-07
## Bear case
The mechanical bear value of 16.10 sits far below the 35.91 close, and the EV/EBITDA method's base of 22.83 is also below the price: on through-cycle earnings the stock isn't clearly cheap [Certain] (fact sheet Fair value). Returns and margins have risen sharply from FY2022 and may be near a peak. China mid-scale lodging is crowded, and franchisee economics can be competed away [Likely]. Management guided net margin slightly lower on mix and tax [Likely] (https://stockanalysis.com/stocks/atat/transcripts/667938-q2-2026/). FCF conversion has fallen from 264.1% to 117.2%, and Piotroski F is only 5 [Certain] [CF,IS,ST]. Q3 results on Nov 10 are a binary event three days out [Certain]. The research is thin: the company site was blocked, so there is no segment mix or RevPAR data [Certain]. China consumer and country risk sit on top [Likely].
## Bull case
ROCE is 56.9% and ROE 59.1% TTM, operating margin has risen from 9.1% to 24.3% since FY2021, and the balance sheet is net cash (net debt/EBITDA -1.52x) [Certain] [RA,IS]. P/E of 17.2x and EV/EBITDA of 10.0x sit below their 5y minimums and well below the peer medians [Certain] [RA]. The reverse DCF implies 8.2% year-1 revenue growth, while Q2 2026 headlines show revenue up 41.4% and retail guidance raised [Likely] (https://stockanalysis.com/stocks/atat/transcripts/667938-q2-2026/). FCF yield is 6.99%, and the share count fell 0.65%, so cash goes back to holders through a dividend policy and buybacks [Certain] [ST]. The DCF base of 53.53 shows the upside if growth holds [Certain].
## Decision
```json
{
  "ticker": "ATAT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-return asset-light China hotel and retail brand trades below its own 5-year minimum P/E and EV/EBITDA, but the blended base fair value is only modestly above the price and the through-cycle earnings method values it below today's price.",
  "rationale": "Quality and cheapness against its own history are real. But the base upside is modest, the EV/EBITDA method and bear value sit below the price, the margin may be near a peak, and guidance is for a softer net margin. Q3 results are due in three days, and primary-source research is thin. Good but not compelling, so AVOID; the entry price is set instead.",
  "price_at_decision": 35.91,
  "price_date": "2026-11-06",
  "research_note": "research/ATAT/2026-11-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below 18%, giving back much of the expansion from 9.1% (FY2021) to 24.3%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18}},
    {"text": "TTM ROE falls below 35%, showing the asset-light returns step-up is reversing.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 35}},
    {"text": "TTM FCF margin falls below 12%, back toward the FY2022 low of 10.9%, showing cash generation is weakening.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA on the ratios page turns positive above 1.0x, ending the net-cash position that funds distributions."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 51.60, "basis": "Growth continues and the multiple re-rates toward its own history; matches the EV/EBITDA bull value of 51.60 and is well below the DCF bull, since the reverse DCF's 8.2% implied growth is beaten [fact sheet Fair value, RA]."},
    "base": {"probability": 0.45, "target_price_12m": 43.29, "basis": "Margins hold near 24.3% TTM with slower growth; the blended DCF/EV-EBITDA base fair value of 43.29 [fact sheet Fair value, IS]."},
    "bear": {"probability": 0.30, "target_price_12m": 22.18, "basis": "Peak-margin reversion and a softer China travel demand case; the EV/EBITDA bear value of 22.18 on through-cycle EBITDA, above the blended bear of 16.10 because net cash and buybacks cushion the downside [fact sheet Fair value, BS]."}
  },
  "entry_price": 34.63,
  "entry_basis": "valuation file: base 43.29 x 0.8, the default 20% margin of safety [ST].",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: GSK plc (LON:GSK) — 2026-10-19
## Bear case
The discount is mostly to peers, not to GSK's own history: P/E 15.8x sits at 68% of its 5y range and P/FCF 10.8x is exactly its 5y median [RA] [Certain]; only EV/EBITDA (8.1x, 17%) looks cheap [Certain]. Peers like AZN and NVS plausibly earn premiums for growth GSK may lack, and a patent-cliff risk on the HIV franchise is the likely reason for the gap [Likely]. FCF margin has fallen from 28.4% to 20.8% and FCF conversion from 159.7% to 143.1% [CF,IS] [Certain], while capex rises with the Pennsylvania hub and Belgian restructuring will bring charges [Likely]. There is no mechanical fair value to anchor upside [Certain], no revenue-growth data in the file [Certain], the stock is down 12.3% over six months and lags SPY by 21.0pp [HI] [Certain], and Q3 results land on Oct 28, 2026 [ST] [Certain]. A weaker dollar would hit reported GBP earnings (macro overlay) [Guessing].
## Bull case
Quality is rising: ROIC 13.5% to 26.4%, operating margin to 29.2%, gross margin to 73.5% [RA,IS] [Certain], with leverage down to 1.40x net debt/EBITDA [RA] [Certain] and Piotroski F of 7 [ST] [Certain]. A 9.24% FCF yield and 1.36% annual share shrinkage [ST] [Certain] give a cash return that needs no re-rating. GSK trades 29-34% below peers on P/E, EV/EBITDA, EV/Sales and P/FCF [RA] [Certain]. Shingrix and ViiV carry patent protection and payer inertia [Likely]; restructuring could lift margins further [Guessing]. Beta of 0.28 makes it defensive [ST] [Certain], and the overlay sees a small FX tailwind from the dollar's 3.1% one-month rise (macro overlay) [Likely]. Pipeline readouts such as the B7-H3 ADC add optionality [Guessing].
## Decision
```json
{
  "ticker": "LON:GSK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A rising-ROIC, 9.24%-FCF-yield pharma trades well below peers, but near its own median P/E and P/FCF with a falling FCF margin and an unpriced patent-cliff risk, so the discount looks deserved rather than mispriced.",
  "rationale": "Quality and cash returns are good, but the cheapness is only relative to faster-growing peers; on its own history P/FCF is at its median and FCF margin is declining. No fair-value anchor, no growth data and results nine days away leave an honest conviction of 3: good but not compelling, so AVOID and watch a lower entry.",
  "price_at_decision": 1862.5,
  "price_date": "2026-10-16",
  "research_note": "research/LON-GSK/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, reversing the five-year rise from 13.5% to 26.4% and showing the quality gain was not durable.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 12%, extending the five-year decline from 28.4% to 20.8% and undermining the cash-yield case.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "TTM operating margin falls below 20%, reversing the expansion to 29.2% and signalling patent-cliff or pricing erosion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA on the ratios page rises above 2.5x, back above the FY2021 peak of 2.48x, showing deals or capex are re-leveraging the balance sheet."}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 2100, "basis": "P/FCF re-rates toward its 5y max of 11.5x and P/E moves above its 12.8x median as rising ROIC and a 9.24% FCF yield narrow the peer discount [RA,ST]; probability lifted slightly by the overlay's small toward-bull dollar tilt (research/LON-GSK/2026-10-19-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 1880, "basis": "P/FCF holds at its 5y median of 10.8x [RA] with buybacks (-1.36% shares YoY [ST]) offsetting a still-declining FCF margin [CF,IS]; no mechanical fair value is available to cross-check."},
    "bear": {"probability": 0.25, "target_price_12m": 1500, "basis": "P/FCF falls below its 5y low of 9.3x [RA] as FCF margin keeps sliding from 20.8% [CF,IS] and patent-cliff and restructuring concerns dominate, toward the 52-week low of 1,592.00 [HI] and beyond."}
  },
  "entry_price": 1604,
  "entry_basis": "No base fair value was computable [data unavailable — no FX rate for GBP], so anchored on P/FCF back at its 5y low of 9.3x [RA] versus 10.8x now: at that level the same evidence would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

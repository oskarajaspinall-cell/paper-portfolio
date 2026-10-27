# Evaluation: Gaztransport & Technigaz SA (EPA:GTT) — 2026-10-27
## Bear case
The fall has a fundamental cause. The Q3 2026 call showed nine-month revenue down year on year, because weak 2025 order intake leaves fewer carriers under construction. Management gave no Q4 guide, reaffirmed 2026 without raising it, and would not be "too bullish" on 2027 [Likely]. Revenue follows orders placed one to three years earlier, so the slowdown is already locked in [Likely]. Trailing profits sit at a cycle peak: operating margin 70.1% TTM against 49.5% in FY2022 [Certain]. A P/E of 15.5x on peak earnings is therefore less cheap than it looks [Likely]. The EV/EBITDA fair-value leg (141.15) is below the price, and the DCF leg capitalises the peak margin [Certain]. Weak spot charter rates and Hormuz transit risk could delay the next order wave [Guessing]. The dip deepened the original obstacle, peak earnings with fading growth; it did not remove it [Likely].
## Bull case
The moat is intact. GTT has 96.8% gross margin, 144.8% ROIC, net cash (-0.52x net debt/EBITDA), FCF conversion of 102.9%, and no visible rival system [Certain]. Year-to-date orders are well above last year, and the Q3 transcript cites an order book of EUR 1.85bn, so the revenue dip looks like timing in a lumpy cycle rather than lost share [Likely]. The stock is in the bottom fifth of its 5y P/E and EV/EBITDA ranges, P/FCF is below its 5y minimum, and it trades well below peers on P/E [Certain]. The reverse DCF implies only 1.9% year-one revenue growth [Certain]. If this year's orders turn into vessel construction, earnings resume growth and the multiple re-rates toward its 5y median [Guessing].
## Decision
```json
{
  "ticker": "EPA:GTT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A patented, net-cash LNG-containment licensor with 144.8% ROIC is cheap against its own history, but its earnings are at a cycle peak while revenue is falling on weak 2025 orders and 2027 visibility is limited.",
  "rationale": "The dip has a cause: Q3 showed falling revenue, an unraised guide and a cautious 2027 tone. That confirms the peak-earnings obstacle behind the 2026-10-19 AVOID rather than removing it. The moat and the low multiples keep conviction at 3, not lower. Good but not compelling: no position, and cash is acceptable.",
  "price_at_decision": 181.10,
  "price_date": "2026-10-26",
  "research_note": "research/EPA-GTT/2026-10-27.md",
  "triggers": [
    {"text": "TTM gross margin falls below 90% (96.8% now), signalling a rival containment system is eroding royalty pricing.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 90}},
    {"text": "TTM operating margin falls below 49%, under the FY2022 five-year low of 49.5%, showing the revenue decline is crushing operating leverage.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 49}},
    {"text": "TTM ROIC falls below 60% (144.8% now), signalling moat economics are deteriorating.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 60}},
    {"text": "Annual revenue (income statement) declines year on year in two consecutive fiscal years, showing the order slowdown is a structural downturn, not timing."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 267.15, "basis": "Year-to-date orders well above last year convert to vessel construction, so the P/E re-rates toward its 5y median of 22.0x [RA], reaching the base fair value of 267.15 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 195, "basis": "Revenue keeps easing through 2027 on weak 2025 intake (Q3 transcript, /quote/epa/GTT/transcripts/655575-q3-2026/) and margins come off the 70.1% peak [IS], so the multiple stays near the bottom of its 5y range; this sits well below the mechanical base fair value because the DCF capitalises the peak margin."},
    "bear": {"probability": 0.30, "target_price_12m": 141.15, "basis": "The earnings downturn deepens with weak charter rates and Hormuz risk (note section 6), and the price falls to the EV/EBITDA fair-value leg of 141.15 [fact sheet Fair value], below the blended bear of 149.29."}
  },
  "entry_price": 160,
  "entry_basis": "P/E back at its 5y low of 13.7x [RA] on TTM earnings, which would pay for the peak-earnings risk. The default (valuation file: base 267.15 x 0.8) is above the price, and the DCF leg rests on a five-year-high margin.",
  "replaces": null,
  "replacement_reason": null
}
```

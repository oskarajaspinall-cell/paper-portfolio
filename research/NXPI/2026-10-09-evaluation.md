# Evaluation: NXP Semiconductors N.V. (NXPI) — 2026-10-09
## Bear case
This is a high-beta (1.81) cyclical whose cheapness rests on peak-ish earnings [Certain]. TTM operating margin of 32.9% is well above the FY2021-FY2025 band of 23.6-28.6%, so the 19.7x P/E is flattered by a cyclical high [Likely]. ROIC (-1.4pp) and ROE (-3.2pp) trends are falling and FY2025 net debt/EBITDA reached 2.28x [Certain]. The through-cycle fair value base of 133.26 sits 42.3% below the 231.07 close, and the reverse DCF implies 24.4% year-1 revenue growth, against management's own 6-8% 2027 CAGR guide [Certain]. Internal inventory of 156 days remains above the 110-day target [Likely]. The macro overlay tilts moderately toward bear: the 10y real yield rose 0.61pp in 3 months, raising the discount rate and pressuring auto financing [Likely]. Q3 results land on Oct 27, 2026, and the stock trails SPY by -14.5pp over 12 months [Certain].

## Bull case
NXP is a quality franchise: TTM ROIC 18.0%, ROCE 19.0%, gross margin a stable 55-57% and FCF margin 21.3% [Certain]. It trades at 13.0x EV/EBITDA, at the 41st percentile of its own 5y range and 54% below the peer median, and its P/B of 5.1x is below its 5y minimum [Certain]. Channel inventory has normalised to 11 weeks and book-to-bill is strong [Likely]. Management reaffirmed its 2027 targets of a 57-63% gross margin and a 34-40% operating margin, driven by software-defined-vehicle content [Likely]. Piotroski F of 7 and Altman Z of 3.58 show no distress, and the share count fell 0.61% YoY [Certain]. If earnings hold, a return to the 5y median 13.8x EV/EBITDA supports the EV/EBITDA method's base of 244.61 [Likely].

## Decision
```json
{
  "ticker": "NXPI",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return auto/industrial semiconductor franchise trades below peers, but at mid-range own-history multiples on above-cycle margins, and the price implies growth far above management's own guide.",
  "rationale": "Quality is real, but the discount to peers reflects cyclicality. Own-history multiples are mid-range on a cyclically high 32.9% operating margin, and the reverse DCF implies 24.4% growth against a 6-8% guide. The macro overlay tilts toward bear, and Q3 results are on Oct 27. The expected value sits below the price. Good but not compelling: AVOID.",
  "price_at_decision": 231.07,
  "price_date": "2026-10-08",
  "research_note": "research/NXPI/2026-10-09.md",
  "triggers": [
    {"text": "TTM gross margin falls below 54%, under the FY2021 5-year low of 54.8%, showing that pricing power or mix is eroding and undercutting the 57-63% 2027 target.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 54}},
    {"text": "TTM operating margin falls below 23.6%, the FY2021 5-year low, showing that the margin expansion has fully reversed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 23.6}},
    {"text": "TTM ROIC falls below 12%, under the 5-year low of 14.0%, showing that the moat is no longer defending returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Automotive segment revenue (earnings release) declines year on year for two consecutive quarters outside a broad industry downturn."}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 281.04, "basis": "Management delivers its reaffirmed 2027 margin targets (transcripts) and EV/EBITDA rerates toward peers, reaching the EV/EBITDA method's bull of 281.04, near the 280.46 swing high [HI]; the probability is cut from 0.25 because the macro overlay's moderate bear tilt (research/NXPI/2026-10-09-macro.md) weighs on the re-rating."},
    "base": {"probability": 0.45, "target_price_12m": 240.00, "basis": "EV/EBITDA drifts from 13.0x toward its 13.8x 5y median [RA] on roughly flat TTM EBITDA, which is below the EV/EBITDA method's base of 244.61 because the 0.61pp real-yield rise holds multiples back (macro overlay); the through-cycle DCF base of 133.26 is not used because its 5.28% risk-free rate and 1.81 beta penalise a franchise with 18% ROIC [RA]."},
    "bear": {"probability": 0.35, "target_price_12m": 162.89, "basis": "The cycle rolls over from the above-range 32.9% TTM operating margin [IS] and EBITDA falls, putting the stock at the EV/EBITDA method's bear of 162.89, still above the DCF bear because the 2027 targets and 11-week channel inventory (transcripts) argue against a trough at the 5y-low margins; the probability is raised from 0.25 by the macro overlay's moderate bear tilt (research/NXPI/2026-10-09-macro.md)."}
  },
  "entry_price": 172.00,
  "entry_basis": "P/E back at its 5y low of 14.7x [RA] on current TTM earnings (from 19.7x at 231.07); at that level the price would compensate for the cyclically high margin. Not the default base 133.26 x 0.8, because the through-cycle DCF understates an 18% ROIC franchise.",
  "replaces": null,
  "replacement_reason": null
}
```

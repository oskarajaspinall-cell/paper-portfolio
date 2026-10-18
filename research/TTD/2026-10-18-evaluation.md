# Evaluation: The Trade Desk, Inc. (TTD) — 2026-10-18
## Bear case
This is a franchise problem, not a valuation problem. The FY2026 Q2 10-Q shows revenue up only 3% YoY, "primarily driven by... a decrease in gross spend from existing clients" [company-reported], and adds new risk language on competition, AI disruption, agencies and suppliers trading directly, and holding-company consolidation [Likely]. Gross margin has slid from 81.5% to 76.9% TTM [Certain], which points to pricing power eroding against Amazon- and Google-scale DSPs [Likely]. A restructuring with exit costs (8-K, 2026-09-04) shows management is reacting to the problem, not ahead of it [Likely]. The stock is down 76.1% over 12 months with short interest at 20.06% of float [Certain]: informed money expects further losses [Likely]. The DCF leg ($19.45) is built on own-history growth that no longer applies, and the EV/EBITDA leg ($96.51) borrows multiples from far faster-growing peers [Likely]. Rising real yields add a small headwind (macro overlay) [Certain].
## Bull case
The price already assumes the stall is permanent: the reverse DCF implies -0.3% revenue growth, while H1 2026 revenue still grew 7% [company-reported] [Certain]. The business remains highly profitable and cash-rich: TTM ROIC 24.8%, operating margin 19.6%, FCF margin 28.9%, net cash (net debt/EBITDA -1.51x), Altman Z 4.72 [Certain]. At a 14.93% FCF yield and P/FCF of 6.7x, against a 5y minimum of 23.1x and a peer median of 29.8x, buybacks (shares -4.27% YoY) compound quickly if cash flow holds [Certain]. Even the conservative DCF leg ($19.45) sits above the $12.23 close [Certain]. The restructuring could lift margins, and ongoing partner integrations (Veeva Crossix, IQVIA, OptimizeRx) suggest the platform is still gaining data partners [Likely]. Short interest of 20.06%, down 5.0% month-on-month, leaves room for a sharp squeeze if Q3 FY2026 results (Nov 5, 2026) show stabilisation [Guessing].

## Decision
```json
{
  "ticker": "TTD",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-FCF ad-tech platform trades far below its own 5-year multiples, but revenue growth has stalled on falling spend from existing clients and gross margin is eroding, so the cheapness may reflect a lasting loss of competitive position rather than mispricing.",
  "rationale": "Cash generation and the multiple are compelling, but the thesis hinges on revenue stabilising, which the latest 10-Q contradicts: spend from existing clients fell, gross margin is falling and a restructuring is under way. Evidence of a structural share loss is unresolved before Q3 results, so conviction is 3: good but not compelling. Cash is acceptable.",
  "price_at_decision": 12.23,
  "price_date": "2026-10-16",
  "research_note": "research/TTD/2026-10-18.md",
  "triggers": [
    {"text": "Q3 FY2026 or later 10-Q shows quarterly revenue growth back above 5% YoY and MD&A no longer cites a decrease in gross spend from existing clients, evidence the stall is not structural (would raise conviction)."},
    {"text": "TTM gross margin falls below 75%, confirming further erosion of pricing power and value-added-service mix.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 75}},
    {"text": "TTM FCF margin falls below 20%, showing cash generation is deteriorating alongside growth and removing the cash-yield support.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 29.35, "basis": "Q3 FY2026 shows client spend stabilising and the restructuring protects the 28.9% FCF margin [CF,IS], so the price reaches the DCF bull value of 29.35 [IS,BS,CF,RA,ST], well below the blended bull because the EV/EBITDA leg's peer-like multiples are not credible for a low-growth name (note section 3)."},
    "base": {"probability": 0.45, "target_price_12m": 12.23, "basis": "Growth stays near the 3% Q2 rate [company-reported, sec.gov 10-Q] that the reverse DCF's -0.3% year-1 growth already roughly prices, so multiples stay below their 5y minimums [RA] and the price holds near the close; below the DCF base of 19.45 because that leg assumes own-history growth the 10-Q contradicts."},
    "bear": {"probability": 0.35, "target_price_12m": 6.23, "basis": "Spend from existing clients keeps falling and gross margin keeps eroding from 76.9% [IS], so the price falls to the mechanical bear fair value of 6.23 [IS,BS,CF,RA,ST,HI]; probability raised slightly because the macro overlay (research/TTD/2026-10-18-macro.md) tilts toward bear (small) on rising real yields and credit spreads."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: at a 14.93% FCF yield the stock is already cheap; the obstacle is unresolved evidence of structural client-spend loss and falling gross margin, so a lower price on the same evidence would not justify conviction 4. Re-research on Q3 FY2026 results.",
  "replaces": null,
  "replacement_reason": null
}
```

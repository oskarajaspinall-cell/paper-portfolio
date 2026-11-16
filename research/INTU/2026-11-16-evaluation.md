# Evaluation: Intuit Inc. (INTU) — 2026-11-16
## Bear case
The 47.4% fall over 12 months [ST] is the market pricing a structural break, not a cheap multiple [Likely]. The latest filing adds free and low-cost competition and government filing risk [Certain], TurboTax federal units fell [company-reported], and Intuit's own Credit Karma Tax now offers free federal filing, which may cannibalise paid tiers [Likely]. AI-native entrants could compress QuickBooks and TurboTax pricing faster than margins show [Guessing]. Gross margin is 81.0% against 82.2% in FY2022 [IS], the one quality line drifting the wrong way [Certain]. The price sits 2.4% below its 200-day average with the 50-day 9.1% below the 200-day [ST], so the trend has not turned [Certain]. Results on Nov 19, 2026 are a near-term event; a weak guide could retest the 252.84 low [Guessing]. Mean-reversion to the 60.1x median P/E is unlikely if growth is being re-based [Likely].
## Bull case
Every rolling quality line is at its 2-year high: ROIC 22.9% (from 18.5%), operating margin 28.8%, FCF margin 40.4% [RA-T, IS-T, CF-T] [Certain]. Nothing in the delivered numbers shows the disruption the price discounts: Global Business Solutions grew 16% and Consumer 11% in fiscal 2026 [company-reported] [Certain]. The reverse DCF implies just 1.5% year-1 revenue growth [Certain]. The stock is in the bottom 5% of its own 5-year range on P/E, EV/EBITDA and P/FCF, at a 9.30% FCF yield, below peers on P/FCF and P/B [RA] [Certain]. Net debt/EBITDA is 0.18x and the share count fell 2.12% YoY, so buybacks compound per-share value at this yield [Certain]. Even the DCF-only base of 452.92 sits well above the price [Likely]. Switching costs in the QuickBooks payroll/payments ecosystem make wholesale share loss slow [Likely].
## Decision
```json
{
  "ticker": "INTU",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Python finds no falling ROIC, operating margin or FCF margin over 1 or 3 years; ROIC 22.9%, operating margin 28.8% and FCF margin 40.4% are all at their 2-year highs [RA-T, IS-T, CF-T].",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Free and AI-driven tax filing (including Intuit's own Credit Karma Tax) and AI-native small-business tools erode TurboTax and QuickBooks pricing, turning the market's disruption discount into falling margins; flagged in the latest 10-K risk factors.",
    "veto": null
  },
  "thesis": "A net-cash, 40%-FCF-margin financial-software franchise with ROIC and margins at their 2-year highs trades at the floor of its own 5-year multiples, pricing near-zero growth that delivered segment growth contradicts.",
  "rationale": "Scorecard conviction 4, unchanged from the 2026-11-08 HOLD on the same evidence. The position already sits at its conviction-4 core size, so an ADD would buy no extra size; free/AI filing risk and the unturned trend argue against going above it ahead of results on Nov 19.",
  "price_at_decision": 341.70,
  "price_date": "2026-11-13",
  "research_note": "research/INTU/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 16%, giving up the rise from 18.5% a year earlier to 22.9% and signalling the returns expansion has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 16}},
    {"text": "TTM FCF margin falls below 30%, back near the FY2024 level of 28.8%, meaning the FY2026 cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "TTM gross margin falls below 78%, under the FY2023 five-year low of 79.3%, signalling free/AI tax-filing competition is forcing price cuts.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 78}},
    {"text": "Global Business Solutions revenue growth in the 10-Q segment note falls below 8% for two consecutive quarters, or Consumer segment revenue declines year on year for two consecutive reported periods."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 568.43, "basis": "Delivered growth disproves the disruption discount and the multiple recovers to the fact sheet's blended base fair value of 568.43 [IS,BS,CF,RA,ST,HI], below the mechanical bull of 672.84 because a full return to the 60.1x 5y median P/E [RA] is unlikely."},
    "base": {"probability": 0.50, "target_price_12m": 452.92, "basis": "Margins hold near 28.8% operating and 40.4% FCF [IS-T, CF-T] and the price moves to the DCF base of 452.92 [IS,BS,CF,RA,ST]; the EV/Revenue leg is excluded because its 5y median 10.4x [RA] reflects a pre-disruption rating."},
    "bear": {"probability": 0.25, "target_price_12m": 249.85, "basis": "Free/AI filing competition flagged in the 10-K (https://www.sec.gov/Archives/edgar/data/896878/000089687826000037/intu-20260731.htm) compresses pricing and the stock falls to the mechanical bear fair value of 249.85, near the 52-week low of 252.84 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Not applicable as an obstacle: the holding is already at conviction 4 and its full core size, and the price is well below the base fair value; a lower price would not change the HOLD, only a thesis trigger or new results would.",
  "replaces": null,
  "replacement_reason": null
}
```

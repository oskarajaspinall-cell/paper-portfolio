# Evaluation: Intuit Inc. (INTU) — 2026-11-08
## Bear case
The market is pricing AI and free filing as a structural threat to TurboTax. The 10-K adds risk language on free competitors, government filing systems and AI, and TurboTax federal units fell [company-reported] [Likely]. Intuit's own free Credit Karma Tax may cannibalise paid TurboTax [Guessing]. Gross margin is the one quality line falling on the five-year view (-1.2pp) [IS] [Certain]. The stock is -47.9% over 12 months with relative strength vs SPY of -56.4pp, and the 50-day sits below the 200-day [ST,HI] [Certain]. The mechanical bear fair value of 255.95 is below the price [Certain]. Mailchimp's resegmentation from Aug 1, 2026 will muddy segment comparisons [company-reported] [Certain]. Fiscal Q1 results on Nov 19 are a near-term binary [Certain]. There is no Direction change line and no material country risk (about 8% non-US, no country near 10%) [company-reported], so the threat is competitive, not macro [Certain].

## Bull case
Fundamentals are improving on both views: the rolling 12 months show ROIC 22.9% vs 18.5%, operating margin 28.8% vs 26.2% and FCF margin 40.4% vs 32.5%, each at its 2-year high [RA-T,IS-T,CF-T] [Certain]. Net debt/EBITDA is 0.18x and the share count fell 2.12%, so buybacks at a 9.49% FCF yield are accretive [ST] [Certain]. Every multiple sits in the bottom 4% of its 5y range and below the peer median (P/FCF 10.5x vs 16.3x) [RA] [Certain]. The reverse DCF implies 0.6% year-1 revenue growth, far below what the business is delivering [Likely]. Global Business Solutions, 60% of revenue [company-reported], is the QuickBooks ledger with payments and payroll attached, a sticky small-business moat that AI tax tools do not directly attack [Likely]. Base fair value of 581.05 sits well above the 341.50 close [Certain].

## Decision
```json
{
  "ticker": "INTU",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A net-cash, 40%-FCF-margin financial-software franchise with ROIC and margins at their 2-year highs on a rolling basis trades at the floor of its own 5-year multiples, pricing near-zero growth that delivered results contradict.",
  "rationale": "Rolling-12-month returns and cash margins are still rising with no Direction change, leverage is minimal and buybacks are accretive at a 9.49% FCF yield. AI/free-filing risk to TurboTax and the Nov 19 print cap conviction at 4, not 5. The position is at its conviction size, so HOLD rather than ADD.",
  "price_at_decision": 341.50,
  "price_date": "2026-11-06",
  "research_note": "research/INTU/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 16%, giving up the rise from 18.5% a year earlier to 22.9% and signalling the returns expansion has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 16}},
    {"text": "TTM FCF margin falls below 30%, back near the FY2024 level of 28.8%, meaning the FY2026 cash step-up was transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "TTM gross margin falls below 78%, under the FY2023 five-year low of 79.3%, signalling free/AI tax-filing competition is forcing price cuts.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 78}},
    {"text": "Consumer segment revenue (10-Q) declines year on year for two consecutive reported periods, or Global Business Solutions revenue growth falls below 10% for a full year, showing free filing and AI eroding the base."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 601.70, "basis": "Rolling FCF margin of 40.4% and ROIC of 22.9% hold [CF-T,RA-T] and the market re-rates toward the DCF bull value of 601.70 [fact sheet Fair value]; set below the EV/Revenue bull because the 5y median multiples reflect a pre-AI-risk era."},
    "base": {"probability": 0.5, "target_price_12m": 471.84, "basis": "Margins stay near TTM levels and the DCF base of 471.84 [fact sheet Fair value] is the anchor; set below the blended base of 581.05 because the EV/Revenue leg assumes a return to 5y median multiples the AI/free-filing risk in the 10-K delta (note section 2) argues against."},
    "bear": {"probability": 0.25, "target_price_12m": 255.95, "basis": "TurboTax units keep falling as free and AI filing spread (10-K, note section 2) and the multiple stays at its 5y floor while earnings reset: the mechanical bear fair value of 255.95 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is already 4 at the current price; no lower entry level is needed for a HOLD at the buy bar.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Coal India Limited (COALINDIA) — 2026-10-25
## Bear case
Returns are falling from a peak, not settling at one. ROIC went from 158.9% (FY2023) to 30.0% (FY2026) and 28.9% TTM. Operating margin fell from 30.6% (FY2024) to 17.8% TTM, and gross margin from 86.2% to 74.8% [Certain]. On those earnings the stock is not cheap against its own history: P/E is 7.9x against a 5y median of 6.9x, and EV/EBITDA is 4.9x against 4.6x and in line with peers at 5.0x [Certain]. State control caps pricing and is pushing capital into iron ore, minerals trading and a possible Chilean lithium deal, so the net-cash balance sheet may be spent on policy rather than returned to shareholders [Likely]. FCF conversion swings widely, from 3.4% in FY2024 to 98.8% in FY2026 [Certain]. Results come on Oct 29, 2026, so the next data point is days away [Certain]. Decarbonisation is a long-term risk to volumes [Guessing].

## Bull case
At a 12.54% FCF yield and P/FCF of 8.0x (5y median 9.7x) with net cash (-1.04x net debt/EBITDA), the price allows for a lot of bad news [Certain]. The reverse DCF implies -7.3% year-1 revenue growth, a decline the business has not reported [Likely]. P/B of 2.0x is below its 5y minimum [Certain]. Demand looks firm: 57 power plants reported critically low stocks (https://timesofindia.indiatimes.com/india/cil-offers-extra-fuel-57-plants-now-report-critically-low-stock/articleshow/133814003.cms) [Likely]. Subsidiary IPOs (MCL filed; https://www.reuters.com/world/india/coal-india-unit-mahanadi-coalfields-files-ipo-2026-09-01/) could bring hidden value to the surface [Guessing]. The blended base fair value of 549.71 INR is well above the 397.45 close [Certain]. Beta of 0.02 means the stock moves little with the market [Certain].

## Decision
```json
{
  "ticker": "NSE:COALINDIA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-FCF state monopoly priced for decline, but with returns and margins still normalising down and capital being redirected to unproven diversification, the cheapness does not yet amount to a compelling core position.",
  "rationale": "FCF yield and net cash are attractive, but the multiples sit only around their history and peer medians while ROIC and margins are still falling. The wide DCF range makes the fair-value gap low-confidence, and results due Oct 29 could reset earnings. Good but not compelling: AVOID, then re-research once results show whether margins have stabilised.",
  "price_at_decision": 397.45,
  "price_date": "2026-10-23",
  "research_note": "research/NSE-COALINDIA/2026-10-25.md",
  "triggers": [
    {"text": "ROIC (statistics page) TTM falls below 20%: the high-return thesis is broken", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Operating margin (statistics page) TTM falls below 14%: normalisation has turned into structural decline", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 14}},
    {"text": "FCF margin (statistics page) falls below 8%: the cash yield case fails", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "Net debt / EBITDA (ratios page) turns positive, above 0.5x, from debt-funded diversification or acquisitions"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 549.71, "basis": "Margins stabilise near the FY2026 operating margin of 18.6% [IS] and the market stops pricing the -7.3% decline in the reverse DCF, re-rating to the blended base fair value 549.71 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 420, "basis": "Multiples stay near their 5y medians (EV/EBITDA 4.6x, P/E 6.9x [RA]) on roughly flat earnings, between the EV/EBITDA method value 375.60 and the blended 549.71, which we discount because the through-cycle DCF ranges from 30.58 to 1,337.85 [fact sheet Fair value]."},
    "bear": {"probability": 0.30, "target_price_12m": 300, "basis": "ROIC and operating margin keep falling from 28.9% and 17.8% TTM [RA,IS] while capital goes to lithium and iron ore (https://www.reuters.com/business/energy/coal-india-weighs-buying-canadas-wealth-minerals-unit-chile-lithium-assets-2026-08-11/); held well above the mechanical bear 89.64 by net cash at -1.04x net debt/EBITDA [BS,IS]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the close is already below base fair value 549.71 x 0.8. What holds conviction at 3 is the still-falling ROIC and margin trend and the unproven diversification spending; a lower price would not change that. Re-research after the Oct 29 results.",
  "replaces": null,
  "replacement_reason": null
}
```

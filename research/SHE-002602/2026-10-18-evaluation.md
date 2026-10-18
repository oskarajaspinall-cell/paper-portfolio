# Evaluation: Zhejiang Century Huatong Group Co.,Ltd (SHE:002602) — 2026-10-18
## Bear case
The quality record is mostly a two-year inflection, not a franchise: ROIC was 1.8%-3.9% through FY2023 and only reached 33.1% TTM after FY2024-25 [Certain] [RA]. Gaming is hit-driven and the note cannot verify the durability of the current game portfolio or content approvals [Guessing]. The market is voting against the margins: the stock is down 35.9% in 12 months, 50.7pp behind SPY, with the 50-day average 10.1% below the 200-day, while reported metrics improved — consistent with investors expecting the hit to fade [Likely] [HI,ST]. The mechanical bear fair value is negative (-6.30), showing how sensitive value is to margin reversion [Certain]. A conglomerate structure with auto parts, a FY2022 loss year of unexplained cause, 1.71% share dilution and low institutional ownership (19.8%) add governance noise [Likely] [ST,IS]. Q3 results on Oct 29, 2026 could confirm decay [Guessing].
## Bull case
On every fact-sheet measure the business has improved: gross margin 71.5% TTM, operating margin 21.0%, FCF margin 19.0% with FCF conversion of 109.3%, and net cash (-1.23x net debt/EBITDA) [Certain] [IS,CF,RA]. Yet the stock trades at 11.9x P/E and 7.9x EV/EBITDA, below its own 5-year minimums (22.2x, 9.2x) and below the peer median on every multiple, at a 9.10% FCF yield [Certain] [RA,ST]. The reverse DCF prices only 1.2% revenue growth fading to terminal, so even flat earnings support the price [Certain]. Base fair value is 22.04, well above the 12.27 close [Certain]. Piotroski 7 and Altman Z 8.13 argue against balance-sheet stress [Certain] [ST]. If Q3 shows margins holding, a re-rating toward the peer median is plausible [Likely].
## Decision
```json
{
  "ticker": "SHE:002602",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash gaming-led conglomerate whose returns inflected sharply in FY2024-25 trades below its own 5-year minimum P/E and EV/EBITDA, but the durability of hit-driven earnings is unproven and the share price is falling against the reported numbers.",
  "rationale": "Cheap on every multiple with strong cash conversion, but the quality record is only two years long, gaming earnings are hit-driven with no verifiable pipeline, the mechanical bear value is negative, and results due Oct 29 are an imminent test. It would also add a fourth China name. Good but not compelling: AVOID.",
  "price_at_decision": 12.27,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-002602/2026-10-18.md",
  "triggers": [
    {"text": "TTM gross margin falls back below 60%, reversing the FY2024-25 step-up and signalling the game portfolio is aging without replacement hits.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 60}},
    {"text": "TTM ROIC falls back below 10%, undoing the FY2024-25 improvement and showing the returns inflection was transitory.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM net margin falls back into single digits, repeating the pre-2024 profitability pattern rather than the TTM 17.4%.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA on the ratios page turns positive beyond 0.5x, showing the net-cash position is being spent without a commensurate return."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 15.3, "basis": "Q3 confirms 71.5% gross margin [IS] holds and P/E re-rates to the 14.8x peer median [RA] on TTM earnings; still below the 22.04 base fair value because the DCF assumes margin durability the note cannot verify."},
    "base": {"probability": 0.45, "target_price_12m": 12.5, "basis": "Earnings roughly flat, as the reverse DCF's 1.2% implied growth assumes, and P/E stays near the current 11.9x [RA]; below the 22.04 base fair value because hit-driven gaming earnings warrant a discount to own-history multiples set before the inflection."},
    "bear": {"probability": 0.3, "target_price_12m": 9.0, "basis": "The lead games decay and margins revert toward FY2023 levels (operating margin 12.5% [IS]) at a similar P/E, in line with the 12-month -35.9% price trend [ST]; above the negative -6.30 bear fair value, which the note calls a modelling artifact given net cash [BS]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its own 5-year minimum multiples and the base fair value less a 20% margin of safety sits above the price. What would lift conviction to 4 is evidence that hit-driven margins are durable (Q3 results on Oct 29, 2026 and beyond), so a lower price alone would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

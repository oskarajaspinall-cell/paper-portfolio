# Evaluation: RenaissanceRe Holdings Ltd. (RNR) — 2026-11-08
## Bear case
The cycle is turning against it. Q3 premiums earned fell on property rate reductions and reduced casualty exposure [company-reported] (https://www.sec.gov/Archives/edgar/data/913144/000091314426000098/rnr-20260930.htm) [Certain]. The **Direction change** line matters: TTM ROIC of 13.1% sits 11.5pp below its 2-year high of 24.5% [RA-T]. The driver is softer pricing plus large-loss events, so returns are normalising downward [Likely]. That threatens any thesis built on peak-cycle ROE [Likely]. Q3 was a net loss, and tangible book value fell on mark-to-market losses [OV] [Certain]. Q3 large-loss estimates (Ras Laffan, Middle East energy, Colombia) could develop adversely [company-reported] [Likely]. The stock is not cheap. P/E of 9.7x is above its 5y max and the 8.4x peer median, and P/B of 1.3x is in line with peers [RA] [Certain]. Buybacks at this P/B add less value per share [Likely]. The mechanical fair value rests on a sustainable-ROE assumption; the P/E method gives 177.36 [Certain].
## Bull case
RenaissanceRe is a top-tier cat underwriter. Even in a large-loss quarter the combined ratio was 79.7% [company-reported], and operating income was positive [OV] [Certain]. The share count fell 12.29% YoY [ST], so per-share book compounds faster than earnings [Certain]. Fee income from DaVinci, Fontana and Upsilon adds capital-light earnings [Likely]. Leverage is low at 0.18x net debt/EBITDA [RA] [Certain]. Beta of 0.13 [ST] gives diversification from the rest of the book [Certain]. The P/B+ROE method yields 703.55 and the blended base fair value is 528.15, against a 347.35 close [Certain]. If ROE holds in the mid-teens, the stock compounds book with optionality from higher reinvestment yields [Likely]. Momentum is strong (+21.4pp vs SPY over 12 months) [HI] [Certain].
## Decision
```json
{
  "ticker": "RNR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A best-in-class catastrophe reinsurer compounding book value via buybacks, but entering a softening rate cycle with returns well off peak and a valuation already at peer level and above its own history.",
  "rationale": "Underwriting quality and buybacks are real, but property rates are falling, ROIC is far below its 2-year high and P/B and P/E sit at or above peers. The high mechanical fair value hinges on a sustainable-ROE assumption that a soft market may not deliver. Expected value sits only modestly above the price: good, not compelling.",
  "price_at_decision": 347.35,
  "price_date": "2026-11-06",
  "research_note": "research/RNR/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE rises above 18% (14.0% now), showing returns are re-accelerating rather than normalising in a soft market.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 18}},
    {"text": "TTM ROIC rises above 18% (13.1% now), back toward FY2025's 18.1%, confirming the cycle has not turned.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 18}},
    {"text": "The 10-Q or earnings release reports property-catastrophe rate increases at renewal, reversing the Q3 property rate reductions."},
    {"text": "Q3 2026 large-loss estimates develop favourably in the next 10-Q, with tangible book value per share plus dividends growing quarter on quarter."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 469.06, "basis": "ROE holds in the mid-teens with continued buybacks (shares -12.29% YoY [ST]); reaches the mechanical bear fair value of 469.06 [fact sheet Fair value], below the base 528.15 because that rests on a sustainable ROE the softening cycle may not deliver (note section 3)."},
    "base": {"probability": 0.5, "target_price_12m": 360.0, "basis": "Book compounds at a TTM-like ROE of 14.0% [RA] while P/B stays near the 1.3x peer median [RA] and property rates soften (10-Q); well below the mechanical base 528.15 because the P/E method alone gives 177.36 [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 275.61, "basis": "Q3 large-loss estimates develop adversely and rate cuts deepen (https://www.sec.gov/Archives/edgar/data/913144/000091314426000098/rnr-20260930.htm), ROE falls toward the note's 10% trigger and the stock returns to its 6-month low of 275.61 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the mechanical base fair value already sits above the price, so a margin-of-safety level would be above today's close. The obstacle is the softening property rate cycle and unsettled Q3 loss estimates; evidence that returns re-accelerate (triggers) would change the decision, not a lower price.",
  "replaces": null,
  "replacement_reason": null
}
```

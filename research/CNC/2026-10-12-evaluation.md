# Evaluation: Centene Corporation (CNC) — 2026-10-12
## Bear case
The cheap multiples sit on earnings that have not yet proved real. TTM ROE is -20.4% and TTM FCF conversion is -175.5%, so the 27.72% FCF yield and 3.6x P/FCF rest on cash flows that do not match earnings [Certain]. No fair value can be computed because TTM EPS is negative [Certain]. ROIC has been low and volatile (3.1%-8.8%), and margins are a government-set spread that Centene does not control. Medicaid rate adequacy and ACA risk pools could reprice against it again, as they did in FY2025 [Likely]. Leverage is unresolved: net debt/EBITDA reads 3.50x or -1.75x depending on the definition [Certain]. The stock is already up 70.0% in 12 months. Q3 results land on Oct 27, short interest rose 6.5% and options flow turned bearish, so there is gap risk around the print [Guessing]. Healthcare is already about 14% of the portfolio through CI and ZTS [Certain].
## Bull case
The 2026 recovery is visible. Q2 HBR improved to 89.6% from 93.0%, FY2026 GAAP EPS guidance was raised above $3.11, and management reaffirmed guidance on 16 September [Certain]. The shares still trade on EV/EBITDA of 5.3x, below their 5-year minimum of 5.5x and 66% below the peer median of 15.5x. P/B is 1.4x against a peer median of 2.6x [Certain]. Shares outstanding fell 2.48% YoY [Certain]. If HBR holds and FY2025 drops out of the TTM figures, ROE turns positive and the stock can re-rate toward its 5-year median multiples (EV/EBITDA 8.1x, P/B 1.5x) [Likely]. Centene's scale as the largest Medicaid MCO keeps its state contracts sticky between re-bids [Likely].
## Decision
```json
{
  "ticker": "CNC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Centene's 2026 margin recovery looks cheap at 5.3x EV/EBITDA and 1.4x book, but negative TTM ROE and FCF conversion, a government-set thin moat and unresolved leverage leave the recovery unproven.",
  "rationale": "The valuation is attractive, but the earnings quality is unproven. TTM ROE is -20.4%, FCF conversion is -175.5%, no fair value is computable and the leverage figures conflict. The Q3 print on Oct 27 is binary, and healthcare is already about 14% of the portfolio. Good but not compelling, so cash is preferred. Re-research once Q3 confirms HBR and cash conversion.",
  "price_at_decision": 65.36,
  "price_date": "2026-10-09",
  "research_note": "research/CNC/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROE returns above 10% (statistics page), showing that FY2025's -28.7% loss has rolled off and the recovery is showing up in reported returns.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 10}},
    {"text": "FCF conversion (cash-flow vs income statement) turns positive for two consecutive quarters, proving that earnings are backed by cash."},
    {"text": "Medicaid HBR in the earnings release rises back above 93.9% for two or more quarters, confirming that rate inadequacy has returned and the AVOID stands."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 88.7, "basis": "HBR gains hold and ROE turns positive, so P/B re-rates to its 5y high of 1.9x [RA] on today's book (price 65.36 / 1.4x); no mechanical fair value exists because TTM EPS is negative [IS], so own-history P/B is the anchor."},
    "base": {"probability": 0.45, "target_price_12m": 70.0, "basis": "Raised FY2026 guidance is delivered but cash conversion stays unproven, so P/B moves only to its 5y median of 1.5x [RA]; the fair-value section is [data unavailable], so P/B on book replaces it."},
    "bear": {"probability": 0.3, "target_price_12m": 46.7, "basis": "Medicaid rate inadequacy or ACA repricing returns as in FY2025 (ROE -28.7% [RA]), so P/B falls back to its 5y low of 1.0x [RA]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: no base fair value is computable, and the stock already trades below its 5y minimum EV/EBITDA and P/FCF [RA]. What is missing is proof that ROE and FCF conversion have recovered, which a lower price would not supply. Re-research after the Oct 27 Q3 results.",
  "replaces": null,
  "replacement_reason": null
}
```

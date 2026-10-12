# Evaluation: Omnicom Group Inc. (OMC) — 2026-10-12
## Bear case
The IPG merger has broken the return profile: ROIC fell from 22.8% (FY2024) to 3.1% (FY2025) and is only 9.9% TTM, ROE 6.1% [Certain] [RA]. Leverage has doubled, net debt/EBITDA 1.09x to 2.20x [Certain] [BS,IS]. Shares rose 27.34% YoY [Certain] [ST], so per-share value creation depends on synergies that have no disclosed target [Certain] (note §2). The second valuation method, EV/EBITDA, puts base fair value at 54.46, below the 76.48 close [Certain] [fact sheet]; the 147.22 blend rests on a DCF that capitalises a FY2025 FCF margin of 16.1%, far above the 5.9%-10.2% of FY2021-24 [Likely]. Short interest is 9.59% and rising, Altman Z 1.23, and the stock lags SPY by 19.6pp over 12 months [Certain] [ST,HI]. Rising real yields lower the DCF range further (macro overlay) [Likely]. Agency fee pressure is structural [Likely].

## Bull case
On cash, OMC is cheap: P/FCF 8.8x is below its 5y minimum of 9.1x, EV/EBITDA 7.9x sits at the bottom of its 7.8x-10.7x range and below the 8.5x peer median, and the FCF yield is 11.39% [Certain] [RA,ST]. The reverse DCF implies -12.2% revenue growth in year 1, while management guides 4.5-5% organic growth [Likely] (Communacopia transcript [OV]). Q2 2026 delivered 6.1% organic growth and 20.4% adjusted EBITDA growth with guidance raised [Likely] (Q2 transcript [OV]). Operating margin has held at about 14.3-15.1% through the merger [Certain] [IS], so the profit collapse is integration accounting, not the business [Likely]. Leverage of 2.4x sits inside a 3.5x covenant [Certain] (SEC 10-Q). The company leads on media billings and new-business wins [Likely] (news [OV]).

## Decision
```json
{
  "ticker": "OMC",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "The world's largest ad holdco trades at an 11.39% FCF yield and below its own 5-year P/FCF minimum on merger-depressed earnings, but whether the IPG integration creates value per share is not yet proven by returns, leverage or a disclosed synergy target.",
  "rationale": "The stock is cheap on cash multiples, but ROIC has collapsed, leverage has doubled, there was 27% dilution and no synergy target is disclosed. The EV/EBITDA method puts base value below the price, and the DCF upside relies on an unusually high FY2025 FCF margin. Q3 results on Oct 23 will be the test. Good but not compelling: AVOID.",
  "price_at_decision": 76.48,
  "price_date": "2026-10-09",
  "research_note": "research/OMC/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC recovers above 15% (9.9% TTM, 22.8% FY2024), showing integration costs were one-off and the combined business earns its pre-merger returns.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 15}},
    {"text": "TTM FCF margin holds above 10% (10.7% TTM) after the merger, confirming that cash conversion is durable and not a FY2025 working-capital release.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Management discloses a quantified synergy target and keeps or raises the 4.5-5% organic growth guidance at Q3 2026 results; a cut below that range would confirm merger-driven client attrition."},
    {"text": "Net debt/EBITDA (site definition) falls back below 2.0x from 2.20x TTM, showing deleveraging from asset disposals and FCF rather than further drift toward the 3.5x covenant."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 106, "basis": "Integration proves out and P/FCF re-rates from 8.8x to its 5y median of 12.2x [RA]. This sits well below the 147.22 base fair value because the DCF capitalises the above-history FY2025 FCF margin of 16.1% [CF,IS]."},
    "base": {"probability": 0.45, "target_price_12m": 85, "basis": "Guided 4.5-5% organic growth is delivered (Communacopia transcript [OV]) and EV/EBITDA moves partway from 7.9x toward its 5y median of 8.8x [RA] on TTM EBITDA with net debt held near 2.2x [BS,IS]."},
    "bear": {"probability": 0.30, "target_price_12m": 63.55, "basis": "Integration disappoints and the price falls to the fact sheet's bear fair value of 63.55, with the EV/EBITDA method at 44.79-54.46 [fact sheet]. Probability is raised by 0.05 from bull for the small toward-bear macro tilt from rising real yields (research/OMC/2026-10-12-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The stock already trades below its 5y P/FCF minimum and the default anchor (base 147.22 x 0.8 = 117.78) is above the price. What is missing is evidence that the merger creates value per share (ROIC recovery, deleveraging, a synergy target), so a lower price alone would not raise conviction to 4.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Verizon Communications Inc. (VZ) — 2026-10-11
## Bear case
Returns are eroding across the board: ROIC fell from 12.3% to 8.3% TTM, ROE from 29.7% to 15.8%, operating margin from 27.4% to 23.1% [Certain] (RA, IS). Leverage is heavy for a no-growth business, with net debt/EBITDA rising to 3.76x and an Altman Z of 1.22 in the distress zone [Certain] (BS, IS, ST). SpaceX's nationwide low-band spectrum purchase attacks the spectrum-scarcity moat directly; the market treated it as structural, with a sector-wide telecom selloff [Certain] (CNBC and Reuters headlines, OV), and its real commercial impact is unknowable before several quarters of subscriber data [Likely]. The macro overlay tilts moderately to bear: 10y real yields up 0.56pp in 3 months raise refinancing cost and pressure bond-proxy multiples [Certain] (macro overlay). EV/EBITDA of 7.1x is already near its own 5y median, so own-history EV/EBITDA fair value (base 39.85) sits below the price [Certain] (fact sheet Fair value).

## Bull case
Cash generation is intact and improving: TTM FCF margin 15.5%, FCF conversion 133.1%, and a 12.44% FCF yield [Certain] (CF, IS, ST). P/FCF of 8.0x is below its own 5y minimum of 8.5x and 7% below peers [Certain] (RA). The reverse DCF implies an 11.4% year-one revenue decline, far worse than VZ's flat revenue history [Certain] (fact sheet Fair value). A satellite direct-to-device entrant needs years of spectrum, handsets and capacity build-out before it dents postpaid share [Likely] (MarketWatch headline, OV). The selloff has left RSI at 21.8, deeply oversold, with the price back near its 52-week low of 38.39 [Certain] (ST, HI). If Q3 results on Oct 26 show stable postpaid trends, the stock could re-rate toward its pre-shock swing highs of 49.01-51.66 [Guessing] (HI).

## Decision
```json
{
  "ticker": "VZ",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Verizon's 12.44% FCF yield and P/FCF below its 5-year minimum price in a severe revenue decline, but falling returns, 3.76x leverage, a new satellite-spectrum competitor and rising real yields leave the risk-reward balanced rather than compelling.",
  "rationale": "Cheap on FCF, but ROIC, ROE and margins are falling, leverage is high (Altman Z 1.22), and the SpaceX spectrum threat is unresolved until subscriber data arrives. Own-history EV/EBITDA value sits below the price and the macro tilt is bearish. Good but not compelling: conviction 3, AVOID; revisit after Q3 results on Oct 26.",
  "price_at_decision": 41.65,
  "price_date": "2026-10-09",
  "research_note": "research/VZ/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROIC rises back above 9.1% (the FY2025 level), showing returns have stabilised despite the new entrant.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 9.1}},
    {"text": "TTM FCF margin falls below 10%, confirming price competition or a capex step-up is breaking the cash case.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 4.0x, removing balance-sheet flexibility.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 4.0}},
    {"text": "Quarterly releases show persistent postpaid phone net losses, or filings disclose material share loss to satellite/direct-to-device entrants (text-only, checked each release)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 50.0, "basis": "Q3 postpaid trends hold and the SpaceX fear fades, so the price returns toward its pre-shock swing highs of 49.01-51.66 [HI] with P/FCF back above its 5y minimum 8.5x [RA]; the DCF base of 112.45 is disregarded because its growth is inconsistent with VZ's flat revenue history [IS]; probability cut by the overlay's moderate bear tilt (research/VZ/2026-10-11-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 41.0, "basis": "EV/EBITDA holds around its 5y median 7.0x [RA], between the fact sheet's EV/EBITDA base 39.85 and bull 41.55, as FCF margin stays near 15.5% [CF,IS] but falling ROIC caps any re-rating."},
    "bear": {"probability": 0.30, "target_price_12m": 35.0, "basis": "Below the EV/EBITDA bear value of 37.11 [fact sheet Fair value] as the spectrum moat is re-priced and rising real yields lift refinancing costs on 3.76x leverage [BS,IS]; probability raised for the overlay's moderate bear tilt (research/VZ/2026-10-11-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: returns are falling (ROIC 12.3% to 8.3% [RA]) and the SpaceX spectrum threat is unresolved, so a lower price would not lift conviction to 4 on this evidence; the default anchor (DCF-driven base fair value 88.25 less the margin of safety) sits far above the price and is unreliable here. Re-research on Q3 subscriber data.",
  "replaces": null,
  "replacement_reason": null
}
```

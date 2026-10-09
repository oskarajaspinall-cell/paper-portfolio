# Evaluation: Sandisk Corporation (SNDK) — 2026-10-09

## Bear case
SNDK is a commodity NAND producer at what looks like a cycle peak. Operating margin went from +12.5% (FY22) to -21.3% (FY23) to 61.6% TTM, which shows the business has no pricing power of its own [Certain]. TTM gross margin of 71.5% and ROIC of 102.2% sit far above anything in its 5y history [Certain]. Sandisk must fund about half of Flash Ventures' capex and fixed costs whatever demand does, plus fixed Kioxia payments through 2029, so its costs cannot shrink if pricing turns [Certain]. P/B is at the 92nd percentile of its 5y range and EV/EBITDA at the 77th [Certain]. The price implies 14.9% year-1 revenue growth on peak margins [Likely]. The mechanical base fair value of 1,415.29 is 12.1% below the last close [Certain]. Samsung's weak preliminary results are already denting the memory trade [Likely], and real yields are rising (macro overlay) [Likely]. Shares rose 6.9% YoY, diluting holders [Certain].

## Bull case
The AI datacenter build-out keeps demand for enterprise SSDs strong, and memory pricing "remains elevated" with a cycle that could last longer than feared [Guessing]. On current earnings the stock is not expensive: P/FCF of 20.5x is 51% below the peer median, EV/EBITDA of 18.2x is 38% below peers, and the FCF yield is 4.88% [Certain]. The balance sheet holds net cash (net debt/EBITDA -0.36x) and FCF conversion is 100.5% [Certain]. If margins hold through the Oct 29 results, the DCF bull value of 2,126.61 (+32.1%) is reachable [Likely]. The stock is still well above its 200-day average (+37.0%) after a pullback from the 2,354.39 high [Certain]. Short interest is low at 3.89% and falling [Certain].

## Decision
```json
{
  "ticker": "SNDK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "Sandisk is a cyclical NAND commodity producer on peak-cycle margins (71.5% gross, 102% ROIC), priced for continued growth with fixed JV cost commitments, so the reward does not justify the cycle-reversal risk.",
  "rationale": "The probability-weighted 12m value (~1,254) is below the 1,609.46 close. The mechanical base fair value is 12.1% below the price, and the reverse DCF needs 14.9% growth on peak margins. Rising real yields tilt the odds toward bear. This is a good business at the wrong point in the cycle, not a high-conviction buy.",
  "price_at_decision": 1609.46,
  "price_date": "2026-10-08",
  "research_note": "research/SNDK/2026-10-09.md",
  "triggers": [
    {"text": "Gross margin falls below 50%: the NAND up-cycle is reversing (would confirm the avoid; a sustained hold above 70% through FY27 would argue the cycle is structurally longer)", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 50}},
    {"text": "ROIC falls below 30%: returns are normalising toward the cycle average", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 30}},
    {"text": "FCF margin turns negative, as it was in FY2023-FY2025", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Net debt/EBITDA rises back above 1.0x as Flash Ventures capex calls absorb cash", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 2126.61, "basis": "AI-driven NAND pricing holds through Oct 29 results and beyond, and the fact sheet's mechanical bull fair value of 2,126.61 [IS,BS,CF,RA,ST,HI] is reached; the probability is cut by the macro overlay's moderate tilt toward bear (research/SNDK/2026-10-09-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 1415.29, "basis": "Margins ease from the 71.5% gross peak [IS] and the price converges on the fact sheet's blended base fair value of 1,415.29 [IS,BS,CF,RA,ST,HI], which is below the 14.9% year-1 growth the reverse DCF says the current price implies."},
    "bear": {"probability": 0.35, "target_price_12m": 548.48, "basis": "The NAND cycle reverses as in FY23 (operating margin -21.3% [IS]) while fixed Flash Ventures costs stay (10-K, https://www.sec.gov/Archives/edgar/data/2023554/000162828026057406/sndk-20260703.htm), so the value falls to the EV/EBITDA method's base value of 548.48 [RA]; the blended bear of -97.11 is a loss-history artifact, so it is not used, and the probability is raised by the overlay's moderate bear tilt from rising real yields (research/SNDK/2026-10-09-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

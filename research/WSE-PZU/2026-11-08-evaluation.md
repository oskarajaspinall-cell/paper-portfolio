# Evaluation: Powszechny Zaklad Ubezpieczen (WSE:PZU) — 2026-11-08
## Bear case
The re-rating has already happened: P/E 9.7x and P/B 0.9x both sit above their 5y maxima of 9.1x and 0.8x [RA] [Certain]. The **Direction change** matters: TTM ROIC fell from 19.0% to 15.2% over the last 12 months, 4.0pp below its 2-year high [RA-T] [Certain]. The likely driver is the fading hard-market and rate tailwind of FY2022-FY2024 [Guessing], which strikes at a thesis built on ROE holding near 20%. The mechanical bear value of 52.65 is -27.9% below the price, against base upside of only +6.4% [fact sheet Fair value] [Certain]. Governance is noisy: the EGM authorised claims against a former board member and up to PLN 3 billion of subordinated bonds for higher capital needs [OV] [Likely]. Underwriting margins are [data unavailable], so quality cannot be tested [Certain]. Results land Nov 19, 2026 [ST] [Certain].

## Bull case
PZU is Poland's largest insurer, with ROE of 20.3% in FY2025 against 13.0% in FY2021 [RA] [Certain]. Scale and distribution in a concentrated home market are a plausible moat [Likely]. Even after the re-rating it trades 26% below peers on P/E and 50% below on P/B [RA, peers] [Certain]. Leverage has come down: net debt/EBITDA (site definition) is 1.00x against 2.78x in FY2021 [RA] [Certain]. Management reported solvency of 230% and a record dividend in H1 2026 [OV transcript] [Likely], so most of the return comes as cash. Beta of 0.25 [ST] makes it a low-correlation diversifier [Certain]. If ROE holds near the TTM 19.5%, the P/B + ROE method supports 86.13 [fact sheet Fair value] [Likely]. Still, the peer discount reflects Poland and state influence more than mispricing [Likely].

## Decision
```json
{
  "ticker": "WSE:PZU",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, deleveraged Polish insurance franchise whose multiples have re-rated above their own 5-year range while ROIC is falling on a rolling basis, leaving modest base upside against a much deeper mechanical bear case.",
  "rationale": "Quality is real and cash returns are generous, but the price sits above its own 5y P/E and P/B ranges just as TTM ROIC is falling. Base fair value upside is thin and the bear downside is several times larger. Good but not compelling: AVOID at conviction 3, and re-research nearer the entry price or after the Nov 19 results.",
  "price_at_decision": 73.00,
  "price_date": "2026-11-06",
  "research_note": "research/WSE-PZU/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE falls below 15% (19.5% now), showing the FY2023-FY2025 return step-up was cyclical rather than structural.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 12% (15.2% now, 19.0% a year earlier), confirming the rolling decline is a lasting normalisation.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA rises above 2.0x (1.00x site definition now), showing the subordinated-bond refinancing is adding leverage rather than replacing it.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "Shares change YoY rises above +5% (flat now), signalling dilutive capital raising to meet higher capital needs.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 81.84, "basis": "ROE holds near the TTM 19.5% [RA] and the record dividend continues (Q2 2026 transcript [OV]), supporting the mechanical bull fair value of 81.84 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 77.65, "basis": "Returns settle between the TTM ROIC of 15.2% and the FY2025 18.5% [RA, RA-T], giving the mechanical base blend of 77.65 (P/B + ROE 86.13, P/E 60.69) [fact sheet Fair value]; macro is context only (research/WSE-PZU/2026-11-08-macro.md)."},
    "bear": {"probability": 0.25, "target_price_12m": 52.65, "basis": "The ROIC slide from 19.0% to 15.2% [RA-T] continues as the hard-market tailwind fades and P/E reverts toward its 5y median of 8.1x [RA], the mechanical bear fair value of 52.65 [fact sheet Fair value]."}
  },
  "entry_price": 62.12,
  "entry_basis": "valuation file: base 77.65 x 0.8 (20% margin of safety); at that level the same evidence, including the falling ROIC, would offer enough asymmetry for conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

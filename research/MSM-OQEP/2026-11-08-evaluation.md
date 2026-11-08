# Evaluation: OQ Exploration and Production SAOG (MSM:OQEP) — 2026-11-08
## Bear case
The cheapness is relative to peers only. Against its own history the stock is expensive: P/E 10.4x, EV/EBITDA 3.9x and P/FCF 13.2x all sit at or above their 5y maxima [RA] [Certain]. The direction changes work against it. Operating margin fell from 61.8% to 54.3% over the last 12 months and ROCE from 64.2% to 54.4%; FCF margin is 21.1%, well below its 33.2% 2-year high [IS-T, RA-T, CF-T] [Certain]. That pattern fits a softer crude price feeding through, which no official series in the overlay can confirm [Likely]. The TTM ROIC rise to 28.9% does not offset falling margins and cash conversion [Likely]. There is no mechanical fair value and no primary-source read [Certain]. The business sits in one sovereign-linked country, Oman, where no fiscal, royalty or currency-peg check was verified, and institutional ownership is 0.1% (macro overlay) [Guessing]. The peer discount may simply be that risk.
## Bull case
This is a low-cost producer: gross margin 79.7%, operating margin 54.3% and ROIC 28.9% TTM, with net debt/EBITDA only 0.21x [IS, RA] [Certain]. FCF conversion was 95.3% of net income in FY2025 and the FCF yield is 7.55% [CF, ST] [Certain]. It trades well below peers on P/E, EV/EBITDA and P/FCF, though the peer set is loose [Likely]. Beta of 0.33 and RSI of 25.5 after a -17.3% six-month move suggest the selling is overdone, not fundamental [Guessing]. If crude firms, margins could recover toward the 62.1% 2-year high [IS-T] [Guessing]. Still, the upside is a call on the commodity price. It is not a business mispricing we can show from the data.
## Decision
```json
{
  "ticker": "MSM:OQEP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A low-cost, lightly levered Omani upstream producer with high returns, but its margins and cash conversion are falling over the last year, it trades above its own 5-year multiple range, and neither fair value nor country risk can be verified.",
  "rationale": "Quality is real but cyclical and fading on a rolling basis, multiples are above their own history, and fair value is unavailable. The upside depends on crude, which we cannot evidence. Single-country sovereign exposure is unverified. The peer discount does not make it compelling, so no position.",
  "price_at_decision": 0.44,
  "price_date": "2026-11-05",
  "research_note": "research/MSM-OQEP/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 45% (54.3% now, 61.8% a year earlier), showing the margin slide is structural rather than a commodity dip.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 45}},
    {"text": "TTM ROIC falls below 20% (28.9% now), under every fiscal year in the 5-year history.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM FCF margin recovers above 30%, back toward its 33.2% 2-year high, which would show cash conversion re-accelerating and could justify re-research.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 30}},
    {"text": "Net debt/EBITDA rises above 1.0x (0.21x TTM now), showing leverage building to fund payouts or capex.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 0.55, "basis": "Operating margin recovers toward its 62.1% 2-year high [IS-T] and the price returns to its 52-week high of 0.55 [HI], helped by the peer discount on EV/EBITDA narrowing [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 0.44, "basis": "Margins stabilise near the TTM 54.3% [IS-T] and P/E holds near the current 10.4x [RA], so the price is flat. No mechanical fair value exists to reconcile against (fact sheet: no method computable)."},
    "bear": {"probability": 0.3, "target_price_12m": 0.36, "basis": "The rolling margin and ROCE declines continue [IS-T, RA-T] and EV/EBITDA falls back from 3.9x toward its 5y median 3.2x [RA], taking the price back to its 52-week low of 0.36 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: price is not the only obstacle. Margins are falling, fair value cannot be computed and Oman country risk is unverified, so a lower price alone would not make this a BUY.",
  "replaces": null,
  "replacement_reason": null
}
```

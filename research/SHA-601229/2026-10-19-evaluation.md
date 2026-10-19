# Evaluation: Bank of Shanghai Co., Ltd. (SHA:601229) — 2026-10-19
## Bear case
Returns are deteriorating, not cyclically depressed: ROE has fallen every year from 11.1% (FY2021) to 9.1% TTM and net margin from 60.9% to 57.4% [RA, IS] [Certain]. PBOC-driven margin compression and property-exposed loan books are structural headwinds for Chinese regional lenders [Likely]. The "cheapness" is thin: P/E of 6.6x sits above its own 5y max of 6.1x, P/B of 0.5x is at its 5y median, and the stock is not cheap versus peers on P/E [RA] [Certain]. The mechanical fair value (base 13.88) assumes a sustainable ROE that the trend contradicts [Likely]. Piotroski F-score is only 4, shares are creeping up 0.92% a year, dividend data is unavailable, and no company-reported capital ratio is available to check capital strength [ST] [Certain]. Results land on Oct 21, 2026, before any thesis could be tested [Certain].

## Bull case
At 0.5x book, 30% below the peer median P/B of 0.7x, the market already prices a lot of further decline [RA] [Certain]. A 9.1% ROE on half of book is still a high earnings yield, and the price implies -8.8% revenue growth in year 1 [ST, fair value] [Certain]. Both mechanical methods put fair value well above the 9.60 close (bear 12.86) [Likely]. The Shanghai deposit franchise is sticky and net margin, though falling, remains high [Likely]. A policy turn in China that stabilises bank margins could re-rate the sector from a depressed base [Guessing]. The near-zero beta (-0.03) gives diversification [ST] [Likely].

## Decision
```json
{
  "ticker": "SHA:601229",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A sub-book Chinese regional bank whose discount reflects a five-year slide in ROE and net margin rather than a mispricing, with P/E above its own 5-year range and P/B only at its median.",
  "rationale": "There is no catalyst or quality trend to underwrite: ROE and net margin fall every year, P/B sits at its own median and P/E is above its 5y max. The mechanical fair value rests on a sustainable-ROE assumption the trend contradicts. Good-but-not-compelling deep value earns an AVOID; cash is acceptable.",
  "price_at_decision": 9.60,
  "price_date": "2026-10-16",
  "research_note": "research/SHA-601229/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROE (statistics page) rises back above 10%, reversing the five-year decline from 11.1% to 9.1% and showing returns have stabilised.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 10}},
    {"text": "TTM net margin (statistics page) falls below 50%, from 57.4%, confirming credit-cost deterioration and the AVOID.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 50}},
    {"text": "Shares outstanding rise more than 5% year on year (0.92% now), a dilutive capital raise signalling capital stress.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 11.50, "basis": "P/B re-rates to its 5y max of 0.6x [RA] on a China bank-policy turn, still below the mechanical bear 12.86 because the falling ROE trend [RA] argues against the sustainable-ROE assumption."},
    "base": {"probability": 0.5, "target_price_12m": 9.60, "basis": "P/B holds at its 5y median 0.5x [RA] as ROE keeps drifting lower (9.1% TTM) [RA], so book growth roughly offsets de-rating; below the mechanical base 13.88 for the same ROE reason."},
    "bear": {"probability": 0.25, "target_price_12m": 7.70, "basis": "P/B falls to its 5y min 0.4x [RA] as net margin keeps sliding from 57.4% [IS] on NIM compression and property-loan credit costs (note section 2)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the five-year decline in ROE and net margin is; a lower price would not change the decision until returns stabilise (trigger 1).",
  "replaces": null,
  "replacement_reason": null
}
```

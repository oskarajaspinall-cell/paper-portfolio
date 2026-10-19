# Evaluation: Kingnet Network Co., Ltd. (SHE:002517) — 2026-10-19
## Bear case
The share is down 37.5% over 12 months and trails SPY by 52.2pp, and nothing in the research explains why: there are no headlines, no company-reported pipeline or bookings data, and no view of game launches [Certain]. The TTM figures already show slippage: gross margin 77.8% vs 80.8% in FY2025, operating margin 30.9% vs 34.3%, net margin 31.6% vs 35.7% [Certain] (IS). ROCE and ROE have trended down over five years [Certain] (RA), and Piotroski F is only 5 [Certain] (ST). A hit-driven Chinese game publisher can see revenue fall away quickly when a title fades [Likely]. It is "cheap" only against its own history; it trades at a premium to peers on every multiple [Certain] (RA), and shares outstanding grew 2.06% [Certain] (ST). Results on Oct 29, 2026 could confirm a fading title cycle [Guessing]. The mechanical bear value of 8.87 sits far below the price [Certain].
## Bull case
The economics are exceptional: ROIC 39.6% TTM, FCF margin 38.1%, FCF conversion 120.5%, and net cash deepening to -2.52x EBITDA [Certain] (RA, CF, BS). At 15.12 the stock trades at the 1st percentile of its 5y P/E range and 4% of its P/FCF range, with an 8.95% FCF yield [Certain] (RA, ST). The reverse DCF implies only 3.0% year-1 revenue growth, and base fair value is 19.27 [Certain]. If margins hold, cash accumulation alone supports value and a re-rating toward the 5y median P/E of 17.8x is plausible [Likely]. Insiders own 19.30%, aligning management [Certain] (ST). Macro is context only: domestic CNY business, net cash, stable yuan (macro overlay) [Likely].
## Decision
```json
{
  "ticker": "SHE:002517",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 39.6%-ROIC game publisher at the bottom of its own 5-year multiples, but with slipping TTM margins, a peer premium and an unexplained 37.5% derating that the evidence cannot yet resolve.",
  "rationale": "Quality and cash generation are excellent and the price sits near 5y lows, but TTM margins are falling, peers are cheaper, and there is no pipeline or news evidence to explain the derating; results are ten days away. Good but not compelling: conviction 3, AVOID. Re-research after the Oct 29 results.",
  "price_at_decision": 15.12,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-002517/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROIC (statistics) rises back above 45%, showing returns on capital re-accelerating with a new title cycle (39.6% TTM now).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 45}},
    {"text": "TTM gross margin (statistics) recovers above 80%, back to the FY2025 level of 80.8%, showing the TTM slippage was transitory.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 80}},
    {"text": "TTM operating margin (statistics) recovers above 34%, back to the FY2025 level of 34.3%, removing the margin-erosion concern.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 34}},
    {"text": "Company-reported results or filings disclose new title launches or revenue growth that explain and reverse the derating; conversely TTM FCF margin below 20% would confirm the bear case.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 26.71, "basis": "Margins hold and the market re-rates toward the bull fair value 26.71 of the DCF/EV-Revenue blend [IS,BS,CF,RA,ST], with P/E back near its 5y median 17.8x [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 17.0, "basis": "Cash generation (FCF margin 38.1% [CF,IS]) holds while TTM margin slippage persists, so only a partial move toward base fair value 19.27 [fact sheet] and the 5y median P/E 17.8x [RA]."},
    "bear": {"probability": 0.3, "target_price_12m": 8.87, "basis": "The title cycle fades as TTM margins already fall (operating margin 30.9% vs 34.3% FY2025 [IS]), and the price converges on the mechanical bear fair value 8.87 [fact sheet]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: base fair value 19.27 x 0.8 already sits above the 15.12 price. The obstacle is evidence (unexplained derating, falling TTM margins, no pipeline data), so a lower price would not lift conviction; the Oct 29, 2026 results are the re-research point.",
  "replaces": null,
  "replacement_reason": null
}
```

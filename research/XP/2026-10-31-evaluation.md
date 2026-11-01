# Evaluation: XP Inc. (XP) — 2026-10-31
## Bear case
The sell-off is a regime change, not noise. Lula's re-election resets Brazil's fiscal path, Selic and the real; the latest FRED BRL point (5.0410, 2026-10-23) predates the result, so the currency hit to USD-translated BRL earnings is still unmeasured [Certain]. The mechanical fair value (base 21.15) assumes only a 3.0% country premium, below what the market now demands [Likely]. Returns are already eroding: ROE fell from 28.4% to 22.6% and ROIC from 5.6% to 2.8% [Certain]. The 70.9% FCF margin and 33.50% FCF yield are inflated by client-flow items, so the cheapness on cash is illusory [Likely]. Client mix is shifting to daily-liquidity products with lower revenue per real (Q2 call) [Likely]. Short interest rose 18.5% vs the prior month and results land on Nov 16, before any post-election flow data exists [Certain]. A cheap P/E can get cheaper when the discount rate is moving [Guessing].

## Bull case
Earnings are intact: operating margin 30.5% and net margin 28.5% TTM, broadly stable over five years, with Q2 client assets up 17% and net income up 5% [Certain]. At 14.29 the stock trades below its 5y minimum P/E (7.3x vs 8.7x) and P/B (1.5x vs 2.0x), at less than half the peer median P/E of 15.4x [Certain]. The reverse DCF implies -3.5% revenue growth, and even the bear fair value of 17.98 sits above the price [Certain]. Buybacks cut the share count 2.91% YoY and Piotroski F is 6 [Certain]. The stock traded around 19-21 in September before the election spike, so the market has round-tripped beyond the pre-election level, arguably pricing a worse outcome than the political facts justify [Likely]. RSI 27.5 marks capitulation; US credit and volatility are calm (HY 3.26%, VIX 17.2) [Certain].

## Decision
```json
{
  "ticker": "XP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A 30%-operating-margin Brazilian investment platform trades below its own 5-year minimum P/E and P/B after the Lula election shock, but the size of the new Brazil risk premium, the real's move and post-election client flows are not yet measurable.",
  "rationale": "Valuation is compelling on reported earnings, but the obstacle is an unmeasured discount-rate and currency shock with results due Nov 16, plus falling ROE/ROIC and flow-inflated FCF. Good but not compelling: conviction 3, so AVOID; revisit after the results show flows and the BRL/Selic reset is visible.",
  "price_at_decision": 14.29,
  "price_date": "2026-10-30",
  "research_note": "research/XP/2026-10-31.md",
  "triggers": [
    {"text": "TTM operating margin falls below 25%, under every year of the five-year range (low 26.9% in FY2022), showing the post-election flow shift is hitting profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}},
    {"text": "TTM ROE falls below 17%, extending the five-year decline from 28.4% to 22.6% and signalling the franchise's returns are structurally impaired.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 17}},
    {"text": "TTM net margin falls below 22%, under the five-year low of 27.4%, confirming margin compression rather than a translation effect.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 22}},
    {"text": "Quarterly revenue (income statement) declines YoY for two consecutive quarters, or the Nov 16 results show net client inflows turning negative, indicating client-asset outflows are hitting fees."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 24.0, "basis": "Fiscal anchor holds and Nov 16 results show intact flows, so P/E recovers most of the way to its 5y median 12.7x [RA] on TTM earnings [IS], a little under the bull fair value 26.39 to allow for BRL translation (macro overlay macro_bull)."},
    "base": {"probability": 0.4, "target_price_12m": 17.0, "basis": "Margins hold near 30.5% [IS] but the Brazil premium stays elevated, so P/E only returns to its 5y minimum 8.7x [RA]; below the base fair value 21.15 because that model assumes just a 3.0% country premium, which the election result has likely made too low."},
    "bear": {"probability": 0.35, "target_price_12m": 10.0, "basis": "BRL weakens and Selic rises, flows shift further to daily-liquidity products (Q2 call, https://stockanalysis.com/stocks/xp/transcripts/673737-q2-2026/) and the multiple compresses further on lower USD earnings; probability raised from 0.30 by the overlay's small toward-bear macro_tilt (research/XP/2026-10-31-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: base fair value less the 20% margin of safety is already above the price. The obstacle is the unmeasured post-election BRL/Selic reset and the Nov 16 client-flow data; a lower price would not change the decision until those are known.",
  "replaces": null,
  "replacement_reason": null
}
```

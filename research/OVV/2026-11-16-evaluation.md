# Evaluation: Ovintiv Inc. (OVV) — 2026-11-16
## Bear case
OVV is a commodity price-taker with no moat beyond cost and inventory [Likely]. The TTM rebound (ROIC 19.6% from 9.7% a year earlier; operating margin 31.4%) mostly reflects higher oil and condensate prices, not structural change [Likely]. The 5-year fiscal trend in ROIC, ROCE and FCF margin is still down, so the direction change may be just the cycle turning up [Likely]. On earnings the stock is not cheap: P/E 13.4x is above its own 5y max of 9.4x, P/FCF 9.9x sits near its 5y max, and the mechanical base fair value of 60.09 is below the 65.39 close [Certain]. After a +71.0% 12-month run, an extended price risks a de-rating if commodity prices or growth slow [Likely]. Deals are heavy: NuVista, the Anadarko sale and Logan, which needs Alberta court and Competition Act approval. Shares rose 3.80% YoY; higher Canadian royalties cut Q3 oil output [Certain].

## Bull case
Balance sheet and cash generation are the strongest in five years: net debt/EBITDA 0.91x, FCF yield 10.09%, FCF conversion 134.1% TTM and Piotroski F of 8 [Certain]. The FY2025 FCF margin of -11.9% was a temporary trough; it is 17.6% TTM [Certain], with the FY2025 figure plausibly depressed by acquisition-related spending [Guessing]. EV/EBITDA of 4.2x sits in the lower half of its 5y range and 24% below the peer median of 5.5x [Certain]. Leverage was 0.7x at Q3 while Montney inventory was added, and 50%–100% of cash flow above capex goes back to shareholders [company-reported] (https://www.sec.gov/Archives/edgar/data/1792580/000119312526445603/ovv-20260930.htm) [Likely]. The trend is healthy: price is above the 200-day average (+11.3%), not overextended, and relative strength vs SPY is positive on 3, 6 and 12 months [Certain].

## Decision
```json
{
  "ticker": "OVV",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Over the last 1 and 3 years ROIC, operating margin and FCF margin are all rising (RA-T, IS-T, CF-T); the 5y fiscal decline reflects the FY2022 commodity peak and the FY2025 acquisition-year FCF trough.",
    "moat": "none",
    "key_risk": "medium",
    "key_risk_text": "Commodity price reversal: TTM returns ride high oil and condensate prices, and with P/E above its 5y max a price fall would de-rate an extended share price.",
    "veto": null
  },
  "thesis": "A low-leverage, high-FCF Permian/Montney producer at a cyclical earnings high, priced fairly on EBITDA but rich on earnings versus its own history.",
  "rationale": "Strong balance sheet and FCF, but returns are commodity-driven with no moat, the price sits above the mechanical base fair value, and P/E is above its 5y range. Good but not compelling: AVOID, with an entry price at the discounted base fair value.",
  "price_at_decision": 65.39,
  "price_date": "2026-11-13",
  "research_note": "research/OVV/2026-11-16.md",
  "triggers": [
    {"text": "ROIC (TTM) falls below 10%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 2.0x, e.g. from debt-funded M&A", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "FCF margin (TTM) falls below 5%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}},
    {"text": "Shares change YoY rises above 5% (continued dilution)", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 73.61, "basis": "TTM margins hold and the price revisits its 52-week high of 73.61 [HI] as EV/EBITDA stays below the peer median of 5.5x [RA]; above the mechanical bull of 61.51 because trend and FCF yield carry it."},
    "base": {"probability": 0.5, "target_price_12m": 60.09, "basis": "EV/EBITDA settles near its 5y median of 4.0x [RA], the mechanical base fair value of 60.09 [fact sheet Fair value], as commodity-driven earnings normalise."},
    "bear": {"probability": 0.25, "target_price_12m": 49.54, "basis": "Commodity prices fall and the P/E above its 5y max de-rates; mechanical bear fair value 49.54 [fact sheet Fair value]."}
  },
  "entry_price": 48.07,
  "entry_basis": "valuation file: base 60.09 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

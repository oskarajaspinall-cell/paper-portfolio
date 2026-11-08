# Evaluation: Essent Group Ltd. (ESNT) — 2026-11-08
## Bear case
Returns are fading, not compounding: ROE fell from 16.8% (FY2021) to 12.0% TTM and ROIC from 15.5% to 11.6% [RA] [Certain]. The rolling 12 months are flat (ROIC 11.6% vs 11.8% [RA-T]), so the slide has paused rather than reversed [Certain]. The main risk is policy. A late-October executive order directs the FHFA to consider a pilot that cancels private mortgage insurance on future loans, and the company says it will evaluate the pilot once terms are final (10-Q, https://www.sec.gov/Archives/edgar/data/1448893/000144889326000032/esnt-20260930.htm) [Certain]. That would hit new insurance written, and a lower price does not resolve it [Likely]. Q3 EPS missed on a revenue beat and defaults rose to 2.75% (transcript headline [OV]) [Likely]. P/E 8.7x sits at 90% of its 5y range [RA], and the P/E fair-value leg (base 57.89) is below the price [Certain]. Short interest rose 33.1% in a month [ST] [Certain].
## Bull case
On book and cash flow it is cheap. P/B 1.0x is 11% below peers, P/FCF 6.5x is below its 5y minimum and the FCF yield is 15.29% [RA,ST] [Certain]. Leverage is low (net debt/EBITDA 0.58x) and FCF conversion is 125.5% [CF,IS] [Certain]. Shares are down 9.10% YoY on buybacks, and a new $500M authorization was reported (transcript headline [OV]) [Likely]. Buying back stock at about book value while ROE is near 12% adds value per share [Likely]. Persistency of 83.3% and high rates support the in-force book and investment income (10-Q) [Likely]. The mechanical base fair value of 98.66 is well above the 63.41 close [Certain], but 67% of that weight sits on the P/B+ROE leg, and that leg assumes a sustainable ROE the falling trend does not yet support [Guessing].

## Decision
```json
{
  "ticker": "ESNT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-leverage, buyback-heavy US mortgage insurer trades near book value with a 15.29% FCF yield, but falling returns, rising defaults and an unresolved FHFA proposal to cancel mortgage insurance on future loans leave the skew balanced rather than compelling.",
  "rationale": "It is cheap on book and cash flow, but returns are drifting lower, the P/E leg of fair value sits below the price and the FHFA cancellation pilot is an open binary policy risk. Good but not compelling: AVOID at conviction 3, and revisit once the pilot's terms are known.",
  "price_at_decision": 63.41,
  "price_date": "2026-11-06",
  "research_note": "research/ESNT/2026-11-08.md",
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The default anchor (base 98.66 x 0.8) sits above the current price, and what blocks a BUY is the unresolved FHFA pilot to cancel private mortgage insurance on future loans (10-Q), so a lower price would not change the decision before its terms are known.",
  "triggers": [
    {"text": "TTM ROE falls below 10% (12.0% now), showing the falling returns trend is structural credit or pricing erosion.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 1.0x (0.39x site definition now), showing capital returns or losses are straining the balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}},
    {"text": "Share count stops shrinking (shares change YoY above 0%, -9.10% now), removing the buyback pillar of the thesis.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "FHFA finalises or launches a pilot cancelling private mortgage insurance on future GSE loans, or drops the proposal, as disclosed in a company filing or release (either outcome prompts a re-research)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 76.0, "basis": "The FHFA pilot stalls, buybacks continue and P/B returns to its 5y max of 1.2x [RA], reaching about the mechanical bear fair value of 75.74 and staying below the base because the P/B+ROE leg assumes a sustainable ROE above the falling trend [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 70.0, "basis": "ROE holds near 12.0% [RA], returns stay flat over 12 months [RA-T] and P/B moves back to its 5y median of 1.1x [RA]; this is below the mechanical base of 98.66 because the P/E leg (base 57.89) is under the price and P/E is already at 90% of its 5y range [RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 55.0, "basis": "The FHFA pilot advances (10-Q, https://www.sec.gov/Archives/edgar/data/1448893/000144889326000032/esnt-20260930.htm) and defaults keep rising from 2.75% (Q3 transcript [OV]), so P/B falls to its 5y min of 0.9x [RA] and toward the P/E leg's base of 57.89, near the 52-week low of 55.34 [HI]."}
  }
}
```

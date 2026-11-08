# Evaluation: Commerce Bancshares, Inc. (CBSH) — 2026-11-08
## Bear case
Profitability is drifting down: ROE fell from 17.8% (FY2023) to 15.1% TTM and net margin is 31.4% TTM, a falling 5y trend [Certain] [RA, IS]. The FineMark deal lifted average loans 18.2% but loan rates fell 31bp and nine-month diluted EPS grew only 3.6% against 7.2% net income growth: growth is partly bought with dilution, shares up 2.13% YoY [company-reported] (https://www.sec.gov/Archives/edgar/data/22356/000002235626000213/cbsh-20260930.htm) [Certain]. The fact sheet's Direction change (FCF margin 29.6% -> 65.8%) is driven by bank balance-sheet cash flows, not distributable earnings, so it neither supports nor threatens the thesis [Likely]. P/B 1.9x is 29% above the peer median 1.4x and P/E 13.3x is in line with peers, so there is no relative discount [Certain]. Macro tilts small toward bear: HY spreads +0.77pp in 3 months and VIX 28.18 raise provision and de-rating risk (macro overlay) [Likely]. Book value per share fell quarter on quarter (headline) [Likely].
## Bull case
A granular, low-cost deposit franchise and large trust/wealth arm sustain an above-peer ROE of 15.1% that still earns a book premium [Likely]. P/E 13.3x sits at the 6th percentile of its 5y range and P/B 1.9x at its 5y minimum [Certain] [RA]. The mechanical base fair value of 67.93 is +23.4% above the 55.04 close, and the reverse DCF implies -2.4% year-1 revenue growth, undemanding for a bank that just grew net interest income 10.5% via acquisition [Certain]/[company-reported]. Q3 EPS rose to $1.08 from $1.01 (Business Wire headline) and the buyback was reauthorised on 3 November, which could start to offset deal dilution [Likely]. Fee-income M&A (Nolan & Associates) diversifies away from rate sensitivity [Guessing]. Falling long yields help securities marks (macro overlay) [Likely].
## Decision
```json
{
  "ticker": "CBSH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, low-cost-deposit regional bank at the bottom of its own multiple range, but with slipping ROE, dilution-aided growth and no discount to peers, it is fairly priced to modestly cheap rather than compelling.",
  "rationale": "The new quarter confirmed the pattern: net income up, per-share growth lagging, ROE drifting lower, loan yields falling. Upside to base fair value rests on a P/B+ROE method fed by a declining ROE, and macro tilts slightly bearish. Good but not compelling; conviction stays 3, no position.",
  "price_at_decision": 55.04,
  "price_date": "2026-11-06",
  "research_note": "research/CBSH/2026-11-08.md",
  "triggers": [
    {"text": "ROE (TTM) falls below 12% (15.1% now): the deposit franchise no longer earns its book premium", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "Net (profit) margin TTM falls below 28% (31.4% now)", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 28}},
    {"text": "Shares outstanding growth YoY stays above 3% (2.13% now): dilution outrunning earnings growth", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}},
    {"text": "Company-reported efficiency ratio rises above 63% (58.34% for nine months to September 2026, 10-Q)"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 67.93, "basis": "P/B re-rates from its 5y minimum 1.9x toward the 2.4x median [RA] as ROE holds near 15.1% and buybacks offset dilution, reaching the mechanical base fair value of 67.93 (fact sheet); held below the 73.22 bull because ROE is slipping."},
    "base": {"probability": 0.45, "target_price_12m": 61.12, "basis": "ROE keeps drifting from 15.1% [RA] while FineMark-driven net interest income growth is diluted per share (10-Q, company-reported), so the stock re-rates only to the mechanical bear fair value of 61.12; below the 67.93 base because that P/B+ROE method assumes a sustainable ROE the trend does not yet confirm."},
    "bear": {"probability": 0.30, "target_price_12m": 49.62, "basis": "Macro overlay tilt small toward bear (HY spread +0.77pp 3m, VIX 28.18) raises provisions and squeezes NIM on falling loan yields, pushing P/B below its 1.9x 5y minimum [RA] and the price back to its 6-month low of 49.62 [HI]; below the 61.12 mechanical bear, which assumes no credit cycle."}
  },
  "entry_price": 54.34,
  "entry_basis": "valuation file: base 67.93 x 0.8; at that price the 20% margin of safety would compensate for the slipping ROE and dilution and justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

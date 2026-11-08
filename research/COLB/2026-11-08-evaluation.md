# Evaluation: Columbia Banking System, Inc. (COLB) — 2026-11-08
## Bear case
ROE fell from 15.4% (FY2021) to 8.5% (FY2025) [RA]; the 11.2% TTM rebound is one merger-boosted year, not a proven level [Likely]. Not cheap on book: P/B 1.2x sits above its 1.1x 5y median and the peer median [RA] [Certain]. The base fair value of 42.94 leans on an FCFE DCF (63.66) built on bank cash flows; the industry's best method, P/B + ROE, gives only 32.57, close to the 30.48 close [Certain]. The **Direction change** (FCF margin up from 35.2% to 52.5% over the last year against a falling 5y trend [CF-T]) comes from balance-sheet flows such as loan runoff, so it does not support the thesis; loans are shrinking and growth stays subdued into H1 2027 (Boston conference transcript) [Likely]. Shares rose 33.02% YoY [ST], Piotroski F is 4, and the macro overlay tilts small toward bear on wider spreads and VIX 28.18 [Likely].

## Bull case
The Pacific Premier integration is done: integration-risk language left the 10-Q and NIM rose to 4.11% from 3.93% as customer deposits replaced wholesale funding [company-reported] (https://www.sec.gov/Archives/edgar/data/887343/000088734326000188/colb-20260930.htm) [Likely]. Q3 operating EPS of $0.82 beat (fact-sheet headline), guidance points to a low-4% NIM and continued buybacks (Q3 transcript) [Likely]. P/E of 10.6x sits at the 11% point of its 5y range, below the 11.5x median [RA] [Certain], and the reverse DCF implies -7.5% year-1 revenue growth, a shrinkage the improving margin does not show [Likely]. Beta is 0.68, the curve is positive at +0.38pp (macro overlay), and Bank Director ranked it the top-performing large US bank [Likely]. If ROE holds near TTM 11.2% and the multiple re-rates, the P/B + ROE bull of 41.94 is reachable [Guessing].

## Decision
```json
{
  "ticker": "COLB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A post-merger western regional bank with a recovering NIM and buybacks, but a five-year falling ROE, shrinking loans and a P/B above its own median leave the best-method fair value close to the price.",
  "rationale": "Integration and NIM recovery are real, but the credible value (P/B + ROE base 32.57) sits only modestly above the close; the larger headline base relies on bank FCFE. ROE has not proven its rebound, loans are shrinking and the macro tilt is toward bear. Good, not compelling: AVOID, with an entry price at the mechanical bear value.",
  "price_at_decision": 30.48,
  "price_date": "2026-11-06",
  "research_note": "research/COLB/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE rises above 12.9% (the FY2022 level), showing the post-merger return recovery is durable rather than a one-year rebound.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 12.9}},
    {"text": "TTM ROE falls below 9%, confirming the five-year decline and removing any case at this price.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 9}},
    {"text": "Net interest margin (10-Q MD&A) holds at 4.11% or above for two more quarters while total loans and leases return to growth, showing the deposit franchise can grow, not just reprice."},
    {"text": "Net interest margin (10-Q MD&A, tax-equivalent) falls below 3.70%, showing deposit competition is reversing the funding-mix gains."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 41.94, "basis": "ROE holds near the 11.2% TTM [RA] as NIM stays low-4% (Q3 transcript) and buybacks continue, reaching the P/B + ROE bull fair value of 41.94 [fact sheet Fair value]; below the blended bull of 62.58 because that leans on FCFE built on bank balance-sheet flows."},
    "base": {"probability": 0.5, "target_price_12m": 32.57, "basis": "Subdued loan growth into H1 2027 (Boston conference transcript) keeps ROE near TTM and P/B near its 1.1x-1.2x range [RA]: the P/B + ROE base of 32.57, the industry's best method, rather than the blended 42.94 inflated by FCFE DCF 63.66 [fact sheet Fair value]."},
    "bear": {"probability": 0.3, "target_price_12m": 24.2, "basis": "Wider spreads lift CRE and commercial credit costs and ROE slides back toward the FY2025 8.5% [RA]: the P/B + ROE bear of 24.20 [fact sheet Fair value]; probability raised from 0.25 for the macro overlay's small toward-bear tilt (research/COLB/2026-11-08-macro.md)."}
  },
  "entry_price": 26.77,
  "entry_basis": "The valuation file's default (base 42.94 x 0.8) is above the price because the base leans on bank FCFE; anchored instead at the mechanical bear fair value of 26.77 [fact sheet Fair value], where the best-method P/B + ROE base of 32.57 would offer a real margin of safety.",
  "replaces": null,
  "replacement_reason": null
}
```

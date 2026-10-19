# Evaluation: International Consolidated Airlines Group (LON:IAG) — 2026-10-19
## Bear case
Airlines are capital-intensive, cyclical price-takers on fuel and labour [Likely]. The TTM figures are near a cyclical peak: operating margin 15.0% and ROIC 27.5% compare with -34.8% and -24.6% in FY2021 [Certain] [RA, IS]. Q2 profit fell 16% on fuel costs and Middle East disruption (https://www.reuters.com/world/uk/british-airways-owner-iag-misses-second-quarter-profit-view-2026-07-31/) [Certain], and crude has kept rising (fact-sheet news, 2026-10-08) [Likely]. The macro overlay flags a stronger dollar (DTWEXBGS +3.72 over ~1m) lifting USD fuel and lease costs [Likely]. Piotroski F is only 4 [Certain] [ST]. The mechanical fair value is unusable: the through-cycle DCF bear value is negative and its base is far above the price, so it cannot anchor anything; the EV/EBITDA method (399.53–463.76 GBX) brackets the price closely [Certain]. Beta 1.36 [ST]. The shares are below the 50-day average with -9.3pp 3m relative strength [Certain] [HI].
## Bull case
The balance sheet has been rebuilt: net debt/EBITDA fell from 4.74x (FY2022) to 0.74x TTM [Certain] [RA]. Cash generation is strong: FCF margin 11.8%, FCF conversion 128.6%, an 18.64% FCF yield [Certain] [CF, ST]. That cash is going back to shareholders: shares fell 8.59% YoY and a final buyback programme completes the return of excess cash (https://www.nasdaq.com/articles/iag-launches-final-eu500-mln-share-buyback-program) [Certain]. EV/EBITDA of 3.5x is below its own 5y minimum of 4.4x and below peers' 3.9x; P/FCF of 5.4x compares with a peer median of 11.8x [Certain] [RA]. Heathrow slots, BA's premium long-haul brand and IAG Loyalty give it better economics than most airlines [Likely]. The reverse DCF implies -23.7% year-1 revenue growth, a far worse outcome than anything the current results point to [Certain]. Q3 results on Nov 6, 2026 could re-rate the stock if margins hold [Guessing].
## Decision
```json
{
  "ticker": "LON:IAG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraged, cash-generative premium airline trades below its own 5-year minimum EV/EBITDA at an 18.64% FCF yield, but peak-cycle margins, rising fuel and dollar costs and an unusable mechanical fair value leave the skew only modestly favourable.",
  "rationale": "Cheap and improving, but airline returns are cyclical, fuel and dollar headwinds are building, Piotroski F is weak, and the only credible valuation anchor (EV/EBITDA) sits close to the price. Good but not compelling: conviction 3, so AVOID. Re-research at the EV/EBITDA bear value or after Q3 results.",
  "price_at_decision": 414.80,
  "price_date": "2026-10-16",
  "research_note": "research/LON-IAG/2026-10-19.md",
  "triggers": [
    {"text": "TTM operating margin falls below 10%, giving up the post-COVID margin recovery (15.0% TTM).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 2.0x (0.74x TTM), reversing the deleveraging that funds the buybacks.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "TTM FCF margin falls below 5% (11.8% TTM), so cash generation no longer supports capital returns.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 5}},
    {"text": "TTM ROIC falls below 15% (27.5% TTM), showing returns reverting to the industry's poor norm.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 492.90, "basis": "Margins hold through Q3 and buybacks continue, so EV/EBITDA moves back toward its 5y median of 4.8x [RA] and the price regains its 6-month high [HI]; the through-cycle DCF bull is ignored because its negative bear value shows the model is unstable here."},
    "base": {"probability": 0.45, "target_price_12m": 444.28, "basis": "Fuel costs offset part of the premium-demand strength, so the stock trades at the EV/EBITDA method's base value [fact-sheet fair value], well below the blended base of 2,106.83, which rests on the unreliable through-cycle DCF."},
    "bear": {"probability": 0.30, "target_price_12m": 332.70, "basis": "Crude and the dollar keep rising (macro overlay 2026-10-19: small tilt toward bear, which raised this probability) and margins compress from peak, returning the shares to their 52-week low [HI]."}
  },
  "entry_price": 399.53,
  "entry_basis": "Base fair value x 0.8 is not usable (the blended base rests on an unstable DCF and is far above the price). Anchor instead on the EV/EBITDA method's bear value of 399.53 GBX (valuation file; fact-sheet fair value [IS,BS,CF,RA,ST]), where the only credible method's whole range sits above the price, provided margins hold at Q3.",
  "replaces": null,
  "replacement_reason": null
}
```

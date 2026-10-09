# Evaluation: Kenvue Inc. (KVUE) — 2026-10-09
## Bear case
KVUE is no longer a standalone 12-month equity: it is the target of a pending Kimberly-Clark acquisition (0.14625 KMB shares + $3.50 cash per share) [Certain] (https://www.sec.gov/Archives/edgar/data/1944048/000110465925105216/tm2529895d1_8k.htm). The upside is capped by the consideration, and a core fundamentals thesis cannot earn it. The downside is open: EU remedies were still being offered on 2026-09-23 [Certain] (https://www.reuters.com/legal/transactional/kimberly-clark-offers-remedies-bid-eu-approval-kenvue-deal-2026-09-23/), and a break would leave a standalone business with operating margin down 2.5pp and net margin down 4.1pp over 5y [Certain] (IS), net debt/EBITDA up from net cash to 2.16x [Certain] (BS,IS) and a Tylenol litigation tail [Guessing]. The base fair value of $16.78 sits below the $17.73 close, so there is no margin of safety [Certain] (fact sheet). The 10y yield at 5.28% raises arb carry cost [Likely] (macro overlay).

## Bull case
On a standalone basis the stock is cheap. P/E is 20.8x against a 5y minimum of 22.4x and a peer median of 26.9x, and EV/EBITDA is 11.9x against a minimum of 12.6x [Certain] (RA, peers). Quality is sound: ROIC is 12.3% TTM, gross margin is rising to 58.4%, FCF conversion is 115.4% and Piotroski F is 8 [Certain] (RA,IS,CF,ST). If the deal closes, holders get KMB stock plus cash. Australia has already cleared it with divestments [Certain] (https://www.reuters.com/legal/litigation/australia-clears-kimberly-clarks-acquisition-kenvue-requires-carefree-stayfree-2026-09-02/), and KMB has started exchange offers for Kenvue notes and named post-close leadership, which signals intent to complete [Likely] (fact-sheet headlines). Beta of 0.45 limits market drawdowns [Certain] (ST). Even so, the edge is a deal spread that the fact sheet cannot measure, not a thesis this portfolio can underwrite [Likely].

## Decision
```json
{
  "ticker": "KVUE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "KVUE is a pending Kimberly-Clark merger-arbitrage target whose returns depend on EU antitrust clearance and KMB's share price, not on Kenvue's fundamentals, so no core fundamentals thesis applies.",
  "rationale": "The fixed stock-plus-cash consideration caps upside, while an EU block would expose a standalone business with falling operating and net margins and higher leverage. Base fair value of $16.78 is below the $17.73 close. The spread cannot be measured from stockanalysis.com data. This is not a high-conviction core idea, so no position.",
  "price_at_decision": 17.73,
  "price_date": "2026-10-08",
  "research_note": "research/KVUE/2026-10-09.md",
  "triggers": [
    {"text": "The Kimberly-Clark merger agreement is terminated (EU block or walk-away, per SEC 8-K), making Kenvue a standalone equity again that needs a fresh core assessment."},
    {"text": "TTM gross margin falls below 56%, back in the FY2021-23 range, signalling eroding brand pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 56}},
    {"text": "TTM FCF margin falls below 8%, under the FY2024 trough of 8.6%, showing cash generation is deteriorating.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "TTM ROIC falls below 10%, under the 5y range of 10.2%-12.3%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 20.13, "basis": "The deal closes and the KMB stock leg recovers, taking KVUE back to its 52-week high of 20.13 [HI]; upside is capped by the fixed consideration, so this sits below the 24.75 bull fair value."},
    "base": {"probability": 0.55, "target_price_12m": 17.73, "basis": "The EU clears the deal with remedies and KVUE tracks the consideration near today's 17.73 close [HI], close to the 16.78 base fair value; the macro overlay (research/KVUE/2026-10-09-macro.md) tilts neutral/small, with the 5.28% 10y yield keeping the arb spread from narrowing, so probabilities are unchanged."},
    "bear": {"probability": 0.20, "target_price_12m": 14.02, "basis": "The EU blocks the deal (remedies still pending per https://www.reuters.com/legal/transactional/kimberly-clark-offers-remedies-bid-eu-approval-kenvue-deal-2026-09-23/) and KVUE reverts to standalone value at its 52-week low of 14.02 [HI]; this is above the 3.20 bear fair value, whose -4.72 DCF leg reflects the mechanical model, not a realistic floor for a business with a 12.4% FCF margin [CF,IS]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: KVUE's value is set by the pending Kimberly-Clark consideration and EU clearance, so a lower price would not create a fundamentals BUY; re-research only if the merger is terminated.",
  "replaces": null,
  "replacement_reason": null
}
```

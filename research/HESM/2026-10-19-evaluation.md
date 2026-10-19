# Evaluation: Hess Midstream LP (HESM) — 2026-10-19
## Bear case
The 2026-10-06 Chevron restructuring changes the business: near-term earnings fall in exchange for longer contracts and a second basin, and the terms are not yet in a primary filing [Likely]. HESM still relies on one customer, and that customer's Bakken drilling was already slowing, with Q2 2026 oil terminaling throughput down 15% y/y [company-reported] (https://www.sec.gov/Archives/edgar/data/1789832/000119312526338055/hesm-20260630.htm). The headline "cheapness" rests on pre-deal history. EV/EBITDA (8.2x) and P/FCF (7.5x) already sit above HESM's own 5y maxima, and the reverse DCF prices a -19.3% revenue year, which matches the guided step-down rather than signalling mispricing [Likely]. Leverage of 3.00x net debt/EBITDA is rising, and revolver-funded buybacks become heavier on a smaller EBITDA base [Likely]. Shares outstanding rose 20.44% y/y, and short interest rose 19.1% in a month [Certain]. Macro adds a small bear tilt through real yields and credit spreads (2026-10-19-macro.md) [Likely].

## Bull case
This is fee-based infrastructure with 77.5% gross margin, 62.1% operating margin, ROCE of 24.7% (rising) and a Piotroski F of 8 [Certain]. At 30.66 it trades at a 10.6x P/E, below its 5y minimum of 12.7x and below the peer median of 13.3x, with a 13.25% FCF yield [Certain]. The deal extends contracts, lowers the unit count and adds a second basin, which reduces the single-basin risk that capped the multiple [Likely] (Barron's, as listed in the fact sheet). RSI of 22.1 and a close near the 52-week low of 29.85 suggest forced selling after a 15.6% one-day fall [Likely]. If a filing confirms that minimum-volume protection survives, the equity could re-rate towards the peer EV/EBITDA median of 11.0x [Guessing].

## Decision
```json
{
  "ticker": "HESM",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-margin, fee-based Bakken midstream franchise trades at a P/E below its 5y minimum, but Chevron's restructuring resets near-term earnings on terms not yet confirmed in a primary filing, so the apparent discount is largely the guided step-down.",
  "rationale": "Quality is real, but the earnings base is being reset by a single-customer deal whose terms are unverified. Own-history fair value predates the deal and overstates upside. EV/EBITDA and P/FCF already exceed their 5y maxima. Leverage is rising and the macro tilt is small bear. Good but not compelling: AVOID until the post-deal economics are filed.",
  "price_at_decision": 30.66,
  "price_date": "2026-10-16",
  "research_note": "research/HESM/2026-10-19.md",
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the post-restructuring contract terms and EBITDA base are unconfirmed in a primary filing, and the mechanical fair value (base 106.97) rests on pre-deal history, so a lower price would not change the decision until the 10-Q/8-K detailing the Chevron deal is filed.",
  "triggers": [
    {"text": "A primary SEC filing (8-K/10-Q) confirms the restructured Bakken/DJ Basin contracts keep minimum-volume protection and extended tenor, making post-deal EBITDA visible and contracted."},
    {"text": "TTM ROIC falls below 18% (20.7% TTM), showing the new structure dilutes returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 18}},
    {"text": "Net debt/EBITDA rises above 3.5x (3.00x TTM) as EBITDA steps down, turning debt-funded buybacks into balance-sheet risk.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}},
    {"text": "TTM FCF margin falls below 40% (51.9% TTM, already falling), showing cash conversion is breaking down.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 40}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 39.0, "basis": "Filed deal terms confirm contracted cash flow, so the price returns to its pre-deal trading range (swing lows 38.57-39.51 [HI]), still far below the mechanical base fair value of 106.97, which rests on pre-deal history."},
    "base": {"probability": 0.45, "target_price_12m": 31.0, "basis": "The price already discounts the guided step-down (reverse DCF -19.3% year-1 revenue [fact sheet]), so the 10.6x P/E [RA] holds broadly flat; the target sits well below the mechanical bear of 73.56 because that range uses pre-deal EBITDA."},
    "bear": {"probability": 0.35, "target_price_12m": 24.0, "basis": "A smaller EBITDA base lifts leverage above 3.00x [RA] while Chevron Bakken volumes keep falling (oil terminaling -15% y/y [company-reported], 10-Q), and the macro overlay's small bear tilt from rising real yields and spreads (2026-10-19-macro.md) adds probability to this case."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

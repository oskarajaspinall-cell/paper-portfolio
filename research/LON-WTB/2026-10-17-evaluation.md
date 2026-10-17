# Evaluation: Whitbread plc (LON:WTB) — 2026-10-17
## Bear case
This is not a post-earnings drift. The 2026-10-06 jump (+5.2% on 2.4x volume) came a week *before* the H1 results of 2026-10-13, so the catalyst was most likely the Corvex activist news, not a results beat [Likely]. The results themselves were in-line: stockanalysis.com's transcript summary describes only marginal revenue and EBITDAR growth against inflation, plus management complaining about business rates and National Insurance [Likely]. With the board rejecting Corvex's seat demand on 2026-10-16, the activist premium may now unwind instead of building [Guessing]. The entry is stretched: RSI 68.7, price +7.7% above the 50-day MA and at its 6-month high of 2,622, while the 50-day still sits below the 200-day (-1.7%), so there is no confirmed uptrend [Certain]. Fundamentals are weakening: TTM net margin is 2.0%, FCF margin 4.1% and net debt/EBITDA 6.55x [Certain].

## Bull case
The stock is cheap on cash earnings: EV/EBITDA of 9.4x is below its 5y minimum of 11.4x and well under the 15.8x peer median [Certain]. An activist pushing for change around the Premier Inn estate could keep a bid under the shares, and the H1 call said UK trading was strong and Germany is on track for profitability [Likely]. Shares outstanding fell 4.23% YoY, so buybacks support per-share value [Certain]. The price held above the reaction day through the results, and the 52-week high of 3,175 sits above the minimum 2:1 target, leaving room overhead [Certain]. Even so, the edge rests on activist news-flow, not on the earnings surprise this setup is meant to trade [Guessing].

## Decision
```json
{
  "ticker": "LON:WTB",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "The flagged drift was driven by activist news ahead of in-line H1 results rather than an earnings beat, so the setup lacks the edge the post-earnings drift rule requires.",
  "rationale": "The reaction day came before the results, and the results showed only marginal growth, so there is no results beat for the price to digest. The entry is overbought at a 6-month high, the 50-day is below the 200-day, and the activist catalyst is binary. A 2:1 plan exists on paper, but its edge is unclear. Cash is preferred.",
  "price_at_decision": 2611.0,
  "price_date": "2026-10-16",
  "research_note": "research/LON-WTB/2026-10-17.md",
  "exit_plan": {"target": 2973.0, "stop": 2430.0, "time_limit": "2026-12-11"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 3175.0, "basis": "Activist pressure and property recycling re-rate EV/EBITDA from 9.4x back toward its 5y minimum of 11.4x [RA], returning the price to its 52-week high of 3,175 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 2611.0, "basis": "In-line H1 trading (OV transcript) and a stable but leveraged balance sheet (net debt/EBITDA 6.55x [BS,IS]) leave the price around today's close; the mechanical fair value is [data unavailable], so this rests on the multiples alone."},
    "bear": {"probability": 0.30, "target_price_12m": 2098.0, "basis": "The activist premium unwinds after the board's rejection (OV news) and FCF margin stays near 4.1% [CF,IS], sending the price back to its 52-week low of 2,098 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Varonis Systems, Inc. (VRNS) — 2026-11-15
## Bear case
This is not a pullback in an uptrend. It is a stock pinned by a pending cash takeover by Proofpoint, a Thoma Bravo portfolio company [Certain] (https://www.tipranks.com/news/proofpoint-to-buy-varonis-vrns-for-6-3-billion-in-ai-security-push). The ATR is only 0.4% of price and there was no earnings reaction in the last 10 sessions, so the screen's signal reflects the deal, not a trend [Likely]. Upside is capped near the deal price. The target of 50.01 needs a break through the 50.31 high that a fixed cash bid should not allow [Likely]. A deal break would gap the price through the 48.40 stop towards the mechanical bear value of 31.79, so the stop does not cap the loss [Likely]. Standalone, the fundamentals are weak: operating margin -22.5%, ROCE down 3.7pp over 12 months, and FCF margin down from 22.0% to 16.5% [Certain]. Shareholder investigations were announced [Likely]. Deal terms are unverified [Guessing].

## Bull case
Deals with a private-equity-backed buyer and a cash price usually close [Guessing]. While the deal is pending, the price drifts toward the offer, and volatility is low [Likely]. FCF margin is still positive at 16.5% and the 5-year trend is rising [Certain]. The Q3 results beat on adjusted EPS [Likely] (https://www.tipranks.com/news/the-fly/varonis-reports-q3-adjusted-eps-9c-consensus-3c-thefly-news). The mechanical base fair value of 54.47 sits above the price [Certain]. Still, a spread capture is merger arbitrage, which is neither of the two permitted tactical setups (owner rule), and it gives no edge for a 2:1 trade [Likely].

## Decision
```json
{
  "ticker": "VRNS",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A deal-pinned takeover target, not a pullback in an uptrend; the capped upside and gap-down risk on a deal break leave no tradable 2:1 edge.",
  "rationale": "The price follows the Proofpoint cash bid, not a trend. The 2:1 target sits at the deal-capped 50.31 high, and a deal break would gap through the ATR stop towards 31.79. This is merger arbitrage, which is outside the owner's two tactical setups, so the trade has no clear edge. AVOID.",
  "price_at_decision": 48.94,
  "price_date": "2026-11-13",
  "research_note": "research/VRNS/2026-11-15.md",
  "exit_plan": {"target": 50.0132, "stop": 48.4034, "time_limit": "2027-02-12"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 50.31, "basis": "The deal closes and the price ends at or just above the 50.31 52-week high [HI]; the cash bid caps the upside below the 54.47 base fair value [IS,RA]."},
    "base": {"probability": 0.6, "target_price_12m": 49.27, "basis": "The price stays pinned near the recent swing high of 49.27 [HI] while the Proofpoint deal is pending (https://www.tipranks.com/news/proofpoint-to-buy-varonis-vrns-for-6-3-billion-in-ai-security-push); this sits below the mechanical base of 54.47 because the bid, not standalone value, sets the price."},
    "bear": {"probability": 0.15, "target_price_12m": 31.79, "basis": "The deal breaks and the stock falls back to the mechanical bear fair value of 31.79 (EV/Revenue, fact sheet Fair value), with operating margin at -22.5% [IS] giving no standalone support."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

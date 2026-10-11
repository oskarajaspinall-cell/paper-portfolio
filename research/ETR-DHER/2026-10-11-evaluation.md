# Evaluation: Delivery Hero SE (ETR:DHER) — 2026-10-11
## Bear case
The "pullback in an uptrend" is not a trend setup at all: the stock is pinned in a takeover-arbitrage range after Delivery Hero agreed to support Uber's offer (company ad-hoc, 2026-09-24) [Certain]. Price has held 36.21-37.18 EUR since early September with ATR just 0.7% of price [Certain], so the ATR stop (35.93) measures range noise, not the real risk. The real risk is binary: South Korea's FTC review of Baemin (2026-09-22) could block, delay or force revised terms [Likely], and on a break the standalone business offers little support: Altman Z 0.34, Piotroski 3, net debt/EBITDA 18.15x, TTM operating margin -0.5% [Certain]. A deal break gaps well through any stop; the EV/Revenue bear fair value is 21.95 EUR [Certain]. Upside, meanwhile, is capped by deal consideration [Likely], so the 2:1 ratio on paper is not a real 2:1.
## Bull case
The 12-month trend is strong: +48.4% over 12 months, 50-day 25.8% above the 200-day, RS vs SPY +32.8pp, RSI 50.0 [Certain]. Mechanically the setup passes: 2:1 target 37.93 sits below the 3-month peak 38.96, 3.5x the stop distance [Certain]. A board-supported bid with the CEO staying through closing raises completion odds [Likely], and the spread to terms could narrow as regulatory milestones pass [Guessing]. EV/Sales of 0.9x vs a peer median of 2.0x and a base fair value of 41.89 EUR (+14.5%) leave room if terms are improved or a rival bidder emerges [Guessing]. But none of this is a pullback edge; it is a merger-spread bet the tactical rules don't cover.
## Decision
```json
{
  "ticker": "ETR:DHER",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "The pullback signal is an artefact of a takeover-arbitrage range around Uber's board-supported bid, so the ATR-based plan understates a binary regulatory gap risk and its upside is capped by deal terms.",
  "rationale": "Not one of the two owner setups in substance: the price is anchored by a pending, regulator-reviewed acquisition, not a dip in a trend. A 0.7% ATR stop cannot protect against a deal break (bear fair value 21.95 EUR), and upside beyond terms is limited. Reward:risk is nominal, not real. Cash is the better outcome.",
  "price_at_decision": 36.60,
  "price_date": "2026-10-09",
  "research_note": "research/ETR-DHER/2026-10-11.md",
  "exit_plan": {"target": 37.93, "stop": 35.93, "time_limit": "2027-01-08"},
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 39.83, "basis": "Deal clears with improved terms or a rival approach, taking the stock back to its 52-week high of 39.83 EUR [HI]; below the 41.89 EUR base fair value [EV/Revenue, fact sheet] because takeover consideration, not standalone value, sets the price."},
    "base": {"probability": 0.6, "target_price_12m": 37.18, "basis": "Uber deal proceeds through the Korean FTC review (https://www.ibtimes.com.au/south-korea-uber-delivery-hero-baemin-merger-review-1875743) and the stock stays in its arb range, settling near the 37.18 EUR swing high [HI]; capped below the 41.89 EUR base fair value by deal terms."},
    "bear": {"probability": 0.2, "target_price_12m": 21.95, "basis": "Deal blocked or abandoned and the stock reverts to standalone value, the EV/Revenue bear fair value of 21.95 EUR [fact sheet], with distressed quality (Altman Z 0.34, net debt/EBITDA 18.15x [ST,RA]) offering no support."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Givaudan SA (SWX:GIVN) — 2026-10-17

## Bear case
The drift may already be spent. The stock held 130% of the reaction-day jump [Certain], RSI(14) is 80.2 [Certain], and the close is +16.7% above the 50-day MA after a +36.1% six-month run [Certain]. The minimum 2:1 target of 4,464.72 CHF has no chart level or valuation anchor behind it. The note uses the minimum only because nothing supports going further [Certain]. For a beta-0.62 name with a 2.2% ATR [Certain], getting there inside the drift window needs another strong leg up right after a crowded rally [Likely]. Valuation is a gap risk. The blended base fair value is 2,364.63 CHF, the reverse DCF implies 19.8% year-1 revenue growth [Certain], and EV/Sales is +68% above peers [Certain]. Any sign that flavours are fading, or news from India's collusion probe, could test the stop quickly [Guessing].

## Bull case
The beat is real. Organic growth came in well ahead of expectations, led by fragrance, with flavours still recovering, and management confirmed its mid/long-term like-for-like target [Likely] (https://www.reuters.com/business/givaudans-quarterly-organic-sales-beat-market-view-fragrance-strength-2026-10-13/). The reaction was +9.4% on 4.2x volume and extended to a new 52-week high of 3,948 [Certain], which leaves no overhead supply. Next earnings (Jan 27, 2027) fall outside the window [Certain]. Quality is improving: ROCE 15.1%, operating margin up +1.8pp over five years, net debt/EBITDA down -0.87x [Certain]. On its own history EV/EBITDA of 24.7x sits at its 5y median of 25.0x [Certain], so the rerating is not extreme by its own standards [Likely].

## Decision
```json
{
  "ticker": "SWX:GIVN",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A genuine Q3 organic-growth beat, but the stock is already extended and overbought, and nothing in the evidence supports the 2:1 target inside the drift window.",
  "rationale": "The setup is valid, but the edge is unclear. The price has gone past the reaction, RSI is 80.2, and the minimum target has no resistance or valuation support for a low-volatility name. Reward:risk passes only mechanically. Good but not compelling, so AVOID; I would revisit on a pullback to the 50-day average.",
  "price_at_decision": 3915.00,
  "price_date": "2026-10-16",
  "research_note": "research/SWX-GIVN/2026-10-17.md",
  "exit_plan": {"target": 4464.72, "stop": 3640.14, "time_limit": "2026-12-11"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 4172.92, "basis": "The fragrance-led beat persists and EV/EBITDA holds above its 5y median, reaching the EV/EBITDA method's bull value of 4,172.92 CHF [RA,IS]; this sits above the blended DCF bull because the DCF's 5.10% risk-free rate penalises a low-beta compounder."},
    "base": {"probability": 0.5, "target_price_12m": 3758.56, "basis": "EV/EBITDA settles at its 5y median of 25.0x on TTM EBITDA, the EV/EBITDA method's base of 3,758.56 CHF [RA,IS]; the blended base of 2,364.63 CHF is lower because the DCF leg sits far below the stock's own-history multiples."},
    "bear": {"probability": 0.25, "target_price_12m": 3026.56, "basis": "Flavours stall and the India collusion probe weighs (Reuters, https://www.reuters.com/world/india-investigates-fragrance-giants-over-price-collusion-document-shows-2026-08-25/), so the multiple de-rates toward the EV/EBITDA method's bear of 3,026.56 CHF [RA]."}
  },
  "entry_price": 3354.18,
  "entry_basis": "A pullback to the 50-day MA (3,354.18 CHF [ST,HI]) inside the uptrend would turn this into a clean pullback setup with the stop room and target headroom that the current extended entry lacks; base fair value x 0.8 is not used because it is meaningless for an 8-week trade.",
  "replaces": null,
  "replacement_reason": null
}
```

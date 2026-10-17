# Evaluation: Lamb Weston Holdings, Inc. (LW) — 2026-10-17
## Bear case
The "beat" is thin: Q1 sales and adjusted EPS each rose only 1% YoY while adjusted EBITDA fell 5% on EMEA potato-cost carry-in, so the drift rests on a guidance raise, not on results that are broadly strong [Likely] (/stocks/lw/transcripts/715204-q1-2027/). The price has already run to base fair value (54.32 vs a 53.59 close) [Certain], RSI is 66.3 [Certain], and the reverse DCF already implies 3.6% growth [Certain]. The volatility stop at 46.21 sits far below the price, so the 2:1 target of 68.35 needs a new 52-week high above 67.07 within 8 weeks for a 0.47-beta staples name, with the 55.69-55.70 swing highs directly overhead [Likely]. Leverage of 3.55x net debt/EBITDA, falling ROIC (8.5% TTM) and Altman Z of 2.62 limit re-rating room [Certain]. Short interest is up 13.6% [Certain].
## Bull case
Management raised FY2027 targets on North America volume momentum and working cost actions, a real guidance upgrade rather than an in-line print [Likely] (https://www.businesswire.com/news/home/20261006592806/en/Lamb-Weston-Announces-First-Quarter-Fiscal-2027-Results-Above-Guidance/). The stock has held well over its full reaction-day jump (270% held) with 5.2x volume, a classic drift signature [Certain]. The trend is constructive: price +7.8% over the 50-day and +16.5% over the 200-day, beating SPY by 12.5pp over 3 months [Certain]. FCF margin has risen to 6.2% TTM and shares fell 2.07% YoY [Certain]. EV/Sales and P/FCF sit near the bottom of their 5y ranges, so the drift is not crowded on valuation [Certain]. If EMEA costs fade, margin recovery could extend the move [Guessing].
## Decision
```json
{
  "ticker": "LW",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 2,
  "thesis": "A guidance-raise drift in Lamb Weston is real but the modest underlying beat, overhead resistance at the swing highs and a wide volatility stop leave the 2:1 target requiring a new 52-week high within 8 weeks, which the evidence does not support.",
  "rationale": "The setup qualifies mechanically, but the honest target is the 55.69-55.70 swing highs or at best the 67.07 52-week high, short of the 68.35 2:1 level from a 46.21 stop. Sales and EPS grew only 1%, EBITDA fell, and price already sits at base fair value. Reward:risk does not hold; cash is preferable.",
  "price_at_decision": 53.59,
  "price_date": "2026-10-16",
  "research_note": "research/LW/2026-10-17.md",
  "exit_plan": {"target": 68.35, "stop": 46.21, "time_limit": "2026-12-11"},
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 67.07, "basis": "NA volume gains and fading EMEA potato costs drive a retest of the 52-week high of 67.07 [HI], still well short of the mechanical bull fair value of 95.24, whose DCF leans on margin recovery the falling ROIC does not yet show [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 54.32, "basis": "Raised FY2027 guidance is already priced: the stock trades at the blended base fair value of 54.32 and the reverse DCF implies 3.6% growth, roughly the delivered pace [IS, ST]."},
    "bear": {"probability": 0.3, "target_price_12m": 40.16, "basis": "EMEA cost pressure (adjusted EBITDA down 5%, /stocks/lw/transcripts/715204-q1-2027/) and 3.55x net debt/EBITDA [BS,IS] push the price back to its 6-month low of 40.16 [HI], above the P/E-method values of 28.95-36.59 because FCF margin has improved to 6.2% [CF,IS]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

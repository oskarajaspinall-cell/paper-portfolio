# Evaluation: Ryder System, Inc. (R) — 2026-10-31
## Bear case
The edge has already been paid. The shares closed +10.5% on 2.3x volume on 2026-10-22 and now hold 168% of the jump, with RSI 76.0 and the price +15.3% above the 50-day average (HI, ST) [Certain]. The drift that is left is thin. The minimum 2:1 target of 350.9 sits far above the 52-week high of 287.00, and the note itself calls it only partly supported [Guessing]. Valuation leaves no room for error: P/E 21.6x and EV/EBITDA 6.7x are both above their 5-year maximums (RA) [Certain], so any freight or used-vehicle softness can gap the stock down [Likely]. The beat leaned on cyclical used-vehicle sales and rental, and guidance had already been raised in September, so the October raise adds little (transcript) [Likely]. Leverage is real: net debt/EBITDA is 2.84x and Altman Z is 1.54 (RA, ST) [Certain].
## Bull case
This was a real beat. Q3 adjusted EPS and revenue came in above consensus, FY2026 EPS guidance went up again, and free cash flow nearly doubled (/stocks/r/transcripts/655428-q3-2026/) [Likely]. Operating margin has risen to 8.0% TTM and ROIC to 7.0% (IS, RA) [Certain]. The stock has no overhead resistance at its 52-week high (HI) [Certain]. It is still well below peers on EV/EBITDA and P/E, and its FCF yield is 13.18% (ST) [Certain]. Shares outstanding fell 6.89% YoY (ST) [Certain]. The reverse DCF implies -11.7% year-1 revenue growth, which leaves the price undemanding on fundamentals [Likely]. Momentum is strong: +65.4% over 12 months, +55.5pp ahead of SPY (ST, HI) [Certain].
## Decision
```json
{
  "ticker": "R",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A genuine Q3 beat with raised guidance, but the post-earnings drift is largely priced: the stock is overbought at a record high and the 2:1 target needs a move well beyond any level the evidence supports.",
  "rationale": "The setup qualifies mechanically, but the trade does not. RSI 76.0, the price +15.3% over its 50-day, multiples above their 5-year maximums and a 350.9 target far above the 287.00 high make reward:risk 2:1 on paper only. Good but not compelling, so no position. A pullback toward the 50-day would reset the trade.",
  "price_at_decision": 282.55,
  "price_date": "2026-10-30",
  "research_note": "research/R/2026-10-31.md",
  "exit_plan": {"target": 350.9, "stop": 248.39, "time_limit": "2026-12-26"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 350.9, "basis": "Guidance raised twice and FCF nearly doubling (transcript /stocks/r/transcripts/655428-q3-2026/) keep the re-rating going; still far below the DCF-driven base fair value 550.71, which capitalises a cyclical-peak TTM FCF margin of 10.9% against -1.0% in FY2023 [CF,IS]."},
    "base": {"probability": 0.45, "target_price_12m": 282.55, "basis": "Earnings growth roughly offsets EV/EBITDA easing from 6.7x, above its 5y max 5.8x [RA]; this sits between the EV/EBITDA method's bull 199.03 and the blended base 550.71, because the DCF leg overstates value on volatile capex-driven FCF [CF]."},
    "bear": {"probability": 0.30, "target_price_12m": 199.03, "basis": "Used-vehicle and rental tailwinds fade and EV/EBITDA reverts toward its 5y range (4.0x-5.8x [RA]), matching the EV/EBITDA method's bull value 199.03; leverage of 2.84x net debt/EBITDA [RA] amplifies the hit."}
  },
  "entry_price": 245.03,
  "entry_basis": "A pullback to the 50-day average 245.03 [ST,HI] removes the overextension (RSI 76.0) and makes a 2:1 target reachable inside the recent range below the 287.00 high [HI]; base fair value x 0.8 lies above the price, so it is not a usable anchor.",
  "replaces": null,
  "replacement_reason": null
}
```

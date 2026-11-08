# Evaluation: Nextpower Inc. (NXT) — 2026-11-07
## Bear case
The drift stop (102.17) sits only about 0.4 ATR below the 104.91 close, while ATR is 6.8% of price and beta is 1.93 with VIX at 28.18 [Certain]. An ordinary day's noise can stop the trade out before any drift plays out [Likely]. The edge is muddied: results came on 28 Oct, but the big move dates to 2026-11-02 alongside a broker "Franchise Pick" addition, so part of the jump is opinion-driven re-rating, not results digestion [Likely]. The longer trend is down (50-day -21.7% below the 200-day, 6-month momentum -16.8%) and RSI 67.2 is stretched after a run from the 75.41 low [Certain]. Management guided second-half margin pressure from inflation and ramp costs, and gross margin has already slipped to 21.8% TTM from 27.7% in FY2024 [Likely]. Base fair value 54.94 and even bull 100.74 sit below the price, a gap risk if sentiment fades [Certain].
## Bull case
The beat is real: record revenue, EBITDA and bookings, backlog above $6B and raised FY27 revenue and EPS guidance (https://stockanalysis.com/stocks/nxt/transcripts/720305-q2-2027/) [Likely]. The 2026-11-04 reaction was +11.1% on 4.5x volume and 83% of the jump is held, a classic drift signature [Certain]. The balance sheet is net cash (net debt/EBITDA -1.30x TTM), ROIC 38.2% TTM, and P/E 26.4x is -37% vs peers, so this is not a fragile name [Certain]. 3-month relative strength vs SPY is +10.9pp, and the nominal target clears the 2:1 minimum with no earnings date inside the window [Likely].
## Decision
```json
{
  "ticker": "NXT",
  "decision": "AVOID",
  "position_type": "TACTICAL",
  "conviction": 3,
  "thesis": "A genuine Q2 FY27 beat with raised guidance produced a drift signature, but a stop within ordinary daily noise, a broker-driven share of the move and a still-falling long-term trend leave the trade's edge unclear.",
  "rationale": "The beat is real, but the volatility-based stop is only about 0.4 ATR below the close in a high-beta, high-VIX tape, so a noise stop-out is likely; the target barely clears the 108.39 swing high and part of the jump was a broker pick, not results. Reward:risk holds on paper only. Not compelling; cash is fine.",
  "price_at_decision": 104.91,
  "price_date": "2026-11-06",
  "research_note": "research/NXT/2026-11-07.md",
  "exit_plan": {"target": 110.40, "stop": 102.17, "time_limit": "2027-01-04"},
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 125.0, "basis": "Raised FY27 guidance and record backlog above $6B (transcript, https://stockanalysis.com/stocks/nxt/transcripts/720305-q2-2027/) grow EBITDA while EV/EBITDA stays toward its 5y max 23.0x [RA], above the mechanical bull 100.74 because that model does not capture the guidance raise."},
    "base": {"probability": 0.45, "target_price_12m": 82.49, "basis": "EV/EBITDA reverts to its 5y median 15.6x [RA] (the EV/EBITDA base value 82.49 in the fact sheet's Fair value), above the blended base 54.94 because the DCF leg is weighed down by FCF margin falling from 21.0% to 13.4% [CF,IS]."},
    "bear": {"probability": 0.30, "target_price_12m": 47.49, "basis": "Guided second-half margin pressure (transcript) extends the gross-margin slide from 27.7% to 21.8% [IS] and EV/EBITDA falls toward its 5y low, matching the EV/EBITDA bear value 47.49 in the fact sheet's Fair value."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: this is a tactical drift assessment whose weakness is setup structure (a stop inside daily noise, a broker-driven share of the move, a downtrend); a lower price would void the drift setup rather than improve it.",
  "replaces": null,
  "replacement_reason": null
}
```

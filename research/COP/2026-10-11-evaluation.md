# Evaluation: ConocoPhillips (COP) — 2026-10-11
## Bear case
COP is priced for a better cycle than its returns show. ROIC fell from 31.3% (FY22) to 9.6% (FY25, TTM 11.6%), and operating margin fell from 33.9% to 20.9% [Certain] [RA, IS]. Yet P/E 17.8x, EV/EBITDA 6.6x and EV/Sales 2.7x all sit above their 5y maxima, and P/FCF 16.0x is at its 5y max [Certain] [RA]. The last close of 134.10 is above even the bull fair value of 112.55, and base fair value 107.11 is 20.1% lower [Certain]. Buybacks have stalled: shares are +0.27% YoY [Certain] [ST]. A new CEO and CFO take over mid-cycle [Certain]. The macro overlay flags a rising dollar and real yields as pressure on oil prices, which hits a pure upstream producer with no refining offset [Likely]. A 3-month run of +24.1% leaves room to give back gains if oil softens [Likely].
## Bull case
The balance sheet is strong: net debt/EBITDA is 0.58x, Altman Z 3.10 and FCF conversion 108.4% TTM [Certain] [RA, ST]. The FCF yield is 6.25% [Certain] [ST]. On P/E (-6%) and EV/EBITDA (-8%), COP is cheaper than the XOM/CVX/EOG/OXY median [Certain]. TTM ROIC (11.6%) and FCF margin (15.6%) have turned up from FY25 [Certain] [RA]. Management sees the oil price floor rising to about $70 [Likely] (Reuters 2026-10-05). The 20-year LNG deal and a possible Norway/Teesside sale could sharpen the portfolio and fund capital returns [Guessing]. With a beta of 0.24, COP would diversify a portfolio that holds no energy [Certain]. Still, none of this offsets paying above own-history multiples for a commodity price-taker with falling returns.
## Decision
```json
{
  "ticker": "COP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A low-leverage, cash-generative upstream producer whose returns have fallen for four years now trades above its own 5-year multiple range and above its bull-case fair value, leaving no margin of safety.",
  "rationale": "The balance sheet and FCF are sound, and COP would diversify the portfolio. But ROIC has more than halved since FY22, every multiple except P/B is at or above its 5y max, and the price sits above even bull fair value. The macro overlay tilts slightly bearish. The business is good, but not compelling at 134.10, so the decision is AVOID.",
  "price_at_decision": 134.10,
  "price_date": "2026-10-09",
  "research_note": "research/COP/2026-10-11.md",
  "triggers": [
    {"text": "TTM ROIC recovers above 15%, reversing the decline from 31.3% (FY22) to 11.6% TTM and showing returns are not just mean-reverting with oil.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 15}},
    {"text": "TTM FCF margin recovers above 22% (FY22 level), up from 15.6% TTM, showing cash generation can fund returns at the current asset base.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 22}},
    {"text": "Net buybacks resume: the share count shrinks by more than 2% YoY (now +0.27%), showing FCF is going back to shareholders.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": -2}},
    {"text": "TTM operating margin falls below 18%, under the FY25 low of 20.9%, which would mean margin compression is deepening and confirms the AVOID."}
  ],
  "scenarios": {
    "bull": {"probability": 0.20, "target_price_12m": 141.62, "basis": "Oil holds near management's ~$70 floor view (Reuters 2026-10-05), and EV/EBITDA stays at the above-range 6.6x [RA] while TTM EBITDA edges up, so the stock retests its 52-week high of 141.62 [HI]; this sits above the bull fair value of 112.55 because it assumes the market keeps the above-range multiple. The macro overlay's small bear tilt (research/COP/2026-10-11-macro.md) cut this probability by 0.05."},
    "base": {"probability": 0.45, "target_price_12m": 122.00, "basis": "EV/EBITDA eases from 6.6x to its 5y max of 6.0x [RA] on flat TTM EBITDA, which gives about 122. That is above the base fair value of 107.11 because a full reversion to the 5.5x median within 12 months is not assumed while TTM ROIC (11.6%) and FCF margin (15.6%) are improving [RA]."},
    "bear": {"probability": 0.35, "target_price_12m": 83.09, "basis": "The dollar and real-yield headwinds in the macro overlay (research/COP/2026-10-11-macro.md, which raised this probability by 0.05) press oil prices, and EV/EBITDA reverts toward its 5y min of 4.4x [RA] on lower EBITDA, matching the fact sheet's bear fair value of 83.09, close to the 52-week low of 85.57 [HI]."}
  },
  "entry_price": 85.69,
  "entry_basis": "valuation file: base 107.11 x 0.8 = 85.69. At that price EV/EBITDA would sit near its 5y median of 5.5x [RA], so a 6.25%+ FCF yield on a 0.58x-levered balance sheet would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: MMG Limited (HKG:1208) — 2026-10-19
## Bear case
MMG is a copper/zinc price-taker with no moat [Certain], and the TTM figures are a cyclical high: operating margin of 42.4% and ROIC of 20.2% compare with 11.8% and 3.6% in FY2023, and all three margins are down over five years [Certain] (IS, RA). A 3.7x EV/EBITDA on record H1 2026 earnings [Likely] is the market pricing mean reversion, not a mispricing [Likely]. The mechanical base fair value of 8.16 HKD is only +6.9% above the 7.63 close, while the bear case of 5.16 is -32.4% [Certain]. Shares are up 3.43% YoY after the ~$1.6bn raise [Certain] (ST). Altman Z is 2.09, in the grey zone [Certain]. Peru, DRC and Botswana carry jurisdiction risk, and state-linked ownership cannot be sized [Guessing]. The macro overlay tilts toward bear: the dollar, real yields and HY spreads all moved against metals over the last month [Likely] (macro overlay).
## Bull case
The balance sheet has been repaired: net debt/EBITDA fell from 3.44x in FY2022 to 0.16x [Certain] (RA). FCF yield is 20.22% and P/FCF is 4.9x [Certain] (ST, RA). EV/EBITDA sits below its own 5y minimum of 4.1x and well below the 10.2x peer median [Certain]. Growth at Kinsevere and Khoemacau, plus lower cost guidance at Las Bambas, Khoemacau and Rosebery, could keep volumes and margins up [Likely] (Q2 2026 transcript). If copper holds, the stock could retest its 52-week high of 11.96 [Guessing]. The mechanical bull value is 17.80 [Certain]. Piotroski F is 7 [Certain].
## Decision
```json
{
  "ticker": "HKG:1208",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraged, cash-generative copper miner that looks cheap on peak-cycle TTM earnings, with no moat and only modest base-case upside to its mechanical fair value.",
  "rationale": "The low multiples rest on cyclical record earnings, not on a structural gain. Base fair value sits barely above the price, the bear case is a deep loss, and the macro tilt is toward bear. Deleveraging and strong FCF are real but not enough to make this compelling, so conviction is 3 and the decision is AVOID.",
  "price_at_decision": 7.63,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-1208/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROIC falls below its own 5y average of about 7.3%, showing the TTM profitability was purely cyclical.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 7.3}},
    {"text": "Net debt/EBITDA rises back above 2.0x, reversing the deleveraging that is the one structural improvement.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.0}},
    {"text": "TTM net margin falls below 5%, showing post-raise earnings power has not held.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 5}},
    {"text": "Shares outstanding grow more than 5% YoY, showing dilution beyond the 2026 raise.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 5}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 11.96, "basis": "Copper firms and the expansions deliver, so the stock retests its 52-week high [HI]. This is set below the mechanical bull of 17.80 because that value needs peak EBITDA plus a re-rating, and the macro overlay's bear tilt cuts this probability slightly (research/HKG-1208/2026-10-19-macro.md)."},
    "base": {"probability": 0.45, "target_price_12m": 8.16, "basis": "EV/EBITDA moves partway back toward its 5y median of 6.3x [RA] while TTM EBITDA normalises from record H1 2026 levels, which matches the mechanical base fair value."},
    "bear": {"probability": 0.35, "target_price_12m": 5.16, "basis": "The dollar, real yields and HY spreads keep tightening (macro overlay, small bear tilt), metal prices and margins revert toward the FY2023 trough [IS], and the result matches the mechanical bear fair value."}
  },
  "entry_price": 6.53,
  "entry_basis": "valuation file: base 8.16 x 0.8 (also the 6-month low of 6.53 [HI]); at that price the margin of safety would offset the cyclical earnings risk."
}
```

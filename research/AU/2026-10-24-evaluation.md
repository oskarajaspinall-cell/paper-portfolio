# Evaluation: AngloGold Ashanti plc (AU) — 2026-10-24
## Bear case
Today's returns come from the gold cycle, not from a moat. TTM operating margin of 49.9% compares with 12.4% in FY2023, and ROIC went from -38.7% to 45.0% in two years, which shows how quickly quality fades when gold falls [Certain]. The low multiples (P/E 11.2x, EV/EBITDA 5.8x) are measured on peak margins. The mechanical base fair value of 37.76 is well below the 83.59 close, so the price assumes peak gold economics last [Likely]. P/B of 4.8x is above its 5y max and 55% above peers [Certain]. The share count rose 7.69% YoY even with a buyback announced [Certain]. The macro overlay is primary and tilts toward bear: the 10y real yield is 2.64%, up 0.21pp over 3m, and the dollar is stronger, the mix most hostile to gold [Likely]. Earnings are due Nov 5, 2026, and the cause of the sell-off is unexplained [Guessing].

## Bull case
The balance sheet is net cash (net debt/EBITDA -0.14x) and the FCF yield is 10.48%, with FCF conversion at 117.4% of net income [Certain]. P/E is below its 5y minimum, and both P/E and EV/EBITDA trade below peer medians [Certain]. The shares are 17.2% below the 50-day average with RSI 31.6, so part of the macro headwind is priced [Likely]. Organic growth in Nevada and Colombia plus the buyback could keep cash returns high if gold holds (https://stockanalysis.com/stocks/au/transcripts/751941-mining-forum-americas-2026/) [Likely]. The mechanical bull value of 115.79 shows how far the shares could run if real yields ease [Guessing]. Altman Z of 7.51 and Piotroski F of 7 confirm the company is financially sound today [Certain].

## Decision
```json
{
  "ticker": "AU",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash gold miner earning peak-cycle margins looks cheap on trailing multiples, but its earnings are a geared bet on gold rather than a durable franchise, and the price sits far above its normalised fair value.",
  "rationale": "The quality is cyclical: margins and ROIC track gold, and FY2023 shows how fast they reverse. Low multiples sit on peak earnings, P/B is above its 5y max, the share count is rising, and the macro overlay leans bearish. There is no margin of safety on normalised earnings, so cash is the better choice.",
  "price_at_decision": 83.59,
  "price_date": "2026-10-23",
  "research_note": "research/AU/2026-10-24.md",
  "triggers": [
    {"text": "TTM gross margin falls below 40%, showing the gold-price margin expansion is reversing.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
    {"text": "TTM FCF margin falls below 20%, showing cash generation is retreating toward the FY2021-23 levels.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 20%, showing returns are normalising with the cycle.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Debt/EBITDA rises above 1.0x, ending the net-cash balance sheet.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 115.79, "basis": "Real yields and the dollar ease and gold re-rates, so EBITDA holds near peak and EV/EBITDA moves back toward its 5y median of 8.0x [RA], in line with the mechanical bull value of 115.79 [FV]."},
    "base": {"probability": 0.45, "target_price_12m": 80, "basis": "Margins hold near TTM levels (operating margin 49.9% [IS]) and EV/EBITDA stays near its 5y low of 5.8x [RA]; this sits above the mechanical base of 37.76 because that value assumes margins normalise, which this scenario does not."},
    "bear": {"probability": 0.35, "target_price_12m": 37.76, "basis": "Real yields keep rising (macro overlay research/AU/2026-10-24-macro.md: tilt toward bear, small, which moves probability from bull to bear) and margins fall back toward the 5y median, in line with the mechanical base fair value of 37.76 [FV]."}
  },
  "entry_price": 30.21,
  "entry_basis": "valuation file: base 37.76 x 0.8; only at a price below normalised fair value would a cyclical miner's peak-margin quality justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

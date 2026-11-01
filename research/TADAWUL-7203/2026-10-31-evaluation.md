# Evaluation: Elm Company (TADAWUL:7203) — 2026-10-31
## Bear case
The stock is down 40.8% over 12 months and trades below its 50-day and 200-day averages, so the market may be pricing a growth reset we cannot see. The note fetched no revenue growth, segment mix or contract data [Certain]. Meanwhile the reverse DCF needs 9.8% year-1 revenue growth [Certain]. Returns and margins have come off their peaks: ROIC 75.3% TTM vs 193.3% in FY2023, and operating margin 21.4% vs 23.2% in FY2024 [Certain]. Net cash is shrinking: net debt/EBITDA went from -2.54x to -0.68x [Certain]. Revenue likely depends on Saudi government budgets, which track oil, so concentration is high [Likely]. Even after the de-rating it trades well above Saudi peers on EV/EBITDA (16.6x vs 8.8x) [Certain]. Results are due Nov 1, which raises gap risk, and liquidity is below the screen's gate [Certain]. The mechanical bear value of 375.15 sits well below the price [Certain].
## Bull case
This is an exceptional business: ROE 56.1%, ROCE 32.3%, a 23.6% FCF margin, FCF conversion of 112.3%, net cash, and Piotroski 7 [Certain]. Gross and operating margins have held in a tight band since FY2022, which argues against structural erosion so far [Certain]. The de-rating is severe. P/E of 20.1x, EV/EBITDA of 16.6x and EV/Sales of 4.1x all sit below their 5y minimums (27.7x, 21.7x, 5.2x), and P/FCF is near its 5y low [Certain]. The FCF yield is 5.59% [Certain]. Base fair value of 663.58 is above the price [Certain]. Incumbency in government digital services is hard to copy [Likely]. Beta is 0.43, so returns don't hinge on the market [Certain]. If the Nov 1 results show growth holding, the stock could re-rate toward its own historical multiples [Guessing].
## Decision
```json
{
  "ticker": "TADAWUL:7203",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-return Saudi government-IT incumbent has de-rated below its own 5-year minimum multiples, but without visible revenue growth or contract data the price's implied 9.8% growth cannot be confirmed.",
  "rationale": "Quality is excellent and the de-rating is real. But growth evidence is missing, returns and margins are drifting down, net cash is shrinking, concentration on Saudi state spending is likely, results land tomorrow and liquidity is thin. The modest base upside against a much deeper mechanical bear value is good but not compelling, so this is an AVOID with an entry price.",
  "price_at_decision": 561.00,
  "price_date": "2026-10-29",
  "research_note": "research/TADAWUL-7203/2026-10-31.md",
  "triggers": [
    {"text": "TTM operating margin falls below 18%, under every year since FY2022 (21.4% TTM now), showing pricing or mix pressure on government contracts.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 18}},
    {"text": "TTM ROIC falls below 40%, under the FY2021 level of 54.8%, signalling the incumbent moat is eroding.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 40}},
    {"text": "TTM FCF margin falls below 15%, back toward the FY2021 low of 13.4%, showing cash conversion has broken.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Revenue (income statement) declines year on year in the FY2026 annual results, or the Nov 1 results show growth well below the 9.8% the reverse DCF implies."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 739.00, "basis": "Results confirm growth and EV/EBITDA moves back toward its 5y minimum of 21.7x [RA], retesting the 6-month high of 739.00 [HI], still below the mechanical bull value of 1,418.03."},
    "base": {"probability": 0.45, "target_price_12m": 620.00, "basis": "Margins hold near 21.4% operating [IS] and multiples recover only partly, toward but below the base fair value of 663.58 [fair value], because peers trade at 8.8x EV/EBITDA [P]."},
    "bear": {"probability": 0.30, "target_price_12m": 427.76, "basis": "A growth or contract reset keeps margins drifting down from 23.2% [IS] and the multiple compresses to the EV/EBITDA bear value of 427.76 [fair value], above the blended bear of 375.15."}
  },
  "entry_price": 530.86,
  "entry_basis": "valuation file: base 663.58 x 0.8 (fact-sheet fair value [IS,BS,CF,RA,ST,HI]); at that margin of safety the missing growth evidence and the bear-case gap would be adequately priced for conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

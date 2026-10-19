# Evaluation: Haidilao International Holding Ltd. (HKG:6862) — 2026-10-19
## Bear case
The cheapness is chasing a deteriorating business. FCF margin has fallen every year from 20.6% (FY2023) to 8.0% TTM, operating margin from 14.2% (FY2024) to 12.3%, and net margin from 11.0% to 9.0% [Certain]. Gross margin slipped from 23.9% to 21.8% [Certain], consistent with price competition in a category with low barriers [Likely]. The moat is execution, not structure; rivals can copy it [Likely]. The price is down 29.5% over 12 months and 39.4% over 6 months, below both moving averages, so the market is still marking down earnings, not just the multiple [Likely]. The mechanical base value is only modestly above the price while the bear value is roughly half of it, so the skew is unattractive [Certain]. Piotroski F of 5 is middling, and 64.19% insider ownership with 8.8% institutional leaves minority holders little influence [Certain]. FX losses produced an H1 2026 net loss [Likely].

## Bull case
Haidilao earns 48.8% ROIC and 41.9% ROE with net cash (net debt/EBITDA -0.27x) and flat share count [Certain]. At 10.8x P/E and 5.8x EV/EBITDA it trades below its own 5-year minimum on every earnings multiple, with a 7.95% FCF yield [Certain]. The reverse DCF implies only 4.0% year-one revenue growth, a low bar for a chain still opening stores and growing delivery and new brands [Likely]. The H1 2026 call described stronger traffic and lower expense ratios, with second-half openings planned, suggesting margins may be troughing [Likely]. If EV/EBITDA merely returned to its 5-year minimum of 9.3x, the EV/EBITDA method's base value of 15.17 HKD would be well above the price [Certain]. Macro is context only: CNY business, beta 0.77, no debt [Likely].

## Decision
```json
{
  "ticker": "HKG:6862",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 48.8%-ROIC hot pot leader trades below its own 5-year minimum multiples, but four straight years of falling FCF margin and slipping operating and gross margins mean the low multiple may be pricing real erosion rather than a mispricing.",
  "rationale": "Returns and balance sheet are excellent and multiples are at historic lows, but cash and operating margins are still falling, the mechanical base value offers only modest upside against a much deeper bear, and the price trend shows no stabilisation. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 9.37,
  "price_date": "2026-10-16",
  "research_note": "research/HKG-6862/2026-10-19.md",
  "triggers": [
    {"text": "TTM FCF margin recovers above 12%, showing the four-year slide from 20.6% has reversed and cash generation is rebuilding (would raise conviction).", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 12}},
    {"text": "TTM operating margin returns above 14.2%, the FY2024 level, confirming the H1 2026 expense-ratio improvement is durable (would raise conviction).", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 14.2}},
    {"text": "TTM ROIC falls below 25%, roughly half its TTM level, showing the post-pandemic return recovery is reversing (would confirm the AVOID).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 25}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 15.17, "basis": "Margins trough as the H1 2026 call's lower expense ratios flow through and EV/EBITDA recovers toward its 5y minimum 9.3x [RA], matching the EV/EBITDA method's base value of 15.17 HKD in the fact sheet's fair-value section."},
    "base": {"probability": 0.5, "target_price_12m": 9.64, "basis": "FCF margin stabilises near 8.0% TTM [CF,IS] and the stock tracks the DCF base value of 9.64 HKD, below the blended 11.49 HKD because the EV/EBITDA leg assumes a rerating toward 5y multiples that falling margins do not yet justify."},
    "bear": {"probability": 0.3, "target_price_12m": 6.5, "basis": "FCF and operating margins keep falling (FCF margin 20.6% to 8.0% over three years [CF,IS]) and P/E compresses further; set above the mechanical bear 4.48 HKD because net cash (net debt/EBITDA -0.27x [RA]) and 41.9% ROE make the DCF bear's negative value implausible."}
  },
  "entry_price": 9.19,
  "entry_basis": "valuation file: base 11.49 x 0.8; at that level the modest base upside widens into a margin of safety that would justify conviction 4 on the same evidence.",
  "replaces": null,
  "replacement_reason": null
}
```

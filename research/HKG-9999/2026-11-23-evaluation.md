# Evaluation: NetEase, Inc. (HKG:9999) — 2026-11-23
## Bear case
Q3 net revenue fell and missed consensus, with lower revenue from some self-developed games weighing on online games (https://www.marketbeat.com/instant-alerts/transcript-what-netease-ntes-said-on-its-q3-earnings-call-2026-11-19/) [Likely]. NetEase is hit-driven: if the slate stays weak, the margin gains reverse with revenue, and the reverse DCF's -11.7% year-1 decline could prove right rather than too gloomy [Guessing]. The price trend is broken: 18.5% below the 200-day average, -28.6% over 12 months, RSI 26.2, near the 52-week low of 150.30 [Certain], so there are no trend points and the market may keep de-rating it. The Direction change lines matter less than they look: ROIC fell from 144.6% to 33.7% on a tiny invested-capital base while ROCE rose; FCF margin is 3.3pp below its 2-year high [Certain]. China game-approval rules, CNY exposure and plaintiff-firm solicitations add headline risk [Likely].
## Bull case
The business is still improving where it counts: TTM operating margin is 36.6%, up 5.0pp in a year and at its 2-year high; gross margin 68.2%; ROCE 23.2% and rising [Certain]. Games gross margin expanded on lower revenue-sharing costs (https://www.fool.com/earnings/takeaways/2026/11/19/netease-3-key-takeaways-for-long-term-investors/) [Likely], so the miss was revenue timing, not eroding economics [Likely]. FCF is 149.9% of net income and net cash is about 3.84x EBITDA [Certain], funding a dividend and buybacks (https://stockanalysis.com/quote/hkg/9999/transcripts/736905-q3-2026/) [Likely]. At 154.00 HKD every multiple is below its own 5-year minimum: P/E 13.1x, EV/EBITDA 5.7x, P/FCF 8.7x, an 11.49% FCF yield [Certain]. Base fair value 218.17 HKD sits well above the price, and the bear value of 147.03 is close to it, so downside on the mechanical range is limited [Certain]. Insiders own 45.32% [Certain].
## Decision
```json
{
 "ticker": "HKG:9999",
 "decision": "ADD",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "temporary",
  "decline_evidence": "ROIC's fall (144.6% to 33.7% TTM) is a denominator effect on a net-cash balance sheet: over the same 12 months operating margin rose 5.0pp to a 2-year high and ROCE rose to 23.2% [RA-T, IS-T]; FCF margin is flat (-0.9pp) at 41.7% [CF-T]. The Q3 revenue dip came from some self-developed games (MarketBeat call summary in the fact sheet), a content-cycle issue with margins intact.",
  "moat": "narrow",
  "key_risk": "medium",
  "key_risk_text": "The game slate stays weak and revenue keeps shrinking, so the margin expansion reverses; China game regulation is the second risk.",
  "veto": null
 },
 "new_evidence": {
  "type": "price_move",
  "text": "Since the 2026-11-15 HOLD the stock fell sharply after the Q3 2026 results of 2026-11-19 (revenue miss on some self-developed games) to 154.00 HKD, below its own 5-year minimum on every multiple, while TTM operating margin reached a 2-year high; the scorecard now clears the buy threshold, not just the hold band."
 },
 "thesis": "A net-cash games franchise with operating margin at a 2-year high of 36.6% and a 41.7% FCF margin trades below its own 5-year minimum on every multiple, pricing a revenue decline its margins and cash generation do not show.",
 "rationale": "The post-results fall is an overreaction to a revenue miss that left margins, cash conversion and net cash intact; the scorecard clears the buy threshold. ADD toward the conviction-4 size as Python sizes it; the China/HK country cap and the cash floor limit how much can actually be added.",
 "price_at_decision": 154.0,
 "price_date": "2026-11-20",
 "research_note": "research/HKG-9999/2026-11-23.md",
 "triggers": [
  {
   "text": "TTM operating margin falls below the FY2024 level of 28.1%, reversing the five-year expansion.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 28.1
   }
  },
  {
   "text": "TTM FCF margin falls below the FY2024 level of 36.5%, signalling cash generation is no longer keeping pace.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 36.5
   }
  },
  {
   "text": "TTM gross margin falls below the FY2024 level of 62.5%, indicating game-portfolio mix or monetization is deteriorating.",
   "check": {
    "source": "statistics",
    "field": "grossMargin",
    "op": "<",
    "value": 62.5
   }
  },
  {
   "text": "A new PRC regulation materially restricts game monetization, or a VIE-related regulatory action forces deconsolidation, as disclosed in a company filing or release."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 240.0,
   "basis": "New titles restore revenue growth and the multiples recover toward their 5y medians (P/E 15.4x, EV/EBITDA 10.4x [RA]), near the mechanical bull value of 244.87 HKD."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 200.0,
   "basis": "Revenue roughly flat with margins held at 36.6% [IS-T]; P/E re-rates partway to its 5y median 15.4x [RA], below the mechanical base 218.17 HKD because the Q3 revenue dip keeps the market cautious."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 140.0,
   "basis": "The self-developed game decline continues (Q3 call, MarketBeat link in fact sheet) and the stock stays below its 5y minimum multiples, a little under the mechanical bear 147.03 HKD."
  }
 },
 "second_opinion": {
  "file": "research/HKG-9999/2026-11-23-evaluation-2.md",
  "conviction": 4
 }
}
```

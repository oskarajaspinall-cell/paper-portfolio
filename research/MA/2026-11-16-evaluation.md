# Evaluation: Mastercard Incorporated (MA) — 2026-11-16
## Bear case
The price carries a large momentum premium: it is +22.0% above its 200-day average after a +34.8% six-month run, and the reverse DCF implies 23.5% year-1 revenue growth [Certain]. Every mechanical fair value (base 365.29, bull 471.90) sits well below the 661.19 close [Certain]. A slowdown in growth would bring a de-rating, and the FCF yield is only 2.79% [Likely]. Cash generation has weakened: TTM FCF margin fell from 54.0% to 44.3% in a year and conversion to 94.8%, while ROIC and ROCE are about 4pp below their March 2026 highs [Certain]. Litigation outflows (opt-out merchant settlements, UK/European interchange claims) are recurring, and the note has not reconciled them to the cash-flow gap [Likely]. Over time, stablecoin and AI-wallet rails could route around card networks [Guessing]. P/E is about double the peer median [Certain].

## Bull case
This is one of the best businesses listed: ROIC 91.0%, operating margin 60.1% at a 2-year high, no credit risk, and net debt/EBITDA of 0.59x [Certain]. The two-sided network effect with issuers, merchants and consumers has not been eroded; returns rose over five years [Likely]. Against its own history the stock is not expensive: P/E is at the 13th percentile of its 5y range and EV/EBITDA at the 3rd [Certain]. Operating margin is rising while FCF margin falls, so the cash gap looks like litigation and working-capital timing, not lost earnings power [Likely]. Value-added services are 41.24% of revenue `[company-reported]` and growing, and agentic commerce through the OpenAI partnership adds volume [Likely]. Buybacks cut the share count 2.63% a year [Certain]. The trend is strong: the stock leads SPY by +33.1pp over six months [Certain]. Macro is context only, per the overlay.

## Decision
```json
{
 "ticker": "MA",
 "decision": "BUY",
 "position_type": "CORE",
 "conviction": 4,
 "scorecard": {
  "decline_cause": "temporary",
  "decline_evidence": "FCF margin fell 54.0% -> 44.3% TTM [CF-T] while operating margin rose to a 2-year high of 60.1% [IS-T]; the 10-Q shows litigation cash outflows and opt-out settlement charges (https://www.sec.gov/Archives/edgar/data/1141391/000114139126000124/ma-20260930.htm), a cash-timing cost, not lost share or pricing. ROIC/ROCE remain far above FY2021-23.",
  "moat": "wide",
  "key_risk": "medium",
  "key_risk_text": "A de-rating from an extended price (+22.0% above the 200-day average, reverse DCF implying 23.5% growth) if growth slows or litigation/interchange regulation keeps cash conversion depressed.",
  "veto": null
 },
 "thesis": "A wide-moat, unlevered payments network with operating margin at a 2-year high and a strong uptrend, bought on trend strength and a low position in its own multiple range rather than a mechanical discount.",
 "rationale": "The scorecard gives 4: top quality, a near-unlevered balance sheet, a wide moat and trend strength, with the FCF dip explained by litigation cash. It does not score on value: the expected value sits near the price and the de-rating risk is real. That supports only the standard core size, which Python volatility-scales. No cap is breached, so nothing is replaced.",
 "price_at_decision": 661.19,
 "price_date": "2026-11-13",
 "research_note": "research/MA/2026-11-16.md",
 "triggers": [
  {
   "text": "TTM ROIC falls below 80%, giving up most of the five-year rise to 91.0% and signalling network pricing erosion.",
   "check": {
    "source": "statistics",
    "field": "roic",
    "op": "<",
    "value": 80
   }
  },
  {
   "text": "TTM operating margin falls below 56%, reversing the five-year expansion from 54.4% to 60.1%.",
   "check": {
    "source": "statistics",
    "field": "operatingMargin",
    "op": "<",
    "value": 56
   }
  },
  {
   "text": "TTM FCF margin falls below 40%, showing the cash gap is structural rather than litigation timing.",
   "check": {
    "source": "statistics",
    "field": "fcfMargin",
    "op": "<",
    "value": 40
   }
  },
  {
   "text": "A final US rule, court decision or law (e.g. the Credit Card Competition Act) materially caps credit interchange or forces network routing choice."
  }
 ],
 "scenarios": {
  "bull": {
   "probability": 0.25,
   "target_price_12m": 760,
   "basis": "P/E re-rates toward its 5y median 35.7x [RA] on earnings lifted by the rising operating margin [IS-T]; above the P/E method's bull fair value 717.46 and far above the FCFE DCF, which misses the network moat."
  },
  "base": {
   "probability": 0.5,
   "target_price_12m": 680,
   "basis": "P/E holds near its 5y low 33.7x [RA] while earnings grow with value-added services `[company-reported]` and buybacks [ST]; above the mechanical range because the DCF is built on a depressed TTM FCF margin of 44.3% [CF-T]."
  },
  "bear": {
   "probability": 0.25,
   "target_price_12m": 470,
   "basis": "Growth slows and the trend premium unwinds, taking the price toward the mechanical bull fair value 471.90 [valuation file], the de-rating risk in the bear case."
  }
 },
 "replaces": null,
 "replacement_reason": null,
 "second_opinion": {
  "file": "research/MA/2026-11-16-evaluation-2.md",
  "conviction": 4
 }
}
```

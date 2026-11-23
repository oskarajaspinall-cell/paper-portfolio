# Evaluation: Wolters Kluwer N.V. (AMS:WKL) — 2026-11-23
## Bear case
The market prices WKL as an information business that generative AI will commoditise: the reverse DCF implies only 0.5% year-1 revenue growth, and the 12-month change is still -9.7% [Certain]. If AI tools erode UpToDate, tax and legal content pricing, today's multiples below their 5-year minimums are a new normal, not a discount [Guessing]. Improvement has plateaued: ROIC is 24.3% TTM against a 2-year high of 25.5%, and operating and FCF margins are flat over the last year [Certain]. Leverage has risen to 2.08x net debt/EBITDA from 1.50x as buybacks outrun cash, and FCF conversion slid to 104.2% from 144.5% [Certain]. The price is 25.7% above its 200-day average after a 21.3% three-month rebound; a slower growth print could de-rate it back toward the June low of 54.64 [Likely]. The nine-month update could not be verified [Certain].
## Bull case
This is a high-quality compounder at a cyclical-style price: ROIC 24.3%, gross margin 74.1% and operating margin 25.5%, with margins higher than five years ago [Certain]. P/E 14.3x, EV/EBITDA 11.6x and P/FCF 13.8x sit below their own 5-year minimums and 36-49% below peers RELX, Thomson Reuters, Verisk and S&P Global, at a 7.27% FCF yield [Certain]. Fair value bear 80.79, base 118.06, bull 130.18 EUR puts the price near the bear end [Certain]. The company is embedding AI into workflow products (Blue Chip IQ, agentic tax prep, an MCP server, the AgileMD deal), turning AI into a product rather than a substitute [Likely]. Shares fell 3.36% year on year via buybacks [Certain]. Beta 0.20 and recurring revenue keep it defensive [Likely]. The pullback from 93.38 came with no adverse company news [Likely].
## Decision
```json
{
  "ticker": "AMS:WKL",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Rolling 12-month ROIC, operating margin and FCF margin are flat (ROIC -0.6pp, operating margin +0.2pp, FCF margin -0.1pp) [RA-T, IS-T, CF-T]; the 5-year trends are rising or flat.", "moat": "narrow", "key_risk": "medium", "key_risk_text": "Generative AI commoditises professional content and erodes pricing; after a 21.3% three-month rebound to 25.7% above the 200-day average, any slowdown would de-rate the stock.", "veto": null},
  "thesis": "A high-return professional-information franchise with stable margins trades below its own 5-year minimum multiples and far below peers, but plateaued returns, rising leverage and unresolved AI-disintermediation risk keep it short of high conviction.",
  "rationale": "Quality is high and the price sits below every own-history multiple minimum, yet the scorecard lands at 3: upside to the value blend falls just short of the top band, leverage is mid-range and AI risk is real. The entry-price dip was a mild pullback, not a re-pricing; good but not compelling.",
  "price_at_decision": 85.88,
  "price_date": "2026-11-20",
  "research_note": "research/AMS-WKL/2026-11-23.md",
  "entry_price": 84.5,
  "entry_basis": "Valuation file: base 118.06 [fact sheet Fair value] blended with this evaluation's expected value gives +28% upside today; near this level it reaches the scorecard's 30% band (conviction 4). The default base x 0.85 sits above the price, so it cannot serve.",
  "triggers": [
    {"text": "TTM ROIC falls below 20%, giving up most of the rise from 18.6% in FY2021 to 24.3%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "TTM operating margin falls below 23%, reversing the five-year expansion and showing AI is forcing price cuts.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 23}},
    {"text": "TTM FCF margin falls below 18%, well under the steady 22.8%, showing cash generation is eroding.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 18}},
    {"text": "Net debt/EBITDA rises above 3.0x (2.08x now), showing buybacks or M&A are being debt-funded beyond a safe level.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 130.18, "basis": "AI products hold pricing and the multiple re-rates toward its 5-year median EV/EBITDA 19.7x [RA], reaching the bull fair value 130.18 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 105, "basis": "Stable margins and buybacks lift the price partway from below its 5-year minimum multiples [RA] toward the DCF base 101.83 and blended base 118.06 [fact sheet Fair value], short of full re-rating while the AI debate persists."},
    "bear": {"probability": 0.25, "target_price_12m": 70, "basis": "AI fears return and multiples stay below their 5-year minimums [RA], taking the price below the DCF bear 76.46 toward the 200-day average 68.32 [ST,HI], as the bear case's de-rating risk."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

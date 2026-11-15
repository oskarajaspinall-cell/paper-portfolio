# Evaluation: United Integrated Services Co., Ltd. (TPE:2404) — 2026-11-15
## Bear case
[Likely] This is a project contractor riding a fab capex boom: gross margin of 22.9% and operating margin of 19.2% sit far above the FY2023 trough of 10.9% and 8.8%, so today's returns look cyclical, not structural. [Likely] FCF at 283.1% of net income is customer advances; it reverses when awards slow, and the FCF margin already fell from 46.7% to 42.1% over 12 months and sits 13.5pp below its 2-year high, while ROCE is 4.9pp below its 2-year high. [Certain] On earnings the stock is only fair: P/E 13.5x vs a 12.5x 5y median, P/B 8.4x at 82% of its range. [Certain] The price is below its 50- and 200-day averages, down 11.7% over 3 months, with results due Nov 19, 2026. [Certain] The mechanical fair value is flagged unreliable (methods disagree 7.5x). [Guessing] Customer concentration in a few chipmakers is unverified.
## Bull case
[Certain] Returns are exceptional and still rising on a 12-month view: TTM ROCE 76.7% vs 61.0% a year earlier, operating margin 19.2% vs 17.6%, ROE 72.7%. [Certain] Net cash every year (net debt/EBITDA -2.64x), dilution minimal (0.41%). [Certain] FCF yield 21.11% and P/FCF 4.7x, below its 5y minimum; EV/EBITDA 7.7x vs peers at 11.3x. [Likely] The FCF dip is a working-capital timing swing from a record level, not a broken model: margins and ROCE are still rising year on year. [Likely] The reverse DCF implies revenue falling 26.6% in year 1, a deep slowdown already priced. [Guessing] Advanced-fab and AI-driven capex keeps the order book full through the next year.
## Decision
```json
{
  "ticker": "TPE:2404",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "FCF margin fell from 46.7% to 42.1% (CF-T,IS-T) and ROCE is 4.9pp below its 2-year high (RA-T), but operating margin and ROCE are still up year on year (IS-T, RA-T) and the company is net cash (BS): a working-capital timing swing from a record level, not lost share.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Margins and FCF are at a cyclical peak tied to customers' fab capex; a slowdown in awards would reverse advance payments and compress margins toward the FY2023 trough (IS), likely within the 12-month horizon.",
    "veto": null
  },
  "thesis": "A net-cash, very high-return cleanroom contractor on a low FCF multiple, but its margins and cash flow are at a cyclical peak tied to customer capex.",
  "rationale": "Quality and balance sheet are excellent and the FCF multiple is low, but the cash flow is the least durable part (advances), earnings multiples are only fair, the price is in a downtrend and the fair value is unreliable. Good but not compelling: AVOID.",
  "price_at_decision": 998.00,
  "price_date": "2026-11-13",
  "research_note": "research/TPE-2404/2026-11-15.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 14%, signalling the capex cycle has turned.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 14}},
    {"text": "FCF margin (TTM) falls below 20%, signalling advance payments are reversing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "ROE (TTM) falls below 40%.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 40}},
    {"text": "The balance sheet moves to net debt (net debt/EBITDA turns positive on the ratios page)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1450, "basis": "Fab awards stay strong and the P/E re-rates toward its 5y max of 19.7x [RA] on rising TTM earnings [IS], retesting the 52-week high of 1,450.00 [HI]."},
    "base": {"probability": 0.45, "target_price_12m": 1080, "basis": "P/E holds near its 5y median of 12.5x [RA] on modestly higher earnings as margins plateau near 19.2% [IS]; the DCF base is ignored because the fair value is flagged unreliable (methods disagree 7.5x) [fact sheet]."},
    "bear": {"probability": 0.30, "target_price_12m": 640, "basis": "Awards slow, margins revert toward the FY2023 8.8% operating margin [IS] and the stock trades near the mechanical bear fair value of 563.93 and the 52-week low of 748.00 [HI]."}
  },
  "entry_price": 750,
  "entry_basis": "Around the 52-week low of 748.00 [HI], where the P/E would sit near the bottom of its 5y range (5y low 8.6x [RA]); the valuation-file base (2,667.94 x 0.8) is unusable because the fair value is flagged unreliable.",
  "replaces": null,
  "replacement_reason": null
}
```

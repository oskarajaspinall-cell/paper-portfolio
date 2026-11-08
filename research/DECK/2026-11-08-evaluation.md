# Evaluation: Deckers Outdoor Corporation (DECK) — 2026-11-08
## Bear case
Management cut the full-year sales outlook and guided Q3 EPS below consensus, citing softer US DTC demand and rival discounting in athletic footwear [Certain]. The Direction change line matters: TTM ROIC fell from 78.5% to 71.9% and sits far below its 2-year high of 118.8%, driven by inventory rising from $487.0 million to $860.8 million in six months [company-reported] ahead of softer demand [Likely]. If that stock clears through markdowns, gross margin (58.9% TTM) and FCF margin would follow ROIC down [Guessing]. TTM earnings are flattered by non-recurring IEEPA tariff refunds of about $46,000k [company-reported], so 11.4x P/E is less cheap than it looks [Certain]. Net cash is shrinking (net debt/EBITDA -0.48x vs -1.14x at FY2026) as buybacks outrun cash flow [Certain]. Short interest is rising [Certain]. Macro is context only: no single foreign country is ~10%+ of sales, so country risk is low [Certain].

## Bull case
The slowdown has not reached profitability: TTM operating margin is flat at 23.6%, FCF margin flat at 18.9% and ROCE rose to a 2-year high of 45.7% [Certain]. The ROIC slide is an invested-capital (seasonal inventory) effect, not margin erosion [Likely]. The stock trades below its own 5-year minimum P/E, EV/EBITDA, EV/Sales and P/FCF, 30% under the peer P/E median, at a 9.09% FCF yield [Certain]. The reverse DCF prices -1.2% revenue growth while the cut outlook still implies growth [Likely]. Shares fell 6.97% year on year, and buybacks at roughly 11x earnings are accretive [Likely]. Base fair value of 112.86 sits well above the price [Certain]. UGG and HOKA brand strength is only partly tested by one soft quarter [Guessing].

## Decision
```json
{
  "ticker": "DECK",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A net-cash, high-return footwear brand owner with flat-to-rising margins and ROCE trades below its own 5-year minimum P/E, EV/EBITDA and P/FCF at a 9.09% FCF yield, pricing a revenue decline that its slowed-but-positive outlook does not show.",
  "rationale": "Margins, FCF and ROCE held through the guidance cut; the ROIC fall is inventory-driven, and valuation already prices shrinkage. Inventory markdown risk and tariff-flattered earnings stop an ADD at 5. The position sits near its conviction-4 size, so HOLD.",
  "price_at_decision": 86.71,
  "price_date": "2026-11-06",
  "research_note": "research/DECK/2026-11-08.md",
  "triggers": [
    {"text": "TTM gross margin falls below 55%, under the FY2024 level of 55.6%, showing rival discounting or inventory markdowns are eroding full-price discipline.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}},
    {"text": "TTM operating margin falls below 20%, reversing most of the five-year expansion from 18.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 14%, showing the inventory build is turning into cash and margin stress rather than a seasonal swing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 14}},
    {"text": "Net sales on the income statement page decline year on year for two consecutive quarters, signalling HOKA and UGG brand fade rather than a soft patch."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 140, "basis": "Growth re-accelerates and P/E re-rates toward its 5y median 17.6x [RA]; set below the mechanical bull of 182.96 [fact sheet Fair value] because TTM earnings include non-recurring tariff refunds (note section 6)."},
    "base": {"probability": 0.5, "target_price_12m": 105, "basis": "Operating margin holds near 23.6% and FCF margin near 18.9% [IS-T, CF-T] while P/E recovers toward its 5y minimum 13.9x [RA]; set below the mechanical base of 112.86 to reflect the cut sales outlook and inventory markdown risk (note sections 2 and 5)."},
    "bear": {"probability": 0.25, "target_price_12m": 67.01, "basis": "Rival discounting forces inventory markdowns and margins fall back: the P/E bear value of 67.01 [fact sheet Fair value]; above the blended bear of 38.06 because net cash and a 9.09% FCF yield [ST] make the DCF bear's sustained decline unlikely."}
  },
  "entry_price": null,
  "entry_basis": "Already conviction 4 at the current price; the obstacle to conviction 5 is inventory and tariff-flattered earnings risk, not price.",
  "replaces": null,
  "replacement_reason": null
}
```

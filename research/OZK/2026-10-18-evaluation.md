# Evaluation: Bank OZK (OZK) — 2026-10-18
## Bear case
The discount reflects a specific, unresolved credit event, not neglect. The "largest credit" missed its original maturity and was extended, and the bank had to answer inquiries about it in a regulatory filing [Certain] (fact sheet news, OV). RESG concentration means one or two outsized construction loans can move earnings [Likely]. Short interest is 17.5% of float and still rising (+6.6% vs the prior month) [Certain] (ST), and Piotroski F is only 4 [Certain] (ST). Net margin has fallen from 50.5% (FY2023) to 44.5% TTM and ROE to 11.3% [Certain] (IS, RA). Real yields up and HY spreads widening raise CRE refinancing stress (macro overlay) [Likely]. Q3 results on Oct 20, 2026 can settle the credit question either way; buying two sessions before a binary disclosure is guessing, not analysis [Likely]. The P/B + ROE fair value assumes losses stay at historical norms, exactly the point in doubt [Likely].

## Bull case
OZK is cheap on every measure: P/E 7.6x vs a 10.8x peer median, P/B 0.8x at the bottom of its own 0.8x-1.2x 5y range, P/FCF 6.6x and a 15.16% FCF yield [Certain] (RA, ST). The reverse DCF prices -12.6% year-1 revenue, which already embeds real credit losses [Certain] (valuation). Even the mechanical bear fair value of 74.95 sits well above the 46.12 close [Certain]. ROE has held in an 11.8%-14.1% band for five years and FCF conversion is 110.3% TTM [Certain] (RA, CF). Capital returns are real: shares down 2.16% YoY, a new buyback programme and sixty-five consecutive quarterly dividend increases [Certain] (ST, OV). If Q3 shows the extended credit performing, a crowded short could cover and the stock re-rate toward its own 1.0x median P/B [Guessing].

## Decision
```json
{
  "ticker": "OZK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A statistically cheap, high-cash-conversion regional bank whose discount is explained by an unresolved single-credit concentration event that Q3 2026 results will clarify.",
  "rationale": "Valuation is compelling but the obstacle is not price: the extended largest RESG credit, rising short interest, weak Piotroski score and a falling net margin leave the key risk unresolved two sessions before Q3 results. Good but not compelling is an AVOID; re-research after the Oct 20 disclosure.",
  "price_at_decision": 46.12,
  "price_date": "2026-10-16",
  "research_note": "research/OZK/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROE falls below 10%, showing provisioning on the RESG book is outrunning earnings power.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "TTM net margin falls below 40%, showing large-credit losses reaching the P&L.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 40}},
    {"text": "TTM FCF margin falls below 40%, signalling cash earnings quality deteriorating as nonaccruals build.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 40}},
    {"text": "The Q3 2026 or later earnings release / SEC filing shows the extended largest credit performing or repaid with no material charge-off, which would lift conviction (re-research)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 60.0, "basis": "Q3 disclosure resolves the largest credit and P/B re-rates toward its own 5y median 1.0x [RA], still below the 74.95 mechanical bear fair value because the peer discount narrows only partly."},
    "base": {"probability": 0.45, "target_price_12m": 50.0, "basis": "Credit overhang lingers, P/B stays near 0.8x [RA] while ROE around 11.3% [RA] and buybacks (shares -2.16% YoY [ST]) accrete book; well below the 84.00 base fair value, which assumes the concentration risk never crystallises."},
    "bear": {"probability": 0.30, "target_price_12m": 36.0, "basis": "The largest RESG credit takes a material loss and ROE breaks below 10%, pushing the stock under its 52-week low of 42.37 [HI]; probability tilted small toward bear per the macro overlay's rising real yields and widening HY spreads (research/OZK/2026-10-18-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades far below even the 74.95 bear fair value; the unresolved largest-credit event is. A lower price would not change the decision; re-research on the Q3 2026 disclosure instead.",
  "replaces": null,
  "replacement_reason": null
}
```

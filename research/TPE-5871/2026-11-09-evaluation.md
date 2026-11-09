# Evaluation: Chailease Holding Company Limited (TPE:5871) — 2026-11-09
## Bear case
ROE halved over five years, from 21.0% (FY2021) to 11.0% (FY2025), and ROIC fell from 3.9% to 2.2% [RA] [Certain]. The rolling-12-month ROIC is flat at 2.3% but still below its 2.7% two-year high [RA-T] [Certain]; no Direction change line is printed. The decline is not yet shown to be temporary: no guided reset, one-off or investment phase is documented in the note, and for a lender the likeliest cause, credit costs and funding spreads in China and ASEAN, cannot be checked because margins, leverage and credit data are [data unavailable] [Likely]. China exposure is unsized and its regulation and policy rates are unverified (macro overlay) [Certain]. The cheap P/E of 9.1x and P/B of 0.9x [RA] may simply price a lower-return business, a value trap [Likely]. Results on Nov 12 are a near-term binary event [Certain].
## Bull case
The stock trades below its own 5-year minimum on P/E (9.1x vs 9.4x), P/B (0.9x vs 0.9x low) and P/FCF (8.0x vs 9.2x) [RA], with a 12.55% FCF yield [ST] [Certain]. The mechanical bear fair value of 104.79 TWD sits above the 102.00 close [fact sheet Fair value] [Certain]. The fall in returns appears to have stopped: TTM ROE of 11.3% is slightly above FY2025 and ROIC is flat year on year [RA, RA-T] [Likely], which looks more like a trough than an ongoing slide. An 11% ROE bought below book is a reasonable return even with no recovery [Likely]. There is no dilution (shares -0.23% YoY [ST]) and beta is 0.67 [Certain]. If credit costs normalise, a re-rating toward the 12.7x median P/E is plausible [Guessing].
## Decision
```json
{
  "ticker": "TPE:5871",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A regional leasing lender trading below its own 5-year minimum P/E and P/B on a stabilised 11% ROE, but the cause of the five-year halving of returns (likely China/ASEAN credit costs) cannot be verified from available data, so the cheapness cannot yet be judged temporary rather than structural.",
  "rationale": "The recent direction is not the obstacle: ROIC is flat and ROE has stopped falling. The obstacle is evidence. For a lender, credit costs, leverage and China exposure are unavailable, so whether the decline is a cyclical trough or a permanently lower-return book is unknown. Cheap but unverifiable: conviction 3, AVOID; re-research after the Nov 12 results.",
  "price_at_decision": 102.00,
  "price_date": "2026-11-06",
  "research_note": "research/TPE-5871/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE falls below 10% (11.3% now), showing the return decline has resumed and is structural rather than a trough.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 2.0% (2.3% now, flat year on year), breaking the stabilisation.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 2.0}},
    {"text": "Shares outstanding rise more than 3% year on year, signalling capital raising to cover credit losses.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 3}},
    {"text": "The Nov 12 results or a company filing disclose rising credit costs or a China-related loss, or conversely show credit costs falling with ROE recovering toward the FY2024 13.5%: either resolves the structural-vs-cyclical question and warrants re-research."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 143.95, "basis": "Credit costs normalise and P/E re-rates to around its 5y median 12.7x [RA] on TTM earnings, matching the mechanical bull fair value of 143.95 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 115.0, "basis": "ROE holds near 11.3% TTM [RA] and P/E recovers only partway from 9.1x; below the mechanical base of 142.28 because that applies a median multiple earned when ROE was 16.6%-21.3% [RA]; macro weight is context only (research/TPE-5871/2026-11-08-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 85.0, "basis": "ROE slips below 10% on China/ASEAN credit stress (unsized exposure, research/TPE-5871/2026-11-08-macro.md) and P/B stays at its 0.9x low [RA] on a smaller earnings base; below the mechanical bear of 104.79, which assumes TTM earnings hold."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below its 5y minimum P/E and P/B and below the default anchor (base 142.28 x 0.8). What is missing is evidence on credit quality and China exposure; a lower price would not change the decision, the Nov 12 results or credit-cost disclosure would.",
  "replaces": null,
  "replacement_reason": null
}
```

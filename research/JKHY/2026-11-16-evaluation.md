# Evaluation: Jack Henry & Associates, Inc. (JKHY) — 2026-11-16
## Bear case
The mechanical fair value (base 123.97, bear 94.47) sits well below the 177.67 close, and the reverse DCF needs 13.6% year-1 revenue growth, above the 8% framework management cites [Certain]. The stock is +15.4% above its 200-day average with RSI 69.2 after a +27.7% six-month run: an extended price risks a de-rating if growth slows to framework or AI, cloud and security costs (a stated margin headwind) bite [Likely]. The Direction change line shows ROIC falling over five fiscal years (24.9% to 23.6%); if FY2024's 19.1% trough recurs, the multiple compresses [Guessing]. Multiples remain far above peers (P/E +90%) [Certain]. Short interest is rising (+5.9% month on month) [Certain]. Deconversion fees flatter results and are lumpy [Likely].
## Bull case
The franchise is high-return and unlevered: TTM ROIC 23.8%, operating margin 25.6%, FCF margin 27.6%, net debt/EBITDA 0.13x [Certain]. The five-year ROIC slide bottomed in FY2024 and the last 12 months are a recovery (21.8% to 23.8%), with FCF margin up 3.0pp; this was a temporary reset, not a structural decline [Likely]. Switching costs on core processing keep community-bank clients for multi-year terms [Likely]. Q1 FY27 brought nine core wins and raised FY27 guidance [Likely]. P/E, EV/EBITDA and P/FCF sit in the lower third of their own 5y ranges (P/FCF at 15%), with a 5.80% FCF yield [Certain]. The P/E method's base of 230.66 shows the DCF may understate a compounding business [Guessing].
## Decision
```json
{
  "ticker": "JKHY",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Nothing is falling over 1 or 3 years: ROIC +2.1pp over the last 12 months and +4.8pp over 3 years [RA-T], FCF margin +3.0pp [CF-T]. The 5-year fiscal ROIC dip to the 19.1% FY2024 trough reflected investment and acquisition costs since absorbed (https://www.sec.gov/Archives/edgar/data/779152/000077915226000098/jkhy-20260930.htm).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "De-rating of an extended price (+15.4% above the 200-day average, reverse DCF needing 13.6% growth) if revenue growth stays at the 8% framework or AI/cloud/security costs compress margins.",
    "veto": null
  },
  "thesis": "A high-return, unlevered core-banking franchise with switching-cost retention and recovering rolling returns, trading in the lower third of its own 5-year multiples but at a price implying growth above the company's framework.",
  "rationale": "Quality, balance sheet and the last-12-month direction are strong, and own-history multiples are low, but the price already implies growth above the 8% framework and sits extended above its 200-day average. The scorecard gives conviction below the buy bar, so hold at the conviction-3 size; no new evidence since the 2026-11-15 HOLD.",
  "price_at_decision": 177.67,
  "price_date": "2026-11-13",
  "research_note": "research/JKHY/2026-11-16.md",
  "triggers": [
    {"text": "TTM ROIC falls below 19%, the FY2024 trough, evidencing moat erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 19}},
    {"text": "TTM operating margin falls below 22%, the FY2024 low, showing AI/cloud/security costs are not being absorbed.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 22}},
    {"text": "TTM FCF margin falls below 22%, losing the cash-conversion recovery.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 22}},
    {"text": "A 10-Q/10-K reports an accelerating loss of core clients, with deconversion revenue persistently above recent levels (SEC filing, MD&A)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 230.66, "basis": "P/E re-rates toward its 5y median 31.7x [RA] as core wins and raised FY27 guidance sustain growth, matching the P/E method's base fair value 230.66 (fact sheet Fair value)."},
    "base": {"probability": 0.45, "target_price_12m": 191.88, "basis": "P/E holds near the current 24.5x [RA] while earnings grow with the 8% revenue-growth framework (KBW transcript headline [OV]); above the DCF base 123.97 because the DCF ignores the switching-cost moat and the FCF margin recovery [CF-T]."},
    "bear": {"probability": 0.30, "target_price_12m": 141.64, "basis": "Growth slows to framework and the extended price de-rates toward the 5y P/E low 19.5x [RA], the P/E method's bear 141.64; not the DCF bear 94.47, which the P/E method disagrees with by a wide margin."}
  },
  "entry_price": 145.65,
  "entry_basis": "P/FCF back at its 5y low of 14.1x [RA] from 17.2x today; at that level the same quality evidence would carry discount points for conviction 4. The default base 123.97 x 0.8 is not used because the DCF and P/E methods disagree widely.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: China Resources Sanjiu Medical & Pharmaceutical (SHE:000999) — 2026-11-08
## Bear case
Capital efficiency has fallen sharply: ROIC went from 17.7% in FY2024 to 13.8% in FY2025 and 10.4% TTM, ROCE from 15.8% to 10.3% [Certain]. Operating margin stayed flat, so the cause looks like a larger capital base, probably acquired, earning less than the legacy business. Neither the note nor the fact sheet identifies that cause [Guessing]. The Direction change lines show only a partial rebound: TTM ROIC is up from 9.1% but still 7.1pp below its 17.5% two-year high, and FCF margin is 2.9pp below its 14.2% high [Certain]. The recovery is one year old and not yet proven, so it threatens a thesis built on returns going back to their old level [Likely]. Net margin has fallen to 10.4% [Certain]. Volume-based procurement and drug-pricing policy are a standing risk [Likely]. The Q3 2026 report was not read, the moat is unevidenced, and the 50-day average sits below the 200-day [Certain].
## Bull case
The stock is cheap on every measure. P/E 13.4x, EV/EBITDA 9.5x and P/B 1.1x are all below their own 5-year minimums, and peers trade at a P/E of 29.5x [Certain]. The reverse DCF implies only 2.6% year-1 revenue growth, and the base fair value of 34.55 already includes a 3.5% China risk premium [Certain]. The balance sheet is net cash (-0.61x), FCF conversion is 108.1% TTM, FCF yield is 8.07% and the Piotroski score is 7 [Certain]. The last 12 months show returns turning: operating margin rose from 12.3% to 14.2% and ROCE from 8.7% to 10.3% [Certain]. If the step-down was an acquisition being absorbed, returns may rebuild toward the mid-teens while the price assumes they don't [Guessing]. Gross margin of 55.6% TTM suggests pricing power is intact [Likely].
## Decision
```json
{
  "ticker": "SHE:000999",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash Chinese branded-medicine maker trades below its own 5-year minimum multiples with an 8.07% FCF yield, but its ROIC has fallen from 17.7% to 10.4% for a reason the research has not identified, so the cheapness may reflect a lasting step-down in returns rather than a mispricing.",
  "rationale": "Valuation and balance sheet are attractive, but the drop in returns has no identified cause, the Q3 report was not read and the moat is unevidenced. One year of rebound does not prove that returns will recover. That makes this good but not compelling: conviction 3, AVOID. Watch for a cheaper price that prices the bear case, or proof that ROIC is recovering.",
  "price_at_decision": 25.95,
  "price_date": "2026-11-06",
  "research_note": "research/SHE-000999/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC rises above 13% (10.4% now), showing the step-down in returns is reversing rather than structural.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 13}},
    {"text": "TTM FCF margin rises above 13.4% (the FY2025 level; 11.2% now), confirming cash generation is back near its two-year high.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 13.4}},
    {"text": "TTM operating margin falls below 12% (14.2% now), which would show procurement or pricing pressure reaching profitability and remove the case entirely.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 12}},
    {"text": "A company filing explains the ROIC decline as acquisition integration with returns guided to recover, and shows no material volume-based-procurement price cuts to key products."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 38.0, "basis": "ROIC keeps recovering from 10.4% toward its 17.5% two-year high [RA-T] and P/E re-rates beyond its 5y median 16.9x [RA]; set below the mechanical bull of 50.08 because the cause of the returns step-down is unidentified."},
    "base": {"probability": 0.45, "target_price_12m": 29.5, "basis": "Operating margin holds near the TTM 14.2% [IS-T] and P/E recovers partway from 13.4x toward its 5y minimum-to-median range of 13.8x-16.9x [RA]; set below the mechanical base of 34.55 because that DCF assumes returns the last two fiscal years did not deliver."},
    "bear": {"probability": 0.30, "target_price_12m": 20.80, "basis": "Returns stay depressed and procurement pricing pressure trims margins (note section 6), giving the mechanical bear fair value of 20.80 [fact sheet Fair value], near the 52-week low of 21.60 [HI]."}
  },
  "entry_price": 21.60,
  "entry_basis": "The default anchor (base 34.55 x 0.8) is above the price, so the obstacle is the unexplained drop in returns, not valuation. At the 52-week low of 21.60 [HI], near the mechanical bear fair value of 20.80, the price would already reflect the bear case, which would justify conviction 4 on the same evidence.",
  "replaces": null,
  "replacement_reason": null
}
```

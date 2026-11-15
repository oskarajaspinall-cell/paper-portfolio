# Evaluation: Halozyme Therapeutics (HALO) — 2026-11-15
## Bear case
Returns are rolling over: TTM ROIC fell from 44.2% to 29.8% and ROCE from 53.3% to 34.1% in a year, with operating margin down 2.7pp [Certain]. The cause looks like a larger, debt-funded, acquisition-enlarged capital base (Elektrofi, Surf Bio), not price pressure, but that means the new assets must earn their keep [Likely]. Revenue rests on a few partners (Roche, Janssen, argenx) and on the MDASE patent fight with Merck; losing it on invalidity would cut the long-dated royalty runway [Likely]. The mechanical fair value (EV/Revenue only, base 87.33) sits below the 100.27 price [Certain], so the score leans on trend strength: the stock is 17.4% above its 200-day average after a 42.0% year, and a growth slowdown could de-rate it further, as the fall from 134.00 already shows [Likely]. Short interest is 12.11% of float [Certain]. Net debt/EBITDA rose to 1.93x [Certain].

## Bull case
This is a royalty toll-road: 76.0% gross margin, 56.7% operating margin, 49.1% FCF margin and FCF/NI of 182.5% [Certain]. Q3 2026 royalties were $341,001k [company-reported] and FY2026 guidance was raised (https://www.prnewswire.com/news-releases/halozyme-reports-third-quarter-2026-results-and-raises-full-year-2026-financial-guidance-302931338.html) [Certain]. A new FDA approval (Rybrevant Faspro, head and neck) adds a royalty line, and management reaffirmed zero to minimal CMS royalty impact through at least 2035 [Likely]. FCF margin rose 0.7pp over the year, so the ROIC fall is capital growth, not weaker economics [Likely]. Valuation is undemanding: P/FCF 12.9x sits at 3% of its 5y range, EV/EBITDA 12.0x at 13% and both 21% below peers, with a 7.75% FCF yield [Certain]. Buybacks cut shares 2.62% YoY [Certain]. The fall from 134.00 left RSI at 26.7 with no confirmed business cause [Guessing].

## Decision
```json
{
  "ticker": "HALO",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "ROIC/ROCE and operating margin fell over 12 months as the capital base grew with the Elektrofi/Surf Bio acquisitions and new convertible debt (note §2, §5; 10-Q https://www.sec.gov/Archives/edgar/data/1159036/000115903626000145/halo-20260930.htm), while FCF margin rose 0.7pp [CF-T] and Q3 royalties hit a record with FY2026 guidance raised (https://www.prnewswire.com/news-releases/halozyme-reports-third-quarter-2026-results-and-raises-full-year-2026-financial-guidance-302931338.html).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "Loss of the Merck MDASE patent case on invalidity, or partner concentration, shortening the royalty runway; plus de-rating from an extended price if royalty growth slows.",
    "veto": null
  },
  "thesis": "A high-margin ENHANZE royalty stream with a raised 2026 guide trades at the low end of its own P/FCF and EV/EBITDA history.",
  "rationale": "Excellent royalty economics and a raised guide, but the scorecard gives conviction 3: the value blend shows no discount, returns fell as the capital base grew, and the Merck patent case is unresolved. Good but not compelling, so AVOID; cash is an acceptable outcome. Re-examine at the entry price.",
  "price_at_decision": 100.27,
  "price_date": "2026-11-13",
  "research_note": "research/HALO/2026-11-15.md",
  "triggers": [
    {"text": "TTM gross margin falls below 70%", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 70}},
    {"text": "TTM FCF margin falls below 40%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 40}},
    {"text": "Net debt / EBITDA rises above 3.0x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.0}},
    {"text": "Company-reported royalty revenue declines year on year in a 10-Q, or the Merck MDASE litigation ends with the patent held invalid"}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 140.0, "basis": "Raised guidance is delivered and new Enhanze approvals (Rybrevant Faspro) keep royalties compounding, retaking the 134.00 high [HI] toward the mechanical bull 172.15 [fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 112.0, "basis": "EV/EBITDA drifts from 12.0x toward its 5y median 14.2x [RA] as royalty growth holds; above the EV/Revenue base 87.33 because that single method ignores the 49.1% FCF margin [CF-T]."},
    "bear": {"probability": 0.25, "target_price_12m": 74.3, "basis": "An adverse US ruling in the Merck MDASE case or slowing royalties de-rates the stock to the mechanical bear 74.30 [fair value]."}
  },
  "entry_price": 69.86,
  "entry_basis": "valuation file: base 87.33 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

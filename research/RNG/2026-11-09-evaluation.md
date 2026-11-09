# Evaluation: RingCentral, Inc. (RNG) — 2026-11-09
## Bear case
The stock has run 163.9% in 12 months and now sits close to its base fair value of 75.85, so most of the re-rating is already paid for [Certain]. The 9.5x P/E is an illusion: net margin of 25.3% against an 8.4% operating margin reflects a one-off release of $544.9 million of tax valuation allowance [company-reported] [Certain]. ROCE fell from 33.0% to 18.5% over the last year and ROIC is 11.4pp below its 2-year high of 35.4%; the note attributes this to capital-base and tax effects rather than operations, which is plausible but unproven [Likely]. Competition from Microsoft, Zoom and AI-agent disruption, plus reliance on third-party LLMs, threatens a seat-based UCaaS model [Likely]. EV/EBITDA of 15.7x is above the peer median of 14.9x, P/B is 32.5x, and Altman Z of 2.22 says leverage is not trivial [Certain]. Upside to base is thin [Likely].

## Bull case
Operations are improving: operating margin is 8.4% TTM, a 2-year high, up from 4.3% a year earlier; FCF margin is 25.5%, also a 2-year high; gross margin is steady at 72.2% [Certain]. P/FCF of 9.1x sits at 4% of its 5y range and below the peer median of 11.8x, with a 10.96% FCF yield [Certain]. Q3 beat and FY guidance was raised, with paid AI ARR doubling per the call summary [Likely]. Net debt/EBITDA has fallen to 2.10x from 3.25x at FY2025, notes are being repurchased, and shares are down 5.00% YoY [Certain]. The reverse DCF implies only 2.4% year-1 revenue growth, a low bar for a business compounding FCF [Likely]. Switching costs in communications and contact-centre software support retention [Likely]. Bull fair value of 96.16 is near the 52-week high of 98.14 [Certain].

## Decision
```json
{
  "ticker": "RNG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "ROIC, operating margin and FCF margin are all higher than a year earlier (RA-T, IS-T, CF-T); the ROCE and ROIC distance from the Dec-2025 peak reflects the capital base and the one-off tax valuation-allowance release, not operations (note section 2, 10-Q).",
    "moat": "narrow",
    "key_risk": "medium",
    "key_risk_text": "AI-agent disruption and competition from Microsoft/Zoom erode seat-based UCaaS pricing and retention (10-Q risk factors).",
    "veto": null
  },
  "thesis": "A deleveraging cloud-communications company with record FCF margins trading at a low P/FCF, but the price already sits near base fair value after a large re-rating.",
  "rationale": "Quality and cash generation are genuinely improving and P/FCF is low versus history and peers, but the mechanical base fair value offers little upside after the 12-month run, competitive AI risk is real, and the scorecard does not reach the buy bar. Good but not compelling: AVOID, with an entry price at base fair value less the margin of safety.",
  "price_at_decision": 72.07,
  "price_date": "2026-11-06",
  "research_note": "research/RNG/2026-11-09.md",
  "triggers": [
    {"text": "Operating margin TTM falls below 6%", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 6}},
    {"text": "FCF margin TTM falls below 20%", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Gross margin falls below 68%", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 68}},
    {"text": "Net debt / EBITDA rises above 3.25x (FY2025 level)", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.25}}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 96.16, "basis": "FCF margin keeps rising from its 25.5% 2-year high [CF-T] and AI ARR growth sustains raised guidance (Q3 transcript), reaching the mechanical bull fair value 96.16 [fact sheet Fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 75.85, "basis": "Margins hold near current levels and the price converges to the mechanical base fair value 75.85, consistent with the reverse DCF's 2.4% implied growth [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 54.5, "basis": "AI-agent competition caps growth and EV/Sales falls back toward its 5y median 2.2x [RA], matching the EV/Revenue method's base 54.50; the DCF bear (negative) is disregarded as unreliable."}
  },
  "entry_price": 60.68,
  "entry_basis": "valuation file: base 75.85 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

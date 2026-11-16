# Evaluation: Otis Worldwide Corporation (OTIS) — 2026-11-16
## Bear case
The mechanical fair value sits below the price: base 68.86 vs a 77.50 close, with the DCF at 57.20; the price already implies 7.3% year-1 revenue growth [Certain]. Operating margin fell from 16.5% to 15.5% over 12 months, which the 10-Q puts down to labour and commodity costs, and FY26 guidance was only held amid China weakness and service investment costs [Likely]. ROIC is 37.7pp below its 2-year high of 95.6% (2024-09-30), so the headline returns are off their peak [Certain]. Leverage keeps rising, net debt/EBITDA 3.12x from 2.48x in FY2023, while buybacks continue [Certain]. China is a material, unsized exposure in new equipment [Likely], and the CEO retires in H1 2027 [Likely]. The price is only 2.4% above its 200-day average after a -11.9% year; if service growth slows, the multiple has no history of re-rating up from here [Guessing].
## Bull case
Otis is a high-return, recurring business: ROIC 58.0% TTM and about 67% of nine-month sales from Service [company-reported] [Certain]. The installed base and maintenance contracts are hard to displace [Likely]. Q3 organic sales rose 6% with 20% modernization growth and new equipment returning to growth (call transcript, fact sheet) [Likely]. FCF margin recovered from 9.2% to 11.1% over 12 months and FCF conversion is 107.5% [Certain], so the margin dip looks like cost timing and investment rather than a broken model [Likely]. On its own history the stock is cheap: P/E 19.4x, EV/EBITDA 15.0x and P/FCF 17.9x all sit below their 5y minimums, and below peer medians [Certain]. FCF yield is 5.60% and shares fell 2.60% YoY [Certain]. RPO of about $19.6 billion [company-reported] supports visibility [Likely].
## Decision
```json
{
  "ticker": "OTIS",
  "decision": "TRIM",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating margin fell 16.5% -> 15.5% TTM; the Q3 10-Q attributes the gross margin fall to labour and commodity costs partly offset by service mix, and the Q3 call cites service investment costs (https://www.sec.gov/Archives/edgar/data/1781335/000178133526000127/otis-20260930.htm). FCF margin rose 9.2% -> 11.1% over the same 12 months and ROIC rose +6.8pp, so the model is intact.",
    "moat": "wide",
    "key_risk": "medium",
    "key_risk_text": "China new-equipment weakness plus labour/commodity cost pressure keep margins sliding while leverage (3.12x net debt/EBITDA) rises; with the price only modestly above its 200-day average, slower growth would leave the multiple at the bottom of its range.",
    "veto": null
  },
  "thesis": "A wide-moat elevator service franchise trading below its own 5y multiple range, but the DCF-based fair value sits under the price and margins and leverage are moving the wrong way, so it is held below the buy bar.",
  "rationale": "Same evidence as the 2026-11-08 TRIM 3: excellent quality and multiples below their 5y range, but the base fair value is under the price, operating margin is slipping and leverage exceeds 3x. Keep it at no more than the conviction-3 size, which it already roughly sits at; no ADD.",
  "price_at_decision": 77.50,
  "price_date": "2026-11-13",
  "research_note": "research/OTIS/2026-11-16.md",
  "triggers": [
    {"text": "Operating margin falls below 14.0% (statistics page), showing cost inflation is outrunning service mix and pricing.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 14.0}},
    {"text": "Gross margin falls below 28.5% (statistics page).", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 28.5}},
    {"text": "Net debt / EBITDA (ratios page) rises above 3.6x, i.e. buybacks funded by debt beyond what the cash flow supports."},
    {"text": "A filing or results release reports Service organic sales growth turning negative or a Service margin decline, breaking the recurring-revenue thesis."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 92.18, "basis": "Service and modernization growth (Q3 call [OV]) lets EV/EBITDA recover toward its 5y median 17.3x [RA], the EV/EBITDA method value 92.18 in the fair value table."},
    "base": {"probability": 0.5, "target_price_12m": 76.00, "basis": "Guidance held but margins flat, multiples stay below their 5y range [RA]; the 5.60% FCF yield [ST] supports the price between the DCF 57.20 and EV/EBITDA 92.18 values."},
    "bear": {"probability": 0.25, "target_price_12m": 55.33, "basis": "China weakness and cost pressure push operating margin further below 15.5% [IS-T] with leverage at 3.12x [BS,IS]; the price falls to the mechanical bear fair value 55.33."}
  },
  "entry_price": 55.09,
  "entry_basis": "valuation file: base 68.86 x 0.8",
  "replaces": null,
  "replacement_reason": null
}
```

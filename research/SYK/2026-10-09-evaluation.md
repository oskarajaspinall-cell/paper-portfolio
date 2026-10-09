# Evaluation: Stryker Corporation (SYK) — 2026-10-09
## Bear case
The 25% de-rating has not made SYK cheap: the $276.97 close sits on the $271 base fair value, and the model range is skewed down (bear -35.1% vs bull +14.2%) [Certain]. The reverse DCF still requires 12.8% year-1 revenue growth [Certain]. SYK trades 28-91% above the ZBH/MDT/BSX/ISRG peer median on every multiple, so being below its own 5y range is not a margin of safety [Certain]. The September disclosure of persisting peripheral vascular problems, after which the shares fell 8.8% in a day, is unresolved into Q3 results on Oct 29 [Likely]. A CEO handover from 1 January 2027 adds execution risk [Likely]. Real yields are up 0.61pp in 3 months, which pressures premium multiples (macro overlay, small tilt toward bear) [Likely]. Momentum is weak: -40.6pp vs SPY over 12 months [Certain].

## Bull case
This is a high-quality franchise whose fundamentals are improving while the stock falls [Certain]. Operating margin has reached 23.8% TTM (+1.5pp over 5 years), FCF margin 18.2% and ROCE 14.9% [Certain]. FCF conversion of 126% and net debt/EBITDA falling to 1.62x fund bolt-on M&A such as ZuriMED without dilution (shares +0.05% YoY) [Certain]. Every multiple is below its own 5-year minimum (P/E 28.7x vs a 35.9x low), and the P/E-based fair value of $399.57 implies room for a re-rating if the vascular issue proves contained [Likely]. Mako robotics and capital equipment create surgeon switching costs that protect the recurring implant revenue [Likely]. A Piotroski score of 7 and an Altman Z of 5.21 show no balance-sheet stress [Certain]. The CEO succession is planned and internal [Likely].

## Decision
```json
{
  "ticker": "SYK",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality med-tech franchise with rising margins and falling leverage trades at its own base fair value and well above peers, with an unresolved vascular product issue and a CEO change, so the price does not yet pay for the risk.",
  "rationale": "Quality is real and improving, but the price sits on base fair value with a downward-skewed range. It still implies 12.8% growth and a premium to peers. The vascular issue is unresolved into Q3, and rising real yields add a small bear tilt. Good but not compelling, so we avoid it and wait for a margin of safety.",
  "price_at_decision": 276.97,
  "price_date": "2026-10-08",
  "research_note": "research/SYK/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, under the FY2022 5-year low of 11.8%, signalling genuine return erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 19%, under the FY2022 5-year low of 19.3%, reversing the margin expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 19}},
    {"text": "TTM FCF margin falls below 11%, the FY2022 5-year low, showing cash conversion has deteriorated.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 11}},
    {"text": "The peripheral vascular issue disclosed in September 2026 becomes a formal recall or FDA warning letter, per an SEC filing or company statement."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 316.25, "basis": "The vascular issue proves contained and rising margins (operating margin 23.8% TTM [IS]) support the fact sheet's bull fair value of 316.25, still below the P/E method's 399.57, because the peer premium caps the re-rating [RA]."},
    "base": {"probability": 0.5, "target_price_12m": 271.0, "basis": "The price stays anchored to the base fair value of 271.00 (DCF/P-E blend [IS,CF,RA]), with the peer premium (P/E 28.7x vs a 21.6x peer median [RA]) limiting any re-rating; the macro overlay's small bear tilt takes 0.05 from bull."},
    "bear": {"probability": 0.3, "target_price_12m": 179.78, "basis": "The vascular problems persist (8.8% one-day fall, prnewswire.com 2026-10-01 headline [OV]) and real yields keep rising (macro overlay, small tilt toward bear), compressing the multiple toward the bear fair value of 179.78."}
  },
  "entry_price": 216.8,
  "entry_basis": "valuation file: base 271.00 x 0.8 = 216.80 (fact-sheet fair value [IS,BS,CF,RA,ST,HI]). At that price the downside to the bear fair value narrows and the peer premium largely closes, which would justify conviction 4 if the vascular issue stays contained.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Comcast Corporation (CMCSA) — 2026-10-08
## Bear case
The cheapness reflects a business that is shrinking, not a mispricing. Domestic broadband revenue fell to $6.3bn from $6.6bn YoY in Q2 2026 as fiber and fixed-wireless take share [Certain] (SEC 10-Q). Operating margin has slid from 18.8% (FY24) to 14.7% TTM, and ROIC (8.1%) has not compounded in five years [Certain] [IS][RA]. The 27.5% FCF yield is flattered: FCF/NI of 182.5% TTM reflects working-capital timing, not a run rate [Likely] [CF]. The NBCUniversal separation (mid-2027, unfinalized) will reallocate 2.43x net debt/EBITDA and dividend capacity on unknown terms [Likely]. Altman Z of 1.40 and 10y yields at 5.27% (+0.72pp/3m) raise refinancing risk into the split [Certain] (macro overlay). The stock is -32.6% over 12 months with RSI 23.0 and Q3 results on 22 Oct: there is no catalyst yet that breaks the downtrend [Certain] [ST][HI].
## Bull case
Every multiple sits at or below its five-year floor: P/E 6.8x (6th percentile), EV/EBITDA 4.6x versus a 5.4x minimum, P/FCF 3.6x versus a 9.2x peer median [Certain] [RA]. The reverse DCF implies a -26.5% year-one revenue decline, far worse than the reported low-single-digit broadband erosion [Likely]. Cash generation is real: FCF margin 16.4% TTM, $2.4bn dividends plus $2.5bn buybacks in H1 2026, and a -4.74% share count YoY [Certain] [CF][ST]. Leverage has fallen to 2.43x from 2.85x [Certain] [BS]. Short interest is low (2.28%) and falling, so no crowding [Certain] [ST]. A separation on clean terms could crystallise value in the parks/content and broadband pieces [Guessing].
## Decision
```json
{
  "ticker": "CMCSA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Comcast is statistically cheap on every multiple, but its core broadband franchise is losing share, operating margin is falling and the unfinalized NBCUniversal separation leaves debt and dividend capacity unknown, so the discount looks more like a value trap than a mispricing.",
  "rationale": "Valuation is compelling, but unlike our other below-floor buys the fundamentals are deteriorating: broadband revenue declining, operating margin down 4pp from FY24, FCF flattered by working capital. Separation terms, Altman Z 1.40, a small macro bear tilt and results in two weeks keep conviction at 3. Good but not compelling: AVOID, hold cash.",
  "price_at_decision": 20.94,
  "price_date": "2026-10-07",
  "research_note": "research/CMCSA/2026-10-08.md",
  "triggers": [
    {
      "text": "TTM operating margin recovers above the FY2024 level of 18.8%, showing broadband/NBCU cost pressure is reversing rather than structural.",
      "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 18.8}
    },
    {
      "text": "Domestic broadband segment revenue (SEC 10-Q/8-K) returns to year-on-year growth, versus the decline to $6.3bn from $6.6bn in Q2 2026, showing share loss to fiber and fixed-wireless has stabilised."
    },
    {
      "text": "NBCUniversal separation terms are filed with the SEC leaving the remaining entity at or below today's 2.43x net debt/EBITDA with dividend capacity intact."
    }
  ],
  "scenarios": {
    "bull": {
      "probability": 0.2,
      "target_price_12m": 34.0,
      "basis": "Clean separation terms and stabilising broadband let EV/EBITDA recover toward its 5.4x five-year floor [RA], landing between the fact sheet's EV/EBITDA-method bear (27.94) and base (40.13) values; below the DCF bull because that DCF extrapolates TTM FCF that the note flags as working-capital flattered (FCF/NI 182.5% [CF])."
    },
    "base": {
      "probability": 0.45,
      "target_price_12m": 24.0,
      "basis": "P/E re-rates only partway from 6.8x toward the 8.1x peer median [RA,P:CHTR,P:T,P:VZ,P:WBD] while earnings drift lower on continued broadband erosion (SEC 10-Q) and operating-margin compression to 14.7% TTM [IS]; well below the mechanical 111.76 base fair value, which assumes no structural decline or separation leakage."
    },
    "bear": {
      "probability": 0.35,
      "target_price_12m": 16.5,
      "basis": "Broadband share loss accelerates and separation terms load debt onto the remaining entity, pushing P/E to its 5.4x five-year minimum [RA] on lower earnings; probability raised by the macro overlay's small tilt toward bear (10y yield 5.27%, +0.72pp/3m, raising refinancing cost into the debt split, research/CMCSA/2026-10-08-macro.md)."
    }
  },
  "replaces": null,
  "replacement_reason": null
}
```

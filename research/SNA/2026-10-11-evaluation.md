# Evaluation: Snap-on Incorporated (SNA) — 2026-10-11
## Bear case
The quality is real, but the price already pays for it. P/E of 18.4x and EV/EBITDA of 12.9x sit at or above their 5-year maximums (17.9x / 12.9x) [Certain] [RA]. The last close of 360.37 is 11.0% above base fair value of 320.61 [Certain] (fact sheet). Returns are slowly fading: ROCE is down 2.2pp and ROE down 2.6pp over five years [Certain] [RA], and the Piotroski F-score is only 4 [Certain] [ST]. The macro overlay tilts toward bear (small): a 10y Treasury at 5.22% and real yields up 0.56pp in 3 months raise funding costs for the Financial Services arm and make technicians' installment purchases less affordable [Likely] (research/SNA/2026-10-11-macro.md). Short interest is 7.25% and rose 8.7% in a month [Certain] [ST]. Q3 results on Oct 22 are a binary event [Certain] [ST]. The DCF bear case of 204.27 shows how far the shares could fall [Certain].

## Bull case
This is a moat business. The franchise-van distribution network is hard to copy [Likely] (note), operating margin has held near 25% for five years and ROIC is 18.4% [Certain] [IS,RA]. The balance sheet is net cash (-0.24x net debt/EBITDA) [Certain] [RA]. FCF conversion is 107% and the share count is falling 1.03% a year [Certain] [CF,ST]. Q2 sales rose 4.7% and EPS 5.1%, and C&I margins hit a record [Certain] (Q2 2026 transcript, [OV]). The stock trades 33% below the peer median P/E and 43% below the peer median P/FCF [Certain] (fact sheet). The reverse DCF implies only 4.5% year-1 growth, which is achievable [Likely]. The shares are 6.5% below their 50-day average with RSI at 31.7, so the sentiment reset has already happened [Certain] [ST,HI]. The bull fair value of 352.81 is close to the current price [Certain].

## Decision
```json
{
  "ticker": "SNA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Snap-on is a high-quality, net-cash franchise with ~25% operating margins, but at 18.4x P/E (above its 5-year maximum) and 11% above base fair value, the price leaves no margin of safety.",
  "rationale": "The business quality is not in doubt, but the valuation is. The stock trades above its own 5-year P/E and EV/EBITDA maximums and above even the bull fair value. Returns are fading slightly, the macro tilt is toward bear, and earnings are due on Oct 22. The reward does not justify a 7% core position. Good but not compelling, so AVOID.",
  "price_at_decision": 360.37,
  "price_date": "2026-10-09",
  "research_note": "research/SNA/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin falls below 23%, under the 5-year range of 24.7%-26.4%, showing pricing power or mix has broken rather than cyclical softness.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 23}},
    {"text": "TTM ROIC falls below 15%, showing the franchise-distribution moat no longer earns clear excess returns (now 18.4%).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 12%, under the FY2022 5-year low of 12.2%, showing cash generation is structurally weaker than earnings.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 12}},
    {"text": "Q3 2026 or later results disclose a material rise in Financial Services delinquencies or a decline in Tools segment organic sales for two consecutive quarters."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 378, "basis": "P/E holds at 18.4x [RA] while EPS compounds at the Q2 2026 rate of 5.1% ([OV] transcript), supported by record C&I margins and 1.03% annual buybacks [ST]; this is above the bull fair value of 352.81 because the multiple holds above its own history."},
    "base": {"probability": 0.5, "target_price_12m": 330, "basis": "EV/EBITDA eases from its 5-year maximum of 12.9x toward the 10.8x median [RA], offset by mid-single-digit growth, which brings the price close to the 320.61 base fair value (fact sheet)."},
    "bear": {"probability": 0.3, "target_price_12m": 262, "basis": "Rates stay high and squeeze Financial Services funding and technician affordability; the macro overlay's small tilt toward bear (research/SNA/2026-10-11-macro.md) raises this probability, and EV/EBITDA de-rates to the 261.64 bear value of the EV/EBITDA method (fact sheet)."}
  },
  "entry_price": 256.49,
  "entry_basis": "valuation file: base 320.61 x 0.8 = 256.49 (research/SNA/2026-10-11-valuation.md). At that price the shares would sit near the bottom of their 5-year multiple range [RA] with the same quality evidence, which would justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

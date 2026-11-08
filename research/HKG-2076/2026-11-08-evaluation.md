# Evaluation: Kanzhun Limited (HKG:2076) — 2026-11-08
## Bear case
The price (68.55) now sits on the base fair value (66.74), and the reverse DCF implies 25.2% year-1 revenue growth, a demanding hurdle [Likely]. Earnings quality is softening: net margin (52.8%) far exceeds operating margin (34.8%), so the 12.2x P/E is flattered by non-operating profit [Likely], and FCF conversion fell to 96.4% from 162.1% in FY2025 [Certain]. The **Direction change** line (FCF margin 50.9%, 4.0pp below its 2-year high of 54.9%) reflects that conversion drop; it is a pullback from a peak, still above a year earlier, so it does not yet threaten the thesis but is the metric to watch [Likely]. Shares outstanding rose 4.74% despite the return plan [Certain]. Revenue is all mainland China, with VIE and listing risk; the overlay sees stable CNY/HKD, so country risk is regulatory, not currency [Likely]. Board turnover and results on 2026-11-13 add event risk [Certain].

## Bull case
The business is improving on the rolling view, not just fiscal-year endpoints: operating margin rose to 34.8% from 23.2% a year earlier and ROCE to 14.0% from 10.6% [Certain]. Gross margin of 85.9% and net cash (net debt/EBITDA -5.79x) show a cash-rich two-sided network [Certain]. On operating measures that strip out the non-operating profit, the stock is cheap against its own history: EV/EBITDA 8.8x is below its 5y minimum of 15.0x and half the peer median 17.8x; P/FCF 12.1x is below its 5y minimum of 15.0x, at an 8.28% FCF yield [Certain]. The mechanical base leans on a DCF carrying a 3.5% China premium; the EV/Revenue method gives 97.40 [Certain]. A dividend and shareholder-return plan add cash returns [Certain]. The original thesis (below 5-year-minimum multiples, fundamentals intact) has not played out; no trigger is near [Likely].

## Decision
```json
{
  "ticker": "HKG:2076",
  "decision": "HOLD",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "China's leading direct-chat recruitment platform, with net cash, a 34.8% and rising operating margin and an 8.28% FCF yield, trades below its own 5-year minimum EV/EBITDA and P/FCF, pricing a China/VIE discount its fundamentals do not show.",
  "rationale": "Thesis intact: operating margin and ROCE rose over the last year and operating multiples remain below their 5-year floors. Reaching base fair value is not a thesis completion, since that DCF embeds a China premium. Softer FCF conversion, dilution and imminent results cap conviction at 4; hold at current size rather than add.",
  "price_at_decision": 68.55,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-2076/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 25% (34.8% now, 23.2% a year earlier), showing the AI-matching and network-effect cost advantage has eroded.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}},
    {"text": "TTM FCF margin falls below 40% (50.9% now), showing the cash step-up and conversion were transitory.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 40}},
    {"text": "TTM gross margin falls below the FY2023 five-year low of 82.2%, signalling pricing or competitive pressure on employer paid services.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 82.2}},
    {"text": "Reported quarterly revenue (income statement / company release) declines year on year for two consecutive quarters, or a VIE-related regulatory action is disclosed in a company filing."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 97.4, "basis": "Operating margin holds near 34.8% [IS-T] and EV/Sales recovers toward the 5y range (3.8x vs 3.9x minimum, 6.6x median [RA]): the EV/Revenue method's base value of 97.40 [fact sheet Fair value]."},
    "base": {"probability": 0.5, "target_price_12m": 80.0, "basis": "FCF margin stays near 50.9% [CF-T] and P/FCF moves partway from 12.1x toward its 5y minimum of 15.0x [RA]; above the blended base of 66.74 because the DCF leg (51.41) carries a 3.5% China premium and the EV/Revenue leg sits at 97.40 [fact sheet Fair value]."},
    "bear": {"probability": 0.25, "target_price_12m": 45.0, "basis": "Non-operating profit fades (net margin 52.8% vs operating 34.8% [IS]) and FCF conversion keeps falling from 96.4% [CF,IS] amid VIE/regulatory pressure (note section 6): between the mechanical bear of 35.80 and the DCF base of 51.41, cushioned by net cash at -5.79x net debt/EBITDA [BS,IS]."}
  },
  "entry_price": 53.39,
  "entry_basis": "valuation file: base 66.74 x 0.8; the level at which an ADD (not just a hold) would be justified on this evidence.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Great Wall Motor (HKG:2333) — 2026-11-08
## Bear case
Profitability is collapsing, and the five-year view hides it. All four rolling metrics carry a Direction change: TTM ROIC fell from 11.2% to 3.1%, ROCE from 7.0% to 1.9%, operating margin from 3.3% to 0.8% and FCF margin from 10.6% to 5.6% [RA-T, IS-T, CF-T] [Certain]. The likely driver is the Chinese auto price war, and there is no moat to defend margins against it, which breaks the thesis [Likely]. The low multiples (P/E 9.2x, EV/EBITDA 4.9x) rest on trough-to-falling earnings, a classic value trap [Likely]. FCF has swung from -48.3% to 330.4% of net income, driven by working capital, so the 12.78% FCF yield is not dependable [Likely]. The Bulgaria and South Africa plant plans add capex at a time of thin margins [Likely]. The mechanical fair value runs from 0.20 to 85.84, which shows it cannot anchor a decision [Certain]. The stock is down 58.0% in 12 months [Certain].

## Bull case
The balance sheet is a fortress, with net debt/EBITDA at -3.43x (net cash), and a Piotroski F of 6 [ST] [Certain]. The stock trades below its 5-year minimum on P/E, EV/EBITDA and P/B, and at a large discount to peers on P/E and EV/EBITDA [RA] [Certain]. FY2024 showed what the franchise can earn at mid-cycle: a 5.3% operating margin and 17.3% ROIC [IS, RA] [Certain]. If even part of that comes back, earnings would multiply off a depressed base [Likely]. Overseas expansion (the Ora 5 plant in Bulgaria and at least 10 European models) could diversify the business away from the domestic price war [Likely]. Modest share reduction (-1.21% YoY) shows capital is being returned [Certain]. Macro is context only: CNY is stable and HKD is pegged [macro overlay] [Likely].

## Decision
```json
{
  "ticker": "HKG:2333",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A net-cash Chinese automaker trading below its own 5-year minimum multiples, but its returns and margins are falling sharply in a price war with no visible moat, so the cheapness rests on trough-and-falling earnings.",
  "rationale": "Every rolling-12-month quality metric is falling (ROIC 11.2% to 3.1%, operating margin 3.3% to 0.8%), and the thesis needs a margin recovery that no evidence yet shows. Cheap multiples and net cash do not offset a deteriorating, moat-less business. The mechanical fair value is too unstable to rely on. Conviction 2: no position.",
  "price_at_decision": 6.40,
  "price_date": "2026-11-06",
  "research_note": "research/HKG-2333/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 3% (0.8% now, 3.3% a year earlier), showing the price-war squeeze is easing and the trough is behind it.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 3}},
    {"text": "TTM ROIC recovers above 8% (3.1% now), back toward the FY2021-FY2025 range of 7.6%-17.3%, showing returns are recovering rather than structurally impaired.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 8}},
    {"text": "Net debt/EBITDA moves above 0x (net debt), meaning overseas capex is consuming the net-cash cushion; this would harden the avoid.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 0}},
    {"text": "Company-reported overseas sales become a material and growing share of revenue in a primary filing, showing diversification away from the domestic price war."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 11.0, "basis": "Operating margin recovers toward the FY2024 5.3% [IS] and EV/EBITDA re-rates from 4.9x toward the 9.0x peer median [RA, peers]; well below the mechanical bull of 85.84 because that through-cycle DCF extrapolates erratic, working-capital-driven FCF (conversion -48.3% to 330.4% [CF,IS])."},
    "base": {"probability": 0.45, "target_price_12m": 6.8, "basis": "Margins stay near the 0.8% TTM trough [IS-T] while net cash (-3.43x net debt/EBITDA [ST]) and the 12.78% FCF yield [ST] put a floor under the price; far below the mechanical base of 32.63, which the note judges not credible given the 0.20 bear and negative DCF bear (research/HKG-2333/2026-11-08.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 4.5, "basis": "The price war deepens the falling rolling trend (ROIC 11.2% to 3.1% [RA-T], FCF margin 10.6% to 5.6% [CF-T]) and Bulgaria and South Africa capex erodes net cash, so the stock breaks below its 6.02 52-week low [HI]; the mechanical bear of 0.20 is an artefact of a negative DCF, not a 12-month outcome."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: returns and margins are deteriorating on every rolling-12-month metric, so a lower price would not change the decision. It is revisited only if the margin and ROIC recovery triggers are met.",
  "replaces": null,
  "replacement_reason": null
}
```

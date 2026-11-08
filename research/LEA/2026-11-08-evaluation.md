# Evaluation: Lear Corporation (LEA) — 2026-11-08
## Bear case
Lear is a price-taker supplier: gross margin 7.8% and operating margin 4.6% have been flat for five years, so OEM pricing pressure caps returns [Certain]. Cash is not improving on a rolling basis: TTM FCF margin is 2.9% against 3.2% a year earlier and below its 3.6% 2-year high, so the rising fiscal-year FCF trend overstates the last year [Certain]. Management cut revenue guidance for China and FX, and Chinese OEMs are taking share globally, which hurts a supplier tied to Western programmes [Likely]. The 10-Q says the US declined to extend USMCA in its current form [company-reported], a live risk for Mexican plants; nothing newer is verified (macro overlay) [Likely]. Thin margins make value fragile: the DCF bear is -9.12 and the blended bear 31.11 [Certain]. Short interest of 6.31% rose 43.2% in a month; the stock is down 19.8% over six months with beta 1.28 [Certain].
## Bull case
The stock trades below its own 5-year minimum on every multiple: P/E 9.7x, EV/EBITDA 4.6x against a 6.6x median, P/FCF 7.6x and a 13.19% FCF yield [Certain]. The reverse DCF implies -8.4% year-1 revenue growth, while Q3 revenue and core operating earnings grew despite lower industry production and core earnings guidance was held [Likely]. Returns are genuinely improving on a rolling basis: ROIC is 11.4% against 9.6% a year earlier, and ROCE 12.9% against 11.1% [Certain]. FCF conversion of 119.9% funds buybacks that cut the share count 5.53% in a year, and the board raised and extended the authorization, while net debt/EBITDA stays at 1.54x [Certain]. At these multiples the repurchases are accretive, and the EV/EBITDA fair value leg alone gives 167.91 against a 110.28 close [Likely].
## Decision
```json
{
  "ticker": "LEA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A cash-generative, buyback-funded seating and E-Systems supplier trading below every 5-year minimum multiple, but its thin, flat margins, a slipping rolling FCF margin, the China share threat and the USMCA risk make the cheapness a cyclical discount rather than a mispricing of a quality business.",
  "rationale": "Valuation is compelling, but quality is not: a 4.6% operating margin leaves little buffer if OEM volumes, Chinese competition or USMCA hit, the mechanical bear is far below the price, and rolling FCF margin is falling. Good but not compelling: conviction 3, so no position.",
  "price_at_decision": 110.28,
  "price_date": "2026-11-06",
  "research_note": "research/LEA/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin rises above 5.0%, breaking the five-year flat range around 4.5% and showing pricing power against OEMs.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 5.0}},
    {"text": "TTM FCF margin rises above its 3.6% 2-year high, showing cash generation improving rather than slipping.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 3.6}},
    {"text": "TTM ROIC rises above 13%, extending the rolling improvement from 9.6% to 11.4% into a clearly higher return level.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 13}},
    {"text": "A 10-Q or company release confirms USMCA-compliant trade terms for Mexican production are settled, with FY guidance held or raised."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 168.0, "basis": "Rolling ROIC keeps rising from 11.4% [RA-T] and EV/EBITDA recovers to the 5y median 6.6x [RA], matching the EV/EBITDA fair value leg of 167.91 [fact sheet Fair value]; below the mechanical bull of 219.36 because the DCF on a 2.9% FCF margin [CF-T] is too sensitive to trust."},
    "base": {"probability": 0.45, "target_price_12m": 130.0, "basis": "Core earnings guidance holds (Q3 2026 release, prnewswire URL in fact sheet) and EV/EBITDA re-rates only partway from 4.6x toward its 6.6x median [RA] as the China/FX revenue cut caps growth; well below the DCF-led base of 200.42 because flat 4.6% operating margins [IS] do not support the DCF's assumptions."},
    "bear": {"probability": 0.3, "target_price_12m": 85.0, "basis": "OEM production weakens, Chinese competitors take share and the USMCA non-extension [company-reported, 10-Q https://www.sec.gov/Archives/edgar/data/842162/000084216226000092/lear-20261003.htm] squeezes Mexican plants, pushing the stock toward its 52-week low of 99.00 [HI] and below; above the mechanical bear of 31.11 because buybacks and 1.54x leverage [BS,IS] limit downside."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below every 5-year minimum multiple [RA] and the base fair value less 20% is above the price. The obstacle is business quality and an unresolved USMCA/China risk; a lower price would not change the decision without margin or cash-flow improvement.",
  "replaces": null,
  "replacement_reason": null
}
```

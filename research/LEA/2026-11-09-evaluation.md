# Evaluation: Lear Corporation (LEA) — 2026-11-09
## Bear case
Lear takes prices from OEMs. Gross margin of 7.8% and operating margin of 4.6% have been flat for five years, so a volume or pricing shock hits equity hard; the DCF bear is -9.12 and the blended bear 31.11 [Certain]. On a rolling basis FCF margin is 2.9% against 3.2% a year earlier and below its 3.6% 2-year high. The fact sheet prints no Direction change line and calls it flat, but cash generation is not improving [Certain]. Revenue guidance was cut for China and FX, and Chinese EV makers taking share is a structural threat to suppliers tied to Western programmes [Likely]. The 10-Q says the US declined to extend USMCA in its current form [company-reported], putting Mexican plants at risk; nothing newer is verified (macro overlay) [Likely]. Part of the discount is sector-wide: EV/EBITDA and P/FCF are in line with peers [Certain]. Short interest rose 43.2% in a month [Certain].
## Bull case
Every multiple is below its own 5-year minimum: P/E 9.7x, EV/EBITDA 4.6x against a 6.6x median, P/FCF 7.6x, and the FCF yield is 13.19% [Certain]. The price sits at about the EV/EBITDA bear leg of 111.56, so the multiple-based model already prices a downturn [Certain]. The reverse DCF implies -8.4% year-1 revenue growth. Q3 sales grew 2% despite weaker global production, adjusted EPS beat, and core operating earnings guidance held [Likely]. The recent direction is not structural decay. Rolling ROIC rose from 9.6% to 11.4% and ROCE from 11.1% to 12.9%, both at 2-year highs. The slip in FCF margin is small, and the guidance cut is explained by FX and China mix [Likely]. FCF conversion of 119.9% funds buybacks that cut shares 5.53% in a year, and the authorization was raised to 2029. Leverage holds at 1.54x and Piotroski F is 7 [Certain].
## Decision
```json
{
  "ticker": "LEA",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A cash-generative seating and E-Systems supplier with rolling ROIC rising to an 11.4% 2-year high, a 13.19% FCF yield and accretive buybacks trades below every 5-year minimum multiple, where the price implies an -8.4% revenue decline that Q3 growth and held core earnings guidance do not show.",
  "rationale": "The recent direction is favourable or flat: returns are rising and the FCF slip is small and explained, so the cheapness is a cyclical discount with an intact balance sheet, not structural decay. Thin margins, sector-wide cheapness, China competition and USMCA cap conviction at 4, not 5. Standard volatility-scaled core size.",
  "price_at_decision": 110.28,
  "price_date": "2026-11-06",
  "research_note": "research/LEA/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 9%, reversing the rolling rise from 9.6% to 11.4% and showing returns are deteriorating.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 9}},
    {"text": "TTM operating margin falls below 4.0%, close to the FY2022 five-year low of 3.8%, showing OEM pricing or Chinese competition is compressing profitability structurally.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 4.0}},
    {"text": "TTM FCF margin falls below 2.0% (2.9% now), showing cash generation can no longer fund the buybacks.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 2.0}},
    {"text": "Management cuts full-year core operating earnings guidance, a 10-Q discloses that tariffs or USMCA terms materially reduce gross profit, or net debt/EBITDA on the ratios page rises above 2.0x."}
  ],
  "scenarios": {
    "bull": {"probability": 0.3, "target_price_12m": 168.0, "basis": "Rolling ROIC keeps rising from 11.4% [RA-T] and EV/EBITDA returns to its 5y median 6.6x [RA], matching the EV/EBITDA fair value leg of 167.91 [fact sheet Fair value]; below the mechanical bull of 219.36 because the DCF on a 2.9% FCF margin [CF-T] is too sensitive to trust."},
    "base": {"probability": 0.45, "target_price_12m": 138.0, "basis": "Core operating earnings guidance holds (Q3 2026 release, prnewswire URL in fact sheet) and EV/EBITDA re-rates partway from 4.6x toward its 6.6x median [RA] while buybacks shrink the share count (-5.53% YoY [ST]); well below the DCF-led base of 200.42 because flat 4.6% operating margins [IS] do not support the DCF's assumptions."},
    "bear": {"probability": 0.25, "target_price_12m": 88.0, "basis": "OEM production weakens, Chinese competitors take share and the USMCA non-extension [company-reported, https://www.sec.gov/Archives/edgar/data/842162/000084216226000092/lear-20261003.htm] squeezes Mexican plants, taking the stock below its 52-week low of 99.00 [HI]; above the mechanical bear of 31.11 because 1.54x leverage [BS,IS] and FCF conversion of 119.9% [CF,IS] limit downside."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

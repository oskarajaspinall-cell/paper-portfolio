# Evaluation: Grupo Aeroportuario del Sureste (BMV:ASUR.B) — 2026-11-08
## Bear case
The 5-year "rising" ROIC reads FY endpoints only; the trailing view has collapsed: ROIC 13.4% vs 26.3% a year earlier, ROCE 13.2% vs 25.7%, operating margin 40.9% vs 50.2% [RA-T, IS-T] [Certain]. The **Direction change** has two drivers. First, the Motiva deal adds 20 lower-margin airports and debt, taking net debt/EBITDA to 2.89x from -0.34x in FY2024 [BS,IS] [Likely]. Second, Mexico traffic fell year on year in August, September and October [Likely]. Both go to the core of the thesis: returns may stay structurally lower. Q3 EBITDA rose only 1.7% on 13% revenue growth (transcript) [Likely]. The price is not cheap against depressed earnings: P/E 14.8x sits at its 5y median of 14.6x, EV/EBITDA 10.6x is above its 9.0x median [RA], and the EV/EBITDA fair value of 404.31 is below the price [Certain]. The peso is 8% weaker over three months, and Brazil tariff risk is unverified (macro overlay) [Likely].
## Bull case
Concession monopolies at Cancún, San Juan and Colombia are hard to replicate [Likely]. The price implies -3.5% year-1 revenue growth, a low bar when consolidation is already adding revenue [Likely]. On a through-cycle view the base fair value of 794.01 (DCF 988.86) is well above the 491.55 close [Certain]. ASUR trades below peers on every multiple: P/E 14.8x vs 18.8x and P/FCF 15.2x vs 28.3x [RA,P] [Certain]. TTM FCF conversion recovered to 97.1% from 43.3% in FY2025 [CF] [Certain], and next-year investment is funded mainly by regional cash flow (transcript) [Likely]. Colombia and Puerto Rico traffic grew in October [Likely]. If Mexico traffic stabilises and the acquired airports' margins improve, returns could recover toward FY2025's 19.7% ROIC [Guessing]. Insiders own 29.74% [Certain].
## Decision
```json
{
  "ticker": "BMV:ASUR.B",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality airport concession franchise is in a leverage-funded expansion with trailing returns and margins falling sharply and home-market traffic declining, at multiples near or above its own 5-year medians, so the skew is balanced rather than compelling.",
  "rationale": "Mechanical base value leans on pre-acquisition margins; the EV/EBITDA method sits below the price. Trailing ROIC has halved, leverage has jumped and Mexico traffic is falling, while multiples are only median. Expected value is near the price, so this is good but not compelling: AVOID, with an entry near the EV/EBITDA fair value.",
  "price_at_decision": 491.55,
  "price_date": "2026-11-06",
  "research_note": "research/BMV-ASUR.B/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, showing the Motiva acquisition permanently dilutes returns rather than ramping.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "TTM operating margin falls below 35% (40.9% now, 50.2% a year earlier), showing traffic weakness and acquired-asset mix are structural.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 35}},
    {"text": "Net debt/EBITDA rises above 3.5x (2.89x TTM now), showing the expansion is outrunning cash generation.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3.5}},
    {"text": "TTM FCF margin falls below 15% (24.4% now), showing the investment plan is no longer funded by regional cash flow.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 652.9, "basis": "Mexico traffic stabilises and margins recover toward FY2025's 45.6% operating margin [IS], re-rating P/E toward the peer median 18.8x [RA,P] and the price back to its 52-week high of 652.90 [HI]; below the mechanical bull of 1,488.52 because that DCF embeds the FY2022-24 pre-acquisition margins."},
    "base": {"probability": 0.45, "target_price_12m": 520.0, "basis": "P/E holds near its 5y median 14.6x [RA] with modest earnings growth from Motiva consolidation offset by weak Mexico traffic (October traffic release); below the mechanical base 794.01 because the through-cycle DCF assumes pre-acquisition margins that TTM ROIC of 13.4% [RA-T] does not support, nearer the EV/EBITDA value of 404.31."},
    "bear": {"probability": 0.3, "target_price_12m": 350.06, "basis": "ROIC stays near 13.4% [RA-T], Mexico traffic keeps falling and leverage at 2.89x [BS,IS] caps the multiple: the EV/EBITDA method's bear value of 350.06 [fact sheet Fair value], above the blended bear 216.51 because concession assets and 6.57% FCF yield [ST] support a floor."}
  },
  "entry_price": 404.31,
  "entry_basis": "Base fair value x 0.8 is above the price, so anchored instead on the EV/EBITDA method's base value 404.31 [fact sheet Fair value], near the 52-week low of 411.22 [HI]: at that level the depressed earnings would be bought cheaply enough to justify conviction 4.",
  "replaces": null,
  "replacement_reason": null
}
```

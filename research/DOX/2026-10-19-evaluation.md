# Evaluation: Amdocs Limited (DOX) — 2026-10-19
## Bear case
Concentration is the thesis risk: AT&T 25.9% and T-Mobile 19.9% of FY2025 revenue, top 10 ~70% [company-reported] (https://www.sec.gov/Archives/edgar/data/1062579/000119312525319187/dox-20250930.htm). Either customer insourcing, consolidating vendors or re-pricing would hit earnings hard, and switching costs give no protection against that [Likely]. Below operating profit, quality is slipping: net margin fell from 16.1% to 9.8% TTM, ROIC dipped to 15.3% TTM from 17.2%, ROE is falling, and net debt/EBITDA climbed from -0.10x to 0.85x as buybacks outran FCF [Certain] (fact sheet IS, RA). The 52-week change of -27.1% and a price below its 200-day average suggest the market is pricing AI-driven disruption of telecom IT services that the "aOS" pivot has not yet disproved [Guessing]. Earnings on Nov 3, 2026 are a near-term binary event [Certain] (ST).

## Bull case
The valuation already assumes the bear case. EV/EBITDA 6.9x, EV/Sales 1.5x and P/FCF 9.8x all sit below their own 5-year minimums and below peers, and the reverse DCF implies -4.4% revenue in year 1 [Certain] (RA, fact sheet). Even the mechanical bear fair value of 63.75 is above the 60.06 close [Certain]. Operating economics are improving, not eroding: gross margin rose from 34.5% to 38.3% and operating margin from 14.0% to 17.8% TTM, ROCE reached 17.6%, and FCF conversion is 140.8% [Certain] (IS, RA, CF). A 10.19% FCF yield funds buybacks (shares -3.52% YoY) [Certain] (ST). New 10-year VEON and multi-year Telefónica Chile contracts show the run-and-modernise model is still winning work [Likely] (https://www.tipranks.com/news/the-fly/veon-amdocs-enter-10-year-strategic-agreement-to-advance-digital-services-thefly-news). Beta of 0.45 and the Vubiquity disposal sharpen the focus on core work [Likely].

## Decision
```json
{
  "ticker": "DOX",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A sticky telecom BSS/OSS franchise with expanding operating margin (17.8% TTM) and a 10.19% FCF yield funding buybacks trades below its own 5-year minimum EV/EBITDA, EV/Sales and P/FCF, where the price implies a revenue decline that new multi-year contracts do not show.",
  "rationale": "The mechanical bear value sits above the price, operating margins are expanding and cash returns are strong, so the skew is favourable. Extreme AT&T/T-Mobile concentration, falling net margin, rising leverage and earnings in two weeks hold conviction at 4, not 5. Standard volatility-scaled core size. Macro is context only.",
  "price_at_decision": 60.06,
  "price_date": "2026-10-16",
  "research_note": "research/DOX/2026-10-19.md",
  "triggers": [
    {"text": "TTM operating margin falls below 15%, reversing the FY2021-25 expansion from 14.0% to 17.9% and signalling pricing pressure from concentrated customers.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM ROIC falls below 13%, under the FY2021 five-year low of 13.9%, giving back the gains in capital efficiency.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 13}},
    {"text": "TTM FCF margin falls below 11%, under the FY2022 five-year low of 11.6%, showing cash generation can no longer fund buybacks.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 11}},
    {"text": "AT&T or T-Mobile discloses non-renewal, a material scope reduction or insourcing of its Amdocs relationship (20-F, 6-K or company release), or net debt/EBITDA on the ratios page rises above 1.5x."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 95.0, "basis": "Renewals plus aOS wins (VEON 10-year deal) restore EV/EBITDA toward its 5y median 11.0x [RA], close to the mechanical bull fair value of 98.10 [fact sheet]."},
    "base": {"probability": 0.5, "target_price_12m": 76.0, "basis": "Operating margin holds near 17.8% [IS] and buybacks continue, so the price moves toward the mechanical base fair value of 80.80, held slightly below it for the AT&T/T-Mobile concentration discount [note, 20-F]."},
    "bear": {"probability": 0.25, "target_price_12m": 50.0, "basis": "A top-customer scope cut or weak Nov 3 results push the price back toward the 52-week low of 49.74 [HI], below the mechanical bear value of 63.75 because that model does not capture a customer loss."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

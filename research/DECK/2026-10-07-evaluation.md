# Evaluation: Deckers Outdoor Corporation (DECK) — 2026-10-07
## Bear case
The market is pricing a HOKA/UGG peak and the early signs are in the numbers. Operating margin has slipped from 23.7% (FY2025) to 22.7% TTM, and net cash has fallen from -1.29x to -0.85x EBITDA [Certain]. The 10-K warns of "pricing and promotional pressure across our brands" and low entry barriers, and one customer holds 18.5% of receivables [Likely]. A large US retailer named HOKA among brands in a "reset" [Likely]. Two brands carry the whole business, so one fashion miss at UGG or share loss at HOKA would hit earnings hard [Likely]. Lower swing highs (104.88→93.09→83.00), a -37pp gap to SPY over 12 months and short interest up 20.4% to 7.02% show sellers are still in control into the 22 Oct print [Certain]. A cheap multiple can get cheaper if margins fall back toward FY2022's 18.0% [Guessing].
## Bull case
This is a 90.6% ROIC, 57.8% gross-margin, net-cash brand owner at 11.3x P/E, 7.5x EV/EBITDA and a 10.05% FCF yield, all below its own 5-year minimums and 32-40% below peers [Certain]. FCF conversion of 110% pays for a 5.72% annual share-count reduction, so per-share value compounds even with zero growth or re-rating [Certain]. FY2026 ROIC, ROCE and gross margin were all still near record levels, so the price is discounting a fundamental collapse that has not appeared [Likely]. An Altman Z of 9.56 and no debt remove balance-sheet risk [Certain]. The macro overlay finds no rate sensitivity [Likely]. Even a return to the 5-year minimum P/E of 13.9x is about 23% upside before buybacks [Certain].
## Decision
```json
{
  "ticker": "DECK",
  "decision": "BUY",
  "position_type": "CORE",
  "conviction": 4,
  "thesis": "A net-cash, 90%-ROIC footwear brand owner trades below its own 5-year minimum P/E, EV/EBITDA and P/FCF at a 10% FCF yield with 5.7% annual buybacks, which prices in a margin collapse that the fundamentals do not yet show.",
  "rationale": "Valuation sits below every 5-year minimum while returns, gross margin and cash conversion remain near records. Buybacks and the FCF yield support returns even with no re-rating. Two-brand concentration, slight margin slippage and weak momentum into earnings hold conviction at 4, not 5: standard 7% core size. No limits are breached.",
  "price_at_decision": 81.66,
  "price_date": "2026-10-06",
  "research_note": "research/DECK/2026-10-07.md",
  "triggers": [
    {"text": "TTM gross margin falls below 55%, below the FY2024 level of 55.6%, signalling competitive or promotional pressure is eroding brand pricing power.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 55}},
    {"text": "TTM operating margin falls below 20%, reversing most of the five-year expansion from 18.0%.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM ROIC falls below 70%, indicating brand-moat economics are deteriorating.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 70}}
  ],
  "scenarios": {
    "bull": {"probability": 0.35, "target_price_12m": 106.20, "basis": "P/E re-rates to its 5y minimum of 13.9x from 11.3x [RA] on TTM EPS lifted by the 5.72% YoY share-count reduction [ST], as rising ROIC (90.6%) and gross margin (57.8%) [RA,IS] ease the HOKA slowdown fear."},
    "base": {"probability": 0.45, "target_price_12m": 86.33, "basis": "P/FCF stays at 9.9x [RA] with flat FCF, and FCF per share grows only by the 5.72% buyback-driven share-count reduction [ST]."},
    "bear": {"probability": 0.20, "target_price_12m": 64.75, "basis": "Operating margin reverts from 22.7% TTM to the FY2022 level of 18.0% [IS] under the 10-K's flagged promotional pressure, cutting earnings about 21% at an unchanged 11.3x P/E [RA]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

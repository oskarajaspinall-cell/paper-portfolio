# Evaluation: Bio-Techne Corporation (TECH) — 2026-10-12
## Bear case
This is no longer a core equity idea: it is a merger-arbitrage position. Merck KGaA's fixed $73.00 cash bid, already approved by shareholders, caps the upside at roughly 0.7% from the $72.46 close [Certain] (note §3; sec.gov 8-K). If antitrust clearance fails, the price falls back toward the standalone bear fair value of $52.82 (-27.1%) [Likely] [HI, fair value]. Standalone, the business does not justify a rebound: ROIC fell from 13.7% to 9.7%, gross margin from 68.6% to 66.2% and operating margin from 25.2% to 22.6% over five years [Certain] [RA, IS]. It also trades at a premium to peers on every multiple (EV/EBITDA 34.1x vs 21.9x) [Certain] [RA]. Even a small break probability makes the expected return worse than the 3.8% cash rate [Likely]. The skew is about 1:40 against [Certain].

## Bull case
The deal looks close to certain. Shareholders approved it on 2026-09-23, antitrust is the only condition left, and Merck owes a $576.1m reverse fee if clearance fails, which gives it a strong incentive to close [Certain] (note §6; sec.gov 8-K). Short interest of 4.73% and 113.4% institutional ownership are typical of arbitrage positioning, not a fundamental short [Likely] [ST]. Even if the deal breaks, the business stays sound: FCF margin 21.7%, net debt/EBITDA 0.07x, Piotroski 7, and share count down 1.70% [Certain] [CF, RA, ST]. The standalone base fair value of $77.57 sits above the deal price [Certain] [fair value], so a broken deal need not mean permanent loss [Guessing]. None of this produces an equity return worth the risk over 12 months [Likely].

## Decision
```json
{
  "ticker": "TECH",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "TECH is pinned just below Merck KGaA's $73.00 cash bid, so the 12-month payoff is about 0.7% if the deal closes against roughly 27% downside to standalone bear fair value if antitrust clearance fails, and a quality profile that has declined for five years.",
  "rationale": "This is not a core equity thesis. It is a deal spread: about 0.7% upside against a -27.1% break scenario, an expected value below the price and below the 3.8% cash rate. Standalone quality has declined for five years and the stock is at a premium to peers. Conviction is 2, so there is no position.",
  "price_at_decision": 72.46,
  "price_date": "2026-10-09",
  "research_note": "research/TECH/2026-10-12.md",
  "triggers": [
    {"text": "The Merck KGaA merger agreement is terminated (sec.gov 8-K), which removes the deal-price cap and requires a fresh standalone core initiation."},
    {"text": "After a terminated deal, TTM ROIC recovers above 11.9% (the FY2023 level), showing the five-year returns decline has reversed.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 11.9}},
    {"text": "After a terminated deal, TTM operating margin recovers above 24.7% (the FY2023 level), showing pricing power and mix are restored.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 24.7}}
  ],
  "scenarios": {
    "bull": {"probability": 0.45, "target_price_12m": 73.00, "basis": "Antitrust clears early and holders receive the $73.00 cash consideration (note §6, sec.gov 8-K). Upside is capped at the deal price, so the standalone bull fair value of 89.50 [fair value] does not apply."},
    "base": {"probability": 0.45, "target_price_12m": 73.00, "basis": "The deal closes within 12 months at the fixed $73.00 cash price, with Merck's $576.1m reverse fee as its incentive to finish (note §6, sec.gov 8-K), which supersedes the standalone base fair value of 77.57 [fair value]."},
    "bear": {"probability": 0.10, "target_price_12m": 52.82, "basis": "Antitrust clearance fails and the stock reverts to the standalone bear fair value of 52.82 (EV/Revenue on own-history multiples [fair value, RA]), consistent with five years of falling ROIC (13.7% to 9.7%) [RA]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

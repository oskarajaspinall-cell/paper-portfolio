# Evaluation: Tata Consultancy Services Limited (NSE:TCS) — 2026-10-07

## Bear case
Offshore IT services look like they are commoditising. Gross margin has fallen from 43.3% (FY2022) to 40.4% TTM and net margin from 20.0% to 18.1% [Certain]. AI-driven productivity could keep shrinking billable effort, so the de-rating may be structural rather than cyclical [Guessing]. The cheapness is sector-wide: TCS still trades at a premium to peer medians on P/E (+11%), EV/EBITDA (+15%) and P/FCF (+30%) [Certain]. That leaves room for its multiple to converge down toward peers [Likely]. ROIC has fallen from 81.0% (FY2024) to 66.4% TTM [Certain], and the Porsche/MHP deals add integration risk without clear margin uplift [Likely]. Earnings land on Oct 8, 2026 [Certain], so an immediate negative print is possible. The shares are -27.6% over 12 months and below both moving averages [Certain]. INR translation adds noise [Likely].

## Bull case
This is a top-tier franchise at a five-year-low valuation. TTM ROIC is 66.4%, ROE 47.7%, operating margin a steady 24.9% versus 25.3% in FY2022, and FCF conversion 96.7% [Certain]. The balance sheet holds net cash (net debt/EBITDA -0.47x) and the Altman Z is 12.47 [Certain]. Every multiple sits below its own five-year minimum: P/E 15.3x vs a 17.3x minimum, P/FCF 15.8x, FCF yield 6.34% [Certain]. The premium to peers is modest relative to TCS's superior returns and scale [Likely]. Recent wins (Porsche AI contract, MHP acquisition, Best Buy GCC taken from Accenture) suggest it is winning AI-era share rather than losing it [Likely]. Beta of 0.18 diversifies an empty portfolio [Certain]. Over ~12 months, a 6.34% FCF yield on stable margins gives an asymmetric entry [Likely].

## Decision
```json
{
  "ticker": "NSE:TCS",
  "decision": "BUY",
  "position_type": "CORE",
  "core_initiation": false,
  "conviction": 3,
  "thesis": "A net-cash, 66% ROIC IT-services leader trading below its five-year multiple range on a 6.34% FCF yield, with stable operating margins, offers attractive 12-month risk/reward.",
  "rationale": "Quality is exceptional and the valuation is the lowest in five years on its own history. The peer premium, gross-margin erosion, AI deflation risk and earnings tomorrow cap conviction at 3 (5%) rather than higher. The portfolio is all cash with no sector exposure, so no limits bind and nothing needs replacing.",
  "price_at_decision": 2100.00,
  "price_date": "2026-10-06",
  "research_note": "research/NSE-TCS/2026-10-07.md",
  "triggers": [
    {"text": "Operating margin falls below 24.1% (the FY2023 five-year low), showing pricing/wage pressure is now hitting operating profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 24.1}},
    {"text": "Gross margin falls below 38.3% (the FY2025 five-year low), showing the commoditisation is deepening.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 38.3}},
    {"text": "ROIC falls below 64.6% (the FY2022 level), confirming the decline from 81.0% is structural erosion of the capital-return advantage.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 64.6}}
  ],
  "exit_plan": null,
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: SK hynix Inc. (KRX:000660) — 2026-10-07
## Bear case
This is a commodity memory maker at a cyclical peak [Likely]. TTM operating margin of 68.0% and net margin of 85.6% compare with -23.6%/-27.8% in FY2023 [Certain]; those profits come from an AI-driven shortage, not a moat [Likely]. The low 7.8x P/E is calculated on peak earnings. EV/Sales (6.6x) and P/B (4.9x) both sit above their 5-year maximums, which is the classic peak-cycle pattern [Certain]. FCF conversion has fallen to 56.6% as capex ramps, and a possible new production base points to industry capacity growth that historically ends in a glut [Likely]. The stock fell 24.3% over 3 months, so the market may already be discounting the turn [Certain]. A beta of 2.39 magnifies any AI-capex pullback [Certain]. If margins normalise toward the 15–35% pre-AI band, earnings could more than halve [Guessing].

## Bull case
SK hynix holds a technology and qualification lead in HBM, with disclosed supply ties to Nvidia. That gives it a higher barrier to entry than commodity DRAM [Likely]. Quality is at a cycle high: ROIC is 61.6%, FCF margin 48.5%, Piotroski F-score 7 and Altman Z 7.28 [Certain]. The balance sheet has swung to net cash (-0.47x net debt/EBITDA from 4.48x in FY2023), so it can fund HBM capacity and absorb a downturn without leverage [Certain]. Even on these figures the stock is cheap against peers: P/E is 45% below the peer median, EV/EBITDA 14% below and P/FCF 24% below, with a 7.10% FCF yield [Certain]. Dilution is negligible (+0.14% YoY) [Certain]. The Oct 29, 2026 results give an early read on whether HBM pricing is holding [Certain].

## Decision
```json
{
  "ticker": "KRX:000660",
  "decision": "BUY",
  "position_type": "CORE",
  "core_initiation": false,
  "conviction": 2,
  "thesis": "SK hynix's HBM leadership and net-cash balance sheet should sustain above-cost-of-capital returns through the AI memory cycle, and the stock trades at a discount to memory peers on earnings and cash flow.",
  "rationale": "Quality, net cash and a peer discount justify owning it. But earnings sit on peak-cycle margins, EV/Sales and P/B are above their 5-year highs, and beta is 2.39. Normalised earnings could be far lower. A 3% starter caps the cyclical downside. The portfolio is all cash, so no limits bind.",
  "price_at_decision": 1773000.00,
  "price_date": "2026-10-06",
  "research_note": "research/KRX-000660/2026-10-07.md",
  "triggers": [
    {"text": "TTM gross margin falls below 40%, a sign the HBM/DRAM pricing premium is eroding back toward the commodity pattern.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 40}},
    {"text": "ROIC falls below 15%, losing the cushion above the cost of capital that sets this cycle apart from the FY2022-23 trough.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "FCF margin turns negative, repeating the FY2022-23 pattern of capex outrunning cash generation in an oversupplied market.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "Net debt/EBITDA (ratios page) rises back above 1.0x, signalling a return to last cycle's leverage build-up."}
  ],
  "replaces": null,
  "replacement_reason": null
}
```

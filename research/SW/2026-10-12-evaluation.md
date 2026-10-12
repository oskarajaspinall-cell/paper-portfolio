# Evaluation: Smurfit Westrock Plc (SW) — 2026-10-12
## Bear case
Post-merger returns have collapsed and have not turned: ROIC 4.1% TTM vs 11.6% FY2021, operating margin 6.1% vs 10.3-12.7% pre-merger [Certain] (factsheet RA, IS). Net debt/EBITDA is 2.95x and Altman Z 1.47 sits in the distress zone [Certain] (ST), yet management is adding debt-funded M&A (CMPC Chile) before deleveraging [Likely] (note §5). The macro overlay flags rising real yields (+0.56pp/3m) and widening HY spreads, which raise both the discount rate and refinancing cost for exactly this kind of balance sheet [Certain] (macro overlay, FRED). On TTM earnings P/E is 43.9x, +150% vs peers [Certain]; the mechanical bear fair value is negative [Certain] (Fair value), showing how much equity value depends on margin recovery. The price trend is weak too: -16.4pp vs SPY over 6 months, short interest +14% m/m [Certain] (HI, ST). Price gains are flagged for 2027, not now [Likely].

## Bull case
On cash-based metrics the stock is cheap: EV/EBITDA 7.7x sits in the 22nd percentile of its 5y range and 6% below peers; P/B 1.2x is near its 5y low of 1.1x [Certain] (RA). FCF conversion of 204% shows that net income is depressed by non-cash merger charges, and the FCF yield is 4.69% [Certain] (CF, ST). Management says paper grades are "sold out globally", with price increases feeding 2027 earnings; Q2 adjusted EBITDA reached $1.14B despite $300M of extra freight [Likely] (transcript). If integration synergies arrive, the operating margin could move back toward the pre-merger 10%+ and the base fair value of 49.15 (+19%) is reachable [Guessing]. Vertical integration and scale are real structural advantages [Likely] (smurfitwestrock.com). The reverse DCF implies 7.9% year-1 revenue growth, which is demanding but not extreme for a pricing upcycle [Guessing].

## Decision
```json
{
  "ticker": "SW",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A scale, vertically integrated containerboard leader is cheap on EV/EBITDA, but post-merger returns, margins and a distress-zone balance sheet are still deteriorating while it levers up for more M&A, so recovery is a hope rather than evidence.",
  "rationale": "Quality is falling on every return metric, Altman Z is 1.47 and leverage is 2.95x with more debt-funded M&A coming. Rising real yields add to the risk (macro overlay). Base upside of +19% does not compensate for a fat left tail. This is a cyclical recovery bet with no turn yet in the reported numbers, so it falls short of the conviction-4 bar.",
  "price_at_decision": 41.29,
  "price_date": "2026-10-09",
  "research_note": "research/SW/2026-10-12.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 8%, showing freight/integration costs were transitory and synergies are landing (vs 6.1% TTM).", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 8}},
    {"text": "TTM ROIC recovers above 6%, evidencing merger returns turning (vs 4.1% TTM).", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 6}},
    {"text": "TTM FCF margin rises above 5.2%, the FY2023 pre-merger level, showing that cash generation can fund deleveraging alongside the CMPC deal.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 5.2}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 52.65, "basis": "2027 containerboard price increases ('sold out globally', Q2 transcript) lift margins toward pre-merger levels and the stock returns to its 52-week high [HI]; this is well below the 111.01 mechanical bull because that bull assumes a full return to pre-merger margins, which the TTM 6.1% operating margin [IS] does not yet support."},
    "base": {"probability": 0.45, "target_price_12m": 44.0, "basis": "EV/EBITDA drifts from 7.7x toward its 7.0x-8.2x own-median/peer band [RA] on roughly flat TTM EBITDA, below the 49.15 base fair value because the macro overlay (research/SW/2026-10-12-macro.md, moderate tilt toward bear) points to a higher discount rate and funding cost."},
    "bear": {"probability": 0.35, "target_price_12m": 32.73, "basis": "Margins stay stuck near 6.1% [IS] while CMPC debt keeps net debt/EBITDA near 3x and Altman Z at 1.47 [ST], so the stock revisits its 52-week low [HI]; bear probability raised 0.05 per the macro overlay's moderate tilt toward bear; the mechanical bear (negative value) is ignored as an equity floor because FCF stays positive at a 3.2% margin [CF,IS]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: returns and margins are still deteriorating, Altman Z is 1.47 and leverage is rising for the CMPC deal, so a lower price would not change the decision; re-evaluate when the margin/ROIC triggers show the recovery.",
  "replaces": null,
  "replacement_reason": null
}
```

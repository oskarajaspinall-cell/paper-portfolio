# Evaluation: Grab Holdings Limited (GRAB) — 2026-10-08
## Bear case
The turnaround is real but thin: TTM ROIC 5.9%, ROCE 1.7% and operating margin 3.7% [Certain] (factsheet RA, IS). Net margin of 16.0% far exceeds operating margin, so earnings quality is low, and FCF margin is negative (-4.3%) with FCF conversion at -26.8% [Certain] (CF, IS). The large cash outlay for 60% of Atome, a consumer lender, moves capital into credit risk while FCF is negative, so it is funded from the balance sheet [Certain] (note §5). Shares outstanding rose 4.45% YoY despite buybacks [Certain] (ST). Piotroski F of 2 and Altman Z of 0.61 are weak [Certain] (ST). The stock still trades at a premium to peers on EV/EBITDA (23.2x vs 19.4x) and P/E [Certain] (valuation table). Indonesian commission caps and a possible Uber/Delivery Hero tie-up threaten take rates [Likely] (note §2). Rising real yields and the dollar add pressure [Likely] (macro overlay).

## Bull case
Every margin has improved for five straight years, and gross margin is steady at 40.5% [Certain] (IS). EV/Sales of 2.1x sits below its own 5y minimum of 3.9x, and P/B of 1.9x is 60% below the peer median [Certain] (RA, peers). The balance sheet is net cash (net debt/EBITDA -13.12x) [Certain] (RA). Insiders, led by the CEO, bought stock near the three-year low, and short interest fell 18.7% month on month [Likely] (news, ST). Management raised its 2028 adjusted-EBITDA ambition at the September investor update, and Atome could speed up profitable lending [Guessing] (OV transcript). The mechanical fair value has a base of $5.25 against a $3.08 close [Certain] (fair-value table). Still, much of that gap comes from the inflated multiples of the pre-profit years, so it overstates the upside [Likely].

## Decision
```json
{
  "ticker": "GRAB",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Grab's margin turnaround is genuine, but returns are barely positive and FCF is negative while a large cash consumer-lending acquisition adds credit risk, so a valuation that is cheap only against its own pre-profit history does not justify a high-conviction core position.",
  "rationale": "The improvement is real, but ROIC of 5.9%, negative FCF, rising share count, weak F-score and an EV/EBITDA premium to peers mean it is not a good business at an attractive price yet. The Atome deal and Indonesia take-rate risk add uncertainty. Conviction 3 is below the buy threshold, so AVOID.",
  "price_at_decision": 3.08,
  "price_date": "2026-10-07",
  "research_note": "research/GRAB/2026-10-08.md",
  "triggers": [
    {"text": "TTM FCF margin turns positive (statistics page), showing that profit converts to cash even after digital-bank and Atome consolidation.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 0}},
    {"text": "Share count shrinks year on year (statistics page), showing buybacks now outweigh issuance from consolidations.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": "<", "value": 0}},
    {"text": "TTM operating margin rises above the TTM net margin of 16.0%, showing that core profitability, not below-the-line items, drives earnings.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 16}},
    {"text": "Q3 2026 results (due around Nov 2, 2026) show stable mobility and delivery take rates despite the Indonesian commission caps, as disclosed in the earnings release or call."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 4.43, "basis": "Margins keep improving and FCF turns positive, so EV/Sales re-rates toward its 5y minimum of 3.9x [RA], reaching the fact sheet's bear fair value of 4.43 [IS,RA]. The mechanical base (5.25) and bull (46.86) cases lean on pre-profit-era multiples (5y max 52.9x [RA]), so they are not used."},
    "base": {"probability": 0.45, "target_price_12m": 3.33, "basis": "EV/Sales holds near 2.1x, close to the 1.9x peer median [RA, P:SE, P:UBER, P:HKG:3690], and the price recovers only to the 50-day average of 3.33 [ST,HI] while Atome integration and take-rate pressure (note §2, §5) cap any re-rating; this sits below the mechanical range for the pre-profit-history reason given in the bull case."},
    "bear": {"probability": 0.30, "target_price_12m": 2.74, "basis": "FCF stays negative (-4.3% TTM [CF,IS]) and Indonesian caps compress take rates, so the price retests the 52-week low of 2.74 [HI]; the bear probability is lifted slightly by the macro overlay's small 'toward bear' tilt from rising real yields and the dollar (research/GRAB/2026-10-08-macro.md)."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

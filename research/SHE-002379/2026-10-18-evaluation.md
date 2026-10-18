# Evaluation: Shandong Hongqiao Aluminum Industry Holding Company Limited (SHE:002379) — 2026-10-18

## Bear case
This is a commodity smelter priced on peak-cycle returns. Two of the last five fiscal years were loss-making (ROIC -10.8% in FY2023) before the alumina/aluminum spread lifted gross margin to 22.0% TTM [Certain] (IS, RA); nothing in the evidence shows a cost-curve moat that keeps it there [Likely]. The 7.5x P/E is a peak-earnings multiple, while P/B of 3.2x sits above its own 5-year max and far above the 1.3x peer median [Certain] (RA): the market still pays for durability. The mechanical bear fair value is negative [Certain]. The shares are down 51.7% over six months, below both moving averages [Certain] (HI), hinting at a turning spread the TTM figures do not yet show [Guessing]. A 31.33% share-count drop is unexplained [Certain] (ST). The macro overlay adds a small bear tilt: a firmer dollar raises imported input costs [Likely].

## Bull case
Today's economics are exceptional: ROIC 43.5%, FCF margin 16.0% with FCF/NI of 107.4%, and net debt/EBITDA of just 0.14x [Certain] (RA, CF). The 14.36% FCF yield [Certain] (ST) means a holder recovers capital quickly if margins merely hold for a few years [Likely]. Base fair value of CNY 21.92 sits well above the 14.16 close, and the reverse DCF only asks for 6.0% revenue growth [Certain]. P/FCF of 7.0x is below the 12.3x peer median [Certain] (RA). Altman Z of 4.73 means the balance sheet can survive a downcycle that previously drove leverage to 13.24x [Likely] (ST, BS). If the share-count fall reflects buybacks, per-share value compounds faster [Guessing].

## Decision
```json
{
  "ticker": "SHE:002379",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A low-leverage, highly cash-generative aluminum producer whose current returns look like a commodity-cycle peak rather than a durable advantage, priced at a book-value premium to peers while its share price signals the spread may already be turning.",
  "rationale": "Core needs a good business at an attractive price; this is a cyclical with two loss years in five, a P/B above its own 5-year max and peers, an unexplained share-count drop, results due Oct 23, 2026, and a small macro bear tilt. The high FCF yield is likely peak cash flow. Not compelling; cash is preferable.",
  "price_at_decision": 14.16,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-002379/2026-10-18.md",
  "triggers": [
    {"text": "TTM gross margin falls below 10%, showing the alumina/aluminum spread behind the FY2024-25 step-up has compressed toward FY2021-23 levels.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 10}},
    {"text": "TTM ROIC falls below 15%, confirming the 43.5% TTM level was cyclical peak earnings.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 8%, showing cash generation is fading with the cycle.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 8}},
    {"text": "Reported results show gross margin held above 20% through a full aluminum/alumina price downturn with the share-count reduction confirmed as buybacks, which would evidence a durable cost advantage and justify re-research toward a BUY."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 24.44, "basis": "Margins hold near the 22.0% TTM gross margin [IS] and the shares re-rate to the through-cycle DCF base value of 24.44 [fact sheet fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 16.88, "basis": "Spread normalises partially and the shares settle at the EV/EBITDA method base value of 16.88 [fact sheet fair value], below the blended 21.92 because the DCF leg extrapolates the peak-cycle FCF margin of 16.0% [CF,IS]."},
    "bear": {"probability": 0.35, "target_price_12m": 7.0, "basis": "Gross margin reverts toward the FY2021-23 range of -1.4% to 4.1% [IS], the mechanical bear fair value is negative [fact sheet], and the P/B premium (3.2x vs 1.3x peers [RA]) compresses; probability raised by the macro overlay's small toward-bear tilt from dollar strength (research/SHE-002379/2026-10-18-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the open question is whether peak-cycle margins are durable, and the base fair value less a 20% margin of safety already sits above the price; a lower price would not change the decision until results show margin durability.",
  "replaces": null,
  "replacement_reason": null
}
```

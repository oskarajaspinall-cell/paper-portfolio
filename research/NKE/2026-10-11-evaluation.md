# Evaluation: NIKE, Inc. (NKE) — 2026-10-11
## Bear case
Every return and margin line is still falling: ROIC 44.9%→18.9% TTM, operating margin 14.3%→9.0%, FCF margin 9.5%→4.6% [Certain] (RA, IS, CF). Management calls the Greater China decline (−26% currency-neutral last quarter) structural, lasting "beyond fiscal 2027", and has guided the year down while launching the ~$1.0bn Pace restructuring [Certain] (SEC 10-Q, 2026-10-02). Buybacks are paused and the last quarter's FCF was negative [Certain]. The cheapness is a statement about depressed earnings, not mispricing: NKE still trades at a premium to peers on every multiple (P/FCF +143%) [Certain], and the reverse DCF needs 27.2% year-1 revenue growth [Certain]. Base fair value 26.52 sits 23.6% below the close [Certain]. Short interest rose 24.5% in a month [Certain]. A stronger dollar and rising real yields add FX and discount-rate drag [Likely] (macro overlay).

## Bull case
NKE trades below its own 5-year minimum on P/E (16.6x vs 22.0x), EV/EBITDA (11.1x vs 14.5x), EV/Sales and P/B [Certain] (RA), so a lot of bad news is already in the price after a 49.8% fall [Certain] (ST). The brand still earns a 43.4% gross margin and ~19% ROIC, and leverage is only 0.56x net debt/EBITDA [Certain] (RA, IS). Pace targets $2.5bn of cumulative savings through FY2031 [Certain] (10-Q), and the dividend is being defended [Likely]. If margins settle, operating leverage on a lower cost base could re-rate the stock toward the P/E-method values (46–65) [Guessing]. But nothing in the filings shows a trough yet: the "final reset" is a hope, not evidence [Likely].

## Decision
```json
{
  "ticker": "NKE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A great brand in a still-unfinished de-rating of its own fundamentals: returns, margins and cash conversion are falling, China decline is guided as structural, and the stock still trades at a premium to peers with a base fair value below the price.",
  "rationale": "Low own-history multiples reflect depressed, still-falling earnings, not mispricing. FCF margin 4.6%, buybacks paused, guidance cut, peer premium on every multiple and base fair value 23.6% below the close leave no margin of safety. Quality must stop deteriorating before price matters; conviction 2, no position.",
  "price_at_decision": 34.71,
  "price_date": "2026-10-09",
  "research_note": "research/NKE/2026-10-11.md",
  "triggers": [
    {"text": "TTM operating margin recovers above 11.5% (FY2023 level), showing Pace savings are restoring profitability rather than funding decline.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 11.5}},
    {"text": "TTM FCF margin recovers above 7.1% (FY2025 level), showing cash conversion has troughed.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 7.1}},
    {"text": "TTM gross margin rises above 44.7% (FY2024 level), evidence that pricing power and channel mix are recovering.", "check": {"source": "statistics", "field": "grossMargin", "op": ">", "value": 44.7}},
    {"text": "A 10-Q shows Greater China revenue growing again currency-neutral, contradicting management's structural-decline guidance."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 47.65, "basis": "Pace savings and a margin trough let the market re-rate toward the 6-month high of 47.65 [HI], still below the fact sheet's bull fair value 51.31 and the P/E-method base of 58.00 [fact sheet fair value]."},
    "base": {"probability": 0.45, "target_price_12m": 31.97, "basis": "Guided-down year with FCF margin near 4.6% [CF,IS] keeps the stock around its 52-week low of 31.97 [HI], between the blended base fair value 26.52 and the price, as the depressed P/E of 16.6x [RA] holds."},
    "bear": {"probability": 0.35, "target_price_12m": 21.29, "basis": "Structural China decline beyond FY2027 (SEC 10-Q 2026-10-02) and falling margins drive price to the fact sheet's bear fair value 21.29; probability raised slightly for the macro overlay's small tilt toward bear (stronger dollar, real yields up; research/NKE/2026-10-11-macro.md)."}
  },
  "entry_price": null,
  "entry_basis": "Not applicable at conviction 2; price is not the obstacle: deteriorating margins, returns and cash conversion with structural China decline must first stabilise, so a lower price alone would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

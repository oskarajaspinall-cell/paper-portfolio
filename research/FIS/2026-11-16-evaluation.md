# Evaluation: Fidelity National Information Services, Inc. (FIS) — 2026-11-16
## Bear case
The fall has a fundamental cause: on November 4 FIS cut its fiscal 2026 outlook and its CFO left abruptly [Likely], and the filing does not let us size the cut [Guessing]. Margins are eroding over the last 12 months: operating margin 22.6% to 21.5%, ROCE 9.2% to 8.1%, FCF margin 24.7% to 21.5% [Certain]; management points to implementation delays and higher cyber spend weighing on 2027 margins, so the reset is not over [Likely]. TTM ROIC of 6.9% is flattered by the Worldpay gain [Likely]. Leverage is the real problem: net debt/EBITDA 5.43x after debt-funded Issuer Solutions, Altman Z 0.31 [Certain], so any further EBITDA slip hits equity hard. Shareholder investigations add noise [Likely]. The price is below its 200-day average with negative 12-month momentum, so there is no trend support, and the mechanical fair value is flagged unreliable [Certain].
## Bull case
The price already discounts a collapse: the reverse DCF implies -24.9% year-1 revenue growth, against a business with about 82% recurring revenue [company-reported] on multi-year bank contracts [Likely]. Every multiple sits below its 5-year minimum: EV/EBITDA 9.5x vs a 14.9x low and 16% below peers, P/FCF 5.5x, FCF yield 18.26% [Certain]. Core-banking switching costs make lost share unlikely, and bank demand is described as strong [Likely]. The SEC delta shows no substantive new risk factors and treats the Issuer Solutions integration as done [Certain]. With FCF at this yield, deleveraging can be fast if margins merely stabilise, and buybacks continue (shares -1.75% YoY) [Certain]. The margin dip stems from delays and investment, not a broken model [Likely].
## Decision
```json
{
  "ticker": "FIS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating, ROCE and FCF margin declines are tied to client-directed implementation delays and higher cyber investment while bank demand stays strong (KBW transcript 2026-11-12, https://stockanalysis.com/stocks/fis/transcripts/796331-kbw-fintech-ecosystem-conference-2026/); no evidence of lost share, and the 3-year FCF margin drop reflects the Worldpay exit.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Net debt/EBITDA of 5.43x [BS,IS] with a fresh, unsized guidance cut and CFO exit: a further EBITDA slip would stress the balance sheet and the equity.",
    "veto": null
  },
  "thesis": "A recurring-revenue bank processor priced for collapse, but with high leverage, eroding margins and an unsized guidance cut the cheapness is not yet a margin of safety.",
  "rationale": "Valuation is extreme on cash flow, but the dip follows a real guidance cut and CFO exit, margins are falling, leverage is 5.43x and the fair value is unreliable. The scorecard puts conviction well below the buy bar; the obstacle is balance-sheet and execution risk, not price. No position.",
  "price_at_decision": 29.54,
  "price_date": "2026-11-13",
  "research_note": "research/FIS/2026-11-16.md",
  "triggers": [
    {"text": "Operating margin (TTM) falls below 19%, showing the margin reset is deeper than delays and investment.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 19}},
    {"text": "FCF margin (TTM) falls below 15%, undermining the cash-flow case for deleveraging.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Net debt / EBITDA rises above 6.5x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 6.5}},
    {"text": "ROCE (ratios TTM page) falls below 7%."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 42.0, "basis": "Margins stabilise and deleveraging starts; the stock re-rates toward its 200-day average of 42.16 [ST,HI], still below its 5y EV/EBITDA low of 14.9x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 32.0, "basis": "Guided reset plays out with operating margin near 21.5% [IS-T]; EV/EBITDA stays near today's 9.5x [RA], below the peer median of 11.3x, so the price drifts modestly; mechanical fair value ignored as unreliable [fact sheet]."},
    "bear": {"probability": 0.30, "target_price_12m": 21.0, "basis": "A further 2027 margin cut from implementation delays and cyber spend (KBW transcript) on 5.43x leverage [BS,IS] breaks the 52-week low of 27.93 [HI]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: at a P/FCF of 5.5x and below every 5y multiple low, the block is leverage of 5.43x, falling margins and an unsized guidance cut; a lower price would not change the decision. Re-examine on evidence the margins have stabilised.",
  "replaces": null,
  "replacement_reason": null
}
```

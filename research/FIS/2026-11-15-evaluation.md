# Evaluation: Fidelity National Information Services, Inc. (FIS) — 2026-11-15
## Bear case
The fall has a stock-specific cause: on 4 November FIS lowered its 2026 outlook and its finance chief left, months after management had voiced high visibility [Likely]. Management now says implementation delays and higher cyber investment weigh on 2027 margins, so the reset may not be over [Likely]. Operating margin fell from 22.6% to 21.5% and FCF margin from 24.7% to 21.5% over the last 12 months, 6.5pp below the 2-year high; ROCE slipped from 9.2% to 8.1% [Certain]. Leverage is the multiplier: net debt/EBITDA rose from 4.06x to 5.43x after the debt-funded Issuer Solutions deal and Altman Z is 0.31, so a small EBITDA miss moves the thin equity sharply [Certain]. Pricing power is limited (vendor cost increases can't be fully offset) [Certain]. ROIC of 6.9% is low for a software franchise, and P/E 4.4x is inflated by a one-off gain [Certain]. The price is far below its 200-day average [Certain].
## Bull case
The price assumes a collapse that recurring contracts do not show: the reverse DCF implies -24.9% revenue growth in year 1 [Certain]. P/FCF 5.5x sits below its 5-year minimum of 8.4x and half the peer median, with an 18.26% FCF yield [Certain]. Core banking platforms carry high switching costs and management says bank demand remains strong [Likely]. ROIC rose from 3.2% to 6.9% over the last year as the portfolio was simplified [Certain]. The margin dip is attributed to client-directed implementation delays and cyber investment, which are timing and investment items rather than lost share [Likely]. The free cash funds the dividend and deleveraging; if guidance holds from here, multiples back toward the 5-year floor offer a large re-rating [Guessing].
## Decision
```json
{
  "ticker": "FIS",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 1,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Operating and FCF margin fell over the last 12 months; management at the KBW conference (https://stockanalysis.com/stocks/fis/transcripts/796331-kbw-fintech-ecosystem-conference-2026/) attributes 2027 margin pressure to client-directed implementation delays and higher cyber investment, with bank demand still strong; the 3-year FCF margin fall reflects the Worldpay disposal mix change.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "Further guidance cuts after the 4 November reset and CFO exit, on 5.43x net debt/EBITDA and an Altman Z of 0.31, would compress the thin equity sharply.",
    "veto": null
  },
  "thesis": "A recurring-revenue core-banking processor at an 18.26% FCF yield and below its 5-year minimum multiples, but a fresh guidance cut, an abrupt CFO exit, falling margins and 5.43x leverage leave the cheapness unproven.",
  "rationale": "The dip has a cause (guidance cut, CFO exit) that raises credibility and leverage risk rather than being a pure overreaction. Valuation is deeply cheap, but quality is low, margins are falling and the balance sheet is stretched. The scorecard gives conviction 1: not a buy; re-check once a quarter shows guidance holding and leverage falling.",
  "price_at_decision": 29.54,
  "price_date": "2026-11-13",
  "research_note": "research/FIS/2026-11-15.md",
  "triggers": [
    {"text": "TTM ROIC falls below 5.0%, giving up the rise from 3.2% to 6.9%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 5.0}},
    {"text": "TTM FCF margin falls below 18%, showing the cash decline is not a timing effect.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 18}},
    {"text": "TTM operating margin falls below 20%, showing the margin reset is deepening.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "Net debt/EBITDA rises above 6.0x at any quarter end (5.43x now).", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 6.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 45.0, "basis": "Guidance holds and P/FCF re-rates toward its 5-year minimum of 8.4x [RA] on current FCF; below the unreliable mechanical fair value, which is weighed lightly."},
    "base": {"probability": 0.45, "target_price_12m": 34.0, "basis": "Margins stabilise near 21.5% [IS-T] and the shares recover part of the drop toward the 50-day average of 34.98 [ST], with leverage at 5.43x [ST] capping the re-rating."},
    "bear": {"probability": 0.30, "target_price_12m": 20.0, "basis": "A further 2027 margin cut from implementation delays and cyber spend (KBW transcript) on 5.43x net debt/EBITDA [ST] compresses the thin equity further."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the stock already trades below every 5-year multiple minimum and the mechanical fair value is flagged unreliable. The obstacles are guidance credibility after the CFO exit and rising leverage; a lower price would not change the decision until a quarter shows margins and leverage stabilising.",
  "replaces": null,
  "replacement_reason": null
}
```

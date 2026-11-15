# Evaluation: Rotork plc (LON:ROR) — 2026-11-15
## Bear case
This is no longer a compounding stake; it is a takeover-pinned price. ABB reportedly agreed on 2026-07-16 to buy Rotork for cash [Likely], and the price action fits merger arbitrage: 3-month momentum only +2.0% and ATR 0.2% of price, sitting just under the 495.00 high [Certain]. If the deal completes, the upside is capped at the offer and the shares delist, ending any 12-month thesis [Likely]. If it breaks, the stock is exposed to a fall back towards the pre-bid range (6-month low 286.40) [Likely], from a P/E of 33.3x against a 5y median of 25.6x and P/B above its 5y maximum [Certain]. That extended price would de-rate sharply if growth slowed without the bid underneath it [Likely]. FCF margin fell from 16.0% to 14.3% over the last 12 months, 3.6pp below its 2-year high, with the cause unverified [Certain]. Terms and conditions are [data unavailable].

## Bull case
The business is excellent: ROIC 26.3%, ROCE 30.5%, gross margin 50.5% and operating margin 24.1%, all rising over five years and over the last 12 months (operating margin +3.5pp) [Certain]. The FCF margin dip looks like working capital or capex rather than lost profitability, since margins rose in the same period [Likely]. Net cash, Piotroski F of 6 and shares down 2.52% YoY show a sound balance sheet and real capital returns [Certain]. The installed base, specification lock-in and service income form a narrow moat [Likely]. A strategic buyer paying a premium validates that quality [Likely], and a competing bid is possible but unevidenced [Guessing]. Trend strength is real: 24.8% above the 200-day average and +49.0% over 12 months [Certain]. But the residual return to holders is small and binary.

## Decision
```json
{
  "ticker": "LON:ROR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "temporary",
    "decline_evidence": "Only FCF margin is falling (16.0% to 14.3% TTM) while operating margin rose 3.5pp and ROIC rose 4.1pp over the same 12 months [IS-T, RA-T], pointing to working capital or capex timing rather than a broken model; cause not verified in the note.",
    "moat": "narrow",
    "key_risk": "high",
    "key_risk_text": "The reported ABB cash takeover pins the price: completion caps upside and delists the shares; failure exposes an extended multiple (P/E 33.3x vs 5y median 25.6x) to a fall towards the pre-bid range.",
    "veto": {"code": "binary_event", "reason": "Pending ABB takeover (reported 2026-07-16): the 12-month outcome is deal completion or break, not the business compounding; terms are unverified from a primary source."}
  },
  "thesis": "A high-quality actuator business whose shares are now pinned by a pending ABB cash takeover, leaving little upside and a binary downside if the deal fails.",
  "rationale": "Quality is excellent, but the reported ABB bid turns the next 12 months into a binary merger-arbitrage outcome with capped upside and a large downside if it breaks. That is not the core mandate. The binary-event veto caps conviction at 3, so the decision is AVOID; price is not the obstacle.",
  "price_at_decision": 493.40,
  "price_date": "2026-11-13",
  "research_note": "research/LON-ROR/2026-11-15.md",
  "triggers": [
    {"text": "ROIC falls below 20% (ratios / statistics page).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Gross margin falls below 46%.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 46}},
    {"text": "FCF margin falls below 10%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 10}},
    {"text": "The ABB takeover lapses or is withdrawn, per a primary company or RNS announcement, removing the binary event (re-research then)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.05, "target_price_12m": 530, "basis": "A competing bid above the ABB terms, unevidenced in the note [Guessing]; only a modest premium to the 495.00 52-week high [HI]."},
    "base": {"probability": 0.75, "target_price_12m": 495, "basis": "Deal completes and holders receive the offer; the price already trades in a narrow range just under the 495.00 high with ATR 0.2% of price [HI], so little is left beyond it."},
    "bear": {"probability": 0.20, "target_price_12m": 300, "basis": "Deal breaks and the shares fall back towards the pre-bid 6-month low of 286.40 [HI], with the P/E of 33.3x reverting towards its 5y median 25.6x [RA]; mechanical fair value is [data unavailable] (no GBP FX rate), so these targets rest on price history and own-history multiples."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the pending ABB takeover makes the outcome binary and caps upside; a lower price would not change the decision while the bid stands. Re-research if the deal lapses.",
  "replaces": null,
  "replacement_reason": null
}
```

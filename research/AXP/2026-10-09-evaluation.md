# Evaluation: American Express Company (AXP) — 2026-10-09
## Bear case
At $308.10 AXP trades 11.5% above its own-history base fair value of $272.52 and only 11.8% below the bull case, so the reward is lopsided the wrong way [Certain]. P/E of 18.7x sits above the 5y median of 16.5x while ROE has drifted down 1.7pp since FY2021 and ROIC is flat at 11.9% [Certain]. FCF conversion has fallen from 255.8% to 131.5% [Certain]. The Fed/OCC AML consent orders and $350m penalty add remediation cost and management distraction, and a future escalation cannot be ruled out [Likely]. Fintechs (Revolut, corporate-card players) are explicitly targeting Amex's premium and commercial customers [Likely]. Real yields (+0.61pp/3m) and HY spreads are both moving against a card lender, raising the discount rate and the provisioning risk ahead of 23 Oct results [Likely]. The stock lags SPY by 21.7pp over 12 months with the 50-day below the 200-day [Certain].
## Bull case
The closed-loop model, owning both merchant and premium cardholder, delivers a durable 34.4% ROE that bank issuers cannot easily copy [Likely]. P/E of 18.7x is 16% below the peer median and P/FCF 13.8x is far below peers, with a 7.23% FCF yield funding a 2.49% annual share-count reduction [Certain]. The consent orders impose no asset cap and, per the 8-K, do not affect 2027 guidance; the penalty is ~0.2% of market cap [Certain]. Investment in lounges and the new Amex Corporate platform defends the premium franchise [Likely]. The 12-month underperformance has likely already priced part of the higher-rate backdrop, and short interest is low and falling at 2.06% [Likely]. If real yields plateau, a re-rating toward the bull fair value of $344.57 is plausible [Guessing].
## Decision
```json
{
  "ticker": "AXP",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality closed-loop premium card franchise with a 34.4% ROE and steady buybacks, but at $308.10 it trades above its own-history base fair value with flat-to-softening returns, a fresh AML consent order and a bear-leaning credit/rate backdrop.",
  "rationale": "Quality is real, but price is the obstacle: 11.5% above base fair value, P/E above its 5y median, ROE trending down, and macro tilting toward bear before Q3 results. That is good but not compelling, so conviction 3 means no position. Revisit at the entry price.",
  "price_at_decision": 308.10,
  "price_date": "2026-10-08",
  "research_note": "research/AXP/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROE falls below 25%, showing the premium-spend model has lost its return advantage (TTM 34.4%).", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 25}},
    {"text": "TTM ROIC falls below 8%, closing the gap to cost of capital (TTM 11.9%, 5y low 10.4%).", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "A Fed/OCC or other bank-regulatory order imposes an asset or receivables growth cap on American Express National Bank, as disclosed in an SEC filing."},
    {"text": "Quarterly results (earnings release, from Q3 2026 on 23 Oct) show net write-off and delinquency rates rising sequentially for two consecutive quarters, signalling consumer-credit stress in the card book."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 344.57, "basis": "Real yields plateau and spreads stay contained, so P/E re-rates toward the upper half of its 14.9x-23.8x 5y range [RA], matching the fact sheet's bull fair value of 344.57 (macro overlay research/AXP/2026-10-09-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 290.31, "basis": "P/E drifts from 18.7x toward its 5y median of 16.5x [RA] as ROE softens (-1.7pp trend [RA]), partly offset by 2.49% buybacks [ST]: midway between the 308.10 close [HI] and base fair value 272.52."},
    "bear": {"probability": 0.3, "target_price_12m": 245.75, "basis": "Rising real yields (+0.61pp/3m) and widening HY spreads lift provisions and compress P/E toward its 5y low of 14.9x [RA], the fact sheet's bear fair value 245.75; bear weight raised slightly per the macro overlay's small toward-bear tilt (research/AXP/2026-10-09-macro.md)."}
  },
  "entry_price": 218.02,
  "entry_basis": "valuation file: base 272.52 x 0.8 (20% margin of safety on own-history P/E fair value).",
  "replaces": null,
  "replacement_reason": null
}
```

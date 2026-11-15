# Evaluation: Rabigh Refining and Petrochemical Company (TADAWUL:2380) — 2026-11-15
## Bear case
Rabigh is a commodity processor whose returns follow refining and petrochemical spreads [Likely]. FY2023-FY2025 ROIC was negative every year (-5.3%, -5.8%, -6.4%) [Certain], and the TTM jump to 21.6% ROIC and 12.1% operating margin is a cycle swing, not proof of a better business [Likely]. The **Direction change** lines (ROIC, ROCE, operating and FCF margin rising over 12 months against a falling 5-year trend) are driven by spreads, which can reverse as fast as they came [Likely]. FCF conversion swung between -328.6% and 237.7%, so the 42.23% FCF yield is likely flattered by working capital [Likely]. Altman Z of 1.44 is weak [Certain]. The price is above its 200-day average but 13.3% below its 50-day with -17.2% 3-month momentum [Certain]: if spreads fade, the low multiples de-rate on falling earnings, not rise. Aramco control may put minorities second [Guessing]. The fair value is flagged unreliable [Certain].
## Bull case
On TTM numbers the stock is extremely cheap: P/E 4.0x, EV/EBITDA 4.3x below its 5y minimum of 12.3x, P/FCF 2.4x [Certain]. The reverse DCF implies -23.2% revenue growth in year 1, so the price already discounts a sharp fade [Certain]. Piotroski F of 8 says the turnaround is broad-based [Certain], and net debt/EBITDA fell to 1.31x, so the balance sheet has de-risked [Certain]. Aramco as parent supplies feedstock and offtake, lowering operating risk [Likely]. The 12-month change is +66.6% and the 50-day sits well above the 200-day [Certain]. If even part of TTM profit proves recurring, the through-cycle DCF base of 45.34 SAR sits far above the price, though the valuation is flagged unreliable [Guessing].
## Decision
```json
{
  "ticker": "TADAWUL:2380",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {
    "decline_cause": "none",
    "decline_evidence": "Over the last 1 and 3 years ROIC, operating margin and FCF margin are all rising (RA-T, IS-T, CF-T); the 5-year fiscal decline reflects FY2023-FY2025 losses at the cycle trough.",
    "moat": "none",
    "key_risk": "high",
    "key_risk_text": "Refining/petrochemical spreads revert and TTM profit (ROIC 21.6% after three negative years) disappears; a commodity processor with no pricing power, so this is the most likely path to a broken thesis.",
    "veto": null
  },
  "thesis": "A cyclical refiner whose TTM recovery makes it look very cheap, but with no evidence the profit is durable rather than a spread peak.",
  "rationale": "Three loss-making years, no moat, unstable cash conversion and an unreliable fair value mean the low multiples likely capitalise a cyclical peak. The scorecard does not reach the buy bar; cash is acceptable.",
  "price_at_decision": 14.58,
  "price_date": "2026-11-12",
  "research_note": "research/TADAWUL-2380/2026-11-15.md",
  "triggers": [
    {"text": "TTM operating margin falls below 5% (spread recovery fading)", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 5}},
    {"text": "TTM FCF margin turns negative", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 0}},
    {"text": "TTM ROIC falls below 8%", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 8}},
    {"text": "Net debt / EBITDA rises above 3x", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 3}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 22.0, "basis": "Spreads hold and TTM EBITDA persists, so EV/EBITDA re-rates partway from 4.3x toward its 5y minimum 12.3x [RA]; well short of the unreliable mechanical base."},
    "base": {"probability": 0.45, "target_price_12m": 14.58, "basis": "Profit fades partly from the TTM peak while the low multiples hold, consistent with the reverse DCF's -23.2% year-1 revenue growth [FV]; mechanical base 60.50 is flagged unreliable so it is not used."},
    "bear": {"probability": 0.3, "target_price_12m": 11.67, "basis": "Spreads revert to the FY2023-FY2025 loss pattern (negative ROIC each year [RA]), matching the mechanical bear fair value of 11.67 SAR [FV]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the question is whether the TTM profit is durable after three loss years; a lower price on the same evidence would not change the decision. Re-check on the January results."
}
```

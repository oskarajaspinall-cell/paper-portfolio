# Evaluation: SK hynix Inc. (KRX:000660) — 2026-11-16
## Bear case
SK hynix is a memory producer at a cyclical extreme: TTM operating margin 74.5% and ROIC 77.0% against -23.6% and -9.7% in FY2023 [IS,RA] [Certain]. P/E 4.3x and EV/EBITDA 3.3x below their 5y minimums are the classic peak-earnings trap: the market is pricing earnings to fall [Likely]. The price is 20.1% below its 200-day average and down 33.9% over 6 months [HI], so there is no trend support, while the reverse DCF still needs 20.6% year-1 revenue growth [Likely]. FCF margin already sits 2.2pp below its 2-year high of 48.5%: small, but the first sign of the rolling peak, and FCF conversion is falling (-15.9pp) as capex rises [CF] [Likely]. Headlines cite a DRAM price-fixing lawsuit and weaker AI-accelerator spending forecasts [OV]; size unverified [Guessing]. Beta 2.46 and ATR 9.8% of price make a de-rating violent [Certain].
## Bull case
Even a halving of earnings leaves the stock near its 5y median P/E of 9.9x [RA] [Likely]. The balance sheet is net cash (net debt/EBITDA -0.46x) [BS], so a downturn would not threaten solvency [Certain]. The HBM lead with AI-accelerator buyers may lengthen this upcycle beyond past memory cycles [Guessing]. FCF yield 15.25% [ST] and Piotroski 7 show cash generation is real today [Certain]. Shares still +100.0% over 12 months; the recent fall is sector-wide (Nvidia, AI spending), not a company miss [OV] [Likely]. If AI demand holds, multiples below peers (-36% on P/E) could close [Likely].
## Decision
```json
{
  "ticker": "KRX:000660",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "scorecard": {"decline_cause": "none", "decline_evidence": "Python finds nothing falling over 1 or 3 years: ROIC, operating margin and FCF margin are all rising [RA-T, IS-T, CF-T]; FCF margin sits 2.2pp below its 2-year high of 48.5%, a minor capex-driven slip with net cash intact.", "moat": "narrow", "key_risk": "high", "key_risk_text": "The memory cycle turns from peak margins (operating margin 74.5% vs -23.6% in FY2023), collapsing earnings and the low multiples with them; likely within 12 months given AI-spending worries.", "veto": null},
  "thesis": "A net-cash memory leader earning cyclical-peak returns looks cheap on trailing multiples, but with the price below its 200-day average and earnings at a peak, the low multiples more likely price a downturn than an opportunity.",
  "rationale": "Peak-cycle margins, a mechanical fair value below the price (flagged unreliable), no trend support and a high cycle risk leave the scorecard at 3, short of the buy bar. Cheap trailing multiples on peak earnings are not a discount. AVOID; cash is an acceptable outcome.",
  "price_at_decision": 1216000,
  "price_date": "2026-11-13",
  "research_note": "research/KRX-000660/2026-11-16.md",
  "triggers": [
    {"text": "TTM operating margin falls below 50% (74.5% now), showing the memory upcycle has turned.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 50}},
    {"text": "TTM gross margin falls below 60% (77.4% now), signalling DRAM/HBM pricing is rolling over.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 60}},
    {"text": "TTM FCF margin falls below 30% (46.2% now), showing capex is outrunning cash generation.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 30}},
    {"text": "Net debt/EBITDA rises above 1.0x (-0.46x now), i.e. capex or a legal settlement turns net cash to debt.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.0}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 1935000, "basis": "AI/HBM demand holds and the stock recovers to its September swing high of 1,935,000 [HI] as multiples move toward peers (P/E peer median 6.7x [RA,P])."},
    "base": {"probability": 0.4, "target_price_12m": 1216000, "basis": "Earnings ease from the peak while the multiple drifts toward its 5y median 9.9x P/E [RA], roughly offsetting, so the price holds near the last close."},
    "bear": {"probability": 0.35, "target_price_12m": 771492, "basis": "The cycle turns and the price falls to the mechanical base fair value of 771,491.59 [valuation, fact sheet], consistent with the FY2022-FY2023 margin collapse [IS]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: earnings are at a cyclical peak and the mechanical fair value is flagged unreliable, so a lower price on falling earnings would not raise conviction; a re-look needs evidence of a through-cycle earnings floor.",
  "replaces": null,
  "replacement_reason": null
}
```

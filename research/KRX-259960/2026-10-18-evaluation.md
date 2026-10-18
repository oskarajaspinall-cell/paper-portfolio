# Evaluation: KRAFTON, Inc. (KRX:259960) — 2026-10-18
## Bear case
Krafton is a single-franchise business whose returns are falling: ROIC down from 40.3% (FY2021) to 18.3% TTM, operating margin from 43.6% (FY2024) to 29.7% TTM and net margin from 48.2% to 18.8% [Certain]. The trough multiples may be correct if PUBG is maturing, and the reverse DCF only says the market expects a -14.5% revenue year, not that it is wrong [Certain]. Governance is a live problem: a court ordered the CEO to reinstate the ousted Unknown Worlds leadership after a plan to avoid the studio head's bonus [Likely], and Q2 2026 showed a net loss despite record operating profit [Likely]. With no company-reported PUBG user or bookings trend, the implied decline can't be refuted before the Nov 4, 2026 print [Certain]. The shares are in a clear downtrend (-33.6% over 12 months, 50-day below 200-day) [Certain], and the name would add a second gaming stock to Communication Services alongside HKG:9999 [Certain].
## Bull case
Every multiple sits below its own 5-year minimum: P/E 10.3x, EV/EBITDA 4.3x, P/FCF 8.9x, an 11.27% FCF yield [Certain]. The business is net cash (net debt/EBITDA -1.61x), converts 113.8% of net income into FCF and shrank its share count 3.05% YoY [Certain]. Even the mechanical bear fair value of 274,700.80 KRW sits above the 194,100 KRW close [Certain]. Q2 2026 brought record first-half revenue and operating profit on PUBG growth and Subnautica 2's launch [Likely], which does not fit the revenue decline the price implies [Likely]. If the Nov 4, 2026 results show the governance charge was one-off and PUBG is stable, a re-rating toward the 5-year median multiples (P/FCF 16.5x, EV/EBITDA 7.1x) is plausible [Guessing].
## Decision
```json
{
  "ticker": "KRX:259960",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, 11.27%-FCF-yield game publisher trades below its own 5-year minimum on every multiple, but falling ROIC and margins, single-IP concentration and an unresolved governance dispute leave the cheapness unproven.",
  "rationale": "Valuation is compelling, but returns and margins have fallen for years, PUBG concentration is untested by any company-reported user data, and the Unknown Worlds court dispute plus the Q2 net loss question management. Good but not compelling: AVOID at conviction 3 and revisit after the Nov 4 results.",
  "price_at_decision": 194100.00,
  "price_date": "2026-10-16",
  "research_note": "research/KRX-259960/2026-10-18.md",
  "triggers": [
    {"text": "TTM ROIC falls below 15%, extending the five-year decline from 40.3% to 18.3% and confirming franchise erosion.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 15}},
    {"text": "TTM FCF margin falls below 15%, from 21.4% now, showing cash generation no longer supports the buyback and the trough-valuation case.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "TTM net margin falls below 15%, beyond the step-down from 22.1% (FY2025) to 18.8% TTM.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 15}},
    {"text": "Reported revenue declines YoY for two consecutive quarters (income statement), confirming the PUBG decline the reverse DCF prices in."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 359850, "basis": "Nov 4 results confirm PUBG stability and a one-off governance charge, and P/FCF re-rates from 8.9x to its 5y median 16.5x [RA] on TTM FCF [CF]; still below the mechanical base fair value 415,111.13 because ROIC has fallen from 40.3% to 18.3% [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 257350, "basis": "FCF holds near the 21.4% TTM margin [CF,IS] and P/FCF recovers only to its 5y minimum 11.8x [RA]; set below the mechanical bear fair value 274,700.80 because the history-based model does not capture the falling ROIC and governance overhang."},
    "bear": {"probability": 0.30, "target_price_12m": 135150, "basis": "FCF margin falls back to its FY2023 level of 14.9% [CF,IS] as PUBG matures, with P/FCF staying at 8.9x [RA]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the default anchor (base 415,111.13 x 0.8) is already above the 194,100 close and even the mechanical bear fair value is above it. The obstacles are declining ROIC and margins, untested PUBG concentration and the unresolved Unknown Worlds governance dispute; a lower price would not change the decision, the Nov 4, 2026 results could.",
  "replaces": null,
  "replacement_reason": null
}
```

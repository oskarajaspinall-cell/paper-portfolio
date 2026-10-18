# Evaluation: Sungrow Power Supply Co., Ltd. (SHE:300274) — 2026-10-18
## Bear case
The returns are already rolling over: ROIC fell from 55.3% in FY2025 to 43.1% TTM, ROE from 30.1% to 22.0% and operating margin from 17.7% to 16.7% [Certain]. Q1 2026 net income fell 40% y/y on storage-market price competition (note) [Certain], and the US move to bar foreign-made grid equipment and software threatens a key export market (note) [Likely]. The low multiples (14.4x P/E, 9.5x EV/EBITDA) sit on earnings that may still be falling, so they may not be cheap at all [Likely]. The mechanical bear fair value is negative (-21.12 CNY), the stock is down 49.2% over 12 months, sits 43.4% below its 200-day average, and results on Oct 31 could reset the base again [Certain]. Rising real yields raise renewable developers' hurdle rates (macro overlay, tilt toward bear, small) [Likely]. A Hong Kong listing could dilute A-share holders (note) [Guessing].
## Bull case
This is still a world-leading inverter and storage franchise with net cash (net debt/EBITDA -2.01x), an 18.9% TTM FCF margin and FCF conversion of 132% of net income [Certain]. At 10.9x P/FCF and a 9.15% FCF yield it trades below its own 5-year minimum on EV/EBITDA, P/FCF and P/B, and roughly half the peer median on P/E [Certain]. The reverse DCF implies -0.1% year-1 revenue growth, near stagnation, for a business whose gross margin is at a 5-year high of 30.9% [Certain]. Base fair value is 144.51 CNY [Certain]. If storage pricing stabilises and US exposure proves manageable, earnings and the multiple could both recover [Guessing].
## Decision
```json
{
  "ticker": "SHE:300274",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash, high-FCF inverter and storage leader trades below its own 5-year minimum multiples, but returns and earnings are falling under storage price competition and a US grid-equipment ban, so the cheapness may sit on still-declining earnings.",
  "rationale": "Cheap and cash-rich, but TTM ROIC, ROE and margins are falling from FY2025 peaks, Q1 profit dropped sharply, the US ban is unresolved and results are due Oct 31. Earnings direction, not price, is the obstacle; good but not compelling. China exposure is already concentrated in the portfolio. Cash is acceptable.",
  "price_at_decision": 76.86,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-300274/2026-10-18.md",
  "triggers": [
    {"text": "TTM gross margin falls below 25%, undoing the 5-year margin recovery (now 30.9%) and confirming storage price competition is structural.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 25}},
    {"text": "TTM ROIC falls below 20%, back toward FY2021-22 levels, showing returns are being competed away.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 20}},
    {"text": "Quarterly results (income statement page) show net income growing y/y again with gross margin held near 30%, evidencing that the competition-driven profit decline has ended (would raise conviction)."},
    {"text": "A primary filing or company release shows the US grid-equipment restriction does not cover Sungrow's inverter/storage products, removing the main regulatory overhang (would raise conviction)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 145, "basis": "Storage pricing stabilises and the US ban proves limited, so the market re-rates toward the base fair value of 144.51 CNY [IS,BS,CF,RA,ST]."},
    "base": {"probability": 0.45, "target_price_12m": 85, "basis": "Earnings stabilise below FY2025 levels and EV/EBITDA recovers only to around its 5-year minimum of 10.5x [RA] on lower TTM EBITDA [IS], consistent with the EV/EBITDA bear fair value of 84.83 CNY rather than the DCF base, which assumes growth the falling ROIC [RA] does not yet support."},
    "bear": {"probability": 0.35, "target_price_12m": 55, "basis": "Competition keeps compressing profit (Q1 2026 net income -40% y/y, note) and the US grid ban bites, with the macro overlay's small tilt toward bear (rising real yields) adding probability here; net cash (-2.01x net debt/EBITDA [RA]) and positive FCF [CF] make the negative mechanical bear fair value implausible, so the bear target sits well above it."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: returns and earnings are deteriorating (TTM ROIC, ROE and margins below FY2025) and the US grid-equipment ban is unresolved; a lower price would not change the decision until the Oct 31 results and later filings show the profit decline has ended.",
  "replaces": null,
  "replacement_reason": null
}
```

# Evaluation: Airtel Africa Plc (LON:AAF) — 2026-11-08
## Bear case
The 1,025.37 GBX base fair value rests on a DCF (1,444.61) driven by FCF at 338.7% of net income, while the own-history EV/EBITDA method gives 186.89, below the 277.60 price [Certain]. EV/EBITDA of 5.5x sits above its 5y median 4.7x, so on its own history the stock is not cheap [Certain]. Reported USD earnings are hostage to African currencies: net margin was -3.3% in FY2024 and ROIC fell to 10.5% in FY2025 [Certain], consistent with devaluation hits [Likely]. Nigeria's revenue share, the naira and the policy rate are all unverified (macro overlay) while the broad dollar is up and VIX is 28.18 [Certain]. **Direction change:** TTM FCF margin fell from 36.7% to 34.8%, 3.2pp below its 2-year high, as capex is front-loaded and spectrum/licence renewals approach [Likely]; it pressures the cash-yield thesis but leaves FCF margin above FY2022's 27.4% [Certain]. Bharti raising its stake shrinks free float [Likely].

## Bull case
Operations are improving on a rolling basis: TTM ROCE 26.1% (from 20.6%), ROIC 14.8% (from 11.2%) and operating margin 33.6% (from 30.9%), all at 2-year highs [Certain]. Gross margin rose to 67.4% and Piotroski F is 8 [Certain]. Leverage fell to 1.84x net debt/EBITDA from 2.69x in FY2025 [Certain]. The 18.92% FCF yield and P/FCF of 5.3x are well below the peer median of 8.6x, and P/E is below peers too [Certain]. The reverse DCF implies -24.8% year-1 revenue, far worse than the strong H1 growth management reported [Likely], so much FX damage looks priced [Likely]. The Airtel Money listing could crystallise value in mobile money [Guessing], and a controlling shareholder buying more stock signals confidence [Likely].

## Decision
```json
{
  "ticker": "LON:AAF",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A pan-African telecom and mobile-money operator with rising returns and margins trades at a high FCF yield, but its USD earnings depend on unverified naira and repatriation conditions and its EV/EBITDA already sits above its own 5-year median.",
  "rationale": "Operations are strong and improving, but the mechanical upside depends on a DCF built on FCF far above net income, the own-history EV/EBITDA value sits below the price, and the central Nigeria FX risk cannot be verified. Expected value is near the price: good, not compelling, so AVOID.",
  "price_at_decision": 277.60,
  "price_date": "2026-11-06",
  "research_note": "research/LON-AAF/2026-11-08.md",
  "triggers": [
    {"text": "TTM operating margin falls below 30% (33.6% now, 30.9% a year earlier), showing fuel inflation or competition is compressing profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 30}},
    {"text": "TTM FCF margin falls below 28% (34.8% now), showing capex and licence renewals are eroding the cash yield structurally.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 28}},
    {"text": "Net debt/EBITDA rises above 2.5x (1.84x TTM now), reversing the deleveraging from the FY2025 2.69x.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 2.5}},
    {"text": "TTM ROCE on the ratios page falls below 20%, or the company discloses a naira devaluation or Nigerian cash-repatriation restriction that cuts USD EBITDA."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 420.0, "basis": "Rolling ROCE 26.1% and operating margin 33.6% keep rising [RA-T, IS-T] and EV/EBITDA moves toward the 6.1x peer median [ST]; the price recovers toward its 436.20 52-week high [HI], well below the mechanical bull of 1,317.40 because that DCF capitalises FCF at 338.7% of net income [CF,IS]."},
    "base": {"probability": 0.45, "target_price_12m": 300.0, "basis": "Operations hold at TTM levels but EV/EBITDA stays near the current 5.5x, above its 5y median 4.7x [RA], with capex pressuring FCF margin (36.7% to 34.8% [CF-T]); far below the mechanical base 1,025.37 because the EV/EBITDA method gives 186.89 and the DCF ignores the FX translation losses seen in FY2024 [IS]; probability trimmed for the overlay's small toward-bear tilt (research/LON-AAF/2026-11-08-macro.md)."},
    "bear": {"probability": 0.30, "target_price_12m": 186.89, "basis": "A further naira devaluation or repatriation limit repeats the FY2024 net margin of -3.3% [IS] and the multiple falls to the fact sheet's EV/EBITDA-method base of 186.89; probability raised from 0.25 for the macro overlay's small toward-bear tilt (stronger dollar, VIX 28.18; research/LON-AAF/2026-11-08-macro.md)."}
  },
  "entry_price": 186.89,
  "entry_basis": "The fact sheet's EV/EBITDA-method base value of 186.89 GBX, where the stock would trade at its own-history EV/EBITDA rather than above its 5y median 4.7x [RA]; the default (base 1,025.37 x 0.8) is above the price because the DCF is unreliable here.",
  "replaces": null,
  "replacement_reason": null
}
```

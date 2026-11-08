# Evaluation: MGIC Investment Corporation (MTG) — 2026-11-08
## Bear case
The shares already price the good news. P/E of 8.9x sits at the top of its own 5y range (median 7.5x) and above the peer median of 8.8x. P/FCF and P/B are at a premium to peers too [RA] [Certain]. Earnings look cycle-peak. Favourable reserve development is supporting the loss ratio, and management expects gradual credit normalisation (Q3 2026 transcript) [Likely]. Returns are drifting: TTM ROIC is down 0.6pp on a year earlier and below its 2-year high of 13.8% [RA-T] [Certain]. The biggest risk is policy, and it is unresolved. The October 2026 Executive Order could lead to a pilot letting borrowers cancel mortgage insurance, which would shorten policy life and shrink insurance in force. Its scope and timing are unknown (10-Q, sec.gov) [Likely]. Short interest rose 42.2% in a month [ST] [Certain]. Buybacks at a peak multiple create less value per share [Likely].
## Bull case
This is a steady, high-return insurer. ROIC was between 12.1% and 16.5% over five years and ROE is 13.8% TTM [RA] [Certain]. FCF conversion is 102.3% and leverage is low (net debt/EBITDA 0.71x) [CF,BS] [Certain]. Capital returns are heavy: share count is down 11.51% YoY and the dividend was declared again [ST] [Certain]. Q3 2026 beat expectations, with annualised ROE of 14.2% and $17B of new insurance written (transcript) [Likely]. The revised bank-capital proposal keeps the existing treatment of mortgage insurance, removing an earlier threat (10-Q) [Likely]. The mechanical base fair value of 38.85, driven by P/B plus sustainable ROE, sits well above the price [Certain]. A 12.44% FCF yield supports a compounding return even with no re-rating [Likely]. The weakness: little of this is mispriced against the stock's own history or its peers.
## Decision
```json
{
  "ticker": "MTG",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-return, capital-returning US mortgage insurer whose quality is real, but whose multiples sit at the top of their own 5-year range and above peers at a late point in the credit cycle, while an unresolved Executive Order on cancelling mortgage insurance threatens policy life.",
  "rationale": "Quality and cash returns are solid, but this is not a mispricing. P/E is above its 5y maximum and at a premium to peers, ROIC is drifting lower, and credit normalisation and the mortgage-insurance cancellation pilot are open risks. Expected value sits near the price. Good but not compelling, so AVOID.",
  "price_at_decision": 28.60,
  "price_date": "2026-11-06",
  "research_note": "research/MTG/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROIC falls below 10%, under the five-year low of 12.1% (12.9% now), showing credit normalisation is eroding underwriting returns.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Net debt/EBITDA rises above 1.5x (0.71x TTM now), showing capital returns are being funded with leverage.", "check": {"source": "statistics", "field": "debtEbitda", "op": ">", "value": 1.5}},
    {"text": "The Executive Order mortgage-insurance cancellation pilot is published with a narrow scope (or dropped), as disclosed in a company filing or release on sec.gov or mgic.com. That would remove the main policy overhang and reopen the BUY case."},
    {"text": "The quarterly report states MGIC no longer meets PMIERs, or the GSEs cut PMIERs credit for its reinsurance."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 34.0, "basis": "ROE holds near its 14.3% FY2025 level [RA], book value compounds and P/B moves to its 5y maximum of 1.3x [RA]. This is below the mechanical bull of 39.79 because that P/B+ROE leg assumes today's ROE persists through the cycle."},
    "base": {"probability": 0.45, "target_price_12m": 30.0, "basis": "Earnings stay flat with gradual credit normalisation (Q3 2026 transcript) and P/E stays near today's 8.9x [RA], so the return is mostly buybacks and the dividend. This is below the mechanical base of 38.85 because the stock already trades above its own 5y P/E maximum."},
    "bear": {"probability": 0.30, "target_price_12m": 22.0, "basis": "Losses normalise and the Executive Order cancellation pilot shortens policy life (10-Q, sec.gov), so P/E falls back to its 5y median of 7.5x [RA] on lower earnings. This is below the mechanical bear of 32.06, which does not model policy-driven runoff of insurance in force."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the main obstacle. The default anchor (base 38.85 x 0.8) is above the current price. What blocks a BUY is the unresolved Executive Order pilot on cancelling mortgage insurance and credit at the top of the cycle, and a lower price would not resolve either one.",
  "replaces": null,
  "replacement_reason": null
}
```

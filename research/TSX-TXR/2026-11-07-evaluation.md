# Evaluation: Torex Gold Resources (TSX:TXR) — 2026-11-07
## Bear case
Torex is a single-asset, single-country (Mexico) price-taker on gold [Likely]. Today's 47.7% operating margin and 25.9% ROIC are near cycle highs; in FY2023-24 operating margin was 24.6% and ROIC 9.0% [Certain], so most of the improvement is the gold price, not a moat [Likely]. No AISC, reserve or NAV data are available to verify a durable cost edge [Certain]. The mechanical fair value (EV/EBITDA on own history) puts base at 16.23 CAD and even bull at 55.96 against a 75.91 close [Certain]. P/B sits at the 96th percentile of its 5y range [Certain]. Shares grew 7.85% YoY despite talk of capital returns [Certain]. The macro overlay tilts toward bear: real yields are high and the dollar firmed over 3 months, while the stock is already up 26.9% in 3 months; beta is 1.41 [Certain].

## Bull case
At current gold, Torex is a cash machine: TTM FCF margin 30.9%, FCF conversion 94.5% and a 12.60% FCF yield [Certain]. P/FCF of 7.9x is at the bottom of its 5y range and about half the peer median of 16.5x [Certain]. The balance sheet is net cash (net debt/EBITDA -0.11x), Altman Z 6.76, Piotroski 7 [Certain]. The FY2024 cash drain was the Los Reyes build, now behind it, and Q3 2026 results cite lower AISC and strong free cash flow (https://www.newsfilecorp.com/release/322448/Torex-Resources-Reports-Q3-2026-Results) [Likely]. Exploration at the San Miguel corridor adds optionality [Guessing]. The mechanical fair value is anchored on 1.3x-1.8x EV/EBITDA from years of lower gold prices, so it probably understates value [Likely]. If gold holds, FCF funds buybacks and the multiple can drift up toward peers [Guessing].

## Decision
```json
{
  "ticker": "TSX:TXR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A net-cash Mexican gold miner throwing off a 12.60% FCF yield at today's gold price, but its returns are commodity-driven rather than moat-driven and its cost advantage cannot be verified, so the cheap FCF multiple is a bet on gold, not on the business.",
  "rationale": "Strong current cash flow and a clean balance sheet, but margins track the gold price, there is no verifiable cost or reserve edge, dilution continues, and the macro overlay tilts toward bear after a sharp rally. The skew is roughly balanced, not compelling: AVOID. Price is not the main obstacle, so no entry price.",
  "price_at_decision": 75.91,
  "price_date": "2026-11-06",
  "research_note": "research/TSX-TXR/2026-11-07.md",
  "triggers": [
    {"text": "TTM operating margin falls below 35%, showing the gold-price-driven margin expansion is reversing toward FY2023-24 levels.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 35}},
    {"text": "TTM FCF margin falls below 15%, showing Los Reyes or sustaining capex is again absorbing the cash flow.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 15}},
    {"text": "Shares outstanding grow more than 10% YoY, showing capital returns are not offsetting dilution.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 10}},
    {"text": "Net debt / EBITDA on the ratios page rises above 1.0x, ending the net-cash position."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 86.0, "basis": "Gold holds and TTM FCF is sustained, so P/FCF re-rates from 7.9x toward its 5y median 9.0x [RA], still well below the 16.5x peer median; above the mechanical bull because that is anchored on low-gold-price history."},
    "base": {"probability": 0.4, "target_price_12m": 74.0, "basis": "Margins stay near TTM levels and EV/EBITDA stays near the 4.0x peer median [RA], with continued dilution (shares +7.85% YoY [ST]) offsetting FCF; above the mechanical base because the 1.8x own-history median reflects lower gold prices."},
    "bear": {"probability": 0.35, "target_price_12m": 42.0, "basis": "Per the macro overlay (research/TSX-TXR/2026-11-07-macro.md, tilt toward bear, small, which raised this probability), higher real yields and a firmer dollar push gold down and operating margin back toward the FY2023 24.6% [IS] at a 4.0x EV/EBITDA, landing below the mechanical bull of 55.96."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the returns are gold-price-driven with no verifiable cost or reserve data (NAV unavailable on stockanalysis.com), and the mechanical fair value from low-gold-price history is not a usable anchor; a lower price would not change the decision.",
  "replaces": null,
  "replacement_reason": null
}
```

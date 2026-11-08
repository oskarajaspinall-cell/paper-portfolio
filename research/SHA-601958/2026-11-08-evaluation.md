# Evaluation: Jinduicheng Molybdenum Co., Ltd. (SHA:601958) — 2026-11-08
## Bear case
This is a single-commodity miner whose returns are a molybdenum upcycle, not a proven moat: ROIC went from 6.5% in FY2021 to 27.9% TTM and margins stepped up in FY2023 [Likely]. The TTM operating margin of 32.3% is at its 2-year high, so EV/EBITDA of 8.8x is measured on near-peak earnings [Certain]. The Direction change line matters most. FCF margin fell to 13.8% from 21.2% a year earlier, 13.2pp below its 2-year high, and FCF/NI is 55.0%. Without capex detail we cannot tell growth spend from a weakening cash cycle, and either way P/FCF of 25.3x and a 3.95% FCF yield are not cheap [Certain]. The stock trades above peers on P/E (+28%) and EV/EBITDA (+39%) [Certain]. Reserves, cost position and NAV are [data unavailable], and the Q3 2026 filing was not read [Certain]. Momentum of -27.2% over 3 months suggests the market sees the commodity price rolling over [Guessing].

## Bull case
The balance sheet is net cash (net debt/EBITDA -1.19x, Altman Z 13.18), so a down-cycle threatens earnings, not solvency [Certain]. On its own history the stock is cheap: P/E of 13.9x sits at 12% of its 5y range against a 15.9x median, and EV/EBITDA of 8.8x is below its 10.2x median [Certain]. Profitability is still rising on a rolling basis. Operating margin is up 4.8pp and ROCE up 2.0pp year on year, so the last 12 months show no earnings roll-over yet [Certain]. Shares are down 0.60% YoY, so there is no dilution [Certain]. The mechanical base fair value of 19.55 CNY is above the 16.65 close [Certain]. If the FCF drop is growth capex, conversion could return toward FY2024's 119.2% [Guessing].

## Decision
```json
{
  "ticker": "SHA:601958",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A net-cash molybdenum miner that looks cheap against its own multiples, but its earnings sit near a commodity-cycle peak, cash conversion is falling and it trades above its peers, with reserves, costs and the latest quarter unverified.",
  "rationale": "Its own history makes it look cheap, but earnings are near peak-cycle margins and FCF conversion is deteriorating. It is dear against peers, and NAV, reserves and the Q3 filing are unverified. The mechanical base upside is modest for a cyclical, set against a bear value below the price. Good but not compelling, so no position.",
  "price_at_decision": 16.65,
  "price_date": "2026-11-06",
  "research_note": "research/SHA-601958/2026-11-08.md",
  "triggers": [
    {"text": "TTM FCF margin recovers above 21% (13.8% now, 21.2% a year earlier), showing the cash-conversion drop was timing or growth capex rather than a weaker cash cycle.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 21}},
    {"text": "A company filing on its own domain discloses reserves and unit costs showing a low-cost, long-life ore body, removing the NAV blind spot."},
    {"text": "TTM operating margin falls below 25%, confirming the down-cycle is under way and the own-history cheapness was a peak-earnings illusion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 25}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 24.0, "basis": "Margins hold near the TTM 32.3% [IS-T] and EV/EBITDA recovers toward its 5y median 10.2x [RA]; below the mechanical bull of 27.26 because peers trade at a 6.3x median EV/EBITDA [RA, peers]."},
    "base": {"probability": 0.45, "target_price_12m": 17.0, "basis": "EV/EBITDA stays near 8.8x [RA] as EBITDA eases from the 2-year-high operating margin [IS-T]; below the mechanical base of 19.55 because that value applies a median multiple to near-peak TTM EBITDA while FCF margin is falling [CF-T]."},
    "bear": {"probability": 0.3, "target_price_12m": 13.49, "basis": "The molybdenum cycle turns, margins revert toward the FY2024-FY2025 levels of 28.4%/28.3% [IS] and the multiple heads to its 5y low of 6.7x [RA]: the mechanical bear fair value of 13.49 [fact sheet Fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: the obstacle is visibility on the commodity cycle, reserves and cash conversion, not price alone, so no entry price is set.",
  "replaces": null,
  "replacement_reason": null
}
```

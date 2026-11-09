# Evaluation: RenaissanceRe Holdings Ltd. (RNR) — 2026-11-09
## Bear case
The Direction change line (TTM ROIC 13.1% vs a 24.5% 2-year high [RA-T]) is cyclical, not structural, but the cycle is still turning against RNR: Q3 premiums earned fell on property rate cuts and casualty de-risking [company-reported] (https://www.sec.gov/Archives/edgar/data/913144/000091314426000098/rnr-20260930.htm) [Likely]. That is the start of a soft market, not a trough with the earnings reset already priced in [Likely]. Nor is the stock cheap on what the market shows: P/E 9.7x is above its 5y max of 7.2x and 17% above peers, P/B 1.3x matches the peer median, and the share price is up 29.9% in 12 months, near its 52-week high [RA,ST,HI] [Certain]. The P/B+ROE value of 703.55 assumes a sustainable ROE and a discount rate set by a beta of 0.13 that understates catastrophe risk; the P/E method gives 177.36 [Likely]. Q3 large-loss reserves remain uncertain [company-reported] (same 10-Q) [Certain].
## Bull case
The fall in returns is explained, not broken: ROIC is +0.7pp on a year earlier, and underlying underwriting stayed profitable through a quarter of large-loss events [company-reported] (https://www.sec.gov/Archives/edgar/data/913144/000091314426000098/rnr-20260930.htm) [Certain]. The Q3 net loss came mostly from mark-to-market losses as yields rose, and these reverse into investment income as bonds roll and pull to par [Likely]. Capital returns are heavy: shares are down 12.29% YoY and the buyback was renewed [ST] [Certain]. Leverage is low at 0.18x net debt/EBITDA [RA] [Certain]. Fee income from the third-party capital vehicles cushions softer pricing [Likely]. The mechanical base fair value of 528.15 is well above the 347.35 close [Certain]. Even so, a business at a peer-level P/B with a falling pricing cycle is fair rather than compelling [Likely].
## Decision
```json
{
  "ticker": "RNR",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A skilled, buyback-heavy cat reinsurer whose return decline is cyclical rather than structural, but which enters a softening pricing cycle at a peer-level P/B and a P/E above its own 5-year range, so the skew is balanced, not compelling.",
  "rationale": "The ROIC fall is cycle normalisation, not a broken model, so direction alone is no reason to reject. But this is no cheap stock in a temporary dip: price is near highs, multiples sit at or above peers and own history, and the high model fair value rests on a low-beta discount rate. Expected value sits near the price: conviction 3, AVOID.",
  "price_at_decision": 347.35,
  "price_date": "2026-11-06",
  "research_note": "research/RNR/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE rises above 18% (14.0% now), showing returns re-accelerating despite softer property pricing, which would lift conviction.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 18}},
    {"text": "TTM ROIC falls below 10% (13.1% now), showing the soft market is eroding underwriting returns beyond normalisation.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 10}},
    {"text": "Shares change YoY turns positive (-12.29% now), showing capital returns have stopped.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "The 10-Q or earnings release reports property-catastrophe rate increases at the January renewals, or a quarterly combined ratio above 100% excluding named large-loss events."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 420, "basis": "ROE recovers toward the FY2025 19.7% [RA] as Q3 mark-to-market losses reverse and the 12.29% share shrink [ST] compounds book per share at a steady 1.3x P/B [RA]; set well below the mechanical bull of 699.12 because the P/B+ROE method's low-beta (0.13 [ST]) discount rate understates catastrophe risk."},
    "base": {"probability": 0.45, "target_price_12m": 360, "basis": "ROE holds near the TTM 14.0% [RA] in a softening market (Q3 property rate reductions, 10-Q https://www.sec.gov/Archives/edgar/data/913144/000091314426000098/rnr-20260930.htm) and P/B stays at the 1.3x peer median [RA,P]; below the mechanical base of 528.15 because the P/E method (177.36) and peer multiples do not support the P/B+ROE value."},
    "bear": {"probability": 0.30, "target_price_12m": 260, "basis": "Soft pricing plus adverse development on the uncertain Q3 large losses [company-reported] (10-Q) cut earnings and the P/E de-rates toward its 5y max of 7.2x [RA]; below the mechanical bear of 469.06 because that value rests on the P/B+ROE method's sustainable-ROE assumption."}
  },
  "entry_price": 300.80,
  "entry_basis": "P/E back to the peer median of 8.4x [RA,P] on TTM earnings (from 9.7x at 347.35), with P/B then below peers: the cycle risk would be paid for. The default (base 528.15 x 0.8) is above the price and not used, because the P/B+ROE value rests on a low-beta discount rate.",
  "replaces": null,
  "replacement_reason": null
}
```

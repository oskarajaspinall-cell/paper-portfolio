# Evaluation: Changjiang Securities Company Limited (SHE:000783) — 2026-10-19
## Bear case
The TTM numbers are a cycle peak, not a new base. ROE ran 8.0%→4.9%→4.7%→5.0%→9.1% over FY2021-25 before 12.3% TTM, and ROIC sat near 1-3% for four years [Certain] [RA]. Operating margin at 51.1% TTM against 22.8%-37.4% in FY2021-24 reflects an A-share trading and margin-lending upcycle that can reverse fast [Likely] [IS]. The 8.6x P/E is cheap only on peak earnings and merely in line with the 8.8x peer median; on P/B, the steadier yardstick for a broker, it trades at 1.0x against a 0.7x peer median [Certain] [RA]. The 40.6% base fair-value upside rests on an FCFE model fed by FCF swinging 17%-281% of revenue, i.e. client-fund and trading-book movements, not owner earnings [Certain] [CF]; the P/E method's base of 7.35 sits below the price [Certain]. Brokerage is commoditised with no moat [Likely], and regulatory capital data are unavailable [Certain].

## Bull case
Earnings power is clearly recovering: ROE doubled from FY2024 to TTM and net margin rose from 28.0% to 39.2% [Certain] [RA, IS]. The price implies a -1.7% year-1 revenue decline, so the market already assumes the upcycle fades [Certain] [fact sheet reverse DCF]. P/E sits below its own five-year minimum of 12.9x [Certain] [RA]. The stock is down 10.6% over 12 months and 11.1% below its 50-day average with RSI 31.5, so sentiment is washed out [Certain] [ST, HI]. If China trading volumes stay elevated, Q3 results on Oct 30, 2026 could confirm a higher run-rate and re-rate the shares toward the 52-week high of 10.73 [Guessing]. Beta of 0.85 and Piotroski 6 suggest no balance-sheet stress [Likely] [ST].

## Decision
```json
{
  "ticker": "SHE:000783",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A commoditised China broker earning peak-cycle returns, cheap on peak P/E but dear on P/B versus peers, with fair-value upside resting on unreliable FCF.",
  "rationale": "Returns are cyclical, not structural: four years of 1-3% ROIC, no moat, and TTM margins far above history. P/B is above peers and the FCFE fair value uses working-capital-driven cash flow, while the P/E method sits below the price. Good cycle, not a compelling twelve-month core holding; cash is preferable.",
  "price_at_decision": 7.67,
  "price_date": "2026-10-16",
  "research_note": "research/SHE-000783/2026-10-19.md",
  "triggers": [
    {"text": "TTM ROIC rises above 4.5% and keeps climbing, showing returns on capital are improving beyond one cyclical print.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 4.5}},
    {"text": "TTM net margin rises above 39.2%, showing the margin expansion is extending rather than fading.", "check": {"source": "statistics", "field": "profitMargin", "op": ">", "value": 39.2}},
    {"text": "FY2026 annual ROE (ratios page) comes in above the FY2025 9.1% for a second consecutive year, evidencing a higher through-cycle return base."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 10.78, "basis": "Trading upcycle persists and the market pays for the FCFE base fair value of 10.78 [fact sheet fair value]; the 16.46 bull value is set aside because it compounds FCF that swung 17%-281% of revenue [CF,IS]."},
    "base": {"probability": 0.45, "target_price_12m": 7.35, "basis": "Earnings fade from the 39.2% TTM net margin toward the FY2021-25 range, matching the P/E method's base of 7.35 [fact sheet fair value, IS]; below the FCFE base because that model rests on non-owner FCF [note section 5]."},
    "bear": {"probability": 0.3, "target_price_12m": 4.9, "basis": "A-share volumes and margin balances reverse, ROE drops back toward the 4.7%-5.0% of FY2023-24 [RA], consistent with the bear fair value of 4.90 [fact sheet fair value]."}
  },
  "entry_price": null,
  "entry_basis": "Conviction is below 3; the obstacle is cyclical, moat-less returns and unreliable FCF, not price alone.",
  "replaces": null,
  "replacement_reason": null
}
```

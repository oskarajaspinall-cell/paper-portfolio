# Evaluation: American Tower Corporation (AMT) — 2026-10-12
## Bear case
At a 5.22% 10y Treasury, a 4.66% FCF yield [ST] pays less than the risk-free rate [Certain]. AMT still carries 6.13x net debt/EBITDA [RA] and is refinancing now: senior notes were priced in September 2026 [Certain] while real yields are up 56bp in 3 months (macro overlay, FRED DFII10) [Certain]. The discount to its own 5-year range (EV/EBITDA 18.2x vs 19.1x min [RA]) mostly reflects a higher-rate world that those 2021-2025 multiples never had to price [Likely]. That makes the own-history P/FFO fair value (base 234.10) look too generous [Likely]. Management calls 2026 a trough year, with DISH churn and refinancing headwinds [Certain]. Margin and FCF-margin data are unavailable [data unavailable], so the 2027 inflection can't be checked from the figures [Certain]. The stock has lagged SPY by 17.5pp over 12 months [HI], and Q3 results on Oct 27 are a binary test [Likely].
## Bull case
Towers are an oligopoly asset with escalator-backed long-term leases, and CoreSite just posted record leasing (Q2 2026 call) [Likely]. Fundamentals are improving: ROIC has risen from 6.3% to 8.0% [RA], net debt/EBITDA has fallen from 8.50x to 6.13x [RA] and shares are down 0.19% YoY [ST] [Certain]. The stock trades below its 5-year minimum on P/E (25.1x vs 32.5x), EV/EBITDA and EV/Sales, and 24% under the peer median on EV/EBITDA [RA] [Certain]. Mechanical fair value is above the price in all three cases: bear 210.40, base 234.10, bull 266.91 [Certain]. A director bought shares in the open market in August and short interest fell 13.5% [ST] [Likely]. If real yields stabilise, AFFO growth re-accelerates in 2027 and the multiple re-rates toward peers [Guessing].
## Decision
```json
{
  "ticker": "AMT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A deleveraging tower oligopoly with rising ROIC trades below its own 5-year multiples, but a 4.66% FCF yield under a 5.22% risk-free rate, 6.1x leverage and rising real yields leave the re-rating dependent on the rate path rather than fundamentals.",
  "rationale": "The business quality and the deleveraging are real, but the discount to its own history is largely the rate regime, the FCF yield is below Treasuries, refinancing costs are rising and the macro tilt is toward bear. The probability-weighted upside is only mid-single-digit, and with Q3 due Oct 27 this is good but not compelling.",
  "price_at_decision": 182.24,
  "price_date": "2026-10-09",
  "research_note": "research/AMT/2026-10-12.md",
  "triggers": [
    {"text": "TTM ROIC falls below 6%, back toward the FY2022 trough of 4.6%, reversing the five-year improvement to 8.0%.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 6}},
    {"text": "TTM ROE falls below 12%, under the FY2023 trough of 12.4%, signalling returns are compressing under refinancing costs.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 12}},
    {"text": "Net debt/EBITDA (site definition, ratios page) rises back above 7x, reversing the deleveraging from 8.50x to 6.13x."},
    {"text": "Q3 2026 results (Oct 27) cut full-year AFFO guidance or push the flagged 2027 AFFO-per-share inflection out, showing churn/refinancing headwinds are not subsiding."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 234.1, "basis": "Real yields stabilise and the 2027 AFFO inflection flagged on the Q2 2026 call (/stocks/amt/transcripts/656096-q2-2026/) re-rates the stock to the P/FFO-proxy base fair value of 234.10 [fact sheet Fair value], still below the peer-median EV/EBITDA of 23.8x [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 196, "basis": "EV/EBITDA recovers only to its 5y minimum of 19.1x [RA] on TTM EBITDA with net debt at 6.13x [RA]; this is below the mechanical base fair value because the 2021-2025 multiples were set before the 10y yield reached 5.22% (macro overlay, FRED DGS10)."},
    "bear": {"probability": 0.35, "target_price_12m": 160, "basis": "The macro overlay's moderate tilt toward bear (real yields +56bp in 3m, FRED DFII10) raises the bear weight: higher refinancing costs on 6.13x leverage [RA] delay deleveraging and the stock retests its 52-week low of 160.06 [HI], below the mechanical bear fair value of 210.40, which does not capture a rising discount rate."}
  },
  "entry_price": null,
  "entry_basis": "The stock already trades below base fair value less 20% (234.10 x 0.8 = 187.28). The obstacle is the real-yield and refinancing path, plus unverified Q3 AFFO delivery, not the price: a lower price alone would not lift conviction to 4. Re-research on Q3 results or a fall in real yields.",
  "replaces": null,
  "replacement_reason": null
}
```

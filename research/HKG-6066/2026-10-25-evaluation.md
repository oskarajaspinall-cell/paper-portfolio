# Evaluation: CSC Financial Co., Ltd. (HKG:6066) — 2026-10-25
## Bear case
CSC is a cyclical mainland broker sitting at peak margins: operating margin 56.8% TTM against 40.2% in FY2021 [IS] [Certain], and earnings depend on China market turnover and policy [Likely]. Returns are poor and falling: ROIC 2.4% TTM, below any plausible cost of capital, and ROE down from 13.8% to 8.4% in FY2025 [RA] [Certain]. The 6.3x P/E is cheap only on peak earnings; P/B of 1.3x is 87% above the 0.7x peer median [RA] [Certain], so on book value it is the expensive name in a crowded, state-influenced industry with no visible moat [Likely]. The mechanical base fair value of 16.08 rests on an FCFE model fed by client-money swings (FCF margin from -91.5% to 358.3%) and carries no signal [Likely]. The stock is below both moving averages with 12-month relative strength of -33.8pp [HI] [Certain], and results on Oct 30, 2026 could show margin normalisation [Guessing].

## Bull case
The stock trades below the minimum of its own 5y P/E range (20.5x–29.1x) and P/B range (1.6x–2.5x) [RA] [Certain]. TTM ROE has recovered to 10.7% from 7.1% in FY2024 and net margin has risen to 44.7% [RA, IS] [Certain], so earnings momentum is real. The reverse DCF implies -12.6% year-1 revenue growth [Certain], a contraction the TTM trend does not show [Likely]. Regulatory market-stabilising measures announced this week could support turnover and issuance (https://www.scmp.com/business/china-business/article/3371701/chinas-stabilisation-pledge-did-not-lift-stocks-why-are-investors-praising-it) [Guessing]. Beta of 0.60 [ST] limits portfolio risk [Certain]. A re-rating towards the bottom of its own P/B range would lift the price materially [Guessing].

## Decision
```json
{
  "ticker": "HKG:6066",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 2,
  "thesis": "A low-return, cyclical mainland broker looks cheap on peak-margin earnings but not on book value versus peers, and its mechanical fair value rests on meaningless client-money cash flows.",
  "rationale": "ROIC 2.4% and ROE well below FY2021 show no durable value creation; margins are at a cyclical high and P/B sits far above peers. The FCFE fair value is not credible for a broker. Cheap P/E alone is not a compelling core case; conviction 2, no position.",
  "price_at_decision": 10.76,
  "price_date": "2026-10-23",
  "research_note": "research/HKG-6066/2026-10-25.md",
  "triggers": [
    {"text": "TTM ROE rises above 13.8% (the FY2021 level) and holds, showing returns can sustainably exceed the cost of equity.", "check": {"source": "statistics", "field": "roe", "op": ">", "value": 13.8}},
    {"text": "TTM ROIC rises above 3.4% (the FY2021 level), reversing the five-year decline in capital efficiency.", "check": {"source": "statistics", "field": "roic", "op": ">", "value": 3.4}},
    {"text": "TTM operating margin falls below 40%, back to FY2021-FY2023 levels, confirming the margin gain was cyclical and the bear case.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 40}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 13.25, "basis": "China stabilisation measures (SCMP URL in the note) lift turnover and P/B re-rates to its 5y minimum of 1.6x [RA], below the FCFE base fair value of 16.08 because broker FCF is client-money noise."},
    "base": {"probability": 0.45, "target_price_12m": 10.5, "basis": "Margins ease from the 56.8% TTM peak [IS] while P/E stays near the current 6.3x, in line with the 5.9x peer median [RA]; well below the mechanical base 16.08, which depends on FCF that the note shows is meaningless."},
    "bear": {"probability": 0.30, "target_price_12m": 8.25, "basis": "Operating margin reverts toward the 40.2% FY2021 level [IS] and P/B compresses toward the 0.7x peer median [RA], matching the fair-value bear of 8.25."}
  },
  "entry_price": null,
  "entry_basis": "Conviction 2: price is not the main obstacle; low ROIC, cyclical peak margins and an FCF-based fair value that carries no signal mean a lower price alone would not make this a conviction-4 BUY.",
  "replaces": null,
  "replacement_reason": null
}
```

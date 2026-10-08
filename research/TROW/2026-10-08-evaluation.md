# Evaluation: T. Rowe Price Group, Inc. (TROW) — 2026-10-08
## Bear case
This is a business in slow decline, and its valuation reflects that. Every quality metric has fallen over the five-year window: ROIC 35.5% to 21.6%, operating margin 48.8% to 33.4%, FCF conversion 104.2% to 75.3% [Certain] (fact sheet RA/IS/CF). FY2025 brought $56.9bn of net outflows. AUM still grew, but only because markets rose [Certain] (10-K). Management itself says passive managers are taking share [Certain]. Outflows continued in 2026 [Certain] (Q2 transcript; August AUM release [OV]). Fees are a percentage of AUM, and beta is 1.47 [Certain] [ST], so a market drawdown cuts earnings and the multiple at the same time. Real yields have risen +0.61pp in 3m (macro overlay) [Certain]. Short interest is 13.12% and rising, and Piotroski is only 4 [Certain] [ST]. Being below the 5-year P/E floor fits a lasting de-rating as well as a bargain [Likely].
## Bull case
The price already assumes the decline continues. P/E is 10.4x and EV/EBITDA 6.6x, both below their own 5-year minimums (11.0x / 7.2x). That is about half the peer median of 22.1x / 12.8x [Certain] (fact sheet RA, peers). The FCF yield is 7.54% and the balance sheet is net cash at -0.94x EBITDA [Certain] [ST][RA]. Share count fell 2.09% YoY, so holders earn a return without any re-rating [Certain] [ST]. Returns have held at about 20% since the FY2023 trough of 16.5% [Certain] [RA]. ETF and fixed-income inflows, large mandates (Q2 transcript [OV]) and the F/m Investments ETF/SMA deal [OV] could slow net outflows [Guessing]. If outflows stabilise, a return to the 5-year median 13.8x P/E is a large re-rating [Likely].
## Decision
```json
{
  "ticker": "TROW",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A net-cash active manager trades below its own 5-year minimum P/E and EV/EBITDA at a 7.54% FCF yield, but structural passive-driven outflows and five years of falling returns and margins make the discount look earned rather than mispriced.",
  "rationale": "Cheap on every measure and net cash, but nothing yet shows the outflows have turned. Margins, ROIC and cash conversion are still trending down, Piotroski is 4 and short interest is rising. With 1.47 beta, upside depends on a re-rating with no visible catalyst. That is good but not compelling: conviction 3, so AVOID. Cash is acceptable.",
  "price_at_decision": 104.07,
  "price_date": "2026-10-07",
  "research_note": "research/TROW/2026-10-08.md",
  "triggers": [
    {"text": "TTM operating margin recovers above the FY2022 level of 36.8%, showing fee and cost pressure has reversed. That would warrant re-initiation as a possible BUY.", "check": {"source": "statistics", "field": "operatingMargin", "op": ">", "value": 36.8}},
    {"text": "TTM FCF margin recovers above the FY2022 level of 32.7%, showing cash conversion is rebuilding rather than eroding.", "check": {"source": "statistics", "field": "fcfMargin", "op": ">", "value": 32.7}},
    {"text": "TTM net margin falls below 25%, through the FY2022 five-year low of 24.0%, confirming the bear case that outflows are overwhelming scale.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 25}},
    {"text": "Company month-end AUM releases or quarterly results report net inflows for two consecutive quarters, showing the passive-share loss has stabilised."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 138, "basis": "Outflows stabilise on ETF/SMA growth (F/m deal [OV]), so P/E returns to its 5y median of 13.8x [RA] on TTM earnings implied by the current 10.4x; the macro tilt is neutral/small (overlay), so this scenario is unchanged."},
    "base": {"probability": 0.45, "target_price_12m": 110, "basis": "Outflows continue at a pace offset by buybacks (-2.09% shares [ST]), and P/E drifts back to its 5y minimum of 11.0x [RA] on flat TTM earnings."},
    "bear": {"probability": 0.30, "target_price_12m": 85, "basis": "Passive share loss plus a high-beta (1.47 [ST]) market drawdown push net margin from 29.3% to its FY2022 low of 24.0% [IS] at an unchanged 10.4x P/E [RA], near the 52-week low of 85.22 [HI]."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

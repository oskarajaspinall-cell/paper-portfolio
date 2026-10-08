# Evaluation: Expedia Group, Inc. (EXPE) — 2026-10-07
## Bear case
The headline cheapness is weaker than it looks. EV/EBITDA of 10.3x is only 4% below the peer median of 10.7x, so the 40% P/E discount mostly reflects the market's view of the business, not mispricing [Certain]. FCF/NI of 219% TTM likely includes merchant-booking working-capital float, so the 14.29% FCF yield overstates owner earnings [Likely]. AI trip-planning agents could take over the top of the funnel. Expedia joining Meta's Muse may protect volume but give up take rate, and Muse coverage is already hitting the OTA peers [Likely]. Short interest rose 20.9% in a month [Certain]. The macro overlay tilts small toward bear: real yields rose 0.71pp in 3m and HY spreads widened 0.44pp in 1m, which pressures discretionary travel for a beta-1.36 stock [Certain]. Altman Z of 1.45 needs watching [Likely].
## Bull case
Five years of steady improvement: operating margin rose from 3.0% to 17.4% TTM, gross margin from 82.3% to 90.4%, and the balance sheet went from 9.38x net debt/EBITDA to net cash [Certain]. The P/E of 16.2x is below the 5-year minimum of 19.4x, and P/FCF is 7.0x against a peer median of 12.2x [Certain]. Buybacks cut the share count 6.17% YoY, and $5.7bn of authorization remains [Certain]. Piotroski F is 7 [Certain]. If Q3 results on Nov 5 show bookings holding through the Muse integration, the AI discount could unwind toward the 5y minimum multiple [Guessing].
## Decision
```json
{
  "ticker": "EXPE",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "An OTA whose margins have improved and whose balance sheet is now net cash trades below its 5-year P/E range, but the discount mostly reflects an unresolved AI-agent disintermediation risk and a cash flow figure helped by working capital, not clear mispricing.",
  "rationale": "Quality and buybacks are real, but EV/EBITDA is in line with peers. FCF looks helped by merchant float, and AI agents (Muse) threaten take rate with no evidence yet either way. The macro overlay tilts small toward bear and short interest is rising. Good but not compelling: conviction 3, below the buy threshold of 4. Hold cash.",
  "price_at_decision": 260.07,
  "price_date": "2026-10-06",
  "research_note": "research/EXPE/2026-10-07.md",
  "triggers": [
    {"text": "TTM gross margin falls below 85%, signalling take-rate erosion from AI-agent disintermediation.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 85}},
    {"text": "TTM operating margin falls below the FY2025 level of 14.7%, reversing the five-year expansion.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 14.7}},
    {"text": "TTM FCF margin falls below the FY2025 level of 21.1%, showing the cash flow step-up was working-capital timing.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 21.1}},
    {"text": "Q3 2026 results or filings show the Muse/AI-agent channel is lowering B2C take rate or direct traffic share."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 311, "basis": "AI fears ease after Q3 results and the P/E re-rates from 16.2x to its 5y minimum of 19.4x on unchanged TTM earnings [RA]."},
    "base": {"probability": 0.45, "target_price_12m": 276, "basis": "The P/E holds at 16.2x [RA] while the 6.17% YoY share-count reduction [ST] lifts per-share earnings by about that much."},
    "bear": {"probability": 0.30, "target_price_12m": 182, "basis": "AI-agent disintermediation plus the macro overlay's small bear tilt (real yields and HY spreads widening; research/EXPE/2026-10-07-macro.md) push P/FCF from 7.0x to its 5y minimum of 4.9x [RA]; bear weight raised by 0.05 for the overlay."}
  },
  "replaces": null,
  "replacement_reason": null
}
```

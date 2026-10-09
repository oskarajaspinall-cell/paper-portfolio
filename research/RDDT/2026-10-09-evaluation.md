# Evaluation: Reddit, Inc. (RDDT) — 2026-10-09
## Bear case
At 36.5x P/E and 34.1x EV/EBITDA, RDDT sits 34-43% above the peer median (27.2x / 23.9x) [Certain] (ST, P:). That premium needs the newest, highest-margin stream, AI data licensing, to keep growing. Yet a headline flags a lower chance that the Google arrangement renews on current terms [Guessing], and Google is piloting payments to publishers for AI Overviews (TheFly, 2026-09-15) [Likely]. Dilution of 8.43% YoY eats into per-share value [Certain] (ST). The fact sheet's "cheap vs own history" signal (EV/Sales 9.8x vs a 18.8-20.7x range) only reflects the post-IPO years, and the DCF is unavailable [Certain]. Beta of 2.05 with real yields up 0.61pp in 3 months is a live multiple headwind (macro overlay) [Likely]. Short interest is 14.11%, up 17.6% m/m [Certain]. The stock is 6.3% below its 200-day MA, and earnings land on Oct 29 [Certain].
## Bull case
The FY2025 inflection is real and still building. Operating margin went from -43.1% (FY2024) to 28.2% TTM, FCF margin is 36.7% and ROE 30.7%, all rising [Certain] (IS, CF, RA). Gross margin of 91.4% and net cash (net debt/EBITDA -3.45x) give room to self-fund [Certain]. P/FCF of 29.6x matches peers (29.4x) despite faster growth [Certain] (RA, P:). The Anthropic contract ruling and the ending of free API/RSS access show Reddit can defend and charge for its data [Likely] (Barron's 2026-09-21; TechCrunch 2026-09-30). Third-party data showed August user growth at a 2026 high [Guessing]. The stock is already 24.0% lower over 12 months, so part of the licensing risk may be in the price [Likely] (ST).
## Decision
```json
{
  "ticker": "RDDT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A newly profitable, 91%-gross-margin community platform with 36.7% FCF margin and net cash, but its premium P/E rests on an AI data-licensing stream whose largest renewal is in doubt.",
  "rationale": "Quality is improving fast, but at a 34-43% earnings premium to peers, an unresolved Google licensing renewal, 8.43% dilution and a moderate bearish macro tilt for a 2.05-beta stock, the reward does not compensate. The fair value is EV/Revenue-only, built on post-IPO multiples. Good but not compelling, so we avoid it.",
  "price_at_decision": 156.47,
  "price_date": "2026-10-08",
  "research_note": "research/RDDT/2026-10-09.md",
  "triggers": [
    {"text": "TTM operating margin falls below 15%, reversing the FY2025 inflection (28.2% TTM).", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 15}},
    {"text": "TTM gross margin falls below 85%, showing that licensing or ad monetization is weakening.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 85}},
    {"text": "TTM FCF margin falls below 20%, giving up most of the step-up from 16.6% (FY2024) to 36.7%.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 20}},
    {"text": "Company results or filings confirm that the Google AI data-licensing arrangement has renewed on equal or better terms, removing the main thesis risk (would raise conviction)."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 208.0, "basis": "The licensing arrangement renews and the 28.2% TTM operating margin [IS] keeps expanding, so the 36.5x P/E [RA] holds on higher earnings and the price returns to the 6-month high of 208.05 [HI]. This is still well below the mechanical EV/Revenue fair value of 297.75, which rests on post-IPO multiples only."},
    "base": {"probability": 0.45, "target_price_12m": 160.0, "basis": "P/FCF stays at peer parity (29.6x vs 29.4x [RA, P:]) while FCF growth is largely offset by 8.43% dilution [ST]. Below the 284.26 base fair value because that EV/Revenue model applies the 18.8-20.7x IPO-era range against a 5.3x peer median [RA]."},
    "bear": {"probability": 0.30, "target_price_12m": 115.0, "basis": "The Google renewal fails or reprices (TheFly 2026-09-15 headline) and the P/E de-rates to the 27.2x peer median [RA, P:], near the 119.27 52-week low [HI]. Probability raised from 0.25 to 0.30 (bull cut from 0.30) for the macro overlay's moderate tilt toward bear (rising real yields on a 2.05-beta stock, research/RDDT/2026-10-09-macro.md)."}
  },
  "entry_price": 116.6,
  "entry_basis": "The P/E would be back at the 27.2x peer median [RA, P:] (156.47 x 27.2/36.5), close to the 119.27 52-week low [HI]. The default base 284.26 x 0.8 = 227.41 is above the price, because the EV/Revenue fair value is built on post-IPO multiples only and is unreliable.",
  "replaces": null,
  "replacement_reason": null
}
```

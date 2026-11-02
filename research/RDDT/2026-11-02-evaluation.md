# Evaluation: Reddit, Inc. (RDDT) — 2026-11-02
## Bear case
The fall was caused by results, not by noise. Q3 global DAUq was flat sequentially and US DAUq fell 5% sequentially and 2% year on year, with growth coming from lower-ARPU rest of world [company-reported] (https://www.sec.gov/Archives/edgar/data/1713445/000171344526000116/rddt-20260930.htm). [Certain] Management guided weakly and said search traffic was "down meaningfully" (https://www.cnbc.com/2026/10/30/reddit-stock-q3-earnings.html). [Likely] Google AI summaries cut the logged-out, search-referred visitors that fill much of the ad inventory. The move to logged-in only may lose more of them. [Likely] New Risk Factors name Google, Meta, OpenAI and Anthropic as rivals and warn that licensing deals may not be renewed. [Certain] Some user growth is bought with marketing, and the share count rose 3.49% [ST]. [Certain] Even after the fall, P/FCF of 14.8x and EV/EBITDA of 15.9x sit above the peer medians of 10.8x and 13.8x [RA]. [Certain] The traffic source looks structurally impaired. [Likely]

## Bull case
The business is still very profitable and growing fast. Q3 revenue was $895.0m, up 53%, and ARPU rose 36% on pricing [company-reported] (same filing). [Certain] Gross margin is 91.5%, operating margin 29.4%, TTM FCF margin 38.8% and FCF/NI 120.8%, with net cash (net debt/EBITDA -3.25x) [IS,CF,RA]. [Certain] P/E of 19.3x is below the peer median of 21.1x and the FCF yield is 6.76% [RA,ST]. [Certain] Every multiple sits far below its own 5y minimum. [Certain] With RSI at 19.2, short interest at 15.28% of float and up 8.8% on the month, positioning is washed out, so any sign that US users are stabilising could cause a sharp re-rating. [Guessing] Logged-in users monetise better and are more valuable to advertisers and licensors. [Guessing] The plaintiff "investigation" is a solicitation, not a filed case. [Likely]

## Decision
```json
{
  "ticker": "RDDT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A highly profitable, net-cash community platform is now cheap on earnings, but its US logged-out traffic source is being disintermediated by AI search, and the Q3 results showed that impairment rather than a one-off miss.",
  "rationale": "The fall answers the question behind the earlier AVOID instead of removing it: US DAUq fell year on year and guidance was weak because search traffic is falling. Margins and cash flow are intact, so this is not conviction 1-2, but cheapness without evidence that users are stabilising is good-not-compelling. No position.",
  "price_at_decision": 91.73,
  "price_date": "2026-10-30",
  "research_note": "research/RDDT/2026-11-02.md",
  "triggers": [
    {"text": "US DAUq (10-Q MD&A) grows year on year again in the next quarterly filing, showing the search-traffic loss has been absorbed; a second year-on-year decline, or global DAUq falling because of logged-in only, confirms the AVOID."},
    {"text": "A content-licensing deal is disclosed as not renewed or materially repriced (10-Q or 8-K), removing a high-margin revenue line."},
    {"text": "TTM operating margin falls below 20%, back to the FY2025 level, showing ad pricing can no longer offset weaker traffic.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM gross margin falls below 85%, back to FY2021-22 levels, signalling weaker ad yield or rising hosting costs per user.", "check": {"source": "statistics", "field": "grossMargin", "op": "<", "value": 85}}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 149.0, "basis": "US DAUq stabilises and logged-in conversion holds, so the price returns to around its 50-day average of 149.17 [ST,HI], still well below the IPO-era EV/Sales range (18.8x-20.7x [RA]) that drives the mechanical fair value."},
    "base": {"probability": 0.45, "target_price_12m": 100.0, "basis": "Revenue growth slows but margins hold (operating margin 29.4% [IS]); P/E moves to the peer median of 21.1x from 19.3x [RA]. This sits far below the mechanical base of 316.29 because that EV/Revenue value applies IPO-era multiples to growth from before the reset (note, section 3)."},
    "bear": {"probability": 0.30, "target_price_12m": 67.0, "basis": "US DAUq keeps declining and logged-in only reduces ad inventory (note, section 6), so P/FCF falls from 14.8x to the peer median of 10.8x [RA]; the mechanical bear of 301.25 ignores this traffic impairment."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle. The open question is whether US search-referred traffic and DAUq stabilise after AI summaries and the logged-in-only move, so a lower price on the same evidence would not justify conviction 4. The mechanical base x 0.8 is also above the current price. Re-research when the next 10-Q shows US DAUq.",
  "replaces": null,
  "replacement_reason": null
}
```

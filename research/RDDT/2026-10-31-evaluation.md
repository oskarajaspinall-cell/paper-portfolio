# Evaluation: Reddit, Inc. (RDDT) — 2026-10-31
## Bear case
The fall is a thesis event, not noise. The Q3 10-Q added risk factors on falling search-engine referrals, AI answers substituting for visits, scraping that undermines licensing and a logged-in-only experiment [Certain]. US DAUq fell 5% quarter on quarter and global DAUq was flat [company-reported] (https://www.sec.gov/Archives/edgar/data/1713445/000171344526000116/rddt-20260930.htm), so growth now rests on ad price, up about 34% [company-reported], which cannot outrun a shrinking audience for long [Likely]. Guidance was weak and management warned user growth could weaken further in Q4 [Likely]. The trailing P/E of 18.7x and 6.76% FCF yield are struck on profits earned before the traffic loss shows in the numbers [Likely]. Distribution is controlled by Google and AI engines, a dependence Reddit cannot fix itself [Likely]. Beta 2.05, short interest 15.36% and rising, plus law-firm solicitations, add gap risk [Certain]. The mechanical fair value (base 316.29) rests on IPO-era sales multiples and is unusable [Likely].

## Bull case
Reddit's corpus of human discussion is scarce, and AI companies pay to license it [Likely]. The economics are outstanding: gross margin 91.5%, operating margin 29.4%, FCF margin 38.8%, FCF conversion 120.8% and net cash [Certain]. At 18.7x P/E and 15.9x EV/EBITDA it trades well below the peer medians of 43.5x and 25.2x [Certain]. Global DAUq is still up 12% year on year [company-reported], and ad pricing up about 34% [company-reported] shows advertisers value the audience [Likely]. Logged-in-only could raise monetisation per user and protect the data from scrapers [Guessing]. With RSI at 17.5 and the price at its 52-week low of 89.28, sentiment is washed out and a stabilisation in traffic could re-rate it sharply [Guessing].

## Decision
```json
{
  "ticker": "RDDT",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "Reddit's exceptional margins and net cash look cheap on trailing profits, but its audience, the source of those profits, is now visibly shrinking in the US as search and AI answer engines divert traffic, so the earnings base itself is in question.",
  "rationale": "The drop is driven by a real fundamental break, not an overreaction: US DAUq is falling, guidance is weak and the 10-Q adds structural traffic risks. Trailing multiples are cheap but rest on pre-erosion profits. Good business, not a compelling one until traffic stabilises; a lower price alone would not fix that.",
  "price_at_decision": 91.73,
  "price_date": "2026-10-30",
  "research_note": "research/RDDT/2026-10-31.md",
  "triggers": [
    {"text": "Evidence the audience has stabilised: US DAUq (10-Q, MD&A) stops declining quarter on quarter for two consecutive quarters, which would remove the main obstacle; conversely, another decline of more than 5% quarter on quarter confirms the break."},
    {"text": "Content-licensing deals are not renewed or disclosed as lost (10-Q Risk Factors / MD&A), undercutting the AI-data leg of the moat."},
    {"text": "TTM operating margin falls below 20%, showing traffic loss is reaching profitability.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 20}},
    {"text": "TTM FCF margin falls below 25%, showing cash generation is eroding with the audience.", "check": {"source": "statistics", "field": "fcfMargin", "op": "<", "value": 25}}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 141, "basis": "Logged-in-only and ad pricing offset the search loss and US DAUq stabilises, so the shares recover toward the September swing lows near 141.32 [HI], still a P/E below the peer median of 43.5x [RA]; far below the mechanical fair value, which rests on IPO-era sales multiples (note section 3)."},
    "base": {"probability": 0.45, "target_price_12m": 92, "basis": "Traffic keeps softening while ad price growth holds earnings roughly flat, so P/FCF stays near today's 14.8x [RA] against the peer median of 12.8x [RA]; the EV/Revenue fair value (base 316.29) is ignored as its 5y range is from loss-making IPO years."},
    "bear": {"probability": 0.35, "target_price_12m": 70, "basis": "US DAUq falls again as guided user weakness and AI substitution deepen (10-Q, https://www.sec.gov/Archives/edgar/data/1713445/000171344526000116/rddt-20260930.htm), earnings decline and the multiple compresses below the peer P/FCF median of 12.8x [RA]."}
  },
  "entry_price": null,
  "entry_basis": "Price is not the obstacle: the audience is shrinking and the 10-Q flags structural search/AI traffic risk, so trailing profits are not a reliable base; a lower price would not change the decision. Re-research when the 10-Q shows US DAUq stabilising.",
  "replaces": null,
  "replacement_reason": null
}
```

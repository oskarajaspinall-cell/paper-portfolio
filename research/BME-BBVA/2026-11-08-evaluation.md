# Evaluation: Banco Bilbao Vizcaya Argentaria (BME:BBVA) — 2026-11-08
## Bear case
The re-rating is done: P/B of 2.0x sits above its 5y max of 1.8x (median 0.9x) and P/E of 11.3x is at its 5y high, a 41% P/B premium to peers [Certain]. The industry's best method (P/B + ROE) gives a base of 19.47 EUR, below the 22.73 close [Certain]. The blended +10.2% upside leans on an FCFE DCF built from bank cash flow, which swings with the balance sheet [Likely]. The **Direction change** line shows FCF margin 46.6pp below its 2-year high of 97.2%. That is balance-sheet noise, not business decline, but shows the FCFE input is unreliable; it does not threaten the ROE thesis [Likely]. Mexico is the main market: the peso is about 5% weaker against the euro in ~3m and the VIX has jumped to 28.2, so translation drag and a higher risk premium hit a stretched multiple (macro overlay) [Likely]. Turkey and Argentina asset quality are watchpoints [Likely].

## Bull case
ROE has compounded from 10.8% (FY2021) to 19.8% TTM, and net margin from 25.0% to 32.6% [Certain]. Q3 profit growth was led by Mexican and Spanish lending, and full-year ROTE guidance was raised [Likely]. A bank earning close to 20% on equity can justify well above 1x book, and the peer premium on P/E is only 6% [Certain]. The buyback's second tranche is running and the share count fell 3.24% YoY, so per-share book and earnings compound even at a flat multiple [Certain]. P/FCF of 6.9x and a 14.52% FCF yield look cheap, if noisy [Likely]. The mechanical bull of 31.23 EUR is reachable if ROE holds and the peso steadies [Guessing]. Still, the evidence describes a high-quality bank fairly priced, not a mispriced one: good but not compelling.

## Decision
```json
{
  "ticker": "BME:BBVA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-ROE Spanish-Mexican bank with rising profitability and buybacks, but its P/B and P/E already sit above their own 5-year ranges and the industry's best fair-value method puts base value below the price, leaving a balanced rather than compelling skew.",
  "rationale": "Quality is real and improving, but the re-rating has already happened: P/B is above its 5y max and P/B + ROE base value is below the price. Upside rests on a noisy FCFE DCF, and the macro overlay tilts toward the bear case on the peso and volatility. Conviction 3: AVOID, with an entry price below.",
  "price_at_decision": 22.73,
  "price_date": "2026-11-06",
  "research_note": "research/BME-BBVA/2026-11-08.md",
  "triggers": [
    {"text": "TTM ROE falls below 15% (19.8% now), giving up most of the rise from 10.8% in FY2021 and breaking the high-return thesis.", "check": {"source": "statistics", "field": "roe", "op": "<", "value": 15}},
    {"text": "TTM net margin falls below 28% (32.6% now), signalling credit costs or margin pressure in Mexico, Turkey or Argentina.", "check": {"source": "statistics", "field": "profitMargin", "op": "<", "value": 28}},
    {"text": "Shares outstanding stop shrinking (YoY change above 0%, -3.24% now), signalling the buyback has ended or capital is being raised.", "check": {"source": "statistics", "field": "sharesgrowthyoy", "op": ">", "value": 0}},
    {"text": "Quarterly net profit on the income statement page declines year on year for two consecutive quarters, or CET1 falls toward the 9.36% SREP requirement."}
  ],
  "scenarios": {
    "bull": {"probability": 0.2, "target_price_12m": 29.0, "basis": "ROE holds near 19.8% TTM [RA] with buybacks shrinking the share count [ST] and the peso steadying, so the premium P/B holds and earnings compound; below the mechanical bull of 31.23 [fact sheet Fair value], and probability cut by the overlay's small toward-bear tilt (research/BME-BBVA/2026-11-08-macro.md)."},
    "base": {"probability": 0.5, "target_price_12m": 24.0, "basis": "Raised ROTE guidance (https://stockanalysis.com/quote/bme/BBVA/transcripts/660051-q3-2026/) grows book while P/B drifts from 2.0x toward the 1.8x top of its 5y range [RA]; below the mechanical base of 25.04 because that blend leans on the FCFE DCF of 36.17 built on volatile bank cash flow [CF], against a P/B + ROE base of 19.47."},
    "bear": {"probability": 0.3, "target_price_12m": 15.99, "basis": "The peso keeps sliding and the VIX stays high (research/BME-BBVA/2026-11-08-macro.md) while Turkey/Argentina asset quality worsens, so P/B compresses toward the 1.4x peer median [RA]: the mechanical bear fair value of 15.99 [fact sheet Fair value]; probability raised for the overlay's small toward-bear tilt."}
  },
  "entry_price": 20.03,
  "entry_basis": "valuation file: base 25.04 x 0.8; near the P/B + ROE base of 19.47, where the industry's best method would no longer show the price above value.",
  "replaces": null,
  "replacement_reason": null
}
```

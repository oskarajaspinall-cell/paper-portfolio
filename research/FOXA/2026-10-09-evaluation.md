# Evaluation: Fox Corporation (FOXA) — 2026-10-09
## Bear case
The re-rating has already happened: P/E 16.6x, P/FCF 18.1x and P/B 2.3x all sit above their own 5-year maxima, and the price of 63.57 is above the mechanical base fair value of 58.52 [Certain] [RA, Fair value]. Cash quality slipped in FY2026: FCF margin fell from 18.4% to 8.6% and FCF/NI from 132.3% to 87.1% [Certain] [CF,IS]. The $22bn Roku acquisition, nearly the size of the 26.5bn market cap, is under a DOJ second request [Certain] (https://www.reuters.com/legal/litigation/us-justice-department-widens-probe-into-foxs-roku-deal-semafor-reports-2026-09-08/). If it closes, it would turn a 0.87x net-leverage balance sheet into a leveraged integration story [Likely]. If it is blocked, the digital-growth narrative behind the recent +19.1% 3-month move fades [Guessing]. A possible News Corp re-merger adds governance uncertainty [Guessing]. Short interest is 13.66% of float [Certain] [ST].
## Bull case
The business keeps getting better: ROIC has risen to 17.4% and operating margin to 20.3%, with Piotroski 7 and Altman Z 3.31 [Certain] [RA,IS,ST]. Fox News and its exclusive NFL/MLB/Big Ten rights are scarce assets, and Tubi and FOX One add digital growth [Likely]. Buybacks cut the share count 4.77% YoY [Certain] [ST]. On P/E and EV/EBITDA the stock trades at a 34-38% discount to media peers [Certain] [RA,P]. The reverse DCF implies only 4.9% year-1 revenue growth, which is not demanding [Certain] [Fair value]. The FY2026 FCF dip may reflect one-off deal costs [Guessing]. If Roku closes with the promised synergies and rapid deleveraging, the bull fair value sits far above the price [Guessing].
## Decision
```json
{
  "ticker": "FOXA",
  "decision": "AVOID",
  "position_type": "CORE",
  "conviction": 3,
  "thesis": "A high-quality, improving sports-and-news franchise whose multiples already sit above their own 5-year range while a transformational $22bn Roku deal under DOJ second request leaves leverage and strategy unresolved.",
  "rationale": "Quality is real and improving, but price is above base fair value and above its own 5-year multiple range. FCF conversion fell to 87.1%, and the pending Roku deal, close to the size of the whole company, makes the next-12-month balance sheet unknowable. Good but not compelling, so no position; cash is acceptable.",
  "price_at_decision": 63.57,
  "price_date": "2026-10-08",
  "research_note": "research/FOXA/2026-10-09.md",
  "triggers": [
    {"text": "TTM ROIC falls below 12%, under the FY2024 level of 12.2%, showing the returns expansion has reversed.", "check": {"source": "statistics", "field": "roic", "op": "<", "value": 12}},
    {"text": "TTM operating margin falls below 17%, under the FY2024 level of 17.5%, signalling cord-cutting is no longer offset by Tubi/FOX One.", "check": {"source": "statistics", "field": "operatingMargin", "op": "<", "value": 17}},
    {"text": "Net debt/EBITDA (balance sheet + income statement) rises above 2.0x, e.g. on a debt-funded Roku close, versus 0.87x today."},
    {"text": "The Roku acquisition is blocked or abandoned, or closes on terms that remove the stated rapid-deleveraging path, as disclosed in an SEC 8-K."}
  ],
  "scenarios": {
    "bull": {"probability": 0.25, "target_price_12m": 76.39, "basis": "Roku clears DOJ review and buybacks continue (-4.77% shares [ST]), so the stock retests its 52-week high of 76.39 [HI]; this is set well below the mechanical bull of 112.58 because that DCF bull (141.02) assumes growth the FY2026 FCF drop to 8.6% [CF] does not support."},
    "base": {"probability": 0.45, "target_price_12m": 60.05, "basis": "Multiples drift back toward the top of their own range as the deal overhang persists, landing at the DCF base of 60.05 [Fair value], in line with the blended base of 58.52."},
    "bear": {"probability": 0.30, "target_price_12m": 50.75, "basis": "A contested Roku close adds leverage or a block removes the digital story, so EV/EBITDA reverts toward its 5y median of 7.1x [RA], consistent with the bear fair value of 50.75 [Fair value]."}
  },
  "entry_price": 46.82,
  "entry_basis": "valuation file: base 58.52 x 0.8; at that level the multiples would sit back inside their own 5-year range [RA], compensating for the unresolved Roku leverage risk.",
  "replaces": null,
  "replacement_reason": null
}
```

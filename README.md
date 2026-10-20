# Paper Portfolio

Paper Portfolio is a hands-off, simulated stock portfolio that runs itself every week, on your own Mac or on GitHub Actions. A Python screen scores thousands of stocks on quality, valuation and momentum. Claude agents then research the best ideas, argue the bear case before the bull case, and must reach a firm decision with a conviction level. Simple scripts handle everything else: prices, position sizing, trading costs, stop-losses and returns, so no maths is left to the AI. Every decision is logged and scored against the S&P 500 at 1, 3, 6 and 12 months, building an honest track record. It's paper trading only, with no broker connection. Fork it, add your own Claude key, and choose your own stocks.

**📊 Live dashboard:** https://oskarajaspinall-cell.github.io/paper-portfolio/ (updated every 15 minutes while markets are open, and after every run)

> **Paper trading only. Not investment advice.** There is no broker connection, no real orders and no
> broker credentials anywhere in this project. Prices and financials are read from
> [stockanalysis.com](https://stockanalysis.com); the scraper respects its robots.txt and makes at most
> one request every 3 seconds. If you run it, you are responsible for using that site within its terms.

This repository ships **paused** (there is a `PAUSED` file), so nothing runs until you set up your own copy.

---

## What happens each week

| Step | What it does | Uses AI? |
|---|---|---|
| **Weekly screen** | Rebuilds the stock list (default: S&P 500 + FTSE 100 + the ~3,800 largest stocks worldwide) drops stocks too thin to trade (under $10M a day traded, or under 20% free float), scores the rest on quality, valuation and momentum, with a 5-year history check on the top 500. Picks 10 core + 10 tactical ideas. Tactical ideas are one of two setups: **post-earnings drift** (a stock that just beat and jumped on heavy volume) or **pullback in an uptrend** (a strong stock that has dipped back to its 50-day average), each with a volatility-based stop, a target at least 2× the risk, and a size that limits a stop-out to ~1% of the portfolio. ~4 hours with the default list. | No |
| **Weekly review** | Fills last week's orders; checks every holding; sells tactical positions that hit their stop, target or time limit; reviews holdings that moved >8% or reported results (using recent headlines); fully re-researches any core holding whose thesis broke; researches the screen's 20 picks (3 at a time; a failed one is skipped and listed); places orders for the next open; updates the decision log, report and dashboard. | Only for flagged holdings and new research |
| **Daily update** (weekdays) | Fills pending orders at their opening price, credits dividends and applies splits, re-prices every holding at its latest close, checks entry prices, re-checks the dip release of the cash reserve, runs the dip radar, places any queued buys that now fit (funding queue), and refreshes the dashboard. | No |
| **Intraday check** (weekdays, ~10:30 New York) | Live prices vs entry prices for US watch stocks; hits, and last night's dip-radar signals, are re-researched at once. | Only for hits |
| **Research loop** (when you start it) | Works through the whole ranked universe, 3 stocks at a time, best first, until it's done or the usage limit stops it (`bin/research-loop`, see below). | Yes |

| Schedule | On your Mac (`bin/install-mac-schedule`) | On GitHub Actions (UTC) |
|---|---|---|
| Screen + review | Friday 22:00, one script (`bin/weekly-local`) | Screen Friday 21:00, review Saturday 08:00 |
| Daily update | Weekdays 21:30 UK (`bin/fill-pending`) | Weekdays 21:30 |
| Intraday check | Weekdays 14:30 + 15:30 UK (`bin/entry-intraday`; acts once, ~10:30 New York) | – |
| Live dashboard | Every 15 min, weekdays 08:00–21:15 UK (`bin/live-dashboard`) | – |

**Only high-conviction ideas are bought** (4 or 5 out of 5); the rest are recorded as AVOID, so cash can stay
high for a while. **Core positions are sized by conviction and volatility**: 7% (conviction 4) or 10% (5), scaled down
for a volatile stock and up for a steady one (between 0.6× and 1.4×; never so far up that it eats into the cash reserve), so one jumpy name can't dominate the
portfolio's risk; a weekly risk table (`reports/risk/`) shows each holding's share of the portfolio's volatility.
A weekly **return attribution** (`reports/attribution/`) splits the return over the S&P 500 into sector bets
(including the cash reserve), stock picking within sectors and their interaction, so a sector tailwind can't hide
weak stock picks. **Trades fill at the live price or the next open**: a decided trade fills at once at the live price when its
market is open, otherwise it becomes a pending order filled at the next opening price (every rule is checked
again at that price); a tactical order that opens beyond its stop or target is cancelled.
**Cash is managed as a position**: each week eight official indicators (credit spreads and their change, VIX, the
yield curve, real yields, the S&P 500's trend, core inflation and fed rate moves) are each scored on a sliding scale
from calm to stressed and combined into a 0–100 stress score. That sets a cash reserve anywhere from 5% to 35%,
moving at most 5 points a week, and an AI macro step may add or take away 5 points with cited official sources.
New buys can't spend the reserve; nothing is sold to reach it. When the S&P 500 drops 10% (20%) below its 52-week high, half (all) of the
reserve is released to buy the dip. The regime is set weekly, but the dip check runs every weekday evening, so
a sell-off frees the reserve for the next morning's open.
A high-conviction buy that the reserve blocks is not thrown away: it waits in a **funding queue** and is bought
automatically at the next open once there is room above the reserve (it drops out after 30 days or if the price
runs 10% above where it was decided). If there is room for at least half a position, the best idea starts with a
smaller starter position straight away and is topped up as more room appears. Each week an AI step also checks whether the best waiting idea is clearly
better than the weakest holding and, if so, swaps them.
**Buying dips in stocks we know**: every weekday night a dip radar checks the holdings and every stock we recently
rated "good but not now" (conviction 3+). If one has fallen unusually since we last researched it — more than its
own volatility and the market's move explain — and the price is at or below our fair value, it is re-researched
the next day. Holdings get an "add to it?" review. A fall alone never triggers a buy: the research decides.
Concentration is capped by rule: no sector above 30%, and China + Hong Kong combined (companies that report in
yuan or Hong Kong dollars) no more than 25%. The AI judges each stock on its own merits; the rules handle the mix.
Uninvested **cash earns interest** at a flat 3.8% AER (set in `CLAUDE.md` `[cash]`), credited daily on each
day's closing cash balance and logged in `portfolio/interest.csv`.
Every fact sheet includes a **fair value**: the industry-appropriate method from
`valuation/industry_methods.csv` (e.g. DCF for software, P/B + ROE for banks and insurers, EV/EBITDA when a
mine or reserve NAV isn't available), with bear/base/bull assumptions taken from the stock's own five-year history,
a discount rate of the 10-year Treasury yield + beta × 5%, and a reverse DCF showing the growth the price implies.
It informs the research only (no buy rule) and is logged with each decision so its accuracy can be checked later.
The one exception is the bulk research loop. A stock priced above its base fair value is **pre-screened
out** there before any AI research (`scripts/prescreen.py`, no model calls; verdicts in `reports/prescreen/`).
Every buy so far had a base fair value well above the price. Your own requests, entry-price hits and holdings
are never pre-screened.
For US companies, core research starts from an **SEC filing delta**: the Risk Factors and MD&A paragraphs that
were added, removed or reworded since the comparable 10-K/10-Q (`scripts/sec_delta.py`). sec.gov asks for a
contact email in automated requests, so this stays off until you add `SEC_CONTACT=you@example.com` to the
git-ignored `.env` file (not `CLAUDE.md`, which is public).
Each research note includes the stock's recent **news headlines** (analyst price targets and ratings are
filtered out by rule) and sentiment figures such as short interest.

Results are committed to the `main` branch ("Weekly run 2026-10-10", "Daily update 2026-10-12"). If anything goes wrong, **no trades
from that run are kept**: only an error log is committed and the run shows a red ✗.

See `reports/weekly/` for real reports, and `reports/sample/` for an older example from a simulated portfolio.

---

## Try it yourself (about 15 minutes, no coding)

### 1. Copy the project to your GitHub account
Click **Fork** (top right of this page) → **Create fork**.

### 2. Give your copy access to Claude (pick one)
- **Anthropic API key (pay as you go):** at <https://console.anthropic.com> → **API Keys** → **Create Key**;
  copy it (starts `sk-ant-`). Strongly recommended: **Settings → Limits** → set a monthly spend limit.
- **Claude subscription token:** if you have Claude Pro/Max and Claude Code installed, run
  `claude setup-token` in Terminal and copy the token it prints.

Then in **your fork**: **Settings** → **Secrets and variables** → **Actions** → **New repository secret**:
- Name `ANTHROPIC_API_KEY` for an API key, **or** `CLAUDE_CODE_OAUTH_TOKEN` for a subscription token.
- Paste the value → **Add secret**. It's stored encrypted by GitHub and never appears in any file.

### 3. Let the workflows save their results
**Settings** → **Actions** → **General** → **Workflow permissions** → **Read and write permissions** → **Save**.
(Don't turn on branch protection for `main`, or the workflows can't commit.)

### 4. Switch it on
1. **Actions** tab → **I understand my workflows, go ahead and enable them**.
2. Delete the pause file: open `PAUSED` → **…** menu → **Delete file** → **Commit changes**.

### 5. First runs
1. **Actions** → **Weekly screen** → **Run workflow**. Wait for the green ✓ (about 4 hours with the default list;
   a few minutes with a small custom list, see below).
2. **Actions** → **Weekly review** → **Run workflow**, tick **Dry run** → **Run workflow**. This does everything
   but changes nothing; open the run and expand **Show report**.
3. Happy? From now on it runs by itself every Friday and Saturday. (Or run **Weekly review** now without
   **Dry run**.)

---

## Choose your stocks

Edit the `[universe]` block in `CLAUDE.md` (open the file on GitHub → pencil icon → **Commit changes**):

```toml
[universe]
sp500 = true                          # S&P 500
ftse100 = true                        # universe/ftse100.txt
allworld_size = 3800                  # largest N stocks worldwide; 0 = none
custom_file = "universe/custom.txt"   # your own tickers
```

Example: to cover only your own 40 stocks, set `sp500 = false`, `ftse100 = false`, `allworld_size = 0`, and
list them in `universe/custom.txt`, one per line, written the way stockanalysis.com writes them:
`AAPL`, `LON:SHEL`, `TYO:7203`, `ETR:SAP`. The screen then takes a couple of minutes instead of hours.

Also editable: `universe/ftse100.txt` (update after each quarterly FTSE review; add `screen=no` to keep a
name out of the screen) and `universe/watchlist.txt` (names always eligible, with their investor-relations
website).

---

## Pause and resume

- **GitHub Actions — pause:** **Add file** → **Create new file** → name it `PAUSED` → **Commit changes**. All
  workflows still start on schedule but exit immediately and change nothing. **Resume:** open `PAUSED` →
  **…** → **Delete file** → **Commit changes**.
- **Your Mac:** `PAUSED` does not stop Mac runs (they use `--local`). Pause with
  `bin/install-mac-schedule --remove`; resume with `bin/install-mac-schedule`.

---

## The dashboard (charts)

Every weekly run rebuilds `docs/index.html`: portfolio value, performance vs the S&P 500, holdings and
sector weights, recent trades, decisions and hit rates.
- **On your computer:** open `docs/index.html` in any browser.
- **As a public web page (free):** on GitHub, **Settings** → **Pages** → under **Build and deployment**,
  Source **Deploy from a branch**, Branch **main**, folder **/docs** → **Save**. After a minute it's live at
  `https://<your-username>.github.io/paper-portfolio/` and updates itself after every weekly run.

## Where to look

| File | What it is |
|---|---|
| `reports/weekly/<date>.md` | Weekly report: summary, trades (and rejections with the rule broken), returns vs SPY, review notes, hit rates |
| `reports/screen/<date>.md` | The screen's rankings and the week's picks |
| `docs/index.html` | The dashboard (also the public GitHub Pages site) |
| `portfolio/state.json` | Cash, every holding (type, thesis, triggers or exit plan, conviction) and pending orders |
| `portfolio/ledger.csv` | Every trade with price, costs and source URL |
| `portfolio/rejections.csv` | Every rejected trade or order, with the rule it broke |
| `portfolio/decisions.csv` | Every decision and how it did vs SPY after 1, 3, 6 and 12 months |
| `research/<TICKER>/` | Fact sheets, research notes and evaluations |
| `runs/<date>/` | Each run's working files and log; `error.log` if it failed |
| `reports/research/<date>-batch-NN.md` | The research loop's batch reports: every decision, its fair value and any order |
| `reports/regime/<date>.md` | The cash strategy: the stress score, each indicator and the reserve |
| `reports/dip-radar/<date>.md` | The dip radar: unusual falls since our last research, and what was queued |
| `portfolio/funding_queue.csv` | Conviction-4 buys waiting for room above the cash reserve (added, started, topped up, dropped) |

A red ✗ in **Actions** means a run failed: read `runs/<date>/error.log`. Nothing from that run was traded.

## Changing the rules

All portfolio rules (starting cash, position sizes, limits, costs, screen settings) are in the config block
in `CLAUDE.md`. `CLAUDE.md` also explains the investment approach and data rules the agents follow.

## Testing the failure handling

**Actions** → **Weekly review** → **Run workflow**, type `decision log` in the **TEST ONLY** box. The run
should end with a red ✗ and one commit, "Weekly run <date> FAILED (error log only)", containing only
`runs/<date>/error.log`; `portfolio/` is unchanged.

## Costs

- **GitHub Actions:** free for public repositories. Private ones include 2,000 free minutes a month; the
  default setup uses roughly 5-6 hours a week (about 1,400 minutes a month). Running on your Mac costs nothing.
- **Claude:** API usage is pay as you go (set a spend limit); a subscription token uses your plan. Quiet
  holdings, mechanical exits and the screen use no AI.

## Running it on your own Mac

Needs Python 3.11+ and the Claude Code CLI (the agents use your own Claude Code login, so no API key).
From the project folder:
```bash
python3 -m pip install -r requirements.txt
```
```bash
bin/py -m pytest
```
```bash
bin/py scripts/universe.py build
```
```bash
bin/py scripts/screen.py --limit 200
```
```bash
bin/py scripts/weekly_run.py --local --dry-run
```
`--local` runs on your computer even though the repository contains `PAUSED` (which then only pauses
GitHub). Drop `--dry-run` for a real run. To run everything automatically (Friday 22:00 screen + review,
weekday 21:30 order fills, each committing and uploading to your GitHub repo):
```bash
bin/install-mac-schedule
```
The Mac must be on at those times: each job keeps it awake while it runs, but a closed lid on battery still
sends it to sleep (the job then pauses until it wakes), so keep it plugged in. The saved copies of
stockanalysis.com pages used by some parser tests are not included in this repository, so those tests are
skipped; everything else runs.

### The research loop
To research the whole universe rather than the weekly 20 picks, build a ranked queue from a day's page cache and
start the loop. It runs in the background (3 stocks at a time), commits a batch report every 6 stocks, sends any
BUY to the portfolio, and stops when it's done or the Claude usage limit stops it; run the same command again to
continue where it stopped.
```bash
bin/py scripts/research_loop.py rank runs/my-loop --cache-date 2026-10-16
```
```bash
bin/research-loop runs/my-loop
```

## License
MIT. See `LICENSE`.

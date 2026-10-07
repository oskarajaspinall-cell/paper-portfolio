# Paper Portfolio

Paper Portfolio is a hands-off, simulated stock portfolio that runs itself every week, on your own Mac or on GitHub Actions. A Python screen scores thousands of stocks on quality, valuation and momentum. Claude agents then research the best ideas, argue the bear case before the bull case, and must reach a firm decision with a conviction level. Simple scripts handle everything else: prices, position sizing, trading costs, stop-losses and returns, so no maths is left to the AI. Every decision is logged and scored against the S&P 500 at 1, 3, 6 and 12 months, building an honest track record. It's paper trading only, with no broker connection. Fork it, add your own Claude key, and choose your own stocks.

**📊 Live dashboard:** https://oskarajaspinall-cell.github.io/paper-portfolio/ (updated after every weekly run)

> **Paper trading only. Not investment advice.** There is no broker connection, no real orders and no
> broker credentials anywhere in this project. Prices and financials are read from
> [stockanalysis.com](https://stockanalysis.com); the scraper respects its robots.txt and makes at most
> one request every 3 seconds. If you run it, you are responsible for using that site within its terms.

This repository ships **paused** (there is a `PAUSED` file), so nothing runs until you set up your own copy.

---

## What happens each week

| Step | What it does | Uses AI? |
|---|---|---|
| **Weekly screen** | Rebuilds the stock list (default: S&P 500 + FTSE 100 + the ~3,800 largest stocks worldwide) and scores every stock on quality, valuation and momentum, with a 5-year history check on the top 500. Picks 10 core + 10 tactical ideas (tactical ideas must have results due soon and not be overextended). ~4 hours with the default list. | No |
| **Weekly review** | Fills last week's orders; checks every holding; sells tactical positions that hit their stop, target or time limit; reviews holdings that moved >8% or reported results (using recent headlines); fully re-researches any core holding whose thesis broke; researches the screen's 20 picks (3 at a time; a failed one is skipped and listed); places orders for the next open; updates the decision log, report and dashboard. | Only for flagged holdings and new research |
| **Daily update** (weekdays) | Fills pending orders at the opening price of the next trading day, re-prices every holding at its latest close, and refreshes the dashboard. | No |

| Schedule | On your Mac (`bin/install-mac-schedule`) | On GitHub Actions (UTC) |
|---|---|---|
| Screen + review | Friday 22:00, one script (`bin/weekly-local`) | Screen Friday 21:00, review Saturday 08:00 |
| Order fills + daily prices | Weekdays 22:30 (`bin/fill-pending`) | Weekdays 21:30 |

**Only high-conviction ideas are bought** (4 or 5 out of 5); the rest are recorded as AVOID, so cash can stay
high for a while. **Trades fill at the next market open**: decisions become pending orders filled at the
opening price of the next trading day; a tactical order that opens beyond its stop or target is cancelled.
After each evaluation, a **Monte Carlo simulation** (numpy, 10,000 paths, fixed seed) turns the researched
bull/base/bear scenarios into return distributions for 3, 6 and 12 months (`research/<TICKER>/<date>-montecarlo.md`);
the AI only extracts cited parameters, never results. Each research note includes the stock's recent **news headlines** (analyst price targets and ratings are
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
weekday 22:30 order fills, each committing and uploading to your GitHub repo):
```bash
bin/install-mac-schedule
```
The Mac must be on at those times (if it is asleep, the job runs when it wakes).
The saved copies of stockanalysis.com pages used by some parser tests are not included in this repository,
so those tests are skipped (about 25 of 197); everything else runs.

## License
MIT. See `LICENSE`.

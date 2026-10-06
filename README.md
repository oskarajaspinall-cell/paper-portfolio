# Paper Portfolio

An automated **paper** (pretend-money) stock portfolio run by Claude agents. Every week it screens
thousands of stocks, researches a few, makes firm buy / avoid / sell decisions, trades a simulated
$100,000 portfolio and keeps a track record of every decision against the S&P 500 (SPY).

> **Paper trading only. Not investment advice.** There is no broker connection, no real orders and no
> broker credentials anywhere in this project. Prices and financials are read from
> [stockanalysis.com](https://stockanalysis.com); the scraper respects its robots.txt and makes at most
> one request every 3 seconds. If you run it, you are responsible for using that site within its terms.

This repository ships **paused** (there is a `PAUSED` file), so nothing runs until you set up your own copy.

---

## What happens each week

| When (UTC) | Workflow | What it does | Uses AI? |
|---|---|---|---|
| Friday 21:00 | **Weekly screen** | Rebuilds the stock list (default: S&P 500 + FTSE 100 + the ~3,800 largest stocks worldwide) and scores every stock on quality, valuation and momentum. Picks 1 core + 1 tactical idea. ~3 hours with the default list. | No |
| Saturday 08:00 | **Weekly review** | Checks every holding; sells tactical positions that hit their stop, target or time limit; reviews holdings that moved >8% or reported results; fully re-researches any core holding whose thesis broke; researches the screen's picks; trades; updates the decision log; writes the weekly report. | Only for flagged holdings and new research |

Results are committed to the `main` branch ("Weekly run 2026-10-10"). If anything goes wrong, **no trades
from that run are kept**: only an error log is committed and the run shows a red ✗.

See `reports/sample/` for an example weekly report (from a simulated portfolio).

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
1. **Actions** → **Weekly screen** → **Run workflow**. Wait for the green ✓ (about 3 hours with the default list;
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

- **Pause:** **Add file** → **Create new file** → name it `PAUSED` → **Commit changes**. Both workflows still
  start on schedule but exit immediately and change nothing.
- **Resume:** open `PAUSED` → **…** → **Delete file** → **Commit changes**.

---

## Where to look

| File | What it is |
|---|---|
| `reports/weekly/<date>.md` | Weekly report: summary, trades (and rejections with the rule broken), returns vs SPY, review notes, hit rates |
| `reports/screen/<date>.md` | The screen's rankings and the week's picks |
| `portfolio/state.json` | Cash and every holding (type, thesis, triggers or exit plan, conviction) |
| `portfolio/ledger.csv` | Every trade with price, costs and source URL |
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
  default setup uses roughly 4 hours a week.
- **Claude:** API usage is pay as you go (set a spend limit); a subscription token uses your plan. Quiet
  holdings, mechanical exits and the screen use no AI.

## Running it on your own computer (optional)

Needs Python 3.11+ (and the Claude Code CLI for the agent steps). From the project folder:
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
bin/py scripts/weekly_run.py --dry-run
```
The saved copies of stockanalysis.com pages used by some parser tests are not included in this repository,
so those tests are skipped (about 20 of 160); everything else runs.

## License
MIT. See `LICENSE`.

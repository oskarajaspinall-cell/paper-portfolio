"""Brinson-Fachler return attribution vs the S&P 500 by sector. No model calls. Informational.

Design by Claude 2026-10-16. Splits the portfolio's excess return over a sector-weighted S&P 500 into:
    allocation   (w_p,s - w_b,s) x (R_b,s - R_b)   sector bets, including CASH (benchmark weight 0)
    selection    w_b,s x (R_p,s - R_b,s)           stock picking within each sector
    interaction  (w_p,s - w_b,s) x (R_p,s - R_b,s)
computed daily and linked over the period with Carino's method, so the three add up to the period's
excess return (residual ~0). The rebuilt portfolio value is checked against portfolio/valuations.csv and
any gap is shown.

Inputs: holdings rebuilt from portfolio/ledger.csv (shares at each close; buys and sells counted at the start
of their fill day), closes from the portfolio price source (Yahoo, stockanalysis.com fallback), non-USD
holdings converted at their fill-day FX rate from the ledger, cash interest from portfolio/interest.csv.
Benchmark: sector returns from the SPDR sector ETFs (prices as above); sector weights = S&P 500 members'
market caps (universe/universe.csv members, caps and sectors from stockanalysis.com's sector list pages).
R_b is the sector-weighted composite; SPY's own return is shown next to it.
Cash's benchmark return is the cash interest rate ([cash].interest_aer_pct): its allocation effect is the
cost (or benefit) of holding the regime's cash reserve instead of the index; its interaction effect is
trading costs. Non-US holdings are measured against the US sector ETF of their sector.

Usage:
    python scripts/attribution.py report [--asof YYYY-MM-DD]   -> reports/attribution/<date>.md/.json
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, load_config  # noqa: E402

OUT = ROOT / "reports" / "attribution"
PORT = ROOT / "portfolio"
SECTOR_ETF = {"Technology": "XLK", "Healthcare": "XLV", "Financials": "XLF", "Consumer Discretionary": "XLY",
              "Consumer Staples": "XLP", "Energy": "XLE", "Industrials": "XLI", "Materials": "XLB",
              "Utilities": "XLU", "Real Estate": "XLRE", "Communication Services": "XLC"}
SIGN = {"BUY": 1, "ADD": 1, "SELL": -1, "TRIM": -1}
CASH = "Cash"


def _read(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as f:
        return list(csv.DictReader(f))


def _eff(r: dict) -> str:
    return r.get("fill_close_date") or r["date"]


def benchmark_weights(fetcher, universe: list[dict]) -> tuple[dict[str, float], list[str]]:
    """S&P 500 sector weights from the members' market caps on stockanalysis.com's sector list pages."""
    from fetch_data import page_nodes
    members = {r["ticker"].upper() for r in universe if "SP500" in (r.get("indexes") or "").split(";")}
    caps, urls = {}, []
    for sector in SECTOR_ETF:
        url = f"https://stockanalysis.com/stocks/sector/{sector.lower().replace(' ', '-')}/"
        rows = page_nodes(fetcher.html(url), url)[-1].get("data")
        if not isinstance(rows, list):
            raise DataError(url, "data", "sector list missing")
        caps[sector] = sum(float(r.get("marketCap") or 0) for r in rows if str(r.get("s", "")).upper() in members)
        urls.append(url)
    tot = sum(caps.values())
    if not tot:
        raise DataError(urls[0], "marketCap", "no S&P 500 members found on the sector pages")
    return {s: c / tot for s, c in caps.items()}, urls


def _close_on(rows: list[dict], day: str) -> float | None:
    """The last close on/before `day` (a holiday on the stock's exchange carries the previous close)."""
    c = None
    for r in rows:
        if r["date"] > day:
            break
        c = r["close"]
    return c


def _interest_through(rows: list[dict], day: str) -> float:
    """Cumulative cash interest credited through `day`, spreading each row evenly over its days."""
    tot = 0.0
    for r in rows:
        a, b, n = dt.date.fromisoformat(r["from"]), dt.date.fromisoformat(r["through"]), int(r["days"])
        d = dt.date.fromisoformat(day)
        if d >= b:
            tot += float(r["interest_usd"])
        elif d >= a:
            tot += float(r["interest_usd"]) * ((d - a).days + 1) / n
    return tot


def daily_effects(days: list[str], ledger: list[dict], hist: dict[str, list[dict]], sectors: dict[str, str],
                  fx: dict[str, float], start_cash: float, interest: list[dict], bench_w: dict[str, float],
                  aer_pct: float) -> list[dict]:
    """One row per day (from the 2nd day): portfolio/benchmark returns and the sector effects."""
    tickers = sorted({r["ticker"] for r in ledger if r["side"] in SIGN})
    ledger = [r for r in ledger if r["side"] in SIGN or r["side"] == "SPLIT"]

    def shares_at(t, day):
        return sum(SIGN.get(r["side"], 0) * float(r["shares"]) + (float(r["shares"]) if r["side"] == "SPLIT" else 0)
                   for r in ledger if r["ticker"] == t and _eff(r) <= day)

    def cash_at(day):
        return start_cash + sum(float(r["cash_change_usd"] or 0) for r in ledger if _eff(r) <= day) \
            + _interest_through(interest, day)

    def mv(t, day):
        c = _close_on(hist[t], day)
        return shares_at(t, day) * c * fx.get(t, 1.0) if c else 0.0

    out = []
    for d0, d1 in zip(days, days[1:]):
        h0 = {t: mv(t, d0) for t in tickers}
        h1 = {t: mv(t, d1) for t in tickers}
        T0, T1 = cash_at(d0) + sum(h0.values()), cash_at(d1) + sum(h1.values())
        flows = {t: 0.0 for t in tickers}
        for r in ledger:
            if d0 < _eff(r) <= d1 and r["side"] in SIGN:
                flows[r["ticker"]] += SIGN[r["side"]] * float(r["gross_usd"])
        B, E = {}, {}
        for t in tickers:
            s = sectors.get(t) or "Other"
            B[s] = B.get(s, 0.0) + h0[t] + flows[t]
            E[s] = E.get(s, 0.0) + h1[t]
        B[CASH], E[CASH] = T0 - sum(B.values()), T1 - sum(E.values())
        rp = T1 / T0 - 1
        rbs = {s: _close_on(hist[e], d1) / _close_on(hist[e], d0) - 1 for s, e in SECTOR_ETF.items()}
        rb = sum(bench_w[s] * rbs[s] for s in bench_w)
        n_days = (dt.date.fromisoformat(d1) - dt.date.fromisoformat(d0)).days
        rbs[CASH] = (1 + aer_pct / 100) ** (n_days / 365) - 1
        rbs["Other"] = rb
        eff = {}
        for s in set(B) | set(bench_w):
            wp = B.get(s, 0.0) / T0
            wb = bench_w.get(s, 0.0)
            rps = E[s] / B[s] - 1 if B.get(s) else rbs[s]
            eff[s] = {"wp": wp, "wb": wb, "rp": rps, "rb": rbs[s],
                      "allocation": (wp - wb) * (rbs[s] - rb), "selection": wb * (rps - rbs[s]),
                      "interaction": (wp - wb) * (rps - rbs[s])}
        spy = hist.get("SPY")
        out.append({"date": d1, "rp": rp, "rb": rb, "spy": (_close_on(spy, d1) / _close_on(spy, d0) - 1) if spy else None,
                    "sectors": eff})
    return out


def carino(days: list[dict]) -> dict:
    """Link daily effects (Carino): scale each day's effects by k_t / K so they sum to R - B over the period."""
    def k(r, b):
        return (math.log1p(r) - math.log1p(b)) / (r - b) if abs(r - b) > 1e-12 else 1 / (1 + r)
    R = math.prod(1 + d["rp"] for d in days) - 1
    Bm = math.prod(1 + d["rb"] for d in days) - 1
    K = k(R, Bm)
    tot: dict[str, dict[str, float]] = {}
    for d in days:
        f = k(d["rp"], d["rb"]) / K
        for s, e in d["sectors"].items():
            t = tot.setdefault(s, {"allocation": 0.0, "selection": 0.0, "interaction": 0.0, "wp_avg": 0.0, "wb": e["wb"]})
            for x in ("allocation", "selection", "interaction"):
                t[x] += f * e[x]
            t["wp_avg"] += e["wp"] / len(days)
    sums = {x: sum(t[x] for t in tot.values()) for x in ("allocation", "selection", "interaction")}
    spy = [d["spy"] for d in days if d["spy"] is not None]
    return {"portfolio": R, "benchmark": Bm, "excess": R - Bm, "spy": math.prod(1 + x for x in spy) - 1 if spy else None,
            "sectors": tot, **sums, "residual": R - Bm - sum(sums.values())}


def _total_on(vals: list[dict], day: str) -> float:
    return float([v for v in vals if v["date"] <= day][-1]["total_usd"])


def report(mkt, fetcher, cfg: dict, asof: str, port: Path = PORT) -> dict:
    from universe import read_universe
    ledger = _read(port / "ledger.csv")
    vals = _read(port / "valuations.csv")
    if not ledger or not vals:
        return {"asof": asof, "note": "no trades yet"}
    hist, sectors, fx = {}, {}, {}
    for r in ledger:
        t = r["ticker"]
        if r["side"] in SIGN and t not in hist:
            hist[t] = mkt.history(t)["rows"]
            sectors[t] = mkt.sector(t)
            if r.get("fx_usd_per_unit"):
                fx[t] = float(r["fx_usd_per_unit"])
    for e in list(SECTOR_ETF.values()) + [cfg["portfolio"]["benchmark"]]:
        hist[e if e != cfg["portfolio"]["benchmark"] else "SPY"] = mkt.history(e)["rows"]
    start = vals[0]["date"]
    days = [r["date"] for r in hist["SPY"] if start <= r["date"] < asof]
    bench_w, urls = benchmark_weights(fetcher, read_universe())
    daily = daily_effects(days, ledger, hist, sectors, fx, float(cfg["portfolio"]["starting_cash_usd"]),
                          _read(port / "interest.csv"), bench_w, float(cfg["cash"]["interest_aer_pct"]))
    if not daily:
        return {"asof": asof, "note": "fewer than two trading days"}
    res = carino(daily)
    last = next((v for v in reversed(vals) if v["date"] <= days[-1]), None)
    if last and daily:
        rebuilt = _total_on(vals, days[0]) * math.prod(1 + d["rp"] for d in daily)
        res["rebuild_gap_usd"] = rebuilt - float(last["total_usd"])
    res.update(asof=asof, start=days[0], end=days[-1], days=len(daily), weight_sources=urls,
               etfs=SECTOR_ETF)
    return res


def report_md(res: dict) -> str:
    def p(x, d=2):
        return "n/a" if x is None else f"{x * 100:+.{d}f}%"
    head = [f"# Return attribution — {res['asof']}", "",
            "Informational (design by Claude 2026-10-16); not meaningful until about 6 months of history. "
            "Brinson-Fachler by sector against a sector-weighted S&P 500 (SPDR sector ETFs; S&P 500 members' market "
            "caps from stockanalysis.com sector pages), linked daily (Carino). Cash is its own sector (benchmark "
            "weight 0, benchmark return = the cash interest rate). Non-US holdings are measured against US sector ETFs.", ""]
    if res.get("note"):
        return "\n".join(head + [res["note"] + "."]) + "\n"
    lines = head + [
        f"Period {res['start']} to {res['end']} ({res['days']} trading days): portfolio {p(res['portfolio'])}, "
        f"sector benchmark {p(res['benchmark'])} (SPY {p(res['spy'])}), excess {p(res['excess'])} = "
        f"allocation {p(res['allocation'])} + selection {p(res['selection'])} + interaction {p(res['interaction'])}"
        f" (residual {p(res['residual'], 3)})."
        + (f" Rebuilt value vs the official valuation: {res['rebuild_gap_usd']:+,.0f} USD." if "rebuild_gap_usd" in res else ""),
        "",
        "| Sector | Avg weight | Index weight | Allocation | Selection | Interaction | Total |",
        "|---|---|---|---|---|---|---|"]
    for s, e in sorted(res["sectors"].items(), key=lambda kv: -abs(kv[1]["allocation"] + kv[1]["selection"] + kv[1]["interaction"])):
        tot = e["allocation"] + e["selection"] + e["interaction"]
        if abs(tot) < 5e-6 and e["wp_avg"] == 0:
            continue
        lines.append(f"| {s} | {e['wp_avg'] * 100:.1f}% | {e['wb'] * 100:.1f}% | {p(e['allocation'])} | "
                     f"{p(e['selection'])} | {p(e['interaction'])} | {p(tot)} |")
    lines += ["", "Sector weights: " + ", ".join(res["weight_sources"][:2]) + " (and the other sector pages)."]
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["report"])
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    a = ap.parse_args(argv)
    from fetch_data import Fetcher
    from portfolio import Market, price_provider
    cfg = load_config()
    f = Fetcher(cfg)
    res = report(Market(f, a.asof, cfg, price_provider(cfg)), f, cfg, a.asof)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{a.asof}.json").write_text(json.dumps(res, indent=1))
    (OUT / f"{a.asof}.md").write_text(report_md(res))
    print(f"OK reports/attribution/{a.asof}.md excess={res.get('excess')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Macro snapshot from FRED (official Federal Reserve data). Macro variables ONLY: company numbers stay
stockanalysis.com-only. No model calls.

    python scripts/macro_data.py [--asof YYYY-MM-DD]   -> reports/macro/<date>.json and .md

Each series in [macro].fred_series: latest observation before `asof` (value + date), and its change vs
~1 month and ~3 months earlier. Downloads https://fred.stlouisfed.org/graph/fredgraph.csv?id=<ID>
(allowed by FRED's robots.txt), robots-checked, 1 request / 3 s, cached per day; a failed series is
reported as [data unavailable], never guessed.

Also used by the weekly scan to test macro refresh triggers: `fired(series_rows, op, value, since, asof)`.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import time
import urllib.robotparser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, DataError, load_config  # noqa: E402

FRED = "https://fred.stlouisfed.org"
CACHE = ROOT / "data" / "cache"


class FredFetcher:
    def __init__(self, cfg: dict, today: str | None = None, cache: Path = CACHE):
        self.ua = cfg["data"]["user_agent"]
        self.interval = float(cfg["data"]["request_interval_seconds"])
        self.dir = cache / (today or dt.date.today().isoformat())
        self.stamp = cache / ".last_request_fred"
        self._robots = None

    def _get(self, url: str) -> str:
        import fcntl

        import requests
        self.stamp.parent.mkdir(parents=True, exist_ok=True)
        with open(self.stamp.with_suffix(".lock"), "w") as lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
            try:
                last = float(self.stamp.read_text())
            except (OSError, ValueError):
                last = 0.0
            if last + self.interval > time.time():
                time.sleep(last + self.interval - time.time())
            try:
                r = requests.get(url, headers={"User-Agent": self.ua}, timeout=30)
            except requests.RequestException as e:
                raise DataError(url, "network", type(e).__name__) from e
            finally:
                self.stamp.write_text(str(time.time()))
        if r.status_code != 200:
            raise DataError(url, "http", f"status {r.status_code}")
        return r.text

    def allowed(self, url: str) -> bool:
        if self._robots is None:
            cached = self.dir / "fred_robots.txt"
            text = cached.read_text() if cached.exists() else self._get(FRED + "/robots.txt")
            cached.parent.mkdir(parents=True, exist_ok=True)
            cached.write_text(text)
            self._robots = urllib.robotparser.RobotFileParser()
            self._robots.parse(text.splitlines())
        return self._robots.can_fetch(self.ua, url)

    def series(self, sid: str) -> dict:
        url = f"{FRED}/graph/fredgraph.csv?id={sid}"
        cached = self.dir / f"fred__{sid}.csv"
        if cached.exists():
            text = cached.read_text()
        else:
            if not self.allowed(url):
                raise DataError(url, "robots.txt", "path disallowed by FRED robots.txt")
            text = self._get(url)
            cached.parent.mkdir(parents=True, exist_ok=True)
            cached.write_text(text)
        return {"id": sid, "source_url": url, "rows": parse_csv(text, url)}


def parse_csv(text: str, url: str) -> list[dict]:
    lines = [l for l in text.strip().splitlines() if l.strip()]
    if not lines or "," not in lines[0]:
        raise DataError(url, "csv", "not a FRED CSV")
    rows = []
    for l in lines[1:]:
        d, _, v = l.partition(",")
        try:
            rows.append({"date": d.strip(), "value": float(v)})
        except ValueError:
            continue  # FRED marks missing observations with "."
    if not rows:
        raise DataError(url, "values", "no observations")
    return rows


def value_on_or_before(rows: list[dict], day: str) -> dict | None:
    prior = [r for r in rows if r["date"] <= day]
    return prior[-1] if prior else None


def summarise(sid: str, label: str, rows: list[dict], url: str, asof: str) -> dict:
    last = value_on_or_before(rows, (dt.date.fromisoformat(asof) - dt.timedelta(days=1)).isoformat())
    if last is None:
        return {"id": sid, "label": label, "value": "[data unavailable]", "source_url": url}
    out = {"id": sid, "label": label, "value": last["value"], "date": last["date"], "source_url": url}
    for name, days in (("chg_1m", 30), ("chg_3m", 91)):
        ref = value_on_or_before(rows, (dt.date.fromisoformat(last["date"]) - dt.timedelta(days=days)).isoformat())
        out[name] = None if ref is None else round(last["value"] - ref["value"], 4)
        out[f"{name}_from"] = None if ref is None else ref["date"]
    return out


def fired(rows: list[dict], op: str, value: float, since: str | None, asof: str) -> dict | None:
    """First observation in (since, asof) meeting `op value`; None if none did."""
    for r in rows:
        if (since is None or r["date"] > since) and r["date"] < asof:
            if (r["value"] > value) if op == ">" else (r["value"] < value):
                return r
    return None


def snapshot(fetcher, cfg: dict, asof: str) -> dict:
    out = {"asof": asof, "source": "FRED (Federal Reserve Bank of St. Louis), official data", "series": []}
    for s in cfg["macro"]["fred_series"]:
        try:
            got = fetcher.series(s["id"])
            out["series"].append(summarise(s["id"], s["label"], got["rows"], got["source_url"], asof))
        except DataError as e:
            out["series"].append({"id": s["id"], "label": s["label"], "value": "[data unavailable]", "error": str(e)})
    return out


def render_md(snap: dict) -> str:
    L = [f"# Macro snapshot — {snap['asof']}", f"Source: {snap['source']}. Facts only (latest observation and its "
         "change); market pricing and inference belong to the macro-overlay step.", "",
         "| Series | Latest | Date | Δ ~1m | Δ ~3m | Source |", "|---|---|---|---|---|---|"]
    for s in snap["series"]:
        if s["value"] == "[data unavailable]":
            L.append(f"| {s['label']} ({s['id']}) | [data unavailable] | | | | |")
            continue
        f = lambda x: "n/a" if x is None else f"{x:+.3g}"  # noqa: E731
        L.append(f"| {s['label']} ({s['id']}) | {s['value']:g} | {s['date']} | {f(s['chg_1m'])} | {f(s['chg_3m'])} | {s['source_url']} |")
    return "\n".join(L) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    a = ap.parse_args(argv)
    cfg = load_config()
    snap = snapshot(FredFetcher(cfg), cfg, a.asof)
    out = ROOT / "reports" / "macro"
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{a.asof}.json").write_text(json.dumps(snap, indent=1))
    (out / f"{a.asof}.md").write_text(render_md(snap))
    missing = [s["id"] for s in snap["series"] if s["value"] == "[data unavailable]"]
    print(json.dumps({"out": f"reports/macro/{a.asof}.md", "series": len(snap["series"]), "unavailable": missing}))
    return 0


if __name__ == "__main__":
    sys.exit(main())

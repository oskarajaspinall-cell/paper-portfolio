"""Build docs/index.html: a self-contained portfolio dashboard (no external libraries, no model calls).

Reads portfolio/state.json, valuations.csv, ledger.csv, decisions.csv, universe/universe.csv (names,
optional) and the latest reports/screen/, reports/risk/ and reports/attribution/ <date>.json. Open the file in any browser, or publish it with
GitHub Pages (Settings -> Pages -> Deploy from branch: main, /docs).

    python scripts/dashboard.py [--out docs/index.html]
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, Ticker, load_config  # noqa: E402
import entry_watch  # noqa: E402
import portfolio  # noqa: E402

OUT = ROOT / "docs" / "index.html"


def _csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as fh:
        return list(csv.DictReader(fh))


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def repo_url() -> str | None:
    try:
        u = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except OSError:
        return None
    if u.startswith("git@github.com:"):
        u = "https://github.com/" + u.split(":", 1)[1]
    return u[:-4] if u.endswith(".git") else (u or None)


def series(vals: list[dict], start_cash: float) -> list[dict]:
    """One point per valuation date (the last row of each date), indexed to 100 at inception."""
    by_date: dict[str, dict] = {}
    for v in vals:
        by_date[v["date"]] = v
    pts = [by_date[d] for d in sorted(by_date)]
    if not pts:
        return []
    spy0 = _f(pts[0]["spy_close"])
    inv = {p["date"]: p for p in portfolio.invested_series(vals)}
    out = []
    for v in pts:
        tot, spy, base, i = _f(v["total_usd"]), _f(v["spy_close"]), _f(v.get("baseline_usd")), inv.get(v["date"])
        out.append({"date": v["date"], "value": tot,
                    "portfolio": None if tot is None else tot / start_cash * 100,
                    "spy": None if not (spy and spy0) else spy / spy0 * 100,
                    "baseline": None if base is None else base / start_cash * 100,
                    "invested": None if not i else 100 + i["pct"] * 100,
                    "spy_same": None if not i or i["spy_pct"] is None else 100 + i["spy_pct"] * 100})
    return out


def week_change(ser: list[dict]) -> dict | None:
    """Latest point vs the latest one at least 7 days earlier (daily points exist), else the first."""
    if len(ser) < 2 or not ser[-1]["portfolio"]:
        return None
    last = ser[-1]
    cut = (dt.date.fromisoformat(last["date"]) - dt.timedelta(days=7)).isoformat()
    prev = ([p for p in ser[:-1] if p["date"] <= cut] or ser[:1])[-1]
    if not prev["portfolio"]:
        return None
    return {"from": prev["date"], "portfolio": last["portfolio"] / prev["portfolio"] - 1,
            "spy": (last["spy"] / prev["spy"] - 1) if last["spy"] and prev["spy"] else None}


def live_snapshot(tickers: list[str], fetch=None) -> dict:
    """Live prices at build time (owner request 2026-10-09: show how current every price is). Yahoo 1-minute
    bars via prices.live_price; a stock with no price is left out. Display only: the portfolio's official
    value stays on closing prices."""
    from concurrent.futures import ThreadPoolExecutor
    from zoneinfo import ZoneInfo
    if fetch is None:
        from prices import live_price as fetch

    def one(t):
        try:
            q = fetch(t)
        except Exception:  # noqa: BLE001
            return t, None
        uk = dt.datetime.fromisoformat(q["time"]).astimezone(ZoneInfo("Europe/London"))
        return t, {"price": round(q["price"], 4), "date": q["date"], "uk": uk.strftime("%a %H:%M") + " UK"}
    with ThreadPoolExecutor(8) as pool:
        return {t: q for t, q in pool.map(one, dict.fromkeys(tickers)) if q}


def expected_fill(order: dict, cfg: dict) -> str:
    """When a pending order should fill: the first weekday on/after its first eligible open, at that exchange's
    opening time (exchange holidays aren't known here, so it can be a session later)."""
    t = order["request"]["ticker"]
    d = dt.date.fromisoformat(portfolio.first_eligible_open(order, t, cfg))
    while d.weekday() >= 5:
        d += dt.timedelta(days=1)
    ex = portfolio.Ticker(t).exchange or "US"
    spec = cfg.get("fills", {}).get("open_times", {}).get(ex)
    return f"{d:%a %d %b} open" + (f" ({spec.split()[1]} {ex} time)" if spec else "")


def est_usd(est: dict, ledger: list[dict]) -> float | None:
    """An order's estimated USD value: recorded by portfolio.py, else shares x price x the latest ledger FX rate."""
    if est.get("usd") is not None:
        return float(est["usd"])
    if not est.get("shares") or est.get("price") is None:
        return None
    if est.get("currency") == "USD":
        return est["shares"] * est["price"]
    fx = next((_f(r.get("fx_usd_per_unit")) for r in reversed(ledger)
               if r.get("currency") == est.get("currency") and _f(r.get("fx_usd_per_unit"))), None)
    return est["shares"] * est["price"] * fx if fx else None


def build_data(live: bool = True) -> dict:
    cfg = load_config()
    port = ROOT / "portfolio"
    near_pct = float(cfg["entry"].get("near_pct", 10))
    state = json.loads((port / "state.json").read_text()) if (port / "state.json").exists() else {"holdings": {}, "cash_usd": 0}
    start = float(cfg["portfolio"]["starting_cash_usd"])
    names = {r["ticker"]: r["name"] for r in _csv(ROOT / "universe" / "universe.csv")}
    hold = []
    recv = sum(r["net_usd"] for r in state.get("receivables", []))  # dividends past the ex-date, not yet paid
    total = state.get("cash_usd", 0.0) + recv + sum(h.get("market_value_usd", 0.0) for h in state["holdings"].values())
    for t, h in sorted(state["holdings"].items(), key=lambda kv: -kv[1].get("market_value_usd", 0)):
        mv, cb = h.get("market_value_usd", 0.0), h.get("cost_basis_usd", 0.0)
        ep, lp = _f(h.get("entry_price")), _f(h.get("last_close"))
        plan = ""
        if h["type"] == "TACTICAL" and h.get("exit_plan"):
            ep_ = h["exit_plan"]
            plan = f"target {ep_['target']} · stop {ep_['stop']} · until {ep_['time_limit']}"
        elif h.get("triggers"):
            plan = f"{len(h['triggers'])} thesis triggers"
        hold.append({"ticker": t, "name": names.get(t, ""), "type": h["type"], "conviction": h.get("conviction"),
                     "sector": h.get("sector") or "", "entry_date": h.get("entry_date", ""), "currency": h.get("currency", ""),
                     "entry_price": ep, "last_price": lp, "last_date": h.get("last_close_date", ""),
                     "change_pct": (lp / ep - 1) * 100 if ep and lp else None,
                     "value": mv, "weight": mv / total * 100 if total else 0, "pl": mv - cb if cb else None,
                     "plan": plan, "thesis": h.get("thesis", "")})
    watch_rows = sorted(_csv(port / "entry_watch.csv"), key=lambda r: -(_f(r.get("pct_to_entry")) or -999))[:40]
    snap = live_snapshot([h["ticker"] for h in hold] + [r["ticker"] for r in watch_rows]) if live else {}
    live_total = state.get("cash_usd", 0.0) + recv
    for h in hold:
        q, lc = snap.get(h["ticker"]), h["last_price"]
        h["live"] = q
        if q and lc:
            h["live_change_pct"] = (q["price"] / h["entry_price"] - 1) * 100 if h["entry_price"] else None
            h["live_value"] = h["value"] * q["price"] / lc
        live_total += h.get("live_value", h["value"])
    sectors: dict[str, float] = {}
    for h in hold:
        sectors[h["sector"] or "Unknown"] = sectors.get(h["sector"] or "Unknown", 0) + h["weight"]
    vals = _csv(port / "valuations.csv")
    ser = series(vals, start)
    all_ledger = _csv(port / "ledger.csv")
    ledger = all_ledger[-25:][::-1]
    decisions = _csv(port / "decisions.csv")
    screens = sorted((ROOT / "reports" / "screen").glob("20??-??-??.json"))
    screen = json.loads(screens[-1].read_text()) if screens else {}

    def latest(kind):
        files = sorted((ROOT / "reports" / kind).glob("20??-??-??.json"))
        return json.loads(files[-1].read_text()) if files else None
    risk, attr = latest("risk"), latest("attribution")
    dip = latest("dip-radar")
    fq = []
    for e in state.get("funding_queue") or []:  # 2026-10-19: conviction-4 ideas waiting for room
        c = e.get("last_close") or e.get("decision_price")
        fv = e.get("fair_value_base")
        h = state["holdings"].get(e["ticker"]) or {}
        fq.append({"ticker": e["ticker"], "name": names.get(e["ticker"], ""), "stage": e.get("stage", "full"),
                   "conviction": e["request"].get("conviction"), "added": e["added"], "expires": e["expires"],
                   "decision_price": e["decision_price"], "close": c, "ccy": e.get("currency", ""),
                   "upside": (fv / c - 1) * 100 if fv and c else None,
                   "weight": h.get("market_value_usd", 0) / total * 100 if h and total else None,
                   "target": h.get("target_pct"), "ordered": e["ticker"] in {o["request"]["ticker"] for o in state.get("pending", [])},
                   "evaluation": next((str(p_.relative_to(ROOT)) for p_ in sorted((ROOT / "research" / Ticker(e["ticker"]).slug).glob("20??-??-??-evaluation.md"))[-1:]), "")})
    fq.sort(key=lambda x: (x["stage"] != "topup", -(x["upside"] or -999)))
    from decision_log import HORIZONS
    hits = {}
    for h in HORIZONS:
        done = [d for d in decisions if d.get(f"hit_{h}m") not in ("", None)]
        hits[f"{h}m"] = {"n": len(done), "hits": sum(int(d[f"hit_{h}m"]) for d in done)}
    last = ser[-1] if ser else None
    week = week_change(ser)
    return {
        "generated": dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "repo": repo_url(),
        "total": total, "cash": state.get("cash_usd", 0.0), "start": start, "receivable": recv,
        "close_date": max((h["last_date"] for h in hold), default=""),
        "live_total": live_total if snap else None, "live_at": dt.datetime.now().strftime("%a %H:%M") + " UK" if snap else None,
        "inception": state.get("inception_date"),
        "since": None if not last or last["portfolio"] is None else last["portfolio"] / 100 - 1,
        "since_spy": None if not last or last["spy"] is None else last["spy"] / 100 - 1,
        "invested": portfolio.invested_return(vals),
        "week": week, "series": ser, "holdings": hold, "interest": state.get("cash_interest"),
        "regime": __import__("regime").latest(dt.date.today().isoformat()),
        "sectors": sorted(([k, v] for k, v in sectors.items()), key=lambda kv: -kv[1]),
        "ledger": [{k: r.get(k, "") for k in ("date", "ticker", "type", "side", "shares", "fill_price", "currency",
                                              "fill_close_date", "gross_usd", "costs_usd", "reason")} for r in ledger],
        "decisions": [{k: d.get(k, "") for k in ("date", "ticker", "type", "decision", "conviction", "price", "currency",
                                                 "excess_1m", "excess_3m", "evaluation", "price_date")}
                      | {"live": "price: live" in (d.get("note") or "")} for d in decisions[::-1][:60]],
        "hits": hits, "n_decisions": len(decisions),
        "watch": sorted(({"ticker": r["ticker"], "close": r.get("last_close"), "entry": r["entry_price"],
                          "close_date": r.get("last_close_date", ""), "live": snap.get(r["ticker"]),
                          "ccy": r.get("currency", ""), "to_entry": _f(r.get("pct_to_entry")), "source": r["source"],
                          "conviction": r.get("conviction"), "hit": r.get("hit_date", ""),
                          "near_since": r.get("near_since", ""), "evaluation": r.get("evaluation", ""),
                          "why": entry_watch.why_not_yet(r) if entry_watch.is_near(r, near_pct) else ""}
                         for r in watch_rows),
                        key=lambda r: -(r["to_entry"] if r["to_entry"] is not None else -999))[:40],
        "near_pct": near_pct,
        "pending": [{"id": o["id"], "placed": o["placed"], "action": o["request"]["action"],
                     "ticker": o["request"]["ticker"], "type": o["request"]["position_type"],
                     "conviction": o["request"].get("conviction"), "est": o.get("estimate", {}),
                     "fills": expected_fill(o, cfg), "replaces": o["request"].get("replaces"),
                     "est_usd": est_usd(o.get("estimate", {}), all_ledger)}
                    for o in state.get("pending", [])],
        "screen": {"asof": screen.get("asof"), "screened": screen.get("screened"), "picks": screen.get("picks", []),
                   "illiquid": len(screen.get("illiquid") or [])},
        "risk": risk and {"asof": risk["asof"], "sigma_p": risk.get("sigma_p_pct"),
                          "rows": sorted(({k: r.get(k) for k in ("ticker", "weight_pct", "target_pct", "vol_pct",
                                                                  "mcr_pct", "risk_share_pct", "flag")}
                                          for r in risk["rows"]), key=lambda r: -(r["risk_share_pct"] or 0))},
        "attribution": attr if attr and not attr.get("note") else None,
        "funding_queue": fq,
        "dip": dip and {"asof": dip["asof"], "watched": len(dip["assessed"]), "hits": [h["ticker"] for h in dip["hits"]],
                        "no_data": len(dip.get("failed") or []),
                        "rows": sorted(({k: a.get(k) for k in ("ticker", "kind", "z", "ret_pct", "spy_pct", "specific_pct",
                                                                 "sessions", "last_research", "vs_base_pct", "signal", "why_not",
                                                                 "close", "close_date", "currency")}
                                        for a in dip["assessed"] if a.get("signal") or (a.get("z") is not None and a["z"] <= -1.0)),
                                       key=lambda a: (not a["signal"], a["z"] if a["z"] is not None else 0))[:15]},
    }


PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Paper Portfolio</title>
<style>
:root{color-scheme:light;--page:#f9f9f7;--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--grid:#e1e0d9;
--axis:#c3c2b7;--ring:rgba(11,11,11,.10);--s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a;--up:#006300;--down:#d03b3b;--wash:rgba(42,120,214,.10)}
@media (prefers-color-scheme:dark){:root:where(:not([data-theme="light"])){color-scheme:dark;--page:#0d0d0d;--surface:#1a1a19;--ink:#fff;
--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#383835;--ring:rgba(255,255,255,.10);--s1:#3987e5;--s2:#d95926;--s3:#199e70;--up:#0ca30c;--down:#e66767;--wash:rgba(57,135,229,.12)}}
:root[data-theme="dark"]{color-scheme:dark;--page:#0d0d0d;--surface:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#383835;
--ring:rgba(255,255,255,.10);--s1:#3987e5;--s2:#d95926;--s3:#199e70;--up:#0ca30c;--down:#e66767;--wash:rgba(57,135,229,.12)}
*{box-sizing:border-box}body{margin:0;background:var(--page);color:var(--ink);font:15px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:1120px;margin:0 auto;padding:24px 16px 48px}header{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}
h1{font-size:20px;margin:0}h2{font-size:16px;margin:0 0 4px}.sub{color:var(--ink2);font-size:13px}.muted{color:var(--muted)}
.card{background:var(--surface);border:1px solid var(--ring);border-radius:12px;padding:16px;margin-top:16px}
.hero{font-size:48px;font-weight:600;line-height:1.1;margin:8px 0 2px}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-top:12px}
.tile .l{color:var(--ink2);font-size:13px}.tile .v{font-size:22px;font-weight:600}.tile .d{font-size:13px}
.up{color:var(--up)}.down{color:var(--down)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}@media (max-width:760px){.grid2{grid-template-columns:1fr}}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:13px;color:var(--ink2);margin:6px 0}
.key{display:inline-block;width:14px;height:2px;vertical-align:middle;margin-right:6px;border-radius:1px}
.sw{display:inline-block;width:10px;height:10px;border-radius:2px;vertical-align:-1px;margin-right:6px}
svg{display:block;width:100%;height:auto;overflow:visible}svg text{fill:var(--muted);font-size:12px;font-family:inherit}
.tw{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:13px}th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--grid);white-space:nowrap}
th{color:var(--ink2);font-weight:600}td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}td.w{white-space:normal;min-width:220px;color:var(--ink2)}
.tip{position:fixed;pointer-events:none;background:var(--surface);border:1px solid var(--ring);border-radius:8px;padding:8px 10px;font-size:13px;
box-shadow:0 4px 16px rgba(0,0,0,.12);display:none;z-index:10}.tip b{font-weight:600}.tip .r{display:flex;align-items:center;gap:6px}
.empty{color:var(--ink2);padding:24px 0;text-align:center}details summary{cursor:pointer;color:var(--ink2);font-size:13px;margin-top:8px}
a{color:var(--s1)}.pill{display:inline-block;padding:1px 8px;border-radius:999px;border:1px solid var(--ring);font-size:12px;color:var(--ink2)}
.tabs{display:flex;gap:4px;margin:8px 0;border-bottom:1px solid var(--grid)}
.tab{background:none;border:0;border-bottom:2px solid transparent;color:var(--ink2);padding:6px 10px;margin-bottom:-1px;cursor:pointer;font:inherit;font-size:14px}
.tab[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--s1);font-weight:600}
.toggle{background:none;border:1px solid var(--ring);border-radius:8px;color:var(--ink2);padding:4px 10px;cursor:pointer;font:inherit;font-size:13px}
</style></head><body><main>
<header><div><h1>Paper Portfolio</h1><div class="sub">Simulated $<span id="start"></span> portfolio · paper trading only, not investment advice · updated <span id="gen"></span></div></div>
<button class="toggle" id="theme" type="button">Toggle dark mode</button></header>
<section class="card" aria-label="Summary"><div class="sub">Portfolio value</div><div class="hero" id="hero"></div><div class="sub" id="heroSub"></div>
<div class="tiles" id="tiles"></div></section>
<section class="card"><h2>Return vs the S&amp;P 500</h2>
<div class="tabs" role="tablist"><button type="button" role="tab" class="tab" data-tab="invested">Invested money</button><button type="button" role="tab" class="tab" data-tab="whole">Whole portfolio</button></div>
<div class="sub" id="lineSub"></div>
<div class="legend" id="lineLegend"></div><div id="line"></div>
<details><summary>Show as a table</summary><div class="tw"><table id="lineTable"></table></div></details></section>
<div class="grid2"><section class="card"><h2>Holdings by weight</h2><div class="legend"><span><span class="sw" style="background:var(--s1)"></span>Core</span>
<span><span class="sw" style="background:var(--s2)"></span>Tactical</span></div><div id="bars"></div></section>
<section class="card"><h2>Sectors</h2><div class="sub">% of the portfolio (cash excluded)</div><div id="sectors"></div></section></div>
<div class="grid2"><section class="card"><h2>Risk</h2><div class="sub" id="riskSub"></div>
<div class="legend"><span><span class="sw" style="background:var(--s1)"></span>Share of portfolio risk</span><span><span class="sw" style="background:var(--axis)"></span>Share of invested money</span></div>
<div id="risk"></div><details><summary>Show as a table</summary><div class="tw"><table id="riskTable"></table></div></details></section>
<section class="card"><h2>Where the excess return came from</h2><div class="sub" id="attrSub"></div><div class="tiles" id="attrTiles"></div>
<div class="tw" style="margin-top:12px"><table id="attrTable"></table></div></section></div>
<section class="card"><h2>Holdings</h2><div class="tw"><table id="holdings"></table></div></section>
<section class="card"><h2>Pending orders</h2><div class="sub">Decided trades fill at the next opening price of their own market; every rule is checked again at that price. The 21:30 UK job records the fills.</div><div class="tw"><table id="pending"></table></div></section>
<section class="card"><h2>Funding queue</h2><div class="sub">Conviction-4 buys waiting for room above the cash reserve, best first. A position that started small (a starter) is topped up first as room appears; the others are bought once there's room, or swapped in for a weaker holding by the weekly review. Each drops out after 30 days or if the price runs 10% above where we decided.</div><div class="tw"><table id="fqueue"></table></div></section>
<section class="card"><h2>Dip radar</h2><div class="sub" id="dipSub"></div><div class="tw"><table id="dips"></table></div></section>
<section class="card"><h2>Close to entry</h2><div class="sub" id="nearSub"></div><div class="tw"><table id="near"></table></div></section>
<section class="card"><h2>Watchlist: entry prices</h2><div class="sub">Conviction-3 names and the price at which we'd consider buying. A close at or below it triggers a full re-research (never an automatic buy). Closest first.</div><div class="tw"><table id="watch"></table></div></section>
<section class="card"><h2>Recent trades</h2><div class="tw"><table id="trades"></table></div></section>
<section class="card"><h2>Decisions &amp; hit rates</h2><div class="sub">A decision is a hit when it was right about direction vs SPY: BUY/ADD/HOLD beat SPY, AVOID/SELL/TRIM lagged it.</div>
<div class="tiles" id="hits"></div><div class="tw" style="margin-top:12px"><table id="decisions"></table></div></section>
<section class="card"><h2>Latest screen</h2><div class="sub" id="screenSub"></div><div id="picks" style="margin-top:8px"></div></section>
<p class="sub muted">All prices and financials from stockanalysis.com. Generated by scripts/dashboard.py. <span id="repo"></span></p>
</main><div class="tip" id="tip" role="tooltip"></div>
<script type="application/json" id="data">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent);
const $=id=>document.getElementById(id),el=(t,a={},...k)=>{const e=document.createElement(t);for(const[x,y]of Object.entries(a))x==='class'?e.className=y:e.setAttribute(x,y);k.forEach(c=>e.append(c));return e;};
const NS='http://www.w3.org/2000/svg',sv=(t,a={})=>{const e=document.createElementNS(NS,t);for(const[x,y]of Object.entries(a))e.setAttribute(x,y);return e;};
const usd=(x,d=0)=>x==null||isNaN(x)?'n/a':(x<0?'-':'')+'$'+Math.abs(x).toLocaleString('en-US',{minimumFractionDigits:d,maximumFractionDigits:d});
const pct=(x,d=2)=>x==null?'n/a':(x>=0?'+':'')+x.toFixed(d)+'%';
const cls=x=>x==null?'':x>=0?'up':'down';
const px=x=>x==null||x===''||isNaN(+x)?'':(+x).toLocaleString('en-US',{maximumFractionDigits:Math.abs(+x)<10?4:2});  // share prices
try{const t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t;}catch(e){}
$('theme').onclick=()=>{const dark=matchMedia('(prefers-color-scheme: dark)').matches;const cur=document.documentElement.dataset.theme||(dark?'dark':'light');
const n=cur==='dark'?'light':'dark';document.documentElement.dataset.theme=n;try{localStorage.setItem('theme',n)}catch(e){}};
$('start').textContent=D.start.toLocaleString('en-US');$('gen').textContent=D.generated;
$('hero').textContent=usd(D.total);
const I=D.invested;
$('heroSub').textContent=(D.inception?`At the ${D.close_date} close. `+(I?`Invested money ${pct(I.pct*100)} vs the same money in the S&P 500 ${pct(I.spy_pct==null?null:I.spy_pct*100)}; whole portfolio incl. cash ${pct(D.since==null?null:D.since*100)} since ${D.series.length?D.series[0].date:D.inception}`:`Since ${D.inception}: ${pct(D.since==null?null:D.since*100)} vs SPY ${pct(D.since_spy==null?null:D.since_spy*100)}`):'No trades yet: the portfolio is all cash.')
 +(D.live_total!=null?` · Live estimate ${usd(D.live_total)} (${pct((D.live_total/D.total-1)*100,2)} since the close) at ${D.live_at}`:'');
const tile=(l,v,d,c)=>el('div',{class:'tile'},el('div',{class:'l'},l),el('div',{class:'v'},v),d?el('div',{class:'d '+(c||'')},d):'');
$('tiles').append(
 I?tile('Return on invested money',pct(I.pct*100),`${usd(I.gain)} gain on ${usd(I.invested)} invested`+(I.dividends?` incl. ${usd(I.dividends)} dividends`:'')+(I.spy_pct==null?'':` · same money in S&P 500 ${pct(I.spy_pct*100)}`),cls(I.spy_pct==null?null:I.pct-I.spy_pct))
  :tile('Return on invested money','–','starts with the first trade'),
 D.inception?tile('Whole portfolio (incl. cash)',D.since==null?'n/a':pct(D.since*100),D.since_spy==null?'':'S&P 500 '+pct(D.since_spy*100),cls(D.since==null||D.since_spy==null?null:D.since-D.since_spy))
  :tile('Whole portfolio (incl. cash)','–','starts with the first trade'),
 tile('This week (whole portfolio)',D.week?pct(D.week.portfolio*100):'n/a',D.week&&D.week.spy!=null?'SPY '+pct(D.week.spy*100):'',''),
 tile('Cash',usd(D.cash),(D.total?(D.cash/D.total*100).toFixed(1)+'% of portfolio':'')+(D.interest?` · earns ${D.interest.aer_pct}% AER, ${usd(D.interest.total_usd)} so far`:'')+(D.receivable?` · ${usd(D.receivable,2)} dividends due`:'')),
 tile('Cash strategy',D.regime?({risk_on:'Risk-on',neutral:'Neutral',defensive:'Defensive'})[D.regime.final_regime]:'n/a',D.regime?(D.regime.stress!=null?`stress ${D.regime.stress}/100 · `:'')+`reserve ${D.regime.reserve_pct}% · S&P ${D.regime.dip.drawdown_pct}% off its high`+(D.regime.dip.multiplier<1?' · buying the dip':''):''),
 tile('Holdings',String(D.holdings.length),D.holdings.filter(h=>h.type==='CORE').length+' core · '+D.holdings.filter(h=>h.type==='TACTICAL').length+' tactical'),
 tile('Decisions logged',String(D.n_decisions),'')
);
const tip=$('tip');function showTip(ev,nodes){tip.replaceChildren(...nodes);tip.style.display='block';const x=Math.min(ev.clientX+14,innerWidth-tip.offsetWidth-8);
tip.style.left=x+'px';tip.style.top=Math.max(8,ev.clientY-tip.offsetHeight-12)+'px';}function hideTip(){tip.style.display='none'}
// ---- line chart
const S=D.series.filter(p=>p.portfolio!=null).map(p=>({...p,...Object.fromEntries(['invested','spy_same','portfolio','spy','baseline'].map(k=>[k,p[k]==null?null:p[k]-100]))}));  // % return since inception
const TABS={invested:{sub:'Gain on the money put into stocks, cash excluded, vs the same money put into the S&P 500 on the same days (%, US dollars).',
  defs:[['invested','Invested money','--s1','Invested'],['spy_same','Same money in S&P 500','--s2','S&P 500']]},
 whole:{sub:'All $100k, cash and its interest included, vs the S&P 500 since inception (%, US dollars). Baseline = the first week\'s picks held unchanged.',
  defs:[['portfolio','Whole portfolio (incl. cash)','--s1','Portfolio'],['spy','S&P 500 (SPY)','--s2','S&P 500'],['baseline','Baseline','--s3','Baseline']]}};
let defs=[];
function setTab(name){const t=TABS[name]||TABS.invested;defs=t.defs.filter(([k])=>S.some(p=>p[k]!=null));
 document.querySelectorAll('.tab').forEach(b=>b.setAttribute('aria-selected',String(b.dataset.tab===name)));
 $('lineSub').textContent=t.sub;$('lineLegend').replaceChildren(...defs.map(([k,n,c])=>el('span',{},el('span',{class:'key',style:`background:var(${c})`}),n)));
 $('lineTable').replaceChildren(el('tr',{},el('th',{},'Date'),...defs.map(([,n])=>el('th',{class:'n'},n)),el('th',{class:'n'},'Value')),
  ...S.map(p=>el('tr',{},el('td',{},p.date),...defs.map(([k])=>el('td',{class:'n'},p[k]==null?'n/a':pct(p[k]))),el('td',{class:'n'},usd(p.value)))));
 try{localStorage.setItem('chartTab',name)}catch(e){}drawLine();}
document.querySelectorAll('.tab').forEach(b=>b.onclick=()=>setTab(b.dataset.tab));
function drawLine(){const box=$('line');box.replaceChildren();
 if(S.length<2){box.append(el('div',{class:'empty'},'The chart appears after the second weekly run.'));return;}
 const W=Math.max(300,Math.round(box.getBoundingClientRect().width)),H=W<560?220:300,L=40,R=W<560?92:120,T=12,B=28,xs=S.map(p=>Date.parse(p.date)),x0=Math.min(...xs),x1=Math.max(...xs);
 const all=S.flatMap(p=>defs.map(([k])=>p[k]).filter(v=>v!=null));let lo=Math.min(0,...all),hi=Math.max(0,...all);const pad=Math.max((hi-lo)*.1,1);lo-=pad;hi+=pad;
 const X=t=>L+(t-x0)/(x1-x0||1)*(W-L-R),Y=v=>T+(hi-v)/(hi-lo)*(H-T-B);const svg=sv('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'Return on invested money vs the same money in the S&P 500, and the whole portfolio (%)'});
 const step=(hi-lo)/4;for(let i=0;i<=4;i++){const v=lo+step*i;svg.append(sv('line',{x1:L,x2:W-R,y1:Y(v),y2:Y(v),stroke:'var(--grid)','stroke-width':1}));
  const t=sv('text',{x:L-6,y:Y(v)+4,'text-anchor':'end'});t.textContent=v.toFixed(Math.abs(hi-lo)<4?1:0)+'%';svg.append(t);}
 const ticks=S.length<=6?S:S.filter((_,i)=>i%Math.ceil(S.length/6)===0);ticks.forEach(p=>{const t=sv('text',{x:X(Date.parse(p.date)),y:H-8,'text-anchor':'middle'});t.textContent=p.date.slice(5);svg.append(t);});
 svg.append(sv('line',{x1:L,x2:W-R,y1:Y(0),y2:Y(0),stroke:'var(--axis)','stroke-width':1}));
 const ends=[];defs.forEach(([k,n,c,short])=>{const P=S.filter(p=>p[k]!=null);if(P.length<2)return;
  svg.append(sv('path',{d:P.map((p,i)=>(i?'L':'M')+X(Date.parse(p.date)).toFixed(1)+','+Y(p[k]).toFixed(1)).join(''),fill:'none',stroke:`var(${c})`,'stroke-width':2,'stroke-linejoin':'round','stroke-linecap':'round'}));
  const e=P[P.length-1];ends.push({y:Y(e[k]),x:X(Date.parse(e.date)),c,label:(short||n)+' '+pct(e[k],1)});});
 ends.sort((a,b)=>a.y-b.y);let prev=-1e9;ends.forEach(e=>{e.ly=Math.max(e.y,prev+16);prev=e.ly;});
 ends.forEach(e=>{svg.append(sv('circle',{cx:e.x,cy:e.y,r:4,fill:`var(${e.c})`,stroke:'var(--surface)','stroke-width':2}));
  if(Math.abs(e.ly-e.y)>2)svg.append(sv('line',{x1:e.x+6,y1:e.y,x2:e.x+12,y2:e.ly,stroke:'var(--axis)','stroke-width':1}));
  const t=sv('text',{x:e.x+14,y:e.ly+4});t.style.fill='var(--ink2)';t.textContent=e.label;svg.append(t);});
 const cross=sv('line',{y1:T,y2:H-B,stroke:'var(--axis)','stroke-width':1,visibility:'hidden'});svg.append(cross);
 const hit=sv('rect',{x:L,y:T,width:W-L-R,height:H-T-B,fill:'transparent'});svg.append(hit);
 hit.addEventListener('pointermove',ev=>{const r=svg.getBoundingClientRect(),px=(ev.clientX-r.left)/r.width*W;let best=S[0];
  S.forEach(p=>{if(Math.abs(X(Date.parse(p.date))-px)<Math.abs(X(Date.parse(best.date))-px))best=p;});const cx=X(Date.parse(best.date));
  cross.setAttribute('x1',cx);cross.setAttribute('x2',cx);cross.setAttribute('visibility','visible');
  const rows=[el('div',{},el('span',{class:'muted'},best.date+' · '+usd(best.value)))];
  defs.forEach(([k,n,c])=>{if(best[k]!=null)rows.push(el('div',{class:'r'},el('span',{class:'key',style:`background:var(${c})`}),el('b',{},pct(best[k])),el('span',{class:'muted'},n)));});showTip(ev,rows);});
 hit.addEventListener('pointerleave',()=>{cross.setAttribute('visibility','hidden');hideTip();});box.append(svg);}
// ---- horizontal bars
function hbars(box,items,emptyMsg){box.replaceChildren();if(!items.length){box.append(el('div',{class:'empty'},emptyMsg));return;}
 const rowH=28,W=Math.max(280,Math.round(box.getBoundingClientRect().width)),R=56,
  L=Math.min(Math.round(W*.45),Math.max(...items.map(i=>i.label.length))*7+12),H=items.length*rowH+8,max=Math.max(...items.map(i=>i.v));const svg=sv('svg',{viewBox:`0 0 ${W} ${H}`,role:'img'});
 items.forEach((it,i)=>{const y=4+i*rowH,w=Math.max(2,(it.v/max)*(W-L-R)),h=16,r=4;
  const lab=sv('text',{x:L-8,y:y+h/2+4,'text-anchor':'end'});lab.style.fill='var(--ink2)';const maxCh=Math.floor((L-12)/7);lab.textContent=it.label.length>maxCh?it.label.slice(0,maxCh-1)+'…':it.label;svg.append(lab);
  const d=`M${L},${y}H${L+w-r}Q${L+w},${y} ${L+w},${y+r}V${y+h-r}Q${L+w},${y+h} ${L+w-r},${y+h}H${L}Z`;
  const bar=sv('path',{d,fill:`var(${it.c||'--s1'})`});svg.append(bar);
  const val=sv('text',{x:L+w+6,y:y+h/2+4});val.textContent=it.v.toFixed(1)+'%';svg.append(val);
  const hit=sv('rect',{x:0,y:y-4,width:W,height:rowH,fill:'transparent',tabindex:0});
  const tipN=()=>[el('div',{},el('b',{},it.v.toFixed(2)+'%'),' ',el('span',{class:'muted'},it.tip||it.label))];
  hit.addEventListener('pointermove',ev=>{bar.style.opacity=.8;showTip(ev,tipN());});hit.addEventListener('pointerleave',()=>{bar.style.opacity=1;hideTip();});
  svg.append(hit);});box.append(svg);}
function drawAll(){drawLine();riskBars();
 hbars($('bars'),D.holdings.map(h=>({label:h.ticker,v:h.weight,c:h.type==='CORE'?'--s1':'--s2',tip:`${h.ticker} ${h.name} · ${h.type.toLowerCase()} · ${usd(h.value)}`})),'No holdings yet.');
 hbars($('sectors'),D.sectors.map(([s,v])=>({label:s,v})),'No holdings yet.');}
// ---- risk: paired bars (risk share vs share of invested money)
function riskBars(){const box=$('risk');box.replaceChildren();const R=D.risk;
 if(!R||!R.rows.some(r=>r.risk_share_pct!=null)){box.append(el('div',{class:'empty'},'Appears after the first weekly risk report.'));return;}
 const inv=R.rows.reduce((a,r)=>a+(r.weight_pct||0),0),rows=R.rows.filter(r=>r.risk_share_pct!=null);
 const rowH=34,W=Math.max(280,Math.round(box.getBoundingClientRect().width)),L=78,Rm=52,H=rows.length*rowH+4,max=Math.max(...rows.flatMap(r=>[r.risk_share_pct,r.weight_pct/inv*100]));
 const svg=sv('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'Each holding: share of portfolio risk vs share of invested money'});
 rows.forEach((r,i)=>{const y=2+i*rowH,ws=r.weight_pct/inv*100,sc=x=>Math.max(2,x/max*(W-L-Rm));
  const lab=sv('text',{x:L-8,y:y+13,'text-anchor':'end'});lab.style.fill='var(--ink2)';lab.textContent=r.ticker;svg.append(lab);
  const b1=sv('rect',{x:L,y:y+2,width:sc(r.risk_share_pct),height:12,rx:3,fill:r.flag?'var(--down)':'var(--s1)'});svg.append(b1);
  const b2=sv('rect',{x:L,y:y+17,width:sc(ws),height:8,rx:2,fill:'var(--axis)'});svg.append(b2);
  const v=sv('text',{x:L+sc(r.risk_share_pct)+6,y:y+12});v.textContent=r.risk_share_pct.toFixed(1)+'%';svg.append(v);
  const hit=sv('rect',{x:0,y,width:W,height:rowH,fill:'transparent'});
  hit.addEventListener('pointermove',ev=>showTip(ev,[el('div',{},el('b',{},r.ticker),el('span',{class:'muted'},` · vol ${r.vol_pct==null?'n/a':r.vol_pct.toFixed(0)+'%'}`)),
   el('div',{},`${r.risk_share_pct.toFixed(1)}% of risk on ${ws.toFixed(1)}% of invested money`),r.flag?el('div',{class:'down'},'over its risk budget (more than 2x)'):'']));
  hit.addEventListener('pointerleave',hideTip);svg.append(hit);});box.append(svg);}
{const R=D.risk;$('riskSub').textContent=R?`${R.asof}: portfolio volatility ${R.sigma_p==null?'n/a':R.sigma_p.toFixed(1)+'%'} a year (cash included). How much of the portfolio's ups and downs each holding drives, next to how much money it holds. Red = more than twice its share. Informational; never trades.`:'No risk report yet.';
 table('riskTable',[{h:'Ticker',f:r=>r.ticker},{h:'Weight',n:1,f:r=>r.weight_pct==null?'':r.weight_pct.toFixed(1)+'%'},{h:'Target',n:1,f:r=>r.target_pct==null?'':r.target_pct.toFixed(1)+'%'},
  {h:'Volatility',n:1,f:r=>r.vol_pct==null?'n/a':r.vol_pct.toFixed(0)+'%'},{h:'MCR',n:1,f:r=>r.mcr_pct==null?'n/a':r.mcr_pct.toFixed(1)+'%'},
  {h:'Risk share',n:1,f:r=>r.risk_share_pct==null?'n/a':r.risk_share_pct.toFixed(1)+'%',c:r=>r.flag?'down':''}],R?R.rows:[],'No risk report yet.');}
{const A=D.attribution,p2=x=>x==null?'n/a':pct(x*100,2);
 if(!A){$('attrSub').textContent='Appears after the first weekly attribution report.';}
 else{$('attrSub').textContent=`${A.start} to ${A.end} (${A.days} trading days) vs a sector-weighted S&P 500. Informational: not meaningful until about 6 months of history. Cash is its own sector, so the reserve's cost or benefit shows in allocation.`;
  $('attrTiles').append(tile('Excess return',p2(A.excess),`portfolio ${p2(A.portfolio)} · index ${p2(A.benchmark)}`,cls(A.excess)),
   tile('Sector bets (allocation)',p2(A.allocation),'which sectors, and cash, we held',cls(A.allocation)),
   tile('Stock picking (selection)',p2(A.selection),'our stocks vs their sector',cls(A.selection)),
   tile('Interaction',p2(A.interaction),'overweight where we also picked well (or not)',cls(A.interaction)));
  const rows=Object.entries(A.sectors).map(([s,e])=>({s,...e,t:e.allocation+e.selection+e.interaction})).filter(r=>r.wp_avg>0||Math.abs(r.t)>5e-5).sort((a,b)=>Math.abs(b.t)-Math.abs(a.t));
  table('attrTable',[{h:'Sector',f:r=>r.s},{h:'Our weight',n:1,f:r=>(r.wp_avg*100).toFixed(1)+'%'},{h:'Index',n:1,f:r=>(r.wb*100).toFixed(1)+'%'},
   {h:'Allocation',n:1,f:r=>p2(r.allocation),c:r=>cls(r.allocation)},{h:'Selection',n:1,f:r=>p2(r.selection),c:r=>cls(r.selection)},
   {h:'Interaction',n:1,f:r=>p2(r.interaction),c:r=>cls(r.interaction)},{h:'Total',n:1,f:r=>p2(r.t),c:r=>cls(r.t)}],rows,'');}}
{let t0='invested';try{t0=localStorage.getItem('chartTab')||t0}catch(e){}setTab(TABS[t0]?t0:'invested');}
drawAll();let rz;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(drawAll,150);});
// ---- tables
function table(id,cols,rows,empty){const t=$(id);t.append(el('tr',{},...cols.map(c=>el('th',{class:c.n?'n':''},c.h))));
 if(!rows.length){t.append(el('tr',{},el('td',{colspan:cols.length,class:'muted'},empty)));return;}
 rows.forEach(r=>t.append(el('tr',{},...cols.map(c=>{const v=c.f(r);const td=el('td',{class:(c.n?'n ':'')+(c.w?'w ':'')+(c.c?c.c(r):'')});
  if(v instanceof Node)td.append(v);else td.textContent=v;return td;}))));}
const link=(path,txt)=>D.repo&&path?el('a',{href:`${D.repo}/blob/main/${path}`,target:'_blank',rel:'noopener'},txt):txt;
table('holdings',[{h:'Ticker',f:r=>r.ticker},{h:'Name',f:r=>r.name},{h:'Type',f:r=>r.type.toLowerCase()},{h:'Conv.',n:1,f:r=>r.conviction??''},
 {h:'Entry',f:r=>r.entry_date},{h:'Entry price',n:1,f:r=>r.entry_price==null?'':px(r.entry_price)+' '+r.currency},{h:'Close',n:1,f:r=>r.last_price==null?'':`${px(r.last_price)} ${r.currency} (${r.last_date})`},
 {h:'Change',n:1,f:r=>pct(r.change_pct,1),c:r=>cls(r.change_pct)},
 {h:'Live',n:1,f:r=>r.live?`${r.live.price.toFixed(2)} (${r.live.uk})`:'–'},{h:'Live change',n:1,f:r=>r.live_change_pct==null?'–':pct(r.live_change_pct,1),c:r=>cls(r.live_change_pct)},{h:'Value',n:1,f:r=>usd(r.value)},{h:'Weight',n:1,f:r=>r.weight.toFixed(1)+'%'},
 {h:'P/L',n:1,f:r=>r.pl==null?'':usd(r.pl),c:r=>cls(r.pl)},{h:'Plan',w:1,f:r=>r.plan}],D.holdings,'No holdings yet: the portfolio is all cash.');
const isHold=r=>r.action==='HOLD';
table('pending',[{h:'Placed',f:r=>r.placed},{h:'Action',f:r=>r.action},{h:'Ticker',f:r=>r.ticker},{h:'Type',f:r=>(r.type||'').toLowerCase()},
 {h:'Conv.',n:1,f:r=>r.conviction??''},{h:'Est. shares',n:1,f:r=>isHold(r)?'–':(r.est.shares??'')},
 {h:'Latest close',n:1,f:r=>isHold(r)||r.est.price==null?'–':`${px(r.est.price)} ${r.est.currency} (${r.est.close_date})`},
 {h:'Est. value',n:1,f:r=>isHold(r)||r.est_usd==null?'–':usd(r.est_usd)},
 {h:'Fills',f:r=>r.fills||''},
 {h:'Note',w:1,f:r=>isHold(r)?'No trade: records the refreshed thesis and conviction from the re-research.':(r.replaces?`Replaces ${r.replaces}.`:'Rules re-checked at the opening price before it fills.')}],
 D.pending,'No pending orders.');
table('fqueue',[{h:'Ticker',f:r=>r.ticker},{h:'Name',f:r=>r.name},{h:'Stage',f:r=>r.stage==='topup'?(r.ordered?'starter ordered':'top-up'):'waiting'},
 {h:'Conv.',n:1,f:r=>r.conviction??''},{h:'Decided',f:r=>`${r.added} at ${px(r.decision_price)} ${r.ccy}`},
 {h:'Latest close',n:1,f:r=>r.close==null?'':`${px(r.close)} ${r.ccy}`},{h:'Base FV upside',n:1,f:r=>r.upside==null?'–':pct(r.upside,0),c:r=>cls(r.upside)},
 {h:'Weight / target',n:1,f:r=>r.stage==='topup'&&r.weight!=null&&r.target!=null?`${r.weight.toFixed(1)}% of ${(+r.target).toFixed(1)}%`:'–'},
 {h:'Expires',f:r=>r.expires},{h:'Evaluation',f:r=>link(r.evaluation,'read')}],D.funding_queue||[],'Nothing waiting: every conviction-4 buy fitted.');
{const P=D.dip;$('dipSub').textContent=P?`${P.asof}: ${P.watched} stocks watched (holdings and recent conviction-3+ AVOIDs). A signal is an unusual fall since our last research, beyond what the market explains (z = standard deviations of the stock's own moves; −2 or lower), with the price at or below base fair value. Signals are re-researched the next day; a fall is never a buy on its own. ${P.hits.length?'Queued: '+P.hits.join(', ')+'.':'Nothing queued.'}`:'The dip radar has not run yet.';
table('dips',[{h:'Ticker',f:r=>r.ticker},{h:'Kind',f:r=>r.kind==='holding'?'holding':'avoid'},{h:'Signal',f:r=>r.signal?'YES':''},
 {h:'z',n:1,f:r=>r.z==null?'–':r.z.toFixed(2),c:r=>r.z!=null&&r.z<=-2?'down':''},
 {h:'Since research',f:r=>r.last_research?`${r.last_research} (${r.sessions} sessions)`:''},
 {h:'Return',n:1,f:r=>r.ret_pct==null?'–':pct(r.ret_pct,1),c:r=>cls(r.ret_pct)},{h:'S&P',n:1,f:r=>r.spy_pct==null?'–':pct(r.spy_pct,1)},
 {h:'Stock-specific',n:1,f:r=>r.specific_pct==null?'–':pct(r.specific_pct,1),c:r=>cls(r.specific_pct)},
 {h:'vs base FV',n:1,f:r=>r.vs_base_pct==null?'–':pct(r.vs_base_pct,0)},{h:'Why not a signal',w:1,f:r=>r.signal?'':(r.why_not||'')}],
 P?P.rows:[],'No unusual falls since our last research (nothing at z −1 or lower).');}
{const np=D.near_pct??10,nr=(D.watch||[]).filter(r=>r.to_entry!=null&&r.to_entry>=-np);
document.getElementById('nearSub').textContent=`Stocks within ${np}% of their entry price, closest first, with the evaluator's reason each isn't a buy yet. Information only: a close at or below the entry price triggers a re-research, never a purchase.`;
const lv=r=>r.live?`${r.live.price.toFixed(2)} (${r.live.uk})`:'–',lte=r=>r.live?(r.entry/r.live.price-1)*100:null;
table('near',[{h:'Ticker',f:r=>r.ticker},{h:'Close',n:1,f:r=>r.close==null||r.close===''?'':`${(+r.close).toFixed(2)} ${r.ccy} (${r.close_date})`},
 {h:'Live',n:1,f:lv},
 {h:'Entry price',n:1,f:r=>`${(+r.entry).toFixed(2)} ${r.ccy}`},{h:'To entry (close)',n:1,f:r=>pct(r.to_entry,1),c:r=>r.to_entry>=0?'up':''},
 {h:'To entry (live)',n:1,f:r=>{const x=lte(r);return x==null?'–':pct(x,1);},c:r=>lte(r)>=0?'up':''},
 {h:'Since',f:r=>r.hit?'HIT '+r.hit:(r.near_since||'')},
 {h:'Why not a buy yet',w:1,f:r=>{const t=r.why||'evaluation',a=link(r.evaluation,t.length>110?t.slice(0,109).replace(/\s\S*$/,'')+'…':t);if(a instanceof Node)a.title=t;return a;}}],nr,`No stock is within ${np}% of its entry price.`);}
table('watch',[{h:'Ticker',f:r=>r.ticker},{h:'Conv.',n:1,f:r=>r.conviction??''},{h:'Close',n:1,f:r=>r.close==null||r.close===''?'':`${(+r.close).toFixed(2)} ${r.ccy} (${r.close_date})`},
 {h:'Live',n:1,f:r=>r.live?`${r.live.price.toFixed(2)} (${r.live.uk})`:'–'},
 {h:'To entry (live)',n:1,f:r=>{const x=r.live?(r.entry/r.live.price-1)*100:null;return x==null?'–':pct(x,1);},c:r=>r.live&&r.entry>=r.live.price?'up':''},
 {h:'Entry price',n:1,f:r=>`${(+r.entry).toFixed(2)} ${r.ccy}`},{h:'To entry (close)',n:1,f:r=>r.to_entry==null?'':pct(r.to_entry,1),c:r=>r.to_entry!=null&&r.to_entry>=0?'up':''},
 {h:'Status',f:r=>r.hit?'HIT '+r.hit+': re-research next run':''},{h:'Set by',f:r=>r.source}],D.watch||[],'No entry prices yet.');
table('trades',[{h:'Date',f:r=>r.date},{h:'Side',f:r=>r.side},{h:'Ticker',f:r=>r.ticker},{h:'Type',f:r=>(r.type||'').toLowerCase()},{h:'Shares',n:1,f:r=>r.shares},
 {h:'Fill',n:1,f:r=>`${px(r.fill_price)} ${r.currency} (${r.fill_close_date})`},{h:'Gross',n:1,f:r=>usd(+r.gross_usd,2)},{h:'Costs',n:1,f:r=>usd(+r.costs_usd,2)},
 {h:'Reason',w:1,f:r=>{const sp=el('span',{title:r.reason||''});sp.textContent=(r.reason||'').length>140?r.reason.slice(0,139)+'…':(r.reason||'');return sp;}}],D.ledger,'No trades yet.');
['1m','3m','6m','12m'].forEach(h=>{const x=D.hits[h];$('hits').append(tile(h+' hit rate',x.n?Math.round(x.hits/x.n*100)+'%':'–',x.n?`${x.hits} of ${x.n} decisions`:'none matured yet'));});
table('decisions',[{h:'Date',f:r=>r.date},{h:'Ticker',f:r=>r.ticker},{h:'Type',f:r=>(r.type||'').toLowerCase()},{h:'Decision',f:r=>r.decision},
 {h:'Conv.',n:1,f:r=>r.conviction},{h:'Price',n:1,f:r=>`${(+r.price).toFixed(2)} ${r.currency} (${r.live?'live, ':'close '}${r.price_date})`},{h:'1m vs SPY',n:1,f:r=>r.excess_1m===''?'–':pct(+r.excess_1m,1),c:r=>r.excess_1m===''?'':cls(+r.excess_1m)},
 {h:'3m vs SPY',n:1,f:r=>r.excess_3m===''?'–':pct(+r.excess_3m,1),c:r=>r.excess_3m===''?'':cls(+r.excess_3m)},{h:'Evaluation',f:r=>link(r.evaluation,'read')}],D.decisions,'No decisions yet.');
$('screenSub').textContent=D.screen.asof?`${D.screen.asof}: ${D.screen.screened} stocks scored${D.screen.illiquid?` (${D.screen.illiquid} too thinly traded to rank were left out first)`:''}. The picks below were sent to research. The score ranks how well a stock fits the screen (core: quality and value; tactical: the strength of its setup). It is not a rating: research decides, and most picks come back AVOID.`:'No screen yet.';
D.screen.picks.forEach(p=>$('picks').append(el('span',{class:'pill',style:'margin:0 6px 6px 0'},`${p.ticker} · ${p.type.toLowerCase()} · ${p.score}`)));
if(D.repo)$('repo').append('Source and research notes: ',el('a',{href:D.repo},D.repo.replace('https://','')));
</script></body></html>
"""


def render(data: dict) -> str:
    blob = json.dumps(data).replace("</", "<\\/")  # never let data close the script tag
    return PAGE.replace("__DATA__", blob)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--no-live", action="store_true", help="skip the live-price snapshot (offline / tests)")
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(build_data(live=not a.no_live)))
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())

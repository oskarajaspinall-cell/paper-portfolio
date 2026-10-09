"""Build docs/index.html: a self-contained portfolio dashboard (no external libraries, no model calls).

Reads portfolio/state.json, valuations.csv, ledger.csv, decisions.csv, universe/universe.csv (names,
optional) and the latest reports/screen/<date>.json. Open the file in any browser, or publish it with
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
from common import ROOT, load_config  # noqa: E402

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
    out = []
    for v in pts:
        tot, spy, base = _f(v["total_usd"]), _f(v["spy_close"]), _f(v.get("baseline_usd"))
        out.append({"date": v["date"], "value": tot,
                    "portfolio": None if tot is None else tot / start_cash * 100,
                    "spy": None if not (spy and spy0) else spy / spy0 * 100,
                    "baseline": None if base is None else base / start_cash * 100})
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


def build_data() -> dict:
    cfg = load_config()
    port = ROOT / "portfolio"
    state = json.loads((port / "state.json").read_text()) if (port / "state.json").exists() else {"holdings": {}, "cash_usd": 0}
    start = float(cfg["portfolio"]["starting_cash_usd"])
    names = {r["ticker"]: r["name"] for r in _csv(ROOT / "universe" / "universe.csv")}
    hold = []
    total = state.get("cash_usd", 0.0) + sum(h.get("market_value_usd", 0.0) for h in state["holdings"].values())
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
    sectors: dict[str, float] = {}
    for h in hold:
        sectors[h["sector"] or "Unknown"] = sectors.get(h["sector"] or "Unknown", 0) + h["weight"]
    vals = _csv(port / "valuations.csv")
    ser = series(vals, start)
    ledger = _csv(port / "ledger.csv")[-25:][::-1]
    decisions = _csv(port / "decisions.csv")
    screens = sorted((ROOT / "reports" / "screen").glob("20??-??-??.json"))
    screen = json.loads(screens[-1].read_text()) if screens else {}
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
        "total": total, "cash": state.get("cash_usd", 0.0), "start": start,
        "inception": state.get("inception_date"),
        "since": None if not last or last["portfolio"] is None else last["portfolio"] / 100 - 1,
        "since_spy": None if not last or last["spy"] is None else last["spy"] / 100 - 1,
        "week": week, "series": ser, "holdings": hold, "interest": state.get("cash_interest"),
        "sectors": sorted(([k, v] for k, v in sectors.items()), key=lambda kv: -kv[1]),
        "ledger": [{k: r.get(k, "") for k in ("date", "ticker", "type", "side", "shares", "fill_price", "currency",
                                              "fill_close_date", "gross_usd", "costs_usd", "reason")} for r in ledger],
        "decisions": [{k: d.get(k, "") for k in ("date", "ticker", "type", "decision", "conviction", "price", "currency",
                                                 "excess_1m", "excess_3m", "evaluation")} for d in decisions[::-1][:40]],
        "hits": hits, "n_decisions": len(decisions),
        "pending": [{"id": o["id"], "placed": o["placed"], "action": o["request"]["action"],
                     "ticker": o["request"]["ticker"], "type": o["request"]["position_type"],
                     "conviction": o["request"].get("conviction"), "est": o.get("estimate", {})}
                    for o in state.get("pending", [])],
        "screen": {"asof": screen.get("asof"), "screened": screen.get("screened"), "picks": screen.get("picks", [])},
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
.toggle{background:none;border:1px solid var(--ring);border-radius:8px;color:var(--ink2);padding:4px 10px;cursor:pointer;font:inherit;font-size:13px}
</style></head><body><main>
<header><div><h1>Paper Portfolio</h1><div class="sub">Simulated $<span id="start"></span> portfolio · paper trading only, not investment advice · updated <span id="gen"></span></div></div>
<button class="toggle" id="theme" type="button">Toggle dark mode</button></header>
<section class="card" aria-label="Summary"><div class="sub">Portfolio value</div><div class="hero" id="hero"></div><div class="sub" id="heroSub"></div>
<div class="tiles" id="tiles"></div></section>
<section class="card"><h2>Performance vs the S&amp;P 500</h2><div class="sub">Indexed to 100 at inception, in US dollars. Baseline = the first week's picks held unchanged.</div>
<div class="legend" id="lineLegend"></div><div id="line"></div>
<details><summary>Show as a table</summary><div class="tw"><table id="lineTable"></table></div></details></section>
<div class="grid2"><section class="card"><h2>Holdings by weight</h2><div class="legend"><span><span class="sw" style="background:var(--s1)"></span>Core</span>
<span><span class="sw" style="background:var(--s2)"></span>Tactical</span></div><div id="bars"></div></section>
<section class="card"><h2>Sectors</h2><div class="sub">% of the portfolio (cash excluded)</div><div id="sectors"></div></section></div>
<section class="card"><h2>Holdings</h2><div class="tw"><table id="holdings"></table></div></section>
<section class="card"><h2>Pending orders</h2><div class="sub">Decided trades fill at the next market open.</div><div class="tw"><table id="pending"></table></div></section>
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
try{const t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t;}catch(e){}
$('theme').onclick=()=>{const dark=matchMedia('(prefers-color-scheme: dark)').matches;const cur=document.documentElement.dataset.theme||(dark?'dark':'light');
const n=cur==='dark'?'light':'dark';document.documentElement.dataset.theme=n;try{localStorage.setItem('theme',n)}catch(e){}};
$('start').textContent=D.start.toLocaleString('en-US');$('gen').textContent=D.generated;
$('hero').textContent=usd(D.total);
$('heroSub').textContent=D.inception?`Since ${D.inception}: ${pct(D.since==null?null:D.since*100)} vs SPY ${pct(D.since_spy==null?null:D.since_spy*100)}`:'No trades yet: the portfolio is all cash.';
const tile=(l,v,d,c)=>el('div',{class:'tile'},el('div',{class:'l'},l),el('div',{class:'v'},v),d?el('div',{class:'d '+(c||'')},d):'');
const rel=(D.since!=null&&D.since_spy!=null)?(D.since-D.since_spy)*100:null;
$('tiles').append(
 D.inception?tile('Vs S&P 500 since inception',rel==null?'n/a':(rel>=0?'+':'')+rel.toFixed(2)+'pp',rel==null?'':(rel>=0?'▲ ahead':'▼ behind'),cls(rel))
  :tile('Vs S&P 500 since inception','–','starts with the first trade'),
 tile('This week',D.week?pct(D.week.portfolio*100):'n/a',D.week&&D.week.spy!=null?'SPY '+pct(D.week.spy*100):'',''),
 tile('Cash',usd(D.cash),(D.total?(D.cash/D.total*100).toFixed(1)+'% of portfolio':'')+(D.interest?` · earns ${D.interest.aer_pct}% AER, ${usd(D.interest.total_usd)} so far`:'')),
 tile('Holdings',String(D.holdings.length),D.holdings.filter(h=>h.type==='CORE').length+' core · '+D.holdings.filter(h=>h.type==='TACTICAL').length+' tactical'),
 tile('Decisions logged',String(D.n_decisions),'')
);
const tip=$('tip');function showTip(ev,nodes){tip.replaceChildren(...nodes);tip.style.display='block';const x=Math.min(ev.clientX+14,innerWidth-tip.offsetWidth-8);
tip.style.left=x+'px';tip.style.top=Math.max(8,ev.clientY-tip.offsetHeight-12)+'px';}function hideTip(){tip.style.display='none'}
// ---- line chart
const S=D.series.filter(p=>p.portfolio!=null);
const defs=[['portfolio','Portfolio','--s1'],['spy','S&P 500 (SPY)','--s2'],['baseline','Baseline','--s3']].filter(([k])=>S.some(p=>p[k]!=null));
defs.forEach(([k,n,c])=>$('lineLegend').append(el('span',{},el('span',{class:'key',style:`background:var(${c})`}),n)));
$('lineTable').append(el('tr',{},el('th',{},'Date'),...defs.map(([,n])=>el('th',{class:'n'},n)),el('th',{class:'n'},'Value')));
S.forEach(p=>$('lineTable').append(el('tr',{},el('td',{},p.date),...defs.map(([k])=>el('td',{class:'n'},p[k]==null?'n/a':p[k].toFixed(2))),el('td',{class:'n'},usd(p.value)))));
function drawLine(){const box=$('line');box.replaceChildren();
 if(S.length<2){box.append(el('div',{class:'empty'},'The chart appears after the second weekly run.'));return;}
 const W=Math.max(300,Math.round(box.getBoundingClientRect().width)),H=W<560?220:300,L=40,R=W<560?92:120,T=12,B=28,xs=S.map(p=>Date.parse(p.date)),x0=Math.min(...xs),x1=Math.max(...xs);
 const all=S.flatMap(p=>defs.map(([k])=>p[k]).filter(v=>v!=null));let lo=Math.min(...all),hi=Math.max(...all);const pad=Math.max((hi-lo)*.1,1);lo-=pad;hi+=pad;
 const X=t=>L+(t-x0)/(x1-x0||1)*(W-L-R),Y=v=>T+(hi-v)/(hi-lo)*(H-T-B);const svg=sv('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'Portfolio vs S&P 500, indexed to 100'});
 const step=(hi-lo)/4;for(let i=0;i<=4;i++){const v=lo+step*i;svg.append(sv('line',{x1:L,x2:W-R,y1:Y(v),y2:Y(v),stroke:'var(--grid)','stroke-width':1}));
  const t=sv('text',{x:L-6,y:Y(v)+4,'text-anchor':'end'});t.textContent=v.toFixed(0);svg.append(t);}
 const ticks=S.length<=6?S:S.filter((_,i)=>i%Math.ceil(S.length/6)===0);ticks.forEach(p=>{const t=sv('text',{x:X(Date.parse(p.date)),y:H-8,'text-anchor':'middle'});t.textContent=p.date.slice(5);svg.append(t);});
 svg.append(sv('line',{x1:L,x2:W-R,y1:Y(100),y2:Y(100),stroke:'var(--axis)','stroke-width':1}));
 const ends=[];defs.forEach(([k,n,c])=>{const P=S.filter(p=>p[k]!=null);if(P.length<2)return;
  svg.append(sv('path',{d:P.map((p,i)=>(i?'L':'M')+X(Date.parse(p.date)).toFixed(1)+','+Y(p[k]).toFixed(1)).join(''),fill:'none',stroke:`var(${c})`,'stroke-width':2,'stroke-linejoin':'round','stroke-linecap':'round'}));
  const e=P[P.length-1];ends.push({y:Y(e[k]),x:X(Date.parse(e.date)),c,label:(W<560?n.replace(' (SPY)',''):n)+' '+e[k].toFixed(1)});});
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
  defs.forEach(([k,n,c])=>{if(best[k]!=null)rows.push(el('div',{class:'r'},el('span',{class:'key',style:`background:var(${c})`}),el('b',{},best[k].toFixed(2)),el('span',{class:'muted'},n)));});showTip(ev,rows);});
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
function drawAll(){drawLine();
 hbars($('bars'),D.holdings.map(h=>({label:h.ticker,v:h.weight,c:h.type==='CORE'?'--s1':'--s2',tip:`${h.ticker} ${h.name} · ${h.type.toLowerCase()} · ${usd(h.value)}`})),'No holdings yet.');
 hbars($('sectors'),D.sectors.map(([s,v])=>({label:s,v})),'No holdings yet.');}
drawAll();let rz;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(drawAll,150);});
// ---- tables
function table(id,cols,rows,empty){const t=$(id);t.append(el('tr',{},...cols.map(c=>el('th',{class:c.n?'n':''},c.h))));
 if(!rows.length){t.append(el('tr',{},el('td',{colspan:cols.length,class:'muted'},empty)));return;}
 rows.forEach(r=>t.append(el('tr',{},...cols.map(c=>{const v=c.f(r);const td=el('td',{class:(c.n?'n ':'')+(c.w?'w ':'')+(c.c?c.c(r):'')});
  if(v instanceof Node)td.append(v);else td.textContent=v;return td;}))));}
const link=(path,txt)=>D.repo&&path?el('a',{href:`${D.repo}/blob/main/${path}`,target:'_blank',rel:'noopener'},txt):txt;
table('holdings',[{h:'Ticker',f:r=>r.ticker},{h:'Name',f:r=>r.name},{h:'Type',f:r=>r.type.toLowerCase()},{h:'Conv.',n:1,f:r=>r.conviction??''},
 {h:'Entry',f:r=>r.entry_date},{h:'Entry price',n:1,f:r=>r.entry_price==null?'':r.entry_price+' '+r.currency},{h:'Last',n:1,f:r=>r.last_price==null?'':r.last_price+' '+r.currency},
 {h:'Change',n:1,f:r=>pct(r.change_pct,1),c:r=>cls(r.change_pct)},{h:'Value',n:1,f:r=>usd(r.value)},{h:'Weight',n:1,f:r=>r.weight.toFixed(1)+'%'},
 {h:'P/L',n:1,f:r=>r.pl==null?'':usd(r.pl),c:r=>cls(r.pl)},{h:'Plan',w:1,f:r=>r.plan}],D.holdings,'No holdings yet: the portfolio is all cash.');
table('pending',[{h:'Placed',f:r=>r.placed},{h:'Action',f:r=>r.action},{h:'Ticker',f:r=>r.ticker},{h:'Type',f:r=>(r.type||'').toLowerCase()},
 {h:'Conv.',n:1,f:r=>r.conviction??''},{h:'Est. shares',n:1,f:r=>r.est.shares??''},{h:'Latest close',n:1,f:r=>r.est.price==null?'':`${r.est.price} ${r.est.currency}`}],
 D.pending,'No pending orders.');
table('trades',[{h:'Date',f:r=>r.date},{h:'Side',f:r=>r.side},{h:'Ticker',f:r=>r.ticker},{h:'Type',f:r=>(r.type||'').toLowerCase()},{h:'Shares',n:1,f:r=>r.shares},
 {h:'Fill',n:1,f:r=>`${r.fill_price} ${r.currency} (${r.fill_close_date})`},{h:'Gross',n:1,f:r=>usd(+r.gross_usd,2)},{h:'Costs',n:1,f:r=>usd(+r.costs_usd,2)},
 {h:'Reason',w:1,f:r=>{const sp=el('span',{title:r.reason||''});sp.textContent=(r.reason||'').length>140?r.reason.slice(0,139)+'…':(r.reason||'');return sp;}}],D.ledger,'No trades yet.');
['1m','3m','6m','12m'].forEach(h=>{const x=D.hits[h];$('hits').append(tile(h+' hit rate',x.n?Math.round(x.hits/x.n*100)+'%':'–',x.n?`${x.hits} of ${x.n} decisions`:'none matured yet'));});
table('decisions',[{h:'Date',f:r=>r.date},{h:'Ticker',f:r=>r.ticker},{h:'Type',f:r=>(r.type||'').toLowerCase()},{h:'Decision',f:r=>r.decision},
 {h:'Conv.',n:1,f:r=>r.conviction},{h:'Price',n:1,f:r=>`${r.price} ${r.currency}`},{h:'1m vs SPY',n:1,f:r=>r.excess_1m===''?'–':pct(+r.excess_1m,1),c:r=>r.excess_1m===''?'':cls(+r.excess_1m)},
 {h:'3m vs SPY',n:1,f:r=>r.excess_3m===''?'–':pct(+r.excess_3m,1),c:r=>r.excess_3m===''?'':cls(+r.excess_3m)},{h:'Evaluation',f:r=>link(r.evaluation,'read')}],D.decisions,'No decisions yet.');
$('screenSub').textContent=D.screen.asof?`${D.screen.asof}: ${D.screen.screened} stocks scored. This week's picks for research:`:'No screen yet.';
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
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(build_data()))
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())

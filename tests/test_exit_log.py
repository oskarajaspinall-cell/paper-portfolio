import exit_log as X

CFG = {"portfolio": {"benchmark": "SPY"}}


class Mkt:
    cfg = CFG

    def __init__(self, closes):  # {ticker: {date: usd close}}
        self.closes = closes

    def quote(self, t, on):
        d = max(x for x in self.closes[t] if x <= on)
        return {"close": self.closes[t][d], "price_usd": self.closes[t][d], "date": d}


def led(date, t, side, px, reason="", shares=10):
    return {"date": date, "ticker": t, "type": "CORE", "side": side, "shares": str(shares), "fill_price": str(px),
            "currency": "USD", "fx_usd_per_unit": "", "gross_usd": str(px * shares), "reason": reason}


def test_kind_from_real_ledger_reasons():
    assert X.kind_of("replaced by HKG:0291: Adding this name would take China/HK") == ("swap", "HKG:0291")
    assert X.kind_of("conviction 3 sizing: below the buy bar (4)") == ("sizing", "")
    assert X.kind_of("The quality thesis holds, but") == ("research", "")


def test_since_exit_swap_and_rebuild_keeps_outcomes():
    ledger = [led("2026-11-10", "OLD", "SELL", 100, "replaced by NEW: cheaper"), led("2026-11-10", "NEW", "BUY", 50),
              led("2026-11-10", "OLD", "BUY", 1)]
    m = Mkt({"OLD": {"2026-11-10": 100, "2026-11-17": 110}, "NEW": {"2026-11-10": 50, "2026-11-17": 60},
             "SPY": {"2026-11-10": 700, "2026-11-17": 707}})
    rows = X.rebuild(ledger, [], m)
    assert len(rows) == 1 and rows[0]["kind"] == "swap" and rows[0]["spy_close"] == 700
    X.since(rows, ledger, m, "2026-11-18")
    r = rows[0]
    assert (r["since_ret"], r["since_spy"], r["since_excess"]) == (10.0, 1.0, 9.0)  # sold name beat SPY: a wrong exit
    assert r["kept_usd"] == 100.0 and r["vs_replacement_since"] == 10.0  # NEW +20% minus OLD +10%
    r["hit_1m"] = 0
    assert X.rebuild(ledger, rows, m)[0]["hit_1m"] == 0  # filled outcomes survive a rebuild


def test_since_one_on_a_decision_row():
    import decision_log as DL
    r = {"ticker": "OLD", "price_date": "2026-11-10", "price_usd": "100", "spy_close": "700", "decision": "BUY"}
    m = Mkt({"OLD": {"2026-11-10": 100, "2026-11-17": 90}, "SPY": {"2026-11-10": 700, "2026-11-17": 707}})
    DL.since_one(r, m, "2026-11-18")
    assert (r["since_date"], r["since_ret"], r["since_spy"], r["since_excess"]) == ("2026-11-17", -10.0, 1.0, -11.0)

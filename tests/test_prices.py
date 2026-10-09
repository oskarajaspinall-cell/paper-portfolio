import json

import pandas as pd
import pytest

from conftest import FakeMarket
import portfolio as P
from prices import YahooPrices, rows_from_frame, yahoo_symbol


def frame(rows):
    idx = pd.DatetimeIndex([pd.Timestamp(d, tz="America/New_York") for d, *_ in rows])
    return pd.DataFrame({"Open": [r[1] for r in rows], "High": [r[2] for r in rows], "Low": [r[3] for r in rows],
                         "Close": [r[4] for r in rows], "Adj Close": [r[4] for r in rows],
                         "Volume": [1000 for _ in rows]}, index=idx)


def test_yahoo_symbols():
    assert yahoo_symbol("DECK") == "DECK" and yahoo_symbol("BRK.B") == "BRK-B"
    assert yahoo_symbol("LON:SHEL") == "SHEL.L" and yahoo_symbol("HKG:9999") == "9999.HK"
    assert yahoo_symbol("HKG:700") == "0700.HK" and yahoo_symbol("SHA:600036") == "600036.SS"
    assert yahoo_symbol("TPE:2330") == "2330.TW" and yahoo_symbol("KRX:000660") == "000660.KS"
    assert yahoo_symbol("TYO:6857") == "6857.T" and yahoo_symbol("NSE:TCS") == "TCS.NS"
    assert yahoo_symbol("TSX:ABX") == "ABX.TO" and yahoo_symbol("XETRA:SAP") is None  # unmapped -> fallback


def test_frame_rows_and_minor_units():
    rows = rows_from_frame(frame([("2026-10-07", 81.15, 81.4, 79.1, 80.38), ("2026-10-08", 80.14, 83.0, 79.9, 82.56)]))
    assert rows[-1] == {"date": "2026-10-08", "open": 80.14, "high": 83.0, "low": 79.9, "close": 82.56,
                        "adj_close": 82.56, "volume": 1000.0}
    y = YahooPrices(loader=lambda sym, p: (frame([("2026-10-08", 3680.5, 3784, 3676.5, 3780.5)]), "GBp"))
    assert y.history("LON:SHEL")["currency"] == "GBX"
    with pytest.raises(P.DataError):
        YahooPrices(loader=lambda sym, p: (frame([]), "USD")).history("AAPL")


class YMarket(FakeMarket):
    """FakeMarket whose prices come from a Yahoo provider first (stockanalysis.com = the fake's history)."""
    def __init__(self, cfg, provider, sa_open=None, **kw):
        from test_portfolio import PRICES
        super().__init__(PRICES, cfg, **kw)
        self.price_source, self.fallbacks, self._sa_open = provider, [], sa_open

    def history(self, t):
        y = self._primary(t)
        if y:
            return {"url": y["url"], "rows": [r for r in y["rows"] if r["date"] < self.asof], "all_rows": y["rows"],
                    "currency": y["currency"], "news": [], "source": "yfinance"}
        h = super().history(t)
        return {**h, "source": "stockanalysis"}

    def stockanalysis_open(self, t, day):
        return self._sa_open


def yahoo(opens):
    return YahooPrices(loader=lambda sym, p: (frame([(d, o, o, o, o) for d, o in opens[sym]]), "USD"))


def test_fill_uses_the_yahoo_open_and_cross_checks(cfg, tmp_path):
    from test_portfolio import WATCH, core_buy
    sp = tmp_path / "state.json"
    P.place_orders([core_buy("AAPL", conv=4)], sp, YMarket(cfg, None), cfg, WATCH, "2026-10-10", port_dir=tmp_path)
    y = yahoo({"AAPL": [("2026-10-09", 200.0), ("2026-10-12", 210.0)]})
    out = P.fill_pending(sp, YMarket(cfg, y, sa_open=209.5, asof="2026-10-13"), cfg, WATCH, port_dir=tmp_path)
    row = out["applied"][0]
    assert row["fill_price"] == 210.0 and "open 210 from yfinance, stockanalysis.com 209.5" in row["reason"]
    assert "PRICE CHECK" not in row["reason"]
    sp.unlink()
    P.place_orders([core_buy("AAPL", conv=4)], sp, YMarket(cfg, None), cfg, WATCH, "2026-10-10", port_dir=tmp_path)
    out = P.fill_pending(sp, YMarket(cfg, y, sa_open=200.0, asof="2026-10-13"), cfg, WATCH, port_dir=tmp_path)
    assert "!! PRICE CHECK: 5.00% apart" in out["applied"][0]["reason"]


def test_yahoo_failure_falls_back_to_stockanalysis(cfg):
    m = YMarket(cfg, YahooPrices(loader=lambda sym, p: (_ for _ in ()).throw(RuntimeError("rate limited"))))
    q = m.quote("AAPL")
    assert q["source"] == "stockanalysis" and m.fallbacks and "rate limited" in m.fallbacks[0]
    bad_ccy = YahooPrices(loader=lambda sym, p: (frame([("2026-10-08", 1.0, 1.0, 1.0, 1.0)]), "EUR"))
    m = YMarket(cfg, bad_ccy)
    assert m.quote("AAPL")["source"] == "stockanalysis" and "expected USD" in m.fallbacks[0]


def test_daily_mark_uses_the_yahoo_close(cfg):
    m = YMarket(cfg, yahoo({"AAPL": [("2026-10-08", 330.0), ("2026-10-09", 335.5)]}), asof="2026-10-10")
    q = m.quote("AAPL")
    assert (q["close"], q["date"], q["source"]) == (335.5, "2026-10-09", "yfinance")



def test_incomplete_latest_bar_falls_back_instead_of_going_stale(cfg):
    import math
    df = frame([("2026-10-07", 81.15, 81.4, 79.1, 80.38), ("2026-10-08", 80.14, 83.0, 79.9, 82.56)])
    df.loc[df.index[-1], "Close"] = math.nan  # what Yahoo served on 2026-10-09 at 01:30 UK
    y = YahooPrices(loader=lambda sym, p: (df, "USD"))
    with pytest.raises(P.DataError, match="incomplete"):
        y.history("AAPL")
    m = YMarket(cfg, y)
    assert m.quote("AAPL")["source"] == "stockanalysis" and "incomplete" in m.fallbacks[0]

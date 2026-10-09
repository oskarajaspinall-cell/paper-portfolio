"""Portfolio prices from Yahoo Finance via yfinance (owner-approved 2026-10-08): the PRIMARY source for
the opening prices that fill orders and the closing prices that re-price the portfolio, with
stockanalysis.com as the automatic fallback. Research, fundamentals, fair value and the screen stay
stockanalysis.com-only. yfinance is an unofficial Yahoo scraper (personal-use terms): any failure,
empty answer or currency mismatch raises DataError so the caller falls back; nothing is ever guessed.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DataError, Ticker  # noqa: E402

SUFFIX = {"LON": ".L", "HKG": ".HK", "SHA": ".SS", "SHE": ".SZ", "TPE": ".TW", "KRX": ".KS", "TYO": ".T",
          "NSE": ".NS", "TSX": ".TO"}
CCY = {"GBp": "GBX", "ZAc": "ZAc", "ILA": "ILA"}  # Yahoo's minor-unit codes -> the codes used here


def yahoo_symbol(ticker: str) -> str | None:
    """stockanalysis.com ticker -> Yahoo symbol; None when the exchange isn't mapped (caller falls back)."""
    t = Ticker(ticker)
    if not t.exchange:
        return t.symbol.replace(".", "-")  # BRK.B -> BRK-B
    sfx = SUFFIX.get(t.exchange)
    if not sfx:
        return None
    sym = t.symbol
    if t.exchange == "HKG" and sym.isdigit():
        sym = sym.zfill(4)
    return sym + sfx


def rows_from_frame(df) -> list[dict]:
    """A yfinance daily frame -> rows shaped like stockanalysis.com history rows (ascending)."""
    out = []
    for idx, r in df.iterrows():
        c = r.get("Close")
        if c is None or c != c:  # NaN: an incomplete row
            continue
        num = lambda k: None if r.get(k) is None or r.get(k) != r.get(k) else float(r.get(k))  # noqa: E731
        out.append({"date": idx.date().isoformat(), "open": num("Open"), "high": num("High"), "low": num("Low"),
                    "close": float(c), "adj_close": num("Adj Close"), "volume": num("Volume")})
    return sorted(out, key=lambda x: x["date"])


class YahooPrices:
    """history(ticker) -> {"url", "rows", "currency"}; raises DataError on anything unusable."""

    def __init__(self, period: str = "6mo", loader=None):
        self.period = period
        self._load = loader or self._yf
        self._cache: dict[str, dict] = {}

    @staticmethod
    def _yf(sym: str, period: str):
        import yfinance as yf
        t = yf.Ticker(sym)
        df = t.history(period=period, interval="1d", auto_adjust=False, actions=False)
        return df, t.fast_info["currency"]

    def history(self, ticker: str) -> dict:
        if ticker in self._cache:
            return self._cache[ticker]
        sym = yahoo_symbol(ticker)
        url = f"https://finance.yahoo.com/quote/{sym}/history" if sym else "https://finance.yahoo.com/"
        if not sym:
            raise DataError(url, "symbol", f"no Yahoo symbol mapping for {ticker}")
        try:
            df, ccy = self._load(sym, self.period)
        except Exception as e:  # noqa: BLE001  network, Yahoo changes, rate limits: fall back
            raise DataError(url, "yfinance", f"{type(e).__name__}: {str(e)[:120]}") from e
        rows = rows_from_frame(df) if df is not None else []
        if not rows:
            raise DataError(url, "yfinance", "no price rows returned")
        if df is not None and len(df) and str(df.index[-1].date()) > rows[-1]["date"]:
            # Yahoo sometimes serves the latest day with a blank close (an unfinished bar): dropping it would
            # silently price the portfolio a day stale, so treat it as a failure and fall back
            raise DataError(url, "yfinance", f"latest daily bar {df.index[-1].date()} is incomplete (no close)")
        self._cache[ticker] = {"url": url, "rows": rows, "currency": CCY.get(ccy, ccy), "symbol": sym}
        return self._cache[ticker]


def live_price(ticker: str, loader=None) -> dict:
    """The latest traded price today from 1-minute bars: {"price", "time" (exchange-local ISO), "date",
    "currency", "url"}. Raises DataError when Yahoo has nothing usable (the caller skips the stock)."""
    sym = yahoo_symbol(ticker)
    url = f"https://finance.yahoo.com/quote/{sym}" if sym else "https://finance.yahoo.com/"
    if not sym:
        raise DataError(url, "symbol", f"no Yahoo symbol mapping for {ticker}")
    try:
        if loader:
            df, ccy = loader(sym)
        else:
            import yfinance as yf
            t = yf.Ticker(sym)
            df, ccy = t.history(period="1d", interval="1m", auto_adjust=False, actions=False), t.fast_info["currency"]
    except Exception as e:  # noqa: BLE001
        raise DataError(url, "yfinance", f"{type(e).__name__}: {str(e)[:120]}") from e
    if df is None or not len(df):
        raise DataError(url, "yfinance", "no intraday bars returned")
    df = df[df["Close"] == df["Close"]]  # drop NaN bars
    if not len(df):
        raise DataError(url, "yfinance", "no intraday bars with a price")
    ts = df.index[-1]
    return {"price": float(df["Close"].iloc[-1]), "time": ts.isoformat(), "date": str(ts.date()),
            "currency": CCY.get(ccy, ccy), "url": url}


def price_at(ticker: str, when, max_age_min: int = 15, loader=None) -> dict:
    """The 1-minute bar at/before `when` (an aware datetime, today or the last few days) as live_price's shape.
    Used to re-price a decision made earlier in the session. Raises DataError if there is no bar within
    `max_age_min` before `when`."""
    sym = yahoo_symbol(ticker)
    url = f"https://finance.yahoo.com/quote/{sym}" if sym else "https://finance.yahoo.com/"
    if not sym:
        raise DataError(url, "symbol", f"no Yahoo symbol mapping for {ticker}")
    try:
        if loader:
            df, ccy = loader(sym)
        else:
            import yfinance as yf
            t = yf.Ticker(sym)
            df, ccy = t.history(period="5d", interval="1m", auto_adjust=False, actions=False), t.fast_info["currency"]
    except Exception as e:  # noqa: BLE001
        raise DataError(url, "yfinance", f"{type(e).__name__}: {str(e)[:120]}") from e
    df = df[(df["Close"] == df["Close"]) & (df.index <= when)] if df is not None and len(df) else df
    if df is None or not len(df):
        raise DataError(url, "yfinance", f"no 1-minute bar at/before {when}")
    ts = df.index[-1]
    if (when - ts).total_seconds() > max_age_min * 60:
        raise DataError(url, "yfinance", f"latest bar {ts} is more than {max_age_min} min before {when}")
    return {"price": float(df["Close"].iloc[-1]), "time": ts.isoformat(), "date": str(ts.date()),
            "currency": CCY.get(ccy, ccy), "url": url}

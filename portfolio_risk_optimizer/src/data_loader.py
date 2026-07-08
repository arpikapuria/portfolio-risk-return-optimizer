"""Data loading utilities for the portfolio optimizer."""

from __future__ import annotations

import pandas as pd
import yfinance as yf


def load_adjusted_close(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    """Download adjusted close prices from Yahoo Finance.

    Parameters
    ----------
    tickers:
        List of stock tickers.
    start:
        Start date in YYYY-MM-DD format.
    end:
        End date in YYYY-MM-DD format.

    Returns
    -------
    pd.DataFrame
        Adjusted close prices indexed by date.
    """
    data = yf.download(tickers, start=start, end=end, auto_adjust=False, progress=False)

    if isinstance(data.columns, pd.MultiIndex):
        prices = data["Adj Close"].copy()
    else:
        prices = data[["Adj Close"]].rename(columns={"Adj Close": tickers[0]})

    prices = prices.dropna(how="all").ffill().dropna()
    return prices


def calculate_daily_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Calculate daily percentage returns from price data."""
    return prices.pct_change().dropna()

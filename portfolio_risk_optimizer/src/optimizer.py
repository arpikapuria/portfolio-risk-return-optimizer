"""Monte Carlo portfolio optimizer."""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.metrics import portfolio_return, portfolio_volatility, sharpe_ratio


def random_weights(n_assets: int) -> np.ndarray:
    """Generate random weights that sum to one."""
    weights = np.random.random(n_assets)
    return weights / weights.sum()


def simulate_portfolios(
    mean_returns: pd.Series,
    covariance_matrix: pd.DataFrame,
    n_portfolios: int = 20000,
    risk_free_rate: float = 0.02,
    seed: int = 42,
) -> pd.DataFrame:
    """Simulate random long-only portfolios.

    Returns a DataFrame with return, volatility, Sharpe ratio, and asset weights.
    """
    np.random.seed(seed)
    tickers = list(mean_returns.index)
    rows = []

    for _ in range(n_portfolios):
        weights = random_weights(len(tickers))
        ret = portfolio_return(weights, mean_returns)
        vol = portfolio_volatility(weights, covariance_matrix)
        sr = sharpe_ratio(ret, vol, risk_free_rate)

        row = {
            "return": ret,
            "volatility": vol,
            "sharpe_ratio": sr,
        }
        for ticker, weight in zip(tickers, weights):
            row[f"weight_{ticker}"] = weight
        rows.append(row)

    return pd.DataFrame(rows)


def best_portfolios(results: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Return max Sharpe and min volatility portfolios."""
    max_sharpe = results.loc[results["sharpe_ratio"].idxmax()]
    min_vol = results.loc[results["volatility"].idxmin()]
    return max_sharpe, min_vol

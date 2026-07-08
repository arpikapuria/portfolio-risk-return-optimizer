"""Portfolio risk and return metrics."""

from __future__ import annotations

import numpy as np
import pandas as pd

TRADING_DAYS = 252


def annualized_returns(daily_returns: pd.DataFrame) -> pd.Series:
    """Calculate annualized mean returns."""
    return daily_returns.mean() * TRADING_DAYS


def annualized_covariance(daily_returns: pd.DataFrame) -> pd.DataFrame:
    """Calculate annualized covariance matrix."""
    return daily_returns.cov() * TRADING_DAYS


def portfolio_return(weights: np.ndarray, mean_returns: pd.Series) -> float:
    """Calculate expected annual portfolio return."""
    return float(np.dot(weights, mean_returns))


def portfolio_volatility(weights: np.ndarray, covariance_matrix: pd.DataFrame) -> float:
    """Calculate annual portfolio volatility."""
    return float(np.sqrt(weights.T @ covariance_matrix.values @ weights))


def sharpe_ratio(port_return: float, port_volatility: float, risk_free_rate: float = 0.02) -> float:
    """Calculate Sharpe ratio."""
    if port_volatility == 0:
        return 0.0
    return (port_return - risk_free_rate) / port_volatility

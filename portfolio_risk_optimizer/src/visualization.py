"""Visualization functions for portfolio optimization."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def plot_efficient_frontier(results: pd.DataFrame, output_path: str) -> None:
    """Plot simulated portfolios by volatility and return."""
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        results["volatility"],
        results["return"],
        c=results["sharpe_ratio"],
        s=8,
        alpha=0.7,
    )
    plt.colorbar(scatter, label="Sharpe Ratio")
    plt.xlabel("Annualized Volatility")
    plt.ylabel("Annualized Return")
    plt.title("Simulated Portfolio Efficient Frontier")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def plot_weight_allocation(portfolio: pd.Series, output_path: str, title: str) -> None:
    """Plot asset weights for a selected portfolio."""
    weights = portfolio.filter(like="weight_").copy()
    weights.index = [name.replace("weight_", "") for name in weights.index]

    plt.figure(figsize=(8, 5))
    weights.sort_values().plot(kind="barh")
    plt.xlabel("Portfolio Weight")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()

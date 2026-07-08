"""Run the portfolio risk and return optimizer."""

from __future__ import annotations

import os

from src.data_loader import calculate_daily_returns, load_adjusted_close
from src.metrics import annualized_covariance, annualized_returns
from src.optimizer import best_portfolios, simulate_portfolios
from src.visualization import plot_efficient_frontier, plot_weight_allocation


def main() -> None:
    os.makedirs("outputs", exist_ok=True)

    tickers = ["AAPL", "MSFT", "JPM", "XOM", "UNH", "NVDA"]
    start_date = "2018-01-01"
    end_date = "2024-12-31"
    risk_free_rate = 0.02

    print("Downloading price data...")
    prices = load_adjusted_close(tickers, start=start_date, end=end_date)
    returns = calculate_daily_returns(prices)

    mean_returns = annualized_returns(returns)
    covariance_matrix = annualized_covariance(returns)

    print("Simulating portfolios...")
    results = simulate_portfolios(
        mean_returns=mean_returns,
        covariance_matrix=covariance_matrix,
        n_portfolios=20000,
        risk_free_rate=risk_free_rate,
    )

    max_sharpe, min_vol = best_portfolios(results)

    results.to_csv("outputs/simulated_portfolios.csv", index=False)
    mean_returns.to_csv("outputs/annualized_returns.csv")
    covariance_matrix.to_csv("outputs/annualized_covariance_matrix.csv")

    plot_efficient_frontier(results, "outputs/efficient_frontier.png")
    plot_weight_allocation(max_sharpe, "outputs/max_sharpe_weights.png", "Maximum Sharpe Portfolio Weights")
    plot_weight_allocation(min_vol, "outputs/min_volatility_weights.png", "Minimum Volatility Portfolio Weights")

    print("\nMaximum Sharpe Portfolio")
    print(max_sharpe.round(4))

    print("\nMinimum Volatility Portfolio")
    print(min_vol.round(4))

    print("\nFiles saved to the outputs/ folder.")


if __name__ == "__main__":
    main()

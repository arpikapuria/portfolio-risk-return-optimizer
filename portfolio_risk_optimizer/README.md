# Portfolio Risk & Return Optimizer

## Overview

This project builds a finance-focused portfolio analysis tool in Python. It downloads historical stock price data, calculates returns and risk metrics, simulates thousands of random portfolios, and identifies portfolios with the highest Sharpe ratio and lowest volatility.

The goal is to connect quantitative finance concepts with real Python code, including expected return, volatility, covariance matrices, diversification, Sharpe ratio, and portfolio optimization.

## Project Goals

- Download historical stock data using `yfinance`
- Calculate daily returns and annualized performance metrics
- Build a covariance matrix for portfolio risk analysis
- Simulate random portfolio allocations
- Identify the maximum Sharpe ratio portfolio
- Identify the minimum volatility portfolio
- Plot the efficient frontier
- Export portfolio results to CSV

## Finance Concepts Used

### Expected Portfolio Return

The expected return of a portfolio is calculated as the weighted average of each asset's expected return.

### Portfolio Volatility

Portfolio risk is calculated using the covariance matrix of asset returns.

### Sharpe Ratio

The Sharpe ratio measures risk-adjusted return:

```text
Sharpe Ratio = (Portfolio Return - Risk-Free Rate) / Portfolio Volatility
```

A higher Sharpe ratio means the portfolio is earning more return per unit of risk.

## Tools and Libraries

- Python
- pandas
- NumPy
- matplotlib
- yfinance

## Skills Demonstrated

- Quantitative finance
- Portfolio optimization
- Risk and return analysis
- Monte Carlo simulation
- Covariance matrix analysis
- Financial data visualization
- Python project organization

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python run_optimizer.py
```

The script will save portfolio metrics and plots inside the `outputs/` folder.

## Project Structure

```text
portfolio-risk-return-optimizer/
│
├── run_optimizer.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── data_loader.py
│   ├── metrics.py
│   ├── optimizer.py
│   └── visualization.py
└── outputs/
```

## Example Tickers

The default portfolio uses:

```text
AAPL, MSFT, JPM, XOM, UNH, NVDA
```

You can change the ticker list inside `run_optimizer.py`.

## Key Takeaway

This project shows how quantitative methods can be used to evaluate portfolio risk and return. It demonstrates how diversification, covariance, and asset weighting affect portfolio performance.

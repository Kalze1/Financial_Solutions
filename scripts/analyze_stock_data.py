import pandas as pd
import matplotlib.pyplot as plt
import pynance as pn
import numpy as np

def analyze_stock_data(df):
    """
    Analyzes stock data, calculates daily returns, cumulative returns, and volatility,
    then plots the results.

    Parameters:
    df (pd.DataFrame): DataFrame containing stock data with a 'Close' price column and 'Date' column.

    Returns:
    pd.DataFrame: A DataFrame containing the stock data with additional calculated columns.
    """
    # Ensure the 'Date' column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Set 'Date' as the index
    df.set_index('Date', inplace=True)

    # Calculate daily returns
    df['Daily_Return'] = df['Close'].pct_change()

    # Calculate cumulative returns using PyNance
    df['Cumulative_Return'] = pn.ind.cumret(df['Daily_Return'])

    # Calculate volatility (annualized) using PyNance
    df['Volatility'] = pn.ind.volatility(df['Close'])

    # Plot the stock price
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'])
    plt.title('Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

    # Plot cumulative returns
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Cumulative_Return'])
    plt.title('Cumulative Returns')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.show()

    # Plot volatility
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Volatility'])
    plt.title('Volatility (Annualized)')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.show()

    return df


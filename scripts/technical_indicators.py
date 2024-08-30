import pandas as pd
import matplotlib.pyplot as plt
import talib

def calculate_moving_averages(df, period_short=20, period_long=50):
    """
    Calculates short-term and long-term simple moving averages (SMA).
    
    Args:
    df (pd.DataFrame): The DataFrame containing stock data with 'Close' prices.
    period_short (int): The time period for the short-term SMA (default is 20).
    period_long (int): The time period for the long-term SMA (default is 50).
    
    Returns:
    pd.DataFrame: DataFrame with added SMA columns.
    """
    df[f'SMA{period_short}'] = talib.SMA(df['Close'], timeperiod=period_short)
    df[f'SMA{period_long}'] = talib.SMA(df['Close'], timeperiod=period_long)
    return df

def calculate_rsi(df, period=14):
    """
    Calculates the Relative Strength Index (RSI).
    
    Args:
    df (pd.DataFrame): The DataFrame containing stock data with 'Close' prices.
    period (int): The time period for calculating RSI (default is 14).
    
    Returns:
    pd.DataFrame: DataFrame with added RSI column.
    """
    df['RSI'] = talib.RSI(df['Close'], timeperiod=period)
    return df

def calculate_macd(df, fastperiod=12, slowperiod=26, signalperiod=9):
    """
    Calculates the Moving Average Convergence Divergence (MACD).
    
    Args:
    df (pd.DataFrame): The DataFrame containing stock data with 'Close' prices.
    fastperiod (int): The short-term EMA period (default is 12).
    slowperiod (int): The long-term EMA period (default is 26).
    signalperiod (int): The signal line EMA period (default is 9).
    
    Returns:
    pd.DataFrame: DataFrame with added MACD, MACD signal, and MACD histogram columns.
    """
    df['MACD'], df['MACDsignal'], df['MACDhist'] = talib.MACD(df['Close'], 
                                                               fastperiod=fastperiod, 
                                                               slowperiod=slowperiod, 
                                                               signalperiod=signalperiod)
    return df

def plot_technical_indicators(df):
    """
    Plots the calculated technical indicators (Moving Averages, RSI, MACD) on the stock data.
    
    Args:
    df (pd.DataFrame): The DataFrame containing stock data and calculated indicators.
    """
    # Plot Moving Averages
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close')
    plt.plot(df['SMA20'], label='SMA20')
    plt.plot(df['SMA50'], label='SMA50')
    plt.legend()
    plt.title('Stock Price with Moving Averages')
    plt.show()

    # Plot RSI
    plt.figure(figsize=(12, 6))
    plt.plot(df['RSI'], label='RSI')
    plt.axhline(70, color='r', linestyle='--', label='Overbought')
    plt.axhline(30, color='r', linestyle='--', label='Oversold')
    plt.title('RSI')
    plt.legend()
    plt.show()

    # Plot MACD
    plt.figure(figsize=(12, 6))
    plt.plot(df['MACD'], label='MACD')
    plt.plot(df['MACDsignal'], label='Signal')
    plt.bar(df.index, df['MACDhist'], alpha=0.5)
    plt.legend()
    plt.title('MACD')
    plt.show()


import numpy as np
import pandas as pd
import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plt

# Fetch historical stock data (e.g., Apple)
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2024-02-01')

# Define a function to generate buy and sell signals
def buy_sell(df):
    # Calculate moving averages
    df['SMA_10'] = ta.sma(df['Adj Close'], length=10)
    df['SMA_30'] = ta.sma(df['Adj Close'], length=30)

    # Generate buy signals
    df['Buy_Signal'] = np.where(df['SMA_10'] > df['SMA_30'], 1, 0)

    # Generate sell signals
    df['Sell_Signal'] = np.where(df['SMA_10'] < df['SMA_30'], -1, 0)

    return df

# Apply the function to your data
data = buy_sell(data)

# Plot the buy and sell signals
plt.figure(figsize=(12, 12))
plt.plot(data.index, data['Adj Close'], label='Adjusted Close Price', alpha=0.5)
plt.scatter(data.index, data['Adj Close'][data['Buy_Signal'] == 1], color='green', marker='^', label='Buy Signal')
plt.scatter(data.index, data['Adj Close'][data['Sell_Signal'] == 1], color='red', marker='v', label='Sell Signal')
plt.title(f'{ticker} Buy/Sell Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

import yfinance as yf
import mplfinance as mpf
import numpy as np

# Fetch historical Bitcoin data
df = yf.download('BTC-USD', start='2021-01-01', end='2024-02-01', interval='1d')

# Generate buy signals (example: based on candlestick patterns)
buy = np.where((df['Close'] > df['Open']) & (df['Close'].shift(1) < df['Open'].shift(1)), 1, np.nan) * 0.95 * df['Low']

# Create an addplot for buy signals
apd = [mpf.make_addplot(buy, scatter=True, markersize=100, marker=r'$\uparrow$', color='green')]

# Plot candlestick chart with buy signals
mpf.plot(df, type='candle', volume=True, addplot=apd)
